# Infos for MkDocs

## Requirements

```bash
pip3 install -r requirements.txt
```

Start with `mkdocs serve` and open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Deploy a single-site

```bash
mkdocs build
cd site
htmlark print_page/index.html -o standalone.html
```

Open `standalone.html` in your browser.

## Run in Docker

```bash
docker run --rm -it -p 8000:8000 -v $(pwd):/docs squidfunk/mkdocs-material
```
