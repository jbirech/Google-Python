import turtle

wd = turtle.Screen()
wd.title("Ping Pong")
wd.setup(width=800, height=600)
wd.bgcolor("yellow")
wd.tracer(0)

#score

sc_a = 0
sc_b = 0
#paddle A
#turtle ==> represents the module
#Turtle ==> represents the Object class
pd_A = turtle.Turtle()
pd_A.speed(0)
pd_A.shape("square")
pd_A.color("white")
pd_A.shapesize(stretch_wid=5, stretch_len=1)
pd_A.penup()
pd_A.goto(-350, 0)

#paddle B
pd_B = turtle.Turtle()
pd_B.speed(0)
pd_B.shape("square")
pd_B.color("white")
pd_B.shapesize(stretch_wid=5, stretch_len=1)
pd_B.penup()
pd_B.goto(350, 0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

#score board

sc = turtle.Turtle()
sc.speed(0)
sc.color("red")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))

#functions to move the paddle up and down
def pd_A_up():
	y = pd_A.ycor()
	y += 20
	pd_A.sety(y)

def pd_A_down():
	y = pd_A.ycor()
	y -= 20
	pd_A.sety(y)

def pd_B_up():
	y = pd_B.ycor()
	y += 20
	pd_B.sety(y)

def pd_B_down():
	y = pd_B.ycor()
	y -= 20
	pd_B.sety(y)
	
#keyboard binding
wd.listen()
wd.onkeypress(pd_A_up, "w")
wd.onkeypress(pd_A_down, "s")
wd.onkeypress(pd_B_up, "Up")
wd.onkeypress(pd_B_down, "Down")
#Main Loop
while True:
	wd.update()

	#move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		sc_a += 1
		sc.clear()
		sc.write("player A: {}  Player B: {}".format(sc_a, sc_b), align="center", font=("courier", 24, "normal"))

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		sc_b += 1
		sc.clear()
		sc.write("player A: {}  Player B: {}".format(sc_a, sc_b), align="center", font=("courier", 24, "normal"))
	#paddle and ball collision

	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pd_B.ycor() + 40 and ball.ycor()  > pd_B.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pd_A.ycor() + 40 and ball.ycor()  > pd_A.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1