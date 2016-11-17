#Homework 9 胡塾绪 2014301020108
##Abstract
This article mainly discusses the billiard problem, one of the chaotic problem, and use programs to plot the trajectories of the billiard and phase space. In addition, solutions of exercise 3.30 and 3.31 are included.
##Background
![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/2016-11-17_150518.png)

When the boundary is a unit circle, the trajectories of the ball are shown by the following pictures.

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/circle2.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/circle3.png)

The initial conditions are different in the two figures. Now, we plot the Phase-spaces of the two balls above, which can be constructed by plotting x-vx figures only when y=0.

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/circle2phase.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/circle3phase.png)

[Here is the code for the above programs.](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/3.30.py)

Vpython demonstration

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/GIF.gif)

The behavior of the billard gets more interesting when we consider other table shapes. Now cut the table along the x axis, and pull the two semicircular halves apart(along y), a distance 2ar. Choosing a=0.1,0.01,0.001 respectively, we plot the trajectories and phase spaces of the ball.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/3.301.py)

Output

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/Stadium%20billiard.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/Phase%20space.png)

From these pictures, we see that the behaviors of the billiard are kind of chaotic when the circle boundary is devided.
##Solution
###Excercise 3.30 Lyapunov exponent
![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/2016-11-17_155302.png)

[The code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/separation.py)

When a=0.1, 

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/Separation%200.16.png)

The Lyapunov exponent is about 0.16

When a=0.01

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/Separation%200.065.png)

The Lyapunov exponent is about 0.065.

When a-0.001,

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/Separation%200.22.png)

The Lyapunov exponent is about 0.22.

It is intruguing to investigate the further evolution of the separation. 

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-9/separation%20long%20time.png)


