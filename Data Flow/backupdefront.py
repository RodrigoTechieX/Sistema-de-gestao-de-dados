import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from backend import BancoDeDados  # Importa o backend para interagir com o banco de dados

# Instanciar e configurar banco de dados
db = BancoDeDados()

# Funções de navegação entre telas
def cadastrar_usuario():
    frame_login.pack_forget()
    frame_cadastro.pack(fill="both", expand=True)

def salvar_usuario():
    usuario = entry_usuario_cadastro.get()
    senha = entry_senha_cadastro.get()
    if db.cadastrar_usuario(usuario, senha):
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        voltar_login()
    else:
        messagebox.showerror("Erro", "Usuário já cadastrado!")

def voltar_login():
    frame_cadastro.pack_forget()
    frame_login.pack(fill="both", expand=True)

def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if db.validar_login(usuario, senha):
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        frame_login.pack_forget()
        TelaPrincipal(janela, db, frame_login)
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

# Função para centralizar a janela
def centralizar_janela(janela, largura, altura):
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

# Função para remover o texto placeholder
def on_click(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)  # Apaga o texto placeholder
        entry.config(fg="black")  # Muda a cor do texto para preto

# Função para colocar o texto placeholder se o campo estiver vazio
def on_focusout(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)  # Coloca o texto placeholder
        entry.config(fg="gray")  # Muda a cor do texto para cinza


# Configuração da janela principal
janela = tk.Tk()
janela.title("Data Flow - Sistema de gerenciamento de dados")

# Centralizar janela
largura_janela = 800
altura_janela = 600
centralizar_janela(janela, largura_janela, altura_janela)

# Frame de Login
frame_login = tk.Frame(janela)
frame_login.pack(fill="both", expand=True)

# Alterar a cor de fundo da janela
#frame_login.configure(bg="white")  # Fundo da aplicação

# Carrega e exibe a imagem da logo com um fundo integrado
imagem_original = Image.open("C:/Users/rodri/OneDrive/Área de Trabalho/Data Flow/imagens/dataflowoficial.png")
imagem_redimensionada = imagem_original.resize((280, 250), Image.LANCZOS)
imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
label_imagem = tk.Label(frame_login, image=imagem_tk)
label_imagem.image = imagem_tk
label_imagem.place(relx=0.5, rely=0.23, anchor="center", relwidth=0.37, relheight=0.4)


# Frame da logo para destacar o fundo
#frame_logo = tk.Frame(frame_login, bg="white")
#frame_logo.place(relx=0.5, rely=0.2, anchor="center", relwidth=0.4, relheight=0.5)

#label_imagem = tk.Label(frame_logo, image=imagem_tk, bg="white")
#label_imagem.image = imagem_tk
#label_imagem.pack(fill="both", expand=True)

# Campos de entrada na tela de login
label_usuario = tk.Label(frame_login, text="Login:", font=("Helvetica", 11, "bold"))
label_usuario.place(relx=0.37 ,rely=0.44, anchor="center")

entry_usuario = tk.Entry(frame_login, fg="gray")
entry_usuario.insert(0, "Digite o seu login")  # Texto placeholder
entry_usuario.bind("<FocusIn>", lambda e: on_click(entry_usuario, "Digite o seu login"))
entry_usuario.bind("<FocusOut>", lambda e: on_focusout(entry_usuario, "Digite o seu login"))
entry_usuario.pack(pady=5)
entry_usuario.place(relx=0.5, rely=0.48, anchor="center", relwidth=0.3, relheight=0.04)

label_senha = tk.Label(frame_login, text="Senha:", font=("Helvetica", 11, "bold"))
label_senha.place(relx=0.37, rely=0.54, anchor="center")

entry_senha = tk.Entry(frame_login, fg="gray")
entry_senha.insert(0, "Senha")  # Texto placeholder
entry_senha.bind("<FocusIn>", lambda e: on_click(entry_senha, "Senha"))
entry_senha.bind("<FocusOut>", lambda e: on_focusout(entry_senha, "Senha"))
entry_senha.pack(pady=5)
entry_senha.place(relx=0.5, rely=0.58, anchor="center", relwidth=0.3, relheight=0.04)

# Botões de Login e Cadastrar
botao_login = tk.Button(frame_login, text="Login", bg="blue", fg="white", command=fazer_login)
botao_login.place(relx=0.5, rely=0.70, anchor="center", relwidth=0.3, relheight=0.04)

botao_cadastrar = tk.Button(frame_login, text="Cadastrar", bg="#D9D9D9", command=cadastrar_usuario)
botao_cadastrar.place(relx=0.5, rely=0.78, anchor="center", relwidth=0.3, relheight=0.04)

