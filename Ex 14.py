alunos=int(input("Digite a quantidade de alunos"))
n=1
soma=0
while n<= alunos:
      nota=float(input("Digite a nota"))
      soma = soma + nota
      n += 1

print("Sua média foi:", soma / alunos)
