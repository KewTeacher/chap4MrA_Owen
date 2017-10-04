import turtle

def make_squares(turt,size,num):
    
    for j in range(num):
        turt.pendown()
        for i in range(4):
            turt.forward(size)
            turt.left(90)
        turt.penup()
        turt.forward(2*size)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

owen=turtle.Turtle()
owen.color("hotpink")
owen.pensize(3)


make_squares(owen,20,5)