import tkinter as tk
#import PIL as pil
#from PIL import Image
#from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog


def fermer_fenetre() :
    racine.destroy()

nb_clics = 0

def compteur(event):
    global nb_clics
    texte['text'] = str(nb_clics)
    nb_clics = nb_clics + 1

    #definir la variable globale compt
    #actualiser la valeur affichée dans le label

#ajouter un canevas

def affiche(event):
    print(event.widget['bg'])



racine= tk.Tk()
racine.title("rappel du 1er semestre")
texte = tk.Label(racine, text="j'adore python")
texte.grid()


bouton = tk.Button(racine, text="quitter", bg="blue", fg="yellow", command=fermer_fenetre)
bouton.grid(column=0, row=1)

canvas_red = tk.Canvas(racine, background = "red", width= 300, height=300)
canvas_red.grid(row =0 , column =1 )

canvas_black = tk.Canvas(racine, background = "black", width= 300, height=300)
canvas_black.grid(row =1 , column =1 )

#canvas_red.bind("<Button-1>", compteur)

canvas_red.bind("<Double-1>", affiche)
canvas_black.bind("<Double-1>", affiche)




racine.mainloop()
