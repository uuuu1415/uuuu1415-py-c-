import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")

# Create a turtle named "star"
star = turtle.Turtle()
star.color("yellow")
star.speed(10)

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        star.forward(size)
        star.right(144)
        star.forward(size)
        star.left(72)

# Draw multiple stars
for size in range(30, 300, 30):
    draw_star(size)
    star.penup()
    star.goto(-size/3, -size/3)
    star.pendown()

# Hide the turtle and display the window
star.hideturtle()
wn.mainloop()