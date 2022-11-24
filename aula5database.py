import sqlite3

class Database:
    conexao = None
    cursor = None

    def __init__(self):
        #global conexao, cursor
        self.conexao = sqlite3.connect("imdb.db")
        self.cursor = self.conexao.cursor()

    def __del__(self):
        self.conexao.commit()