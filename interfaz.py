import tkinter as tk
from tkinter import messagebox
import pygame
from modulo_canciones import canciones  # Importamos el diccionario de canciones


class ReproductorDeMusica:
    def __init__(self):
        pygame.mixer.init()
        self.listas_de_reproduccion = {}  # Diccionario para listas de reproducción
        self.cola = []  # Cola de reproducción
        self.indice_actual = 0  # Índice de la canción actual en la cola

    def crear_lista_de_reproduccion(self, nombre_lista, lista_de_canciones):
        """Crea una nueva lista de reproducción con el nombre y canciones proporcionadas."""
        if nombre_lista in self.listas_de_reproduccion:
            return f"La lista '{nombre_lista}' ya existe."
        self.listas_de_reproduccion[nombre_lista] = lista_de_canciones
        return f"Lista '{nombre_lista}' creada con {len(lista_de_canciones)} canciones."

    def mostrar_listas_de_reproduccion(self):
        """Devuelve un texto con todas las listas de reproducción y sus canciones."""
        if not self.listas_de_reproduccion:
            return "No hay listas de reproducción disponibles."
        resultado = ""
        for nombre, canciones_ids in self.listas_de_reproduccion.items():
            canciones_lista = [canciones[c] for c in canciones_ids if c in canciones]
            resultado += f"Lista '{nombre}': {', '.join(canciones_lista)}\n"
        return resultado

    def agregar_cancion_a_lista(self, nombre_lista, cancion_id):
        """Agrega una canción a una lista de reproducción existente."""
        if nombre_lista in self.listas_de_reproduccion:
            self.listas_de_reproduccion[nombre_lista].append(cancion_id)
            return f"Canción con ID {cancion_id} agregada a la lista '{nombre_lista}'."
        return f"La lista '{nombre_lista}' no existe."

    def eliminar_cancion_de_lista(self, nombre_lista, cancion_id):
        """Elimina una canción de una lista de reproducción."""
        if nombre_lista in self.listas_de_reproduccion:
            try:
                self.listas_de_reproduccion[nombre_lista].remove(cancion_id)
                return f"Canción con ID {cancion_id} eliminada de la lista '{nombre_lista}'."
            except ValueError:
                return f"La canción con ID {cancion_id} no está en la lista '{nombre_lista}'."
        return f"La lista '{nombre_lista}' no existe."

    def agregar_lista_a_cola(self, nombre_lista):
        """Agrega todas las canciones de una lista de reproducción a la cola."""
        if nombre_lista in self.listas_de_reproduccion:
            self.cola.extend(self.listas_de_reproduccion[nombre_lista])
            return f"Lista '{nombre_lista}' agregada a la cola de reproducción."
        return f"La lista '{nombre_lista}' no existe."

    def mostrar_cola(self):
        """Muestra la cola de reproducción actual."""
        if not self.cola:
            return "La cola de reproducción está vacía."
        return ", ".join([canciones[c] for c in self.cola if c in canciones])

    def reproducir_siguiente(self):
        """Reproduce la siguiente canción en la cola."""
        if self.indice_actual < len(self.cola):
            cancion_id = self.cola[self.indice_actual]
            ruta_cancion = canciones.get(cancion_id)

            if ruta_cancion:
                pygame.mixer.music.load(ruta_cancion)
                pygame.mixer.music.play()
                print(f"Reproduciendo: {ruta_cancion}")
                self.indice_actual += 1
            else:
                print("No se encontró la canción en el módulo de canciones.")
        else:
            print("La cola de reproducción ha terminado.")
            self.detener_cancion()

    def pausar_cancion(self):
        """Pausa la canción actual."""
        pygame.mixer.music.pause()

    def reanudar_cancion(self):
        """Reanuda la canción pausada."""
        pygame.mixer.music.unpause()

    def detener_cancion(self):
        """Detiene la reproducción de la canción."""
        pygame.mixer.music.stop()
        self.indice_actual = 0  # Reinicia el índice de la cola


class App:
    def __init__(self, master):
        self.master = master
        self.reproductor = ReproductorDeMusica()

        self.master.title("Reproductor de Música")

        # Crear widgets de la interfaz
        self.nombre_lista_entry = tk.Entry(master)
        self.nombre_lista_entry.pack()

        self.crear_lista_button = tk.Button(master, text="Crear Lista", command=self.crear_lista)
        self.crear_lista_button.pack()

        self.mostrar_listas_button = tk.Button(master, text="Mostrar Listas", command=self.mostrar_listas)
        self.mostrar_listas_button.pack()

        self.mostrar_cola_button = tk.Button(master, text="Mostrar Cola", command=self.mostrar_cola)
        self.mostrar_cola_button.pack()

        self.agregar_cola_button = tk.Button(master, text="Agregar Lista a Cola", command=self.agregar_a_cola)
        self.agregar_cola_button.pack()

        self.reproducir_button = tk.Button(master, text="Reproducir Siguiente", command=self.reproductor.reproducir_siguiente)
        self.reproducir_button.pack()

        self.pausar_button = tk.Button(master, text="Pausar", command=self.reproductor.pausar_cancion)
        self.pausar_button.pack()

        self.reanudar_button = tk.Button(master, text="Reanudar", command=self.reproductor.reanudar_cancion)
        self.reanudar_button.pack()

        self.detener_button = tk.Button(master, text="Detener", command=self.reproductor.detener_cancion)
        self.detener_button.pack()

        self.resultado_text = tk.Text(master, height=15, width=50)
        self.resultado_text.pack()

    def crear_lista(self):
        nombre_lista = self.nombre_lista_entry.get()
        lista_de_canciones = [1, 2, 3]  # Cambia esta lista con IDs válidos de canciones
        resultado = self.reproductor.crear_lista_de_reproduccion(nombre_lista, lista_de_canciones)
        self.resultado_text.insert(tk.END, resultado + '\n')

    def mostrar_listas(self):
        resultado = self.reproductor.mostrar_listas_de_reproduccion()
        self.resultado_text.insert(tk.END, resultado + '\n')

    def mostrar_cola(self):
        resultado = self.reproductor.mostrar_cola()
        self.resultado_text.insert(tk.END, resultado + '\n')

    def agregar_a_cola(self):
        nombre_lista = self.nombre_lista_entry.get()
        resultado = self.reproductor.agregar_lista_a_cola(nombre_lista)
        self.resultado_text.insert(tk.END, resultado + '\n')