##Problema:
##Faça um código para ler a senha de um usuário e após 3 tentativas erradas, sair do programa, informando que a senha esta bloqueada

senha="1111"
acesso=input("Digite uma senha")
n=1

while senha!=acesso:
      n=n+1
      print("senha incorreta, digite novamente")
      acesso=input()
      print(n)
      if n>2 and acesso!=senha:
            print("Senha bloqueada")
            break
else:
      print("Acesso liberado")