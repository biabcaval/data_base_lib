CREATE PROCEDURE biblioteca.add_livro(
    IN p_titulo VARCHAR(100),    
    IN p_autor VARCHAR(100),
    IN p_genero VARCHAR(100),
    OUT p_mensagem VARCHAR(100)
)
BEGIN
    IF EXISTS (SELECT 1 FROM livros WHERE titulo = p_titulo) THEN
        SET p_mensagem = 'Livro já existe';
    ELSE
        BEGIN
            INSERT INTO livros (titulo, autor, genero)
            VALUES (p_titulo, p_autor, p_genero);
            SET p_mensagem = 'Livro adicionado com sucesso';
            SELECT 'Valor de p_mensagem atribuído com sucesso' AS Debug;
        END;
    END IF;
END