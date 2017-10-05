import turtle
def make_square(turt,sz):
    """
    makes a square
    turt is turtle, sz is the length of the square's side
    """
    for i in range(4):
            turt.forward(sz)
            turt.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

owen=turtle.Turtle()
owen.color("hotpink")
owen.pensize(3)
owen.speed(10)

#we're using two variables for size,
#original_size stayes the same in order to keep the spacing the same
#size increase by orginal_size with each repitition
orginal_size = 20
size = orginal_size
for i in range(5):
    owen.pendown()
    make_square(owen,size)
    owen.penup()
    owen.backward(orginal_size/2)
    owen.right(90)
    owen.forward(orginal_size/2)
    owen.left(90)
    size = size + orginal_size

