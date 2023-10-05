import turtle
import random

world = turtle.Screen()
world.setup(width=400, height=400)
world.setworldcoordinates(0,0,400,400)
world.bgcolor("black")
world.colormode(255)


tula = turtle.Turtle()
tula.speed(5)

tula.up()
tula.goto(50,50)
tula.down()
tula.color("white")
tula.width(3)
tula.setheading(90)
tula.forward(300)
tula.right(90)
tula.forward(200)
tula.right(90)
tula.forward(300)
tula.right(90)
tula.forward(200)



def dot_visibility():
    c = random.randint(0,1)
    if c == 0:
        tula.color("white")
    else:
        tula.color("black")
        

#Draw dot #1
dot_visibility()
tula.up()
tula.goto(100, 300)
tula.down()

tula.dot(45)

#Draw dot #2
dot_visibility()
tula.up()
tula.goto(100, 200)
tula.down()

tula.dot(45)


#Draw dot #3
dot_visibility()
tula.up()
tula.goto(100, 100)
tula.down()

tula.dot(45)

#Draw dot #4
dot_visibility()
tula.up()
tula.goto(200, 300)
tula.down()

tula.dot(45)

#Draw dot #5
dot_visibility()
tula.up()
tula.goto(200, 200)
tula.down()

tula.dot(45)


#Draw dot #6
dot_visibility()
tula.up()
tula.goto(200, 100)
tula.down()

tula.dot(45)
