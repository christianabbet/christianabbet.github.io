# christianabbet.github.io

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
uv run python scripts/generate_thumbnails.py
```

Reads images from `assets/images/` and writes fixed-size thumbnails to `assets/images_thumbnails/`, which is what the site actually displays.
