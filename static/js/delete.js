function delete_livro(id) {
    if(confirm("Tem certeza que deseja deletar o livro com ID: " + id + "?")) {
      fetch("/api/delete", {
        method: "POST",
        body: JSON.stringify({ id_deletado: id }),
        headers: {
          "Content-Type": "application/json"
        }
      }).then(response => {
        return response.json();
      }).then(data => {
        if (data.success) {
          alert("Livro deletado com sucesso!");
          window.location.reload(); // Recarrega a página para atualizar a tabela
        } else {
          alert("Houve um erro ao deletar o livro. Por favor, tente novamente.");
        }
      }).catch(error => {
        console.error("Erro na requisição DELETE: ", error);
      });
    }
  }