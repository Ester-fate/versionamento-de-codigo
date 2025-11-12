print("Lista com nomes das cidades!")
lista_cidades = []
print("Digite os nomes de cidades que você dseja colocar a lista.")
print("Para terminar, digite 'sair' ou pressione ENTER para finalizar.")
while True:
  cidade = input("Digite o nome de uma cidade:")
  if cidade == 'sair' or cidade == "":
    break
  lista_cidades.append(cidade)
  print(lista_cidades)
  print("\nLista de cidades adicionadas:")
  for cidade in lista_cidades:
    print(cidade)