## item_002_importer_l_export_api_de_l_univers_ogame_du_joueur - Importer l export API de l univers OGame du joueur
> From version: 1.0.0
> Schema version: 1.0
> Status: Ready
> Understanding: 90%
> Confidence: 85%
> Progress: 0%
> Complexity: High
> Theme: Operator workflow and runtime integration
> Reminder: Update status/understanding/confidence/progress and linked request/task references when you edit this doc.

# AI Context
- Summary: Découverte, implémentation et validation du connecteur d'export de compte pour un univers identifié.
- Keywords: discovery, contrat, mapping, sécurité, fixture, import
- Use when: Construire le connecteur externe et ses tests.
- Skip when: Le numéro d'univers ou un exemple de réponse n'est pas encore disponible.

# Problem
Le modèle `Empire` du MVP est prêt, mais il faut supprimer la ressaisie manuelle sans compromettre la sécurité ou la fiabilité des recommandations.

# Scope
- In:
  - recherche documentée de la source officielle de l'univers ciblé
  - contrat de données versionné et fixture anonymisée
  - adaptateur de l'export vers `Empire`, validation et erreurs actionnables
  - gestion locale et éphémère de l'authentification si celle-ci est requise
- Out:
  - actions de jeu, stockage de compte et support de plusieurs sources non validées

# Acceptance criteria
- AC1: La source officielle, ses prérequis et ses limites d'utilisation sont prouvés avant toute implémentation réseau.
- AC2: Le mapping de chaque champ économique requis vers `Empire` est documenté et couvert par une fixture.
- AC3: L'import ne produit jamais un empire partiel sans avertissement explicite ni secret persistant.
- AC4: Les tests de contrat passent sur une réponse valide, incomplète et incompatible.

# AC Traceability
- request-AC1 -> Backlog-AC1. Proof: la documentation de la source est une condition préalable contrôlée.
- request-AC2 -> Backlog-AC2. Proof: le mapping est contractuel et testé par fixture.
- request-AC3 -> Backlog-AC3. Proof: le validateur refuse les états incomplets ou incompatibles.
- request-AC4 -> Backlog-AC3. Proof: aucune persistance de secret n'est dans le périmètre de l'adaptateur.
- request-AC5 -> Backlog-AC4. Proof: les fixtures pilotent les tests de contrat.

# Decision framing
- Product framing: `prod_004_importer_l_export_api_de_l_univers_ogame_du_joueur`.
- Architecture framing: `adr_006_importer_l_export_api_de_l_univers_ogame_du_joueur`.

# Links
- Product brief(s): `prod_004_importer_l_export_api_de_l_univers_ogame_du_joueur`
- Architecture decision(s): `adr_006_importer_l_export_api_de_l_univers_ogame_du_joueur`
- Request: `logics/request/req_001_importer_l_export_api_de_l_univers_ogame_du_joueur.md`
- Primary task(s): (none yet)

# Priority
- Priority: High
- Rationale: L'import réel est le principal passage entre le prototype et une recommandation utile pour ce compte.

# Notes
- Dépendance bloquante : le joueur fournit le serveur/univers et un export anonymisé ou la documentation officielle du mécanisme d'export.

# Tasks
- `task_002_importer_l_export_api_de_l_univers_ogame_du_joueur`
