
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Pasta onde os arquivos enviados serão salvos
UPLOAD_FOLDER = "uploads"

# Cria a pasta automaticamente caso ela não exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Página principal
@app.route("/")
def inicio():
    return render_template("index.html")


# Recebe o PDF enviado pelo formulário
@app.route("/upload", methods=["POST"])
def upload():

    # Verifica se o formulário enviou um arquivo
    if "arquivo" not in request.files:
        return "Nenhum arquivo foi enviado."

    arquivo = request.files["arquivo"]

    # Verifica se o usuário escolheu um arquivo
    if arquivo.filename == "":
        return "Nenhum arquivo foi selecionado."

    # Aceita somente PDF
    if not arquivo.filename.lower().endswith(".pdf"):
        return "Erro: envie somente arquivos PDF."

    # Caminho onde o arquivo será salvo
    caminho = os.path.join(
        app.config["UPLOAD_FOLDER"],
        arquivo.filename
    )

    # Salva o arquivo
    arquivo.save(caminho)

    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Análise de Notas</title>
    </head>

    <body>

        <h1>PDF enviado com sucesso! ✅</h1>

        <p>Arquivo recebido:</p>

        <strong>{arquivo.filename}</strong>

        <br><br>

        <p>O próximo passo será analisar as notas do PDF.</p>

        <a href="/">Voltar</a>

    </body>
    </html>
    """


# Inicia o servidor
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

