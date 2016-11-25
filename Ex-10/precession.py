from visual import *
sun = sphere(pos=(0,0,0), radius=0.045, color=color.red)
m = sphere(pos=(0.39,0,0), radius=0.011, color=color.yellow,make_trail=True)

m.velo=vector(0,9.82,1.09)
dt = 0.0001
a=0.02
while True:
  rate(500)
  r=sqrt((m.x)**2+(m.y)**2+(m.z)**2)
  m.velo=m.velo-vector(4*(pi**2)*m.x*dt*(1+a/r**2)/(r**3),4*(pi**2)*m.y*dt*(1+a/r**2)/(r**3),4*(pi**2)*m.z*dt*(1+a/r**2)/(r**3))
  m.pos=m.pos+(m.velo[0]*dt,m.velo[1]*dt,m.velo[2]*dt)


