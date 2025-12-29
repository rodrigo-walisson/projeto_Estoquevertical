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
