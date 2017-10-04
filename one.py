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
owen.color("hotpink")
owen=turtle.Turtle()



make_squares(owen,20,5)