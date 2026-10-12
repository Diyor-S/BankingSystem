# SmartBank – Product Backlog, task cards and Sprint 1 plan

Text copy of the Trello board content (Tasks 4.3–4.5 of the report). Figures are in the report and in `diagrams/`.

## 4.3. Product Backlog and Trello board

The Trello board “SmartBank SB-2026” has five columns: Backlog → To Do → In Progress → Testing → Done. Figure 2 shows its state at Sprint 1 planning on Day 1: all user stories and the 8 task cards of Section 4.4 are in Backlog; the three Sprint 1 tasks and the key User Story US-01 are in To Do. Labels: orange – User Story, purple – Design, blue – Dev, green – QA. The public link is in the link list. **Before submission, replace Figure 2 with a real screenshot of the team’s Trello board** (the picture here shows the intended structure).

<img src="media/cc7852ed37f4b710843b32191103c66b5d66e133.png" title="figure" style="width:6.25in;height:4.625in" alt="diagram" />

*Figure 2 – Trello board “SmartBank SB-2026” at Sprint 1 planning*

Table 12 lists the Product Backlog. Priorities follow MoSCoW, estimates use the Fibonacci Story Point scale (1, 2, 3, 5, 8, 13).

**Product Backlog: User Stories with acceptance criteria**

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 27%" />
<col style="width: 41%" />
<col style="width: 10%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>User Story</strong></th>
<th><strong>Acceptance criteria</strong></th>
<th><strong>Priority</strong></th>
<th><strong>Story Point</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>US-01</td>
<td>As a customer, I want to transfer money from my linked card to another card by its number, because I do not want to visit a branch or carry cash.</td>
<td><p>1) The transfer is rejected with “insufficient funds” (HTTP 422) if balance &lt; amount.</p>
<p>2) A recipient card that does not exist or is blocked is rejected (HTTP 404).</p>
<p>3) Debit and credit are written in one atomic transaction; there is never a partial transfer.</p>
<p>4) The transfer is executed only after the correct OTP is entered.</p>
<p>5) A repeated request with the same idempotency key does not create a second transfer.</p>
<p>6) A receipt with a reference number is shown in ≤ 3 s.</p></td>
<td>Must</td>
<td>8</td>
</tr>
<tr class="even">
<td>US-02</td>
<td>As a new customer, I want to register by entering only my passport ID, because I do not want to fill in forms or visit a branch.</td>
<td>The passport ID is found in the Passport Registry (mock); the full name and phone are taken from it; an OTP is sent to that phone; after the correct code the account is created; one account per passport; unknown passport ID is rejected.</td>
<td>Must</td>
<td>5</td>
</tr>
<tr class="odd">
<td>US-03</td>
<td>As a customer, I want to log in with my phone number and an OTP, because I do not want to remember a password.</td>
<td>6-digit code valid 3 minutes; maximum 3 attempts, then a 15-minute pause; session ends after 5 minutes of inactivity.</td>
<td>Must</td>
<td>3</td>
</tr>
<tr class="even">
<td>US-04</td>
<td>As a customer, I want to link my bank card to my profile, because I need a source of money for transfers.</td>
<td>The card exists and is active in the Card Registry (mock); the phone attached to the card is equal to my phone from the passport; the card is not linked to another customer; an OTP confirms the linking; otherwise the reason is shown.</td>
<td>Must</td>
<td>5</td>
</tr>
<tr class="odd">
<td>US-05</td>
<td>As a customer, I want to see my linked cards and balances, because I need to know how much money I have.</td>
<td>List of cards with masked numbers (last 4 digits) and balances in UZS opens in ≤ 2 s; balance equals the card registry value.</td>
<td>Must</td>
<td>3</td>
</tr>
<tr class="even">
<td>US-06</td>
<td>As a customer, I want to see my transaction history, because I want to check my past transfers.</td>
<td>List of the last 12 months, newest first, with date, amount, counterpart (masked) and status; filter by date; opens in ≤ 2 s.</td>
<td>Should</td>
<td>3</td>
</tr>
<tr class="odd">
<td>US-07</td>
<td>As a customer, I want to receive an SMS for every transaction, because I want to notice unauthorised operations quickly.</td>
<td>SMS to the sender and the recipient ≤ 10 s after the transaction; text has amount and masked card; exactly one SMS per participant.</td>
<td>Must</td>
<td>3</td>
</tr>
<tr class="even">
<td>US-08</td>
<td>As an admin, I want to view all users, their cards and transactions, because I must monitor the system.</td>
<td>Lists with search by passport ID, phone or card; each user page shows linked cards and transactions; every view of personal data is written to the audit log; customers cannot open admin pages.</td>
<td>Must</td>
<td>5</td>
</tr>
<tr class="odd">
<td>US-09</td>
<td>As an admin, I want to freeze and unfreeze a customer’s account, because suspicious accounts must be stopped quickly.</td>
<td>After freezing, all debit operations of the customer are declined and the customer sees the reason; unfreezing restores them; action and admin name are written to the audit log.</td>
<td>Should</td>
<td>3</td>
</tr>
<tr class="even">
<td>US-10</td>
<td>As a customer, I want to unlink a card, because I no longer use it.</td>
<td>Unlinking needs an OTP; history stays; the card can be linked again later.</td>
<td>Could</td>
<td>2</td>
</tr>
<tr class="odd">
<td>US-11</td>
<td>As a customer, I want to pay bills online from my card, because I do not want to queue.</td>
<td>Not planned for this release (needs a payment-network integration).</td>
<td>Won’t</td>
<td>13</td>
</tr>
</tbody>
</table>

