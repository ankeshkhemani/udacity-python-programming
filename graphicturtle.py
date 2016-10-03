import turtle
def draw_circle(brad):
    brad.circle(100)

def draw_triangle(brad):
    for x in range(3):
        brad.forward(100)
        brad.right(120)
    
    
def draw_square(brad):
    for x in range(4):
        brad.forward(100)
        brad.right(90)


window = turtle.Screen()
window.bgcolor("red")
brad=turtle.Turtle()
brad.shape("circle")
brad.color("yellow")
brad.speed(5)

for x in range(36):
    draw_square(brad)
    brad.right(10)
#draw_circle(brad)
#draw_triangle(brad)
window.exitonclick()

