<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime
import os

app = Flask(__name__)

CSV_FILE = "estoque.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Endereco", "SKU", "Lote", "Validade", "Quantidade", "Conferente", "Data_Hora"])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        endereco = request.form.get("endereco")
        sku = request.form.get("sku")
        lote = request.form.get("lote")
        validade = request.form.get("validade")
        quantidade = request.form.get("quantidade")
        conferente = request.form.get("conferente")
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([endereco, sku, lote, validade, quantidade, conferente, data_hora])

        return redirect(url_for('index'))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
=======
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
>>>>>>> 312fc4c553f03576468bbf7e6512f4bd9f267593
