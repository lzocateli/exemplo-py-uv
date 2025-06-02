## Configurar git

```bash
git config --global user.name 'lzocateli'
git config --global user.email lincoln@zocate.li
git config --global core.editor 'code -wait --new-window'
git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'
git config --global core.ignorecase false
```

## Instalar as dependências com uv
- Para instalar as dependências listadas no seu pyproject.toml usando o uv, você pode usar o seguinte comando no terminal, dentro do diretório do projeto:
```bash
uv pip install -r pyproject.toml
```
- No entanto, o uv também suporta diretamente o uso do pyproject.toml com:
```bash 
uv venv
uv install # Ainda não é totalmente compativel, use o comando anterior
```

Explicação:

- uv venv: cria um ambiente virtual no diretório .venv (ou outro, se especificado).
- uv install: lê o pyproject.toml e instala as dependências listadas em [tool.uv.dependencies].

Dica:

Se quiser ativar o ambiente virtual criado, use:
- No Linux/macOS:
```bash
  source .venv/bin/activate
```
- No Windows:
```powershell
  .venv\Scripts\activate
```
