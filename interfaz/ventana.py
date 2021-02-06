import tkinter as tk
from tkinter import ttk


class Ventana:
    def __init__(self, titulo, tam):
        self.root = tk.Tk()
        self.root.title(titulo)
        self.root.geometry(tam)

        # crear el layout
        visor = tk.Frame(master=self.root, width=400, height=1000, bg="gray")
        visor.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        controles = tk.Frame(master=self.root, width=300, height=1000, bg="gray")
        controles.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

        self.hacer_controles(controles)

    def hacer_controles(self, controles):

        contenedor = tk.Frame(master=controles, width=300, height=1000, bg="blue")
        contenedor.pack(fill=tk.BOTH, side=tk.LEFT, expand=False, padx=20, pady=20)
        contenedor.pack_propagate(0)

        lbl = tk.Label(master=contenedor, text="Elegir variante")
        lbl.pack(side=tk.TOP, anchor=tk.NW)

        self.cmb_variante = ttk.Combobox(master=contenedor)
        self.cmb_variante.pack(side=tk.TOP, anchor=tk.NW)
        self.cmb_variante["values"] = ["Clásica", "4 hormigas"]

    def ejecutar(self):
        self.root.mainloop()