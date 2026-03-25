# CSE 231 Fall 2012
# Project 02
# Section: [your section]    Date: [today's date]
# Description: Draw a pleasing picture with multiple colored shapes using turtle.
import turtle
import random
import time

print("This program draws multiple colored shapes using turtle.")
print("You will supply a single integer: the number of shapes to draw (3..60).")

# input validation (while loop 1)
while True:
    s = input("Enter number of shapes (integer between 3 and 60): ").strip()
    if s.isdigit():
        n = int(s)
        # selection (if) to enforce range
        if 3 <= n <= 60:
            break
    print("Invalid input — please enter an integer between 3 and 60.")

# choose size/spacing depending on n (if used to vary layout)
if n <= 12:
    size = 120
    radius = 150
else:
    size = max(20, 300 // n)
    radius = max(60, 120 + (12 - min(n,12)) * 5)

turtle.colormode(1.0)
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(0, 0)

angle = 360 / n

# draw shapes (for loop)
for i in range(n):
    # random color
    color = (random.random(), random.random(), random.random())
    turtle.pencolor(color)
    turtle.fillcolor(color)

    # position turtle on circle
    turtle.penup()
    turtle.home()
    turtle.right(i * angle)
    turtle.forward(radius)
    turtle.pendown()

    # draw a filled polygon (4-sided square) — inner loop (second repetition)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

# write a short label at center
turtle.penup()
turtle.home()
turtle.goto(-60, -10)
turtle.pencolor("black")
turtle.write(f"{n} shapes", font=("Arial", 16, "normal"))

# keep window open a bit (or use turtle.done())
time.sleep(0.5)
turtle.done()