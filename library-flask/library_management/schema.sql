CREATE TABLE `livros` (
  `id_livro` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) NOT NULL,
  `autor` varchar(100) NOT NULL,
  `genero` varchar(100) NOT NULL,
  `disponivel` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id_livro`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `emprestimos` (
  `id_emprestimo` int NOT NULL AUTO_INCREMENT,
  `aluno` varchar(100) NOT NULL,
  `id_livro` int NOT NULL,
  `data_emprestimo` date NOT NULL,
  `data_devolucao` date NOT NULL,
  PRIMARY KEY (`id_emprestimo`),
  KEY `id_livro` (`id_livro`),
  CONSTRAINT `emprestimos_ibfk_1` FOREIGN KEY (`id_livro`) REFERENCES `livros` (`id_livro`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;