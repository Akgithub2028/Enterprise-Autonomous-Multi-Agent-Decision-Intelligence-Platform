# Evaluation Framework

## Evaluation Composition

The project incorporates three levels of rigorous evaluation:

1. **Unit Tests**: Verify contract integrity for models, parsers, services, and tools;
2. **Offline Integration Tests**: Validate deterministic end-to-end agent workflows;
3. **Retrieval Benchmarks & System Task Suites**: Quantify ranking performance and multi-agent decision quality.

## Public Verification Results

| Verification Suite | Result |
| --- | ---: |
| Unit Tests | 1,802 Passed |
| Stable Offline Integration Tests | 235 Passed |
| Deterministic Boundary Tests | 28 / 28 Passed |

GitHub Actions runs six automated checks across Pull Requests and the `main` branch: `quality`, `unit`, `security-evaluation`, `secret-scan`, `dependency-scan`, and `offline-integration`.

## Retrieval Benchmark v2

Retrieval Benchmark v2 contains 200 synthetic enterprise queries (160 answerable, 40 unanswerable). Hit@K and MRR metrics evaluate against the 160 answerable queries.

| Child Chunk Metrics | RRF Baseline | Cross-Encoder Reranked |
| --- | ---: | ---: |
| Hit@1 | 137 / 160 = 85.62% | 154 / 160 = 96.25% |
| MRR@5 | 146.7 / 160 = 91.69% | 157.0 / 160 = 98.12% |
| Hit@5 | 160 / 160 = 100% | 160 / 160 = 100% |

Cross-Encoder reranking improves Child Hit@1 by +10.63 percentage points and MRR@5 by +6.44 percentage points. The script `scripts/verify_retrieval_v2_evidence.py` verifies artifact checksums and recomputes all published metrics deterministically.

The legacy 50-query v1 benchmark is retained for historical baseline comparison: RRF Hit@1 = 84.78%, Cross-Encoder Hit@1 = 93.48%, RRF MRR@5 = 91.67%, Cross-Encoder MRR@5 = 96.74%.

## System Task Evaluation

| Metric | Result |
| --- | ---: |
| Formal Runtime | 8 / 9 |
| Deterministic Boundaries | 4 / 4 |
| Overall Accuracy | 12 / 13 |
| Unanswerable Handling | 2 / 3 |
| Provider Invocations | 45 |
| Input / Output Tokens | 38,549 / 4,258 |
| E2E Latency (P50 / P95) | 9.594s / 24.250s |

A single answerability misjudgment case is documented in the failure cases for continuous improvement of evidence sufficiency checks and abstention boundaries.

## Verification Procedures

Retrieval v1/v2 and M9 metric evaluations execute completely offline. Public verification requires no external model downloads or Provider API keys; see the README and `artifacts/public-evaluation/` for execution commands.
