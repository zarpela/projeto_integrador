import customtkinter as ctk  # Biblioteca CustomTkinter para interface gráfica moderna
import tkinter as tk  # Biblioteca Tkinter base para GUI
from tkinter import ttk  # Widgets temáticos do Tkinter
import json  # Biblioteca para manipulação de JSON
from PIL import Image  # Biblioteca PIL para manipulação de imagens
import matplotlib.pyplot as plt  # Biblioteca matplotlib para gráficos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Backend para integrar matplotlib com Tkinter
import datetime  # Biblioteca para trabalhar com datas
import bd  # Módulo local para conexão com banco de dados

ctk.set_appearance_mode("Dark")  # Define o modo escuro para a interface

altura = 400  # Altura definida para a área de desenho/interface
largura = 400  # Largura definida para a área de desenho/interface

janela_principal = ctk.CTk()  # Criação da janela principal do aplicativo
janela_principal.title("Sistema de Sustentabilidade")  # Define o título da janela
janela_principal.geometry("650x400")  # Define o tamanho inicial da janela
janela_principal.resizable(False, False)  # Janela não redimensionável

#-----Frames da Janela Principal-----
frame1 = ctk.CTkFrame(master=janela_principal,  # Frame principal para conteúdo dinâmico
                          width=altura,  # Define largura do frame
                          height=largura,  # Define altura do frame
                          fg_color="#ffffff",  # Cor de primeiro plano (foreground) branca
                          bg_color="#ffffff")  # Cor de fundo branca
frame1.place(x=0, y=0)  # Posiciona frame1 no canto superior esquerdo da janela

frame2 = ctk.CTkFrame(janela_principal,  # Frame lateral para controles fixos
                          width=250,  # Largura do frame lateral
                          height=400,  # Altura do frame lateral
                          fg_color="#cccccc",  # Cor clara para o frame lateral
                          bg_color="#cccccc")  # Mesma cor para fundo
frame2.place(x=400, y=0)  # Posiciona frame2 à direita, junto ao frame1

