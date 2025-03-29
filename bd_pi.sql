
CREATE TABLE IF NOT EXISTS usuarios (
    u_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    u_un VARCHAR(50) NOT NULL UNIQUE,
    u_senha VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS sustentabilidade (
    s_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    su_id INTEGER NOT NULL,
    s_data DATE NOT NULL,
    s_agua FLOAT NOT NULL,
    s_reciclaveis FLOAT NOT NULL,
    s_energia FLOAT NOT NULL,
    s_transporte VARCHAR(30) NOT NULL,
    CONSTRAINT fk_sustentabilidade_usuario FOREIGN KEY (su_id) REFERENCES usuarios (u_id) ON DELETE CASCADE
);

insert into usuarios(u_un, u_senha) values("admin", "admin");

#insert into sustentabilidade(su_id, s_data, s_agua, s_reciclaveis, s_energia, s_transporte) values(1, "2025-03-29", 30, 45, 60, "carro");

#select * from sustentabilidade;
select * from usuarios;
#delete from usuarios where u_id=1;