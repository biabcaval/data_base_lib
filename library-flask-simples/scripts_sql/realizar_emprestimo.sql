
CREATE PROCEDURE biblioteca.realizar_emprestimo(
    IN p_id_emprestimo INT,
    IN p_id_aluno INT,
    IN p_id_livro INT
)
BEGIN
                -- Inserir o novo empréstimo
    INSERT INTO emprestimos (id_emprestimo, id_aluno, id_livro, data_emprestimo, data_prevista_devolucao, status)
    VALUES (p_id_emprestimo, p_id_aluno, p_id_livro, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 15 DAY), 'emprestado');
                -- Atualizar o status do livro para indisponível
    update livros SET disponivel = 0 where id_livro = p_id_livro;
END