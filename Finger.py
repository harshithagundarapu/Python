import turtle

screen = turtle.Screen()
screen.title("Human Finger")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(5)
t.pensize(3)

# Draw the finger
t.penup()
t.goto(-40, -150)
t.pendown()

t.color("black", "peachpuff")
t.begin_fill()

# Left side
t.setheading(90)
t.forward(220)

# Rounded fingertip
t.circle(40, 180)

# Right side
t.forward(220)

# Bottom
t.circle(40, 180)

t.end_fill() 

# Draw finger joint lines
t.penup()
t.goto(-38, -30)
t.pendown()
t.setheading(0)
t.forward(76)

t.penup()
t.goto(-38, 40
