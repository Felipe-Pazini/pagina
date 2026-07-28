
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


=======
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Conexão com o MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="172909",
    database="almoxarifado"
)

cursor = conexao.cursor()

if conexao.is_connected():
    print("Conectado ao MySQL!")

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

