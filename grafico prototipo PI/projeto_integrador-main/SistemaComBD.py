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
                    print("nice")
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
    elif aba == "Acoes":

        def Editar():
            try:
                # Obtém o item selecionado na tabela
                item_selecionado = tabela.selection()
                if not item_selecionado:
                    tk.messagebox.showinfo("Aviso", "Por favor, selecione um registro para editar.")
                    return

                # Obtém o ID do registro selecionado
                valores = tabela.item(item_selecionado, "values")
                id_a_editar = int(valores[0])  # O ID está na primeira coluna da tabela

                print (id_a_editar)
                ("Sucesso", "Registro editado com sucesso.")
            
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
                texto_grafico.place(x=90, y=10)

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
                        canvas.get_tk_widget().place(x=10, y=70)


                # --- Combobox customtkinter ---
                combo_tipo = ctk.CTkComboBox(frame1,
                values=["Médias", "Máximos e Mínimos", "Transporte"],
                command=atualizar_grafico,
                width=160,
                dropdown_font=("Arial", 12),
                font=("Arial", 12))
                combo_tipo.set("Médias")
                combo_tipo.place(x=110, y=40)

                # --- Canvas do gráfico ---
                canvas = FigureCanvasTkAgg(fig, master=frame1)
                atualizar_grafico()  # Exibe o gráfico inicial
                canvas.get_tk_widget().place(x=10, y=80)

            else:
                tk.messagebox.showinfo("Aviso", "Nenhum dado encontrado para exibir no gráfico.")
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Erro ao carregar dados para o gráfico: {e}")

        
    #-----Aba Estatistica-----
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



def chamar_janela():
    mudar_aba("Adicionar registros")
    janela_principal.mainloop()