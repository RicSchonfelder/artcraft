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
    "photocraft":  "**mesclado** (pt-BR pelo PR #700, a partir do nosso #637; correções #833). +245 linhas: PR [#10573](https://github.com/storytold/photocraft/pull/10573)",
    "filmcraft":   "**mesclado** (PR #176). +68 linhas: PR [#3818](https://github.com/storytold/filmcraft/pull/3818)",
    "lightcraft":  "**mesclado** (PR #228)",
    "effectcraft": "**mesclado** (PR #217)",
    "printcraft":  "**mesclado** (PR #165; upstream `storytold/pdfcraft`)",
    "designcraft": "**mesclado** (PR #103)",
    "vectorcraft": "**mesclado** (PR #384). +174 linhas: PR [#4996](https://github.com/storytold/vectorcraft/pull/4996)",
    "wordcraft":   "catálogo pt-BR do próprio upstream (completo; sem PR necessário)",
    "gridcraft":   "catálogo pt-BR do próprio upstream",
    "deckcraft":   "**PR [#259](https://github.com/storytold/deckcraft/pull/259) draft**, empilhado no [#34](https://github.com/storytold/deckcraft/pull/34) — catálogo pt-BR completo (1.232 linhas); o upstream não tem i18n, pelo que o 0.13.1 instalado está em inglês",
    "soundcraft":  "upstream ainda sem i18n — interface em inglês",
    "cadcraft":    "**mesclado** (PR #791). +191 linhas e 4 menus: PR [#2581](https://github.com/storytold/cadcraft/pull/2581)",
}

# Versões instaladas nesta máquina em 2026-10-31 (releases oficiais do upstream):
# repo -> (versão anterior, versão instalada, nota)
INSTALADO = {
    "photocraft":  ("0.9.0",  "0.18.0"),
    "filmcraft":   ("0.9.0",  "0.15.0"),
    "lightcraft":  ("0.8.0",  "0.16.0"),
    "effectcraft": ("0.10.0", "0.19.0"),
    "printcraft":  ("0.8.0",  "0.16.1"),
    "designcraft": ("0.8.0",  "0.15.2"),
    "vectorcraft": ("0.12.0", "0.19.0"),
    "wordcraft":   ("0.7.0",  "0.13.2"),
    "gridcraft":   ("0.7.0",  "0.14.2"),
    "deckcraft":   ("0.7.0",  "0.13.1"),
    "soundcraft":  ("0.7.0",  "0.15.0"),
    "cadcraft":    ("0.7.0",  "0.15.1"),
}

# Aplicativos cujo fork (com README.pt-BR) é nosso.
FORKED = {"photocraft", "filmcraft", "lightcraft", "effectcraft",
          "printcraft", "designcraft", "vectorcraft"}

# Forks nossos sem README.pt-BR (criados só para contribuir com a tradução).
FORK_NO_README = {"cadcraft", "deckcraft"}


def upstream_name(repo: str) -> str:
    return UPSTREAM.get(repo, repo)


