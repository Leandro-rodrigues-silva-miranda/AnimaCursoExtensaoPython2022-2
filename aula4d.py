import aula4c as bd

con, cur = bd.conectar()

nome = input("Nome herói/vilão: ")
nome_civil = input("Nome civil do herói/vilão: ")
tipo_num = int(input("Tecle 1 para Herói(na) 2 para Vilã(o)"))

#Consulta para incremento
sql = "SELECT MAX(pessoa_id) FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]+1

tipo = "Herói(na)" if tipo_num == 1 else "Vilã(o)"

sql = f"INSERT INTO pessoas VALUES ({pessoa_id},'{nome}','{nome_civil}','{tipo}')"
cur.execute(sql)

con.commit()
con.close()




