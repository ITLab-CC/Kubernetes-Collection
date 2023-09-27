# Infos for MkDocs

## Requirements

```bash
pip3 install -r requirements.txt
```

Start with `mkdocs serve` and open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Info

> The Docs are automatically deployed via GitHub Actions to GitHub Pages.

## Deploy a single-site

```bash
mkdocs build
cd site
htmlark print_page/index.html -o standalone.html
```

Open `standalone.html` in your browser.
