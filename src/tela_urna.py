import os
import tkinter as tk
from tkinter import ttk, messagebox
from common import Eleitores, Candidatos, Urna
import pygame

u = None
e = None
c = None
votou = False

som_path = os.path.abspath("src/som.mp3")

def on_button_click(p):
    current_text = label_var.get().replace("_", "")
    if current_text == "FIM" or votou:
        return
    if len(current_text) < 2:
        new_text = current_text + str(p)
        label_var.set(new_text.ljust(2, "_"))
        update_candidate_name(new_text)

def remove_last_value():
    current_text = label_var.get().replace("_", "")
    if current_text == "FIM" or votou:
        return
    if len(current_text) > 0:
        new_text = current_text[:-1]
        label_var.set(new_text.ljust(2, "_"))
        update_candidate_name(new_text)

def confirma():
    global u, e, c, votou
    current_text = label_var.get().replace("_", "")
    if len(current_text) == 2:
        if votou:
            messagebox.showinfo("Aviso", "Você já votou!")
            return
        confirma_str = current_text
        label_var.set("FIM")
        candidate_name_var.set("")
        u.votar(e, c, confirma_str)
        votou = True
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(som_path)
            pygame.mixer.music.play()
        except Exception as ex:
            messagebox.showerror("Erro", f"Erro ao reproduzir o áudio: {ex}")
    else:
        if not votou:
            messagebox.showwarning("Erro", "Por favor, insira exatamente dois valores.")

def update_candidate_name(vote_number):
    candidate_name_var.set("")
    if len(vote_number) == 2:
        for candidate in c:
            if str(candidate.numero) == vote_number:
                candidate_name_var.set(f"{candidate.nome}")
                return
        candidate_name_var.set("Nulo")

def cria_interface(urna, eleitores, candidatos):
    global u, e, c, candidate_name_var, label_var, votou
    u = urna
    e = eleitores
    c = candidatos

    root = tk.Tk()
    root.title("Urna Eletrônica")
    root.geometry("500x300")

    container = ttk.Frame(root)
    container.pack(padx=10, pady=10, fill="both", expand=True)

    label_var = tk.StringVar(value="__")
    label = ttk.Label(
        container,
        textvariable=label_var,
        font=("Courier", 24),
        anchor="center",
        width=10,
        relief="solid",
        padding=(10, 5),
    )
    label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    candidate_name_var = tk.StringVar(value="")
    candidate_label = ttk.Label(
        container,
        textvariable=candidate_name_var,
        font=("Arial", 14),
        anchor="center",
    )
    candidate_label.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

    teclado_frame = ttk.Frame(container)
    teclado_frame.grid(row=0, column=1, padx=10, pady=10)

    for i in range(1, 10):
        btn = ttk.Button(teclado_frame, text=str(i), command=lambda p=i: on_button_click(p), width=5)
        row, col = divmod(i - 1, 3)
        btn.grid(row=row, column=col, padx=5, pady=5)

    btn_0 = ttk.Button(teclado_frame, text="0", command=lambda: on_button_click(0), width=5)
    btn_0.grid(row=3, column=1, padx=5, pady=5)

    botoes_frame = ttk.Frame(container)
    botoes_frame.grid(row=1, column=1, padx=10, pady=10)

    corrigir_btn = ttk.Button(botoes_frame, text="Corrigir", command=remove_last_value, width=12)
    corrigir_btn.grid(row=0, column=0, padx=10, pady=5)

    confirmar_btn = ttk.Button(botoes_frame, text="Confirmar", command=confirma, width=12)
    confirmar_btn.grid(row=0, column=1, padx=10, pady=5)

    root.mainloop()
