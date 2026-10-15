# Swiss BirdDex

Website: https://christianabbet.github.io

## Run locally

`fetch` requires a server, so opening `index.html` directly won't load the data.

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000 in your browser.

## Thumbnail generation

Uses [uv](https://docs.astral.sh/uv/) to manage the Python environment.

```bash
uv sync
uv run python scripts/generate_index.py --input path/to/cards.json
uv run python scripts/generate_thumbnails.py --input assets/images
```
