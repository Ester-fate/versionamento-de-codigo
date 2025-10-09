ano_nasc = int(input("digite o ano do seu nascimento:"))
ano_atual = int(input("digite o ano em que estamos:"))
soma = ano_nasc - ano_atual
print ("voce tem:",soma)
idade=18
if(soma < idade):
     print("voce ainda fará 18 anos.")
else:
     if(soma >= idade):
          print("voce já fez 18 anos!")
