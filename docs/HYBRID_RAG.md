# Hybrid Retrieval (Hybrid RAG)

## Retrieval Pipeline

```text
Dense Retrieval + BM25
  -> KnowledgeScope Filtering
  -> RRF Fusion (k=60)
  -> Cross-Encoder Reranking
  -> Parent Expansion
  -> Evidence Context Assembly
  -> Evidence Selection
  -> Answerability Review
  -> Grounded Answer with Citations
```

The enterprise knowledge corpus uses versioned Parent/Child chunking. Dense retrieval utilizes `BAAI/bge-small-zh-v1.5` generating 512-dimensional normalized embeddings, while BM25 handles exact keyword recall. Reciprocal Rank Fusion (RRF) merges dual-stream Child rankings, `BAAI/bge-reranker-base` reranks candidates, and Parent Expansion restores surrounding document context.

The default configuration is Dense Top 10, BM25 Top 10, RRF Top 10, Reranker Top 5, Parent Top 5, with Evidence Context capped at 5 items and 6,000 characters.

## Retrieval Benchmark v2

The published evaluation suite contains 200 synthetic enterprise queries:

| Dataset Component | Count |
| --- | ---: |
| Total Queries | 200 |
| Answerable Queries | 160 |
| Unanswerable Queries | 40 |
| Documents | 12 |
| Parent records | 36 |
| Child evidence windows | 101 |

| Child Chunk Metrics | RRF Baseline | Cross-Encoder Reranked | Gain |
| --- | ---: | ---: | ---: |
| Hit@1 | 85.62% | 96.25% | +10.63 pp |
| MRR@5 | 91.69% | 98.12% | +6.44 pp |
| Hit@5 | 100% | 100% | — |

Ranking metrics use the 160 answerable queries as the denominator. The 96.25% Child Hit@1 measures precision at rank 1 after cross-encoder reranking.

## Evidence Verification

Run the following command to verify artifact SHA-256 checksums, dataset counts, and evidence schema, recomputing Hit@1, Hit@5, and MRR@5 metrics deterministically:

```bash
python scripts/verify_retrieval_v2_evidence.py
```

## Evidence Assembly

`KnowledgeScope` enforces document-level authorization before rank fusion. Top reranked Child chunks are expanded to full Parent blocks, from which the `EvidenceSelector` identifies the precise evidence items needed for answer generation, linking final citations directly to document IDs, versions, and source files.
