import turtle

bob=turtle.Turtle()


bob.color("black", "red")
bob.begin_fill()


for i in range(0,4):
    bob.forward(50)
    bob.left(90)

bob.end_fill()
