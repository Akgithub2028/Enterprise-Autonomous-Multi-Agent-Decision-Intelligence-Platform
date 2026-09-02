# Security Boundaries and Audit Controls

## Request Context

Every request carries a `RequestPrincipal` and `SecurityContext`, specifying tenant, session, policy version, and optional `DataScope` and `KnowledgeScope`. This context governs which Skills, Tools, knowledge documents, and operational database tables the request is authorized to access.

## Layered Defense Architecture

```text
Identity & Session Validation
  -> Scenario & Route Filtering
  -> Workflow / Skill / Tool Discovery
  -> KnowledgeScope / DataScope Access Guards
  -> Provider Input Redaction & Budget Controls
  -> Reviewer & Citation Validation
  -> Response Emission & AuditEvent Logging
```

`KnowledgeScope` filters out unauthorized documents prior to RRF fusion and reranking; `DataScope` validates database access at MCP client initialization and query execution. Provider inputs undergo token budgeting and recursive redaction of sensitive identifiers.

## Guarded Execution and Answer Validation

Data queries must pass through MCP, SQLGlot parsing, SQLGuard security checks, strict table/column whitelists, mandatory LIMIT clauses, and query execution timeouts. Knowledge QA answers pass through Evidence Selection, Answerability Review, and strict Citation Validation. The final Reviewer audits workflow status, grounded answers, and cited evidence.

## Tracing and Audit Logs

Traces correlate Routing, Planning, Skill dispatch, Tool Calling, Retrieval, and Reviewer stages using unified Request IDs and Trace IDs. `AuditEvent` persists security-critical lifecycle events with append-only JSONL files and hash-chain integrity for verifiable local audit.

## Deterministic Security Benchmark

The security evaluation test suite comprises 28 deterministic test cases covering data access scopes, knowledge boundaries, provider input redaction, tool calling constraints, and response release checks (28 / 28 Passed).
