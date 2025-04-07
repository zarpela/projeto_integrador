import customtkinter as ctk
import tkinter
import SistemaComBD

#-----Aparência-----
ctk.set_appearance_mode("Dark")

#-----Função Validar Login-----
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    if usuario == '' and senha == '':
        resultado_login.configure(text="Login feito com sucesso", text_color='green')
        SistemaComBD.chamar_janela()
    else:
        resultado_login.configure(text="Login incorreto", text_color='red')       


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