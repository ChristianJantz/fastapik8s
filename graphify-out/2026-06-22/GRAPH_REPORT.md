# Graph Report - .  (2026-06-22)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 13 nodes · 13 edges · 4 communities (3 shown, 1 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `db012053`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_API Route Handlers|API Route Handlers]]
- [[_COMMUNITY_Project Dependencies|Project Dependencies]]
- [[_COMMUNITY_Data Models|Data Models]]

## God Nodes (most connected - your core abstractions)
1. `ItemTypeEnum` - 2 edges
2. `ItemModel` - 2 edges
3. `ResponseItem` - 2 edges
4. `FastAPI (standard) 0.113.0` - 2 edges
5. `Pydantic 2.8.0` - 2 edges
6. `fastapik8s README` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (4 total, 1 thin omitted)

### Community 1 - "Project Dependencies"
Cohesion: 0.67
Nodes (3): fastapik8s README, FastAPI (standard) 0.113.0, Pydantic 2.8.0

### Community 2 - "Data Models"
Cohesion: 0.67
Nodes (3): ItemModel, ResponseItem, BaseModel

## Knowledge Gaps
- **1 isolated node(s):** `fastapik8s README`
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ItemModel` connect `Data Models` to `API Route Handlers`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **Why does `ResponseItem` connect `Data Models` to `API Route Handlers`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **What connects `fastapik8s README` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._