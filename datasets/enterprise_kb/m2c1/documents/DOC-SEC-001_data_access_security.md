# DOC-SEC-001 Enterprise Data Access and Information Security Specification

Version: 1.0
Scope: Data classification, access approvals, log auditing, and security incident response for Huaheng Intelligent Technology Co., Ltd.
Responsible Department: Information Security Office; Data Owning Departments, IT Operations, and General Manager Office coordinate in execution.

## I. Data Classification Principles

Data owning departments determine sensitivity classifications based on public disclosure risk, operational criticality, personal privacy rights, and legal obligations, while the Information Security Office provides standard criteria and audits high-level data assets. Classification inheres in actual data assets and usage scenarios rather than physical storage locations; mixed data sets are protected under the highest applicable classification tier; downgrades require documented evidence and formal authorization.

Clause ID: SEC-DATA-L1

L1 designates Public Data, authorized for external distribution within defined release scopes, such as official published product specifications. Verification of document version, intellectual property, and content accuracy is required prior to publication; internal drafts cannot be treated as L1 simply because their subject matter is public. Withdrawn or expired content must be updated promptly to prevent the dissemination of erroneous information.

Clause ID: SEC-DATA-L2

L2 designates Internal Data, restricted to standard operational business execution, including general internal workflows and routine work materials containing no sensitive operational details. L2 data does not require dual-role approval mandated for L3, but remains subject to role-based authorization and least-privilege principles; "Internal" cannot be construed as permitting arbitrary bulk downloading, forwarding, or uncontrolled archiving.

Clause ID: SEC-DATA-L3

L3 designates Confidential Data, whose unauthorized disclosure could cause significant commercial, customer, or regulatory impact, such as unpublished pricing strategies and sensitive supplier assessment scorecards. Access requires defined business purposes, precise field scopes, and explicit validity timeframes, subject to dedicated dual approval and continuous audit. Permissions must be revoked immediately upon project completion or role transitions without relying on self-cleanup.

Clause ID: SEC-DATA-L4

L4 designates Strictly Restricted Data, whose disclosure or compromise would inflict catastrophic harm on enterprise survival or core assets. Systems must enforce the most stringent identity authentication, dedicated hardware, isolated network, end-to-end encryption, and operational controls, restricted to a minimal set of vetted roles. Operational convenience cannot justify tier downgrades; anonymization, tokenization, aggregation, or secure enclaves must be prioritized to minimize raw data exposure.

## II. Access Authorization

Clause ID: SEC-ACCESS-L3

Access to L3 Confidential Data requires joint approval from both the Department Head and the Information Security Office. Application dossiers must specify dataset identifiers, requested columns/fields, operational purpose, authorized user identities, target environments, validity durations, and data export formats; both approvals are mandatory. The Department Head verifies operational necessity, and the Information Security Office validates technical controls; neither party can substitute for the other.

Clause ID: SEC-ACCESS-L4

Access to L4 Strictly Restricted Data requires joint approval from both the Information Security Head and the General Manager. Authorizations must be granted to specific named individuals, precise data scopes, isolated execution environments, and minimum necessary durations; blanket approvals for broad departments or project teams are prohibited. Emergency situations cannot utilize L3 approval paths as substitutes; immediate containment such as resource isolation or service shutdown that avoids data exposure must be deployed first.

Clause ID: SEC-LEAST-PRIVILEGE

All data access tiers enforce least privilege, minimum duration, and separation of duties. When aggregate summaries satisfy the query intent, granular records must not be exposed; when read-only access suffices, write permissions are denied; when specific fields can be isolated, entire tables remain restricted. Bulk exports, cross-border transfers, or vendor sharing require independent assessments; prior access approvals do not automatically extend to new usage modes.

Clause ID: SEC-ACCESS-REVIEW

Data owning departments and the Information Security Office conduct regular audits of elevated permissions, persistent standing access, transferred/terminated personnel, and concluded project accounts. Accounts lacking current business needs, exceeding authorized scope, or reaching expiration dates must be revoked immediately. Audit logs must capture original authorizations, actual access logs, and disposal actions; inactive accounts cannot be overlooked due to recent lack of logins.

## III. Logging and Audit Trails

Clause ID: SEC-LOG-GENERAL-180D

Standard system access and operational audit logs must be retained for a minimum of one hundred eighty days. Logs must capture verifiable user accounts, timestamps, source systems, action types, and execution outcomes under unified NTP time synchronization and tamper-evident integrity protection. Retention begins on the log creation date; storage capacity constraints cannot justify premature log deletion and must be addressed via automated tiering or expansion.

Clause ID: SEC-LOG-L3L4-365D

Access and operational audit logs for L3 and L4 data must be retained for a minimum of three hundred sixty-five days, recording application linkages, accessing identities, accessed field scopes, query operations, export actions, and anomalous outcomes. This requirement supersedes the standard 180-day baseline and cannot be shortened because standard logs exist. Where statutory regulations mandate longer retention, the longer duration prevails.

Clause ID: SEC-LOG-PROTECTION

Audit log storage must enforce strict write-once, read-only permissions restricting modification and deletion; critical systems utilize centralized collection, cryptographic hashing, and offsite backups. Systems engineers cannot simultaneously hold unmonitored log deletion rights and business approval authorizations. When logs contain sensitive values, logs themselves inherit corresponding protection levels; auditors access only the scope required for investigations.

## IV. Security Incidents and Third Parties

Clause ID: SEC-INCIDENT-REPORT

Suspected privilege escalations, data leaks, malware detections, hardware loss, or audit log anomalies must be reported immediately to the Information Security Office with forensic environments preserved. Incident response prioritizes risk isolation, evidence preservation, and critical service continuity; unauthorized log tampering or external public statements are strictly prohibited. Incidents receive formal severity grading, designated incident commanders, recovery timelines, and post-mortem reviews.

Clause ID: SEC-THIRD-PARTY

External suppliers requiring enterprise data access must complete security assessments, nondisclosure agreements, least-privilege scoping, and expiration deprovisioning protocols prior to access. L3 and L4 access tiers enforce standard executive approvals regardless of outsourcing contracts. Vendors may process data solely within approved environments for designated purposes; subcontracting, model training, or marketing use is prohibited; data destruction/return must be verified upon contract termination.

## V. Exceptions and Governance

Security exceptions must detail unfulfillable controls, operational necessity, risk assessments, compensating safeguards, and explicit expiration dates, approved by the Information Security Head; changes involving L4 data scopes continue to require joint approval with the General Manager. Exceptions expire automatically without continuous rollover. The Information Security Office conducts monthly reviews of elevated access, data exports, anomalous logs, and deprovisioning compliance. Where policies do not specify exact password rotation days or cryptographic algorithms, fabricating ungrounded answers is prohibited; separate technical standards govern such implementation parameters.
