import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

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
        texto_addRegistros.place(x=140, y=30)
        
        #-----Texto e entrada do campo agua-----
        texto_consumoAgua = ctk.CTkLabel(frame1, 
                     text="Consumo de água (L):", 
                     text_color="black")
        texto_consumoAgua.place(x=50, y=80)
        
        entrada_agua = ctk.CTkEntry(frame1, 
                                    width=200)
        entrada_agua.place(x=50, y=100)
        
        #-----Texto e entrada da geração de resíduos-----
        texto_geracaoResiduos = ctk.CTkLabel(frame1,
                     text="Não recicláveis (kg):",
                     text_color="black")
        texto_geracaoResiduos.place(x=50, y=130)
        
        entrada_geracaoResiduos= ctk.CTkEntry(frame1, 
                                         width=200)
        entrada_geracaoResiduos.place(x=50, y=150)
        
        #-----Texto e entrada da energia gasta-----
        texto_energiaGasta = ctk.CTkLabel(frame1, 
                     text="Energia elétrica (kWh):", 
                     text_color="black")
        texto_energiaGasta.place(x=50, y=180)
        
        entrada_energiaGasta = ctk.CTkEntry(frame1, 
                                     width=200)
        entrada_energiaGasta.place(x=50, y=200)
        
        #-----Texto e entrada do tipo de transporte-----
        texto_tipoTransporte = ctk.CTkLabel(frame1, 
                     text="Tipo de transporte:",
                     text_color="black")
        texto_tipoTransporte.place(x=50, y=230)
        
        entrada_tipoTransporte = ctk.CTkEntry(frame1, 
                                        width=200)
        entrada_tipoTransporte.place(x=50, y=250)
        
        #-----Botão adicionar registros-----
        botao_addResgistros = ctk.CTkButton(frame1, 
                      text="Cadastrar", 
                      fg_color="#474444", 
                      corner_radius=50,
                      command=lambda: messagebox.showinfo("Cadastro", "Dados cadastrados com sucesso!"))
        botao_addResgistros.place(x=140, y=310)
    
    #-----Aba "Registros"-----
    elif aba == "Registros":
        texto_consultarID = ctk.CTkLabel(frame1, 
                     text="Consultar por ID:", 
                     text_color="black")
        texto_consultarID.place(x=50, y=80)
        
        entrada_id = ctk.CTkEntry(frame1, width=200)
        entrada_id.place(x=50, y=100)
        
        botao_consultar = ctk.CTkButton(frame1, 
                      text="Consultar", 
                      fg_color="#474444", 
                      command=lambda: messagebox.showinfo("Consulta", "Exibir detalhes do registro..."))
        botao_consultar.place(x=50, y=130)
        
    #-----Aba Ações-----
    elif aba == "Acoes":
    
        minha_imagem = ctk.CTkImage(light_image=Image.open('ApresentaçãoPI\Acoes.png'),
                                    dark_image=Image.open('ApresentaçãoPI\Acoes.png'),
                                    size=(360,500))
        label_foto = ctk.CTkLabel(frame1, text="", image=minha_imagem)
        label_foto.place(x=0, y=0)
        
    #-----Aba Graficos-----
    elif aba == "Grafico":
        minha_imagem = ctk.CTkImage(light_image=Image.open('ApresentaçãoPI\Grafico.png'),
                                    dark_image=Image.open('ApresentaçãoPI\Grafico.png'),
                                    size=(360,450))
        label_foto = ctk.CTkLabel(frame1, text="", image=minha_imagem)
        label_foto.place(x=0, y=0)
    
    elif aba == "Estatistica":
        minha_imagem = ctk.CTkImage(light_image=Image.open('ApresentaçãoPI\Estatistica.png'),
                                    dark_image=Image.open('ApresentaçãoPI\Estatistica.png'),
                                    size=(360,450))
        label_foto = ctk.CTkLabel(frame1, text="", image=minha_imagem)
        label_foto.place(x=0, y=0)
        

botao_adiconarRegistro = ctk.CTkButton(janela_principal,
                                text="Adicionar registros",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434",
                                command=lambda: mudar_aba("Adicionar registros"))
botao_adiconarRegistro.place(x=460, y=60)
    
botao_registros = ctk.CTkButton(janela_principal,
                                text="Registros",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434",
                                command=lambda: mudar_aba("Registros"))
botao_registros.place(x=460, y=120)
    
botao_acoes = ctk.CTkButton(janela_principal,
                                text="Ações",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434",
                                command=lambda: mudar_aba("Acoes"))
botao_acoes.place(x=460, y=180)
    
botao_graficos = ctk.CTkButton(janela_principal,
                                text="Gráfico",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434",
                                command=lambda: mudar_aba("Grafico"))
botao_graficos.place(x=460, y=240)
    
botao_estatistica = ctk.CTkButton(janela_principal,
                                text="Estatística",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434",
                                command=lambda: mudar_aba("Estatistica"))
botao_estatistica.place(x=460, y=300)

titulo_addRegistro = ctk.CTkLabel(frame1,
                                  text='Sistema Sustentabilidade',
                                  text_color="black",
                                  font=("Arial", 23))
titulo_addRegistro.place(x=100, y=altura/20)

mudar_aba("Adicionar registros")

#-----Iniciar programa-----
janela_principal.mainloop()
