import turtle

# Create screen
screen = turtle.Screen()
screen.title("Human Face")
screen.bgcolor("white")

# Create turtle
t = turtle.Turtle()
t.speed(5)
t.pensize(3)

# Draw face
t.penup()
t.goto(0, -100)
t.pendown()
t.color("black", "peachpuff")
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw left eye
t.penup()
t.goto(-40, 30)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(15)
t.end_fill()

# Draw left pupil
t.penup()
t.goto(-35, 35)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(7)
t.end_fill()

# Draw right eye
t.penup()
t.goto(40, 30)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(15)
t.end_fill()

# Draw right pupil
t.penup()
t.goto(45, 35)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(7)
t.end_fill()

# Draw nose
t.penup()
t.goto(0, 25)
t.pendown()
t.setheading(-90)
t.forward(35)

# Draw smiling mouth
t.penup()
t.goto(-40, -35)
t.setheading(-60)
t.pendown()
t.circle(45, 120)

# Draw left ear
t.penup()
t.goto(-100, 0)
t.setheading(180)
t.pendown()
t.circle(20, 180)

# Draw right ear
t.penup()
t.goto(100, 0)
t.setheading(0)
t.pendown()
t.circle(20, 180)

# Finish
t.hideturtle()
turtle.done()
