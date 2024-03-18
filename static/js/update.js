function openModal(idLivro, autor, titulo, genero) {
  document.getElementById('idLivroInput').value = idLivro;
  document.getElementById('autorInput').value = autor;
  document.getElementById('tituloInput').value = titulo;
  document.getElementById('generoInput').value = genero;
  document.getElementById('updateModal').classList.add('modal-open');
}

function closeModal() {
  document.getElementById('updateModal').classList.remove('modal-open');
}

function updateLivro() {
  var form = document.getElementById('updateForm');
  var formData = new FormData(form);
  var idLivro = formData.get('id_livro');

  fetch('/api/update/' + idLivro, {
    method: 'POST',
    body: formData,

  })
  .then(response => response.json())
  .then(data => {
    if(data.success) {
      alert('Livro atualizado com sucesso.');
      closeModal();
      location.reload(); // Opcional: recarregar a página para ver as atualizações
    } else {
      alert('Falha ao atualizar livro.');
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
}