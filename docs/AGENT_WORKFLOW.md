# Agent Workflow

## Overall Process

The system employs a coordinated architecture separating responsibilities across Router, Planner, Skill, Tool, and Reviewer components. The language model is responsible for intent understanding, plan formulation, and response organization, while the server runtime handles workflow orchestration, tool registration, context assembly, result validation, and state persistence.

```text
Request Validation
  -> Load Session Context
  -> Router Identifies Task Category
  -> Coordinator Dispatches Skill
  -> Planner Formulates Structured Plan
  -> Skill & Tool Execution
  -> Evidence Selection & Answer Generation
  -> Reviewer Validates Output & Citations
  -> Emit Response & Persist Trace
```

## Routes and Skills

| Route | Skill | Scope |
| --- | --- | --- |
| Knowledge | `enterprise-knowledge-qa` | Enterprise document retrieval, evidence selection, and cited answers |
| Data | `enterprise-data-analysis` | Operational data query, execution, and analysis |
| Mixed | `inventory-risk-diagnosis` | Combined knowledge policy and operational data inventory risk recommendations |

Knowledge and Data requests execute their respective single Skill workflows; Mixed requests compose knowledge and data subtasks before passing both Evidence streams into the synthesis and review stages.

## Prompts and Structured Output

The system designs dedicated prompt templates for each stage and strictly enforces structured contracts via Pydantic validation:

1. `routing`: Identifies Knowledge, Data, or Mixed tasks;
2. `planning`: Generates workflow execution plans;
3. `data_planning`: Generates schema-grounded data query plans and SQL;
4. `evidence_selection`: Selects required evidence items from retrieved chunks;
5. `answerability_review`: Assesses whether available evidence is sufficient to answer;
6. `knowledge_answer` and `data_answer`: Generates grounded, cited answers;
7. `inventory_synthesis`: Synthesizes inventory data with replenishment policy rules;
8. `workflow_review`: Audits final answers, citations, and terminal execution status.

Each route activates only the stages required for its specific task.

## Error Handling

Routing, planning, tool execution, retrieval, and review stages all return explicit lifecycle statuses and error codes. Upon execution failure, workflows transition into deterministic failure branches and record stage-level diagnostics into the Trace, enabling end-to-end debugging via the unified Request ID.
