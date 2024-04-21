function search() {
    let livro = document.getElementById('searchInput').value;
    fetch('/api/search_livro?nome_livro=' + encodeURIComponent(livro))
    .then(response => response.text())
    .then((data) =>{

        //Limpa o conteúdo atual da tabela
        let tableBody = document.getElementById('change').getElementsByTagName('tbody')[0];
        tableBody.innerHTML = '';

        //Verifica se há dados retornados
        if (data.trim()){
            tableBody.innerHTML = data;

        } else {
            tableBody.innerHTML = '<tr><td colspan="5">Nenhum livro encontrado.</td></tr>';
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro de conexão com o servidor.');
    });
}

