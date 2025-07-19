CREATE TABLE IF NOT EXISTS incidentes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    data_ocorrencia DATE NOT NULL,
    ip_origem VARCHAR(45) NOT NULL,
    status VARCHAR(20) NOT NULL,
    descricao TEXT
);