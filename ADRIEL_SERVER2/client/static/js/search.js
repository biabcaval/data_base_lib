function search() {
    let livro = document.getElementById('searchInput').value;
    fetch('/api/search?nome_livro=' + encodeURIComponent(livro)).then(response => response.text()).then((data) =>{
        document.getElementById('change').innerHTML = data;
    });
}

