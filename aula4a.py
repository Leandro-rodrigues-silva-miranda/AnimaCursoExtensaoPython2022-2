#Acesso a banco de dados 16/11/2022
import sqlite3

conexao = sqlite3.connect("dc_universe.db")
cur = conexao.cursor()
sql = "SELECT nome,tipo FROM pessoas"
cur.execute(sql)
pessoas = cur.fetchall()
for i in pessoas:
    print(i[0],end=" é ")
    print(i[1])

