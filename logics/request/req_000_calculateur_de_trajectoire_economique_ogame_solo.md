## req_000_calculateur_de_trajectoire_economique_ogame_solo - Calculateur de trajectoire economique OGame solo
> From version: 1.0.0
> Schema version: 1.0
> Status: Done
> Understanding: Créer un MVP de planification économique solo : projection et optimisation de production à 10, 30 et 90 jours, puis import de l’état actuel du compte via l’export de données de compte.
> Confidence: high
> Complexity: high
> Theme: product
> Reminder: Update status/understanding/confidence and linked backlog/task references when you edit this doc.

# AI Context
- Summary: Un conseiller économique personnel pour OGame, centré sur un empire solo de mineur et sur la maximisation de production de métal, cristal et deutérium.
- Keywords: OGame, économie, mines, optimisation, simulation, trajectoire, API export, empire
- Use when: Concevoir le MVP, le moteur de calcul, l'import d'état de compte ou les scénarios de production.
- Skip when: Concevoir un bot, automatiser des actions de jeu, optimiser le combat, les flottes ou l'espionnage.

# Needs
- À partir d'un état d'empire renseigné ou importé, proposer pour chaque horizon de 10, 30 et 90 jours une séquence d'investissements économique qui maximise la production cumulée de ressources.
- Présenter une recommandation explicable : ordre des constructions, dates de lancement, coûts, ressources attendues et hypothèses utilisées.

# Context
- Le joueur adopte une stratégie principalement solo et minière : les mines, centrales, stockage et technologies de production sont prioritaires.
- Les règles varient selon l'univers : vitesse économique, classe, formes de vie, officiers, collecteur et bonus doivent donc être des paramètres explicites, avec des valeurs neutres par défaut.
- L'import doit partir de l'export officiel de données du compte ; avant de figer le connecteur, le format réellement disponible, ses champs et son mode d'authentification doivent être vérifiés sur l'univers cible.
- L'outil est un conseiller de décision : il ne se connecte pas au jeu pour effectuer des actions et ne stocke jamais de clé/API-token côté serveur.

# Acceptance criteria
- AC1: L'utilisateur peut saisir ou importer un empire multi-planètes comprenant ressources disponibles, niveaux de mines, énergie, bâtiments économiques, technologies pertinentes et files de construction.
- AC2: Le moteur produit pour 10, 30 et 90 jours un plan ordonné d'investissements réalisables et compare sa production cumulée à une stratégie « ne rien construire ».
- AC3: Chaque recommandation affiche ses coûts, son instant de départ, l'impact sur la production par heure et les hypothèses de calcul (vitesse, bonus et paramètres économiques).
- AC4: Pour un même état, les mêmes paramètres et la même version de règles, le résultat est déterministe et couvert par des scénarios de référence.
- AC5: Le MVP empêche les configurations impossibles (énergie insuffisante, ressources indisponibles, prérequis manquants, construction simultanée sur une même planète).

# Definition of Ready (DoR)
- [x] Problem statement is explicit and user impact is clear.
- [x] Scope boundaries (in/out) are explicit.
- [x] Acceptance criteria are testable.
- [x] Dependencies and known risks are listed.

# Companion docs
- Product brief(s): `prod_002_calculateur_de_trajectoire_economique_ogame_solo`
- Architecture decision(s): `adr_003_calculateur_de_trajectoire_economique_ogame_solo`

# Scope boundaries
- In: projection économique, optimisation de construction, multi-planètes, saisie manuelle et import d'export de compte, restitution web locale.
- Out: automatisation du jeu, combat, flotte, défense, espionnage, commerce/alliance, simulation de formes de vie détaillée et recommandations basées sur des données privées tierces.

# Backlog
- `item_001_calculateur_de_trajectoire_economique_ogame_solo`
