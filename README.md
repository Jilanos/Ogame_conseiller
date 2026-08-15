# OGame Conseiller

Un calculateur local de trajectoires économiques pour un empire OGame solo orienté mines.

Le MVP vise des recommandations explicables pour maximiser la production cumulée de métal, cristal et deutérium à 10, 30 et 90 jours. Il partira d'une saisie manuelle ou d'un export de données du compte, sans automatiser d'action dans le jeu.

Le cadrage produit, les choix d'architecture et le plan de développement sont dans le [corpus Logics](logics/INDEX.md).

## Essai local

```bash
python3 -m pytest -q
PYTHONPATH=src python3 -m ogame_conseiller.cli examples/empire.json
```

L'import MVP est un JSON normalisé (voir [examples/empire.json](examples/empire.json)). Il produit un résultat JSON avec la production de référence, la production projetée, le gain par ressource et les constructions recommandées pour chaque horizon.

## Limites du MVP

- Pas de bot ni d'action automatisée dans OGame.
- Pas de stratégie militaire ou de commerce.
- Les règles et bonus d'univers sont paramétrables et versionnés ; les bonus non gérés doivent être signalés.
