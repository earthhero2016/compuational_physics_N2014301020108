#Homework 7 胡塾绪 2014301020108
##Abstract
This article mainly discusses chaos in thee driven nonlinear pendulum and involves the solutions of exercise 3.12,3.13,3.14.The crucial method used in the article is Euler_Cromer method.
##Background

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/2016-10-29_220600.png)

First, we investigate the behaviours of \theta for F_D=0.5 and F_D=1.2 with the same other parameters.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/theta.py)
Output

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/122.png)

From this, we see that the pendulum eventually oscillates with the driven force when F_D=0.5,however, when F_D is 1.2, the behaviour of the pendulum becomes unpredictable, namely, is in chaos.

Then, we plot the angular velocity versus time and the angular velocity versus \theta.
[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/omega.py)
Output

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/123.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/121.png)

This demonstrates that the angular velocity is also in chaos when F_D=1.2.
##Solution
###Exercise 3.12 Poincare section
In the phase-space graph, plot \omega versus \theta only at times that are in phase with the driving force. That is, only the points with fixed driven force phase. This is known as Poincare section. And it is a very useful way to plot and analyze the behavior of a dynamical system. To construct Poincare section, we plot points only when the phases of the driven force are fixed and therefore the times are also in fixed phase. Choose the driven force phases as 0, pi/4, pi/2, and 3pi/3.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/3.12.py)

When F_D=1.2

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/3.12_%E7%9C%8B%E5%9B%BE%E7%8E%8B.png)

It is intriguing to investigate what the Poincare section looks like when F_D=0.5.
The following figure shows what it is.

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/3.12%20F%3D0.5_.png)

It is not unacceptable that the points are so few because the behaviors of the system,including theta and angular velocity, are regular under F_D=0.5. To construct Poincare section, we select the points with fixed driven force phase. Since theta and omega would oscillate at the frequency of the driven force when the system comes to the steady state, the phases of the theta and omega would also be fixed. Thus, there are only few points on Poincare section.
###Exercise3.13 Comparison of two identical pendulums with slight difference of initial angles.
Imagine two identical pendulums only with slightly different initial angles. The difference is 0.001rad. Let us investigate the evolution of the difference of the angles of the two systems.

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/2016-10-29_234945.png)

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/3.13.py)

When F_D=0.5

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/3.131.png)
The Lyapunov exponent is -0.25.

When F_D=1.2

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-7/3.132.png)

The Lyapunov exponent is 0.16.
