from __future__ import annotations

import json
from pathlib import Path

from .domain import Empire


def load_empire(path: str | Path) -> Empire:
    """Charge le format MVP normalisé ; un adaptateur OGame officiel pourra le remplacer."""
    try:
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Export JSON invalide : {exc}") from exc
    except OSError as exc:
        raise ValueError(f"Impossible de lire l'export : {exc}") from exc
    if not isinstance(raw, dict):
        raise ValueError("L'export doit être un objet JSON")
    return Empire.from_dict(raw)
