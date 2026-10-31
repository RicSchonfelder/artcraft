# 🇧🇷 Guia de instalação e uso da suíte ArtCraft no Linux (pt-BR)

Guia prático para compilar e usar os **12 aplicativos da suíte ArtCraft** no Linux, com a **interface
em português**. Escrito a partir do que foi realmente executado nesta máquina (nada aqui é teórico).

> Resumo: são editores *clean-room* em **Rust puro**, cada um no lugar de um programa comercial.
> A tradução pt-BR é do próprio upstream (contribuída app por app) — veja o `README.md` do hub para
> o estado de cada PR.

## O que é a suíte

| Aplicativo | Faz o papel de | Repositório (upstream) |
|---|---|---|
| **PhotoCraft** | Adobe Photoshop | `storytold/photocraft` |
| **FilmCraft** | Adobe Premiere Pro | `storytold/filmcraft` |
| **LightCraft** | Adobe Lightroom | `storytold/lightcraft` |
| **EffectCraft** | Adobe After Effects | `storytold/effectcraft` |
| **PrintCraft** | Adobe Acrobat | `storytold/pdfcraft` |
| **DesignCraft** | Adobe InDesign | `storytold/designcraft` |
| **VectorCraft** | Adobe Illustrator | `storytold/vectorcraft` |
| **WordCraft** | Microsoft Word | `storytold/wordcraft` |
| **GridCraft** | Microsoft Excel | `storytold/gridcraft` |
| **DeckCraft** | Microsoft PowerPoint | `storytold/deckcraft` |
| **SoundCraft** | Adobe Audition | `storytold/soundcraft` |
| **CadCraft** | Autodesk AutoCAD | `storytold/cadcraft` |

## Pré-requisitos

