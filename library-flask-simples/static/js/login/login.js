function login() {
    console.log('Função login chamada');
    let matricula = document.getElementById('matricula').value;
    let senha = document.getElementById('senha').value;

    //vai enviar os dados do formulário via solicitação GET
    fetch(`/login?matricula=${matricula}&senha=${senha}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.redirected) {
            //redireciona para a página de livros 
            //se as informações forem encontradas 
            window.location.href = response.url; 
        } else {
            console.error('Erro nas informações de login:', response.statusText);
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}
