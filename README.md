# OGame Conseiller

Un calculateur local qui recommande quelles mines construire en priorité dans OGame.

## Problème résolu

Un joueur solo orienté mines doit choisir, planète par planète, quoi améliorer et dans quel ordre. L'outil lit l'état d'un empire et propose une suite de constructions pour maximiser la production cumulée de métal, de cristal et de deutérium à 10, 30 et 90 jours. Il ne joue pas à la place du joueur : aucune action n'est automatisée dans le jeu.

## Fonctionnalités

- Import d'un empire au format JSON normalisé (voir [examples/empire.json](examples/empire.json)).
- Modèle économique : mines de métal, de cristal et de deutérium, centrale solaire, stockage, fenêtres d'indisponibilité.
- Optimiseur par recherche en faisceau (`--beam-width`, `--max-actions`) qui attend les ressources avant de planifier une amélioration.
- Sortie JSON par horizon : production de référence, production projetée, gain par ressource, constructions recommandées avec coûts, heures de début et de fin.
- Pondération des ressources et vitesse d'économie de l'univers paramétrables.

## Démarrage rapide

Python 3.11 ou plus récent.

```bash
python3 -m venv .venv
.venv/bin/pip install -e . pytest
.venv/bin/python -m pytest -q
.venv/bin/ogame-conseiller examples/empire.json
```

## Stack

Python (bibliothèque standard uniquement), pytest pour les tests, setuptools pour le packaging.

## État

Prototype (v0.1.0), 14 tests verts. La saisie se fait par un JSON écrit à la main. L'import d'un export de compte est spécifié dans le [corpus Logics](logics/INDEX.md) mais pas encore implémenté.

## Limites

- Pas de bot ni d'action automatisée dans OGame.
- Pas de stratégie militaire ni de commerce.
- Les règles et bonus d'univers sont paramétrables ; les bonus non gérés doivent être signalés.

Le cadrage produit, l'architecture et le plan de développement sont dans le [corpus Logics](logics/INDEX.md).
