import pygame
import tkinter as tk
from os import walk
from tkvideo import tkvideo

a = 0
i = 0

def check_event():
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            global i
            label['text'] = ''
            i = i + 1
            #play(f'music/{f[i]}')
            try:
                play(f[i])
            except:
                label['text'] = "Music ended(\nThank you for watching!"            
    root.after(100, check_event)
def play(name):
    pygame.mixer.music.load(f'music/{name}')
    #pygame.mixer.music.load(name)
    label['text'] = f[i]
    print(f'Now playing: {f[i]}')
    pygame.mixer.music.play()
# --- main ---
pygame.init()

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

root = tk.Tk()
root.configure(background='black')

label = tk.Label(root, bg='#000', fg='#fff')
label.pack()

my_label = tk.Label(root)
my_label.pack()

player = tkvideo("intro.mp4", my_label, loop = 1, size = (1280,720))
player.play()

#button = tk.Button(root, text='Play', command=play)
#button.pack()


if(a == 0):
    f = []
    for (dirpath, dirnames, filenames) in walk("music"):
        f.extend(filenames)
    a = 1
    print(f)
    play(f[i])

check_event()

root.mainloop()

pygame.quit()