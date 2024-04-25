function gerar_relatorio() {
    fetch('/api/gerar_relatorio')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        exibir_relatorio_na_tabela(data);
        const novaJanela = window.open('', '_blank');
        const corpoHTML = '<!DOCTYPE html>' +
                          '<html lang="pt-BR">' +
                          '<head>' +
                          '<meta charset="UTF-8">' +
                          '<title>Relatório de Livros</title>' +
                          '</head>' +
                          '<body>' +
                          '<h1>Relatório de Livros</h1>' +
                          '<div id="relatorio"></div>' +
                          '</body>' +
                          '</html>';
        novaJanela.document.write(corpoHTML);
        const divRelatorio = novaJanela.document.getElementById('relatorio');
        divRelatorio.appendChild(exibir_relatorio_na_tabela(data));
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao gerar o relatório.');
    });
}

function exibir_relatorio_na_tabela(data) {
    const tabela = document.createElement('table');
    const cabecalho = tabela.createTHead();
    const linha_cabecalho = cabecalho.insertRow();

     const thIdLivro = document.createElement('th');
    thIdLivro.textContent = 'id_livro';
    linha_cabecalho.appendChild(thIdLivro);

 
    ['titulo', 'autor', 'genero'].forEach(chave => {
        const th = document.createElement('th');
        th.textContent = chave;
        linha_cabecalho.appendChild(th);
    });

    const corpo_tabela = tabela.createTBody();
    data.forEach(item => {
        const linha = corpo_tabela.insertRow();

        const celulaIdLivro = linha.insertCell();
        celulaIdLivro.textContent = item['id_livro'];
        const celulaTitulo = linha.insertCell();
        celulaTitulo.textContent = item['titulo'];
        const celulaAutor = linha.insertCell();
        celulaAutor.textContent = item['autor'];
        const celulaGenero = linha.insertCell();
        celulaGenero.textContent = item['genero'];
    });

    return tabela; 
}