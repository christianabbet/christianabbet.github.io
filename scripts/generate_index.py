"""Generate birds.json from a wingspan-swiss-unofficial cards.json file."""

import argparse
import json
from pathlib import Path


def to_birds(cards: list) -> list:
    """Convert cards to bird entries, sorted by vogelwarte id with 1-based ids.

    Args:
        cards (list): entries of cards.json, each holding a "bird" dict.

    Returns:
        list: bird dicts with id, name (fr/en), vogelwarte_id and location.
    """
    birds = sorted((c["bird"] for c in cards), key=lambda b: b["bird_id"])
    return [
        {
            "id": i,
            "name": {"fr": b["name"]["fr"], "en": b["name"]["en"]},
            "vogelwarte_id": b["bird_id"],
            "location": [k.removeprefix("loc_") for k, v in b["loc"].items() if v],
        }
        for i, b in enumerate(birds, start=1)
    ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True, help="path to cards.json")
    parser.add_argument("--output", type=Path, required=True, help="path to birds.json")
    args = parser.parse_args()
    cards = json.loads(args.input.read_text(encoding="utf-8"))
    birds = to_birds(cards)
    out = json.dumps(birds, ensure_ascii=False, indent=2) + "\n"
    args.output.write_text(out, encoding="utf-8")
    print(f"Wrote {len(birds)} birds to {args.output}")
