# Huaheng Intelligence Internal Test Environment Security Guidelines

This document is fictional internal material for mixed-format ingestion testing, isolated from the formal enterprise knowledge base and retrieval benchmark.

## Test Data Preparation

Test personnel should prioritize synthetic data and verify that files contain no real customers, employees, contact details, or access credentials prior to ingestion. Content used to validate parsing and chunking needs only to retain necessary business structures, and must not duplicate production databases, real contracts, or undisclosed operating materials. Filenames should be stable and readable, avoiding embedded usernames, machine directories, or random runtime identifiers.

## Permissions and Operations

Test directories adopt the principle of least privilege, open only to personnel responsible for verification. When results must be shared, summaries, checksums, or redacted snippets should be provided rather than transmitting entire working directories. No access tokens, database passwords, or service connection strings may be written into Markdown, test logs, or version control repositories. If suspected sensitive content is discovered, propagation must stop immediately and be reported following security procedures.

## Verification and Cleanup

Parsing verification should use the real ParserRegistry and verify document identity, source, content hashes, and parser names within unified DocumentBlock objects. Chunking verification uses the real ParentChildChunker to confirm parent-child relationships, offsets, and source traceability. Only deterministic static fixtures remain after tests complete; temporary outputs, caches, and dynamically generated files must be cleaned up.

This guideline does not define production password rotation periods, encryption algorithms, or data retention durations, and does not participate in query blueprints, business fact registries, or retrieval metric calculations.
