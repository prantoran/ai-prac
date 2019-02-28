import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(10)

    for i in range(1, 36):
        draw_square(brad)
        brad.right(10)

    # brad.forward(100)
    # brad.right(90)
    # brad.forward(100)
    # brad.right(90)
    # brad.forward(100)
    # brad.right(90)
    # brad.forward(100)
    # brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)



    window.exitonclick()

draw_art()
