from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = "123"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="172909",
        database="almoxarifado"
    )

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE email = %s AND senha = %s",
        (email, password)
    )

    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    if usuario:
        session["usuario"] = email
        session["cargo"] = usuario[3]

        return redirect("/home")
    else:
        return render_template(
            "index.html",
            erro="E-mail ou senha incorretos!"
        )


@app.route("/cadastro")
def cadastro():

    if session.get("cargo") != "admin":
        return "Acesso negado!"

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


@app.route("/cadastrar_usuario", methods=["POST"])
def cadastrar_usuario():

    email = request.form["email"]
    senha = request.form["password"]
    cargo = request.form["gender"]

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="172909",
        database="almoxarifado"
    )

    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO usuarios (email, senha, cargo) VALUES (%s, %s, %s)",
        (email, senha, cargo)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

    