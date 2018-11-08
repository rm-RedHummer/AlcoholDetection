from vpython import *
ball = sphere(pos=vector(-5,0,0), radius=.5, color=color.cyan)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)
wallL = box(pos=vector(-6,0,0), size=vector(0.2,12,12), color=color.blue)
wallU = box(pos=vector(0,6,0), size=vector(0.2,12,12), color=color.yellow ,axis=vector(0,1,0))
wallD = box(pos=vector(0,-6,0), size=vector(0.2,12,12), color=color.red ,axis=vector(0,1,0))
wallB = box(pos=vector(0,0,-6), size=vector(0.2,12,12), color=color.orange ,axis=vector(0,0,1))
wallF = box(pos=vector(0,0,6), size=vector(0.2,12,12), color=color.orange , opacity=0, axis=vector(0,0,1))
wallU.rotate(radians(90), axis=wallU.axis, origin=wallU.pos)
wallD.rotate(radians(90), axis=wallD.axis, origin=wallD.pos)
wallB.rotate(radians(90), axis=wallB.axis, origin=wallB.pos)
wallF.rotate(radians(90), axis=wallF.axis, origin=wallF.pos)
ball.velocity = vector(20,1,-6)
deltat = 0.005
t = 0
vscale = 0.1
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.yellow)
#ball.trail = curve(color=ball.color)
while True:
    rate(100)
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.x < wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.y > wallU.pos.y:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.y < wallD.pos.y:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.z < wallB.pos.z:
        ball.velocity.z = -ball.velocity.z
    if ball.pos.z > wallF.pos.z:
        ball.velocity.z = -ball.velocity.z
    varr.pos = ball.pos #position of the tail
    varr.axis = vscale*ball.velocity #this is where the arrow is pointed
    ball.pos = ball.pos + ball.velocity*deltat
    #ball.trail.append(pos=ball.pos)
    t = t + deltat
    print(ball.pos)
