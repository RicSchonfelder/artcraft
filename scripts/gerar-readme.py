#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o README.md do hub com os links dos repositórios de RicSchonfelder.
Requires: gh (GitHub CLI) autenticado. Uso: python3 scripts/gerar-readme.py
"""
import json
import subprocess
import sys

OWNER = "RickSchonfelder" if False else "RicSchonfelder"


def gh_repo_list():
    out = subprocess.run(
        ["gh", "repo", "list", OWNER, "--limit", "300",
         "--json", "name,description,visibility,isFork"],
        check=True, capture_output=True, text=True).stdout
    return json.loads(out)


def md_esc(s: str) -> str:
    return (s or "").replace("|", "/").replace("\n", " ")


# (repo no upstream, Nome, Propósito, No lugar de)
SUITE = [
    ("photocraft",  "PhotoCraft",  "Edição de imagens",                       "Adobe Photoshop"),
    ("filmcraft",   "FilmCraft",   "Edição de vídeo, cor e som",              "Adobe Premiere Pro"),
    ("lightcraft",  "LightCraft",  "Biblioteca de fotos e revelação RAW",     "Adobe Lightroom"),
    ("effectcraft", "EffectCraft", "Motion graphics e efeitos visuais",       "Adobe After Effects"),
    ("printcraft",  "PrintCraft",  "Workbench de PDF",                        "Adobe Acrobat"),
    ("designcraft", "DesignCraft", "Layout de página e publicação",           "Adobe InDesign"),
    ("vectorcraft", "VectorCraft", "Ilustração vetorial",                     "Adobe Illustrator"),
    ("wordcraft",   "WordCraft",   "Documentos de texto",                     "Microsoft Word"),
    ("gridcraft",   "GridCraft",   "Planilhas de cálculo",                    "Microsoft Excel"),
    ("deckcraft",   "DeckCraft",   "Apresentações de slides",                 "Microsoft PowerPoint"),
    ("soundcraft",  "SoundCraft",  "Edição e mixagem de áudio",               "Adobe Audition"),
    ("cadcraft",    "CadCraft",    "Desenho técnico CAD (2D/3D)",             "Autodesk AutoCAD"),
]

# Nome do repositório no upstream, quando difere do local.
UPSTREAM = {"printcraft": "pdfcraft"}

# Estado da tradução pt-BR, por aplicativo.
PTBR = {
    "photocraft":  "aceito no upstream (PR #637 → #700); correções PR #833 em revisão",
    "filmcraft":   "**mesclado** (PR #176)",
    "lightcraft":  "**mesclado** (PR #228)",
    "effectcraft": "PR #217 aberto",
    "printcraft":  "**mesclado** (PR #165; upstream `storytold/pdfcraft`)",
    "designcraft": "**mesclado** (PR #103)",
    "vectorcraft": "**mesclado** (PR #384)",
    "wordcraft":   "catálogo pt-BR do próprio upstream (completo; sem PR necessário)",
    "gridcraft":   "catálogo pt-BR do próprio upstream",
    "deckcraft":   "upstream ainda sem i18n — interface em inglês",
    "soundcraft":  "upstream ainda sem i18n — interface em inglês",
    "cadcraft":    "**PR [#791](https://github.com/storytold/cadcraft/pull/791) aberto** (238 linhas; catálogo pt-BR completo)",
}

# Aplicativos cujo fork (com README.pt-BR) é nosso.
FORKED = {"photocraft", "filmcraft", "lightcraft", "effectcraft",
          "printcraft", "designcraft", "vectorcraft"}

# Forks nossos sem README.pt-BR (criados só para contribuir com a tradução).
FORK_NO_README = {"cadcraft"}


def upstream_name(repo: str) -> str:
    return UPSTREAM.get(repo, repo)


def build(repos):
    by_name = {r["name"]: r for r in repos}

    L = []
    A = L.append
    A("# 🎨 ArtCraft — suíte com tradução pt-BR")
    A("")
    A("Este repositório reúne os **doze aplicativos da suíte ArtCraft** — editores *clean-room* "
      "reimplementados em **Rust puro**, cada um no lugar de um software comercial. Sete deles têm a "
      "**interface traduzida para o português do Brasil (pt-BR)** por mim e já mesclada no upstream "
      "(via os meus forks); os outros cinco rodam a partir do **upstream**, com a tradução pt-BR "
      "conforme o próprio upstream oferece (ou ainda não oferece).")
    A("")
    A(f"- Perfil: https://github.com/{OWNER}")
    A("")

    # ---- No lugar de quais programas ----
    A("## 📦 No lugar de quais programas")
    A("")
    A("Cada aplicativo da suíte **faz o lugar de um software comercial**:")
    A("")
    for repo, nome, prop, subs in SUITE:
        A(f"- **{nome}** ({prop}) → no lugar do **{subs}**")
    A("")

    # ---- Suíte ArtCraft ----
    A("## ✨ A suíte (12 aplicativos)")
    A("")
    A("| Aplicativo | Propósito | No lugar de | Meu fork (pt-BR) | Upstream | Tradução pt-BR |")
    A("|---|---|---|---|---|---|")
    for repo, nome, prop, subs in SUITE:
        if repo in FORKED and repo in by_name:
            fork = f"[{nome}](https://github.com/{OWNER}/{repo}) · [README.pt-BR](https://github.com/{OWNER}/{repo}/blob/main/README.pt-BR.md)"
        elif repo in FORK_NO_README and repo in by_name:
            fork = f"[{nome}](https://github.com/{OWNER}/{repo})"
        else:
            fork = "—"
        up = f"[storytold/{upstream_name(repo)}](https://github.com/storytold/{upstream_name(repo)})"
        A(f"| **{nome}** | {prop} | {subs} | {fork} | {up} | {PTBR[repo]} |")
    A("")
    A("Instalação no Linux, compilação e mais detalhes: veja o `README.pt-BR.md` de cada fork (links acima).")
    A("Site da suíte: https://getartcraft.com · Discord: https://discord.gg/artcraft")
    A("")

    A("## ♻️ Atualizar esta lista")
    A("")
    A("```bash")
    A("python3 scripts/gerar-readme.py   # usa o GitHub CLI (`gh`) autenticado")
    A('git commit -am "atualiza lista de repositórios" && git push')
    A("```")
    A("")
    A("---")
    A("")
    A("*Gerado automaticamente.*")
    A("")
    return "\n".join(L)


def main():
    repos = gh_repo_list()
    out = build(repos)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(out)
    print(f"README.md gerado com {len(repos)} repositórios.")


if __name__ == "__main__":
    main()
