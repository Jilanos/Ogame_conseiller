## task_002_importer_l_export_api_de_l_univers_ogame_du_joueur - Importer l export API de l univers OGame du joueur
> From version: 1.0.0
> Schema version: 1.0
> Status: Ready
> Understanding: 90%
> Confidence: 85%
> Progress: 0%
> Complexity: Medium
> Theme: Implementation delivery
> Reminder: Update status/understanding/confidence/progress and linked request/backlog references when you edit this doc.

# AI Context
- Summary: Implémenter un adaptateur de l'export réel vers le format interne de l'optimiseur.
- Keywords: API, mapping, validation, sécurité, tests de contrat
- Use when: La source de l'univers et un exemple de réponse anonymisé sont disponibles.
- Skip when: Les seules informations disponibles sont l'identifiant de compte ou des secrets.

# Definition of Done (DoD)
- [ ] La source officielle et son contrat ont été validés sur l'univers cible.
- [ ] L'adaptateur importe toutes les données nécessaires à l'optimisation ou signale explicitement leur absence.
- [ ] Les fixtures anonymisées et tests de contrat couvrent format valide, incomplet et rompu.
- [ ] Aucun secret n'est stocké, affiché ou commité.
- [ ] Meaningful waves followed ADR 009: affected docs updated and the repo left commit-ready without automatic commits.

# Backlog
- `item_002_importer_l_export_api_de_l_univers_ogame_du_joueur`

# Acceptance criteria
- AC1: La source officielle, ses prérequis et ses limites d'utilisation sont prouvés avant toute implémentation réseau.
- AC2: Le mapping de chaque champ économique requis vers `Empire` est documenté et couvert par une fixture.
- AC3: L'import ne produit jamais un empire partiel sans avertissement explicite ni secret persistant.
- AC4: Les tests de contrat passent sur une réponse valide, incomplète et incompatible.

# Plan
- [ ] Identifier l'univers, consulter la documentation officielle et capturer un exemple d'export anonymisé.
- [ ] Écrire le schéma externe, le tableau de mapping vers `Empire` et les règles de champs obligatoires.
- [ ] Implémenter l'adaptateur isolé dans `src/ogame_conseiller/importer.py` ou un module dédié.
- [ ] Ajouter fixtures, tests de contrat et messages d'erreur actionnables.
- [ ] Vérifier le chemin local de secrets et mettre à jour l'aide CLI/README.

# Validation
- (no validation recorded yet)

# Report
- Not started.

# Links
- Request: `req_001_importer_l_export_api_de_l_univers_ogame_du_joueur`
- Product brief(s): `prod_004_importer_l_export_api_de_l_univers_ogame_du_joueur`
- Architecture decision(s): `adr_006_importer_l_export_api_de_l_univers_ogame_du_joueur`
