import tkinter as tk
import random as rd


def draw_circle():
    centre_x = rd.randint(50, CANVAS_WIDTH - 50)
    centre_y = rd.randint(50, CANVAS_HEIGHT - 50)

    mon_canvas.create_oval(centre_x - 50, centre_y - 50, centre_x + 50, centre_y + 50, fill = "blue") 


racine = tk.Tk()
racine.title("mon dessin")

bouton_cercle = tk.Button(racine, text="cercle", command=draw_circle)
bouton_carre = tk.Button(racine, text="carré")
bouton_croix = tk.Button(racine, text="croix", background= "blue", 
foreground="red", activeforeground="black", activebackground="yellow", font=("helvetica", 26))
bouton_couleur = tk.Button(racine, text="choisir une couleur")

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
mon_canvas = tk.Canvas(racine, background = "black", width= CANVAS_WIDTH, height=CANVAS_HEIGHT, borderwidth= 5, relief="raised")

bouton_cercle.grid(row= 1, column=0)
bouton_carre.grid(row= 2, column=0)
bouton_croix.grid(row= 3, column=0)
bouton_couleur.grid(row= 0, column = 1)
mon_canvas.grid(row=1, column=1, rowspan= 3)

racine.mainloop()