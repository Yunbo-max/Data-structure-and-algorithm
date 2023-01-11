import turtle
def tree(brench):
    if brench>0:
        t.forward(brench)
        t.right(20)
        tree(brench-6)
        t.left(40)
        tree(brench-6)
        t.right(20)
        t.backward(brench)

t=turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(1)

tree(60)
turtle.done()