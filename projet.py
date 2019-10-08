import tkinter

fenetre = tkinter.Tk()

canv = tkinter.Canvas(fenetre)
canv.grid(row = 0,column = 0)
canv.grid_columnconfigure(0,weight=0)
canv.grid_rowconfigure(0,weight=0)

fenetre.mainloop()