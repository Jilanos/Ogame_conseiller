## item_001_calculateur_de_trajectoire_economique_ogame_solo - Calculateur de trajectoire economique OGame solo
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
- Summary: Livraison MVP complète du conseiller économique : modèle, simulateur, optimiseur, import et restitution.
- Keywords: simulation événementielle, branchement, mines, énergie, import, multi-planètes
- Use when: Découper et implémenter le MVP OGame Conseiller.
- Skip when: Traiter une évolution militaire ou un connecteur non validé.

# Problem
Un joueur mineur ne peut pas estimer simplement l'enchaînement de constructions qui produit le plus de ressources sur une échéance donnée, particulièrement sur plusieurs planètes.

# Scope
- In:
  - noyau de règles économique configurable et testable
  - simulation discrète à événements des ressources, constructions, énergie et prérequis
  - recherche de plans candidats pour 10, 30 et 90 jours
  - saisie manuelle, import de fichier d'export et présentation des résultats
- Out:
  - automatisation d'OGame et fonctions militaires
  - validation d'un connecteur réseau avant documentation du format d'export officiel

# Acceptance criteria
- AC1: Le modèle de domaine calcule coûts, production, énergie, prérequis et temps de construction pour les règles configurées.
- AC2: Un optimiseur retourne pour chaque horizon un plan faisable, déterministe et expliqué, avec un budget de calcul contrôlé.
- AC3: L'utilisateur charge ou saisit un état de compte, corrige les données incomplètes, puis compare les projections 10/30/90 jours.
- AC4: Des tests de scénarios couvrent le calcul de production, la faisabilité et l'absence de régression de l'optimisation.

# AC Traceability
- request-AC1 -> Backlog-AC3. Proof: l'état importé ou saisi comprend l'empire et ses paramètres exploitables.
- request-AC2 -> Backlog-AC2. Proof: l'optimiseur produit un plan pour les trois horizons et sa comparaison de référence.
- request-AC3 -> Backlog-AC2. Proof: le plan expose coûts, instants et impacts de production.
- request-AC4 -> Backlog-AC4. Proof: les scénarios de référence et le résultat déterministe sont testés.
- request-AC5 -> Backlog-AC1 et Backlog-AC2. Proof: le moteur de domaine et le simulateur ne proposent que des actions faisables.

# Decision framing
- Product framing: `prod_002_calculateur_de_trajectoire_economique_ogame_solo` définit la valeur utilisateur et les limites.
- Architecture framing: `adr_003_calculateur_de_trajectoire_economique_ogame_solo` fixe simulation pure et import adaptateur.

# Links
- Product brief(s): `prod_002_calculateur_de_trajectoire_economique_ogame_solo`
- Architecture decision(s): `adr_003_calculateur_de_trajectoire_economique_ogame_solo`
- Request: `logics/request/req_000_calculateur_de_trajectoire_economique_ogame_solo.md`
- Primary task(s): (none yet)

# Priority
- Priority: High
- Rationale: C'est le premier incrément qui rend le produit utilisable et qui valide toutes les hypothèses de valeur.

# Notes
- Découpage recommandé : (1) modèle et tests, (2) simulateur, (3) recherche de trajectoire, (4) import/validation, (5) interface et comparaison.

# Tasks
- `task_001_calculateur_de_trajectoire_economique_ogame_solo`
