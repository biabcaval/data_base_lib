function search() {
    
    console.log('Função search chamada');
    let livro = document.getElementById('searchInput').value;
    console.log('Livro:', livro);
    fetch('/api/search_livro?nome_livro=' + encodeURIComponent(livro),{
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
})
        .then(response => response.text())
        .then((data) => {
            console.log('Dados recebidos:', data);
            let tableBody = document.getElementById('change');
            tableBody.innerHTML = data;
            //document.getElementById('change').innerHTML = data;
        })
        .catch(error => {
            console.error('Erro:', error);
        });
}
