import tkinter as tk


racine = tk.Tk()

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
mon_canvas = tk.Canvas(racine, background = "black", width= CANVAS_WIDTH, height=CANVAS_HEIGHT)
mon_canvas.grid(row=1, column=1, rowspan= 3)

bouton= tk.Button(racine, text="recommencer")
bouton.grid(row= 3, column=1)

mon_canvas.create_rectangle(200, 300, 100, 100,width=0, fill = "red")
mon_canvas.create_rectangle(200, 300, 100, 100,width=0, fill = "blue")

racine.mainloop()