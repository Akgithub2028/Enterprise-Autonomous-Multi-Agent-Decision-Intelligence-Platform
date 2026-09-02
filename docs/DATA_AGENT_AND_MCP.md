# MCP Data Agent and Tool Calling

## Full Execution Chain

```text
Data Skill
  -> Native Tool Calling
  -> run_data_agent
  -> MCP fetches Schema and Business Definitions
  -> Data Planner generates SQL Plan
  -> MCP executes Query
  -> SQLGlot / SQL Guard Validation
  -> SQLAlchemy
  -> MySQL
  -> Data Evidence & Analysis Results
```

Native Tool Calling selects and invokes `run_data_agent`. Inside Data Agent, MCP exposes enterprise schemas, business definitions, and query execution tools. The Data Planner translates the natural language query into a structured query plan based on these contracts.

## MCP Tools

The MCP Server exposes three tools:

| Tool | Purpose |
| --- | --- |
| `get_enterprise_schema` | Returns authorized business tables and columns |
| `get_business_definitions` | Returns canonical business rules (sales, inventory, procurement, delivery) |
| `execute_safe_query` | Executes validated SQL and returns structured query results |

MCP decouples the Agent workflow from direct database access; schemas, query parameters, and result sets adhere to strict data contracts.

## Data Query Planning

The Data Planner produces a structured plan given the user query, authorized schema, and business definitions:

- Query status (`ready`, `needs_clarification`, `unsupported`);
- Business intent;
- SQL statement;
- Decision rationale;
- Missing information (for clarification requests).

Pydantic enforces strict contract validation over the plan. Once ready, Data Agent invokes MCP to execute the SQL, then formats query results into Data Evidence and cited answers.

## Query Security Rules

SQLGlot and SQLGuard parse MySQL syntax and enforce single-statement constraints, read-only guarantees, authorized table/column access, mandatory LIMITs, query timeouts, and result row caps. `DataScope` enforces the exact business resources accessible for each request.

## Local Data and Execution

`docker/mysql/init/01-schema.sql` and `02-seed.sql` provide synthetic relational data across products, suppliers, sales orders, inventory snapshots, and purchase orders. `03-create-readonly-user.sh` provisions the local read-only database user. MCP client and server sessions are managed by the runtime lifecycle, while offline integration tests utilize deterministic in-memory stubs.
