import tkinter as tk
from tkinter import messagebox
import pygame
from modulo_canciones import canciones 
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
    def mostrar_canciones_de_lista(self, nombre_lista):
        """
        Retorna las canciones de la lista de reproducción especificada.
        """
        if nombre_lista in self.listas_de_reproduccion:
            canciones = self.listas_de_reproduccion[nombre_lista]
            return f"Canciones en la lista '{nombre_lista}':\n" + "\n".join(f"{idx + 1}. {cancion}" for idx, cancion in enumerate(canciones))
        else:
            return f"La lista '{nombre_lista}' no existe."
    def mostrar_canciones_de_lista(self):
        """
        Obtiene el nombre de la lista desde la entrada y muestra sus canciones en el área de texto.
        """
        nombre_lista = self.nombre_lista_entry.get()
        if nombre_lista:
            resultado = self.reproductor.mostrar_canciones_de_lista(nombre_lista)
            self.resultado_text.delete("1.0", tk.END)  # Limpiar el área de texto
            self.resultado_text.insert(tk.END, resultado + "\n")
        else:
            messagebox.showerror("Error", "Por favor, ingresa el nombre de la lista de reproducción.")