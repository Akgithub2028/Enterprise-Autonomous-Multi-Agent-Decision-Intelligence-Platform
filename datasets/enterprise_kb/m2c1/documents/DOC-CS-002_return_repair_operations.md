# DOC-CS-002 Returns, Exchanges, and Repair Operations Specification

Version: 1.0
Scope: Standard product returns, dead-on-arrival (DOA) exchanges, and repair operations for Huaheng Intelligent Technology Co., Ltd.
Responsible Department: Customer Service Department; Warehouse Management Department, Sales Operations Department, and Supply Chain Center coordinate in execution.

## I. Intake Principles

This specification establishes unopened returns, DOA defect exchanges, and warranty repairs as three distinct operational workflows. Intake personnel must verify customer tier, product model, delivery receipt date, packaging condition, and software activation status before selecting the workflow intake path. Skipping verification criteria simply because a customer requests a "return or exchange" is strictly prohibited. All calendar-day and workday criteria must be explicitly communicated; cutoff dates are determined by successful system submission timestamps.

Clause ID: CS-RETURN-INTAKE

Customer applications must include order/contract identifiers, product serial numbers, proof of delivery, problem descriptions, and necessary photographic evidence. For incomplete submissions, Customer Service provides a one-time notification of missing items and logs the initial contact timestamp. Formal review begins only after product identity and eligibility windows can be verified, preventing cross-contamination between orders, accessories, or customer tiers.

Clause ID: CS-RETURN-UNOPENED-7D

Unopened standard products in intact original packaging are eligible for standard return within seven calendar days of delivery receipt. Intact packaging requires seals, included accessories, user manuals, and outer carton labeling to remain in resalable condition. Applications submitted within the seven-day window whose physical return shipment arrives later remain valid based on submission records, subject to warehouse physical inspection upon arrival.

Clause ID: CS-RETURN-EXCLUSIONS

Custom configurations, activated software licenses, and customer-induced damage are strictly excluded from no-reason returns. Custom configurations refer to deliveries where standard hardware, firmware parameters, or exclusive branding have been modified per customer confirmation; standard purchases of genuine accessories do not inherently constitute customization. When customer damage is detected, the case transitions to liability inspection; minor outer box transit scuffs shall not be automatically classified as customer damage.

## II. Dead-on-Arrival (DOA) Defect Exchanges

Clause ID: CS-DOA-A-15D

Enterprise customer Product A units experiencing reproducible factory manufacturing defects within fifteen calendar days of delivery receipt are eligible for DOA exchange. Customer Service must verify receipt dates and host serial numbers, confirming that defects do not stem from configuration errors, local network issues, non-genuine charging equipment, or external physical damage. Accessory defects are evaluated independently based on accessory identity.

Clause ID: CS-DOA-B-30D

Enterprise customer Product B units experiencing reproducible factory manufacturing defects within thirty calendar days of delivery receipt are eligible for DOA exchange. This thirty-day window cannot be applied to Product A, nor is it equivalent to the seven-day unopened return policy. Environmental operating conditions must be logged concurrently for issues occurring in rugged environments to differentiate manufacturing defects from non-compliant operational use.

Clause ID: CS-DOA-VERIFICATION

DOA defects must be validated via remote system logs, standardized reproduction procedures, or testbench diagnostics. For intermittent failures, customers may provide continuous operation logs; technical personnel shall not close tickets solely based on a single failed reproduction attempt. If diagnostic evidence remains insufficient, further testing must be scheduled with estimated timeline milestones. Exchange determinations must explicitly record product model, failure symptoms, and liability rationale.

Clause ID: CS-DOA-AFTER-WINDOW

Products exceeding their respective DOA exchange windows transition into the standard repair workflow and are no longer eligible for direct replacement. Transitioning to repair does not forfeit base warranty entitlements; whether fees apply depends on warranty periods and exclusions defined in DOC-CS-001. Intake personnel must clearly explain the distinction between exchange windows and warranty periods to the customer.

## III. Repair Logistics and Quality

Clause ID: CS-REPAIR-ROUTING

The repair workflow includes preliminary diagnosis, data backup reminders, shipping instructions, receiving inspection, technical diagnostics, quotation/warranty confirmation, repair verification, and return dispatch. Customer Service serves as the unified communication window, Warehouse Management verifies physical receipt/dispatch, and Supply Chain coordinates spare parts. Internal reassignments must never generate isolated records detached from the original service ticket ID.

Clause ID: CS-REPAIR-DATA

Customers must be reminded to back up and clear non-essential business data prior to dispatch. If a device cannot power on, data status must be logged and handled under restricted access controls. Repair personnel may only access data strictly necessary for diagnostic troubleshooting and are prohibited from duplicating customer business files. Devices handling L3 or L4 data must simultaneously comply with approval, least-privilege, and audit requirements in DOC-SEC-001.

Clause ID: CS-REPAIR-QUOTE

For repairs outside base warranty coverage, a detailed quotation including itemized parts, quantities, unit prices, and estimated repair timelines must be provided and confirmed by the customer prior to part replacement. Diagnostic, logistics, and repair fees must be itemized separately. If the customer declines the quotation, the device is returned under agreed terms. Concealing total costs through unbundled line items or performing repairs prior to customer authorization is strictly prohibited.

Clause ID: CS-REPAIR-QUALITY

Following repair completion, the original defect, core functions, charging, and communication subsystems must be re-tested and replaced components recorded. A technician other than the repairing engineer must conduct pre-shipment quality verification. If the same failure recurs within a short interval, the case must be escalated for technical root-cause analysis to identify batch defects, diagnostic errors, or environmental factors rather than repeating identical ineffective repairs.

## IV. Exceptions and Disputes

Clause ID: CS-RETURN-EXCEPTION

When shipment errors by the company, carrier liability, or batch quality incidents require resolution beyond standard timelines, Customer Service compiles order details, root cause, quantities, costs, and customer impact for joint review by Sales Operations and Supply Chain. Matters involving refunds, additional compensation, or policy commitments also require Finance approval. Exception approvals shall not alter foundational policy rules.

Clause ID: CS-RETURN-DISPUTE

Customers disputing packaging assessments, liability determinations, or timeline calculations may request a one-time administrative review. The reviewer must be independent of the initial decision-maker and must inspect original delivery receipts, photos, system logs, and diagnostic records. Review determinations must document reasons for sustaining or modifying decisions; where evidence cannot rule out company liability, uncertainties must be stated clearly with actionable remediation plans.

## V. Ledger and Governance

System ledgers track counts for 7-day unopened returns, Product A 15-day DOA exchanges, Product B 30-day DOA exchanges, and repairs separately. Customer Service conducts monthly audits of timeline compliance, mandatory fields, and closure documentation, while Warehouse Management verifies physical inventory flows. Reclassifying exchanges as repairs, backdating application dates, or deleting recurring failure records to manipulate performance metrics is strictly prohibited; audit trails preserve all pre- and post-correction modification history.
