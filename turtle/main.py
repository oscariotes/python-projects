#####Turtle Intro######

import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)


######## Challenge 1 - Draw a Square ############

# timmy_the_turtle.clear()

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# ************ Draw Dashes **************


""" for _ in range(20):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
 """

# for _ in range(3):
#     timmy_the_turtle.backward(-120)
#     # timmy_the_turtle.left(-120)
#     # timmy_the_turtle.backward(100)
#     # timmy_the_turtle.left(-120)

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)


for shape in range (3, 11):
    draw_shape(shape)
    


t.exitonclick()
