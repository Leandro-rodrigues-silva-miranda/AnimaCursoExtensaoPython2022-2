#while
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

#for
fruta = "morango"
print(fruta)

frutas = ["morango","laranja","tomate"]

print(frutas)

print(frutas[2])

print(len(frutas))

#adição

frutas.append("manga")

print(frutas)
print(len(frutas))

#while
print("Frutas com while: ")
i=0
while(i<len(frutas)):
    print(frutas[i])
    i+=1;

print("Frutas com for: ")
for x in frutas:
    print(x)