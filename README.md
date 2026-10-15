# Metro Ticket Booking System using ServiceNow

This package was prepared from the two uploaded archives:
- `1. Ideation Phase` (empathy map, brainstorming/prioritization, problem statement templates)
- `2. Requirement Analysis` (solution requirements, technology stack, data-flow/user-story templates)

The five Drive folder links were not all uploaded as files. This package therefore uses the two ZIP archives available in this chat and the project description supplied by the user. Upload the remaining phase folders if you want those templates filled as well.

## Deliverables
- `Metro_Ticket_Booking_Project_Report.docx` — editable report
- `Metro_Ticket_Booking_Project_Report.pdf` — PDF report
- `Metro_Ticket_Booking_Presentation.pptx` — presentation
- `ServiceNow_Setup_Guide.md` — implementation/configuration guide
- `servicenow_scripts/` — starter ServiceNow scripts
- `generate_qr_ticket.py` — local demo QR generator
- `assets/demo_metro_ticket_qr.png` — sample QR image
- `requirements.txt` — Python dependency for QR generator

## Quick start: QR generator
Install Python 3.9+ and the dependency:
```bash
python -m pip install -r requirements.txt
```
Generate a demo ticket QR:
```bash
python generate_qr_ticket.py --origin Central --destination Museum --travel-date 2026-10-15 --passengers 1 --fare 15 --output demo_ticket.png
```
The generated QR encodes a demo payload. It is not a valid metro ticket.

## ServiceNow implementation
Follow `ServiceNow_Setup_Guide.md`. Script files are starting examples and need adaptation to your scoped app/table names, ACLs, fare rules, and notification design. Test in a non-production instance.

## Fare assumptions
Demo fare: INR 10 base + INR 5 per station interval, multiplied by passenger count. This is only an example and must be replaced with approved operator fare rules.

## Security warning
Do not embed personal or payment information in the QR code. QR content must be verified against a trusted server-side ticket record. A production system needs ticket status/expiry checks and replay prevention.

## Current source coverage
Only the Ideation Phase and Requirement Analysis ZIPs were attached in this conversation. The other three Drive folder archives are not present in this package.
