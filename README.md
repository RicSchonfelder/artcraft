# 🎨 ArtCraft — suíte com tradução pt-BR

Este repositório reúne os **doze aplicativos da suíte ArtCraft** — editores *clean-room* reimplementados em **Rust puro**, cada um no lugar de um software comercial. Oito deles têm a **interface traduzida para o português do Brasil (pt-BR)** por mim e já mesclada no upstream (via os meus forks); outros dois (WordCraft e GridCraft) trazem o catálogo pt-BR do próprio upstream. DeckCraft tem a tradução pronta mas ainda em PR draft; SoundCraft ainda não tem i18n.

- Perfil: https://github.com/RicSchonfelder

## 📦 No lugar de quais programas

Cada aplicativo da suíte **faz o lugar de um software comercial**:

- **PhotoCraft** (Edição de imagens) → no lugar do **Adobe Photoshop**
- **FilmCraft** (Edição de vídeo, cor e som) → no lugar do **Adobe Premiere Pro**
- **LightCraft** (Biblioteca de fotos e revelação RAW) → no lugar do **Adobe Lightroom**
- **EffectCraft** (Motion graphics e efeitos visuais) → no lugar do **Adobe After Effects**
- **PrintCraft** (Workbench de PDF) → no lugar do **Adobe Acrobat**
- **DesignCraft** (Layout de página e publicação) → no lugar do **Adobe InDesign**
- **VectorCraft** (Ilustração vetorial) → no lugar do **Adobe Illustrator**
- **WordCraft** (Documentos de texto) → no lugar do **Microsoft Word**
- **GridCraft** (Planilhas de cálculo) → no lugar do **Microsoft Excel**
- **DeckCraft** (Apresentações de slides) → no lugar do **Microsoft PowerPoint**
- **SoundCraft** (Edição e mixagem de áudio) → no lugar do **Adobe Audition**
- **CadCraft** (Desenho técnico CAD (2D/3D)) → no lugar do **Autodesk AutoCAD**

## ✨ A suíte (12 aplicativos)

