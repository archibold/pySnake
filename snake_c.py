from turtle import Turtle

LEFT = 180
DOWN = 270
UP = 90
RIGHT = 0


class Snake:
    _elements = []
    _moving = 'right'

    def __init__(self):
        for n in range(3):
            elem = Turtle()
            elem.speed(10)
            elem.penup()
            elem.shape('square')
            elem.color('green')
            elem.teleport(-10 * n, 0)
            self._elements.append(elem)
        self.head = self._elements[0]

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        self._moving = 'up'

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        self._moving = 'down'

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        self._moving = 'left'

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        self._moving = 'right'

    def move_one(self):
        pos = self.head.pos()
        if (pos[0] > 285 or pos[0] < -285) or (pos[1] > 285 or pos[1] < -285):
            return False
        for elem in self._elements:
            elem.forward(10)
            if self.head == elem:
                pass
            elif self.head.distance(elem) < 7:
                return False

        for index, elem in reversed(list(enumerate(self._elements))):
            if index != 0:
                elem.seth(self._elements[index-1].heading())
        return True

    def add_snake_element(self):
        elem = Turtle()
        elem.speed(10)
        elem.penup()
        elem.color('green')
        elem.shape('square')
        last_pos = self._elements[-1].pos()
        last_head = self._elements[-1].heading()
        self.move_one()
        elem.teleport(last_pos[0], last_pos[1])
        elem.setheading(last_head)
        self._elements.append(elem)