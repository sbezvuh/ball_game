import tkinter as tk


root = tk.Tk()
root.title('Гра')
root.geometry('500x600+700+50')
root.resizable(False, False)
canv = tk.Canvas(root, width=500, height=700, bg='white')
canv.pack()


root.mainloop()