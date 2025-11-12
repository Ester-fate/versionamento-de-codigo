import tkinter as tk
from tkinter import messagebox


estoque = {
    "arroz": 5000,
    "feijao": 3000,
    "carne": 2000,
    "salada": 1000
}

consumo = {
    "arroz": 100,
    "feijao": 50,
    "carne": 25,
    "salada": 10
}

def mostrar_estoque():
    texto = "=== ESTOQUE ATUAL ===\n"
    for item, qtd in estoque.items():
        texto += f"{item.capitalize()}: {qtd}g\n"
    return texto

def marmitas_possiveis():
    quantidades = {item: estoque[item] // consumo[item] for item in estoque}
    total = min(quantidades.values())
    texto = "=== MARMITAS POSSÍVEIS ===\n"
    for item, qtd in quantidades.items():
        texto += f"Com {item}: {qtd} marmitas\n"
    texto += f"\nTotal possível: {total} marmitas"
    return texto

def vender_marmita(qtd):
    global estoque
    possivel = min(estoque[item] // consumo[item] for item in estoque)
    if qtd > possivel:
        messagebox.showwarning("Aviso", f"Não há insumos suficientes para {qtd} marmitas!")
        return

    for item in estoque:
        estoque[item] -= consumo[item] * qtd
    messagebox.showinfo("Sucesso", f"{qtd} marmita(s) vendida(s) com sucesso!")


janela = tk.Tk()
janela.title("Sistema de Marmitex")
janela.geometry("400x400")


texto_saida = tk.Text(janela, height=15, width=45)
texto_saida.pack(pady=10)


def mostrar_estoque_ui():
    texto_saida.delete(1.0, tk.END)
    texto_saida.insert(tk.END, mostrar_estoque())

def marmitas_possiveis_ui():
    texto_saida.delete(1.0, tk.END)
    texto_saida.insert(tk.END, marmitas_possiveis())

def vender_ui():
    try:
        qtd = int(entrada_qtd.get())
        vender_marmita(qtd)
        mostrar_estoque_ui()
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido!")


frame = tk.Frame(janela)
frame.pack(pady=5)

tk.Label(frame, text="Digite quantidade de marmitas vendidas:").grid(row=0, column=0, padx=5)
entrada_qtd = tk.Entry(frame, width=10)
entrada_qtd.grid(row=0, column=1, padx=5)

tk.Button(janela, text="Mostrar estoque", width=20, command=mostrar_estoque_ui).pack(pady=3)
tk.Button(janela, text="Ver marmitas possíveis", width=20, command=marmitas_possiveis_ui).pack(pady=3)
tk.Button(janela, text="Registrar venda", width=20, command=vender_ui).pack(pady=3)


mostrar_estoque_ui()

janela.mainloop()