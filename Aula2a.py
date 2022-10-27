#Comando input
nome = input("Digite seu nome: ")
print(f"Seu nome é: {nome}")

#Conversão para inteiro
idade = int(input(f"Qual sua idade {nome}?"))
print(f"Sua idade é {idade}")
print(f"O dobre da sua idade é {idade}")

#Se, senão
if idade >= 18:
    print("Pode beber ou dirigir")
else:
    print("Não pode beber e nem dirigir")

sexo = input("Qual seu genero? (f/m) ").lower()
#Condição composta
if idade>=18 and sexo=='m':
    print("E você precisou alistar-se.")

