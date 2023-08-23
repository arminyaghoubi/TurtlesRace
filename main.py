from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
screen.title("Turtle Race")
user_bet = screen.textinput("Your bet", "Which turtle will win[Red,Blue,Purple,Gold,Silver]?")

finish_line = Turtle()
finish_line.penup()
finish_line.goto(x=230, y=150)
finish_line.right(90)
finish_line.pendown()
finish_line.forward(300)

colors = ["red", "deep sky blue", "dark green", "dark slate blue", "gold", "dim gray"]
turtle_list = []
start_position_list = [80, 40, 0, -40, -80]
for i in range(0, 5):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=start_position_list[i])
    turtle_list.append(new_turtle)

best_turtle_position = -230

while best_turtle_position < 230:
    for player in turtle_list:
        forward = random.randint(1, 10)
        player.forward(forward)
        if best_turtle_position < player.xcor():
            best_turtle_position = player.xcor()
        if player.xcor() > 230:
            if player.pencolor() == user_bet:
                print(f"You've won!")
            else:
                print(f"You've lost!")
            break

screen.exitonclick()
