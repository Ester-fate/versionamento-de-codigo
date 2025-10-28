frutas = []
fruta_laranja = input("Digite o nome da primeira fruta (laranaja):")
frutas.append(fruta_laranja)
fruta_limao = input("Digite o nome da segunda fruta (limão):")
frutas.append(fruta_limao)
fruta_banana = input("Digite o nome da terceira fruta (banana):")
frutas.append(fruta_banana)
fruta_pera = input("Digite o nome da quarta fruta (pera):")
frutas.append(fruta_pera)
fruta_uva = input("Digite o nome da quinta fruta (uva):")
frutas.append(fruta_uva)
print("\nLista de frutas em ordem: ")
for i, fruta in enumerate(frutas, start=1):
    print(f"{i}º {fruta}")