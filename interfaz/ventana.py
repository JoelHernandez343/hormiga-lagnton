import tkinter as tk
from tkinter import ttk

from .widgets.ScrollableFrame import ScrollableFrame
from .widgets.HormigaPanel import HormigaPanel


class Ventana:
    def __init__(self, titulo, tam):
        self.root = tk.Tk()
        self.root.title(titulo)
        self.root.geometry(tam)

        # crear el layout
        visor = tk.Frame(master=self.root, width=400, height=1000, bg="gray")
        visor.pack(fill="both", side="left", expand=True)

        controles = tk.Frame(master=self.root, width=300, height=1000, bg="gray")
        controles.pack(fill="both", side="left", expand=False)

        self.hacer_controles(controles)

    def hacer_controles(self, controles):

        contenedor = tk.Frame(master=controles, width=300, height=1000)
        contenedor.pack(fill="both", side="left", expand=False, padx=20, pady=20)

        """ Menú para variante """
        lbl = tk.Label(master=contenedor, text="Elegir variante:")
        lbl.pack(side="top", anchor="nw")

        self.cmb_variante = ttk.Combobox(master=contenedor)
        self.cmb_variante.pack(side="top", fill="x")
        self.cmb_variante["values"] = ["Clásica", "4 hormigas"]

        """ Cargar / guardar configuración """
        lbl = tk.Label(master=contenedor, text="Cargar configuración:")
        lbl.pack(side="top", anchor="nw")

        grupo = tk.Frame(master=contenedor)
        grupo.pack(fill="x")

        self.btn_cargar_hormigas = tk.Button(master=grupo, text="Hormigas")
        self.btn_cargar_hormigas.pack(fill="x", side="left", expand=True)

        self.btn_cargar_matriz = tk.Button(master=grupo, text="Matriz")
        self.btn_cargar_matriz.pack(fill="x", side="left", expand=True)

        lbl = tk.Label(master=contenedor, text="Guardar configuración:")
        lbl.pack(side="top", anchor="nw")

        grupo = tk.Frame(master=contenedor)
        grupo.pack(fill="x")

        self.btn_guardar_hormigas = tk.Button(master=grupo, text="Hormigas")
        self.btn_guardar_hormigas.pack(fill="x", side="left", expand=True)

        self.btn_guardar_matriz = tk.Button(master=grupo, text="Matriz")
        self.btn_guardar_matriz.pack(fill="x", side="left", expand=True)

        """ Configuración individual """
        lbl = tk.Label(master=contenedor, text="Configuración:")
        lbl.pack(side="top", anchor="nw")

        grupo2 = tk.Frame(master=contenedor, width=250)
        grupo2.pack(fill="x")

        lbl = tk.Label(master=grupo2, text="#:", width=3)
        lbl.pack(fill="x", side="left", expand=True)

        self.ent_n_hormigas = tk.Entry(master=grupo2, width=15)
        self.ent_n_hormigas.pack(side="left", expand=True)

        self.btn_est_hormigas = tk.Button(master=grupo2, text="Establecer")
        self.btn_est_hormigas.pack(fill="x", side="left", expand=True)

        grupo = ScrollableFrame(
            master=contenedor, borderwidth=1, relief="solid", width=250
        )
        grupo.pack(fill="both")

        self.fr_lista_hormigas = tk.Frame(master=grupo.content)
        self.fr_lista_hormigas.pack(fill="x")

        for i in range(200):
            h = HormigaPanel(master=self.fr_lista_hormigas, index=i, variante=1)
            h.pack(fill="x", padx=(10, 30))

    def ejecutar(self):
        self.root.mainloop()