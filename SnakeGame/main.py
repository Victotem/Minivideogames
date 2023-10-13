from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        scoreboard.increase_score() 
        food.refresh()
        snake.extend()
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280 or snake.segments[0].ycor() > 280:
        game_is_on = False
        scoreboard.game_over()
        
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            
            


'''
starting_positions=[(0,0),(-20,0),(-40,0)]
segments=[]

for position in starting_positions:
    new_segment= Turtle("square") #shape es un atributo que se puede inicializar al invocar a la clase
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1): #El último cuadrado es el primero de la lista, es necesario hacerlo asi. Esto es como se hace en java version python
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward()
        
        
        

 '''



screen.exitonclick()
