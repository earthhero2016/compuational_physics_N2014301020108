from visual import*
from math import *
scene.height,scene.width,scene.center=500,500,(0,-15,0)
L=18
r=2
t=0
dt=0.001
thet=pi/18 #degree 10
bracket=box(pos=(0,0.6*(-L-r),-2.5),length=1,width=0.5,height=25,material=materials.wood,color=color.yellow)
seat=box(pos=bracket.pos-(0,bracket.height/2.0,-2.5),length=20,width=12,height=1,material=materials.marble,color=(200,256,256))
cylinder(pos=(0,0,0.5),axis=(0,0,-3),radius=0.3)
f=frame()
ball=sphere(frame=f,pos=(L*sin(thet),-L*cos(thet),0),radius=r,material=materials.earth,color=color.orange)
rope=cylinder(frame=f,pos=(0,0,0),axis=ball.pos,radius=0.2,material=materials.rough,color=(0.5,0.,0.5))
while True:
   rate(1000)
   f.rotate(origin=(0,0,0),axis=(0,0,1),angle=thet*cos(sqrt(9.8/L)*(t+dt))-thet*cos(sqrt(9.8/L)*t))
   t+=dt
