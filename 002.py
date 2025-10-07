idade_atual = int(input("Digite a sua idade:"))
if 0 <= idade_atual <= 11:
  print("Você é criança.")
else:
  if 12 <= idade_atual <= 18:
    print("Você é adoescente.")
  else:
    if 19 <= idade_atual <= 24:
      print("Você é Jovem.")
    else:
      if 25 <= idade_atual <= 40:
        print("Você é Adulto.")
      else:
        if 41 <= idade_atual <= 60:
          print("Você está na Meia Idade.")
        else:
          if 60 <= idade_atual:
            print("Você é Idoso.")
    