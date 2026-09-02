# M2C-1 Enterprise Knowledge Base Package

This directory describes the policies and operational rules of the fictional enterprise "Huaheng Intelligent Technology Co., Ltd." It is intended solely for offline engineering testing, retrieval evaluation blueprints, and manual auditing, and does not represent any real enterprise, individual, or production system.

## Directory Responsibilities

- `entity_dictionary.json`: Standardized IDs for companies, departments, products, accessories, regions, customer tiers, suppliers, and taxonomy categories.
- `business_fact_registry.json`: Fixed business facts that must remain consistent across documents along with their clause citations.
- `document_manifest.json`: Registry of 12 Markdown documents including versions, responsible departments, categories, and classification levels.
- `query_blueprint.jsonl`: 60 natural query blueprints, reference answers, relevant clauses, and hard negatives.
- `documents/`: Long-form enterprise policy documents with stable manual Clause IDs.

Clause IDs are manually maintained stable business labels, not Chunk IDs generated at retrieval runtime. Parent IDs or Child IDs are generated using the Markdown Parser and `ParentChildChunker`.

## Canonical Source Format & Multi-Format Ingestion

The 12 documents in the formal benchmark uniformly use Markdown as their canonical source format for maintaining Clause IDs, character offsets, version diffs, and ground truth. In addition, `tests/fixtures/ingestion/mixed_format/` contains static TXT, Markdown, and PDF fixtures to verify that `ParserRegistry` parses multiple formats into unified `DocumentBlock` models and feeds them into `ParentChildChunker`.

## Enterprise Profile & Capability Boundaries

- `DOC-ORG-001` serves as the authoritative source for the enterprise profile, establishing Huaheng Intelligent Technology Co., Ltd. as a fictional manufacturing and operations demonstration enterprise covering Products A/B, original batteries, procurement, inventory, sales fulfillment, and after-sales warranty scenarios.
- `DOC-AGENT-001` serves as the authoritative source for Agent capability boundaries, defining Knowledge, Data, and Mixed evidence-grounded capabilities, as well as explicit boundaries against open-web search, ungrounded chit-chat, long-term user profiling, and unauthorized write operations.

## Parent/Child Ground Truth

Clause IDs serve as stable manual semantic labels. Generated Parent/Child IDs and JSONL files are produced by the real Markdown Parser and `ParentChildChunker`. Ground truth mapping uses positive character interval overlap between clauses and chunk spans.
