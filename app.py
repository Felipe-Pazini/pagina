from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Rotas
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/estoque")
def estoque():
    return render_template("estoque.html")

# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)


