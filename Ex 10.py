contador=0
cont2=0
for x in range(10):
    numero = int(input("Digite um numero:"))
    if numero >=10 and numero <=20:
        contador=contador+1
    else:
        cont2+=1

print("Existem",contador," numeros no intervalo de 10 e 20 e" ,cont2, "fora do intervalo")