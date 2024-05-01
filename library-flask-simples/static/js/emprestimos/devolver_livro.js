function fazer_emprestimo(id_emprestimo,id_livro) {
    //var id_livro = document.getElementById('id_livro').value;

    url = "/alunos/emprestimos/devolver_livro";
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({id_emprestimo:id_emprestimo, id_livro: id_livro})
    })

    .then (response => response.text())
    .then(message => {
        alert(message);
        window.location.reload();
    })

    .catch(error => {
        
        console.error('Erro ao fazer a devolução:', error);
        alert('Erro ao realizar a devolução');
    });
}