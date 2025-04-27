import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import json
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import date
import bd

ctk.set_appearance_mode("Dark")

altura = 400
largura = 400

janela_principal = ctk.CTk()
janela_principal.title("Sistema de Sustentabilidade")
janela_principal.geometry("650x400")
janela_principal.resizable(False, False)


#-----Frames da Janela Principal-----
frame1 = ctk.CTkFrame(master=janela_principal,
                          width=altura, 
                          height=largura,
                          fg_color="#ffffff", 
                          bg_color="#ffffff")
frame1.place(x=0, y=0)

frame2 = ctk.CTkFrame(janela_principal,
                          width=250,
                          height=400,
                          fg_color="#cccccc", 
                          bg_color="#cccccc")
frame2.place(x=400, y=0)



#----Atribuir cores nas estatísticas-----
def criar_bloco_estatistica_agua(master, titulo, valor, mensagem, y_pos):
        cor = "green" if valor >= 0 and valor <=100 else "yellow" if valor > 100 and valor <= 150 else "red"

        texto = ctk.CTkLabel(master, 
                            text=f"{titulo.upper()} -> {mensagem}", 
                            text_color="black",
                            font=("Arial", 12))
        texto.place(x=95, y=y_pos)

        entrada = ctk.CTkEntry(master, 
                            corner_radius=50,
                            border_color=cor,
                            placeholder_text=f"{valor}",
                            width=75)
        entrada.configure(state="readonly")
        entrada.place(x=15, y=y_pos) 
        
def criar_bloco_estatistica_reciclaveis(master, titulo, valor, mensagem, y_pos):
        cor = "green" if valor >= 0.5 and valor < 0.95 else "yellow" if valor >= 0.95 and valor <= 1.25 else "red"

        texto = ctk.CTkLabel(master, 
                            text=f"{titulo.upper()} -> {mensagem}", 
                            text_color="black",
                            font=("Arial", 12))
        texto.place(x=95, y=y_pos)

        entrada = ctk.CTkEntry(master, 
                            corner_radius=50,
                            border_color=cor,
                            placeholder_text=f"{valor}",
                            width=75)
        entrada.configure(state="readonly")
        entrada.place(x=15, y=y_pos) 

def criar_bloco_estatistica_energia(master, titulo, valor, mensagem, y_pos):
        cor = "green" if valor >= 2.5 and valor <= 4.5 else "yellow" if valor > 4.5 and valor <= 6 else "red"

        texto = ctk.CTkLabel(master, 
                            text=f"{titulo.upper()} -> {mensagem}", 
                            text_color="black",
                            font=("Arial", 12))
        texto.place(x=95, y=y_pos)

        entrada = ctk.CTkEntry(master, 
                            corner_radius=50,
                            border_color=cor,
                            placeholder_text=f"{valor}",
                            width=75)
        entrada.configure(state="readonly")
        entrada.place(x=15, y=y_pos) 

def criar_bloco_estatistica_transporte(master, titulo, valor, mensagem, y_pos):
        cor = "green" if valor == 0  else "yellow" if valor >=0.25 and valor <= 0.5 else "red"

        texto = ctk.CTkLabel(master, 
                            text=f"{titulo.upper()} -> {mensagem}", 
                            text_color="black",
                            font=("Arial", 12))
        texto.place(x=95, y=y_pos)

        entrada = ctk.CTkEntry(master, 
                            corner_radius=50,
                            border_color=cor,
                            placeholder_text=f"{valor}",
                            width=75)
        entrada.configure(state="readonly")
        entrada.place(x=15, y=y_pos) 
    
