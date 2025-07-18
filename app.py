from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/mainpage")
def mainpage():
    projetos = [
        {"imagem": "/static/image (2).png", "titulo": "Projeto 1", "descricao": "Descrição do Projeto 1"},
        {"imagem": "/static/image 6.png", "titulo": "Projeto 2", "descricao": "Descrição do Projeto 2"},
        {"imagem": "/static/image (2).png", "titulo": "Projeto 3", "descricao": "Descrição do Projeto 3"},
    ]
    return render_template("mainpage.html", projetos=projetos)


@app.route("/teste-imagem")
def teste_imagem():
    return """
    <html>
      <body>
        <h1>Teste Imagem</h1>
        <img src="/static/image (2).png" alt="Imagem">
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
