print("lista com nomes das cidades !")
lista_cidades =[]
print("digite os nomes de cidades que voce deseja colocar a lista.")
print("para terminar, digite 'sair' ou precione ENTER para finalizar.")
while true:
    cidade = input("digita o nome de uma cidade :")
    if cidade == 'sair' or cidade =="":
        break 
    lista_cidades.append(cidade)
    print(lista_cidades)
    print("\nlista de cidades adicionadas:")
    for cidade in lista_cidades:
        print(cidade)