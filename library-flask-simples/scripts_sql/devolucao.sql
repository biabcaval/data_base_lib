CREATE PROCEDURE biblioteca.devolucao(
in p_id_emprestimo VARCHAR(5),
in p_id_livro INT
)
begin
	update emprestimos set status = 'devolvido' where id_emprestimo = p_id_emprestimo;
	update emprestimos set data_real_devolucao = CURDATE() where id_emprestimo = p_id_emprestimo;
	update livros set disponivel = 1 where id_livro = p_id_livro;
END