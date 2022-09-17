import turtle


def drawSpiral(how_far, how_much):
    if how_far > 0:
        t.forward(how_far)
        t.right(how_much)
        drawSpiral(how_far-5, how_much)


turtle.Screen().bgcolor('black')
t = turtle.Turtle()
t.reset()
t.pencolor('red')
t.pen(speed=10)
turtle.delay(10)
lenth = 600
turn_by = 121
t.penup()
t.setpos(-lenth/2, lenth/2)
t.pendown()
drawSpiral(lenth, turn_by)
