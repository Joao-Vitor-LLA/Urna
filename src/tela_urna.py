from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from common import *

def tela(eleitores, candidatos):  # Recebe os dois parâmetros necessários
    u = Urna(eleitores, candidatos)  # Cria a instância da urna
    e = eleitores
    c = candidatos
    root = Tk()
    teclado = ttk.Frame(root, padding=10)
    tela = ttk.Frame(root, padding=100)
    root.title("Urna")
    teclado.grid(column=1, row=0)
    tela.grid(column=0, row=0)

    n = 9

    # Variáveis para armazenar os dados
    confirma_str = ""  # Armazena a string formada pelos 2 valores confirmados
    branco_str = ""  # Armazena a string "branco" quando o botão "Branco" for clicado


    # Função para atualizar o label com o valor clicado
    def on_button_click(p):
        current_text = label_var.get()

        # Se o texto atual estiver vazio, apenas coloca o valor
        if current_text == "":
            label_var.set(f"{p}")
        else:
            # Caso contrário, concatena o novo valor com um espaço
            # Limita para no máximo 2 valores
            values = current_text.split()
            if len(values) < 2:
                label_var.set(f"{current_text} {p}")
            else:
                label_var.set(f"{values[0]} {values[1]}")  # Mantém apenas 2 valores


    # Função para remover o último valor
    def remove_last_value():
        current_text = label_var.get()
        values = current_text.split()

        if len(values) > 0:
            # Remove o último valor
            values.pop()
            # Atualiza o texto no label
            if len(values) > 0:
                label_var.set(f"{values[0]}")
            else:
                label_var.set("")  # Se não houver mais valores, o label ficará vazio


    # Função para confirmar a entrada e armazenar os dois valores
    def confirma():

        global confirma_str
        current_text = label_var.get()
        values = current_text.split()

        if len(values) == 2:  # Só confirma se houver exatamente 2 valores
            confirma_str = f"{values[0]}{values[1]}"  # Armazena os dois valores concatenados
            label_var.set("")  # Limpa o label para o próximo uso
            u.votar(e, c, confirma_str)  # Chama a função votar com os parâmetros corretos
        else:
            messagebox.showwarning("Erro", "Por favor, insira exatamente dois valores.")


    # Função para definir o valor "branco"
    def branco():
        global branco_str
        branco_str = "branco"
        print(f"Valor branco armazenado: {branco_str}")  # Apenas para depuração
        label_var.set("")  # Limpa o label para o próximo uso


    # Botões de números (1 a 9)
    for i in range(3):
        for j in range(3):
            button = ttk.Button(teclado, text=n, command=lambda n=n: on_button_click(n))
            button.grid(column=j, row=i)
            n -= 1

    # Botões extras
    button = ttk.Button(teclado, text=0, command=lambda: on_button_click(0)).grid(column=1, row=4)
    button = ttk.Button(teclado, text="Branco", command=branco).grid(column=0, row=4)
    button = ttk.Button(teclado, text="Confirma", command=confirma).grid(column=2, row=4)

    # Botão "Remover" à direita
    button_remove = ttk.Button(root, text="Remover", command=remove_last_value)
    button_remove.grid(row=1, column=1, padx=10, pady=10)

    # Definir a variável vinculada ao label
    label_var = StringVar()
    label = ttk.Label(root, textvariable=label_var, font=("Arial", 14))
    label.grid(row=1, column=0, padx=10, pady=10)

    root.mainloop()
