import turtle
import random
import math

screen = turtle.Screen()
screen.title("atom particle collision")
screen.bgcolor("black")
screen.setup(width=1200, height=800)

is_finished = False
galaxy_stars = []

screen.addshape("star", ((0, -10), (3, -3), (10, 0), (3, 3), (0, 10), (-3, 3), (-10, 0), (-3, -3), (0, -10)))
particles = []
stars = []

num_particles = 100

def color_gradient(fraction, color1=(1, 0.1, 0), color2=(1, 1, 0)):
    r = color1[0] * (1 - fraction) + color2[0] * fraction
    g = color1[1] * (1 - fraction) + color2[1] * fraction
    b = color1[2] * (1 - fraction) + color2[2] * fraction
    return (r, g, b)

def blue_gradient(fraction, start_color=(255, 255, 255), end_color=(0, 0, 255)):
    r = start_color[0] * (1 - fraction) + end_color[0] * fraction
    g = start_color[1] * (1 - fraction) + end_color[1] * fraction
    b = start_color[2] * (1 - fraction) + end_color[2] * fraction
    return (int(r), int(g), int(b))

for _ in range(num_particles):
    particle = turtle.Turtle()
    particle.shape("circle")
    particle.shapesize(0.8)  
    particle.penup()
    particle.speed(0)
    particle.goto(0, 0)
    angle = random.randint(0, 360)
    particle.setheading(angle)
    particle.velocity = random.uniform(20, 40)
    random_fraction = random.random()
    particle.color(color_gradient(random_fraction, (1, 0.1, 0), (1, 1, 0)))
    particles.append(particle)

def create_star(particle):
    star = turtle.Turtle()
    star.shape("star")
    random_size = random.uniform(0.1, 0.6)  
    star.shapesize(random_size)
    star.penup()
    star.speed(0)
    star.goto(particle.pos())
    star.color("white")
    stars.append(star)

def form_galaxy():
    arms = 8  
    arm_angle = 360 / arms
    turtle.colormode(255)  
    galaxy_stars = []
    
    for i, star in enumerate(stars):
        galaxy_star = turtle.Turtle()
        galaxy_star.shape("star")
        galaxy_star.shapesize(0.5)  
        fraction = (i // arms) / (len(stars) // arms)
        color = blue_gradient(fraction)
        galaxy_star.color(color)
        galaxy_star.penup()
        angle = i * 0.5
        radius = 200 * math.sqrt(i / len(stars))
        theta = math.radians(angle + arm_angle * (i % arms))
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        galaxy_star.goto(x, y)
        galaxy_stars.append(galaxy_star)
    
    return galaxy_stars

def move_particles():
    for particle in particles[:]:
        particle.forward(particle.velocity)
        particle.velocity *= 0.9

        current_color = particle.color()[0]
        new_color = color_gradient(particle.velocity / 40, current_color, (0, 0, 0))
        particle.color(new_color)
        particle.shapesize(max(0.3, particle.shapesize()[0] * 0.95))

        if particle.velocity < 10:
            create_star(particle)
            particle.hideturtle()
            particles.remove(particle)

while particles:
    move_particles()
    screen.update()

galaxy_stars = form_galaxy()

screen.mainloop()
