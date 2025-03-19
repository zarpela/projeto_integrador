#projeto integrador engenharia de software
import mysql.connector as conexao
from prettytable import PrettyTable
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


banco = conexao.connect(
    host = "localhost",
    user = "root",
    password = "zarpela123",
    database= "sustentabilidade",
    autocommit=True
    )

cursor = banco.cursor()
def menu():
    print("="*30)
    print("- 1 -  Cadastro")
    print("-"*30)
    print("- 2 -  Estatísticas")
    print("-"*30)
    print("- 3 -  Registros")
    print("-"*30)
    print("- 4 -  Ações")
    print("-"*30)
    print("- 5 -  Gráficos")
    print("-"*30)
    print("- 6 -  Salvar")
    print("="*30)
    op = int(input("Escolha sua opção: "))
    if(op==1):
        cadastro()
    elif(op==2):
        status()
    elif(op==3):
        registros()
    elif(op==4):
        acoes()
    elif(op==5):
        graficos()
    elif(op==6):
        commitar()
    else:
        print("erro!")
        menu()

def cadastro():
    consumo = float(input("Consumo(L): "))
    nr = float(input("Não-recicláveis (KG): "))
    energia = float(input("Energia elétrica (kWh): "))
    trans = input("Tipo de transporte: ")

    if int(input("Deseja cadastrar?(0-Não, 1-Sim"))==1 :

        valores = str(consumo) + "," + str(nr) + "," +str(energia)+ ", '" +str(trans)+"'"

        sql = "INSERT INTO cadastro(consumo, nr, energia, trans) values("+valores+");"
        cursor.execute(sql)
    menu()
        
    
def status():
    print("estatistica")
    menu()
    


def registros():
    limpar()
    resultado = cursor.execute("SELECT * FROM cadastro")
    colunas = cursor.fetchall()

    if not colunas:
        print("Nenhum registro encontrado.")
        return

    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cursor.description]

    for coluna in colunas:
        tabela.add_row(coluna)

    print(tabela)
    
    menu()

    
def acoes():
    print("acoes")
    menu()
    
def graficos():
    print("graficos")
    menu()

def commitar():
    resp = bool(int(input("Quer commitar as mudanças? (0-Não, 1-Sim): ")))
    if(resp):
        banco.commit()
        banco.close()
        print("Obrigado por usar o sistema!")
    else:
        menu()

if __name__ == '__main__':
    menu()
