#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o README.md do hub com os links de TODOS os repositórios de RicSchonfelder.
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

SUITE = [
    ("photocraft",  "PhotoCraft",  "Edição de imagens",              "Adobe Photoshop"),
    ("filmcraft",   "FilmCraft",   "Edição de vídeo, cor e som",     "Adobe Premiere Pro"),
    ("lightcraft",  "LightCraft",  "Biblioteca de fotos e revelação RAW", "Adobe Lightroom"),
    ("effectcraft", "EffectCraft", "Motion graphics e efeitos visuais", "Adobe After Effects"),
    ("printcraft",  "PrintCraft",  "Workbench de PDF",               "Adobe Acrobat"),
    ("designcraft", "DesignCraft", "Layout de página e publicação",  "Adobe InDesign"),
    ("vectorcraft", "VectorCraft", "Ilustração vetorial",            "Adobe Illustrator"),
]
PR = {
    "photocraft":  "aceito no upstream (PR #637 → #700); correções PR #833",
    "filmcraft":   "**mesclado** (PR #176)",
    "lightcraft":  "PR #228 aberto",
    "effectcraft": "PR #217 aberto",
    "printcraft":  "PR #165 aberto (upstream `storytold/pdfcraft`)",
    "designcraft": "PR #103 aberto",
    "vectorcraft": "**mesclado** (PR #384)",
}

def build(repos):
    by_name = {r["name"]: r for r in repos}

    L = []
    A = L.append
    A("# 🎨 ArtCraft — forks com tradução pt-BR")
    A("")
    A("Este repositório reúne os sete aplicativos da **suíte ArtCraft** — forks com a **interface traduzida para o "
      "português do Brasil (pt-BR)**. É um conjunto **similar ao pacote Adobe (Creative Cloud)**: cada aplicativo "
      "ocupa o lugar de um software da Adobe, reimplementado em **Rust puro** e de forma *clean-room*.")
    A("")
    A(f"- Perfil: https://github.com/{OWNER}")
    A("")

    # ---- Similar ao pacote Adobe ----
    A("## 📦 Similar ao pacote Adobe")
    A("")
    A("Cada aplicativo da suíte **faz o lugar de um software da Adobe**:")
    A("")
    for repo, nome, prop, adobe in SUITE:
        A(f"- **{nome}** ({prop}) → no lugar do **{adobe}**")
    A("")

    # ---- Suíte ArtCraft ----
    A("## ✨ Os 7 aplicativos traduzidos")
    A("")
    A("| Aplicativo | Propósito | Reimplementação de | Meu fork (pt-BR) | Upstream | Tradução pt-BR |")
    A("|---|---|---|---|---|---|")
    for repo, nome, prop, adobe in SUITE:
        fork = f"[{nome}](https://github.com/{OWNER}/{repo})"
        up_name = "pdfcraft" if repo == "printcraft" else repo
        up = f"[storytold/{up_name}](https://github.com/storytold/{up_name})"
        readme_pt = f"[README.pt-BR](https://github.com/{OWNER}/{repo}/blob/main/README.pt-BR.md)"
        A(f"| **{nome}** | {prop} | {adobe} | {fork} · {readme_pt} | {up} | {PR[repo]} |")
    A("")
    A("Instalação no Linux, compilação e mais detalhes: veja o `README.pt-BR.md` de cada fork (links acima).")
    A("Site da suíte: https://getartcraft.com · Discord: https://discord.gg/artcraft")
    A("")

    A("## ♻️ Atualizar esta lista")
    A("")
    A("```bash")
    A("python3 scripts/gerar-readme.py   # usa o GitHub CLI (`gh`) autenticado")
    A("git commit -am \"atualiza lista de repositórios\" && git push")
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