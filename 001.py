ano_nasc = int(input("Digite o ano do seu nascimento:"))
ano_atual = int(input("Digite o ano em que estamos:"))
soma = ano_nasc - ano_atual
print ("Você tem:", soma)
idade = 18
if(soma < idade):
    print ("Você ainda fará 18 anos.")
else:
    if (soma >= idade):
        print ("Você já fez 18 anos!")