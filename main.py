import tkinter as tk
import time
import random


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.kolo = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.kolo, 245, 100)
        numbers = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(numbers)
        self.y = random.choice(numbers)

    def draw(self):
        self.canvas.move(self.kolo, self.x, self.y)
        pos = self.canvas.coords(self.kolo)
        if pos[1] <= 0:
            self.y *= -1
        if pos[3] >= 600:
            self.y *= -1
        if pos[0] <= 0:
            self.x *= -1
        if pos[2] >= 500:
            self.x *= -1





root = tk.Tk()
root.title('Гра')
root.geometry('500x600+700+50')
root.resizable(False, False)
canv = tk.Canvas(root, width=500, height=700, bg='white')
canv.pack()

ball = Ball(canv, 'red')

while True:
    ball.draw()
    root.update()
    time.sleep(0.01)


root.mainloop()