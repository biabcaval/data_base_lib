DELIMITER //

CREATE PROCEDURE realizar_emprestimo(
    IN id_aluno INT,
    IN id_livro INT,
    OUT mensagem VARCHAR(100)
)

BEGIN
    DECLARE num_emprestimos INT;
    DECLARE emprestimo_atrasado INT;

    SELECT COUNT(*) INTO num_emprestimos
    FROM emprestimos
    WHERE id_aluno = id_usuario AND status = 'emprestado';