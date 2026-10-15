# Metro Ticket Generating System — Updated Project Package

Updated: 15 October 2026  
Platform concept: ServiceNow Service Catalog + Flow Designer

## What changed after reviewing the additional phase archives
The uploaded Project Design, Project Planning, and Project Development archives were reviewed. Most files are generic templates or examples; some are for unrelated platforms (Tableau, Power BI, Salesforce, ML, AI, and GenAI). This package includes project-specific adapted documents for the metro-ticketing workflow rather than copying unrelated metrics or example stories.

## Main deliverables
- `Metro_Ticket_Generating_System_Project_Report.docx` — consolidated report with updated source review, design, planning, testing, and production-readiness sections.
- `Metro_Ticket_Generating_System_Project_Report.pdf` — PDF summary report.
- `Metro_Ticket_Generating_System_Presentation.pptx` — original deck extended with design, sprint planning, testing, and UAT slides.
- `design_phase/Metro_Ticketing_Project_Design.docx` — problem–solution fit, proposed solution, and architecture.
- `planning_phase/Metro_Ticketing_Project_Planning.docx` — project-specific backlog, story points, sprint plan, and Definition of Done.
- `development_testing/Metro_Ticketing_Development_Testing_UAT.docx` — functional cases, performance/reliability plan, UAT, defect log, and sign-off template.
- `development_testing/functional_test_cases.csv` and `performance_test_plan.csv` — editable test logs.
- `ServiceNow_Setup_Guide.md` — implementation notes.
- `generate_qr_ticket.py` and `assets/demo_metro_ticket_qr.png` — local demonstration only.
- `source_templates/` — the three uploaded source ZIP archives, retained unchanged for traceability.

## Important limits
- The sample fare (INR 10 base + INR 5 per station interval) is illustrative, not an official fare.
- No live metro operator, payment gateway, station database, or gate validator is connected.
- QR code images alone do not prove ticket validity. A trusted server-side verification service is required.
- Tests are marked **Not executed / Pending**. Run them in your own ServiceNow sub-production instance and fill in actual results. No test pass rate, accuracy, performance result, or velocity is claimed.
- The included ServiceNow scripts, if present, are illustrative and require adaptation to your actual instance and table/variable names.

## Recommended next steps
1. Confirm actual ServiceNow table names, catalog variables, roles, and instance version.
2. Replace demo station/fare assumptions with approved configuration.
3. Configure server-side validation, ACLs, Flow Designer, notifications, and secure ticket verification.
4. Execute functional, security, performance, accessibility, and UAT cases; record evidence and sign-off.
