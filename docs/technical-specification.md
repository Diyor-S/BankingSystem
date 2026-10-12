# SmartBank – Technical Specification (GOST 34.602 structure)

Markdown copy of Section 5.3 of the report. Requirement IDs (FR-xx, NFR-xx) refer to Section 5.1 of the report.

## 5.3. Technical Specification (TS)

The TS below follows the structure of GOST 34.602 and refers to the identifiers of Section 5.1. It is a short working version for the MVP; it is updated at the end of each Sprint.

## *1. General information*

**TS section 1 – general information**

| **Item**              | **Value**                                                                                                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System name           | SmartBank – digital banking system (code SB-2026)                                                                                                                          |
| Client                | SmartBank JSC (hypothetical), pilot with 2,000 selected customers                                                                                                          |
| Developer             | Diyorxo'ja Saidaliyev, group 319-24 (individual project)                                                                                                                   |
| Deadlines             | Start: week 1. Sprint 1 result: end of week 4. Complete MVP: end of week 10. System, security and acceptance testing: weeks 11–12. Pilot launch and handover: weeks 13–14. |
| Basis for development | Project charter (Table 4), Product Backlog (Table 12), requirements FR-01…FR-13 and NFR-01…NFR-08.                                                                         |

## *2. Purpose of the system and objectives of its development*

**Purpose:** to let a person become a bank customer and make safe card-to-card transfers online, using only a passport ID, a phone number and OTP codes, and to give the bank an admin tool for monitoring. **Objectives:** (1) registration in ≤ 2 minutes; (2) at least 70 % of the pilot customers’ transfers made digitally; (3) zero balance discrepancies; (4) transfer time ≤ 3 s; (5) full audit of admin actions. Success is measured by the criteria of the charter (Table 4).

## *3. Description of the object of automation*

**Environment.** A commercial bank serves customers through branches. A customer has a passport, a phone number and one or more bank cards; each card is attached to a phone number. In the real world the passport data are stored in the national citizen registry and the card data in the bank’s card-processing system. In this project these systems are **imitated by mock services** with seeded test data (Table 20). Admins use desktop computers; customers use smartphones.

**Existing problems:** (a) onboarding and simple transfers require a branch visit; (b) there is no instant check of the person by passport and phone; (c) customers are not told about operations immediately; (d) the bank has no simple tool to monitor users and transactions. Existing digital services (see Table 7) are widely used, but a bank that does not control its own reliable channel depends on third parties.

**Mock external services and test data**

| **Mock service**  | **What it imitates**                                                                     | **Data and behaviour**                                                                                                                                                                                                                                                                                                                                              |
|-------------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Passport Registry | National citizen / passport database; in reality also read with a camera (out of scope). | Table passports: passport_id (2 letters + 7 digits), full_name, birth_date, phone. 30 fictional citizens. API: GET /registry/passports/{id} returns the record or 404.                                                                                                                                                                                              |
| Card Registry     | Card-processing system of the bank.                                                      | Table cards: card_number (16 digits), attached_phone, holder_name, balance (UZS), status (active / blocked), customer_id (empty until the card is linked). 40 cards; some have a phone that differs from the owner’s passport phone, some are blocked, and 10 are already linked to 5 seeded test customers, to test all rejection cases. API: GET /cards/{number}. |
| SMS gateway       | Telecom operator’s SMS service.                                                          | POST /sms stores the message (phone, text, time) in a table and shows it in a developer inbox page; delivery can be switched off to test failures. OTP codes are read from this inbox during demos.                                                                                                                                                                 |

## *4. System requirements*

**4.1 Functional requirements:** FR-01…FR-13 of Table 15. **4.2 Non-functional requirements:** NFR-01…NFR-08 of Table 16. Further requirements:

**TS section 4 – hardware, software, interface and security requirements**

