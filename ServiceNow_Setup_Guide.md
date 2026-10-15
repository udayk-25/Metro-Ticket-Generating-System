# ServiceNow Setup Guide — Metro Ticket Booking

## Important
These scripts are starter examples, not a deployable update set. Test in a non-production instance and adjust scoped table names, fields, access controls, and fare policy. Do not issue real tickets until the metro operator approves fare and validation rules.

## 1. Create tables
Create `x_metro_station` with station_code (string, unique), station_name (string), line (string), sequence (integer), active (true/false).
Create `x_metro_booking` with number (auto-number), requested_for (reference sys_user), origin_station (reference/string), destination_station (reference/string), travel_date (date), passenger_count (integer), fare_amount (currency/decimal), ticket_status (choice), ticket_id (unique string), qr_payload (string), notification_status (choice).
Optional: create `x_metro_fare_rule` for base_fare, per_station_fare, minimum_fare, effective dates, and active status.

## 2. Configure Service Catalog
Create a catalog item named `Book a Metro Ticket`. Add required variables: origin_station, destination_station, travel_date, passenger_count. Prefer reference variables backed by active station records. Add UI policies for usability and use the provided client script only as a convenience check.

## 3. Add server-side fare logic
Create a Script Include named `MetroFareService` in the appropriate application scope. If called from another scope, configure cross-scope access deliberately. Replace sample fares with the approved fare rules and validate all inputs on the server.

## 4. Flow Designer
Trigger: Service Catalog → Requested Item created.
Suggested actions:
1. Read catalog variables.
2. Resolve station records and ensure both are active and distinct.
3. Validate travel date and passenger count.
4. Call server-side fare calculation.
5. Create booking/ticket record with a generated unique ticket ID.
6. Set QR payload to an opaque ticket ID (not personal data).
7. Update request/booking status.
8. Send notification using a notification record or Send Email action.
9. On failure, log a safe error and route to a support queue; avoid duplicate tickets on retries.

## 5. Notifications
Create a notification for the booking record, triggered when ticket_status becomes Confirmed. Include ticket number, origin, destination, travel date, passenger count, and fare. Avoid exposing unnecessary personal data. Link to an authenticated ticket view if one exists.

## 6. QR generation and verification
The included local Python generator creates a QR PNG for demo payloads. In ServiceNow, either render a QR image through an approved internal service or display a QR generated in a trusted client view. QR payload should contain an opaque ticket ID or signed verification URL. A scanner must verify the ticket against a trusted server-side record, enforce date/status/reuse policy, and never trust QR contents alone.

## 7. Security and ACLs
- Apply least-privilege ACLs to booking, station, and fare tables.
- Recompute fare on the server; never trust a client-submitted total.
- Restrict fare-rule changes to authorized admins.
- Validate and normalize all inputs.
- Keep credentials in platform credential storage.
- Audit state changes and protect logs from sensitive data.
- Test authorization failures and ticket replay.

## 8. Test cases
- Valid booking; same origin/destination; invalid/inactive station; past date; passenger count outside 1–10.
- Fare arithmetic at minimum fare and across multiple intervals.
- Notification failure and flow retry; duplicate flow trigger.
- QR references unknown, cancelled, expired, already-used, and confirmed tickets.
- Keyboard-only navigation and screen-reader labels.
