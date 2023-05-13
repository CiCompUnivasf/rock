
function validateLogin(event) {
    event.preventDefault(); // Impede o envio do formulário

    // Obtenha os valores dos campos de usuário e senha
    var username = document.getElementById("usuario").value;
    var password = document.getElementById("senha_usuario").value;

    // Realize a validação do login
    if (username === "admin" && password === "@rock@") {
        // Obtém a URL atual
        var currentURL = new URL(window.location.href);

        // Constrói o caminho para a outra página
        var outraPaginaPath = '/static/rocksite/amostragem/tabela.html';

        // Redireciona para a outra página
        window.location.href = outraPaginaPath;
    } else {
        alert("Credenciais inválidas. Tente novamente.");
    }
}