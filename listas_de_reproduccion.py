# Importa el diccionario de canciones desde el módulo
from modulo_canciones import canciones
class ReproductorDeMusica:
    def __init__(self):
        # Lista que almacenará todas las listas de reproducción con su nombre
        self.listas_de_reproduccion = []
    def crear_nueva_lista(self, nombre_lista, indices_canciones):
        """
        Crea una nueva lista de reproducción con el nombre dado y una lista de índices.
        Los índices se refieren a las llaves en el diccionario de canciones importado.
        """
        # Filtramos las canciones a partir de los índices dados y el diccionario importado
        lista_canciones = {i: canciones[i] for i in indices_canciones if i in canciones}
        nueva_lista = {"nombre": nombre_lista, "canciones": lista_canciones}
        self.listas_de_reproduccion.append(nueva_lista)
        print(f"Lista de reproducción '{nombre_lista}' creada con {len(lista_canciones)} canciones.")

    def mostrar_listas(self):
        """Muestra todas las listas de reproducción disponibles con sus nombres y canciones."""
        for idx, lista in enumerate(self.listas_de_reproduccion, 1):
            print(f"Lista {idx} - {lista['nombre']}:")
            for num, cancion in lista["canciones"].items():
                print(f"  {num}. {cancion}")

    def agregar_cancion(self, nombre_lista, indices_canciones):
        """
        Agrega canciones a una lista de reproducción existente, usando una lista de índices
        que hacen referencia a las llaves en el diccionario de canciones.
        """
        for lista in self.listas_de_reproduccion:
            if lista["nombre"] == nombre_lista:
                # Encuentra la última posición en la lista de reproducción para numerar correctamente
                ultima_posicion = max(lista["canciones"].keys()) if lista["canciones"] else 0
                for i, indice in enumerate(indices_canciones, start=ultima_posicion + 1):
                    if indice in canciones:
                        lista["canciones"][i] = canciones[indice]
                print(f"Se han agregado {len(indices_canciones)} canciones a la lista '{nombre_lista}'.")
                return
        print(f"No se encontró la lista de reproducción con el nombre '{nombre_lista}'.")

    def eliminar_cancion(self, nombre_lista, numero_cancion):
        """
        Elimina una canción de una lista de reproducción existente utilizando su número en la lista.
        """
        for lista in self.listas_de_reproduccion:
            if lista["nombre"] == nombre_lista:
                if numero_cancion in lista["canciones"]:
                    del lista["canciones"][numero_cancion]
                    print(f"La canción número {numero_cancion} ha sido eliminada de la lista '{nombre_lista}'.")
                else:
                    print(f"La canción número {numero_cancion} no existe en la lista '{nombre_lista}'.")
                return
        print(f"No se encontró la lista de reproducción con el nombre '{nombre_lista}'.")
