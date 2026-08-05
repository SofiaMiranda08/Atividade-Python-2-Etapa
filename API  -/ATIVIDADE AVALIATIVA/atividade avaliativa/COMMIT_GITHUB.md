# Como publicar no GitHub

Abra o terminal nesta pasta e execute:

```bash
git init
git add .
git commit -m "Conclui atividade de API com Thunder Client"
git branch -M main
git remote add origin URL_DO_SEU_REPOSITORIO
git push -u origin main
```

Substitua `URL_DO_SEU_REPOSITORIO` pela URL do repositório criado na sua conta.
Se esta pasta já estiver em um repositório, use somente:

```bash
git add .
git commit -m "Conclui atividade de API com Thunder Client"
git push
```