# Frame de Cadastro
frame_cadastro = tk.Frame(janela)

label_usuario_cadastro = tk.Label(frame_cadastro, text="Login:", font=("Helvetica", 11, "bold"))
label_usuario_cadastro.place(relx=0.37 ,rely=0.44, anchor="center")

entry_usuario_cadastro = tk.Entry(frame_cadastro, fg="gray")
entry_usuario_cadastro.insert(0, "Crie o seu login")  # Texto placeholder
entry_usuario_cadastro.bind("<FocusIn>", lambda e: on_click(entry_usuario_cadastro, "Crie o seu login"))
entry_usuario_cadastro.bind("<FocusOut>", lambda e: on_focusout(entry_usuario_cadastro, "Crie o seu login"))
entry_usuario_cadastro.pack(pady=5)
entry_usuario_cadastro.place(relx=0.5, rely=0.48, anchor="center", relwidth=0.3, relheight=0.04)

label_senha_cadastro = tk.Label(frame_cadastro, text="Senha:", font=("Helvetica", 11, "bold"))
label_senha_cadastro.place(relx=0.37, rely=0.54, anchor="center")

entry_senha_cadastro = tk.Entry(frame_cadastro, fg="gray")
entry_senha_cadastro.insert(0, "Crie a sua senha")  # Texto placeholder
entry_senha_cadastro.bind("<FocusIn>", lambda e: on_click(entry_senha_cadastro, "Crie a sua senha"))
entry_senha_cadastro.bind("<FocusOut>", lambda e: on_focusout(entry_senha_cadastro, "Crie a sua senha"))
entry_senha_cadastro.pack(pady=5)
entry_senha_cadastro.place(relx=0.5, rely=0.58, anchor="center", relwidth=0.3, relheight=0.04)

botao_voltar = tk.Button(frame_cadastro, text="Voltar", bg="red", command=voltar_login)
botao_voltar.place(relx=0.4, rely=0.7, anchor="center", relwidth=0.2)

botao_salvar = tk.Button(frame_cadastro, text="Cadastrar", bg="green", command=salvar_usuario)
botao_salvar.place(relx=0.6, rely=0.7, anchor="center", relwidth=0.2)

# Adicionar uma função para alterar o título da janela
def alterar_titulo(janela, novo_titulo):
    janela.title(novo_titulo)

# Modificar a função voltar_login para restaurar o título do login
def voltar_login():
    frame_cadastro.pack_forget()
    frame_login.pack(fill="both", expand=True)
    alterar_titulo(janela, "Data Flow - Sistema de gerenciamento de dados")  # Restaurar o título da tela de login

# Atualizar a classe TelaPrincipal para alterar o título ao inicializá-la e restaurar ao voltar para o login
class TelaPrincipal:
    def __init__(self, master, db, frame_login):
        self.master = master
        alterar_titulo(self.master, "Data Flow - Sistema de gerenciamento de dados")  # Define o título para a tela principal
        self.master.geometry("800x600")
        self.db = db
        self.frame_login = frame_login  # Passa a referência do frame_login para a classe

        # Frame de Lobby
        self.frame_principal = tk.Frame(master)
        self.frame_principal.pack(fill="both", expand=True)

        # Título de Lobby
        tk.Label(self.frame_principal, text="Bem-vindo ao Lobby", font=("Arial", 16, "bold")).pack(pady=20)

        # Botões
        botao_ir_filmes = tk.Button(self.frame_principal, text="Tabela de Filmes", command=self.ir_para_filmes)
        botao_ir_filmes.place(relx=0.6, rely=0.7, anchor="center", relwidth=0.1, relheight=0.1)
        
        # Botão de voltar ao login
        botao_voltar_login = tk.Button(self.frame_principal, text="Voltar",bg="red", command=self.voltar_login)
        botao_voltar_login.place(relx=0.05, rely=0.1, anchor="center", relwidth=0.05, relheight=0.05)

    def ir_para_filmes(self):
        # Esconde a tela principal e exibe a tela de filmes
        self.frame_principal.pack_forget()
        SistemaDeGerenciamento(self.master, self.db)  # Passa para a tela de filmes sem criar uma nova instância desnecessária

    def voltar_login(self):
        self.frame_principal.pack_forget()
        frame_login.pack(fill="both", expand=True)
        alterar_titulo(self.master, "Data Flow - Sistema de gerenciamento de dados")  # Restaurar o título da tela de login


