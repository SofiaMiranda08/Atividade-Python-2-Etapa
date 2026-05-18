from flask import Flask

app = Flask(__name__)

@app.route('/decorator') 
def home(): 
    return '''
    <h1> O que é um decorator em Python </h1>
    Decorators em Python são funções que modificam ou estendem o comportamento de outras funções, métodos ou classes sem alterar seu código original. Eles atuam como "embalagens inteligentes" (wrappers), permitindo executar ações antes ou depois da função principal, ideal para logging, controle de acesso ou medição de performance 

    <h1>  Para que ele serve  </h1>
    Decorators em Python servem para modificar ou estender o comportamento de funções, métodos ou classes de forma elegante, reutilizável e sem alterar o código original. Eles permitem adicionar funcionalidades extras (como logs, autorização ou controle de tempo) "embrulhando" uma função com outra, sendo aplicados com a sintaxe @nome_do_decorator
     

    <h1> Como ele é utilizado no Flask (exemplo: @app.route) </h1>
    No Flask, o decorator @app.route é utilizado para mapear URLs específicas a funções Python. Ele diz ao Flask: "quando o usuário acessar este endereço, execute esta função".O decorator transforma uma função comum em uma view function (função de visualização) que gerencia uma rota específica da aplicação web 
'''


if __name__ == '__main__':
    app.run(debug=True)
