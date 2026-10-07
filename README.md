# 🎨 ArtCraft — forks com tradução pt-BR

Este repositório reúne os sete aplicativos da **suíte ArtCraft** — forks com a **interface traduzida para o português do Brasil (pt-BR)**. As ferramentas reimplementam, em **Rust puro** e de forma *clean-room*, as ferramentas de criação da Adobe.

- Perfil: https://github.com/RicSchonfelder

## ✨ Os 7 aplicativos traduzidos

| Aplicativo | Propósito | Reimplementação de | Meu fork (pt-BR) | Upstream | Tradução pt-BR |
|---|---|---|---|---|---|
| **PhotoCraft** | Edição de imagens | Adobe Photoshop | [PhotoCraft](https://github.com/RicSchonfelder/photocraft) · [README.pt-BR](https://github.com/RicSchonfelder/photocraft/blob/main/README.pt-BR.md) | [storytold/photocraft](https://github.com/storytold/photocraft) | aceito no upstream (PR #637 → #700); correções PR #833 |
| **FilmCraft** | Edição de vídeo, cor e som | Adobe Premiere Pro | [FilmCraft](https://github.com/RicSchonfelder/filmcraft) · [README.pt-BR](https://github.com/RicSchonfelder/filmcraft/blob/main/README.pt-BR.md) | [storytold/filmcraft](https://github.com/storytold/filmcraft) | **mesclado** (PR #176) |
| **LightCraft** | Biblioteca de fotos e revelação RAW | Adobe Lightroom | [LightCraft](https://github.com/RicSchonfelder/lightcraft) · [README.pt-BR](https://github.com/RicSchonfelder/lightcraft/blob/main/README.pt-BR.md) | [storytold/lightcraft](https://github.com/storytold/lightcraft) | PR #228 aberto |
| **EffectCraft** | Motion graphics e efeitos visuais | Adobe After Effects | [EffectCraft](https://github.com/RicSchonfelder/effectcraft) · [README.pt-BR](https://github.com/RicSchonfelder/effectcraft/blob/main/README.pt-BR.md) | [storytold/effectcraft](https://github.com/storytold/effectcraft) | PR #217 aberto |
| **PrintCraft** | Workbench de PDF | Adobe Acrobat | [PrintCraft](https://github.com/RicSchonfelder/printcraft) · [README.pt-BR](https://github.com/RicSchonfelder/printcraft/blob/main/README.pt-BR.md) | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | PR #165 aberto (upstream `storytold/pdfcraft`) |
| **DesignCraft** | Layout de página e publicação | Adobe InDesign | [DesignCraft](https://github.com/RicSchonfelder/designcraft) · [README.pt-BR](https://github.com/RicSchonfelder/designcraft/blob/main/README.pt-BR.md) | [storytold/designcraft](https://github.com/storytold/designcraft) | PR #103 aberto |
| **VectorCraft** | Ilustração vetorial | Adobe Illustrator | [VectorCraft](https://github.com/RicSchonfelder/vectorcraft) · [README.pt-BR](https://github.com/RicSchonfelder/vectorcraft/blob/main/README.pt-BR.md) | [storytold/vectorcraft](https://github.com/storytold/vectorcraft) | **mesclado** (PR #384) |

Instalação no Linux, compilação e mais detalhes: veja o `README.pt-BR.md` de cada fork (links acima).
Site da suíte: https://getartcraft.com · Discord: https://discord.gg/artcraft

## ♻️ Atualizar esta lista

```bash
python3 scripts/gerar-readme.py   # usa o GitHub CLI (`gh`) autenticado
git commit -am "atualiza lista de repositórios" && git push
```

---

*Gerado automaticamente.*