#-----Mudar Abas-----
def mudar_aba(aba):
    for widget in frame1.winfo_children():
        widget.destroy()
    
    #-----Aba Adicionar Registros-----
    if aba == "Adicionar Registros":

        botao_adiconarRegistro.configure(fg_color="#363434")
        botao_registros.configure(fg_color="#686564")
        botao_acoes.configure(fg_color="#686564")
        botao_graficos.configure(fg_color="#686564")
        botao_estatistica.configure(fg_color="#686564")
        
        texto_addRegistros = ctk.CTkLabel(frame1, 
                     text="Adicionar Registros", 
                     text_color="black",
                     font=("Arial", 18))
        texto_addRegistros.place(x=135, y=30)
        
        #-----Texto e entrada do campo agua-----
        texto_consumoAgua = ctk.CTkLabel(frame1, 
                     text="Consumo de água (L):", 
                     text_color="black",
                     font=("Arial", 12))
        texto_consumoAgua.place(x=110, y=75)
        
        entrada_agua = ctk.CTkEntry(frame1, 
                                    corner_radius=50,
                                    border_color="Grey",
                                    width=200)
        entrada_agua.place(x=110, y=100)
        
        #-----Texto e entrada da geração de resíduos-----
        texto_geracaoResiduos = ctk.CTkLabel(frame1,
                                            text="Não recicláveis (kg):",
                                            text_color="black",
                                            font=("Arial", 12))
        texto_geracaoResiduos.place(x=110, y=135)
        
        entrada_geracaoResiduos= ctk.CTkEntry(frame1,
                                            corner_radius=50, 
                                            border_color="Grey",
                                            width=200)
        entrada_geracaoResiduos.place(x=110, y=160)
        
        #-----Texto e entrada da energia gasta-----
        texto_energiaGasta = ctk.CTkLabel(frame1, 
                                            text="Energia elétrica (KWh):", 
                                            text_color="black",
                                            font=("Arial", 12))
        texto_energiaGasta.place(x=110, y=195)
        
        entrada_energiaGasta = ctk.CTkEntry(frame1, 
                                            corner_radius=50,
                                            border_color="Grey",
                                            width=200)
        entrada_energiaGasta.place(x=110, y=220)
        
        #-----Texto e entrada do tipo de transporte-----
        texto_tipoTransporte = ctk.CTkLabel(frame1,
                                            text="Tipo de transporte utilizado:",
                                            text_color="black",
                                            font=("Arial", 12))
        texto_tipoTransporte.place(x=110, y=255)
        
        transportes = ["Transporte Público", "Bicicleta", "Caminhada", "Carona", "Carro Particular", "Moto Particular"]
        entrada_tipoTransporte = ctk.CTkComboBox(frame1,
                                            values=transportes, 
                                            corner_radius= 15,
                                            justify="left",
                                            border_color="Grey",
                                            width=200)
        entrada_tipoTransporte.place(x=110, y=280)
        
        #-----Botão adicionar registros-----
        botao_addResgistros = ctk.CTkButton(frame1, 
                                            text="Cadastrar", 
                                            fg_color="#474444", 
                                            corner_radius=50,
                                            width= 145,
                                            height= 35,
                                            command=lambda: adicionar_dados())
        botao_addResgistros.place(x=135, y=330)

        # -----Função para adicionar os dados ao banco de dados-----
        def adicionar_dados():
            add_agua = entrada_agua.get()
            add_residuos = entrada_geracaoResiduos.get()
            add_energia = entrada_energiaGasta.get()
            add_transporte = entrada_tipoTransporte.get()
            cursor = bd.banco.cursor()
            try:
                # Verifica se os campos estão preenchidos
                if not add_agua or not add_residuos or not add_energia or not add_transporte:
                    tk.messagebox.showerror("Erro", "Preencha todos os campos.")
                    return
                else:
                    dados = (
                        int(1),
                        #data em formato YYYY-MM-DD
                        date.today().strftime("%Y-%m-%d"),
                        float(add_agua),
                        float(add_residuos),
                        float(add_energia),
                        add_transporte
                    )
                    cursor.execute("INSERT INTO sustentabilidade (su_id, s_data, s_agua, s_reciclaveis, s_energia, s_transporte) VALUES (%s, %s, %s, %s, %s, %s)", dados)
                    bd.banco.commit()
                    entrada_agua.delete(0, tk.END)
                    entrada_geracaoResiduos.delete(0, tk.END)
                    entrada_energiaGasta.delete(0, tk.END)
                    entrada_tipoTransporte.set("")
                    tk.messagebox.showinfo("Cadastro", "Dados cadastrados com sucesso!")
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao adicionar dados: {e}")
            finally:
                cursor.close()
                # Limpa os campos após o cadastro
                
            
    
    #-----Aba "Consultar"-----
    elif aba == "Consultar":
        
        botao_adiconarRegistro.configure(fg_color="#686564")
        botao_registros.configure(fg_color="#363434")
        botao_acoes.configure(fg_color="#686564")
        botao_graficos.configure(fg_color="#686564")
        botao_estatistica.configure(fg_color="#686564")
        
        # Função para carregar os dados do JSON
        def carregar_dados():
            try:
        # Consulta ao banco de dados para obter os dados no formato JSON
                cursor = bd.banco.cursor()
                cursor.execute("""
                    SELECT JSON_ARRAYAGG(
                    JSON_OBJECT(
                        'Id', s_id,
                        'Data', s_data,
                        'Consumo de Agua', s_agua,
                        'Nao Reciclaveis', s_reciclaveis,
                        'Energia Eletrica', s_energia,
                        'Tipo Transporte', s_transporte
                        )
                    ) AS dados_json
                    FROM sustentabilidade;
                """)
                resultado = cursor.fetchone()
                #print(resultado)
        
        # Verifica se há dados retornados
                if resultado and resultado[0]:
                    dados = json.loads(resultado[0])  # Converte o JSON retornado para um objeto Python
                    for item in tabela.get_children():
                        tabela.delete(item)
                    for item in dados:
                        tabela.insert("", "end", values=(
                        item.get("Id", ""),
                        item.get("Consumo de Agua", ""),
                        item.get("Nao Reciclaveis", ""),
                        item.get("Energia Eletrica", ""),
                        item.get("Tipo Transporte", ""),
                        item.get("Data", "")
                ))
                else:
                    tk.messagebox.showinfo("Aviso", "Nenhum dado encontrado.")
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")
    
                
        #Função pegar valor, ler BD (atualmente .json) e depois retornar consulta
        def Consulta(entradaId):
            try:
                entrada_idInt = int(entrada_id.get())  # Obtém o ID inserido pelo usuário
                cursor = bd.banco.cursor()
                
                # Consulta ao banco de dados para obter os dados no formato JSON
                cursor.execute(f"""
                    SELECT JSON_ARRAYAGG(
                        JSON_OBJECT(
                            'Id', s_id,
                            'Data', s_data,
                            'Consumo de Agua', s_agua,
                            'Nao Reciclaveis', s_reciclaveis,
                            'Energia Eletrica', s_energia,
                            'Tipo Transporte', s_transporte
                        )
                    ) AS dados_json
                    FROM sustentabilidade
                    WHERE s_id = {entrada_idInt};
                """)
                resultado = cursor.fetchone()
                
                # Verifica se há dados retornados
                if resultado and resultado[0]:
                    dados = json.loads(resultado[0])  # Converte o JSON retornado para um objeto Python
                    for item in tabela.get_children():
                        tabela.delete(item)
                    for item in dados:
                        tabela.insert("", "end", values=(
                            item.get("Id", ""),
                            item.get("Consumo de Agua", ""),
                            item.get("Nao Reciclaveis", ""),
                            item.get("Energia Eletrica", ""),
                            item.get("Tipo Transporte", ""),
                            item.get("Data", "")
                         ))
                else:
                    tk.messagebox.showinfo("Aviso", "Nenhum dado encontrado para o ID informado.")
            except ValueError:
                tk.messagebox.showinfo("Erro", "Por favor, insira um número válido.")
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao consultar dados: {e}")
        
        #-----Texto adicionar registro-----
        texto_addRegistros = ctk.CTkLabel(frame1, 
                     text="Consultar Registros", 
                     text_color="black",
                     font=("Arial", 18))
        texto_addRegistros.place(x=135, y=30)
        
        
        #-----Texto e entrada para consultar ID-----
        texto_consultarID = ctk.CTkLabel(frame1, 
                     text="Consultar por ID:", 
                     text_color="black")
        texto_consultarID.place(x=80, y=75)
        
        entrada_id = ctk.CTkEntry(frame1,
                                  corner_radius=50,
                                  width= 125,
                                  height= 35)
        entrada_id.place(x=183, y=72)
        
        #-----Botão consultar ID-----
        botao_consultar = ctk.CTkButton(frame1, 
                      text="Consultar", 
                      fg_color="#474444", 
                      corner_radius=50,
                      width= 145,
                      height= 35,
                      command=lambda: Consulta(entrada_id))
        botao_consultar.place(x=135, y=115)

        #-----Criar um frame interno para a tabela-----
        tabela_frame = ctk.CTkFrame(frame1,
                                    fg_color="white",
                                    width=380,
                                    height=250)
        tabela_frame.place(x=5, y=160)
        
        #-----Botão consultar ID-----
        botao_limpar = ctk.CTkButton(frame1, text="Limpar Tabela",
                                    text_color="white",
                                    fg_color="#474444", 
                                    corner_radius=50,
                                    width= 145,
                                    height= 35,
                                    command=carregar_dados)
        botao_limpar.place(x= 135, y= 350)

        #-----Criar barras de rolagem-----
        scroll_y = tk.Scrollbar(tabela_frame, orient="vertical")
        scroll_x = tk.Scrollbar(tabela_frame, orient="horizontal")

        #-----Criar tabela-----
        colunas = ("Id", "Água (L)", "Resíduos", "Energia", "Transporte", "Data")
        tabela = ttk.Treeview (tabela_frame,
                               columns=colunas,
                               show="headings",
                               height= 7,
                               yscrollcommand=scroll_y.set,
                               xscrollcommand=scroll_x.set)

        #-----Adicionar barras de rolagem-----
        scroll_y.config(command=tabela.yview)
        scroll_x.config(command=tabela.xview)

        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")

        tabela.pack(expand=True, fill="both")

        #-----Definir largura das colunas (mais compactas)-----
        tabela.column("Id", width=20, anchor="center")
        tabela.column("Água (L)", width=59, anchor="center")
        tabela.column("Resíduos", width=59, anchor="center")
        tabela.column("Energia", width=59, anchor="center")
        tabela.column("Transporte", width=110, anchor="center")
        tabela.column("Data", width=70, anchor="center")

        #-----Definir cabeçalhos das colunas-----
        for col in colunas:
            tabela.heading(col, text=col)

        #-----Carregar os dados ao abrir a aba-----
        carregar_dados()
        
        
    #-----Aba Ações-----
    elif aba == "Editar Registros":
        
        botao_adiconarRegistro.configure(fg_color="#686564")
        botao_registros.configure(fg_color="#686564")
        botao_acoes.configure(fg_color="#363434")
        botao_graficos.configure(fg_color="#686564")
        botao_estatistica.configure(fg_color="#686564")
        
        #Função Editar
        def Editar():
            try:
                # Obtém o item selecionado na tabela
                item_selecionado = tabela.selection()
                if not item_selecionado:
                    tk.messagebox.showinfo("Aviso", "Por favor, selecione um registro para editar.")
                    return

                # Obtém os valores do registro selecionado
                valores = tabela.item(item_selecionado, "values")
                id_a_editar = int(valores[0])  # O ID está na primeira coluna da tabela

                # Cria uma nova janela para edição
                
                janela_editar = ctk.CTkToplevel()
                janela_editar.title("Editar Registros")
                janela_editar.geometry("350x400")

                # Dados disponíveis para o ComboBox de transporte
                opcoes_transporte = ["Transporte Público", "Bicicleta", "Caminhada", "Carona", "Carro Particular", "Moto Particular"]

                # Campos de entrada para edição
                
                texto_editarRegistros = ctk.CTkLabel(janela_editar,
                     text="Adicionar Registros", 
                     text_color="white",
                     font=("Arial", 18)).pack(pady=3)
                
                ctk.CTkLabel(janela_editar, text="Consumo de Água (L):").pack(pady=3)
                entrada_agua = ctk.CTkEntry(janela_editar, corner_radius=50)
                entrada_agua.insert(0, valores[1])  # Preenche com o valor atual
                entrada_agua.pack(pady=5)

                ctk.CTkLabel(janela_editar, text="Não Recicláveis (kg):").pack(pady=3)
                entrada_residuos = ctk.CTkEntry(janela_editar, corner_radius=50)
                entrada_residuos.insert(0, valores[2])
                entrada_residuos.pack(pady=5)

                ctk.CTkLabel(janela_editar, text="Energia Elétrica (KWh):").pack(pady=3)
                entrada_energia = ctk.CTkEntry(janela_editar, corner_radius=50)
                entrada_energia.insert(0, valores[3])
                entrada_energia.pack(pady=5)

                ctk.CTkLabel(janela_editar, text="Tipo de Transporte:").pack(pady=3)
                entrada_transporte = ctk.CTkComboBox(janela_editar, corner_radius=10, values=opcoes_transporte)
                entrada_transporte.set(valores[4])  # Preenche com o valor atual
                entrada_transporte.pack(pady=5)

                # Função para salvar as alterações
                def salvar_alteracoes():
                    try:
                        novo_agua = float(entrada_agua.get())
                        novo_residuos = float(entrada_residuos.get())
                        novo_energia = float(entrada_energia.get())
                        novo_transporte = entrada_transporte.get()

                        # Atualiza o registro no banco de dados
                        cursor = bd.banco.cursor()
                        cursor.execute("""
                            UPDATE sustentabilidade
                            SET s_agua = %s, s_reciclaveis = %s, s_energia = %s, s_transporte = %s
                            WHERE s_id = %s
                        """, (novo_agua, novo_residuos, novo_energia, novo_transporte, id_a_editar))
                        bd.banco.commit()

                        # Atualiza a tabela e fecha a janela
                        tk.messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
                        carregar_dados()
                        janela_editar.destroy()
                    except Exception as e:
                        tk.messagebox.showerror("Erro", f"Erro ao salvar alterações: {e}")

                # Botão para salvar as alterações
                ctk.CTkButton(janela_editar, text="Salvar", command=salvar_alteracoes).pack(pady=20)

            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao editar dados: {e}")
            

        def Excluir():
            try:
                # Obtém o item selecionado na tabela
                item_selecionado = tabela.selection()
                if not item_selecionado:
                    tk.messagebox.showinfo("Aviso", "Por favor, selecione um registro para excluir.")
                    return

                # Obtém o ID do registro selecionado
                valores = tabela.item(item_selecionado, "values")
                id_a_deletar = int(valores[0])  # O ID está na primeira coluna da tabela

                # Confirmação de exclusão
                confirmacao = tk.messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o registro com ID {id_a_deletar}?")
                if not confirmacao:
                    return

                # Executa a exclusão no banco de dados
                cursor = bd.banco.cursor()
                cursor.execute(f"DELETE FROM sustentabilidade WHERE s_id = {id_a_deletar};")
                bd.banco.commit()

                # Verifica se o registro foi excluído
                if cursor.rowcount > 0:
                    tk.messagebox.showinfo("Sucesso", "Registro excluído com sucesso.")
                    carregar_dados()  # Atualiza a tabela após a exclusão
                else:
                    tk.messagebox.showinfo("Aviso", "Nenhum dado encontrado para o ID informado.")
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao excluir dados: {e}")

        # Função para carregar os dados do banco de dados
        def carregar_dados():
            try:
                cursor = bd.banco.cursor()
                cursor.execute("""
                    SELECT JSON_ARRAYAGG(
                        JSON_OBJECT(
                            'Id', s_id,
                            'Consumo de Agua', s_agua,
                            'Nao Reciclaveis', s_reciclaveis,
                            'Energia Eletrica', s_energia,
                            'Tipo Transporte', s_transporte,
                            "Data", s_data
                        )
                    ) AS dados_json
                    FROM sustentabilidade;
                """)
                resultado = cursor.fetchone()

                # Verifica se há dados retornados
                if resultado and resultado[0]:
                    dados = json.loads(resultado[0])  # Converte o JSON retornado para um objeto Python
                    for item in tabela.get_children():
                        tabela.delete(item)
                    for item in dados:
                        tabela.insert("", "end", values=(
                            item.get("Id", ""),
                            item.get("Consumo de Agua", ""),
                            item.get("Nao Reciclaveis", ""),
                            item.get("Energia Eletrica", ""),
                            item.get("Tipo Transporte", ""),
                            item.get("Data", "")
                         ))
                else:
                    tk.messagebox.showinfo("Aviso", "Nenhum dado encontrado.")
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")

        # Criar um frame interno para a tabela
        tabela_frame = ctk.CTkFrame(frame1,
                                    fg_color="white",
                                    width=380,
                                    height=250)
        tabela_frame.place(x=5, y=75)

        # Criar barras de rolagem
        scroll_y = tk.Scrollbar(tabela_frame, orient="vertical")
        scroll_x = tk.Scrollbar(tabela_frame, orient="horizontal")

        # Criar tabela
        colunas = ("Id", "Água (L)", "Resíduos", "Energia", "Transporte", "Data")
        tabela = ttk.Treeview(tabela_frame,
                              columns=colunas,
                              show="headings",
                              height=11,
                              yscrollcommand=scroll_y.set,
                              xscrollcommand=scroll_x.set)

        # Adicionar barras de rolagem
        scroll_y.config(command=tabela.yview)
        scroll_x.config(command=tabela.xview)

        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")

        tabela.pack(expand=True, fill="both")

        # Definir largura das colunas (mais compactas)
        tabela.column("Id", width=20, anchor="center")
        tabela.column("Água (L)", width=59, anchor="center")
        tabela.column("Resíduos", width=59, anchor="center")
        tabela.column("Energia", width=59, anchor="center")
        tabela.column("Transporte", width=110, anchor="center")
        tabela.column("Data", width=70, anchor="center")

        # Definir cabeçalhos das colunas
        for col in colunas:
            tabela.heading(col, text=col)

        # Carregar os dados ao abrir a aba
        carregar_dados()

        texto_acoes = ctk.CTkLabel(frame1,
                                   text="Ações do Sistema",
                                   text_color="black",
                                   font=("Arial", 18))
        texto_acoes.place(x=135, y=30)

        # Botão da ação editar
        botao_editar = ctk.CTkButton(frame1,
                                     text="Editar",
                                     fg_color="#474444",
                                     corner_radius=50,
                                     width=145,
                                     height=35,
                                     command=Editar)
        botao_editar.place(x=50, y=350)

        # Botão da ação excluir
        botao_excluir = ctk.CTkButton(frame1,
                                      text="Excluir",
                                      fg_color="#474444",
                                      corner_radius=50,
                                      width=145,
                                      height=35,
                                      command=Excluir)
        botao_excluir.place(x=220, y=350)
    
    
    #-----Aba Graficos-----
    elif aba == "Grafico":
        
        botao_adiconarRegistro.configure(fg_color="#686564")
        botao_registros.configure(fg_color="#686564")
        botao_acoes.configure(fg_color="#686564")
        botao_graficos.configure(fg_color="#363434")
        botao_estatistica.configure(fg_color="#686564")
        
        try:
                cursor = bd.banco.cursor()
                cursor.execute("""
                    SELECT JSON_ARRAYAGG(
                        JSON_OBJECT(
                            'Consumo de Agua', s_agua,
                            'Nao Reciclaveis', s_reciclaveis,
                            'Energia Eletrica', s_energia
                        )
                    ) AS dados_json
                    FROM sustentabilidade;
                """)
                resultado = cursor.fetchone()

                if resultado and resultado[0]:
                    dados = json.loads(resultado[0])
                    num_registros = len(dados)

                    categorias = ["Água", "Não Recicláveis", "Energia"]
                    valores = [
                        sum(dado["Consumo de Agua"] for dado in dados) / num_registros,
                        sum(dado["Nao Reciclaveis"] for dado in dados) / num_registros,
                        sum(dado["Energia Eletrica"] for dado in dados) / num_registros
                    ]

                    texto_grafico = ctk.CTkLabel(frame1,
                                                text="Gráfico de Sustentabilidade",
                                                text_color="black",
                                                font=("Arial", 18))
                    texto_grafico.place(x=95, y=15)

                    # --- Criação da figura do gráfico ---
                    fig, ax = plt.subplots(figsize=(4.0, 3.2))

                    # --- Função de atualização do gráfico ---
                    def atualizar_grafico(event=None):
                            tipo = combo_tipo.get()

                            # Remove o gráfico antigo do frame (caso exista)
                            for widget in frame1.winfo_children():
                                if isinstance(widget, FigureCanvasTkAgg):
                                    widget.get_tk_widget().destroy()

                            # Define os dados de categorias (fixo para barras e pizza padrão)
                            categorias = ["Água", "Não Recicláveis", "Energia"]

                            # Dados para gráfico de barras (médias)
                            valores_barras = [
                                sum(dado["Consumo de Agua"] for dado in dados) / num_registros,
                                sum(dado["Nao Reciclaveis"] for dado in dados) / num_registros,
                                sum(dado["Energia Eletrica"] for dado in dados) / num_registros
                            ]

                            # Define tamanho do gráfico por tipo
                            if tipo == "Médias":
                                fig, ax = plt.subplots(figsize=(4.2, 3.2))

                                # Categorias e valores originais
                                categorias = ["Água", "Não Recicláveis", "Energia"]
                                ax.bar(categorias, valores_barras, color=['blue', 'green', 'red'])
                                ax.set_title("Médias das Categorias")
                                ax.set_ylabel("Média dos Valores")

                            elif tipo == "Transporte":
                                cursor.execute("""
                                    SELECT s_transporte, COUNT(*) 
                                    FROM sustentabilidade 
                                    GROUP BY s_transporte;
                                """)
                                resultados = cursor.fetchall()

                                labels_transporte = [linha[0] for linha in resultados]
                                valores_transporte = [linha[1] for linha in resultados]

                                fig, ax = plt.subplots(figsize=(4.0, 3.2))  # maior para caber os nomes dos transportes
                                ax.set_position([0.1, 0.1, 0.78, 0.73])  # [esquerda, baixo, largura, altura]
                                ax.pie(valores_transporte,
                                    labels=labels_transporte,
                                    autopct='%1.1f%%',
                                    startangle=140,
                                    radius=0.5)
                                ax.axis('equal')
                            elif tipo == "Máximos e Mínimos":
                                fig, ax = plt.subplots(figsize=(4.2, 3.2))

                                # Categorias
                                categorias = ["Água", "Não Recicláveis", "Energia"]

                                # Máximos e mínimos por categoria
                                maximos = [
                                    max(dado["Consumo de Agua"] for dado in dados),
                                    max(dado["Nao Reciclaveis"] for dado in dados),
                                    max(dado["Energia Eletrica"] for dado in dados)
                                ]
                                minimos = [
                                    min(dado["Consumo de Agua"] for dado in dados),
                                    min(dado["Nao Reciclaveis"] for dado in dados),
                                    min(dado["Energia Eletrica"] for dado in dados)
                                ]

                                # Largura das barras
                                largura = 0.35
                                x = range(len(categorias))

                                # Barras lado a lado
                                ax.bar([i - largura/2 for i in x], maximos, width=largura, label="Máximo", color="red")
                                ax.bar([i + largura/2 for i in x], minimos, width=largura, label="Mínimo", color="blue")

                                ax.set_xticks(x)
                                ax.set_xticklabels(categorias)
                                ax.set_ylabel("Valores")
                                ax.set_title("Máximos e Mínimos por Categoria")
                                ax.legend()

                            # Insere o novo gráfico
                            canvas = FigureCanvasTkAgg(fig, master=frame1)
                            canvas.draw()
                            canvas.get_tk_widget().place(x=8, y=85)


                    # --- Combobox customtkinter ---
                    combo_tipo = ctk.CTkComboBox(frame1,
                    values=["Médias", "Máximos e Mínimos", "Transporte"],
                    command=atualizar_grafico,
                    width=160,
                    dropdown_font=("Arial", 12),
                    font=("Arial", 12))
                    combo_tipo.set("Médias")
                    combo_tipo.place(x=117, y=50)

                    # --- Canvas do gráfico ---
                    canvas = FigureCanvasTkAgg(fig, master=frame1)
                    atualizar_grafico()  # Exibe o gráfico inicial
                    canvas.get_tk_widget().place(x=40, y=80)

                else:
                    tk.messagebox.showinfo("Aviso", "Nenhum dado encontrado para exibir no gráfico.")
        except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao carregar dados para o gráfico: {e}")
        
    #-----Aba Estatistica-----
    elif aba == "Estatistica":
    
        botao_adiconarRegistro.configure(fg_color="#686564")
        botao_registros.configure(fg_color="#686564")
        botao_acoes.configure(fg_color="#686564")
        botao_graficos.configure(fg_color="#686564")
        botao_estatistica.configure(fg_color="#363434")
    
        cursor = bd.banco.cursor()
        cursor.execute("""
            SELECT JSON_ARRAYAGG(
                JSON_OBJECT(
                    'Id', s_id,
                    'Data', s_data,
                    'Consumo de Agua', s_agua,
                    'Nao Reciclaveis', s_reciclaveis,
                    'Energia Eletrica', s_energia,
                    'Tipo Transporte', s_transporte
                )
            ) AS dados_json
            FROM sustentabilidade;
        """)

        resultado = cursor.fetchone()

        texto_estatisticas = ctk.CTkLabel(
            frame1,
            text="Estatísticas média do Usuário",
            text_color="black",
            font=("Arial", 18)
        )
        texto_estatisticas.place(x=90, y=30)

        if resultado and resultado[0]:
            cursor.execute("SELECT AVG(s_agua), AVG(s_reciclaveis), AVG(s_energia), AVG(s_transporte) FROM sustentabilidade")
            resultado = cursor.fetchone()

            if resultado and all(v is not None for v in resultado):
                s_agua, s_reciclaveis, s_energia, media_transporte = [round(v, 2) for v in resultado]

                transporte_sustentavel = round((1 - media_transporte) * 100, 2)

                pontuacao = int(round(
                    ((s_agua * 0.2) +
                    (s_reciclaveis * 0.3) +
                    (s_energia * 0.3) +
                    (transporte_sustentavel * 0.2)) / 100 * 5
                ))

                dados = {
                    "agua": {"valor": s_agua, "mensagem": "você precisa reduzir o consumo de água"},
                    "nao_reciclaveis": {"valor": s_reciclaveis, "mensagem": "está OK"},
                    "energia": {"valor": s_energia, "mensagem": "Sustentável"},
                    "transporte": {"valor": transporte_sustentavel, "mensagem": "Considere meios mais sustentáveis"},
                    "pontuacao": pontuacao
                }

                criar_bloco_estatistica_agua(frame1, "ÁGUA", dados["agua"]["valor"], dados["agua"]["mensagem"], 80)
                criar_bloco_estatistica_reciclaveis(frame1, "NÃO RECICLÁVEIS", dados["nao_reciclaveis"]["valor"], dados["nao_reciclaveis"]["mensagem"], 120)
                criar_bloco_estatistica_energia(frame1, "ENERGIA ELÉTRICA", dados["energia"]["valor"], dados["energia"]["mensagem"], 160)
                criar_bloco_estatistica_transporte(frame1, "TRANSPORTE", dados["transporte"]["valor"], dados["transporte"]["mensagem"], 200)

                texto_estatisticasPontuacao = ctk.CTkLabel(
                    frame1, text="ESTRELAS", text_color="black", font=("Arial", 12)
                )
                texto_estatisticasPontuacao.place(x=180, y=260)

                puxar_estatisticasPontuacao = ctk.CTkEntry(
                    frame1,
                    corner_radius=50,
                    border_color="gold",
                    placeholder_text=str(dados["pontuacao"]),
                    width=70
                )
                puxar_estatisticasPontuacao.configure(state="readonly")
                puxar_estatisticasPontuacao.place(x=100, y=260)

            else:
                tk.messagebox.showinfo("Estatísticas", "Não foi possível calcular as médias.")
        else:
            tk.messagebox.showinfo("Estatísticas", "Nenhum dado encontrado no banco de dados.")




