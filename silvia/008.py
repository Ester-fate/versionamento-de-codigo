frutas = []
fruta_laranja = input("digite o nome da primeira fruta (laranja):")
frutas . append (fruta_laranja)
fruta_limão = input("digite o nome da sengunda fruta (limão):")
frutas.append(fruta_limão)
fruta_banana = input("digite o nome da terceira fruta (banana):")
frutas.append(fruta_banana)
fruta_pera = input("digite o nome da quarta fruta(pera): ") 
frutas . append(fruta_pera) 
fruta_uva = input("digite o nome da quinta fruta (uva ):") 
frutas . append(fruta_uva)  
print("\nlista de frutas em ordem :")
for i , fruta in enumerate (frutas, start=1):
   print(f"{1}  {fruta}")