import tkinter as tk

racine = tk.Tk()

bouton = tk.Button(racine, text = "Restart")
bouton.grid(row=0, column=1)

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
mon_canvas = tk.Canvas(racine, background = "blue", width= CANVAS_WIDTH, height=CANVAS_HEIGHT)
mon_canvas.grid(row= 1, column= 1)

bouton_rectangle = tk.Button(racine, text="", background= "green",
 activeforeground="black", activebackground="yellow")
boton_rectangle_window = mon_canvas.create_window(200, 200, window=bouton_rectangle) 


racine.mainloop()