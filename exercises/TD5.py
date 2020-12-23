import tkinter as tk 

racine = tk.Tk()
racine.title("titre de fenetre")
bouton = tk.Button(racine, text = "mon bouton")
bouton.grid(row = 0, column = 1)

canvas = tk.Canvas(racine, width = 500, height = 500, background = "black")
canvas.grid(row = 0, column = 1)


racine.mainloop()
