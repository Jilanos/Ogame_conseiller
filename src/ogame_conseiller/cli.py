from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from .importer import load_empire
from .optimizer import optimize


def main() -> int:
    parser = argparse.ArgumentParser(description="Projette et optimise la production économique d'un empire OGame.")
    parser.add_argument("export", help="Chemin vers un export JSON au format MVP")
    parser.add_argument("--beam-width", type=int, default=12)
    parser.add_argument("--max-actions", type=int, default=14)
    args = parser.parse_args()
    try:
        empire = load_empire(args.export)
        results = [optimize(empire, days, beam_width=args.beam_width, max_actions=args.max_actions) for days in (10, 30, 90)]
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps([asdict(result) for result in results], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
