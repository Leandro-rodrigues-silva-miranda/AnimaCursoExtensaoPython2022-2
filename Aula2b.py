#Nome aluno e nota 0 a 10
nome = str(input("Digite seu nome: "))
nota = float(input("Qual sua nota: "))

if nota == 10:
    print(f"{nome}, cê é o bichão mesmo")
elif nota >= 6 and nota<10:
    print(f"{nome}, eh... dá pro gasto.")
else:
    print("Burro demais, inutil.")