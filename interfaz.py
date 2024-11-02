import tkinter as tk
from tkinter import messagebox
import pygame
from modulo_canciones import canciones
from listas_de_reproduccion import ReproductorDeMusica
from cola_reporduccion import ReproductorDeMusica
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