| **Group**         | **Requirement**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Linked to**               |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Hardware (server) | Pilot: one application and database server with 4 vCPU, 8 GB RAM, 100 GB SSD, located in Uzbekistan; staging server with 2 vCPU, 4 GB RAM. Daily backups to a second location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | NFR-02, NFR-05              |
| Hardware (client) | Customers: any smartphone with 2 GB RAM and a modern browser. Admins: PC or laptop, screen ≥ 1280 px.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | NFR-07                      |
| Software          | Ubuntu LTS, Docker; Python 3.12 + FastAPI; PostgreSQL 16; Redis; React + TypeScript; Nginx; GitHub Actions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | NFR-05                      |
| Interface         | Responsive web interface from 360 px; touch targets ≥ 44 px; font ≥ 16 px; text contrast ≥ 4.5:1; a transfer takes ≤ 5 steps; amounts always shown with currency; card numbers masked; every irreversible action has a confirmation screen. (Uzbek / Russian / English interface is a later release.)                                                                                                                                                                                                                                                                                                                                                | NFR-04, NFR-07              |
| Security          | Roles: customer, admin (admins are created by the seed script); access by role only; OTP stored as a hash with expiry and attempt limit; rate limiting of OTP requests; HTTPS (TLS ≥ 1.2); encryption of passport ID and card number at rest; masking in the interface and logs; audit log of admin actions and personal-data views; consent of the customer to personal-data processing recorded at registration; data stored on servers in Uzbekistan; a threat model (STRIDE) and an OWASP ASVS checklist. A real launch would also require integration with the real registries and legal review (Central Bank rules, AML/KYC, Law No. ZRU-547). | FR-03, FR-07, FR-11, NFR-03 |
| Integration       | The Passport Registry, Card Registry and SMS gateway are accessed through replaceable adapters (interfaces); mocks are used in this project and real services can be connected later without changing the business logic. The API is documented in OpenAPI.                                                                                                                                                                                                                                                                                                                                                                                          | FR-01, FR-04, FR-10         |

## *5. Scope and stages of work*

**TS section 5 – stages of work aligned with Sprints**

| **Stage / Sprint**     | **Weeks** | **Content (User Stories, tasks)**                                                                                                                | **Result**                                                       |
|------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Initiation             | 1–2       | Charter, analysis, backlog, requirements, TS, kick-off page (this assignment)                                                                    | Approved documents                                               |
| Sprint 1               | 3–4       | US-01 core (transfer without OTP) and the minimal card list of US-05; mock Card Registry; tasks T-02, T-04, T-05                                 | Working card-to-card transfer with atomic update and idempotency |
| Sprint 2               | 5–6       | US-01 OTP step (T-06), US-02 registration, US-03 login, US-04 card linking; mock Passport Registry and SMS gateway; tasks T-01, T-03, T-07, T-08 | Full flow: register → login → link card → transfer               |
| Sprint 3               | 7–8       | US-05 complete, US-06 history, US-07 notifications, US-08 admin monitoring                                                                       | Customer features and admin view complete                        |
| Sprint 4               | 9–10      | US-09 freeze / unfreeze, US-10 unlink card; defect fixing, security hardening and performance tuning                                             | Complete MVP                                                     |
| Testing and acceptance | 11–12     | System, load, security and concurrency testing; UAT with test customers and an admin                                                             | Test report, acceptance protocol                                 |
| Pilot and handover     | 13–14     | Deployment for the pilot group, admin guide, KPI measurement                                                                                     | System in operation, acceptance act                              |

Estimates are initial and will be recalibrated after Sprint 1, when the real velocity is known.

## *6. Testing and acceptance procedure*

- **Levels:** unit tests (pytest, Jest); API tests; UI tests (Playwright); manual test cases for every User Story (including all rejection cases of the passport–phone–card check); concurrency tests (50 and 1,000 parallel transfers); load test (Locust, 200 users); security scan (OWASP ZAP) and review against the threat model.

- **Every Sprint:** the Definition of Done (Section 4.5) is checked and a demo is given to the Product Owner and the client’s representative.

- **Acceptance:** the system is accepted when (a) all “Must” User Stories pass their acceptance criteria; (b) all NFR metrics are measured and met; (c) there are no open Critical or High defects and no High/Critical security findings; (d) UAT with at least 10 test customers and 1 admin gives SUS ≥ 75.

- **Procedure:** a test report is prepared; the client signs the acceptance act; open Medium and Low defects are written into the backlog.

## *7. Documentation requirements*

The deliverables are: this TS; the Product Backlog and Trello archive; UML diagrams (use case, ER, architecture); OpenAPI description of the REST API and of the mock services; README with installation, seed data and deployment instructions; user guide for customers; admin guide; threat model and security checklist; test plan and test report; list of risks and decisions.

## *8. Development sources*

GOST 34.602-2020 (technical specification for automated systems); ISO/IEC/IEEE 29148:2018 (requirements engineering); ISO/IEC 25010 (product quality model); the Scrum Guide 2020; OWASP ASVS (security requirements); Law of the Republic of Uzbekistan No. ZRU-547 “On Personal Data”; the project charter and the results of interviews with customers and bank staff; the competitor analysis of Section 2.3. The full list is in the References.

