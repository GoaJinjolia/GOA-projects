from turtle import *


#we want to paint a house
speed(10) #30 is too fast
#step 1:  draw a square
width(7)
color("purple")
forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)
left(90)
#end of square


#drawing a dor 
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)

pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
color("blue")
begin_fill()
goto(200, 120)
pendown()
right(60)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

right(90)
forward(60)

color("white")
forward(80)


color("blue")
begin_fill()
forward(60)
right(90)

forward(60)
right(90)
forward(60)

right(90)
forward(60)
end_fill()


exitonclick()