import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(10)
col = ['yellow', 'blue', 'white', 'red']
c = 0
# apron_khunger

for i in range(75):
    t.forward(i*10)
    t.right(144)
    t.color(col[c])
    if c == 3:
        c = 0
    else:
        c += 1
