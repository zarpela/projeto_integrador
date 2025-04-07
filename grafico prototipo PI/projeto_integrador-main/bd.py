import mysql.connector as conexao

banco = conexao.connect(
    host = "localhost",
    user = "root",
    password = "murillo123",
    database= "sustentabilidade",
    autocommit=True
    )