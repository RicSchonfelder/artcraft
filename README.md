# 🎨 ArtCraft — suíte com tradução pt-BR

Este repositório reúne os **doze aplicativos da suíte ArtCraft** — editores *clean-room* reimplementados em **Rust puro**, cada um no lugar de um software comercial. Sete deles têm a **interface traduzida para o português do Brasil (pt-BR)** por mim e já mesclada no upstream (via os meus forks); os outros cinco rodam a partir do **upstream**, com a tradução pt-BR conforme o próprio upstream oferece (ou ainda não oferece).

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
| **PhotoCraft** | Edição de imagens | Adobe Photoshop | [PhotoCraft](https://github.com/RicSchonfelder/photocraft) · [README.pt-BR](https://github.com/RicSchonfelder/photocraft/blob/main/README.pt-BR.md) | [storytold/photocraft](https://github.com/storytold/photocraft) | aceito no upstream (PR #637 → #700); correções PR #833 em revisão |
| **FilmCraft** | Edição de vídeo, cor e som | Adobe Premiere Pro | [FilmCraft](https://github.com/RicSchonfelder/filmcraft) · [README.pt-BR](https://github.com/RicSchonfelder/filmcraft/blob/main/README.pt-BR.md) | [storytold/filmcraft](https://github.com/storytold/filmcraft) | **mesclado** (PR #176) |
| **LightCraft** | Biblioteca de fotos e revelação RAW | Adobe Lightroom | [LightCraft](https://github.com/RicSchonfelder/lightcraft) · [README.pt-BR](https://github.com/RicSchonfelder/lightcraft/blob/main/README.pt-BR.md) | [storytold/lightcraft](https://github.com/storytold/lightcraft) | **mesclado** (PR #228) |
| **EffectCraft** | Motion graphics e efeitos visuais | Adobe After Effects | [EffectCraft](https://github.com/RicSchonfelder/effectcraft) · [README.pt-BR](https://github.com/RicSchonfelder/effectcraft/blob/main/README.pt-BR.md) | [storytold/effectcraft](https://github.com/storytold/effectcraft) | PR #217 aberto |
| **PrintCraft** | Workbench de PDF | Adobe Acrobat | [PrintCraft](https://github.com/RicSchonfelder/printcraft) · [README.pt-BR](https://github.com/RicSchonfelder/printcraft/blob/main/README.pt-BR.md) | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | **mesclado** (PR #165; upstream `storytold/pdfcraft`) |
| **DesignCraft** | Layout de página e publicação | Adobe InDesign | [DesignCraft](https://github.com/RicSchonfelder/designcraft) · [README.pt-BR](https://github.com/RicSchonfelder/designcraft/blob/main/README.pt-BR.md) | [storytold/designcraft](https://github.com/storytold/designcraft) | **mesclado** (PR #103) |
| **VectorCraft** | Ilustração vetorial | Adobe Illustrator | [VectorCraft](https://github.com/RicSchonfelder/vectorcraft) · [README.pt-BR](https://github.com/RicSchonfelder/vectorcraft/blob/main/README.pt-BR.md) | [storytold/vectorcraft](https://github.com/storytold/vectorcraft) | **mesclado** (PR #384) |
| **WordCraft** | Documentos de texto | Microsoft Word | — | [storytold/wordcraft](https://github.com/storytold/wordcraft) | catálogo pt-BR do próprio upstream (completo; sem PR necessário) |
| **GridCraft** | Planilhas de cálculo | Microsoft Excel | — | [storytold/gridcraft](https://github.com/storytold/gridcraft) | catálogo pt-BR do próprio upstream |
| **DeckCraft** | Apresentações de slides | Microsoft PowerPoint | — | [storytold/deckcraft](https://github.com/storytold/deckcraft) | upstream ainda sem i18n — interface em inglês |
| **SoundCraft** | Edição e mixagem de áudio | Adobe Audition | — | [storytold/soundcraft](https://github.com/storytold/soundcraft) | upstream ainda sem i18n — interface em inglês |
| **CadCraft** | Desenho técnico CAD (2D/3D) | Autodesk AutoCAD | [CadCraft](https://github.com/RicSchonfelder/cadcraft) | [storytold/cadcraft](https://github.com/storytold/cadcraft) | **PR [#791](https://github.com/storytold/cadcraft/pull/791) aberto** (238 linhas; catálogo pt-BR completo) |

Instalação no Linux, compilação e mais detalhes: veja o `README.pt-BR.md` de cada fork (links acima).
Site da suíte: https://getartcraft.com · Discord: https://discord.gg/artcraft

## ♻️ Atualizar esta lista

```bash
python3 scripts/gerar-readme.py   # usa o GitHub CLI (`gh`) autenticado
git commit -am "atualiza lista de repositórios" && git push
```

---

*Gerado automaticamente.*
