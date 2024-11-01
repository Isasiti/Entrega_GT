import tkinter as tk
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Reproductor de Música")
        
        # Configuración de pygame mixer
        mixer.init()
        
        # Cola de reproducción y favoritos
        self.queue = []  # Aquí se almacenarán las canciones en cola
        self.favorites = []  # Lista de canciones favoritas
        self.current_song_index = 0
        # Botones de control
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.next_button = tk.Button(root, text="Next", command=self.next_song)
        # Posiciona los botones en la interfaz
        self.play_button.pack()
        self.pause_button.pack()
        self.next_button.pack()
    def play_music(self):
        if self.queue:
            mixer.music.load(self.queue[self.current_song_index])
            mixer.music.play()

    def pause_music(self):
        mixer.music.pause()
    
    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.queue)
        self.play_music()
root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()
