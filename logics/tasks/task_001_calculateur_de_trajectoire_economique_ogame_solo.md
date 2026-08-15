## task_001_calculateur_de_trajectoire_economique_ogame_solo - Calculateur de trajectoire economique OGame solo
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
- Summary: Plan d'implémentation du MVP de calcul de trajectoires économiques OGame.
- Keywords: domaine, simulation, beam search, import, UI, tests
- Use when: Démarrer le développement du MVP.
- Skip when: L'export de compte n'a pas encore été caractérisé et qu'un connecteur réel est requis.

# Definition of Done (DoD)
- [ ] Le modèle économique et les scénarios de référence sont implémentés.
- [ ] La simulation produit des états et événements cohérents jusqu'aux trois horizons.
- [ ] La recherche génère des plans faisables et explique le score de chacun.
- [ ] L'interface permet saisie/import, paramétrage et comparaison des résultats.
- [ ] Les tests unitaires, d'intégration et de non-régression passent.
- [ ] Meaningful waves followed ADR 009: affected docs updated and the repo left commit-ready without automatic commits.

# Backlog
- `item_001_calculateur_de_trajectoire_economique_ogame_solo`

# Acceptance criteria
- AC1: Le modèle de domaine calcule coûts, production, énergie, prérequis et temps de construction pour les règles configurées.
- AC2: Un optimiseur retourne pour chaque horizon un plan faisable, déterministe et expliqué, avec un budget de calcul contrôlé.
- AC3: L'utilisateur charge ou saisit un état de compte, corrige les données incomplètes, puis compare les projections 10/30/90 jours.
- AC4: Des tests de scénarios couvrent le calcul de production, la faisabilité et l'absence de régression de l'optimisation.

# Plan
- [ ] Établir les règles versionnées et fixtures de comptes fictifs, puis tester coûts et production.
- [ ] Construire le simulateur à événements qui attend les ressources, déclenche les constructions et met à jour l'empire.
- [ ] Implémenter une recherche faisable à largeur bornée (beam search) avec score de production cumulée pondérée.
- [ ] Ajouter le parseur d'export local avec schéma, erreurs actionnables et adaptateur isolé du domaine.
- [ ] Construire la vue de saisie/import et les tableaux/timelines de comparaison 10/30/90 jours.
- [ ] Vérifier performance, reproductibilité et validation de toutes les entrées.

# Validation
- Tests unitaires de formules et prérequis ; tests de simulation de planètes ; fixtures d'import ; tests de propriétés (jamais de ressources négatives ni construction incompatible) ; scénario end-to-end multi-planètes.

# Report
- Not started.

# Links
- Request: `req_000_calculateur_de_trajectoire_economique_ogame_solo`
- Product brief(s): `prod_002_calculateur_de_trajectoire_economique_ogame_solo`
- Architecture decision(s): `adr_003_calculateur_de_trajectoire_economique_ogame_solo`
