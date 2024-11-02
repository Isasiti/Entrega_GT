import tkinter as tk
from tkinter import messagebox
import pygame
from modulo_canciones import canciones
from listas_de_reproduccion import ReproductorDeMusica
class ReproductorDeMusica:
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
