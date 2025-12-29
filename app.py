from flask import Flask, render_template, request, redirect
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)

# Nome do arquivo CSV
ARQUIVO = "estoque.csv"

# Colunas da base
COLUNAS = [
    "Endereco",
    "SKU",
    "Lote",
    "Validade",
    "Quantidade",
    "Conferente",
    "Data_Hora"
]

# Cria CSV vazio se não existir
if not os.path.exists(ARQUIVO):
    df = pd.DataFrame(columns=COLUNAS)
    df.to_csv(ARQUIVO, index=False)

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            novo_registro = {
                "Endereco": request.form.get("endereco"),
                "SKU": request.form.get("sku"),
                "Lote": request.form.get("lote"),
                "Validade": request.form.get("validade"),
                "Quantidade": request.form.get("quantidade"),
                "Conferente": request.form.get("conferente"),
                "Data_Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Lê CSV existente e adiciona novo registro
            df = pd.read_csv(ARQUIVO)
            df = pd.concat([df, pd.DataFrame([novo_registro])], ignore_index=True)
            df.to_csv(ARQUIVO, index=False)

            return redirect("/")

        return render_template("index.html")
    except Exception as e:
        return f"Erro interno: {str(e)}"

if __name__ == "__main__":
    # Porta segura para Windows
    port = 8000
    app.run(host="0.0.0.0", port=port, debug=True)