## 4.4. Breaking the feature into tasks (decomposition)

Feature F5 (US-01, card-to-card transfer) is divided into 8 tasks: 3 design, 3 development and 2 testing tasks. Every task is a separate Trello card with an owner, an estimate and a measurable result.

**Decomposition of the transfer feature into tasks**

| **ID** | **Task (outcome-oriented)**                                                                                                                                                                                                                                                                                                                                       | **Owner**             | **Estimate** | **Sprint** |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------|------------|
| T-01   | \[Design\] Draw the end-to-end transfer user flow in draw.io (choose card → enter recipient card and amount → confirm → enter OTP → receipt) with at least 8 steps and 3 error branches (insufficient funds, wrong OTP, recipient not found).                                                                                                                     | Diyorxo'ja Saidaliyev | 3 h          | 2          |
| T-02   | \[Design\] Create low-fidelity wireframes (Figma or draw.io) for the 3 screens of the transfer flow – card list with balances, transfer form (recipient card, amount), OTP entry with receipt – and check them with 2 potential users.                                                                                                                            | Diyorxo'ja Saidaliyev | 6 h          | 1          |
| T-03   | \[Design\] Draw the ER diagram with 6 tables (customers, cards, transactions, otp_codes, admins, audit_log), keys and the constraints CHECK(balance ≥ 0) and UNIQUE(idempotency_key).                                                                                                                                                                             | Diyorxo'ja Saidaliyev | 3 h          | 2          |
| T-04   | \[Dev\] Implement POST /api/transfers (debit and credit in one DB transaction with row locks and an idempotency key; returns 201, 404 for an unknown recipient card, 409 for a duplicate key or 422 for insufficient funds) and GET /api/cards with balances; includes the DB migration and seed data of 5 test customers with 8 cards in the mock Card Registry. | Diyorxo'ja Saidaliyev | 12 h         | 1          |
| T-05   | \[Dev\] Build the React page “Transfer money” (card selector, recipient card field, amount, confirmation dialog, receipt, error messages for insufficient funds, unknown card and duplicate) connected to the endpoints of T-04; works from 360 px screen width.                                                                                                  | Diyorxo'ja Saidaliyev | 10 h         | 1          |
| T-06   | \[Dev\] Add OTP confirmation to the transfer: generate a 6-digit code, send it through the mock SMS gateway, valid 3 minutes, maximum 3 attempts; the transfer is executed only after the correct code.                                                                                                                                                           | Diyorxo'ja Saidaliyev | 6 h          | 2          |
| T-07   | \[QA\] Write and run 15 manual test cases (TC-01…TC-15) for transfers: normal flow, insufficient funds, zero or negative amount, same card, unknown recipient, blocked card, double click, wrong OTP, 360 px layout.                                                                                                                                              | Diyorxo'ja Saidaliyev | 5 h          | 2          |
| T-08   | \[QA\] Write an automated pytest test that sends 50 parallel transfers of 100,000 UZS from a card holding 1,000,000 UZS and checks that exactly 10 succeed, 40 are rejected, the final balance is 0, it never goes negative and the total money of all cards is unchanged.                                                                                        | Diyorxo'ja Saidaliyev | 3 h          | 2          |

