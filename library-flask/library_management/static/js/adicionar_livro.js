document.getElementById('btnAbrirModal').addEventListener('click', function() {
    document.getElementById('addLivroModal').classList.add('modal-open');
  });
  

function enviarFormulario() {
    let form = document.getElementById('addLivroForm');
    let formDataAddLivro = new FormData(form);

    let data = {
        titulo: formDataAddLivro.get('titulo'),
        autor: formDataAddLivro.get('autor'),
        genero: formDataAddLivro.get('genero')
    };

    fetch('/api/adicionar_livro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Livro cadastrado com sucesso.');
            closeModal(); // Fechar o modal após cadastrar o livro
            location.reload(); // Opcional: recarregar a página para ver as atualizações
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro de conexão com o servidor.');
    });
}

// so enviar o form qnd dar o click uma vez
document.onload = function() {
    document.getElementById('btnSalvarLivro').addEventListener('click', function() {
        enviarFormulario();
    });
}



function closeModal() {
    document.getElementById('addLivroModal').classList.remove('modal-open');
    // Limpar os campos do formulário após fechar o modal, se necessário
    document.getElementById('autorInput').value = '';
    document.getElementById('tituloInput').value = '';
    document.getElementById('generoInput').value = '';
}
