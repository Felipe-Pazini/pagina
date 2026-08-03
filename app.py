from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = "123"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro")
def cadastro():


    return render_template("cadastro.html")

@app.route("/home")
def home():

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="172909",
        database="almoxarifado"
    )

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template("home.html", produtos=produtos)

@app.route("/estoque")
def estoque():
    return render_template("estoque.html")

@app.route("/adicionar", methods=["POST"])
def adicionar():

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="172909",
        database="almoxarifado"
    )

    cursor = conexao.cursor()

    nome = request.form["nome"]
    quantidade = request.form["quantidade"]

    foto = request.files["foto"]

    nome_foto = foto.filename

    caminho = os.path.join("static", "image", nome_foto)

    foto.save(caminho)

    cursor.execute(
        "INSERT INTO produtos(nome, quantidade, foto) VALUES (%s, %s, %s)",
        (nome, quantidade, nome_foto)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/home")


if __name__ == "__main__":
    app.run(debug=True)

    