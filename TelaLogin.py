import customtkinter as ctk
import SistemaComBD

# --- Configuração inicial ---
ctk.set_appearance_mode("Dark")

janela = ctk.CTk()
janela.title("Sistema de Sustentabilidade")
janela.geometry("400x400")

# --- Título global ---
titulo = ctk.CTkLabel(janela, text="Bem-vindo!", font=ctk.CTkFont(size=24, weight="bold"))
titulo.pack(pady=20)

# --- Frame principal para trocar entre login e cadastro ---
frame_abas = ctk.CTkFrame(janela)
frame_abas.pack(pady=10)

# --- Frame que muda com o conteúdo de login/cadastro ---
frame_conteudo = ctk.CTkFrame(janela)
frame_conteudo.pack(pady=15)

# --- Label de resultado geral ---
resultado = ctk.CTkLabel(janela, text="", font=ctk.CTkFont(size=12))
resultado.pack(pady=8)

# --- Referência global dos botões ---
botao_login = None
botao_cadastro = None

# --- Funções de abas com mudança de cor ---
def exibir_login():
    resultado.configure(text="")
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    botao_login.configure(fg_color="#4caf50", hover_color="#388e3c")
    botao_cadastro.configure(fg_color="#2e7d32", hover_color="#1b5e20")

    campo_usuario = ctk.CTkEntry(frame_conteudo, placeholder_text="Usuário", border_color="#81c784", width=260)
    campo_usuario.pack(pady=10)
    
    campo_senha = ctk.CTkEntry(frame_conteudo, placeholder_text="Senha", show="*", border_color="#81c784", width=260)
    campo_senha.pack(pady=10)

    def login():
        usuario = campo_usuario.get()
        senha = campo_senha.get()
        if usuario == "" and senha == "":
            # --- Esconde a janela de login ---
            janela.withdraw()  
            SistemaComBD.chamar_janela()
        else:
            resultado.configure(text="Usuário ou senha incorretos", text_color="#ff8a80")

    ctk.CTkButton(frame_conteudo, text="Entrar", command=login, fg_color="#4caf50", hover_color="#388e3c", width=200).pack(pady=15)

def exibir_cadastro():
    resultado.configure(text="")
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    botao_cadastro.configure(fg_color="#4caf50", hover_color="#388e3c")
    botao_login.configure(fg_color="#2e7d32", hover_color="#1b5e20")

    campo_usuario = ctk.CTkEntry(frame_conteudo, placeholder_text="Usuário", border_color="#81c784", width=260)
    campo_usuario.pack(pady=10)

    campo_senha = ctk.CTkEntry(frame_conteudo, placeholder_text="Senha", show="*", border_color="#81c784", width=260)
    campo_senha.pack(pady=10)

    def cadastrar():
        usuario = campo_usuario.get()
        senha = campo_senha.get()

        if usuario and senha:
            resultado.configure(text="Cadastro realizado com sucesso!", text_color="#b9fbc0")
        else:
            resultado.configure(text="Preencha todos os campos.", text_color="#ffb74d")

    ctk.CTkButton(frame_conteudo, text="Cadastrar", command=cadastrar, fg_color="#4caf50", hover_color="#388e3c", width=200).pack(pady=15)

# --- Criar botões Login e Cadastrar ---
botao_login = ctk.CTkButton(frame_abas, text="Login", width=100, command=exibir_login)
botao_login.grid(row=0, column=0, padx=10, pady=10)

botao_cadastro = ctk.CTkButton(frame_abas, text="Cadastrar", width=100, command=exibir_cadastro)
botao_cadastro.grid(row=0, column=1, padx=10, pady=10)

# --- Rodapé ---
rodape = ctk.CTkLabel(janela, text="2025 Sistema de Sustentabilidade", font=ctk.CTkFont(size=10, slant="italic"), text_color="#a5d6a7")
rodape.pack(side="bottom", pady=10)

# --- Inicia com login ---
exibir_login()

# --- Iniciar programa ---
janela.mainloop()