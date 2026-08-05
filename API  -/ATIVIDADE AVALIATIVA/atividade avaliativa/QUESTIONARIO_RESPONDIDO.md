# Questionário respondido — Aula 14

1. **Qual método HTTP lista todos os cadastros?**  
   `GET /api/cadastros`.

2. **Qual método cria uma pessoa?**  
   `POST /api/cadastros`, enviando um objeto JSON no body.

3. **Qual método atualiza uma pessoa?**  
   `PUT /api/cadastros/<id>`. Nesta atividade foi usado o ID 1.

4. **Qual método exclui uma pessoa?**  
   `DELETE /api/cadastros/<id>`. Nesta atividade foi usado o ID 2.

5. **Qual cabeçalho deve ser usado no POST e no PUT?**  
   `Content-Type: application/json`.

6. **Por que os dados devem estar organizados como dicionário?**  
   Porque o body JSON é formado por pares de chave e valor. No Flask, esse objeto
   é recebido por `request.get_json()` como um dicionário Python.

7. **Quem completa logradouro, bairro, cidade e estado?**  
   O serviço `brasilapi_cep.py` consulta a Brasil API com o CEP e devolve os dados
   de endereço para a API de cadastros.

8. **Onde os dados ficam armazenados?**  
   No banco SQLite `cadastros.db`, por meio do model `Cadastro` e do SQLAlchemy.

9. **Qual é a função de cada camada?**

   - Model: representa e persiste os cadastros.
   - Service: consulta dados do CEP na Brasil API.
   - Controller: recebe requisições e devolve HTML ou JSON.
   - View: apresenta as páginas HTML ao usuário.

10. **Quais códigos de resposta são esperados?**

    - POST criado com sucesso: `201 Created`.
    - GET ou PUT bem-sucedido: `200 OK`.
    - DELETE bem-sucedido: `204 No Content`.
    - Dados inválidos: `400 Bad Request`.
    - Cadastro inexistente: `404 Not Found`.