| Aplicativo | Propósito | No lugar de | Meu fork (pt-BR) | Upstream | Tradução pt-BR |
|---|---|---|---|---|---|
| **PhotoCraft** | Edição de imagens | Adobe Photoshop | [PhotoCraft](https://github.com/RicSchonfelder/photocraft) · [README.pt-BR](https://github.com/RicSchonfelder/photocraft/blob/main/README.pt-BR.md) | [storytold/photocraft](https://github.com/storytold/photocraft) | **mesclado** (pt-BR pelo PR #700, a partir do nosso #637; correções #833). +245 linhas: PR [#10573](https://github.com/storytold/photocraft/pull/10573) |
| **FilmCraft** | Edição de vídeo, cor e som | Adobe Premiere Pro | [FilmCraft](https://github.com/RicSchonfelder/filmcraft) · [README.pt-BR](https://github.com/RicSchonfelder/filmcraft/blob/main/README.pt-BR.md) | [storytold/filmcraft](https://github.com/storytold/filmcraft) | **mesclado** (PR #176). +68 linhas: PR [#3818](https://github.com/storytold/filmcraft/pull/3818) |
| **LightCraft** | Biblioteca de fotos e revelação RAW | Adobe Lightroom | [LightCraft](https://github.com/RicSchonfelder/lightcraft) · [README.pt-BR](https://github.com/RicSchonfelder/lightcraft/blob/main/README.pt-BR.md) | [storytold/lightcraft](https://github.com/storytold/lightcraft) | **mesclado** (PR #228) |
| **EffectCraft** | Motion graphics e efeitos visuais | Adobe After Effects | [EffectCraft](https://github.com/RicSchonfelder/effectcraft) · [README.pt-BR](https://github.com/RicSchonfelder/effectcraft/blob/main/README.pt-BR.md) | [storytold/effectcraft](https://github.com/storytold/effectcraft) | **mesclado** (PR #217) |
| **PrintCraft** | Workbench de PDF | Adobe Acrobat | [PrintCraft](https://github.com/RicSchonfelder/printcraft) · [README.pt-BR](https://github.com/RicSchonfelder/printcraft/blob/main/README.pt-BR.md) | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | **mesclado** (PR #165; upstream `storytold/pdfcraft`) |
| **DesignCraft** | Layout de página e publicação | Adobe InDesign | [DesignCraft](https://github.com/RicSchonfelder/designcraft) · [README.pt-BR](https://github.com/RicSchonfelder/designcraft/blob/main/README.pt-BR.md) | [storytold/designcraft](https://github.com/storytold/designcraft) | **mesclado** (PR #103) |
| **VectorCraft** | Ilustração vetorial | Adobe Illustrator | [VectorCraft](https://github.com/RicSchonfelder/vectorcraft) · [README.pt-BR](https://github.com/RicSchonfelder/vectorcraft/blob/main/README.pt-BR.md) | [storytold/vectorcraft](https://github.com/storytold/vectorcraft) | **mesclado** (PR #384). +174 linhas: PR [#4996](https://github.com/storytold/vectorcraft/pull/4996) |
| **WordCraft** | Documentos de texto | Microsoft Word | — | [storytold/wordcraft](https://github.com/storytold/wordcraft) | catálogo pt-BR do próprio upstream (completo; sem PR necessário) |
| **GridCraft** | Planilhas de cálculo | Microsoft Excel | — | [storytold/gridcraft](https://github.com/storytold/gridcraft) | catálogo pt-BR do próprio upstream |
| **DeckCraft** | Apresentações de slides | Microsoft PowerPoint | [DeckCraft](https://github.com/RicSchonfelder/deckcraft) | [storytold/deckcraft](https://github.com/storytold/deckcraft) | **PR [#259](https://github.com/storytold/deckcraft/pull/259) draft**, empilhado no [#34](https://github.com/storytold/deckcraft/pull/34) — catálogo pt-BR completo (1.232 linhas); o upstream não tem i18n, pelo que o 0.13.1 instalado está em inglês |
| **SoundCraft** | Edição e mixagem de áudio | Adobe Audition | — | [storytold/soundcraft](https://github.com/storytold/soundcraft) | upstream ainda sem i18n — interface em inglês |
| **CadCraft** | Desenho técnico CAD (2D/3D) | Autodesk AutoCAD | [CadCraft](https://github.com/RicSchonfelder/cadcraft) | [storytold/cadcraft](https://github.com/storytold/cadcraft) | **mesclado** (PR #791). +191 linhas e 4 menus: PR [#2581](https://github.com/storytold/cadcraft/pull/2581) |

Instalação no Linux, compilação e mais detalhes: veja o `README.pt-BR.md` de cada fork (links acima).
Site da suíte: https://getartcraft.com · Discord: https://discord.gg/artcraft

## 🖥️ Instalado nesta máquina (31/10/2026)

Todos os doze passaram para as **releases oficiais** do upstream — binário e `-cli`, `.desktop` com a categoria `X-ArtCraft`, ícones hicolor e man pages — em `~/Projetos/Programas/<app>/bin/` e `~/.local/bin/<app>`. As versões anteriores ficaram em `~/Projetos/Programas/_bak-2026-10-31/`.

| Aplicativo | Antes | Agora | pt-BR |
|---|---|---|---|
| **PhotoCraft** | 0.9.0 | **0.18.0** | sim |
| **FilmCraft** | 0.9.0 | **0.15.0** | sim |
| **LightCraft** | 0.8.0 | **0.16.0** | sim |
| **EffectCraft** | 0.10.0 | **0.19.0** | sim |
| **PrintCraft** | 0.8.0 | **0.16.1** | sim |
| **DesignCraft** | 0.8.0 | **0.15.2** | sim |
| **VectorCraft** | 0.12.0 | **0.19.0** | sim |
| **WordCraft** | 0.7.0 | **0.13.2** | sim |
| **GridCraft** | 0.7.0 | **0.14.2** | sim |
| **DeckCraft** | 0.7.0 | **0.13.1** | **não** (upstream sem i18n) |
| **SoundCraft** | 0.7.0 | **0.15.0** | **não** (upstream sem i18n) |
| **CadCraft** | 0.7.0 | **0.15.1** | sim |

Atualizar de novo, sem compilar (é o que foi feito aqui):

```bash
# 1. ver a release mais recente e baixar o tarball + somas
gh release view -R storytold/<app> --json tagName -q .tagName
gh release download <tag> -R storytold/<app> -p '<app>-<ver>-linux-x86_64.tar.gz' -p SHA256SUMS.txt
# 2. conferir a soma, extrair e instalar binário + -cli
sha256sum <app>-<ver>-linux-x86_64.tar.gz    # comparar com SHA256SUMS.txt
tar xzf <app>-<ver>-linux-x86_64.tar.gz && install -m755 <app>-<ver>-linux-x86_64/bin/<app> \
  ~/Projetos/Programas/<app>/bin/<app>
```

O `.desktop` do tarball vem com `Exec=<app>`: trocar por `Exec=$HOME/Projetos/Programas/<app>/bin/<app> %F` e acrescentar `X-ArtCraft;` às `Categories=` (senão o app não agrupa com a suíte no menu).

## 🌎 Tradução pt-BR — o que mudou em 31/10/2026

Os catálogos pt-BR já mesclados ficaram **desatualizados** com o trabalho recente do upstream: strings novas (verificação de atualizações, diálogos de plotagem e unidades, Camera Raw, smart objects, presets de impressão, avisos de codec) continuavam em inglês. Foram traduzidas e enviadas como PRs — todas validadas por um verificador de placeholders, reticências, dois-pontos e duplicados:

| Aplicativo | Linhas novas | PR |
|---|---:|---|
| **CadCraft** | 191 + 4 menus | [#2581](https://github.com/storytold/cadcraft/pull/2581) |
| **PhotoCraft** | 245 | [#10573](https://github.com/storytold/photocraft/pull/10573) |
| **VectorCraft** | 174 | [#4996](https://github.com/storytold/vectorcraft/pull/4996) |
| **FilmCraft** | 68 | [#3818](https://github.com/storytold/filmcraft/pull/3818) |

Pendente: **DeckCraft** — o catálogo pt-BR existe (#259, 1.232 linhas), mas o upstream refatorou a UI em ~1.700 commits desde o branch, e o `i18n` nunca foi mesclado. Portar exige refazer a extração de strings sobre o 0.13.1 (24 ficheiros em conflito no rebase).

## 🇧🇷 Guia e glossário

- **[Guia de instalação e uso no Linux (pt-BR)](GUIA-pt-BR.md)** — compilar, instalar no menu e pôr a interface em português, com as duas pegadinhas conhecidas (`craft-libs` e a categoria `X-ArtCraft`).
- **[Glossário pt-BR](GLOSSARIO-pt-BR.md)** — o vocabulário dos catálogos por domínio (CAD, slides, texto, planilha, áudio) e as regras de estilo que os repositórios exigem.

## ♻️ Atualizar esta lista

```bash
python3 scripts/gerar-readme.py   # usa o GitHub CLI (`gh`) autenticado
git commit -am "atualiza lista de repositórios" && git push
```

---

*Gerado automaticamente.*
