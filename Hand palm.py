import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.title("Hand Palm Shape")
screen.bgcolor("white")

t.speed(3)
t.pensize(3)
t.color("black", "peachpuff")

# Draw the palm and fingers
t.penup()
t.goto(-60, -100)
t.setheading(90)
t.pendown()

t.begin_fill()

# Left side of palm and little finger
t.forward(100)
t.circle(-15, 180)
t.forward(60)

# Ring finger
t.circle(-15, 180)
t.forward(75)

# Middle finger
t.circle(-15, 180)
t.forward(85)

# Index finger
t.circle(-15, 180)
t.forward(65)

# Thumb
t.circle(-20, 100)
t.forward(65)
t.circle(-20, 100)

# Bottom of palm
t.forward(70)
t.circle(-40, 90)
t.forward(100)
t.circle(-40, 90)

t.end_fill()

t.hideturtle()
turtle.done()
