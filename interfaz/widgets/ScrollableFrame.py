"""
    Code from https://blog.tecladocode.com/tkinter-scrollable-frames/
"""

import tkinter as tk
from tkinter import ttk


class ScrollableFrame(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        width = None
        if "width" in kwargs:
            width = kwargs.get("width")

        canvas = tk.Canvas(self, width=width, height=1000)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.content = ttk.Frame(canvas, width=width)

        self.content.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all"),
            ),
        )

        canvas.create_window((0, 0), window=self.content, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
