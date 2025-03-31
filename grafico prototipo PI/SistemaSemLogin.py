import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import json
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Instalar Pillow, customtkinter e tkinter

ctk.set_appearance_mode("Dark")

altura = 400
largura = 400

janela_principal = ctk.CTk()
janela_principal.title("Sistema de Sustentabilidade")
janela_principal.geometry("650x400")
    
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
    
#-----Mudar Abas-----
def mudar_aba(aba):
    for widget in frame1.winfo_children():
        widget.destroy()
    
    #-----Aba Adicionar Registros-----
    if aba == "Adicionar registros":

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
                                            command=lambda: tk.messagebox.showinfo("Cadastro", "Dados cadastrados com sucesso!"))
        botao_addResgistros.place(x=135, y=330)
    
    
    #-----Aba "Consultar"-----
    elif aba == "Consultar":
        
        # Função para carregar os dados do JSON
        def carregar_dados():
            try:
                with open("dados.json", encoding='utf-8') as file:
                    dados = json.load(file)
                    for item in tabela.get_children():
                        tabela.delete(item)
                    for item in dados:
                        tabela.insert("", "end", values=(
                            item.get("Id", ""),
                            item.get("Consumo de Agua", ""),
                            item.get("Nao Reciclaveis", ""),
                            item.get("Energia Eletrica", ""),
                            item.get("Tipo Transporte", "")
                        ))
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")
    
                
        #Função pegar valor, ler BD (atualmente .json) e depois retornar consulta
        def Consulta(entradaId):
            try: 
                entrada_idInt = int(entrada_id.get())
                with open("dados.json", encoding='utf-8') as meu_json:
                    dados = json.load(meu_json)
                    for item in tabela.get_children():
                        tabela.delete(item)
                    for i in dados:
                        if i['Id'] == entrada_idInt:
                            tabela.insert("", "end", values=(
                            i.get("Id", ""),
                            i.get("Consumo de Agua", ""),
                            i.get("Nao Reciclaveis", ""),
                            i.get("Energia Eletrica", ""),
                            i.get("Tipo Transporte", "")
                        ))
                        
            except ValueError:
                tk.messagebox.showinfo("Erro", "Por favor inserir um número")
        
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
        tabela_frame.place(x=10, y=160)
        
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
        colunas = ("Id", "Água (L)", "Resíduos", "Energia", "Transporte")
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
        tabela.column("Id", width=30, anchor="center")
        tabela.column("Água (L)", width=80, anchor="center")
        tabela.column("Resíduos", width=75, anchor="center")
        tabela.column("Energia", width=75, anchor="center")
        tabela.column("Transporte", width=110, anchor="center")

        #-----Definir cabeçalhos das colunas-----
        for col in colunas:
            tabela.heading(col, text=col)

        #-----Carregar os dados ao abrir a aba-----
        carregar_dados()
        
        
    #-----Aba Ações-----
    elif aba == "Acoes":
            #def Editar():
            #def Excluir():
            
        # Função para carregar os dados do JSON
        def carregar_dados():
            try:
                with open("dados.json", encoding='utf-8') as file:
                    dados = json.load(file)
                    for item in tabela.get_children():
                        tabela.delete(item)
                    for item in dados:
                        tabela.insert("", "end", values=(
                            item.get("Id", ""),
                            item.get("Consumo de Agua", ""),
                            item.get("Nao Reciclaveis", ""),
                            item.get("Energia Eletrica", ""),
                            item.get("Tipo Transporte", "")
                        ))
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")
        
                # Criar um frame interno para a tabela
        tabela_frame = ctk.CTkFrame(frame1,
                                    fg_color="white",
                                    width=380,
                                    height=250)
        tabela_frame.place(x=10, y=75)
                
                # Criar barras de rolagem
        scroll_y = tk.Scrollbar(tabela_frame, orient="vertical")
        scroll_x = tk.Scrollbar(tabela_frame, orient="horizontal")

        # Criar tabela
        colunas = ("Id", "Água (L)", "Resíduos", "Energia", "Transporte")
        tabela = ttk.Treeview (tabela_frame,
                               columns=colunas,
                               show="headings",
                               height= 11,
                               yscrollcommand=scroll_y.set,
                               xscrollcommand=scroll_x.set)

        # Adicionar barras de rolagem
        scroll_y.config(command=tabela.yview)
        scroll_x.config(command=tabela.xview)

        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")

        tabela.pack(expand=True, fill="both")

        # 🔹 **Definir largura das colunas (mais compactas)**
        tabela.column("Id", width=30, anchor="center")
        tabela.column("Água (L)", width=80, anchor="center")
        tabela.column("Resíduos", width=75, anchor="center")
        tabela.column("Energia", width=75, anchor="center")
        tabela.column("Transporte", width=110, anchor="center")

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
        
        #-----Botão da ação editar-----
        botao_editar = ctk.CTkButton(frame1, 
                        text="Editar", 
                        fg_color="#474444", 
                        corner_radius=50,
                        width= 145,
                        height= 35)
        botao_editar.place(x=50, y=350) 

        #-----Botão da ação excluir-----
        botao_excluir = ctk.CTkButton(frame1, 
                        text="Excluir", 
                        fg_color="#474444", 
                        corner_radius=50,
                        width= 145,
                        height= 35)
        botao_excluir.place(x=220, y=350)
    
    
    #-----Aba Graficos-----
    elif aba == "Grafico":
            
        with open("dados.json", encoding='utf-8') as jorge:
            dados = json.load(jorge)

        if not dados:
            tk.messagebox.showinfo("Aviso", "Nenhum dado encontrado para exibir no gráfico.")
            return
        
        texto_acoes = ctk.CTkLabel(frame1, 
                        text="Gráfico de Sustentabilidade", 
                        text_color="black",
                        font=("Arial", 18))
        texto_acoes.place(x=110, y=30)

        num_registros = len(dados)
            
        categorias = ["Água", "Não Recicláveis", "Energia"]
        valores = [
            sum(dado["Consumo de Agua"] for dado in dados) / num_registros,
            sum(dado["Nao Reciclaveis"] for dado in dados) / num_registros,
            sum(dado["Energia Eletrica"] for dado in dados) / num_registros
        ]
            
        fig, ax = plt.subplots(figsize = (4.2, 3.4))
        ax.bar(categorias, valores, color=['blue', 'green', 'red'])
        ax.set_ylabel("Média dos Valores")
            
        canvas = FigureCanvasTkAgg(fig, master=frame1)
        canvas.draw()
        canvas.get_tk_widget().place(x=10, y=50)
        
    #-----Aba Graficos-----
    elif aba == "Estatistica":
        
        texto_TituloEstatisticas = ctk.CTkLabel(frame1, 
                     text="Estatísticas do Usuário", 
                     text_color="black",
                     font=("Arial", 18))
        texto_TituloEstatisticas.place(x=135, y=30)
    
        texto_estatisticasAgua = ctk.CTkLabel(frame1, 
                     text="ÁGUA -> você precisa reduzir o consumo de água", 
                     text_color="black",
                     font=("Arial", 12))
        texto_estatisticasAgua.place(x=75, y=80)
        
        puxar_estatisticasAgua = ctk.CTkEntry(frame1, 
                                    corner_radius=50,
                                    border_color="Grey",
                                    placeholder_text="40%",
                                    width=60)
        puxar_estatisticasAgua.configure(state="readonly")
        puxar_estatisticasAgua.place(x=10, y=80)
        
        texto_estatisticasNaoReciclaveis = ctk.CTkLabel(frame1, 
                     text="NÃO RECICLÁVEIS -> está OK", 
                     text_color="black",
                     font=("Arial", 12))
        texto_estatisticasNaoReciclaveis.place(x=75, y=120)
        
        puxar_estatisticasNaoReciclaveis = ctk.CTkEntry(frame1, 
                                    corner_radius=50,
                                    border_color="Grey",
                                    placeholder_text="55%",
                                    width=60)
        puxar_estatisticasNaoReciclaveis.configure(state="readonly")
        puxar_estatisticasNaoReciclaveis.place(x=10, y=120)

        texto_estatisticasEnergia = ctk.CTkLabel(frame1, 
                     text="ENERGIA ELÉTRICA -> Sustentável", 
                     text_color="black",
                     font=("Arial", 12))
        texto_estatisticasEnergia.place(x=75, y=160)
        
        puxar_estatisticasEnergia = ctk.CTkEntry(frame1, 
                                    corner_radius=50,
                                    border_color="Grey",
                                    placeholder_text="85%",
                                    width=60)
        puxar_estatisticasEnergia.configure(state="readonly")
        puxar_estatisticasEnergia.place(x=10, y=160)

        texto_estatisticasTransporte = ctk.CTkLabel(frame1, 
                     text="TRANSPORTE -> você precisa reduzir transportes privados", 
                     text_color="black",
                     font=("Arial", 12))
        texto_estatisticasTransporte.place(x=75, y=200)
        
        puxar_estatisticasTransporte = ctk.CTkEntry(frame1, 
                                    corner_radius=50,
                                    border_color="Grey",
                                    placeholder_text="35%",
                                    width=60)
        puxar_estatisticasTransporte.configure(state="readonly")
        puxar_estatisticasTransporte.place(x=10, y=200)
        
        texto_estatisticasPontuacao = ctk.CTkLabel(frame1, 
                     text="ESTRELAS", 
                     text_color="black",
                     font=("Arial", 12))
        texto_estatisticasPontuacao.place(x=170, y=260)
        
        puxar_estatisticasPontuacao = ctk.CTkEntry(frame1, 
                                    corner_radius=50,
                                    border_color="Grey",
                                    placeholder_text="4",
                                    width=60)
        puxar_estatisticasPontuacao.configure(state="readonly")
        puxar_estatisticasPontuacao.place(x=100, y=260)


botao_adiconarRegistro = ctk.CTkButton(janela_principal,
                                text="Adicionar registros",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434",
                                width= 145,
                                height= 35,
                                command=lambda: mudar_aba("Adicionar registros"))
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
botao_registros.place(x=460, y=125)
    
botao_acoes = ctk.CTkButton(janela_principal,
                                text="Ações",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434",
                                width= 145,
                                height= 35,
                                command=lambda: mudar_aba("Acoes"))
botao_acoes.place(x=460, y=190)
    
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
botao_graficos.place(x=460, y=255)
    
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
botao_estatistica.place(x=460, y=320)

mudar_aba("Adicionar registros")

#-----Iniciar programa-----
janela_principal.mainloop()