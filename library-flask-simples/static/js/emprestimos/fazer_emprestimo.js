function fazer_emprestimo(id_livro) {
    //var id_livro = document.getElementById('id_livro').value;

    url = "/alunos/livros/fazer_emprestimo";
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({id_livro: id_livro})
    })

    .then (response => response.text())
    .then(message => {
        alert(message);
        window.location.reload();
    })

    .catch(error => {
        
        console.error('Erro ao realizar o empréstimo:', error);
        alert('Erro ao realizar o empréstimo');
    });
}