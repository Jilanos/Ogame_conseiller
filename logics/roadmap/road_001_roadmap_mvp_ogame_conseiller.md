## road_001_roadmap_mvp_ogame_conseiller - Roadmap MVP OGame Conseiller
> Date: 2026-08-15
> Status: Proposed
> Related product: prod_002_calculateur_de_trajectoire_economique_ogame_solo
> Related request: `req_000_calculateur_de_trajectoire_economique_ogame_solo`
> Reminder: Update status, milestone scope, linked refs, risks, and success signals when you edit this doc.

# AI Context
- Summary: Roadmap for Roadmap MVP OGame Conseiller.
- Keywords: roadmap, milestones, versions, roadmap mvp ogame conseiller
- Use when: Planning or sequencing versions for Roadmap MVP OGame Conseiller.
- Skip when: You need execution details for a single backlog item or task.

# Summary
Livrer un premier conseiller économique local, fiable et explicable pour un empire OGame solo orienté mines.

# Milestones
## 0.1 - MVP
- Goal: Calculer et comparer des trajectoires économiques 10/30/90 jours à partir d'un état d'empire réel ou saisi.
- Scope: `item_001_calculateur_de_trajectoire_economique_ogame_solo`, `task_001_calculateur_de_trajectoire_economique_ogame_solo`, règles économiques, simulation, beam search, import local et interface de restitution.
- Exit signal: Une fixture multi-planètes importée produit trois plans déterministes, réalisables et expliqués, avec tests automatisés verts.

# Sequencing
- Deliver milestones in ascending version order unless dependencies force a documented exception.
- Keep each increment independently reviewable and linked to concrete workflow docs.

# Risks
- Le format/export officiel peut être indisponible ou différent selon l'univers : la saisie manuelle et l'import de fichier restent le chemin de repli MVP.
- Les bonus non modélisés peuvent biaiser un résultat : les afficher et les désactiver explicitement au lieu de les supposer.
- Le coût de recherche peut exploser : borner la beam search et mesurer ses performances sur des fixtures réalistes.

# References
- Product brief(s): `prod_002_calculateur_de_trajectoire_economique_ogame_solo`
- Request(s): `req_000_calculateur_de_trajectoire_economique_ogame_solo`
- Backlog item(s): `item_001_calculateur_de_trajectoire_economique_ogame_solo`
- Task(s): `task_001_calculateur_de_trajectoire_economique_ogame_solo`
