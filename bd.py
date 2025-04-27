import mysql.connector as conexao

banco = conexao.connect(
    host = "localhost",
    user = "root",
    password = "guilherme123",
    database= "sustentabilidade",
    autocommit=True
    )