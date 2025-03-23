import customtkinter as ctk
import tkinter

#-----Aparência-----
ctk.set_appearance_mode("Dark")

#-----Função Validar Login-----
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    if usuario == 'jorge' and senha == '123':
        resultado_login.configure(text="Login feito com sucesso", text_color='green')
        tela_principal()
    else:
        resultado_login.configure(text="Login incorreto", text_color='red')
        
    if usuario == '' and senha == '':
        resultado_login.configure(text="Login feito com sucesso", text_color='green')
        tela_principal()


#-----Função Criar Janela Principal-----
def tela_principal():
    janela_principal = ctk.CTkToplevel(janela_login)
    janela_principal.title("Sustentabilidade")
    janela_principal.geometry("700x500")
    
    #-----Frames da Janela Principal-----
    frame1 = ctk.CTkFrame(master = janela_principal,
                          width=400, 
                          height=400,
                          fg_color="#ffffff", 
                          bg_color="#ffffff")
    frame1.place(x=10, y=50)

    frame2 = ctk.CTkFrame(janela_principal,
                          width=250,
                          height=400,
                          fg_color="#cccccc", 
                          bg_color="#cccccc")
    frame2.place(x=400, y=50)
    
    #-----Mudar Abas-----
    botao_adiconarRegistro = ctk.CTkButton(janela_principal,
                                text="Adicionar registros",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434")
    botao_adiconarRegistro.place(x=460, y=110)
    
    botao_registros = ctk.CTkButton(janela_principal,
                                text="Registros",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434")
    botao_registros.place(x=460, y=170)
    
    botao_acoes = ctk.CTkButton(janela_principal,
                                text="ações",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434")
    botao_acoes.place(x=460, y=230)
    
    botao_graficos = ctk.CTkButton(janela_principal,
                                text="Gráfico",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434")
    botao_graficos.place(x=460, y=290)
    
    botao_estatistica = ctk.CTkButton(janela_principal,
                                text="Estatística",
                                text_color="white",
                                fg_color="#686564",
                                corner_radius=50,
                                bg_color="#cccccc",
                                hover_color="#363434")
    botao_estatistica.place(x=460, y=350)


#-----Criar Janela de Login-----
janela_login =  ctk.CTk()
janela_login.title("Login")
janela_login.geometry('300x300')


#-----Tela de Login-----
texto_usuario = ctk.CTkLabel(janela_login, text='Usuário')
texto_usuario.pack(pady = 7)
campo_usuario = ctk.CTkEntry(janela_login, placeholder_text='Digite o usuário')
campo_usuario.pack(pady = 7)

texto_senha = ctk.CTkLabel(janela_login, text='Senha')
texto_senha.pack(pady = 7)
campo_senha = ctk.CTkEntry(janela_login, placeholder_text='Digite a senha', show='*')
campo_senha.pack(pady = 7)

botao_login = ctk.CTkButton(janela_login, text='Login', command=validar_login)
botao_login.pack(pady = 20)

resultado_login = ctk.CTkLabel(janela_login, text='')
resultado_login.pack(pady = 7)


#-----Iniciar programa-----
janela_login.mainloop()