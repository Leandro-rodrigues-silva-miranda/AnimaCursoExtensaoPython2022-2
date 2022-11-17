import sqlite3

conexao = sqlite3.connect("dc_universe.db")
cur = conexao.cursor()
sql = "INSERT INTO pessoas values (12, 'Flash', 'Barry Allen', 'Herói(na)')"
cur.execute(sql)
conexao.commit()
conexao.close()


