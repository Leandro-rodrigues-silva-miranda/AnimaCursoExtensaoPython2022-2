import sqlite3
#Função conectar
def conectar():
    conexao = sqlite3.connect("dc_universe.db")
    cur = conexao.cursor()
    return conexao,cur
