import turtle
turtle.colormode(255)
s= turtle.Screen().bgcolor("black")
#making files 
file= turtle.Turtle()
file.hideturtle

def files(x,y,angles):
    file.penup()
    file.goto(x,y)
    file.right(angles)
    file.pendown()
    file.begin_fill()
    file.fillcolor((255,115,0))
    for i in range (4):
        if i%2==0:
            file.fd(100)
            file.right(90)
        else:
            file.fd(20)
            file.right(90)
    file.end_fill()
#making the basket
basket= turtle.Turtle()
basket.color("grey")
basket.begin_fill()
basket.fillcolor((160,160,160))
basket.fd(75)
basket.left(90)
basket.fd(60)
basket.right(90)
basket.fd(20)
basket.right(90)
basket.fd(80)
basket.right(90)

basket.fd(190)

basket.right(90)
basket.fd(80)
basket.right(90)
basket.fd(20)
basket.right(90)
basket.fd(60)
basket.left(90)
basket.fd(75)
basket.end_fill()
basket.hideturtle()

file.color((255,0,0))
file.right(180)
files(50,20,0)
files(50,43,15)
files(55,66,15)
files(66,88,15)
files(83,106,15)
turtle.write("Stack Overflow" , font=('Arial', 32 , 'bold'))
turtle.exitonclick()





























