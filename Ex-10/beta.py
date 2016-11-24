from visual import *
a = sphere(pos=(1,0,0), radius=0.1, color=color.red,make_trail=True)
b = sphere(pos=(1,0,0), radius=0.1, color=color.yellow,make_trail=True)
a.velo=vector(0,4,0)
b.velo=vector(0,6.28)
beta=2.5
dt = 0.001

while True:
  rate(400)
  for p in [a,b]:
      r=sqrt((p.x)**2+(p.y)**2)
      p.velo=p.velo-vector(4*(pi**2)*p.x*dt/(r**(beta+1)),4*(pi**2)*p.y*dt/(r**(beta+1)),0)
      p.pos=p.pos+(p.velo[0]*dt,p.velo[1]*dt,0)


