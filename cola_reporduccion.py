class ListaDeReproduccion:
    def __init__(self):
        self.cola = []

    def agregar_cancion_a_cola(self, cancion):
        """Agrega una canción al final de la cola de reproducción."""
        self.cola.append(cancion)
        print(f"La canción '{cancion}' ha sido agregada a la cola de reproducción.")

    def mostrar_cola(self):
        """Muestra la cola de reproducción."""
        if not self.cola:
            print("La cola de reproducción está vacía.")
        else:
            print("Cola de reproducción actual:")
            for indice, cancion in enumerate(self.cola, start=1):
                print(f"{indice}. {cancion}")