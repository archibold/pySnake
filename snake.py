from turtle import Screen
import time
from snake_c import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title('Ssssnake!!!')
scoreboard = Scoreboard()
screen.tracer(0)
screen.setup(600, 600)

screen.register_shape("square", ((5,5), (-5,5), (-5,-5), (5,-5)))

snake = Snake()
food = Food()
screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.move_left, 'Left')
screen.onkey(snake.move_right, 'Right')

screen.onkey(snake.move_one, 'w')
is_game = True
screen.listen()
screen.bgcolor("orange")

while is_game:
    screen.update()
    is_game = snake.move_one()
    time.sleep(scoreboard.speed)

    if snake.head.distance(food) < 7:
        snake.add_snake_element()
        food.regenerate()
        scoreboard.add_point()


scoreboard.game_over()
screen.exitonclick()



# while True:
#     snake.move_one()
#     screen.delay(50)


print(screen.screensize())


