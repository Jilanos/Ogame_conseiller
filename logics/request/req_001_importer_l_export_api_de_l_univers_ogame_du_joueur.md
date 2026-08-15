## req_001_importer_l_export_api_de_l_univers_ogame_du_joueur - Importer l export API de l univers OGame du joueur
> From version: 1.0.0
> Schema version: 1.0
> Status: Ready
> Understanding: Permettre au calculateur de charger l état réel de l empire depuis l export/API officiel de l univers du joueur, après caractérisation documentée du format et de l authentification.
> Confidence: medium
> Complexity: High
> Theme: integration
> Reminder: Update status/understanding/confidence and linked backlog/task references when you edit this doc.

# AI Context
- Summary: Connecter l'état réel d'un empire au calculateur au moyen du mécanisme d'export officiellement disponible dans son univers OGame.
- Keywords: OGame, univers, API, export, authentification, import, adaptateur
- Use when: Chercher, implémenter ou tester le connecteur de données de compte.
- Skip when: Demander un bot ou une automatisation d'actions dans le jeu.

# Needs
- Charger les données économiques d'un compte depuis un export/API, les vérifier, puis les convertir en `Empire` utilisable par l'optimiseur.

# Context
- L'univers n'est pas encore identifié ; l'API, les champs et le mécanisme d'autorisation doivent être confirmés sur sa documentation ou avec un export réel anonymisé.
- Les données de compte sont sensibles. Aucun mot de passe, cookie, session ou token ne doit être commité, journalisé ou envoyé à un serveur applicatif.
- Une saisie manuelle et l'import JSON MVP restent disponibles si l'export officiel n'est pas accessible.

# Acceptance criteria
- AC1: La source officielle de l'univers est documentée avec URL, authentification, cadence autorisée et exemples anonymisés de réponse.
- AC2: Un adaptateur valide et normalise les planètes, ressources, mines, énergie, bâtiments économiques, technologies et files de construction vers le format `Empire`.
- AC3: Les données manquantes ou incompatibles produisent des erreurs compréhensibles, sans résultat silencieusement faux.
- AC4: Le connecteur n'écrit aucun secret sur disque ni dans les logs ; les secrets éventuels passent uniquement par variables d'environnement ou saisie locale éphémère.
- AC5: Des fixtures anonymisées et des tests de contrat détectent toute rupture du format externe.

# Definition of Ready (DoR)
- [x] Problem statement is explicit and user impact is clear.
- [x] Scope boundaries (in/out) are explicit.
- [x] Acceptance criteria are testable.
- [x] Dependencies and known risks are listed.

# Companion docs
- Product brief(s): `prod_004_importer_l_export_api_de_l_univers_ogame_du_joueur`
- Architecture decision(s): `adr_006_importer_l_export_api_de_l_univers_ogame_du_joueur`

# Scope boundaries
- In: lecture/export autorisé, adaptateur de format, validation, fixtures anonymisées, import local.
- Out: automatisation de jeu, contournement de sécurité, conservation de secrets, scraping non autorisé ou dépendance à une API communautaire non explicitement choisie.

# Backlog
- `item_002_importer_l_export_api_de_l_univers_ogame_du_joueur`
