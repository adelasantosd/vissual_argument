#!/usr/bin/env python3
"""Genera las tres versiones del sitio (ES, EN, FR) a partir de una sola plantilla.

Uso: python3 build.py  ->  escribe index.html, en/index.html y fr/index.html
Para añadir un argumento visual, agrega una entrada a PROJECTS y vuelve a ejecutar.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
SITE = "https://visualargument.org"

PERSON = {
    "name": "Adela Santos Domínguez",
    "email": "adela.santos@graduateinstitute.ch",
    "orcid": "https://orcid.org/0009-0009-1480-3668",
    "linkedin": "https://www.linkedin.com/in/adelasantos",
    "linktree": "https://linktr.ee/adela.santos",
    "github": "https://github.com/adelasantosd",
}

# Cada argumento conserva su propia identidad: color, motivo y tono.
PROJECTS = [
    {
        "id": "ghd",
        "url": "https://globalhealthdiplomacy.visualargument.org/",
        "accent": "#2f5d62",
        "tint": "#e8efee",
        "motif": "genealogy",
        "lang": "EN",
        "doi": "10.5281/zenodo.22127805",
        "code": "https://github.com/adelasantosd/global-health-diplomacy-concept_genealogy",
        "title": {
            "es": "La genealogía de la diplomacia sanitaria global",
            "en": "The Genealogy of Global Health Diplomacy",
            "fr": "La généalogie de la diplomatie de la santé mondiale",
        },
        "question": {
            "es": "¿Cómo adquirió su significado la expresión «diplomacia sanitaria global»?",
            "en": "How did the term ‘global health diplomacy’ acquire its meaning?",
            "fr": "Comment l’expression « diplomatie de la santé mondiale » a-t-elle acquis son sens ?",
        },
        "kind": {"es": "Genealogía conceptual", "en": "Concept genealogy", "fr": "Généalogie conceptuelle"},
        "facts": {
            "es": ["Revisión sistemática de 3 395 documentos", "60 nodos y 65 relaciones con fuente", "1974–2025"],
            "en": ["Systematic review of 3,395 documents", "60 nodes and 65 sourced edges", "1974–2025"],
            "fr": ["Revue systématique de 3 395 documents", "60 nœuds et 65 liens sourcés", "1974–2025"],
        },
    },
    {
        "id": "fabric",
        "url": "https://fabric.visualargument.org/",
        "accent": "#9b2226",
        "tint": "#f6e9e6",
        "motif": "weave",
        "lang": "EN",
        "doi": "10.26443/mjgh.v15i1.1926",
        "code": None,
        "title": {
            "es": "El tejido del financiamiento de la salud global",
            "en": "The Fabric of Global Health Funding",
            "fr": "Le tissu du financement de la santé mondiale",
        },
        "question": {
            "es": "¿Se sostiene la red que financia a la OMS cuando se retira su actor más influyente?",
            "en": "Does the network that funds WHO hold together when its most consequential actor leaves?",
            "fr": "Le réseau qui finance l’OMS tient-il lorsque son acteur le plus déterminant se retire ?",
        },
        "kind": {"es": "Ensayo visual de datos", "en": "Visual data essay", "fr": "Essai visuel de données"},
        "facts": {
            "es": ["Datos de financiamiento de la OMS", "Análisis de redes, 2016–2025", "Basado en un artículo con revisión por pares"],
            "en": ["WHO financing data", "Network analysis, 2016–2025", "Based on a peer-reviewed article"],
            "fr": ["Données de financement de l’OMS", "Analyse de réseaux, 2016–2025", "Fondé sur un article évalué par les pairs"],
        },
    },
    {
        "id": "cedip",
        "url": "https://cedip-calendario26.visualargument.org/",
        "accent": "#7f1d3a",
        "tint": "#f4e8ec",
        "motif": "timeline",
        "lang": "ES",
        "doi": "10.5281/zenodo.24015656",
        "code": "https://github.com/adelasantosd/cedip_calendario-electoral26",
        "title": {
            "es": "Ruta a la LXVII Legislatura",
            "en": "Road to the 67th Legislature",
            "fr": "En route vers la LXVIIe Législature",
        },
        "question": {
            "es": "¿Qué fechas llevan a la nueva Cámara de Diputados de México, y qué ley fija cada una?",
            "en": "Which dates lead to Mexico’s new Chamber of Deputies, and which law sets each one?",
            "fr": "Quelles échéances mènent à la nouvelle Chambre des députés du Mexique, et quelle loi fixe chacune d’elles ?",
        },
        "kind": {"es": "Calendario interactivo", "en": "Interactive calendar", "fr": "Calendrier interactif"},
        "facts": {
            "es": ["Elaborado para el CEDIP, Cámara de Diputados", "Elección 2027, INE y Congreso", "Se actualiza cada viernes"],
            "en": ["Prepared for CEDIP, Chamber of Deputies", "2027 election, INE and Congress", "Updated every Friday"],
            "fr": ["Réalisé pour le CEDIP, Chambre des députés", "Élection de 2027, INE et Congrès", "Mis à jour chaque vendredi"],
        },
    },
]

T = {
    "es": {
        "path": "/", "label": "Español",
        "title": "Vissual Argument",
        "desc": "Una práctica para comunicar investigación compleja mediante formas visuales interactivas, con su evidencia y sus límites a la vista.",
        "skip": "Ir al contenido",
        "nav": ["Qué es", "Argumentos", "Origen", "Autora"],
        "kicker": "Divulgación científica · Ciencias sociales",
        "lede": "Investigación compleja contada para más personas, con su evidencia y sus límites a la vista.",
        "what_h": "Qué es un argumento visual",
        "what_p": "Un argumento visual cuenta una investigación como una historia: parte de una pregunta, propone una respuesta y muestra la evidencia que la sostiene. Usa analogías y formas cotidianas para hacer legible lo complejo, sin ocultar lo que los datos no permiten afirmar.",
        "cmp": [
            ("Infografía", "Resume hechos para consultarlos de un vistazo."),
            ("Visualización de datos", "Muestra patrones en los datos; la interpretación queda en manos de quien la lee."),
            ("Argumento visual", "Sostiene una afirmación, enseña su evidencia y declara sus límites. Publica datos y métodos para que otras personas puedan revisarlo."),
        ],
        "projects_h": "Argumentos",
        "projects_p": "Cada argumento tiene su propia identidad, de acuerdo con su tema y su público.",
        "open": "Abrir", "lang_of": "Idioma", "langs": {"EN": "inglés", "ES": "español"}, "data": "DOI", "code": "Código",
        "origin_h": "Origen",
        "origin": [
            "Vissual Argument es una práctica en evolución, dirigida por su autora, para comunicar investigación compleja mediante formas visuales interactivas. Pone a la vista la evidencia y los límites de un argumento para lectores más allá de su público especializado habitual.",
            "Se inspira en la narración visual explicativa basada en datos, como el trabajo de The Pudding, y explora cómo ese enfoque puede servir a la investigación conceptual y empírica en ciencias sociales. Es un esfuerzo exploratorio.",
            "Parte de una convicción: la ciencia debe ser abierta. Contar un debate académico con una historia, una analogía o un objeto conocido permite que más personas lo lean, lo discutan y lo cuestionen.",
        ],
        "contrib_h": "Sugerencias y contribuciones",
        "contrib_p": "Las sugerencias y contribuciones documentadas son bienvenidas. Cada argumento enlaza sus datos y, cuando existe, su repositorio, donde pueden abrirse propuestas y correcciones.",
        "about_h": "Autora",
        "roles": [
            "Investigadora posdoctoral visitante, Global Health Centre, Geneva Graduate Institute (2025–2026)",
            "Investigadora «A», Centro de Estudios de Derecho e Investigaciones Parlamentarias (CEDIP), Cámara de Diputados",
        ],
        "links_h": "Enlaces",
        "ai": "Se utilizó Claude (Anthropic) como herramienta de asistencia para el diseño y la programación de esta página. La investigación, los contenidos y las decisiones editoriales son de la autora.",
    },
    "en": {
        "path": "/en/", "label": "English",
        "title": "Vissual Argument",
        "desc": "A practice for communicating complex research through interactive visual forms, with its evidence and limits in view.",
        "skip": "Skip to content",
        "nav": ["What it is", "Arguments", "Origin", "Author"],
        "kicker": "Science communication · Social sciences",
        "lede": "Complex research told for more readers, with its evidence and its limits in view.",
        "what_h": "What a visual argument is",
        "what_p": "A visual argument tells a piece of research as a story: it starts from a question, proposes an answer and shows the evidence behind it. It uses analogies and familiar forms to make complex work legible, without hiding what the data cannot support.",
        "cmp": [
            ("Infographic", "Summarises facts to be read at a glance."),
            ("Data visualisation", "Shows patterns in data and leaves the interpretation to the reader."),
            ("Visual argument", "Makes a claim, shows its evidence and states its limits. Data and methods are published so that others can check it."),
        ],
        "projects_h": "Arguments",
        "projects_p": "Each argument keeps its own identity, suited to its subject and its readers.",
        "open": "Open", "lang_of": "Language", "langs": {"EN": "English", "ES": "Spanish"}, "data": "DOI", "code": "Code",
        "origin_h": "Origin",
        "origin": [
            "Vissual Argument is an author-led, evolving practice for communicating complex research through interactive visual forms. It brings an argument’s evidence and limits into view for readers beyond its usual specialist audience.",
            "It draws on data-led explanatory visual storytelling, including work such as The Pudding, and explores how that approach may inform conceptual and empirical research in the social sciences. It is an exploratory effort.",
            "It starts from a conviction: science should be open. Telling an academic debate through a story, an analogy or a familiar object lets more people read it, discuss it and question it.",
        ],
        "contrib_h": "Suggestions and contributions",
        "contrib_p": "Documented suggestions and contributions are welcome. Each argument links its data and, where one exists, its repository, where proposals and corrections can be opened.",
        "about_h": "Author",
        "roles": [
            "Postdoctoral Visiting Fellow, Global Health Centre, Geneva Graduate Institute (2025–2026)",
            "Researcher «A», Centre for Legal and Parliamentary Studies (CEDIP), Mexican Chamber of Deputies",
        ],
        "links_h": "Links",
        "ai": "Claude (Anthropic) was used as an assistive tool for the design and coding of this page. The research, content and editorial decisions are the author’s.",
    },
    "fr": {
        "path": "/fr/", "label": "Français",
        "title": "Vissual Argument",
        "desc": "Une pratique pour communiquer une recherche complexe au moyen de formes visuelles interactives, en rendant visibles ses preuves et ses limites.",
        "skip": "Aller au contenu",
        "nav": ["Définition", "Arguments", "Origine", "Autrice"],
        "kicker": "Médiation scientifique · Sciences sociales",
        "lede": "Une recherche complexe racontée pour un public plus large, avec ses preuves et ses limites en vue.",
        "what_h": "Qu’est-ce qu’un argument visuel ?",
        "what_p": "Un argument visuel raconte une recherche comme une histoire : il part d’une question, propose une réponse et montre les preuves qui la soutiennent. Il recourt à des analogies et à des formes familières pour rendre lisible ce qui est complexe, sans dissimuler ce que les données ne permettent pas d’affirmer.",
        "cmp": [
            ("Infographie", "Résume des faits à saisir d’un coup d’œil."),
            ("Visualisation de données", "Montre des tendances dans les données et laisse l’interprétation au lecteur ou à la lectrice."),
            ("Argument visuel", "Défend une affirmation, en montre les preuves et en déclare les limites. Données et méthodes sont publiées pour que d’autres puissent le vérifier."),
        ],
        "projects_h": "Arguments",
        "projects_p": "Chaque argument garde sa propre identité, adaptée à son sujet et à son public.",
        "open": "Ouvrir", "lang_of": "Langue", "langs": {"EN": "anglais", "ES": "espagnol"}, "data": "DOI", "code": "Code",
        "origin_h": "Origine",
        "origin": [
            "Vissual Argument est une pratique évolutive, menée par son autrice, pour communiquer une recherche complexe au moyen de formes visuelles interactives. Elle rend visibles les preuves et les limites d’un argument pour un public qui dépasse les seuls spécialistes.",
            "Elle s’inspire de la narration visuelle explicative fondée sur les données, notamment des travaux de The Pudding, et explore la manière dont cette approche peut nourrir la recherche conceptuelle et empirique en sciences sociales. C’est une démarche exploratoire.",
            "Elle part d’une conviction : la science doit être ouverte. Raconter un débat académique au moyen d’une histoire, d’une analogie ou d’un objet familier permet à davantage de personnes de le lire, d’en discuter et de le remettre en question.",
        ],
        "contrib_h": "Suggestions et contributions",
        "contrib_p": "Les suggestions et contributions documentées sont les bienvenues. Chaque argument renvoie à ses données et, le cas échéant, à son dépôt, où l’on peut proposer des ajouts et des corrections.",
        "about_h": "Autrice",
        "roles": [
            "Chercheuse postdoctorale invitée, Global Health Centre, Geneva Graduate Institute (2025–2026)",
            "Chercheuse « A », Centre d’études de droit et de recherches parlementaires (CEDIP), Chambre des députés du Mexique",
        ],
        "links_h": "Liens",
        "ai": "Claude (Anthropic) a été utilisé comme outil d’assistance pour la conception et la programmation de cette page. La recherche, les contenus et les choix éditoriaux relèvent de l’autrice.",
    },
}

MOTIFS = {
    # Genealogía: un tronco que se ramifica
    "genealogy": '<svg viewBox="0 0 240 120" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round">'
                 '<path d="M14 100 C60 100 70 60 110 60 S170 30 226 26"/><path d="M110 60 C150 60 170 78 226 84"/>'
                 '<path d="M62 92 C90 86 96 104 130 104"/><path d="M160 46 C180 52 196 60 226 56"/></g>'
                 '<g fill="currentColor"><circle cx="14" cy="100" r="4.5"/><circle cx="110" cy="60" r="4.5"/><circle cx="226" cy="26" r="4"/>'
                 '<circle cx="226" cy="84" r="4"/><circle cx="130" cy="104" r="3.5"/><circle cx="226" cy="56" r="3.5"/><circle cx="160" cy="46" r="3"/></g></svg>',
    # Tejido: hilos que se cruzan y uno que se suelta
    "weave": '<svg viewBox="0 0 240 120" aria-hidden="true"><g stroke="currentColor" stroke-width="1.4" fill="none">'
             + "".join(f'<path d="M{x} 8 L{x} 112" opacity="{0.35 + (i % 3) * 0.2:.2f}"/>' for i, x in enumerate(range(16, 232, 18)))
             + "".join(f'<path d="M8 {y} C80 {y - 4} 160 {y + 4} 232 {y}" opacity="{0.4 + (i % 2) * 0.3:.2f}"/>' for i, y in enumerate(range(18, 112, 16)))
             + '<path d="M150 66 C170 80 190 96 214 116" stroke-width="2.2"/></g></svg>',
    # Línea de tiempo: eje con fechas a ambos lados
    "timeline": '<svg viewBox="0 0 240 120" aria-hidden="true"><path d="M120 6 V114" stroke="currentColor" stroke-width="2"/>'
                '<g stroke="currentColor" stroke-width="1.2"><path d="M120 24 H86"/><path d="M120 50 H160"/><path d="M120 76 H70"/><path d="M120 98 H176"/></g>'
                '<g><rect x="30" y="17" width="56" height="14" rx="2" fill="#3f7d54"/><rect x="160" y="43" width="58" height="14" rx="2" fill="#7f1d3a"/>'
                '<rect x="20" y="69" width="50" height="14" rx="2" fill="#3d6b9e"/><rect x="176" y="91" width="44" height="14" rx="2" fill="#8a6413"/></g>'
                '<g fill="#fffefb" stroke="currentColor" stroke-width="2"><circle cx="120" cy="24" r="5"/><circle cx="120" cy="50" r="5"/><circle cx="120" cy="76" r="5"/><circle cx="120" cy="98" r="5"/></g></svg>',
}



def card(p, lang, t):
    facts = "".join(f"<li>{escape(f)}</li>" for f in p["facts"][lang])
    code = f' · <a href="{p["code"]}" target="_blank" rel="noopener">{t["code"]}</a>' if p["code"] else ""
    return f'''
    <article class="arg arg-{p["id"]}" style="--accent:{p["accent"]};--tint:{p["tint"]}">
      <a class="arg-link" href="{p["url"]}" lang="{p["lang"].lower()}">
        <div class="motif">{MOTIFS[p["motif"]]}</div>
        <p class="arg-kind">{escape(p["kind"][lang])}</p>
        <h3 class="arg-title">{escape(p["title"][lang])}</h3>
      </a>
      <p class="arg-q">{escape(p["question"][lang])}</p>
      <ul class="arg-facts">{facts}</ul>
      <p class="arg-meta"><span>{t["lang_of"]}: {t["langs"][p["lang"]]}</span><span>{t["data"]}: <a href="https://doi.org/{p["doi"]}" target="_blank" rel="noopener">{p["doi"]}</a>{code}</span></p>
      <a class="arg-open" href="{p["url"]}">{t["open"]} <span aria-hidden="true">→</span></a>
    </article>'''


def page(lang):
    t = T[lang]
    alt = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{T[l]["path"]}">' for l in T)
    switch = " ".join(
        f'<a href="{T[l]["path"]}" lang="{l}" hreflang="{l}"{" aria-current=\"true\"" if l == lang else ""}>{l.upper()}</a>' for l in T
    )
    ids = ["que", "argumentos", "origen", "autora"]
    nav = "".join(f'<a href="#{i}">{escape(n)}</a>' for i, n in zip(ids, t["nav"]))
    cmp_rows = "".join(
        f'<div class="cmp-item{" is-va" if k == len(t["cmp"]) - 1 else ""}"><h3>{escape(a)}</h3><p>{escape(b)}</p></div>'
        for k, (a, b) in enumerate(t["cmp"])
    )
    origin = "".join(f"<p>{escape(x)}</p>" for x in t["origin"])
    roles = "".join(f"<li>{escape(r)}</li>" for r in t["roles"])
    cards = "".join(card(p, lang, t) for p in PROJECTS)
    pr = PERSON
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
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
<link rel="preload" href="/assets/fonts/inter-tight-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<a class="skip" href="#main">{t["skip"]}</a>
<header class="top wrap">
  <a class="brand" href="{t["path"]}">Vissual Argument</a>
  <nav class="nav" aria-label="Secciones">{nav}</nav>
  <nav class="langs" aria-label="Idioma / Language / Langue">{switch}</nav>
</header>

<main id="main">
<section class="hero wrap">
  <p class="kicker">{t["kicker"]}</p>
  <h1>Vissual<br>Argument</h1>
  <p class="lede">{escape(t["lede"])}</p>
</section>

<section class="wrap block" id="que" aria-labelledby="que-h">
  <h2 id="que-h">{escape(t["what_h"])}</h2>
  <p class="body-serif">{escape(t["what_p"])}</p>
  <div class="cmp">{cmp_rows}</div>
</section>

<section class="wrap block" id="argumentos" aria-labelledby="arg-h">
  <h2 id="arg-h">{escape(t["projects_h"])}</h2>
  <p class="sub">{escape(t["projects_p"])}</p>
  <div class="args">{cards}
  </div>
</section>

<section class="wrap block two" id="origen" aria-labelledby="orig-h">
  <div>
    <h2 id="orig-h">{escape(t["origin_h"])}</h2>
    <div class="body-serif">{origin}</div>
  </div>
  <aside class="note">
    <h3>{escape(t["contrib_h"])}</h3>
    <p>{escape(t["contrib_p"])}</p>
  </aside>
</section>

<section class="wrap block two" id="autora" aria-labelledby="about-h">
  <div>
    <h2 id="about-h">{escape(t["about_h"])}</h2>
    <p class="person">{pr["name"]}</p>
    <ul class="roles">{roles}</ul>
  </div>
  <div>
    <h3 class="links-h">{escape(t["links_h"])}</h3>
    <ul class="links">
      <li><span>ORCID</span><a href="{pr["orcid"]}" rel="me noopener" target="_blank">0009-0009-1480-3668</a></li>
      <li><span>LinkedIn</span><a href="{pr["linkedin"]}" rel="me noopener" target="_blank">in/adelasantos</a></li>
      <li><span>GitHub</span><a href="{pr["github"]}" rel="me noopener" target="_blank">adelasantosd</a></li>
      <li><span>Linktree</span><a href="{pr["linktree"]}" rel="me noopener" target="_blank">adela.santos</a></li>
      <li><span>Email</span><a href="mailto:{pr["email"]}">{pr["email"]}</a></li>
    </ul>
  </div>
</section>
</main>

<footer class="foot wrap">
  <p>© 2026 {pr["name"]} · Vissual Argument</p>
  <p class="ai">{escape(t["ai"])}</p>
</footer>
</body>
</html>
'''


if __name__ == "__main__":
    for lang, t in T.items():
        out = ROOT / t["path"].strip("/") / "index.html" if t["path"] != "/" else ROOT / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang), encoding="utf-8")
        print("escrito", out.relative_to(ROOT))
