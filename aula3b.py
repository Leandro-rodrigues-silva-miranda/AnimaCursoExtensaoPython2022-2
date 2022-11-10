#declaração de funções:

preco = 1999.90

#calculo imposto 5%

imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(f"R${imposto:.2f}")

# Função de calcular_imposto

def calcular_imposto(preco):
    imposto = preco*0.05
    return imposto

preco = 300
print(calcular_imposto(preco))

#variavel global e local
print(preco)
preco_produto = 100 #se for retirada essa linha tera erro
print(preco_produto)

#imposto de aliquota variavel:

def calc_imposto(preco,aliquota):
    imposto = float(preco*aliquota/100)
    return imposto

preco = 100
aliquota = 11
print(calc_imposto(preco,aliquota))

