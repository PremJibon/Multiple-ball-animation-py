from tkinter import *
import time
from Ball import *

window = Tk()
window.title("Multiple ball animation")

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,'white')
tennise_ball = Ball(canvas,0,0,100,2,3,'red')
foot_ball = Ball(canvas,0,0,100,4,1,'blue')
hero_ball = Ball(canvas,0,0,100,3,1,'brown')

while True:
    volley_ball.move()
    tennise_ball.move()
    foot_ball.move()
    hero_ball.move()


    window.update()
    time.sleep(0.01)

window.mainloop()