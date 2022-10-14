import tkinter
from tkinter import ttk

window = tkinter.Tk()

def salir ():
    select.set( 'none')

select = tkinter.StringVar()
rb1 = ttk.Radiobutton(window, text = 'Opcion 1',value= 1, variable= select)
rb2 = ttk.Radiobutton(window, text = 'Opcion 2',value= 2, variable= select)
rb3 = ttk.Radiobutton(window, text = 'Opcion 3', value= 3, variable= select)

rb1.grid(column= 0, row= 0, padx= 5, pady= 5)
rb2.grid(column= 0, row= 1, padx= 5, pady= 5)
rb3.grid(column= 0, row= 2, padx= 5, pady= 5)


boton = ttk.Button(window, text= 'Reiniciar', command= salir)
boton.grid (column=0, row= 7)






window.mainloop()