
from flask import Flask, render_template, request
import os

app = Flask(__name__)


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER



@app.route("/")
def inicio():
    return render_template("index.html")



@app.route("/upload", methods=["POST"])
def upload():

   
    if "arquivo" not in request.files:
        return "Nenhum arquivo foi enviado."

    arquivo = request.files["arquivo"]

    
    if arquivo.filename == "":
        return "Nenhum arquivo foi selecionado."

   
    if not arquivo.filename.lower().endswith(".pdf"):
        return "Erro: envie somente arquivos PDF."

   
    caminho = os.path.join(
        app.config["UPLOAD_FOLDER"],
        arquivo.filename
    )

    
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



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