Figure 3 shows the draft wireframes of the 3 screens of task T-02 (card list with balances, transfer form, OTP entry); the OTP screen is added to the build in Sprint 2.

<img src="media/50cfc8a5d1bea71ddabcde2e3ed45bf63613d67d.png" title="figure" style="width:6.25in;height:3.38542in" alt="diagram" />

*Figure 3 – Draft wireframes of the transfer flow (task T-02)*

## 4.5. Sprint plan

**Sprint 1 (2 weeks, weeks 3–4). Capacity:** 1 person × 20 h per week × 2 weeks = 40 h; the selected tasks need 28 h, and the remaining 12 h (30 %) are a buffer for self-review, testing, the demo and unexpected problems.

**Sprint goal:** By the end of Sprint 1 a seeded test customer can open the web page, see their cards with balances and transfer money from a card to another card by card number; the transfer is stored atomically, the balance never becomes negative and a repeated request does not create a second transfer.

**Tasks moved to the To Do column for Sprint 1**

| **ID** | **Task**                                        | **Owner**             | **Estimate** | **Why it is in Sprint 1**                                                                                                           |
|--------|-------------------------------------------------|-----------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------|
| T-02   | \[Design\] Wireframes of 3 transfer screens     | Diyorxo'ja Saidaliyev | 6 h          | The frontend needs agreed screens; this fixes the “8 screens without scenarios” problem and stops design work on unrelated screens. |
| T-04   | \[Dev\] Transfer API with atomic balance update | Diyorxo'ja Saidaliyev | 12 h         | Critical path and the biggest technical risk; nothing can be shown without it.                                                      |
| T-05   | \[Dev\] React transfer page                     | Diyorxo'ja Saidaliyev | 10 h         | Gives users and the client something visible and usable at the end of the Sprint.                                                   |

**Why these three tasks.** Together they form the shortest path to a usable result: T-02 defines what the user sees, T-04 provides the data and the money rules, T-05 connects them in a page. T-01 and T-03 document what the Sprint already implements; T-06 (OTP confirmation) and the two QA tasks improve and verify the result but do not block the demonstration; they start in Sprint 2, when US-01 is completed with the OTP step. For Sprint 1 the users and cards are seeded test data with a temporary login (until US-02 and US-03 in Sprint 2) and all money is test money. Quality is controlled by the Definition of Done below.

**Definition of Done** – a task is “done” when:

- The code is merged into the main branch by a pull request after a self-review checklist (the diff is read again the next day) and passing CI checks; a classmate may review it if available.

- Unit and API tests of the task pass in CI (GitHub Actions) and cover at least 70 % of the new code; for money operations the concurrency test also passes.

- The acceptance criteria of the linked User Story are verified by the Product Owner on the staging server during a live demonstration.

- A security check is done: no secrets in the code, input is validated, access is by role, personal data are masked, and no High or Critical finding remains from the automated scan.

- There are no open Critical or High bugs related to the task.

- The API is documented in OpenAPI/Swagger and the README describes how to run the result (for design tasks: the Figma link is added to the card and the screens were checked with 2 potential users).

- The Trello card is moved to Done only after the Product Owner’s acceptance.