- **Rust** (stable) — `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
- **~15 GB livres** de disco por app durante a compilação (o alvo do Cargo é grande; você pode apagar
  depois de instalar o binário).
- **8 GB de RAM** (16 GB deixa a compilação paralela confortável).
- Bibliotecas de sistema para GUI/áudio (no Debian/Ubuntu: `libxkbcommon-dev libwayland-dev
  libasound2-dev`).
- Os fontes compartilhados (**craft-fonts**) são um *input opcional* do build, mas o resultado fica
  muito melhor com eles.

## Atalho: instalar a release oficial (sem compilar)

Desde outubro de 2026 o upstream publica binários para Linux x86_64 em cada release. É o caminho
mais rápido para **atualizar** — e o que foi usado nesta máquina em 31/10/2026:

```bash
APP=photocraft                       # nome do pacote (PrintCraft = pdfcraft)
VER=$(gh release view -R storytold/$APP --json tagName -q .tagName); V=${VER#v}
gh release download "$VER" -R storytold/$APP \
  -p "$APP-$V-linux-x86_64.tar.gz" -p SHA256SUMS.txt
sha256sum "$APP-$V-linux-x86_64.tar.gz"      # comparar com SHA256SUMS.txt
tar xzf "$APP-$V-linux-x86_64.tar.gz"
install -m755 "$APP-$V-linux-x86_64/bin/$APP"     "$HOME/Projetos/Programas/$APP/bin/$APP"
install -m755 "$APP-$V-linux-x86_64/bin/$APP-cli" "$HOME/Projetos/Programas/$APP/bin/$APP-cli"
```

Depois **copie o `.desktop` e os ícones** do próprio tarball (`share/applications/`,
`share/icons/hicolor/`), trocando o `Exec=`/`TryExec=` pelo caminho acima e acrescentando
`X-ArtCraft;` às `Categories=` — é a pegadinha nº 2 do fim deste guia. O tarball também traz
`share/man/`, `share/metainfo/` e `share/mime/`, que podem ir para `~/.local/share/`.

Compilar (abaixo) continua a ser o caminho para testar um branch com tradução nova — por exemplo o
`i18n/pt-br` do DeckCraft, que o upstream ainda não mesclou.

## Passo a passo (compilar)

### 1. Rust e os fontes

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
git clone https://github.com/storytold/craft-fonts ~/Projetos/craft-fonts
```

### 2. Corrija a autenticação do `craft-libs` (pegadinha nº 1)

Alguns apps (SoundCraft, CadCraft…) dependem de `storytold/craft-libs` via git. Se a máquina tem
um rewrite de `https://github.com/` para `git@github.com:` (comum para usar SSH), o **libgit2 do
Cargo falha** com *"failed to authenticate"*. Solução:

```bash
mkdir -p ~/.cargo
cat >> ~/.cargo/config.toml <<'EOF'
[net]
git-fetch-with-cli = true
EOF
```

### 3. Compile e instale um app

Receita usada para **todos** os 12 (troque `<app>`; para o PrintCraft o repo é `pdfcraft`):

```bash
export PATH="$HOME/.cargo/bin:$PATH"
export CRAFT_FONTS_DIR="$HOME/Projetos/craft-fonts"
export CRAFT_FONTS_REQUIRED=1
export CARGO_TARGET_DIR="$HOME/Projetos/craft-targets/<app>"   # um alvo por app

git clone https://github.com/storytold/<app> "$HOME/Projetos/craft-repos/<app>"
cd "$HOME/Projetos/craft-repos/<app>"
cargo build --release -p <app>

mkdir -p "$HOME/Projetos/Programas/<app>/bin"
install -m755 "$CARGO_TARGET_DIR/release/<app>" "$HOME/Projetos/Programas/<app>/bin/<app>"
ln -sfn "$HOME/Projetos/Programas/<app>/bin/<app>" "$HOME/.local/bin/<app>"
```

> **Um `CARGO_TARGET_DIR` por app** evita que uma compilação concorra com outra e facilita apagar o
> alvo depois (`rm -rf ~/Projetos/craft-targets/<app>`) para liberar disco.
>
> Alguns apps também geram um `<app>-cli` (headless, scriptável, servidor MCP) — compile com
> `-p <app>-cli` e instale do mesmo jeito.

### 4. Atalho no menu (pegadinha nº 2)

Cada repositório traz `packaging/linux/ai.storyteller.<app>.desktop` e os ícones em
`assets/app-icon/hicolor/`. **Atenção:** os `.desktop` do upstream vêm com categorias diferentes
(`Office;…`, `AudioVideo;…`) e **não** aparecem agrupados com os outros ArtCraft. A suíte usa a
categoria **`X-ArtCraft`** como primeira — acrescente-a:

```bash
APP=<app>; BIN="$HOME/Projetos/Programas/$APP/bin/$APP"
APPDIR="$HOME/.local/share/applications"; ID="ai.storyteller.$APP"

sed -e "s|^Exec=.*|Exec=$BIN %F|" -e "s|^TryExec=.*|TryExec=$BIN|" \
    "$HOME/Projetos/craft-repos/$APP/packaging/linux/$ID.desktop" > "$APPDIR/$ID.desktop"
grep -q '^Categories=X-ArtCraft' "$APPDIR/$ID.desktop" || \
  sed -i 's|^Categories=\(.*\)|Categories=X-ArtCraft;\1|' "$APPDIR/$ID.desktop"

cp -R "$HOME/Projetos/craft-repos/$APP/assets/app-icon/hicolor/." "$HOME/.local/share/icons/hicolor/"

update-desktop-database "$APPDIR"
gtk-update-icon-cache -qtf "$HOME/.local/share/icons/hicolor" 2>/dev/null
xfce4-panel -r 2>/dev/null   # XFCE: recarrega o menu
```

### 5. Coloque a interface em português

Cada app tem a troca de idioma na própria UI:

- **CadCraft / DeckCraft / WordCraft / GridCraft:** menu **Edit/Editar ▸ Interface Language ▸
  Português (Brasil)** (ou nas Preferências).
- Com **Auto (idioma do sistema)**, um `LANG=pt_BR.UTF-8` já abre em português.

## Uso por agentes (opcional, mas o diferencial da suíte)

Todo app é 100% comandável — a mesma ação da UI é um comando com id e JSON:

```bash
# canal de controle (JSON por linha) para um agente dirigir o app aberto
<app> --control 7990

# MCP (stdio) — para Claude/Cursor/opencode
<app>-cli mcp                 # headless, com motor próprio
<app>-cli mcp --connect 7990  # dirigindo o app que está aberto
```

Exemplo real: uma apresentação inteira de 9 slides (tema, títulos, tópicos, tabela de preços,
gráfico, transições e export PDF/PPTX/PNG) foi montada **só por MCP** no DeckCraft.

## Problemas comuns

| Sintoma | Causa | Solução |
|---|---|---|
| `failed to authenticate` ao baixar `craft-libs` | libgit2 + rewrite de URL | `net.git-fetch-with-cli = true` (passo 2) |
| O app instalou mas **não aparece no menu** | `.desktop` sem `X-ArtCraft` | passo 4 |
| Ícone cinza/genérico | ícones não copiados | `cp -R … hicolor/.` + `gtk-update-icon-cache` |
| Compilação sem fontes bonitas | `CRAFT_FONTS_DIR` ausente | passo 1 e exportar a variável |
| Disco cheio | alvos do Cargo | apagar `~/Projetos/craft-targets/<app>` |

---

Voltar ao índice: [`README.md`](README.md) · Glossário de tradução: [`GLOSSARIO-pt-BR.md`](GLOSSARIO-pt-BR.md)
