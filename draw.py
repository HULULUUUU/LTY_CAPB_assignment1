import turtle
  

screen = turtle.Screen()    
screen.bgcolor("white")  

pen = turtle.Turtle()  
pen.speed(3)  

pen.color("blue")  
pen.penup()  
pen.goto(-50, -50)
pen.pendown()  
pen.begin_fill()  
for _ in range(2):  
    pen.forward(100)  
    pen.right(90)  
    pen.forward(60)  
    pen.right(90)  
pen.end_fill()  
  
def draw_w(x, y, radius):  
    pen.penup()  
    pen.goto(x, y)  
    pen.pendown()  
    pen.color("black")  
    pen.begin_fill()  
    pen.circle(radius)  
    pen.end_fill()  
  
draw_w(-60, 10, 20)  

draw_w(40, 10, 20)  
  

pen.color("white")  
pen.penup()  
pen.goto(-30, -10)  
pen.pendown()  
pen.begin_fill()  
for _ in range(2):  
    pen.forward(60)  
    pen.right(90)  
    pen.forward(20)  
    pen.right(90)  
pen.end_fill()  
  
  
pen.hideturtle()  

turtle.done()