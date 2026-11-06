# Vissual Argument

Hub site for **Vissual Argument**, an author-led practice for communicating complex research through interactive visual forms, with the evidence and limits of each argument in view.

- **Live site:** <https://visualargument.org> (Spanish), `/en/` (English), `/fr/` (French)
- **Author:** Adela Santos Domínguez · [ORCID 0000-0002-8691-0544](https://orcid.org/0000-0002-8691-0544)

## Structure

```
.
├── build.py            Generates the three language versions from one template
├── index.html          Spanish (generated)
├── en/index.html       English (generated)
├── fr/index.html       French (generated)
├── assets/
│   ├── site.css        Shared visual identity of the series
│   ├── favicon.svg
│   └── fonts/          Self-hosted typefaces (WOFF2) and their SIL OFL licences
└── vercel.json
```

## Adding a visual argument

1. Add an entry to `PROJECTS` in `build.py` (URL, colour, motif, DOI and the question it answers in ES, EN and FR).
2. Run `python3 build.py`.
3. Commit the regenerated HTML files.

The site is static: no dependencies, no build step on Vercel, and no requests to third parties.

## Current arguments

| Argument | Subdomain | Language |
|---|---|---|
| The Genealogy of Global Health Diplomacy | `globalhealthdiplomacy.visualargument.org` | English |
| The Fabric of Global Health Funding | `fabric.visualargument.org` | English |
| Ruta a la LXVII Legislatura | `cedip-calendario26.visualargument.org` | Spanish |
