class Usuario:
    def __init__(self):
        self.usuarios = {}
    def crear_nuevo_usuario(self, nombre_usuario, contraseña):
        if nombre_usuario in self.usuarios:
        #este print si es medio necesario#
            print("Error: El usuario ya existe.")
        else:
            self.usuarios[nombre_usuario] = contraseña
        #Como se hara esto en tkinter?#
            print(f"Usuario {nombre_usuario} creado correctamente.")
    def validar_credenciales(self, nombre_usuario, contraseña):
        if nombre_usuario in self.usuarios and self.usuarios[nombre_usuario] == contraseña:
            return True
        else:
            return False
#Voy a usar muchos prints que sirven como referencia para la interfaz, MUCHOS#
class ReproductorDeMusica:
    def __init__(self):
        # Lista que almacenará todas las listas de reproducción con su nombre
        self.listas_de_reproduccion = []
    def crear_nueva_lista(self, nombre_lista, canciones):
        lista = {i + 1: canciones[i] for i in range(len(canciones))}
        nueva_lista = {"nombre": nombre_lista, "canciones": lista}
        self.listas_de_reproduccion.append(nueva_lista)
        #Insisto en que todos los prints son referencias para hacer despues en la interfaz :V#
        print(f"Lista de reproducción '{nombre_lista}' creada con {len(canciones)} canciones.")
    def mostrar_listas(self):
        """Muestra todas las listas de reproducción disponibles con sus nombres y canciones."""
        for idx, lista in enumerate(self.listas_de_reproduccion, 1):
        #No se como se hara esto en  la interfaz grafica#
            print(f"Lista {idx} - {lista['nombre']}: {lista['canciones']}")
    
    def agregar_cancion(self, nombre_lista, canciones):
        # Encontrar la lista de reproducción por nombre
        for lista in self.listas_de_reproduccion:
            if lista["nombre"] == nombre_lista:
                # Obtener el número de la última canción en la lista
                ultima_posicion = max(lista["canciones"].keys()) if lista["canciones"] else 0
                # Agregar cada canción nueva
                for i, cancion in enumerate(canciones, ultima_posicion + 1):
                    lista["canciones"][i] = cancion
                #este print lo dejo como referencia para la interfaz grafica#
                print(f"Se han agregado {len(canciones)} canciones a la lista '{nombre_lista}'.")
                return
        #en la mayoria de los prints se implementara manejo de errores pa la interfaz grafica#
        print(f"No se encontró la lista de reproducción con el nombre '{nombre_lista}'.")
    def eliminar_cancion(self, nombre_lista, numero_cancion):
        for lista in self.listas_de_reproduccion:
            if lista["nombre"] == nombre_lista:
                if numero_cancion in lista["canciones"]:
                    del lista["canciones"][numero_cancion]
                else:
                #Implementar manejo de errores,pero despues(no se como hacerlo)#
                    print(f"La canción número {numero_cancion} no existe en la lista '{nombre_lista}'.")
                return
    
    
