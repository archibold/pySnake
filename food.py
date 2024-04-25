from turtle import Turtle
import random


class Food(Turtle):
    point = 0

    def __init__(self):
        super().__init__()
        self.regenerate()

    def regenerate(self):
        self.point += 1
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed(10)
        self.goto(random.randint(-27, 27) * 10, random.randint(-27, 27) * 10)