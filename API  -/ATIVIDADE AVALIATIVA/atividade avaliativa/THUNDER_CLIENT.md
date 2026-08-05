# Passo a passo no Thunder Client

Com o projeto em execução em `http://127.0.0.1:5000`:

1. No VS Code, instale a extensão **Thunder Client**.
2. Clique no ícone de raio ou pressione `Ctrl + Shift + P` e execute
   `Thunder Client: New Request`.
3. Nos requests POST e PUT, abra **Headers** e informe:
   `Content-Type` = `application/json`.
4. Em **Body**, escolha **JSON** e cole o conteúdo do arquivo indicado.

## 1. Adicionar Ariana Grande

- Método: `POST`
- URL: `http://127.0.0.1:5000/api/cadastros`
- Body: `requests/01_ariana_grande.json`
- Resposta esperada: `201 Created`

## 2. Adicionar Miley Cyrus

- Método: `POST`
- URL: `http://127.0.0.1:5000/api/cadastros`
- Body: `requests/02_miley_cyrus.json`
- Resposta esperada: `201 Created`

## 3. Atualizar a pessoa de índice 1

- Método: `PUT`
- URL: `http://127.0.0.1:5000/api/cadastros/1`
- Body: `requests/03_atualiza_pessoa.json`
- Resposta esperada: `200 OK`

## 4. Excluir a pessoa de índice 2

- Método: `DELETE`
- URL: `http://127.0.0.1:5000/api/cadastros/2`
- Body: nenhum
- Resposta esperada: `204 No Content`

## Conferência

- JSON: `GET http://127.0.0.1:5000/api/cadastros`
- Site: `http://127.0.0.1:5000/cadastros/`

