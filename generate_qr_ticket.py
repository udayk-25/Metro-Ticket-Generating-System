#!/usr/bin/env python3
"""Generate a demo metro ticket QR code. Prototype only; not a valid transit ticket."""
import argparse, json, uuid
from datetime import date
from pathlib import Path
import qrcode

def main():
    parser = argparse.ArgumentParser(description="Generate a demo QR code for a metro ticket.")
    parser.add_argument("--origin", default="Central")
    parser.add_argument("--destination", default="Museum")
    parser.add_argument("--travel-date", default=date.today().isoformat())
    parser.add_argument("--passengers", type=int, default=1)
    parser.add_argument("--fare", type=float, default=15.0)
    parser.add_argument("--ticket-id", default=None)
    parser.add_argument("--output", default="metro_demo_ticket_qr.png")
    args = parser.parse_args()
    if args.origin.strip().lower() == args.destination.strip().lower():
        parser.error("Origin and destination must differ.")
    if args.passengers < 1 or args.passengers > 10:
        parser.error("Passengers must be between 1 and 10.")
    ticket_id = args.ticket_id or ("DEMO-" + uuid.uuid4().hex[:12].upper())
    payload = {
        "type": "METRO_DEMO_TICKET",
        "ticket_id": ticket_id,
        "origin": args.origin,
        "destination": args.destination,
        "travel_date": args.travel_date,
        "passengers": args.passengers,
        "fare_inr": round(args.fare, 2),
        "note": "DEMO ONLY — verify with the issuing system; QR alone is not proof of validity"
    }
    img = qrcode.make(json.dumps(payload, separators=(",", ":")))
    img.save(args.output)
    print("QR image:", Path(args.output).resolve())
    print("Demo ticket ID:", ticket_id)
    print(json.dumps(payload, indent=2))
if __name__ == "__main__":
    main()
