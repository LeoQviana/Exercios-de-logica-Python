numero=int(input("Digite o numero de Alunos"))
soma=0
for x in range(numero):
    nota=float(input("Digite a nota"))
    soma+=nota
media=soma/numero

print(media)
