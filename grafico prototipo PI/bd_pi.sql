-- Cria a tabela 'usuarios' caso ela não exista
CREATE TABLE IF NOT EXISTS usuarios ( 
    u_id INTEGER AUTO_INCREMENT PRIMARY KEY,  -- Identificador único para cada usuário (chave primária, auto incremento)
    u_un VARCHAR(50) NOT NULL UNIQUE,         -- Nome de usuário (único, não pode ser nulo)
    u_senha VARCHAR(50) NOT NULL              -- Senha do usuário (não pode ser nula)
);

-- Cria a tabela 'sustentabilidade' caso ela não exista
CREATE TABLE IF NOT EXISTS sustentabilidade (
    s_id INTEGER AUTO_INCREMENT PRIMARY KEY,  -- Identificador único para cada registro de sustentabilidade (auto incremento)
    su_id INTEGER NOT NULL,                   -- ID do usuário relacionado (não pode ser nulo)
    s_data DATE NOT NULL,                      -- Data da entrada de dados (não pode ser nula)
    s_agua FLOAT NOT NULL,                     -- Quantidade de água consumida (não pode ser nula)
    s_reciclaveis FLOAT NOT NULL,              -- Quantidade de não-recicláveis descartados (não pode ser nula)
    s_energia FLOAT NOT NULL,                  -- Consumo de energia (não pode ser nulo)
    s_transporte VARCHAR(30) NOT NULL,         -- Meio de transporte utilizado (não pode ser nulo)
    CONSTRAINT fk_sustentabilidade_usuario     -- Define uma restrição de chave estrangeira
        FOREIGN KEY (su_id)                    -- Relaciona 'su_id' da tabela sustentabilidade com 'u_id' da tabela usuarios
        REFERENCES usuarios (u_id) 
        ON DELETE CASCADE                      -- Se um usuário for deletado, os registros de sustentabilidade dele também serão deletados
);

-- Insere um usuário padrão com nome de usuário 'admin' e senha 'admin'
#INSERT INTO usuarios (u_un, u_senha) VALUES ("admin", "admin");

-- Insere um registro de sustentabilidade para o usuário com ID 1 (comentado para não executar automaticamente)
#INSERT INTO sustentabilidade (su_id, s_data, s_agua, s_reciclaveis, s_energia, s_transporte) 
# VALUES (1, "2025-03-29", 30, 45, 60, "carro");

-- Seleciona todos os registros da tabela 'sustentabilidade' (comentado)
# SELECT * FROM sustentabilidade;

-- Seleciona todos os registros da tabela 'usuarios' (comentado)
#SELECT * FROM usuarios;

-- Deleta o usuário com ID 1 da tabela 'usuarios' (comentado para evitar exclusão acidental)
# DELETE FROM usuarios WHERE u_id = 1;
