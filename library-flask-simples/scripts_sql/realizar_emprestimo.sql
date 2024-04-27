CREATE PROCEDURE biblioteca.realizar_emprestimo(
    IN id_emprestimo INT,
    IN id_aluno INT,
    IN id_livro INT,
    IN data_emprestimo DATE,
    OUT mensagem VARCHAR(100)
)

BEGIN
    DECLARE num_emprestimos INT;
    DECLARE emprestimo_atrasado INT;

    -- Conta o num de emprestimos do aluno
    SELECT COUNT(*) INTO num_emprestimos
    FROM emprestimos
    WHERE id_aluno = id_aluno AND status IN ('emprestado','em atraso');

    -- Verifica se o aluno já atingiu o limite de empréstimos
    IF num_emprestimos >= 2 THEN
        SET mensagem = 'O aluno já atingiu o limite de empréstimos';
    ELSE
        -- Verifica se  o já tem um empréstimo em atraso
        SELECT COUNT(*) INTO emprestimo_atrasado
        FROM emprestimo_atrasados
        WHERE id_aluno = id_aluno AND status = 'em atraso';

        IF emprestimo_atrasado > 0 THEN
            SET mensagem = 'Você possui um empréstimo em atraso e não pode realizar um novo empréstimo';
        ELSE
            -- Inserir o novo empréstimo
            INSERT INTO emprestimos (id_emprestimo, id_aluno, id_livro, data_emprestimo, data_prevista_devolucao, status)
            VALUES (id_emprestimo, id_aluno, id_livro, data_emprestimo, DATE_ADD(data_emprestimo, INTERVAL 15 DAY), 'emprestado');
            SET mensagem = 'Empréstimo realizado com sucesso';
        END IF;
    END IF;
END 