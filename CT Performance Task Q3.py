import turtle

screen = turtle.Screen()
screen.bgcolor("black")

octagon = turtle.Turtle()
octagon.shape("turtle")
octagon.color("#FFD700") 
octagon.fillcolor("#FFD700") 

octagon.penup()
octagon.goto(-50, -50) 
octagon.pendown()

octagon.begin_fill()

for _ in range(8):
    octagon.forward(100)
    octagon.left(45)

octagon.end_fill()

turtle.done()