contador=0

for x in range(10):
    numero = int(input("Digite um numero:"))
    if numero < 0:
        contador=contador+1
print(contador)