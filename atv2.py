from flask import Flask

app = Flask(__name__)

@app.route('/decorator') 
def home(): 
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
        <h1> Curriculo Sofia Miranda </h1>

        <h1> DADOS PARA CONTATO </h1>
        <p>Endereço: Rua: Barbosa de Resende, 142/201, Grajaú.</p>
        <p>Telefone: (31) 9 7212-0857</p>
        <p>Email: sofia.miranda0098@gmail.com<p>
         
        <h1> PERFIL </h1>
        <p>Técnica em Informática em formação, com experiência em suporte técnico, manutenção de computadores e atendimento ao cliente. Atuação focada em diagnóstico e resolução ágil de problemas.</p>

        <h1>FORMAÇÃO ACADÊMICA</h1>
         <p> Ensino Fundamental (concluído) 6oao 8o ano - Rede de Ensino Coleguium</p>
         <p>9o ano – Escola estatudal Pandiá Calógeras</p>
         <p>Ensino Médio (cursando) 1o ano – Ensino Técnico de Tecnologia da Informação -COTEMIG</p>
         <p>2o ano – Ensino Técnico de Tecnologia da Informação -COTEMIG</p>
         <p>3o ano – Ensino Técnico de Tecnologia da Informação -COTEMIG</p>

         <h1>OBJETIVO</h1>
         <p>Busco estágio em TI para atuar com suporte, infraestrutura ou desenvolvimento, aplicando meus conhecimentos na prática.</p>

         <h1>HABILIDADES TÉCNICAS:</h1>

         <h1>Suporte e Infraestrutura:</h1> 
         <p>Manutenção de hardware e software</p>
         <p>Instalação de Windows</p>
         <p>Diagnóstico de problemas</p>

         <h1>Programação</h1>
         <p>C# (lógica e aplicações básicas)</p>
         <p>Python (automação básica)</p>
         <p> MySQL (consultas simples)</p>




</body>
</html>
'''


if __name__ == '__main__':
    app.run(debug=True)
