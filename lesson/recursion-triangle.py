import turtle
def sierpinski(degree,points):
    colormap=['purple','red','green','yellow','pink','orange','light blue']
    drawtriangle(points,colormap[degree])
    if degree >0:
        sierpinski(degree-1,{'left':points['left'],
                             'top':getmid(points['left'],points['top']),
                             'right':getmid(points['left'],points['right'])})
        sierpinski(degree-1,{'left':getmid(points['left'],points['top']),
                             'top':points['top'],
                             'right':getmid(points['top'],points['right'])})
        sierpinski(degree-1,{'left':getmid(points['left'],points['right']),
                             'top':getmid(points['top'],points['right']),
                             'right':points['right']})
def drawtriangle(points,color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()
def getmid(p1,p2):
    return((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
t=turtle.Turtle()
points={'left':(-200,-100),'top':(0,200),'right':(200,-100)}
sierpinski(3,points)
turtle.done()














