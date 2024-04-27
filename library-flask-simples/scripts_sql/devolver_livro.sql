CREATE PROCEDURE biblioteca.devolver_livro(
    IN id_emprestimo INT,
    IN data_devolucao DATE,
    OUT mensagem VARCHAR(100)
)

BEGIN
    DECLARE data_devolucao DATE;
    DECLARE multa DECIMAL(5,2);
    DECLARE data_prevista DATE;
    DECLARE status_emprestimo ENUM('emprestado','devolvido','em atraso');
    DECLARE emprestimo_existe INT;
    DECLARE id_livro_emprestado INT;

    -- Verifica se o empréstimo existe
    SELECT COUNT(*) INTO emprestimo_existe
    FROM emprestimos
    WHERE id_emprestimo = id_emprestimo;

    IF emprestimo_existe = 0 THEN
        SET mensagem = 'Empréstimo não encontrado';
    ELSE
        -- Verifica se o livro já foi devolvido
        SELECT status INTO status_emprestimo
        FROM emprestimos
        WHERE id_emprestimo = id_emprestimo;


        IF status_emprestimo = 'devolvido' THEN
            SET mensagem = 'Livro já devolvido';
        ELSE
            -- Obter o ID do livro associado ao emprestimo
            SELECT id_livro INTO id_livro_emprestado
            FROM emprestimos
            WHERE id_emprestimo = id_emprestimo;

            -- Atualiza o empréstimo
            UPDATE emprestimos
            SET data_real_devolucao = data_devolucao, status = 'devolvido'
            WHERE id_emprestimo = id_emprestimo;

            -- Atualiza a disponibilidade do livro
            UPDATE livros SET disponivel = 1 WHERE id_livro = id_livro_emprestado;

            SET mensagem = 'Devolução realizada com sucesso';
        END IF;
    END IF;
END