# Frontend - Interface Gráfica de Filmes
class SistemaDeGerenciamento:
    def __init__(self, master, db):
        self.master = master
        self.master.title("Data Flow - Sistema de gerenciamento de dados")
        self.master.geometry("800x600")

        self.db = db  # Banco de dados já instanciado

        # Configuração do Frame de Filmes
        self.frame_filmes = tk.Frame(master)
        self.frame_filmes.pack(fill="both", expand=True)
        self.filme_atual_id = None  # ID do filme sendo editado (se houver)

        self.setup_tela_filmes()
        self.carregar_filmes()  # Carregar os filmes assim que a tela for carregada

         #Vincula o movimento do mouse ao frame_filmes
        #self.frame_filmes.bind("<Motion>", self.atualizar_coordenadas)

    def setup_tela_filmes(self):
       # Frame esquerdo para campos e botões
        frame_esquerdo = tk.Frame(self.frame_filmes)
        frame_esquerdo.pack(side="left", fill="y", padx=10, pady=10)

       # Rótulo para exibir as coordenadas do mouse
       # self.label_coordenadas = tk.Label(frame_esquerdo, text="Coordenadas: (x=0, y=0)", font=("Helvetica", 10))
       # self.label_coordenadas.pack(pady=5)

       # Rótulos e campos de entrada
        tk.Label(frame_esquerdo, text="Título do Filme:").pack(anchor="w", pady=5)
        self.entry_titulo = tk.Entry(frame_esquerdo)
        self.entry_titulo.pack(pady=5)

        tk.Label(frame_esquerdo, text="Diretor:").pack(anchor="w", pady=5)
        self.entry_diretor = tk.Entry(frame_esquerdo)
        self.entry_diretor.pack(pady=5)

        tk.Label(frame_esquerdo, text="Ano:").pack(anchor="w", pady=5)
        self.entry_ano = tk.Entry(frame_esquerdo)
        self.entry_ano.pack(pady=5)

        tk.Label(frame_esquerdo, text="Gênero:").pack(anchor="w", pady=5)
        self.entry_genero = tk.Entry(frame_esquerdo)
        self.entry_genero.pack(pady=5)

        tk.Label(frame_esquerdo, text="Duração (em minutos):").pack(anchor="w", pady=5)
        self.entry_duracao = tk.Entry(frame_esquerdo)
        self.entry_duracao.pack(pady=5)

       # Botões
        tk.Button(frame_esquerdo, text="Adicionar Filme", bg="#40F020", command=self.adicionar_filme, width=15).pack(pady=5)
        tk.Button(frame_esquerdo, text="Editar Filme", bg="#EFDE0F", command=self.editar_filme, width=15).pack(pady=5)
        tk.Button(frame_esquerdo, text="Excluir Filme", bg="#F01612", command=self.excluir_filme, width=15).pack(pady=5)
        tk.Button(frame_esquerdo, text="Voltar para o Lobby", bg="#535557", command=self.voltar_lobby, width=15).pack(pady=5)

        # Frame direito para pesquisa e tabela
        frame_direito = tk.Frame(self.frame_filmes)
        frame_direito.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Botão de registro de auditoria no canto superior direito do frame_direito
        tk.Button(frame_direito, text="Registro de Auditoria", bg="#0E80F0", command=self.ir_para_auditoria, width=15, height=1).place(relx=1.0, y=5, anchor="ne")

        # Barra de Pesquisa no topo do frame direito
        label_pesquisa = tk.Label(frame_direito, text="Pesquisar Filme:", font=("Helvetica", 12))
        label_pesquisa.pack(anchor="center", pady=5)

        # Entry para pesquisa de filmes
        self.entry_pesquisa = tk.Entry(frame_direito, width=40)
        self.entry_pesquisa.pack(pady=5)
        self.entry_pesquisa.bind("<KeyRelease>", self.filtrar_filmes)

        # Tabela de Filmes com Barra de Rolagem
        self.frame_tabela = tk.Frame(frame_direito)
        self.frame_tabela.pack(fill="both", expand=True, pady=7)

        # Adiciona a barra de rolagem
        scrollbar = ttk.Scrollbar(self.frame_tabela, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # Configura a Treeview para usar a barra de rolagem
        self.tree = ttk.Treeview(self.frame_tabela, columns=("ID", "Título", "Diretor", "Ano", "Gênero", "Duração"), show="headings", yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tree.yview)

        # Configuração das colunas
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col, anchor="center")
            self.tree.column(col, anchor="center")

            self.tree.pack(fill="both", expand=True)

 

    #def atualizar_coordenadas(self, event):
    #    """Atualiza o rótulo com as coordenadas do mouse."""
    #    x, y = event.x, event.y
    #    self.label_coordenadas.config(text=f"Coordenadas: (x={x}, y={y})")

    def ir_para_auditoria(self):
        self.frame_filmes.pack_forget()
        TelaAuditoria(self.master, self.db, self.frame_filmes)



    def voltar_lobby(self):
        self.frame_filmes.pack_forget()
        TelaPrincipal(self.master, self.db, frame_login) 



    def adicionar_filme(self):
        titulo = self.entry_titulo.get()
        diretor = self.entry_diretor.get()
        ano = self.entry_ano.get()
        genero = self.entry_genero.get()
        duracao = self.entry_duracao.get()

        if not titulo or not diretor or not genero or not ano.isdigit() or not duracao.isdigit():
            messagebox.showwarning("Aviso", "Preencha todos os campos corretamente!")
            return

        if self.filme_atual_id:  # Se estiver em modo de edição
            self.db.atualizar_filme(self.filme_atual_id, titulo, diretor, ano, genero, duracao)
            messagebox.showinfo("Sucesso", "Filme atualizado com sucesso!")
            self.filme_atual_id = None
        else:
            self.db.adicionar_filme(titulo, diretor, ano, genero, duracao)
            messagebox.showinfo("Sucesso", "Filme adicionado com sucesso!")

        self.limpar_campos()
        self.carregar_filmes()

    def editar_filme(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione um filme para editar!")
            return

        item = self.tree.item(selected_item)
        filme = item["values"]

        self.filme_atual_id = filme[0]
        self.entry_titulo.delete(0, tk.END)
        self.entry_titulo.insert(0, filme[1])
        self.entry_diretor.delete(0, tk.END)
        self.entry_diretor.insert(0, filme[2])
        self.entry_ano.delete(0, tk.END)
        self.entry_ano.insert(0, filme[3])
        self.entry_genero.delete(0, tk.END)
        self.entry_genero.insert(0, filme[4])
        self.entry_duracao.delete(0, tk.END)
        self.entry_duracao.insert(0, filme[5])

    def limpar_campos(self):
        self.entry_titulo.delete(0, tk.END)
        self.entry_diretor.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_genero.delete(0, tk.END)
        self.entry_duracao.delete(0, tk.END)

    def excluir_filme(self):
        selected_item = self.tree.selection()
        if selected_item:
            id_filme = self.tree.item(selected_item)["values"][0]
            self.db.excluir_filme(id_filme)
            messagebox.showinfo("Sucesso", "Filme excluído com sucesso!")
            self.carregar_filmes()
        else:
            messagebox.showwarning("Aviso", "Selecione um filme para excluir!")

    def carregar_filmes(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for filme in self.db.consultar_filmes():
            self.tree.insert("", "end", values=filme)

    def filtrar_filmes(self, event):
        filtro = self.entry_pesquisa.get().lower()

        for item in self.tree.get_children():
            self.tree.delete(item)

        filmes_filtrados = self.db.pesquisar_filmes(filtro)

        for filme in filmes_filtrados:
            self.tree.insert("", "end", values=filme)


    def voltar_login(self):
        self.frame_filmes.pack_forget()
        # Insira a lógica para exibir o frame de login ou uma mensagem de redirecionamento.

        frame_login.pack(fill="both", expand=True)


class TelaAuditoria:
    def __init__(self, master, db, callback_voltar):
        self.master = master
        self.db = db
        self.callback_voltar = callback_voltar

        # Cria o frame principal da tela de auditoria
        self.frame_auditoria = tk.Frame(self.master)
        self.frame_auditoria.pack(fill="both", expand=True)

        self.setup_tela()
        self.carregar_auditoria()

    def setup_tela(self):
        # Título e botões no topo da tela
        frame_topo_auditoria = tk.Frame(self.frame_auditoria)
        frame_topo_auditoria.pack(fill="x", pady=10)

        label_titulo_auditoria = tk.Label(frame_topo_auditoria, text="Auditoria de Registros", font=("Arial", 16, "bold"))
        label_titulo_auditoria.pack(side="top", padx=20)

        # Barra de Pesquisa
        label_pesquisa = tk.Label(frame_topo_auditoria, text="Pesquisar na Auditoria:")
        label_pesquisa.pack(side="left", padx=10)
        self.entry_pesquisa = tk.Entry(frame_topo_auditoria)
        self.entry_pesquisa.pack(side="left", padx=10)
        self.entry_pesquisa.bind("<KeyRelease>", self.filtrar_auditoria)

        botao_restaurar_dados = tk.Button(frame_topo_auditoria, text="Restaurar Dados Selecionados", command=self.restaurar_dados)
        botao_restaurar_dados.pack(side="left", padx=10)

        botao_excluir_registro = tk.Button(frame_topo_auditoria, text="Excluir Registro Selecionado", command=self.excluir_registro)
        botao_excluir_registro.pack(side="right", padx=10)

        botao_voltar = tk.Button(frame_topo_auditoria, text="Voltar", command=self.voltar_tela_anterior)
        botao_voltar.pack(side="left", padx=10)

        # Configuração da tabela de auditoria
        scrollbar_auditoria = ttk.Scrollbar(self.frame_auditoria, orient="vertical")
        scrollbar_auditoria.pack(side="right", fill="y")

        self.tree_auditoria = ttk.Treeview(
            self.frame_auditoria,
            columns=("ID", "Operação", "Tabela", "Dados", "Data e Hora"),
            show="headings",
            yscrollcommand=scrollbar_auditoria.set
        )
        scrollbar_auditoria.config(command=self.tree_auditoria.yview)

        # Configurações das colunas
        self.tree_auditoria.heading("ID", text="ID")
        self.tree_auditoria.heading("Operação", text="Operação")
        self.tree_auditoria.heading("Tabela", text="Tabela")
        self.tree_auditoria.heading("Dados", text="Dados")
        self.tree_auditoria.heading("Data e Hora", text="Data e Hora")

        self.tree_auditoria.column("ID", anchor="center", width=50)
        self.tree_auditoria.column("Operação", anchor="center", width=100)
        self.tree_auditoria.column("Tabela", anchor="center", width=100)
        self.tree_auditoria.column("Dados", anchor="w", width=300)
        self.tree_auditoria.column("Data e Hora", anchor="center", width=150)

        self.tree_auditoria.pack(fill="both", expand=True)

    def carregar_auditoria(self):
        # Limpa a tabela antes de adicionar os registros atualizados
        for item in self.tree_auditoria.get_children():
            self.tree_auditoria.delete(item)

        # Carrega todos os registros de auditoria do banco de dados
        for registro in self.db.consultar_auditoria():
            self.tree_auditoria.insert("", "end", values=registro)


    def filtrar_auditoria(self, event):
        # Obtém o texto da pesquisa
        filtro = self.entry_pesquisa.get().lower()

        # Limpa a tabela
        for item in self.tree_auditoria.get_children():
            self.tree_auditoria.delete(item)

        # Filtra os registros no banco de dados
        registros_filtrados = self.db.pesquisar_auditoria(filtro)

        # Adiciona os registros filtrados à tabela
        for registro in registros_filtrados:
            self.tree_auditoria.insert("", "end", values=registro)

    def restaurar_dados(self):
        selected_item = self.tree_auditoria.selection()
        if selected_item:
            registro = self.tree_auditoria.item(selected_item)["values"]  # Obtém os dados do registro selecionado
            tabela = registro[2]  # Tabela (exemplo: "filmes")
            dados = registro[3]  # Campo "Dados" com os valores

            confirmar = messagebox.askyesno("Confirmação", f"Deseja restaurar os dados selecionados na tabela '{tabela}'?")
            if confirmar:
                try:
                    self.db.restaurar_dados(tabela, dados)  # Chama o método do backend para restaurar
                    messagebox.showinfo("Sucesso", "Dados restaurados com sucesso!")
                    self.carregar_auditoria()  # Atualiza a tabela de auditoria
                except Exception as e:
                    messagebox.showerror("Erro", f"Falha ao restaurar dados: {e}")
        else:
            messagebox.showwarning("Aviso", "Selecione um registro para restaurar!")

    def excluir_registro(self):
        selected_item = self.tree_auditoria.selection()
        if selected_item:
            id_registro = self.tree_auditoria.item(selected_item)["values"][0]  # Obtém o ID do registro
            confirmar = messagebox.askyesno("Confirmação", "Tem certeza de que deseja excluir este registro?")
            if confirmar:
                self.db.excluir_registro_auditoria(id_registro)  # Chama o método do backend
                messagebox.showinfo("Sucesso", "Registro excluído com sucesso!")
                self.carregar_auditoria()
        else:
            messagebox.showwarning("Aviso", "Selecione um registro para excluir!")



    def voltar_tela_anterior(self):
        self.frame_auditoria.pack_forget()

        SistemaDeGerenciamento(self.master, self.db)
        

  
# iIncializar a janela principal
janela.mainloop()