#-----Mudar Abas-----
def mudar_aba(aba):  # Função para alternar abas/visualizações
    global botao_OqueFazer  # Variável global, usada possivelmente em outro contexto
    for widget in frame1.winfo_children():  # Limpa widgets atuais no frame1
        widget.destroy()  # Remove (destroi) o widget atual do frame1 para limpar a tela antes de exibir a nova aba
    
    #-----Aba Adicionar Registros-----
    if aba == "Adicionar Registros":  # If para verificar se aba é "Adicionar Registros"

        botao_adiconarRegistro.configure(fg_color="#363434")  # Destaca o botão "Adicionar registros" como ativo (cor escura)
        botao_registros.configure(fg_color="#686564")  # Define cor de botão inativo para "Consultar Registros"
        botao_acoes.configure(fg_color="#686564")  # Define cor de botão inativo para "Editar Registros"
        botao_graficos.configure(fg_color="#686564")  # Define cor de botão inativo para "Gráfico"
        botao_estatistica.configure(fg_color="#686564")  # Define cor de botão inativo para "Estatística"
        
        texto_addRegistros = ctk.CTkLabel(frame1,  # Texto título da aba
                     text="Adicionar Registros",  # Define o texto exibido no título da aba
                     text_color="black",          # Define a cor do texto do título
                     font=("Arial", 18))          # Define a fonte e o tamanho do texto do título
        texto_addRegistros.place(x=135, y=30)  # Posiciona título
        
        #-----Texto e entrada do campo agua-----
        texto_consumoAgua = ctk.CTkLabel(frame1,  # Label para o consumo de água
                     text="Consumo de água (L):",  # Define o texto do label para o campo de água
                     text_color="black",           # Define a cor do texto do label
                     font=("Arial", 12))           # Define a fonte e o tamanho do texto do label
        texto_consumoAgua.place(x=110, y=75)        # Posiciona o label na tela nas coordenadas x=110, y=75
        
        entrada_agua = ctk.CTkEntry(frame1,  # Campo de entrada para água
                                    corner_radius=50,  # Bordas arredondadas
                                    border_color="Grey",  # Cor da borda
                                    width=200)  # Largura campo entrada
        entrada_agua.place(x=110, y=100)  # Posiciona o campo de entrada de água nas coordenadas x=110, y=100
        
        #-----Texto e entrada da geração de resíduos-----
        texto_geracaoResiduos = ctk.CTkLabel(frame1,  # Label não recicláveis
                                            text="Não recicláveis (kg):",  # Define o texto do label para o campo de resíduos não recicláveis
                                            text_color="black", # Define a cor do texto do label
                                            font=("Arial", 12)) # Define a fonte e o tamanho do texto do label
        texto_geracaoResiduos.place(x=110, y=135) # Posiciona o label na tela nas coordenadas x=110, y=135
        
        entrada_geracaoResiduos= ctk.CTkEntry(frame1,  # Entrada resíduos não recicláveis
                                            corner_radius=50, # Define bordas arredondadas para o campo de entrada de resíduos
                                            border_color="Grey", # Define a cor da borda do campo de entrada de resíduos
                                            width=200) # Define a largura do campo de entrada de resíduos
        entrada_geracaoResiduos.place(x=110, y=160) # Posiciona o campo de entrada de resíduos nas coordenadas x=110, y=160
        
        #-----Texto e entrada da energia gasta-----
        texto_energiaGasta = ctk.CTkLabel(frame1,  # Label energia elétrica consumida
                                            text="Energia elétrica (KWh):", 
                                            text_color="black",
                                            font=("Arial", 12))
        texto_energiaGasta.place(x=110, y=195)
        
        entrada_energiaGasta = ctk.CTkEntry(frame1,  # Campo para entrada da energia
                                            corner_radius=50,
                                            border_color="Grey",
                                            width=200)
        entrada_energiaGasta.place(x=110, y=220)
        
        #-----Texto e entrada do tipo de transporte-----
        texto_tipoTransporte = ctk.CTkLabel(frame1,  # Label para transporte utilizado
                                            text="Tipo de transporte utilizado:",
                                            text_color="black",
                                            font=("Arial", 12))
        texto_tipoTransporte.place(x=110, y=255)
        
        transportes = ["Transporte Público", "Bicicleta", "Caminhada", "Carona", "Carro Particular", "Moto Particular"]  # Opções de transporte
        entrada_tipoTransporte = ctk.CTkComboBox(frame1,  # ComboBox para seleção transporte
                                            values=transportes, 
                                            corner_radius= 15,
                                            justify="left",
                                            border_color="Grey",
                                            width=200,
                                            state="readonly")  # Só permite seleção, não edição livre
        entrada_tipoTransporte.place(x=110, y=280)
        
        #-----Botão adicionar registros-----
        botao_addResgistros = ctk.CTkButton(frame1,  # Botão para enviar dados
                                            text="Cadastrar", 
                                            fg_color="#474444", 
                                            corner_radius=50,
                                            width= 145,
                                            height= 35,
                                            command=lambda: adicionar_dados())  # Chama função para adicionar dados
        botao_addResgistros.place(x=135, y=330)

        # -----Função para adicionar os dados ao banco de dados-----
        def adicionar_dados():  # Função ao clicar em 'Cadastrar'
            add_agua = entrada_agua.get()  # Obtem valor da entrada de água
            add_residuos = entrada_geracaoResiduos.get()  # Valor resíduos
            add_energia = entrada_energiaGasta.get()  # Valor energia elétrica
            add_transporte = entrada_tipoTransporte.get()  # Tipo transporte escolhido
            cursor = bd.banco.cursor()  # Abre cursor para manipular banco de dados
            try:
                # Verifica se os campos estão preenchidos
                if not add_agua or not add_residuos or not add_energia or not add_transporte:
                    tk.messagebox.showerror("Campo(s) Inválido(s)", "Preencha todos os campos.")  # Exibe erro para falta de dados
                    return
                else:
                    if float(add_agua) <= 0 or float(add_residuos) <= 0 or float(add_energia) <= 0:
                        tk.messagebox.showerror("Valor Inválido", "Por favor, coloque um valor positivo.")  # Validação para valores positivos
                    else:
                        dados = (
                            int(1),  # Id usuário fixo (possível placeholder)
                            datetime.date.today().strftime("%Y-%m-%d"),  # Data atual formatada
                            float(add_agua),  # Consumo de água como float
                            float(add_residuos),  # Resíduos
                            float(add_energia),  # Energia
                            add_transporte  # Transporte usado
                        )
                        cursor.execute("INSERT INTO sustentabilidade (su_id, s_data, s_agua, s_reciclaveis, s_energia, s_transporte) VALUES (%s, %s, %s, %s, %s, %s)", dados)  # Insere dados na tabela
                        bd.banco.commit()  # Confirma a transação
                        entrada_agua.delete(0, tk.END)  # Limpa campo água
                        entrada_geracaoResiduos.delete(0, tk.END)  # Limpa campo resíduos
                        entrada_energiaGasta.delete(0, tk.END)  # Limpa campo energia
                        entrada_tipoTransporte.set("")  # Reseta seleção transporte
                        tk.messagebox.showinfo("Cadastro", "Dados cadastrados com sucesso!")  # Mensagem de sucesso
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao adicionar dados: {e}")  # Exibe erro de exceção
            finally:
                cursor.close()  # Fecha cursor para liberar recursos
                # Limpa os campos após o cadastro
                      
    
    #-----Aba "Consultar"-----
    elif aba == "Consultar":  # Caso a aba seja "Consultar"
        
        botao_adiconarRegistro.configure(fg_color="#686564")  # Ajusta botões para indicar aba ativa
        botao_registros.configure(fg_color="#363434")
        botao_acoes.configure(fg_color="#686564")
        botao_graficos.configure(fg_color="#686564")
        botao_estatistica.configure(fg_color="#686564")
        
        # Função para carregar os dados do JSON
        def carregar_dados():  # Função que carrega dados da tabela no BD
            try:
                cursor = bd.banco.cursor()  # Cursor para banco de dados
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
                resultado = cursor.fetchone()  # Busca primeira linha do resultado
                    
                # Verifica se há dados retornados
                if resultado and resultado[0]:
                    dados = json.loads(resultado[0])  # Transforma JSON texto em objeto Python
                    for item in tabela.get_children():
                        tabela.delete(item)  # Limpa tabela antes de exibir os dados
                    for item in dados:
                        tabela.insert("", "end", values=(  # Insere cada linha na tabela
                        item.get("Id", ""),
                        item.get("Consumo de Agua", ""),
                        item.get("Nao Reciclaveis", ""),
                        item.get("Energia Eletrica", ""),
                        item.get("Tipo Transporte", ""),
                        item.get("Data", "")
                ))
                else:
                    tk.messagebox.showinfo("Aviso", "Nenhum dado encontrado.")  # Sem dados encontrados
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")  # Exibe erro
                
                
        #Função pegar valor, ler BD (atualmente .json) e depois retornar consulta
        def Consulta(entradaId):  # Função para consultar dados por ID ou data
            try:
                entrada_valor = entrada_id.get()  # Captura valor digitado pelo usuário
        
                try:
                    entrada_idInt = int(entrada_valor)  # Tenta converter para inteiro (ID)
                    consulta_sql = f"WHERE s_id = {entrada_idInt}"  # SQL para ID
                
                except ValueError:
                    try:
                        entrada_data = datetime.datetime.strptime(entrada_valor, "%Y-%m-%d").date()  # Tenta converter para data
                        consulta_sql = f"WHERE s_data = '{entrada_data}'"  # SQL para data
                    
                    except ValueError:
                        tk.messagebox.showinfo("Erro", "Por favor, insira um número (ID) ou uma data no formato AAAA-MM-DD.")  # Erro formato inválido
                        return
                
                cursor = bd.banco.cursor()  # Abre cursor para BD
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
                    {consulta_sql};""")
                resultado = cursor.fetchone()  # Busca resultado
                
                if resultado and resultado[0]:
                    dados = json.loads(resultado[0])  # Converte para objeto Python
                    for item in tabela.get_children():
                        tabela.delete(item)  # Limpa tabela
                    for item in dados:
                        tabela.insert("", "end", values=(  # Insere dados na tabela
                            item.get("Id", ""),
                            item.get("Consumo de Agua", ""),
                            item.get("Nao Reciclaveis", ""),
                            item.get("Energia Eletrica", ""),
                            item.get("Tipo Transporte", ""),
                            item.get("Data", "")
                         ))
                else:
                    tk.messagebox.showinfo("Aviso", "Nenhum dado encontrado para o ID ou Data informada.")  # Info sem resultados
            except ValueError:
                tk.messagebox.showinfo("Erro", "Por favor, insira um número válido.")  # Erro valor inválido
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao consultar dados: {e}")  # Erro geral
                
        #-----Texto adicionar registro-----
        texto_addRegistros = ctk.CTkLabel(frame1,  # Cria um rótulo no frame1 para o título da aba
                        text="Consultar Registros",  # Texto do rótulo
                        text_color="black",  # Cor do texto
                        font=("Arial", 18))  # Fonte e tamanho do texto
        texto_addRegistros.place(x=135, y=30)  # Posiciona o rótulo na janela nas coordenadas X=135, Y=30


        #-----Texto e entrada para consultar ID-----
        texto_consultarID = ctk.CTkLabel(frame1,  # Cria um rótulo para a instrução de busca
                        text="Consultar por ID/Data:",  # Texto do rótulo
                        text_color="black")  # Cor do texto
        texto_consultarID.place(x=50, y=75)  # Posiciona o rótulo na posição X=80, Y=75

        entrada_id = ctk.CTkEntry(frame1,  # Cria um campo de entrada para digitar ID ou Data
                                corner_radius=50,  # Bordas arredondadas do campo
                                width=125,  # Largura do campo
                                height=35)  # Altura do campo
        entrada_id.place(x=183, y=72)  # Posiciona o campo na janela (X=183, Y=72)

        #-----Botão consultar ID-----
        botao_consultar = ctk.CTkButton(frame1,  # Cria um botão para executar consulta
                        text="Consultar",  # Texto do botão
                        fg_color="#474444",  # Cor de fundo do botão
                        corner_radius=50,  # Bordas arredondadas do botão
                        width=145,  # Largura do botão
                        height=35,  # Altura do botão
                        command=lambda: Consulta(entrada_id))  # Função chamada ao clicar, passando o campo de entrada
        botao_consultar.place(x=135, y=115)  # Posiciona o botão na janela (X=135, Y=115)

        #-----Criar um frame interno para a tabela-----
        tabela_frame = ctk.CTkFrame(frame1,  # Cria um frame dentro do frame1 para abrigar a tabela de dados
                                    fg_color="white",  # Cor de fundo do frame
                                    width=380,  # Largura do frame
                                    height=250)  # Altura do frame
        tabela_frame.place(x=5, y=160)  # Posiciona o frame na janela (X=5, Y=160)

        #-----Botão limpar tabela-----
        botao_limpar = ctk.CTkButton(frame1,  # Botão para recarregar/limpar dados da tabela
                                    text="Limpar Tabela",  # Texto exibido no botão
                                    text_color="white",  # Cor do texto do botão
                                    fg_color="#474444",  # Cor de fundo do botão
                                    corner_radius=50,  # Bordas arredondadas
                                    width=145,  # Largura do botão
                                    height=35,  # Altura do botão
                                    command=carregar_dados)  # Função chamada para recarregar dados
        botao_limpar.place(x=135, y=350)  # Posiciona o botão (X=135, Y=350)

        #-----Criar barras de rolagem-----
        scroll_y = tk.Scrollbar(tabela_frame, orient="vertical")  # Barra de rolagem vertical para tabela
        scroll_x = tk.Scrollbar(tabela_frame, orient="horizontal")  # Barra de rolagem horizontal para tabela

        #-----Criar tabela-----
        colunas = ("Id", "Água (L)", "Resíduos", "Energia", "Transporte", "Data")  # Define as colunas da tabela
        tabela = ttk.Treeview(tabela_frame,  # Cria a tabela no frame especificado
                            columns=colunas,  # Colunas da tabela
                            show="headings",  # Mostrar somente o cabeçalho, sem árvore
                            height=7,  # Altura da tabela (número de linhas visíveis)
                            yscrollcommand=scroll_y.set,  # Conecta barra de rolagem vertical
                            xscrollcommand=scroll_x.set)  # Conecta barra de rolagem horizontal

        #-----Adicionar barras de rolagem-----
        scroll_y.config(command=tabela.yview)  # Configura a barra vertical para controlar o scroll da tabela
        scroll_x.config(command=tabela.xview)  # Configura a barra horizontal para controlar o scroll da tabela

        scroll_y.pack(side="right", fill="y")  # Posiciona barra vertical na direita do frame, preenchendo eixo Y
        scroll_x.pack(side="bottom", fill="x")  # Posiciona barra horizontal na parte inferior, preenchendo eixo X

        tabela.pack(expand=True, fill="both")  # Empacota a tabela para expandir e preencher todo espaço disponível no frame

        #-----Definir largura das colunas (mais compactas)-----
        tabela.column("Id", width=20, anchor="center")  # Define a largura e o alinhamento central para coluna "Id"
        tabela.column("Água (L)", width=59, anchor="center")  # Coluna água
        tabela.column("Resíduos", width=59, anchor="center")  # Coluna resíduos
        tabela.column("Energia", width=59, anchor="center")  # Coluna energia
        tabela.column("Transporte", width=110, anchor="center")  # Coluna transporte
        tabela.column("Data", width=70, anchor="center")  # Coluna data

        #-----Definir cabeçalhos das colunas-----
        for col in colunas:  # Para cada coluna na lista
            tabela.heading(col, text=col)  # Define o texto do cabeçalho da tabela

        #-----Carregar os dados ao abrir a aba-----
        carregar_dados()  # Chama a função para carregar dados no momento da abertura dessa aba


#-----Aba Ações-----
    elif aba == "Editar Registros":  # Se a aba selecionada for para editar registros
        
        botao_adiconarRegistro.configure(fg_color="#686564")  # Atualiza cor dos botões indicando aba ativa/inativa
        botao_registros.configure(fg_color="#686564")
        botao_acoes.configure(fg_color="#363434")
        botao_graficos.configure(fg_color="#686564")
        botao_estatistica.configure(fg_color="#686564")
        
        #Função Editar
        def Editar():  # Função chamada para editar registro selecionado
            try:
                item_selecionado = tabela.selection()  # Pega o item selecionado na tabela
                if not item_selecionado:  # Verifica se nada foi selecionado
                    tk.messagebox.showinfo("Aviso", "Por favor, selecione um registro para editar.")  # Alerta usuário
                    return
                
                valores = tabela.item(item_selecionado, "values")  # Pega os valores do registro selecionado
                id_a_editar = int(valores[0])  # ID do registro, primeira coluna

                janela_editar = ctk.CTkToplevel()  # Cria uma nova janela (modal) para edição
                janela_editar.title("Editar Registros")  # Título da janela
                janela_editar.geometry("350x400")  # Define o tamanho da janela

                opcoes_transporte = ["Transporte Público", "Bicicleta", "Caminhada",  # Opções para ComboBox transporte
                                    "Carona", "Carro Particular", "Moto Particular"]

                # Campo para editar Consumo de Água
                texto_editarRegistros = ctk.CTkLabel(janela_editar,
                            text="Adicionar Registros", 
                            text_color="white",
                            font=("Arial", 18)).pack(pady=3)

                ctk.CTkLabel(janela_editar, text="Consumo de Água (L):").pack(pady=3)
                entrada_agua = ctk.CTkEntry(janela_editar, corner_radius=50)
                entrada_agua.insert(0, valores[1])  # Preenche campo com valor atual
                entrada_agua.pack(pady=5)

                # Campo para editar Resíduos não recicláveis
                ctk.CTkLabel(janela_editar, text="Não Recicláveis (kg):").pack(pady=3)
                entrada_residuos = ctk.CTkEntry(janela_editar, corner_radius=50)
                entrada_residuos.insert(0, valores[2])
                entrada_residuos.pack(pady=5)

                # Campo para editar Energia elétrica
                ctk.CTkLabel(janela_editar, text="Energia Elétrica (KWh):").pack(pady=3)
                entrada_energia = ctk.CTkEntry(janela_editar, corner_radius=50)
                entrada_energia.insert(0, valores[3])
                entrada_energia.pack(pady=5)

                # ComboBox para editar Transporte
                ctk.CTkLabel(janela_editar, text="Tipo de Transporte:").pack(pady=3)
                entrada_transporte = ctk.CTkComboBox(janela_editar, corner_radius=10,
                                                    values=opcoes_transporte, state="readonly")
                entrada_transporte.set(valores[4])
                entrada_transporte.pack(pady=5)

                def salvar_alteracoes():  # Função para salvar alterações feitas
                    try:
                        novo_agua = float(entrada_agua.get())  # Pega novo valor água
                        novo_residuos = float(entrada_residuos.get())  # Pega novo valor resíduos
                        novo_energia = float(entrada_energia.get())  # Pega novo valor energia
                        novo_transporte = entrada_transporte.get()  # Pega nova seleção transporte

                        # Validação de dados positivos e transporte selecionado
                        if novo_agua <= 0 or novo_residuos <= 0 or novo_energia <= 0:
                            tk.messagebox.showerror("Valor Inválido", "Por favor, coloque um valor positivo.")
                        elif not novo_transporte:
                            tk.messagebox.showerror("Valor Inválido", "Por favor, selecione um tipo de transporte válido.")
                        else:
                            cursor = bd.banco.cursor()  # Abre cursor SQL
                            cursor.execute("""  # Comando de atualização SQL
                                UPDATE sustentabilidade
                                SET s_agua = %s, s_reciclaveis = %s, s_energia = %s, s_transporte = %s
                                WHERE s_id = %s
                            """, (novo_agua, novo_residuos, novo_energia, novo_transporte, id_a_editar))
                            bd.banco.commit()  # Aplica as alterações no banco

                            # Atualiza interface e fecha janela edição
                            tk.messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
                            carregar_dados()  # Atualiza a tabela
                            janela_editar.destroy()  # Fecha janela de edição
                    except Exception as e:
                        tk.messagebox.showerror("Erro", f"Erro ao salvar alterações: {e}")  # Mostra erro ao salvar

                # Botão para salvar dados editados
                ctk.CTkButton(janela_editar, text="Salvar", command=salvar_alteracoes).pack(pady=20)

            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao editar dados: {e}")  # Mostra erro geral da função editar

        def Excluir():  # Função para excluir registro selecionado
            try:
                item_selecionado = tabela.selection()  # Pega o item selecionado na tabela
                if not item_selecionado:  # Verifica se nada foi selecionado
                    tk.messagebox.showinfo("Aviso", "Por favor, selecione um registro para excluir.")  # Alerta
                    return

                valores = tabela.item(item_selecionado, "values")  # Obtém valores do registro
                id_a_deletar = int(valores[0])  # Pega ID, que está na primeira coluna

                # Confirmação da exclusão
                confirmacao = tk.messagebox.askyesno("Confirmação",
                                                    f"Tem certeza que deseja excluir o registro com ID {id_a_deletar}?")
                if not confirmacao:
                    return  # Sai se o usuário escolher 'Não'

                cursor = bd.banco.cursor()  # Abre cursor SQL
                cursor.execute(f"DELETE FROM sustentabilidade WHERE s_id = {id_a_deletar};")  # Comando excluir
                bd.banco.commit()  # Aplica exclusão no banco

                # Verifica se algo foi excluído
                if cursor.rowcount > 0:
                    tk.messagebox.showinfo("Sucesso", "Registro excluído com sucesso.")  # Confirma exclusão
                    carregar_dados()  # Atualiza tabela
                else:
                    tk.messagebox.showinfo("Aviso", "Nenhum dado encontrado para o ID informado.")  # Se não encontrou
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao excluir dados: {e}")  # Mostra erro ao excluir

        # Função para carregar os dados do banco de dados e exibir na tabela
        def carregar_dados():
            try:
                cursor = bd.banco.cursor()  # Abrir cursor para manipular banco de dados
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
                resultado = cursor.fetchone()  # Recebe resultado da consulta (uma linha)

                # Checa se o resultado é válido e contém dados
                if resultado and resultado[0]:
                    dados = json.loads(resultado[0])  # Converte string JSON em objeto Python (lista de dicionários)
                    # Remove itens anteriores da tabela para limpar visualização
                    for item in tabela.get_children():
                        tabela.delete(item)
                    # Itera sobre a lista de registros e insere cada um na tabela exibida
                    for item in dados:
                        tabela.insert("", "end", values=(
                            item.get("Id", ""),  # Busca campo 'Id' ou vazio se não existir
                            item.get("Consumo de Agua", ""),  # Consumo de Água
                            item.get("Nao Reciclaveis", ""),  # Resíduos não recicláveis
                            item.get("Energia Eletrica", ""),  # Energia elétrica consumida
                            item.get("Tipo Transporte", ""),  # Tipo de transporte utilizado
                            item.get("Data", "")  # Data do registro
                        ))
                else:
                    tk.messagebox.showinfo("Aviso", "Nenhum dado encontrado.")  # Alerta quando banco está vazio
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")  # Exibe erro caso falha na consulta

        # Cria um frame interno para conter a tabela dos dados
        tabela_frame = ctk.CTkFrame(frame1,
                                    fg_color="white",  # Cor de fundo do frame
                                    width=380,
                                    height=250)
        tabela_frame.place(x=5, y=75)  # Posiciona o frame na janela principal

        # Criação das barras de rolagem vertical e horizontal
        scroll_y = tk.Scrollbar(tabela_frame, orient="vertical")  # Barra vertical para rolagem na tabela
        scroll_x = tk.Scrollbar(tabela_frame, orient="horizontal")  # Barra horizontal

        # Configuração da tabela com colunas definidas
        colunas = ("Id", "Água (L)", "Resíduos", "Energia", "Transporte", "Data")
        tabela = ttk.Treeview(tabela_frame,
                            columns=colunas,
                            show="headings",  # Exibe somente os cabeçalhos das colunas, não a estrutura em árvore
                            height=11,  # Altura da tabela em número de linhas visíveis
                            yscrollcommand=scroll_y.set,  # Barra vertical conectada para controlar o scroll vertical
                            xscrollcommand=scroll_x.set)  # Barra horizontal para scroll horizontal

        # Configuração dos comandos para controlar a visualização com as barras de rolagem
        scroll_y.config(command=tabela.yview)
        scroll_x.config(command=tabela.xview)

        # Empacotamento das barras de rolagem nos lados adequados do frame
        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")

        # Empacota e expande a tabela dentro do frame para uso responsivo
        tabela.pack(expand=True, fill="both")

        # Configuração de largura e alinhamento para cada coluna da tabela
        tabela.column("Id", width=20, anchor="center")  # Coluna Id, pequena e centralizada
        tabela.column("Água (L)", width=59, anchor="center")  # Coluna água, largura moderada
        tabela.column("Resíduos", width=59, anchor="center")  # Mesmo tamanho e alinhamento
        tabela.column("Energia", width=59, anchor="center")  # Igual às anteriores
        tabela.column("Transporte", width=110, anchor="center")  # Coluna maior para texto possivelmente longo
        tabela.column("Data", width=70, anchor="center")  # Coluna para data com largura intermediária

        # Definição dos nomes cabeçalhos que aparecerão para cada coluna
        for col in colunas:
            tabela.heading(col, text=col)

        # Chamada inicial para preencher a tabela ao abrir a aba
        carregar_dados()

        # Criação e posicionamento do título para as ações na interface
        texto_acoes = ctk.CTkLabel(frame1,
                                text="Ações do Sistema",
                                text_color="black",
                                font=("Arial", 18))
        texto_acoes.place(x=135, y=30)

        # Botão para acionar a edição de dados selecionados na tabela
        botao_editar = ctk.CTkButton(frame1,
                                    text="Editar",
                                    fg_color="#474444",
                                    corner_radius=50,
                                    width=145,
                                    height=35,
                                    command=Editar)  # Liga ao método Editar previamente definido
        botao_editar.place(x=50, y=350)

        # Botão para acionar a exclusão de dados selecionados
        botao_excluir = ctk.CTkButton(frame1,
                                    text="Excluir",
                                    fg_color="#474444",
                                    corner_radius=50,
                                    width=145,
                                    height=35,
                                    command=Excluir)  # Liga ao método Excluir previamente definido
        botao_excluir.place(x=220, y=350)

    #-----Aba Graficos-----
    elif aba == "Grafico":  # Se a aba para exibir gráficos for selecionada
        
        # Atualiza as cores dos botões para refletir a aba selecionada
        botao_adiconarRegistro.configure(fg_color="#686564")
        botao_registros.configure(fg_color="#686564")
        botao_acoes.configure(fg_color="#686564")
        botao_graficos.configure(fg_color="#363434")  # Aba gráfica destacada
        botao_estatistica.configure(fg_color="#686564")
        
        try:
            cursor = bd.banco.cursor()  # Abre cursor para banco
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
            resultado = cursor.fetchone()  # Recebe o resultado
            
            if resultado and resultado[0]:
                dados = json.loads(resultado[0])  # Converte JSON para objeto Python
                num_registros = len(dados)  # Número de registros para cálculo de médias

                categorias = ["Água", "Não Recicláveis", "Energia"]  # Categorias para o gráfico
                valores = [  # Calcula médias para cada categoria
                    sum(dado["Consumo de Agua"] for dado in dados) / num_registros,
                    sum(dado["Nao Reciclaveis"] for dado in dados) / num_registros,
                    sum(dado["Energia Eletrica"] for dado in dados) / num_registros
                ]

                # Cria rótulo para título do gráfico na interface
                texto_grafico = ctk.CTkLabel(frame1,
                                            text="Gráfico de Sustentabilidade",
                                            text_color="black",
                                            font=("Arial", 18))
                texto_grafico.place(x=95, y=15)

                # Criação da figura do gráfico com matplotlib
                fig, ax = plt.subplots(figsize=(4.0, 3.2))

                # Função para atualizar o gráfico dependendo da opção selecionada
                def atualizar_grafico(event=None):
                    tipo = combo_tipo.get()  # Obtém o tipo selecionado no combo

                    # Remove o gráfico antigo antes de desenhar o novo
                    for widget in frame1.winfo_children():
                        if isinstance(widget, FigureCanvasTkAgg):
                            widget.get_tk_widget().destroy()

                    categorias = ["Água", "Não Recicláveis", "Energia"]  # Categorias fixas

                    # Dados para gráfico de barras (médias)
                    valores_barras = [
                        sum(dado["Consumo de Agua"] for dado in dados) / num_registros,
                        sum(dado["Nao Reciclaveis"] for dado in dados) / num_registros,
                        sum(dado["Energia Eletrica"] for dado in dados) / num_registros
                    ]

                    # Verifica tipo selecionado e cria gráfico correspondente
                    if tipo == "Médias":
                        fig, ax = plt.subplots(figsize=(4.2, 3.2))
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

                        labels_transporte = [linha[0] for linha in resultados]  # Labels para pizza
                        valores_transporte = [linha[1] for linha in resultados]  # Valores para pizza

                        fig, ax = plt.subplots(figsize=(4.0, 3.2))  # Maior para caber nomes
                        ax.set_position([0.1, 0.1, 0.78, 0.73])  # Ajusta posição do gráfico no canvas
                        ax.pie(valores_transporte,
                            labels=labels_transporte,
                            autopct='%1.1f%%',
                            startangle=140,
                            radius=0.5)
                        ax.axis('equal')  # Mantém o círculo do gráfico proporcional

                    elif tipo == "Máximos e Mínimos":
                        fig, ax = plt.subplots(figsize=(4.2, 3.2))

                        categorias = ["Água", "Não Recicláveis", "Energia"]

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

                        largura_barra = 0.35
                        x = range(len(categorias))

                        ax.bar([i - largura_barra/2 for i in x], maximos, width=largura_barra, label="Máximo", color="red")
                        ax.bar([i + largura_barra/2 for i in x], minimos, width=largura_barra, label="Mínimo", color="blue")

                        ax.set_xticks(x)
                        ax.set_xticklabels(categorias)
                        ax.set_ylabel("Valores")
                        ax.set_title("Máximos e Mínimos por Categoria")
                        ax.legend()

                    # Insere o gráfico no tkinter usando FigureCanvasTkAgg
                    canvas = FigureCanvasTkAgg(fig, master=frame1)
                    canvas.draw()
                    canvas.get_tk_widget().place(x=8, y=85)

                # Combobox para seleção do tipo de gráfico
                combo_tipo = ctk.CTkComboBox(frame1,
                                            values=["Médias", "Máximos e Mínimos", "Transporte"],
                                            command=atualizar_grafico,
                                            width=160,
                                            dropdown_font=("Arial", 12),
                                            font=("Arial", 12))
                combo_tipo.set("Médias")  # Valor inicial selecionado
                combo_tipo.place(x=117, y=50)

                # Inicializa o canvas do gráfico
                canvas = FigureCanvasTkAgg(fig, master=frame1)
                atualizar_grafico()  # Desenha o gráfico inicial
                canvas.get_tk_widget().place(x=40, y=80)

            else:
                tk.messagebox.showinfo("Aviso", "Nenhum dado encontrado para exibir no gráfico.")  # Info se não houver dados

        except Exception as e:
            tk.messagebox.showerror("Erro", f"Erro ao carregar dados para o gráfico: {e}")  # Exibe erro caso ocorra problema

    #-----Aba Estatística-----
    elif aba == "Estatistica":

        #----Atribuir cores nas estatísticas-----

        # Função para criar um bloco de estatística para consumo de água
        def criar_bloco_estatistica_agua(master, titulo, valor, mensagem, y_pos):
            # Define a cor da borda com base no valor
            cor = "green" if valor >= 0 and valor <= 100 else "yellow" if valor > 100 and valor <= 150 else "red"

            # Cria um rótulo para exibir o título e mensagem
            texto = ctk.CTkLabel(master, 
                                text=f"{titulo.upper()} -> {mensagem}", 
                                text_color="black",
                                font=("Arial", 12))
            texto.place(x=95, y=y_pos)

            # Cria um campo de entrada apenas para exibição do valor
            entrada = ctk.CTkEntry(master, 
                                corner_radius=50,
                                border_color=cor,
                                placeholder_text=f"{valor}",
                                width=75)
            entrada.configure(state="readonly")
            entrada.place(x=15, y=y_pos) 

        # Função para criar um bloco de estatística para materiais recicláveis
        def criar_bloco_estatistica_reciclaveis(master, titulo, valor, mensagem, y_pos):
            # Define a cor da borda com base no valor
            cor = "green" if valor >= 0 and valor < 0.95 else "yellow" if valor >= 0.95 and valor <= 1.25 else "red"

            # Cria um rótulo para exibir o título e mensagem
            texto = ctk.CTkLabel(master, 
                                text=f"{titulo.upper()} -> {mensagem}", 
                                text_color="black",
                                font=("Arial", 12))
            texto.place(x=95, y=y_pos)

            # Cria um campo de entrada apenas para exibição do valor
            entrada = ctk.CTkEntry(master, 
                                corner_radius=50,
                                border_color=cor,
                                placeholder_text=f"{valor}",
                                width=75)
            entrada.configure(state="readonly")
            entrada.place(x=15, y=y_pos) 

        # Função para criar um bloco de estatística para consumo de energia elétrica
        def criar_bloco_estatistica_energia(master, titulo, valor, mensagem, y_pos):
            # Define a cor da borda com base no valor
            cor = "green" if valor >= 0 and valor <= 4.5 else "yellow" if valor > 4.5 and valor <= 6 else "red"

            # Cria um rótulo para exibir o título e mensagem
            texto = ctk.CTkLabel(master, 
                                text=f"{titulo.upper()} -> {mensagem}", 
                                text_color="black",
                                font=("Arial", 12))
            texto.place(x=95, y=y_pos)

            # Cria um campo de entrada apenas para exibição do valor
            entrada = ctk.CTkEntry(master, 
                                corner_radius=50,
                                border_color=cor,
                                placeholder_text=f"{valor}",
                                width=75)
            entrada.configure(state="readonly")
            entrada.place(x=15, y=y_pos) 

        # Função para criar um bloco de estatística para transporte utilizado
        def criar_bloco_estatistica_transporte(master, titulo, valor, mensagem, y_pos):
            # Define a cor da borda com base no valor
            cor = "green" if valor >= 0 and valor <= 0.25 else "yellow" if valor > 0.25 and valor <= 0.75 else "red"

            # Cria um rótulo para exibir o título e mensagem
            texto = ctk.CTkLabel(master, 
                                text=f"{titulo.upper()} -> {mensagem}", 
                                text_color="black",
                                font=("Arial", 12))
            texto.place(x=95, y=y_pos)

            # Cria um campo de entrada apenas para exibição do valor
            entrada = ctk.CTkEntry(master, 
                                corner_radius=50,
                                border_color=cor,
                                placeholder_text=f"{valor}",
                                width=75)
            entrada.configure(state="readonly")
            entrada.place(x=15, y=y_pos) 

        # Configuração dos botões de navegação na aba de estatísticas
        botao_adiconarRegistro.configure(fg_color="#686564")
        botao_registros.configure(fg_color="#686564")
        botao_acoes.configure(fg_color="#686564")
        botao_graficos.configure(fg_color="#686564")
        botao_estatistica.configure(fg_color="#363434")

        # Consulta SQL para obter dados de sustentabilidade do banco de dados
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

        # Recupera os resultados da consulta
        resultado = cursor.fetchone()

        # Exibe um rótulo indicando estatísticas médias do usuário
        texto_estatisticas = ctk.CTkLabel(
            frame1,
            text="Estatísticas média do Usuário",
            text_color="black",
            font=("Arial", 18)
        )
        texto_estatisticas.place(x=90, y=30)

        # Dicionário para atribuir valores ao tipo de transporte utilizado
        valor_transporte = {
            "Transporte Público": 0.75,
            "Bicicleta": 1,
            "Caminhada": 1,
            "Carona": 0.5,
            "Carro Particular": 0.25,
            "Moto Particular": 0
        }
        
        if resultado and resultado[0]: #Confirma se tem dados na lista resultado
            cursor.execute("SELECT s_transporte FROM sustentabilidade")
            transportes = cursor.fetchall()
            
            soma_transporte = 0
            quantidade_transportes = 0

            for transporte in transportes:
                tipo_transporte = transporte[0] 
                if tipo_transporte in valor_transporte:
                    soma_transporte += valor_transporte[tipo_transporte]  
                    quantidade_transportes += 1  
         
            if quantidade_transportes > 0:
                media_transporte = round(soma_transporte / quantidade_transportes, 2)
            else:
                media_transporte = 0 
            cursor.execute("SELECT s_agua, s_reciclaveis, s_energia FROM sustentabilidade")
            dados = cursor.fetchall()

            agua_values = [d[0] for d in dados if d[0] is not None]
            reciclaveis_values = [d[1] for d in dados if d[1] is not None]
            energia_values = [d[2] for d in dados if d[2] is not None]

            min_agua, max_agua = min(agua_values), max(agua_values)
            min_reciclaveis, max_reciclaveis = min(reciclaveis_values), max(reciclaveis_values)
            min_energia, max_energia = min(energia_values), max(energia_values)

            transporte_sustentavel = round((1 - media_transporte), 2)
            cursor.execute("SELECT AVG(s_agua), AVG(s_reciclaveis), AVG(s_energia) FROM sustentabilidade")
            resultado = cursor.fetchone()

            if resultado and all(v is not None for v in resultado):
                s_agua, s_reciclaveis, s_energia = [round(v, 2) for v in resultado]
                s_agua_normalizado = (s_agua - min_agua) / (max_agua - min_agua) if max_agua > min_agua else 0
                s_reciclaveis_normalizado = (s_reciclaveis - min_reciclaveis) / (max_reciclaveis - min_reciclaveis) if max_reciclaveis > min_reciclaveis else 0
                s_energia_normalizado = (s_energia - min_energia) / (max_energia - min_energia) if max_energia > min_energia else 0

                transporte_sustentavel = round((1 - media_transporte), 2)

                pontuacao = float(round(
                    ((s_agua_normalizado * 0.2) +
                    (s_reciclaveis_normalizado * 0.3) +
                    (s_energia_normalizado * 0.3) +
                    (transporte_sustentavel * 0.2)),2
                ))

                if pontuacao >=0 and pontuacao <0.2:
                    estrelas = 5
                elif pontuacao >=0.2 and pontuacao <0.4:
                    estrelas = 4
                elif pontuacao >=0.4 and pontuacao <0.6:
                    estrelas = 3
                elif pontuacao >=0.6 and pontuacao <0.8:
                    estrelas = 2
                else:   
                    estrelas = 1
                
                 # ---------------- ÁGUA ----------------
                if s_agua >= 0 and s_agua <= 100:
                    mensagemA = "Sustentável, Parábens"
                    mensagemPopUpA = "Você está sustentável no consumo de água!"
                elif s_agua > 100 and s_agua <= 150:
                    mensagemA = "Pouco Sustentável"
                    mensagemPopUpA = "Feche a torneira, tome banhos curtos e reutilize sempre que possível. Cada gota economizada faz a diferença!"
                else:
                    mensagemA = "Insustentável"
                    mensagemPopUpA = "O consumo irresponsável hoje gera escassez amanhã. Crie planilhas para gerenciar formas de sustentabilizar seu consumo de água!"

                # ---------------- RECICLÁVEIS ----------------
                if s_reciclaveis >= 0 and s_reciclaveis < 0.95:
                    mensagemR = "Sustentável, Parábens"
                    mensagemPopUpR = "Você está sustentável com poucos itens não recicláveis! Continue assim!"
                elif s_reciclaveis >= 0.95 and s_reciclaveis <= 1.25:
                    mensagemR = "Pouco Sustentável"
                    mensagemPopUpR = "Você ainda gera uma quantidade considerável de resíduos. Busque reduzir, reutilizar e reciclar!"
                else:
                    mensagemR = "Insustentável"
                    mensagemPopUpR = "Produção elevada de resíduos não recicláveis! Reavalie seus hábitos e prefira materiais recicláveis."

                # ---------------- ENERGIA ----------------
                if s_energia >= 0 and s_energia <= 4.5:
                    mensagemE = "Sustentável, Parábens"
                    mensagemPopUpE = "Seu consumo de energia está em um ótimo nível! Continue adotando práticas conscientes!"
                elif s_energia > 4.5 and s_energia <= 6:
                    mensagemE = "Pouco Sustentável"
                    mensagemPopUpE = "Seu consumo de energia pode ser melhorado! Desligue aparelhos em standby e use energia natural!"
                else:
                    mensagemE = "Insustentável"
                    mensagemPopUpE = "Alto consumo de energia detectado! Tente adotar lâmpadas LED e reduzir o uso de eletrônicos desnecessários."

                # ---------------- TRANSPORTE ----------------
                if transporte_sustentavel >= 0 and transporte_sustentavel <=0.25:
                    mensagemT = "Sustentável, Parábens"
                    mensagemPopUpT = "Você utiliza transportes sustentáveis com frequência! Ótimo para o meio ambiente e para você!"
                elif transporte_sustentavel >0.25 and transporte_sustentavel <=0.75:
                    mensagemT = "Pouco Sustentável"
                    mensagemPopUpT = "Você usa meios sustentáveis às vezes, mas ainda pode melhorar! Dê preferência a bicicletas, caminhadas e transporte público."
                else:
                    mensagemT = "Insustentável"
                    mensagemPopUpT = "Uso elevado de transportes poluentes! Reduza a dependência de carros particulares e adote alternativas mais verdes."
                    
                dados = {
                    "agua": {"valor": s_agua, "mensagem": mensagemA},
                    "nao_reciclaveis": {"valor": s_reciclaveis, "mensagem": mensagemR},
                    "energia": {"valor": s_energia, "mensagem": mensagemE},
                    "transporte": {"valor": transporte_sustentavel, "mensagem": mensagemT},
                    "pontuacao": estrelas
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
                
                botao_OqueFazer = ctk.CTkButton(frame1,
                                    text="Como Melhorar?",
                                    text_color="white",
                                    fg_color="#686564",
                                    corner_radius=50,
                                    bg_color="#FFFFFF",
                                    hover_color="#363434",
                                    width= 145,
                                    height= 35,
                                    command=lambda: OqueFazer(mensagemPopUpA, mensagemPopUpR, mensagemPopUpE, mensagemPopUpT))
                botao_OqueFazer.place(x=115, y=315)
                                
            else:
                tk.messagebox.showinfo("Estatísticas", "Não foi possível calcular as médias.")
        else:
            tk.messagebox.showinfo("Estatísticas", "Nenhum dado encontrado no banco de dados.")

def OqueFazer(mensagemPopUpA, mensagemPopUpR, mensagemPopUpE, mensagemPopUpT):
    janela_OqueFazer = ctk.CTkToplevel()
    janela_OqueFazer.title("Melhorar minha Sustentabilidade")
    janela_OqueFazer.geometry("450x450") 

    janela_OqueFazer.grab_set()
    janela_OqueFazer.configure(bg_color="#2E2E2E")  

    ctk.CTkLabel(janela_OqueFazer, text="Água:", text_color="white", font=("Arial", 16, "bold")).pack(pady=(10, 0))
    ctk.CTkLabel(janela_OqueFazer, text=mensagemPopUpA, text_color="white", font=("Arial", 14), wraplength=400).pack(pady=5)

    ctk.CTkLabel(janela_OqueFazer, text="Não Recicláveis:", text_color="white", font=("Arial", 16, "bold")).pack(pady=(10, 0))
    ctk.CTkLabel(janela_OqueFazer, text=mensagemPopUpR, text_color="white", font=("Arial", 14), wraplength=400).pack(pady=5)

    ctk.CTkLabel(janela_OqueFazer, text="Energia Elétrica:", text_color="white", font=("Arial", 16, "bold")).pack(pady=(10, 0))
    ctk.CTkLabel(janela_OqueFazer, text=mensagemPopUpE, text_color="white", font=("Arial", 14), wraplength=400).pack(pady=5)

    ctk.CTkLabel(janela_OqueFazer, text="Transporte:", text_color="white", font=("Arial", 16, "bold")).pack(pady=(10, 0))
    ctk.CTkLabel(janela_OqueFazer, text=mensagemPopUpT, text_color="white", font=("Arial", 14), wraplength=400).pack(pady=5)


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