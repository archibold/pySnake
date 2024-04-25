from turtle import Turtle


class Scoreboard(Turtle):
    point = 0
    speed = 0.1

    def __init__(self):
        super().__init__()
        self.penup()
        self.teleport(0, 260)
        self.write('Points: 0', False, align='center', font=('Arial', 30, 'normal'))

        self.hideturtle()

    def add_point(self):
        self.point += 1
        self.clear()
        self.write(f'Points: {self.point}', False, align='center', font=('Arial', 30, 'normal'))
        if self.point == 5:
            self.speed = 0.05
        if self.point == 10:
            self.speed = 0.04
        if self.point == 20:
            self.speed = 0.03
        if self.point == 30:
            self.speed = 0.025

    def game_over(self):
        self.teleport(0, 220)
        self.write(f'Game over', False, align='center', font=('Arial', 30, 'normal'))


