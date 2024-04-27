CREATE PROCEDURE biblioteca.apply_multa()
BEGIN
    DECLARE multa DECIMAL(5,2);
    DECLARE id_emprestimo INT;
    DECLARE data_prevista DATE;
    DECLARE data_atual DATE;
    DECLARE done INT DEFAULT 0; -- Variável para controle do loop

    -- Cursor para percorrer os empréstimos em atraso
    DECLARE cursor_emprestimos CURSOR FOR
        SELECT id_emprestimo, data_prevista_devolucao
        FROM emprestimos
        WHERE status = 'emprestado' AND data_prevista_devolucao < CURDATE();
    
    -- Cursor handler
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1; -- Define done como 1 ao final do cursor

    -- Abre o cursor
    OPEN cursor_emprestimos;

    read_loop: LOOP
        FETCH cursor_emprestimos INTO id_emprestimo, data_prevista;

        IF done = 1 THEN
            LEAVE read_loop; -- Sai do loop quando done for 1
        END IF;

        -- Calcula a multa
        SET data_atual = CURRENT_DATE();
        SET multa = DATEDIFF(data_atual, data_prevista) * 0.10;

        -- Insere a multa e atualiza o status para "em atraso"
        UPDATE emprestimos SET multa = multa, status = 'em atraso' WHERE id_emprestimo = id_emprestimo;
    END LOOP;

    CLOSE cursor_emprestimos;
END
