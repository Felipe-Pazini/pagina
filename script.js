
function adicionarProduto() {

    let nome = document.getElementById("nomeProduto").value;
    let quantidade = document.getElementById("quantidadeProduto").value;

    if (nome == "" || quantidade == "") {
        alert("Preencha todos os campos!");
        return;
    }

    let tabela = document.getElementById("tabelaProdutos");

    tabela.innerHTML += `
        <tr>
            <td>${nome}</td>
            <td>${quantidade}</td>
            <td><button onclick="entrada(this)">+</button></td>
            <td><button onclick="saida(this)">-</button></td>
             <td><button onclick="excluirProduto(this)">🗑️</button></td>
        </tr>
    `;

    document.getElementById("nomeProduto").value = "";
    document.getElementById("quantidadeProduto").value = "";
}

function entrada(botao) {

    let linha = botao.parentNode.parentNode;

    let quantidade = linha.cells[1];

    quantidade.innerHTML = Number(quantidade.innerHTML) + 1;

}

function saida(botao) {

    let linha = botao.parentNode.parentNode;

    let quantidade = linha.cells[1];

    if (Number(quantidade.innerHTML) > 0) {

        quantidade.innerHTML = Number(quantidade.innerHTML) - 1;

    }

}
function excluirProduto(botao) {

    let linha = botao.parentNode.parentNode;

    linha.remove();

}