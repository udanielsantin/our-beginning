from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/mainpage")
def mainpage():
    import datetime
    projetos = [
        {"imagem": "/static/image (2).png", "titulo": "Projeto 1", "descricao": "Descrição do Projeto 1"},
        {"imagem": "/static/image 6.png", "titulo": "Projeto 2", "descricao": "Descrição do Projeto 2"},
        {"imagem": "/static/image (2).png", "titulo": "Projeto 3", "descricao": "Descrição do Projeto 3"},
    ]
    # Data alvo
    target = datetime.datetime(2025, 5, 20, 22, 12, 0)
    now = datetime.datetime.now()
    diff = target - now
    # Calcular anos, meses, dias, horas, minutos, segundos
    years = target.year - now.year
    months = target.month - now.month
    days = target.day - now.day
    hours = target.hour - now.hour
    minutes = target.minute - now.minute
    seconds = target.second - now.second

    if seconds < 0:
        seconds += 60
        minutes -= 1
    if minutes < 0:
        minutes += 60
        hours -= 1
    if hours < 0:
        hours += 24
        days -= 1
    if days < 0:
        # Ajusta mês anterior
        prev_month = (now.month - 1) if now.month > 1 else 12
        prev_year = now.year if now.month > 1 else now.year - 1
        days_in_prev_month = (datetime.datetime(prev_year, prev_month + 1, 1) - datetime.datetime(prev_year, prev_month, 1)).days
        days += days_in_prev_month
        months -= 1
    if months < 0:
        months += 12
        years -= 1

    timer_str = f"{years} anos, {months} meses, {days} dias, {hours} horas, {minutes} minutos, {seconds} segundos"
    return render_template("mainpage.html", projetos=projetos, timer_str=timer_str)


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
