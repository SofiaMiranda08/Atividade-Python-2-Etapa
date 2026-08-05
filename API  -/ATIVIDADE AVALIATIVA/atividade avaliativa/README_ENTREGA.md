# Atividade — API de Cadastros com Thunder Client

Este pacote contém o projeto Flask, o banco de dados no estado final da atividade,
os corpos JSON usados nos requests e os prints de comprovação.

## Como executar

No terminal, dentro desta pasta:

```bash
python -m venv .venv
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Linux/macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Depois acesse: http://127.0.0.1:5000/cadastros/

## Requests da atividade

Todos os requests usam o cabeçalho `Content-Type: application/json`.

1. `POST http://127.0.0.1:5000/api/cadastros` com `requests/01_ariana_grande.json`.
2. `POST http://127.0.0.1:5000/api/cadastros` com `requests/02_miley_cyrus.json`.
3. `PUT http://127.0.0.1:5000/api/cadastros/1` com `requests/03_atualiza_pessoa.json`.
4. `DELETE http://127.0.0.1:5000/api/cadastros/2` (sem body).
5. `GET http://127.0.0.1:5000/api/cadastros` para conferir o resultado final.

Os dados enviados estão organizados como objetos JSON, equivalentes a dicionários
em Python.

## Evidências

Os arquivos estão em `print_atividade/`:

- `add_pessoa1.png`
- `add_pessoa2.png`
- `atualiza_pessoa.png`
- `exibicao_final.png`

## Observação sobre o questionário

O ZIP recebido continha apenas o projeto e o arquivo `Aula14.txt`; não havia um
questionário separado. O arquivo `QUESTIONARIO_RESPONDIDO.md` reúne as respostas
conceituais e práticas que podem ser respondidas com o material anexado.

