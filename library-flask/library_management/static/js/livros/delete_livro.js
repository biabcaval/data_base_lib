function delete_livro(id, button) {
  if (confirm("Tem certeza que deseja deletar o livro com ID: " + id + "?")) {
      button.disabled = true; // Desabilita o botão
      button.innerHTML = '<svg class="spinner" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke-width="2" stroke="#ffffff" stroke-opacity="0.5" fill="none"></circle></svg>'; // Adiciona um spinner como indicador de loading

      fetch("/api/delete_livro", {
          method: "DELETE",
          body: JSON.stringify({ id_deletado: id }),
          headers: {
              "Content-Type": "application/json"
          }
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              alert("Livro deletado com sucesso!");
              document.getElementById('row-' + id).remove(); // Remove a linha da tabela
          } else {
              alert("Houve um erro ao deletar o livro. Por favor, tente novamente.");
          }
      })
      .catch(error => {
          console.error("Erro na requisição DELETE: ", error);
          alert("Houve um erro ao processar a requisição.");
      })
      .finally(() => {
          button.disabled = false; // Habilita o botão após o processamento da requisição
          button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="1.8rem" height="1.8rem" viewBox="0 0 1024 1024"><path fill="#2B3440" d="M864 256H736v-80c0-35.3-28.7-64-64-64H352c-35.3 0-64 28.7-64 64v80H160c-17.7 0-32 14.3-32 32v32c0 4.4 3.6 8 8 8h60.4l24.7 523c1.6 34.1 29.8 61 63.9 61h454c34.2 0 62.3-26.8 63.9-61l24.7-523H888c4.4 0 8-3.6 8-8v-32c0-17.7-14.3-32-32-32m-200 0H360v-72h304z"/></svg>'; // Restaura o ícone original do botão
      });
  }
}
