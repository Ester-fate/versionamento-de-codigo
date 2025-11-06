from datetime import datetime, timedelta


PRECO_HORA = 12.00
PRECO_FRACAO_15_MIN = 3.00
PRECO_DIARIA = 60.00
MINUTOS_HORA = 60
MINUTOS_FRACAO = 15

def calcular_valor_estacionamento(entrada_str, saida_str):
    """
    Calcula o valor total do estacionamento com base nas regras fornecidas.
    """
    try:
       
        formato = "%d/%m/%Y %H:%M"
        entrada = datetime.strptime(entrada_str, formato)
        saida = datetime.strptime(saida_str, formato)

        
        if saida < entrada:
            return "Erro: A data/hora de saída deve ser posterior à de entrada.", None, None

        
        diferenca = saida - entrada
        total_minutos = diferenca.total_seconds() / 60

        minutos_cobranca = total_minutos
        if total_minutos % MINUTOS_FRACAO != 0:
            minutos_cobranca = (total_minutos // MINUTOS_FRACAO + 1) * MINUTOS_FRACAO

        total_horas = minutos_cobranca / MINUTOS_HORA
        
        valor_calculado = (total_horas * PRECO_HORA)
        

        if total_horas >= 9 and valor_calculado > PRECO_DIARIA:
            valor_total = PRECO_DIARIA
        else:
            valor_total = valor_calculado

    
        dias = diferenca.days
        valor_total = dias * PRECO_DIARIA


        minutos_restantes = total_minutos % (24 * 60)
        
        if minutos_restantes % MINUTOS_FRACAO != 0:
            minutos_restantes = (minutos_restantes // MINUTOS_FRACAO + 1) * MINUTOS_FRACAO
   
        valor_horas_restantes = (minutos_restantes / MINUTOS_HORA) * PRECO_HORA
        valor_total += valor_horas_restantes

      
        if valor_horas_restantes > PRECO_DIARIA:
            valor_total = (dias + 1) * PRECO_DIARIA


        horas, minutos = divmod(total_minutos, 60)
        dias, horas = divmod(horas, 24)
        tempo_permanencia = f"{int(dias)} dias, {int(horas)} horas e {int(minutos)} minutos"

        return valor_total, tempo_permanencia, saida

    except ValueError:
        return "Erro: Formato de data/hora inválido. Use DD/MM/AAAA HH:MM.", None, None

def emitir_ticket(placa, entrada_str):
    """
    Solicita a hora de saída e emite o ticket completo.
    """
    print(f"\nVeículo de placa {placa} registrou entrada em {entrada_str}.")
    saida_str = input("Digite a data e hora de saída (DD/MM/AAAA HH:MM): ")

    valor, tempo, saida_obj = calcular_valor_estacionamento(entrada_str, saida_str)

    if isinstance(valor, str):
        print(valor)
    else:
        print("\n" + "="*30)
        print("      TICKET DE ESTACIONAMENTO")
        print("="*30)
        print(f"Placa do Veículo: {placa}")
        print(f"Entrada:          {entrada_str}")
        print(f"Saída:            {saida_str}")
        print("-" * 30)
        print(f"Tempo Total:      {tempo}")
        print(f"Valor Total a Pagar: R$ {valor:.2f}")
        print("="*30)

placa_veiculo = input("Digite a placa do carro (ex: ABC1234): ")
entrada_veiculo_str = input("Digite a data e hora de entrada (DD/MM/AAAA HH:MM): ")

emitir_ticket(placa_veiculo, entrada_veiculo_str)