# 15.4 — Non-Nested Models

## What this section is doing

Standard hierarchical models have a nested structure — companies within sectors, sectors within countries. Non-nested models handle crossed structures — the same observation is influenced by multiple group memberships that are not hierarchically related.

---

## Simplification

An analyst covers 30 companies across 5 sectors and 4 geographic regions. Each observation is simultaneously a member of a sector and a region. A non-nested hierarchical model estimates sector effects and region effects simultaneously — the two groupings are crossed, not nested.

---

## Financial application

A global equity model where each company belongs to a sector and a country. Both sector effects and country effects influence earnings growth, and they are not nested — a Japanese consumer company belongs to both Japan and Consumer Staples. The non-nested model estimates both dimensions of effects simultaneously while properly accounting for their correlation.

---

## See also
- Section 15.1 for the nested hierarchical regression this generalizes
