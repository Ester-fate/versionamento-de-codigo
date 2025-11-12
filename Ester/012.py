
estoque = {
    "arroz": 5000,    # 5 kg
    "feijao": 3000,   # 3 kg
    "carne": 2000,    # 2 kg
    "salada": 1000    # 1 kg
}

consumo = {
    "arroz": 100,
    "feijao": 50,
    "carne": 25,
    "salada": 10
}

def mostrar_estoque():
    print("\n=== ESTOQUE ATUAL ===")
    for item, qtd in estoque.items():
        print(f"{item.capitalize()}: {qtd}g")
    print("======================")

def marmitas_possiveis():
    
    quantidades = {item: estoque[item] // consumo[item] for item in estoque}
    
    total = min(quantidades.values())
    print("\n=== MARMITAS POSSÍVEIS ===")
    for item, qtd in quantidades.items():
        print(f"Com {item}: {qtd} marmitas")
    print(f"\n Total possível: {total} marmitas")
    print("===========================")

def vender_marmita(qtd):
    global estoque
    
    possivel = min(estoque[item] // consumo[item] for item in estoque)
    if qtd > possivel:
        print(f"\n Não há insumos suficientes para {qtd} marmitas!")
        marmitas_possiveis()
        return
    
    for item in estoque:
        estoque[item] -= consumo[item] * qtd
    print(f"\n {qtd} marmita(s) feita(s) com sucesso!")

while True:
    print("\n=== SISTEMA DE MARMITEX ===")
    print("1 - Mostrar estoque")
    print("2 - Ver marmitas possíveis")
    print("3 - Registrar venda")
    print("0 - Sair")
    print("===========================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_estoque()
    elif opcao == "2":
        marmitas_possiveis()
    elif opcao == "3":
        qtd = int(input("Quantas marmitas foram vendidas? "))
        vender_marmita(qtd)
    elif opcao == "0":
        print("Encerrando o sistema... ")
        break
    else:
        print("Opção inválida, tente novamente.")