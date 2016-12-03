from visual import *
Saturn = sphere(pos=(0,0,0), radius=0.2, color=color.yellow)
m1 = sphere(pos=(0.92,0,0), radius=0.05, color=color.red,make_trail=True)
m2 = sphere(pos=(1.08,0,0), radius=0.05, color=color.blue,make_trail=True)
rc =vector(1,0,0)
vc=vector(0,5,0)
dt = 0.0001
theta=0
omega=0
while True:
  rate(500)
  r=sqrt((rc.x)**2+(rc.y)**2)
  vc=vc-vector(4*(pi**2)*rc.x*dt/(r**3),4*(pi**2)*rc.y*dt/(r**3),0)
  rc=rc+(vc[0]*dt,vc[1]*dt,vc[2]*dt)
  beta=-3*4*(pi**2)/r**5*(rc.x*sin(theta)-rc.y*cos(theta))*(rc.x*cos(theta)+rc.y*sin(theta))
  omega=omega+beta*dt
  theta=theta+omega*dt
  m1.pos=rc+(0.08*cos(theta),0.08*sin(theta),0)
  m2.pos=rc-(0.08*cos(theta),0.08*sin(theta),0)                                                      
                                                           

