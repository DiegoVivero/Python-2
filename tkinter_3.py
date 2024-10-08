import tkinter as tk

def mostrar_mensaje():
    print("¡Haz hecho click en el botón!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de botón")

#Crear un botón
boton = tk.Button(ventana, text="Haz Click Aquí", command=mostrar_mensaje)
boton.pack()

# Iniciar el bucle principal
ventana.mainloop()