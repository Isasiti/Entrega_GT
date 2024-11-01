import random
class ListaDeReproduccion:
    def __init__(self):
        # Diccionario que almacenará todas las listas de reproducción con sus nombres y canciones
        self.listas_de_reproduccion = {}
        self.cola = []  # Cola de reproducción para almacenar listas de reproducción completas

    def crear_lista_de_reproduccion(self, nombre_lista, canciones):
        """
        Crea una nueva lista de reproducción con un nombre y un diccionario de canciones.
        `canciones` debe ser un diccionario donde la clave es un número y el valor es el nombre de la canción.
        """
        if nombre_lista not in self.listas_de_reproduccion:
            self.listas_de_reproduccion[nombre_lista] = canciones
            print(f"Lista de reproducción '{nombre_lista}' creada con {len(canciones)} canciones.")
        else:
            print(f"Ya existe una lista de reproducción con el nombre '{nombre_lista}'.")

    def agregar_lista_a_cola(self, nombre_lista):
        """Agrega una lista de reproducción completa a la cola de reproducción."""
        lista = self.listas_de_reproduccion.get(nombre_lista)
        if lista:
            self.cola.append((nombre_lista, lista))  # Guarda el nombre y la lista de canciones
            print(f"La lista de reproducción '{nombre_lista}' ha sido agregada a la cola.")
        else:
            print(f"No se encontró ninguna lista de reproducción con el nombre '{nombre_lista}'.")

    def mostrar_cola(self):
        """Muestra la cola de reproducción actual con las listas de reproducción."""
        if not self.cola:
            print("La cola de reproducción está vacía.")
        else:
            print("Cola de reproducción actual:")
            for indice, (nombre_lista, canciones) in enumerate(self.cola, start=1):
                print(f"{indice}. Lista '{nombre_lista}' con canciones: {list(canciones.values())}")

    def modo_aleatorio(self):
        """Selecciona una canción aleatoria de todas las listas de reproducción en la cola."""
        if not self.cola:
            print("No hay listas de reproducción en la cola.")
            return
        # Elegir una lista de reproducción aleatoria de la cola
        lista_aleatoria = random.choice(self.cola)
        nombre_lista, canciones = lista_aleatoria
        numero_aleatorio = random.choice(list(canciones.keys()))
        cancion_aleatoria = canciones[numero_aleatorio]
        print(f"Reproduciendo en modo aleatorio: '{cancion_aleatoria}' de la lista '{nombre_lista}'")