DELIMITER //

CREATE PROCEDURE apply_multa()

BEGIN
    DECLARE multa DECIMAL(5,2);
    DECLARE id_emprestimo INT;
    DECLARE data_prevista DATE;
    DECLARE data_atual DATE;

    -- Cursor para percorrer os emp em atraso
    DECLARE cursor_emprestimos CURSOR FOR
        SELECT id_emprestimo, data_prevista_devolucao
        FROM emprestimos
        WHERE status = 'emprestado' AND data_prevista_devolucao < CURDATE();
    
    -- Cursor handler
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Abre o cursor
    OPEN cursor_emprestimos;
    set done = FALSE;


    read_loop: LOOP
        FETCH cursor_emprestimos INTO id_emprestimo, data_prevista;

        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calcula a multa

        SET data_atual = CURRENT_DATE();
        SET multa = DATEDIFF(data_atual, data_prevista) * 0.10;

        -- Insere a multa
        UPDATE emprestimos SET multa = multa WHERE id_emprestimo = id_emprestimo;

    END LOOP;


    close cursor_emprestimos;

END //

DELIMITER;