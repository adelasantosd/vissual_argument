#!/usr/bin/env python3
"""Genera las tres versiones del sitio (ES, EN, FR) a partir de una sola plantilla.

Uso: python3 build.py  ->  escribe index.html, en/index.html y fr/index.html
Para añadir un ensayo, agrega una entrada a ESSAYS (el primero es la pieza principal) y vuelve a ejecutar.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
SITE = "https://visualargument.org"
PUDDING = '<a href="https://pudding.cool/" target="_blank" rel="noopener">The Pudding</a>'

PERSON = {
    "name": "Adela Santos Domínguez",
    "email": "adela.santos@graduateinstitute.ch",
    "orcid": "https://orcid.org/0009-0009-1480-3668",
    "linkedin": "https://www.linkedin.com/in/adelasantos",
    "linktree": "https://linktr.ee/adela.santos",
    "github": "https://github.com/adelasantosd",
}

ESSAYS = [
    {
        "id": "ghd",
        "url": "https://globalhealthdiplomacy.visualargument.org/",
        "accent": "#2f5d62",
        "motif": "genealogy",
        "lang": "en",
        "doi": "10.5281/zenodo.22127805",
        "code": "https://github.com/adelasantosd/global-health-diplomacy-concept_genealogy",
        "kicker": {"es": "Salud global", "en": "Global health", "fr": "Santé mondiale"},
        "title": {
            "es": "La genealogía de la diplomacia sanitaria global",
            "en": "The Genealogy of Global Health Diplomacy",
            "fr": "La généalogie de la diplomatie de la santé mondiale",
        },
        "dek": {
            "es": "La práctica existió antes que el nombre. Una revisión de 3 395 documentos reconstruye cómo la expresión «diplomacia sanitaria global» llegó a significar lo que hoy significa, y quién quedó fuera del canon.",
            "en": "The practice came before the name. A review of 3,395 documents traces how ‘global health diplomacy’ came to mean what it means today, and who was left out of the canon.",
            "fr": "La pratique a précédé le nom. Une revue de 3 395 documents retrace comment l’expression « diplomatie de la santé mondiale » a pris son sens actuel, et qui est resté en dehors du canon.",
        },
    },
    {
        "id": "fabric",
        "url": "https://fabric.visualargument.org/",
        "accent": "#9b2226",
        "motif": "weave",
        "lang": "en",
        "doi": "10.26443/mjgh.v15i1.1926",
        "code": None,
        "kicker": {"es": "Financiamiento", "en": "Health financing", "fr": "Financement de la santé"},
        "title": {
            "es": "El tejido del financiamiento de la salud global",
            "en": "The Fabric of Global Health Funding",
            "fr": "Le tissu du financement de la santé mondiale",
        },
        "dek": {
            "es": "Nueve años de financiamiento de la OMS leídos como una red, y lo que le ocurre cuando se retira su financiador más influyente.",
            "en": "Nine years of WHO financing read as a network, and what happens to it when its most influential funder walks away.",
            "fr": "Neuf ans de financement de l’OMS lus comme un réseau, et ce qu’il en reste quand son principal bailleur se retire.",
        },
    },
    {
        "id": "cedip",
        "url": "https://cedip-calendario26.visualargument.org/",
        "accent": "#7f1d3a",
        "motif": "timeline",
        "lang": "es",
        "doi": "10.5281/zenodo.24015656",
        "code": "https://github.com/adelasantosd/cedip_calendario-electoral26",
        "kicker": {"es": "Congreso mexicano", "en": "Mexican Congress", "fr": "Congrès mexicain"},
        "title": {
            "es": "Ruta a la LXVII Legislatura",
            "en": "Road to the 67th Legislature",
            "fr": "En route vers la LXVIIe Législature",
        },
        "dek": {
            "es": "La elección federal de 2027, el relevo en la presidencia del INE y la agenda de la Cámara de Diputados, cada fecha con su fundamento legal. Elaborado para el CEDIP; se actualiza los viernes.",
            "en": "Mexico’s 2027 federal election, the change at the head of its electoral institute and the agenda of the Chamber of Deputies, each date with its legal basis. Prepared for CEDIP and updated on Fridays.",
            "fr": "L’élection fédérale de 2027 au Mexique, le renouvellement à la tête de l’institut électoral et l’agenda de la Chambre des députés, chaque date avec son fondement juridique. Réalisé pour le CEDIP, mis à jour le vendredi.",
        },
    },
]

T = {
    "es": {
        "path": "/",
        "tagline": "Ensayos visuales sobre investigación en ciencias sociales",
        "desc": "Ensayos visuales basados en investigación propia en salud global, gobernanza y política parlamentaria.",
        "skip": "Ir al contenido",
        "latest": "Ensayos",
        "by": "Por",
        "read": "Leer el ensayo",
        "in_lang": {"en": "En inglés", "es": "En español"},
        "code": "Datos y código",
        "about_h": "Sobre el proyecto",
        "about": [
            "Vissual Argument publica ensayos visuales basados en investigación propia. Cada pieza parte de un artículo, una base de datos o una revisión sistemática y la convierte en algo que se puede recorrer: una red, una línea de tiempo, el árbol genealógico de una idea.",
            "Lo que la separa de una infografía es el argumento. Hay una tesis, la evidencia que la sostiene y una nota que dice hasta dónde llegan los datos. Los datos y el código quedan publicados para quien quiera revisarlos.",
            f"El proyecto toma ideas del periodismo de datos, en particular de {PUDDING}, y las pone a prueba con preguntas de las ciencias sociales. Es un trabajo en curso. Si encuentra un error o una fuente que falta, escríbame.",
        ],
        "author_h": "La autora",
        "bio": "Investigadora posdoctoral visitante en el Global Health Centre del Geneva Graduate Institute (2025–2026) e Investigadora «A» en el Centro de Estudios de Derecho e Investigaciones Parlamentarias (CEDIP) de la Cámara de Diputados. Estudia la gobernanza de la salud global, el derecho internacional y las redes de financiamiento.",
        "write": "Escribir",
        "ai": "Página diseñada y programada con asistencia de Claude (Anthropic). La investigación y los textos son de la autora.",
    },
    "en": {
        "path": "/en/",
        "tagline": "Visual essays on social science research",
        "desc": "Visual essays built on original research in global health, governance and parliamentary politics.",
        "skip": "Skip to content",
        "latest": "Essays",
        "by": "By",
        "read": "Read the essay",
        "in_lang": {"en": "In English", "es": "In Spanish"},
        "code": "Data and code",
        "about_h": "About the project",
        "about": [
            "Vissual Argument publishes visual essays built on original research. Each piece starts from an article, a dataset or a systematic review and turns it into something a reader can move through: a network, a timeline, the family tree of an idea.",
            "What sets it apart from an infographic is the argument. There is a thesis, the evidence behind it and a note on where the data stop. Data and code are published for anyone who wants to check them.",
            f"The project borrows from data journalism, {PUDDING} in particular, and tries those methods on questions from the social sciences. It is a work in progress. If you spot an error or a missing source, please write.",
        ],
        "author_h": "The author",
        "bio": "Postdoctoral Visiting Fellow at the Global Health Centre, Geneva Graduate Institute (2025–2026), and Researcher «A» at the Centre for Legal and Parliamentary Studies (CEDIP) of the Mexican Chamber of Deputies. Her work covers global health governance, international law and financing networks.",
        "write": "Write",
        "ai": "Page designed and coded with assistance from Claude (Anthropic). The research and writing are the author’s.",
    },
    "fr": {
        "path": "/fr/",
        "tagline": "Essais visuels sur la recherche en sciences sociales",
        "desc": "Essais visuels fondés sur des recherches originales en santé mondiale, gouvernance et vie parlementaire.",
        "skip": "Aller au contenu",
        "latest": "Essais",
        "by": "Par",
        "read": "Lire l’essai",
        "in_lang": {"en": "En anglais", "es": "En espagnol"},
        "code": "Données et code",
        "about_h": "À propos du projet",
        "about": [
            "Vissual Argument publie des essais visuels fondés sur des recherches originales. Chaque pièce part d’un article, d’un jeu de données ou d’une revue systématique et en fait un objet que l’on peut parcourir : un réseau, une chronologie, l’arbre généalogique d’une idée.",
            "Ce qui la distingue d’une infographie, c’est l’argument. Il y a une thèse, les preuves qui la soutiennent et une note qui indique où s’arrêtent les données. Données et code sont publiés pour qui veut les vérifier.",
            f"Le projet emprunte au journalisme de données, en particulier à {PUDDING}, et met ces méthodes à l’épreuve de questions de sciences sociales. C’est un travail en cours. Si vous repérez une erreur ou une source manquante, écrivez-moi.",
        ],
        "author_h": "L’autrice",
        "bio": "Chercheuse postdoctorale invitée au Global Health Centre du Geneva Graduate Institute (2025–2026) et chercheuse « A » au Centre d’études de droit et de recherches parlementaires (CEDIP) de la Chambre des députés du Mexique. Ses travaux portent sur la gouvernance de la santé mondiale, le droit international et les réseaux de financement.",
        "write": "Écrire",
        "ai": "Page conçue et programmée avec l’aide de Claude (Anthropic). La recherche et les textes sont de l’autrice.",
    },
}

MOTIFS = {
    "genealogy": '<svg viewBox="0 0 240 150" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round">'
                 '<path d="M14 130 C60 130 70 80 110 80 S170 40 226 34"/><path d="M110 80 C150 80 170 102 226 110"/>'
                 '<path d="M62 120 C90 112 96 136 130 136"/><path d="M160 60 C180 68 196 78 226 72"/><path d="M190 104 C205 92 214 96 226 92"/></g>'
                 '<g fill="currentColor"><circle cx="14" cy="130" r="4.5"/><circle cx="110" cy="80" r="4.5"/><circle cx="226" cy="34" r="4"/>'
                 '<circle cx="226" cy="110" r="4"/><circle cx="130" cy="136" r="3.5"/><circle cx="226" cy="72" r="3.5"/><circle cx="160" cy="60" r="3"/><circle cx="226" cy="92" r="3"/></g></svg>',
    "weave": '<svg viewBox="0 0 240 150" aria-hidden="true"><g stroke="currentColor" stroke-width="1.2" fill="none">'
             + "".join(f'<path d="M{x} 10 L{x} 140" opacity="{0.3 + (i % 3) * 0.2:.2f}"/>' for i, x in enumerate(range(16, 232, 14)))
             + "".join(f'<path d="M8 {y} C80 {y - 4} 160 {y + 4} 232 {y}" opacity="{0.35 + (i % 2) * 0.35:.2f}"/>' for i, y in enumerate(range(20, 140, 13)))
             + '<path d="M150 84 C172 100 192 120 218 148" stroke-width="2.2"/></g></svg>',
    "timeline": '<svg viewBox="0 0 240 150" aria-hidden="true"><path d="M120 6 V144" stroke="currentColor" stroke-width="1.6"/>'
                '<g stroke="currentColor" stroke-width="1"><path d="M120 26 H86"/><path d="M120 56 H160"/><path d="M120 86 H70"/><path d="M120 116 H176"/></g>'
                '<g><rect x="30" y="20" width="56" height="12" rx="1" fill="#3f7d54"/><rect x="160" y="50" width="58" height="12" rx="1" fill="#7f1d3a"/>'
                '<rect x="20" y="80" width="50" height="12" rx="1" fill="#3d6b9e"/><rect x="176" y="110" width="44" height="12" rx="1" fill="#8a6413"/></g>'
                '<g fill="#fbfaf7" stroke="currentColor" stroke-width="1.6"><circle cx="120" cy="26" r="4.5"/><circle cx="120" cy="56" r="4.5"/><circle cx="120" cy="86" r="4.5"/><circle cx="120" cy="116" r="4.5"/></g></svg>',
}


def meta(e, lang, t):
    code = f' · <a href="{e["code"]}" target="_blank" rel="noopener">{t["code"]}</a>' if e["code"] else ""
    return (f'<p class="meta"><span>{t["by"]} {PERSON["name"]}</span><span>{t["in_lang"][e["lang"]]}</span>'
            f'<span>DOI <a href="https://doi.org/{e["doi"]}" target="_blank" rel="noopener">{e["doi"]}</a>{code}</span></p>')


def lead(e, lang, t):
    return f'''
  <article class="lead" style="--accent:{e["accent"]}">
    <div class="lead-text">
      <p class="kicker">{escape(e["kicker"][lang])}</p>
      <h2 class="headline"><a href="{e["url"]}" hreflang="{e["lang"]}">{escape(e["title"][lang])}</a></h2>
      <p class="dek">{escape(e["dek"][lang])}</p>
      {meta(e, lang, t)}
      <a class="read" href="{e["url"]}" hreflang="{e["lang"]}">{t["read"]}</a>
    </div>
    <a class="lead-art" href="{e["url"]}" tabindex="-1" aria-hidden="true">{MOTIFS[e["motif"]]}</a>
  </article>'''


def secondary(e, lang, t):
    return f'''
    <article class="story" style="--accent:{e["accent"]}">
      <a class="story-art" href="{e["url"]}" tabindex="-1" aria-hidden="true">{MOTIFS[e["motif"]]}</a>
      <p class="kicker">{escape(e["kicker"][lang])}</p>
      <h3 class="headline"><a href="{e["url"]}" hreflang="{e["lang"]}">{escape(e["title"][lang])}</a></h3>
      <p class="dek">{escape(e["dek"][lang])}</p>
      {meta(e, lang, t)}
    </article>'''


def page(lang):
    t = T[lang]
    pr = PERSON
    alt = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{T[l]["path"]}">' for l in T)
    switch = "".join(
        f'<a href="{T[l]["path"]}" lang="{l}" hreflang="{l}"{" aria-current=\"page\"" if l == lang else ""}>{l.upper()}</a>' for l in T
    )
    about = "".join(f"<p>{x}</p>" for x in t["about"])  # texto propio, contiene el enlace a The Pudding
    rest = "".join(secondary(e, lang, t) for e in ESSAYS[1:])
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Vissual Argument · {escape(t["tagline"])}</title>
<meta name="description" content="{escape(t["desc"])}">
<meta name="author" content="{pr["name"]}">
<link rel="canonical" href="{SITE}{t["path"]}">
{alt}
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta property="og:title" content="Vissual Argument">
<meta property="og:description" content="{escape(t["desc"])}">
<meta property="og:url" content="{SITE}{t["path"]}">
<meta property="og:type" content="website">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/source-serif-4-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<a class="skip" href="#main">{t["skip"]}</a>

<header class="masthead">
  <div class="wrap bar">
    <span class="edition">{escape(t["tagline"])}</span>
    <nav class="langs" aria-label="Idioma · Language · Langue">{switch}</nav>
  </div>
  <div class="wrap brand-row">
    <a class="wordmark" href="{t["path"]}">Vissual Argument</a>
  </div>
</header>

<main id="main" class="wrap">
  <h1 class="sr-only">Vissual Argument</h1>
  {lead(ESSAYS[0], lang, t)}

  <section class="more" aria-label="{escape(t["latest"])}">{rest}
  </section>

  <section class="about" id="about" aria-labelledby="about-h">
    <div class="about-text">
      <h2 class="section-h" id="about-h">{escape(t["about_h"])}</h2>
      {about}
    </div>
    <aside class="author" aria-labelledby="author-h">
      <h2 class="section-h" id="author-h">{escape(t["author_h"])}</h2>
      <p class="author-name">{pr["name"]}</p>
      <p class="bio">{escape(t["bio"])}</p>
      <ul class="links">
        <li><a href="{pr["orcid"]}" rel="me noopener" target="_blank">ORCID</a></li>
        <li><a href="{pr["linkedin"]}" rel="me noopener" target="_blank">LinkedIn</a></li>
        <li><a href="{pr["github"]}" rel="me noopener" target="_blank">GitHub</a></li>
        <li><a href="{pr["linktree"]}" rel="me noopener" target="_blank">Linktree</a></li>
        <li><a href="mailto:{pr["email"]}">{t["write"]}</a></li>
      </ul>
    </aside>
  </section>
</main>

<footer class="foot">
  <div class="wrap">
    <p class="foot-mark">Vissual Argument</p>
    <p>© 2026 {pr["name"]}</p>
    <p class="ai">{escape(t["ai"])}</p>
  </div>
</footer>
</body>
</html>
'''


if __name__ == "__main__":
    for lang, t in T.items():
        out = ROOT / "index.html" if t["path"] == "/" else ROOT / t["path"].strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang), encoding="utf-8")
        print("escrito", out.relative_to(ROOT))
