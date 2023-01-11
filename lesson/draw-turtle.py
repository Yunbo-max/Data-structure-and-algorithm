import turtle
t=turtle.Turtle()
t.pensize(2)
t.pencolor("red")
def drawspriral(t,line):
    if line>0:
        t.forward(line)
        t.right(144)
        drawspriral(t,line-5)


drawspriral(t,200)
turtle.done()

