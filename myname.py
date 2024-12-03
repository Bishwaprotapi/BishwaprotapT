import turtle
import random

# Set up the turtle
t = turtle.Turtle()
t.speed(5)  # Increased speed for better animation
t.width(3)  # Make lines thicker

# List of colors for random selection
colors = ['red', 'blue', 'green', 'purple', 'orange', 'magenta', 'cyan']

# Function to set random color
def random_color():
    t.color(random.choice(colors))

# Function to draw the letter 'B'
def draw_B():
    random_color()
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    t.left(90)
    t.forward(120)  # Made taller
    t.right(90)
    t.circle(-30, 180)  # Made bigger
    t.left(180)
    t.circle(-30, 180)
    t.penup()
    t.home()

# Function to draw the letter 'i'
def draw_i():
    random_color()
    t.penup()
    t.goto(-230, 0)  # Adjusted position
    t.pendown()
    t.left(90)
    t.forward(80)
    t.penup()
    t.goto(-230, 100)  # Adjusted dot position
    t.pendown()
    t.dot(15)
    t.penup()
    t.home()

# Function to draw the letter 's'
def draw_s():
    random_color()
    t.penup()
    t.goto(-180, 0)  # Adjusted position
    t.pendown()
    t.circle(30, 180)
    t.right(180)
    t.circle(-30, 180)
    t.penup()
    t.home()

# Function to draw the letter 'h'
def draw_h():
    random_color()
    t.penup()
    t.goto(-130, 0)  # Adjusted position
    t.pendown()
    t.left(90)
    t.forward(120)
    t.backward(60)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(60)
    t.penup()
    t.home()

# Function to draw the letter 'w'
def draw_w():
    random_color()
    t.penup()
    t.goto(-70, 120)  # Start from top
    t.pendown()
    t.right(90)
    t.forward(120)
    t.left(135)
    t.forward(60)
    t.right(90)
    t.forward(60)
    t.left(135)
    t.forward(120)
    t.penup()
    t.home()

# Function to draw the letter 'a'
def draw_a():
    random_color()
    t.penup()
    t.goto(-10, 0)  # Adjusted position
    t.pendown()
    t.left(75)
    t.forward(120)
    t.right(150)
    t.forward(120)
    t.backward(60)
    t.right(105)
    t.forward(35)
    t.penup()
    t.home()

# Function to draw the letter 'p'
def draw_p():
    random_color()
    t.penup()
    t.goto(50, 0)  # Adjusted position
    t.pendown()
    t.left(90)
    t.forward(120)
    t.right(90)
    t.circle(-30, 180)
    t.penup()
    t.home()

# Function to draw the letter 'r'
def draw_r():
    random_color()
    t.penup()
    t.goto(110, 0)  # Adjusted position
    t.pendown()
    t.left(90)
    t.forward(120)
    t.backward(60)
    t.right(90)
    t.circle(-30, 180)
    t.penup()
    t.home()

# Function to draw the letter 'o'
def draw_o():
    random_color()
    t.penup()
    t.goto(170, 0)  # Adjusted position
    t.pendown()
    t.circle(30)
    t.penup()
    t.home()

# Function to draw the letter 't'
def draw_t():
    random_color()
    t.penup()
    t.goto(230, 120)  # Start from top
    t.pendown()
    t.right(90)
    t.forward(120)
    t.left(90)
    t.backward(30)
    t.forward(60)
    t.penup()
    t.home()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor('black')  # Dark background
t.speed(5)  # Set speed

# Draw the name
draw_B()
draw_i()
draw_s()
draw_h()
draw_w()
draw_a()
draw_p()
draw_r()
draw_o()
draw_t()
draw_a()
draw_p()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()