import tkinter as tk
from tkinter import ttk, messagebox

class Database:
    def __init__(self):
        self.filmes = []
        self.auditoria = []

    def adicionar_filme(self, titulo, diretor, ano):
        novo_filme = {"titulo": titulo, "diretor": diretor, "ano": ano}
        self.filmes.append(novo_filme)
        self.auditoria.append({"acao": "Adicionado", "dados": novo_filme})

    def editar_filme(self, index, titulo, diretor, ano):
        filme_original = self.filmes[index]
        self.filmes[index] = {"titulo": titulo, "diretor": diretor, "ano": ano}
        self.auditoria.append({"acao": "Editado", "dados": filme_original})

    def excluir_filme(self, index):
        filme_excluido = self.filmes.pop(index)
        self.auditoria.append({"acao": "Excluído", "dados": filme_excluido})

    def restaurar_dados(self, dados):
        self.filmes.append(dados)

class TelaFilmes:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Gerenciar Filmes")

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("Titulo", "Diretor", "Ano"), show="headings")
        self.tree.heading("Titulo", text="Título")
        self.tree.heading("Diretor", text="Diretor")
        self.tree.heading("Ano", text="Ano")
        self.tree.pack(pady=10, fill="both", expand=True)

        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Adicionar", command=self.adicionar).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Editar", command=self.editar).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Excluir", command=self.excluir).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Tela de Auditoria", command=self.abrir_tela_auditoria).pack(side="left", padx=5)

        self.carregar_filmes()

    def carregar_filmes(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for filme in self.db.filmes:
            self.tree.insert("", "end", values=(filme["titulo"], filme["diretor"], filme["ano"]))

    def adicionar(self):
        self.abrir_formulario("Adicionar Filme", self.db.adicionar_filme)

    def editar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um filme para editar!")
            return
        index = self.tree.index(selecionado[0])
        filme = self.db.filmes[index]
        self.abrir_formulario("Editar Filme", self.db.editar_filme, index, filme)

    def excluir(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um filme para excluir!")
            return
        index = self.tree.index(selecionado[0])
        self.db.excluir_filme(index)
        self.carregar_filmes()

    def abrir_formulario(self, titulo, acao, index=None, filme=None):
        form = tk.Toplevel(self.root)
        form.title(titulo)

        ttk.Label(form, text="Título:").grid(row=0, column=0, padx=5, pady=5)
        titulo_entry = ttk.Entry(form)
        titulo_entry.grid(row=0, column=1, padx=5, pady=5)
        if filme:
            titulo_entry.insert(0, filme["titulo"])

        ttk.Label(form, text="Diretor:").grid(row=1, column=0, padx=5, pady=5)
        diretor_entry = ttk.Entry(form)
        diretor_entry.grid(row=1, column=1, padx=5, pady=5)
        if filme:
            diretor_entry.insert(0, filme["diretor"])

        ttk.Label(form, text="Ano:").grid(row=2, column=0, padx=5, pady=5)
        ano_entry = ttk.Entry(form)
        ano_entry.grid(row=2, column=1, padx=5, pady=5)
        if filme:
            ano_entry.insert(0, filme["ano"])

        def salvar():
            titulo = titulo_entry.get()
            diretor = diretor_entry.get()
            ano = ano_entry.get()

            if not (titulo and diretor and ano):
                messagebox.showwarning("Aviso", "Preencha todos os campos!")
                return

            try:
                ano = int(ano)
            except ValueError:
                messagebox.showwarning("Aviso", "O ano deve ser um número inteiro!")
                return

            if filme:
                acao(index, titulo, diretor, ano)
            else:
                acao(titulo, diretor, ano)
            self.carregar_filmes()
            form.destroy()

        ttk.Button(form, text="Salvar", command=salvar).grid(row=3, column=0, columnspan=2, pady=10)

    def abrir_tela_auditoria(self):
        TelaAuditoria(self.root, self.db, self.carregar_filmes)

class TelaAuditoria:
    def __init__(self, root, db, callback):
        self.root = tk.Toplevel(root)
        self.db = db
        self.callback = callback
        self.root.title("Tela de Auditoria")

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("Ação", "Dados"), show="headings")
        self.tree.heading("Ação", text="Ação")
        self.tree.heading("Dados", text="Dados")
        self.tree.pack(pady=10, fill="both", expand=True)

        ttk.Button(self.frame, text="Restaurar Dados", command=self.restaurar_dados).pack(pady=10)

        self.carregar_auditoria()

    def carregar_auditoria(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for registro in self.db.auditoria:
            self.tree.insert("", "end", values=(registro["acao"], registro["dados"]))

    def restaurar_dados(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um registro para restaurar!")
            return
        index = self.tree.index(selecionado[0])
        dados = self.db.auditoria[index]["dados"]
        self.db.restaurar_dados(dados)
        self.callback()
        messagebox.showinfo("Sucesso", "Dados restaurados com sucesso!")

if __name__ == "__main__":
    db = Database()
    root = tk.Tk()
    TelaFilmes(root, db)
    root.mainloop()
