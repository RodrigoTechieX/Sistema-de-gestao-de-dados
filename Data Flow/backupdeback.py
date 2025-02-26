import sqlite3
from datetime import datetime

class BancoDeDados:
    def __init__(self):
        self.conexao = sqlite3.connect("dados.db")
        self.criar_tabelas()

    def criar_tabelas(self):
        cursor = self.conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY,
                            usuario TEXT UNIQUE,
                            senha TEXT)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS filmes (
                            id INTEGER PRIMARY KEY,
                            titulo TEXT,
                            diretor TEXT,
                            ano INTEGER,
                            genero TEXT,
                            duracao INTEGER)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS auditoria (
                            id INTEGER PRIMARY KEY,
                            operacao TEXT,
                            tabela TEXT,
                            dados TEXT,
                            data_hora TEXT)''')  # Tabela para armazenar logs de auditoria
        
        # Método de pesquisa flexível no banco de dados
    def pesquisar_filmes(self, termo_pesquisa):
        cursor = self.conexao.cursor()
        cursor.execute('''SELECT * FROM filmes WHERE
                          id LIKE ? OR
                          titulo LIKE ? OR 
                          diretor LIKE ? OR 
                          ano LIKE ? OR 
                          genero LIKE ? OR 
                          duracao LIKE ?''',
                   ('%' + termo_pesquisa + '%',) * 6)  # Aplica o filtro em todos os campos
        return cursor.fetchall()
    
    def pesquisar_auditoria(self, ação_pesquisa):
        cursor = self.conexao.cursor()
        cursor.execute('''SELECT * FROM auditoria WHERE
                          id LIKE ? OR
                          operacao LIKE ? OR
                          tabela LIKE ? OR
                          dados LIKE ? OR
                          data_hora LIKE ?''',
                   ('%' + ação_pesquisa + '%',) * 5)  # Aplica o filtro em todos os campos
        return cursor.fetchall()
                  
        

    def registrar_auditoria(self, operacao, tabela, dados):
        cursor = self.conexao.cursor()
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO auditoria (operacao, tabela, dados, data_hora) VALUES (?, ?, ?, ?)",
                       (operacao, tabela, dados, data_hora))
        self.conexao.commit()

    def cadastrar_usuario(self, usuario, senha):
        cursor = self.conexao.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
            self.conexao.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def validar_login(self, usuario, senha):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
        return cursor.fetchone() is not None

    def adicionar_filme(self, titulo, diretor, ano, genero, duracao):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO filmes (titulo, diretor, ano, genero, duracao) VALUES (?, ?, ?, ?, ?)", 
                       (titulo, diretor, ano, genero, duracao))
        self.conexao.commit()

        # Registrar auditoria
        dados = f"Título: {titulo}, Diretor: {diretor}, Ano: {ano}, Gênero: {genero}, Duração: {duracao}"
        self.registrar_auditoria("ADICIONADO", "filmes", dados)

    def atualizar_filme(self, id_filme, titulo, diretor, ano, genero, duracao):
        cursor = self.conexao.cursor()
        cursor.execute('''UPDATE filmes
                          SET titulo = ?, diretor = ?, ano = ?, genero = ?, duracao = ?
                          WHERE id = ?''', (titulo, diretor, ano, genero, duracao, id_filme))
        self.conexao.commit()

        # Registrar auditoria
        dados = f"ID: {id_filme}, Novo Título: {titulo}, Novo Diretor: {diretor}, Novo Ano: {ano}, Novo Gênero: {genero}, Nova Duração: {duracao}"
        self.registrar_auditoria("ALTERADO", "filmes", dados)

    def excluir_filme(self, id_filme):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM filmes WHERE id = ?", (id_filme,))
        filme = cursor.fetchone()
        if filme:
            titulo, diretor, ano, genero, duracao = filme[1], filme[2], filme[3], filme[4], filme[5]
            cursor.execute("DELETE FROM filmes WHERE id = ?", (id_filme,))
            self.conexao.commit()

            # Registrar auditoria
            dados = f"ID: {id_filme}, Título: {titulo}, Diretor: {diretor}, Ano: {ano}, Gênero: {genero}, Duração: {duracao}"
            self.registrar_auditoria("EXCLUÍDO", "filmes", dados)

    def excluir_registro_auditoria(self, registro_id):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM auditoria WHERE id = ?", (registro_id,))
        self.conexao.commit()
   
    def restaurar_dados(self, tabela, dados):
        cursor = self.conexao.cursor()
        if tabela == "filmes":
            # Parseia o campo 'dados' recebido do formato "ID: X, Título: Y, Diretor: Z, Ano: W, Gênero: V, Duração: U"
            partes = {p.split(": ")[0]: p.split(": ")[1] for p in dados.split(", ")}
            titulo = partes["Título"]
            diretor = partes["Diretor"]
            ano = int(partes["Ano"])
            genero = partes["Gênero"]
            duracao = int(partes["Duração"])
            
            cursor.execute("INSERT INTO filmes (titulo, diretor, ano, genero, duracao) VALUES (?, ?, ?, ?, ?)",
                           (titulo, diretor, ano, genero, duracao))
            self.conexao.commit()

            # Registrar auditoria da restauração
            self.registrar_auditoria("RESTAURADO", tabela, dados)



    def consultar_filmes(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM filmes")
        return cursor.fetchall()

    def consultar_auditoria(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM auditoria ORDER BY data_hora DESC")
        return cursor.fetchall()