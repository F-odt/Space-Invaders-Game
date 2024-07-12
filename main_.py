import turtle
import random
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Space Invaders")

# Create the player's spaceship
player = turtle.Turtle()
player.color("lime")
player.shape("turtle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)  # rotates the turtle to face upwards

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# Create aliens
aliens = []

# Scoring
score = 0
high_score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.setposition(-380, 280)
score_display.hideturtle()
score_display.write(f"Score: {score}  High Score: {high_score}", align="left", font=("Arial", 14, "normal"))

# Game state
game_over = False


# Functions
def move_left():
    x = player.xcor()
    if x > -380:
        x -= 20
    player.setx(x)


def move_right():
    x = player.xcor()
    if x < 380:
        x += 20
    player.setx(x)


def fire_bullet():
    if not bullet.isvisible():
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    return distance < 20


def create_alien():
    alien = turtle.Turtle()
    alien.color("red")
    alien.shape("circle")
    alien.penup()
    alien.speed(0)
    x = random.randint(-380, 380)
    y = random.randint(200, 250)
    alien.setposition(x, y)
    aliens.append(alien)


# Set up key bindings
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")
screen.listen()

# Create initial aliens
for _ in range(5):
    create_alien()

# Main game loop
while not game_over:
    screen.update()

    # Move the bullet
    if bullet.isvisible():
        y = bullet.ycor()
        y += 20
        bullet.sety(y)

        # Check for bullet off-screen
        if bullet.ycor() > 280:
            bullet.hideturtle()

    # Move aliens
    for alien in aliens:
        y = alien.ycor()
        y -= 0.5
        alien.sety(y)

        # Check for alien collision with player
        if is_collision(player, alien):
            player.hideturtle()
            for a in aliens:
                a.hideturtle()
            screen.update()
            score_display.clear()
            score_display.write(f"Game Over! Final Score: {score}",
                                align="center", font=("Arial", 24, "normal"))
            game_over = True
            break

        # Check for bullet hitting alien
        if bullet.isvisible() and is_collision(bullet, alien):
            bullet.hideturtle()
            alien.hideturtle()
            aliens.remove(alien)
            score += 10
            if score > high_score:
                high_score = score
            score_display.clear()
            score_display.write(f"Score: {score}  High Score: {high_score}",
                                align="left", font=("Arial", 14, "normal"))

        # Check for alien off-screen
        if alien.ycor() < -280:
            alien.hideturtle()
            aliens.remove(alien)

    # Create new aliens
    if len(aliens) < 5:
        create_alien()

screen.mainloop()