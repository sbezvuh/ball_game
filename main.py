import tkinter as tk
import time
import random


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.kolo = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.kolo, 245, 100)
        numbers = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(numbers)
        self.y = random.choice(numbers)
        self.collide_bottom = False

    def collide(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.rect)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.kolo, self.x, self.y)
        pos = self.canvas.coords(self.kolo)
        if pos[1] <= 0:
            self.y *= -1
        if pos[3] >= 600:
            self.y *= -1
        if pos[3] >= 600:
            self.collide_bottom = True
        if self.collide(pos) == True:
            self.y *= -1
        if pos[0] <= 0:
            self.x *= -1
        if pos[2] >= 500:
            self.x *= -1


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.rect, 200, 500)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.rect, self.x, 0)
        pos = self.canvas.coords(self.rect)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= 500:
            self.x = 0

    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2


root = tk.Tk()
root.title('Гра')
root.geometry('500x600+700+50')
root.resizable(False, False)
canv = tk.Canvas(root, width=500, height=600, bg='white')
canv.pack()

paddle = Paddle(canv, 'blue')
ball = Ball(canv, paddle, 'red')


while True:
    if ball.collide_bottom == False:
        ball.draw()
        paddle.draw()
    root.update()
    time.sleep(0.01)


root.mainloop()