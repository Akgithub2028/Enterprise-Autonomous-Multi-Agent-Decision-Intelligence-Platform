# DOC-INV-001 Inventory Safety Stock and Replenishment Management Policy

Version: 1.0
Scope: Inventory monitoring, replenishment, and emergency allocation of inspection host terminals and original batteries for Huaheng Intelligent Technology Co., Ltd.
Responsible Department: Warehouse Management Department; Supply Chain Center, Procurement Management Department, and Sales Operations Department coordinate in execution.

## I. Inventory Accounting Criteria

This policy evaluates threshold triggers strictly against sellable available quantity. Sellable available quantity equals quality-passed warehouse stock minus committed order reserves, quality inspection holds, dedicated repair pools, and pending write-offs. In-transit inventory is tracked and reported separately and cannot offset safety stock lines prior to formal quality acceptance and warehouse intake. Warehouse Management generates daily inventory snapshots at a fixed cutoff time; Supply Chain schedules replenishment based on run-rate trends and supplier lead times.

Clause ID: INV-STOCK-DEFINITION

Inventory records must be segregated by stable product and accessory IDs. Product A, Product B, Model A Original Battery, and Model B Original Battery must not be aggregated. Physical count discrepancies trigger an immediate freeze on affected quantities pending root-cause investigation; recording uninspected in-transit goods as available stock to avoid triggering procurement, or treating repair buffer stock as sellable inventory, is strictly prohibited.

Clause ID: INV-A-REORDER-180

The reorder trigger threshold for Product A is one hundred eighty units. When sellable available quantity reaches or falls below this line, the Supply Chain Center formulates replenishment proposals based on unfulfilled orders, sales forecasts, and vendor lead times. The reorder line triggers early procurement planning and does not indicate an emergency state; replenishment quantities must avoid excessive inventory buildup from short-term demand fluctuations.

Clause ID: INV-A-SAFETY-120

The safety stock threshold for Product A is one hundred twenty units. When available quantity falls below safety stock, replenishment must be initiated immediately, and Sales Operations reviews the impact of pending large-volume orders. The safety stock line must not be confused with the 180-unit reorder trigger line or the 80-unit emergency stock line; all reports must display the specific threshold tier currently activated.

Clause ID: INV-A-EMERGENCY-80

The emergency stock threshold for Product A is eighty units. Dropping below this line triggers emergency procurement procedures and sales allocation controls, prioritizing executed contracts, critical warranty replacements, and confirmed strategic projects. New low-priority orders must be flagged for delivery risks; bypassing allocation controls to reserve inventory privately is strictly prohibited.

## II. Product B and Battery Thresholds

Clause ID: INV-B-REORDER-120

The reorder trigger threshold for Product B is one hundred twenty units. While this value equals Product A's safety stock threshold, its operational significance is distinct; automated and manual reports must explicitly present both product model and threshold type. Reaching or dropping below this trigger initiates planned replenishment and must not be erroneously reported as Product B being below safety stock.

Clause ID: INV-B-SAFETY-80

The safety stock threshold for Product B is eighty units. When inventory drops below this line, replenishment must be triggered and in-transit delivery reliability verified; if shipment delay probabilities are elevated, emergency procurement options must be evaluated proactively. Applying Product A's 120-unit safety line to Product B, or confusing this clause with the emergency stock line, is prohibited.

Clause ID: INV-B-EMERGENCY-50

The emergency stock threshold for Product B is fifty units. Dropping below fifty units triggers emergency procurement workflows and strict sales allocation controls. Warehouse Management increases cycle count frequency, Supply Chain updates delivery schedules daily, and Sales Operations restricts new delivery commitments; the 50-unit emergency line cannot be interchanged with the 80-unit safety stock line.

Clause ID: INV-BATTERY-A-SAFETY-200

The safety stock threshold for Model A Original Battery is two hundred pieces. Falling below this line triggers standard replenishment, sizing batch orders based on Product A in-warranty installed base, repair consumption rates, and sales attachment ratios. Battery inventory is measured in pieces and cannot be summed directly with host units; non-genuine batteries are excluded from this policy.

Clause ID: INV-BATTERY-B-SAFETY-120

The safety stock threshold for Model B Original Battery is one hundred twenty pieces. Dropping below this line triggers replenishment, focusing on Product B after-sales replacement demand and vendor manufacturing cycles. While this numerical value matches Product B's reorder trigger line, the target item and unit of measure differ; reports must explicitly state "Battery Safety Stock" rather than merely listing 120.

## III. Replenishment and Emergency Allocation

Clause ID: INV-REPLENISHMENT-PROCESS

The replenishment workflow encompasses threshold alert generation, demand review, stock vs. in-transit verification, purchase requisition, multi-level approval, delivery tracking, inbound acceptance, and alert resolution. Standard purchases require tiered authorization per DOC-PROC-001. When inventory breaches emergency lines under qualified emergency conditions, emergency procurement paths may be used; splitting purchase orders to circumvent approval limits during inventory shortages is prohibited.

Clause ID: INV-ALLOCATION-CONTROL

Emergency stock allocation evaluates requirements in strict sequence: executed contract commitments, critical warranty replacements, confirmed strategic customer projects, and other general orders, considering committed delivery dates and technical substitution feasibility. Customer tier is not the sole criterion; uncontracted strategic opportunities cannot displace legally executed orders from regular customers. Every allocation adjustment must record approved quantities, business justification, and approver details.

Clause ID: INV-COUNT-RECONCILIATION

Warehouse Management conducts comprehensive monthly physical inventory counts, increasing cycle counts for high-risk materials or items operating below emergency thresholds. When system balances diverge from physical counts, available quantities must be adjusted immediately with difference audit trails preserved before investigating receiving, allocation, or scrapping records. Fabricating inbound or outbound transactions to artificially restore balances above safety lines is prohibited.

## IV. Exceptions and Governance

Clause ID: INV-EXCEPTION

New product introductions, end-of-life run-outs, product recalls, or approved large-scale enterprise projects may establish temporary threshold rules. Supply Chain must submit justification, validity periods, and exit conditions for joint review by Sales Operations and Finance. Temporary rules apply strictly to specified materials and timeframes without altering the permanent baseline thresholds codified in this policy.

## V. Execution Reporting

Daily inventory alert reports must detail material ID, sellable available quantity, in-transit quantity, reorder trigger line, safety stock line, emergency stock line, and current remediation actions. Where accessories have only safety stock definitions, fabricating artificial reorder or emergency thresholds is prohibited. Supply Chain reviews active alert durations, procurement tracking, and sales allocation weekly, ensuring identical numerical values preserve clear context regarding product model, measurement unit, and threshold type across all reporting channels.
