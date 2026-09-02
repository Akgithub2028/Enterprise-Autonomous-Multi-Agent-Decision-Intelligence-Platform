# Retrieval Evaluation v2 Public Evidence

This evidence package is used for independent verification of the 200-query retrieval benchmark metrics without requiring model downloads or external provider credentials.

## Core Results

The evaluation dataset contains 200 synthetic enterprise scenario queries (160 answerable, 40 unanswerable). Ranking metrics use the 160 answerable queries as the denominator.

| Child Metric | RRF | Cross-Encoder |
| --- | ---: | ---: |
| Hit@1 | 137 / 160 = 85.62% | 154 / 160 = 96.25% |
| Hit@5 | 160 / 160 = 100.00% | 160 / 160 = 100.00% |
| MRR@5 | 146.7 / 160 = 91.69% | 157.0 / 160 = 98.12% |

## Verification Command

Execute from the repository root:

```bash
python3 scripts/verify_retrieval_v2_evidence.py
```

The script verifies fixed file hashes, query counts, Evidence schema, and recalculates Hit@1, Hit@5, and MRR@5 from `ranking_records.jsonl` and `relevance_freeze.jsonl`.

## File Descriptions

- `relevance_freeze.jsonl`: Fixed query and Child relevance annotations
- `ranking_records.jsonl`: RRF and Cross-Encoder ranking results for 200 queries
- `metrics.json`: Complete metrics, slicing, and coverage analysis
- `experiment_report.md`: Experimental procedure and metric explanations
- `failure_cases.md`: Cross-Encoder Top-1 missed cases
- `relevance_audit.md`: Relevance annotation review record
- `runtime.json`: Model versions, configuration, and offline execution metadata
- `manifest.json`: Counts, identities, and file hashes
