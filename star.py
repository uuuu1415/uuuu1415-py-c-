import turtle

def setup_screen():
    screen = turtle.Screen()
    screen.bgcolor("black")
    return screen

def create_star_turtle():
    star_turtle = turtle.Turtle()
    star_turtle.color("yellow")
    star_turtle.speed(10)
    return star_turtle

def draw_star(turtle, size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

def draw_multiple_stars(turtle, start_size=30, end_size=300, step_size=30):
    turtle.clear()
    for size in range(start_size, end_size, step_size):
        draw_star(turtle, size)
        turtle.penup()
        turtle.goto(-size / 2, -size / 2)
        turtle.pendown()

def main():
    screen = setup_screen()
    star_turtle = create_star_turtle()
    # Hide the turtle after drawing all stars
    star_turtle.hideturtle()
    star_turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()