import tkinter as tk
from tkinter import messagebox
import random

class ListaDeReproduccion:
    def __init__(self):
        self.listas_de_reproduccion = {}
        self.cola = []

    def crear_lista_de_reproduccion(self, nombre_lista, canciones):
        if nombre_lista not in self.listas_de_reproduccion:
            self.listas_de_reproduccion[nombre_lista] = canciones
            return f"Lista '{nombre_lista}' creada con {len(canciones)} canciones."
        else:
            return f"Ya existe una lista con el nombre '{nombre_lista}'."

    def agregar_lista_a_cola(self, nombre_lista):
        lista = self.listas_de_reproduccion.get(nombre_lista)
        if lista:
            self.cola.append((nombre_lista, lista))
            return f"La lista '{nombre_lista}' ha sido agregada a la cola."
        else:
            return f"No se encontró la lista '{nombre_lista}'."

    def mostrar_cola(self):
        if not self.cola:
            return "La cola está vacía."
        else:
            return [f"Lista '{nombre_lista}' con canciones: {list(canciones.values())}" 
                    for nombre_lista, canciones in self.cola]

    def modo_aleatorio(self):
        if not self.cola:
            return "No hay listas en la cola."
        lista_aleatoria = random.choice(self.cola)
        nombre_lista, canciones = lista_aleatoria
        numero_aleatorio = random.choice(list(canciones.keys()))
        cancion_aleatoria = canciones[numero_aleatorio]
        return f"Reproduciendo en modo aleatorio: '{cancion_aleatoria}' de la lista '{nombre_lista}'"

class App:
    def __init__(self, master):
        self.master = master
        self.reproductor = ListaDeReproduccion()

        self.master.title("Reproductor de Música")

        self.label = tk.Label(master, text="Reproductor de Música")
        self.label.pack()

        self.nombre_lista_entry = tk.Entry(master)
        self.nombre_lista_entry.pack()
        self.nombre_lista_entry.insert(0, "Nombre de la lista")

        self.canciones_entry = tk.Entry(master)
        self.canciones_entry.pack()
        self.canciones_entry.insert(0, "Canciones (números separados por coma)")

        self.crear_lista_button = tk.Button(master, text="Crear Lista", command=self.crear_lista)
        self.crear_lista_button.pack()

        self.agregar_lista_button = tk.Button(master, text="Agregar a Cola", command=self.agregar_a_cola)
        self.agregar_lista_button.pack()

        self.mostrar_cola_button = tk.Button(master, text="Mostrar Cola", command=self.mostrar_cola)
        self.mostrar_cola_button.pack()

        self.modo_aleatorio_button = tk.Button(master, text="Reproducir Aleatorio", command=self.reproducir_aleatorio)
        self.modo_aleatorio_button.pack()

        self.resultado_label = tk.Label(master, text="")
        self.resultado_label.pack()

    def crear_lista(self):
        nombre_lista = self.nombre_lista_entry.get()
        canciones_str = self.canciones_entry.get()
        canciones = {i + 1: nombre for i, nombre in enumerate(canciones_str.split(','))}
        resultado = self.reproductor.crear_lista_de_reproduccion(nombre_lista, canciones)
        self.resultado_label.config(text=resultado)

    def agregar_a_cola(self):
        nombre_lista = self.nombre_lista_entry.get()
        resultado = self.reproductor.agregar_lista_a_cola(nombre_lista)
        self.resultado_label.config(text=resultado)

    def mostrar_cola(self):
        cola = self.reproductor.mostrar_cola()
        if isinstance(cola, list):
            self.resultado_label.config(text="\n".join(cola))
        else:
            self.resultado_label.config(text=cola)

    def reproducir_aleatorio(self):
        resultado = self.reproductor.modo_aleatorio()
        self.resultado_label.config(text=resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