botao_adiconarRegistro = ctk.CTkButton(janela_principal,
                                text="Adicionar registros",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434",
                                width= 145,
                                height= 35,
                                command=lambda: mudar_aba("Adicionar Registros"))
botao_adiconarRegistro.place(x=460, y=60)
    
botao_registros = ctk.CTkButton(janela_principal,
                                text="Consultar Registros",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434",
                                width= 145,
                                height= 35,
                                command=lambda: mudar_aba("Consultar"))
botao_registros.place(x=460, y=120)
    
botao_acoes = ctk.CTkButton(janela_principal,
                                text="Editar Registros",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434",
                                width= 145,
                                height= 35,
                                command=lambda: mudar_aba("Editar Registros"))
botao_acoes.place(x=460, y=180)
    
botao_graficos = ctk.CTkButton(janela_principal,
                                text="Gráfico",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434",
                                width= 145,
                                height= 35,
                                command=lambda: mudar_aba("Grafico"))
botao_graficos.place(x=460, y=240)
    
botao_estatistica = ctk.CTkButton(janela_principal,
                                text="Estatística",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434",
                                width= 145,
                                height= 35,
                                command=lambda: mudar_aba("Estatistica"))
botao_estatistica.place(x=460, y=300)

# --- Rodapé ---
rodape = ctk.CTkLabel(janela_principal,
                      text="Sistema de Sustentabilidade 2025 ",
                      font=ctk.CTkFont(size=11, slant="italic"),
                      text_color="black",
                      bg_color="#cccccc")
rodape.place(x=445, y=360)


def chamar_janela():
    mudar_aba("Adicionar Registros")
    janela_principal.mainloop()