def build(repos):
    by_name = {r["name"]: r for r in repos}

    L = []
    A = L.append
    A("# 🎨 ArtCraft — suíte com tradução pt-BR")
    A("")
    A("Este repositório reúne os **doze aplicativos da suíte ArtCraft** — editores *clean-room* "
      "reimplementados em **Rust puro**, cada um no lugar de um software comercial. Oito deles têm a "
      "**interface traduzida para o português do Brasil (pt-BR)** por mim e já mesclada no upstream "
      "(via os meus forks); outros dois (WordCraft e GridCraft) trazem o catálogo pt-BR do próprio "
      "upstream. DeckCraft tem a tradução pronta mas ainda em PR draft; SoundCraft ainda não tem i18n.")
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

    A("## 🖥️ Instalado nesta máquina (31/10/2026)")
    A("")
    A("Todos os doze passaram para as **releases oficiais** do upstream — binário e `-cli`, `.desktop` com a "
      "categoria `X-ArtCraft`, ícones hicolor e man pages — em `~/Projetos/Programas/<app>/bin/` e "
      "`~/.local/bin/<app>`. As versões anteriores ficaram em `~/Projetos/Programas/_bak-2026-10-31/`.")
    A("")
    A("| Aplicativo | Antes | Agora | pt-BR |")
    A("|---|---|---|---|")
    SEMENTE = {
        "photocraft": "sim", "filmcraft": "sim", "lightcraft": "sim", "effectcraft": "sim",
        "printcraft": "sim", "designcraft": "sim", "vectorcraft": "sim", "wordcraft": "sim",
        "gridcraft": "sim", "cadcraft": "sim", "deckcraft": "**não** (upstream sem i18n)",
        "soundcraft": "**não** (upstream sem i18n)",
    }
    for repo, nome, prop, subs in SUITE:
        antes, agora = INSTALADO[repo]
        A(f"| **{nome}** | {antes} | **{agora}** | {SEMENTE[repo]} |")
    A("")
    A("Atualizar de novo, sem compilar (é o que foi feito aqui):")
    A("")
    A("```bash")
    A("# 1. ver a release mais recente e baixar o tarball + somas")
    A("gh release view -R storytold/<app> --json tagName -q .tagName")
    A("gh release download <tag> -R storytold/<app> -p '<app>-<ver>-linux-x86_64.tar.gz' -p SHA256SUMS.txt")
    A("# 2. conferir a soma, extrair e instalar binário + -cli")
    A("sha256sum <app>-<ver>-linux-x86_64.tar.gz    # comparar com SHA256SUMS.txt")
    A("tar xzf <app>-<ver>-linux-x86_64.tar.gz && install -m755 <app>-<ver>-linux-x86_64/bin/<app> \\")
    A("  ~/Projetos/Programas/<app>/bin/<app>")
    A("```")
    A("")
    A("O `.desktop` do tarball vem com `Exec=<app>`: trocar por `Exec=$HOME/Projetos/Programas/<app>/bin/<app> %F` "
      "e acrescentar `X-ArtCraft;` às `Categories=` (senão o app não agrupa com a suíte no menu).")
    A("")

    A("## 🌎 Tradução pt-BR — o que mudou em 31/10/2026")
    A("")
    A("Os catálogos pt-BR já mesclados ficaram **desatualizados** com o trabalho recente do upstream: "
      "strings novas (verificação de atualizações, diálogos de plotagem e unidades, Camera Raw, "
      "smart objects, presets de impressão, avisos de codec) continuavam em inglês. Foram traduzidas "
      "e enviadas como PRs — todas validadas por um verificador de placeholders, reticências, "
      "dois-pontos e duplicados:")
    A("")
    A("| Aplicativo | Linhas novas | PR |")
    A("|---|---:|---|")
    A("| **CadCraft** | 191 + 4 menus | [#2581](https://github.com/storytold/cadcraft/pull/2581) |")
    A("| **PhotoCraft** | 245 | [#10573](https://github.com/storytold/photocraft/pull/10573) |")
    A("| **VectorCraft** | 174 | [#4996](https://github.com/storytold/vectorcraft/pull/4996) |")
    A("| **FilmCraft** | 68 | [#3818](https://github.com/storytold/filmcraft/pull/3818) |")
    A("")
    A("Pendente: **DeckCraft** — o catálogo pt-BR existe (#259, 1.232 linhas), mas o upstream "
      "refatorou a UI em ~1.700 commits desde o branch, e o `i18n` nunca foi mesclado. Portar exige "
      "refazer a extração de strings sobre o 0.13.1 (24 ficheiros em conflito no rebase).")
    A("")

    A("## 🇧🇷 Guia e glossário")
    A("")
    A("- **[Guia de instalação e uso no Linux (pt-BR)](GUIA-pt-BR.md)** — compilar, instalar no menu e pôr a interface em português, com as duas pegadinhas conhecidas (`craft-libs` e a categoria `X-ArtCraft`).")
    A("- **[Glossário pt-BR](GLOSSARIO-pt-BR.md)** — o vocabulário dos catálogos por domínio (CAD, slides, texto, planilha, áudio) e as regras de estilo que os repositórios exigem.")
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
