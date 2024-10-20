import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.resultado = tk.StringVar()
        self.resultado.set("0")

        self.entrada = tk.Entry(master, textvariable=self.resultado, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entrada.grid(row=0, column=0, columnspan=4)

        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]

        for (text, row, column) in botones:
            self.crear_boton(text, row, column)

        boton_clear = tk.Button(master, text='C', padx=20, pady=20, command=self.limpiar)
        boton_clear.grid(row=5, column=0, columnspan=4)

    def crear_boton(self, texto, fila, columna):
        boton = tk.Button(self.master, text=texto, padx=20, pady=20, command=lambda: self.click_boton(texto))
        boton.grid(row=fila, column=columna)

    def click_boton(self, texto):
        if texto == '=':
            try:
                self.resultado.set(eval(self.resultado.get()))
            except Exception as e:
                self.resultado.set("Error")
        else:
            if self.resultado.get() == "0" or self.resultado.get() == "Error":
                self.resultado.set(texto)
            else:
                self.resultado.set(self.resultado.get() + texto)

    def limpiar(self):
        self.resultado.set("0")

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()
