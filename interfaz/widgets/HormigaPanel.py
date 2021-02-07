import tkinter as tk
from tkinter import ttk


class HormigaPanel(tk.Frame):
    def __init__(
        self,
        master=None,
        index=0,
        posicion=None,
        direccion=None,
        categoria=None,
        variante=0,
    ):
        super().__init__(master, borderwidth=1, relief="solid")

        lbl = tk.Label(master=self, text=f"Hormiga {index}")
        lbl.pack(side="top", fill="x")

        grupo = tk.Frame(self)
        grupo.pack(side="top", fill="x")

        tk.Label(master=grupo, text="Posicion: (x,y) ").pack(side="left", fill="x")

        self.x = tk.Entry(master=grupo, width=5)
        self.x.pack(side="left", fill="x", padx=2)

        self.y = tk.Entry(master=grupo, width=5)
        self.y.pack(side="left", fill="x", padx=2)

        grupo = tk.Frame(self)
        grupo.pack(side="top", fill="x")

        tk.Label(master=grupo, text="Orientación:").pack(side="left", fill="x")

        self.menu_orientacion = ttk.Combobox(master=grupo, width=10)
        self.menu_orientacion.pack(side="left", fill="x", padx=2)
        self.menu_orientacion["values"] = [
            "0. Arriba",
            "1. Derecha",
            "2. Abajo",
            "3. Izquierda",
        ]

        if variante != 0:
            grupo = tk.Frame(self)
            grupo.pack(side="top", fill="x")

            tk.Label(master=grupo, text="Categoría:").pack(side="left", fill="x")

            self.menu_cat = ttk.Combobox(master=grupo, width=10)
            self.menu_cat.pack(side="left", fill="x", padx=2)
            self.menu_cat["values"] = [
                "0. Reina",
                "1. Obrera",
                "2. Reproductora",
                "3. Soldado",
            ]
