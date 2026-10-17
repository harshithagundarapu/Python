import turtle

t = turtle.Turtle()
t.speed(5)
t.pensize(4)

# Draw Doraemon's blue face
t.penup()
t.goto(0, -150)
t.pendown()
t.color("black", "deepskyblue")
t.begin_fill()
t.circle(150)
t.end_fill()

# Draw white face
t.penup()
t.goto(0, -130)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(130)
t.end_fill()

# Draw left eye
t.penup()
t.goto(-40, 100)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(25)
t.end_fill()

# Draw right eye
t.penup()
t.goto(40, 100)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

# Draw pupils
t.penup()
t.goto(-30, 120)
t.dot(12, "black")

t.goto(30, 120)
t.dot(12, "black")

# Draw red nose
t.goto(0, 70)
t.dot(25, "red")

# Draw nose line
t.goto(0, 70)
t.pendown()
t.goto(0, -20)

# Draw mouth
t.penup()
t.goto(-65, -20)
t.pendown()
t.setheading(-60)
t.circle(75, 120)

# Draw whiskers
t.penup()
t.goto(-40, 20)
t.pendown()
t.goto(-110, 40)

t.penup()
t.goto(-40, 0)
t.pendown()
t.goto(-115, 0)

t.penup()
t.goto(-40, -20)
t.pendown()
t.goto(-110, -40)

t.penup()
t.goto(40, 20)
t.pendown()
t.goto(110, 40)

t.penup()
t.goto(40, 0)
t.pendown()
t.goto(115, 0)

t.penup()
t.goto(40, -20)
t.pendown()
t.goto(110, -40)

# Hide turtle and display window
t.hideturtle()
turtle.done()
