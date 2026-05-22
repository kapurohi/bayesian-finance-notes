# 23.3 — Applications and Extensions

## What this section is doing

Gelman covers hierarchical DP models — where each group has its own DP prior that shares atoms with other groups. This is the Hierarchical Dirichlet Process (HDP), appropriate when multiple related groups should share cluster structure but not be forced to have identical clusters.

---

## Financial application

**Sector-level portfolio segmentation:** Within each sector, companies cluster into subgroups (large-cap growth, mid-cap value, small-cap speculative). Across sectors, the same cluster types may appear. The HDP model captures this: within-sector clusters are drawn from a sector-specific DP, and the sector-level DPs share a common top-level DP. Companies across sectors can be assigned to the same cluster type without forcing identical cluster structures.

**Topic models for earnings transcripts:** The Latent Dirichlet Allocation (LDA) model — a text mining tool — is a DP mixture model applied to documents. Earnings call transcripts can be modeled as mixtures of latent topics. The HDP extension allows the same topics to appear across multiple companies without fixing the number of topics in advance.
