#Homework 8 胡塾绪 2014301020108
##Abstract
This article mainly discusses chaos in thee driven nonlinear pendulum and involves the solutions of exerciseS 3.18,3.20, which focus on Poincare section and bifurcation diagrams.
##Background
![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/XXXXX1.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/2016-11-12_233208.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/3.12.png)
##Solution
###Exercise 3.18 Poincare section for different drive force amplitude.
Then parameters F_D chosen by the problem is 1.4,1.44,1.465 respecctively. In order to investigate the property of the pendulum with these driving force amplitude, we plot theta versus time first.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/theta.py)

Output

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/figure_1.png)

From this picture, we can see that the system with these parameters is not in chaos and actually it seems to be periodic after a few seconds. Additional, the period of theta when F_D=1.44 is twice as when F_D=1.4 and period when F_D=1.465 is four times as when F_D=1.4. Back to the last assignment, we have known that there are only few points in the Poincare section when the system is regular. This time, we remove the initial points corresponding to a non-steady state.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/3.18.py)

Output
When F_D=1.4

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/3.18%20FD%3D1.4.png)

When F_D=1.44

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/3.18%20FD%3D1.44.png)

When F_D=1.465

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/3.18%20FD%3D1.465.png)
