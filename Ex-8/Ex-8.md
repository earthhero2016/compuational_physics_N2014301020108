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

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/3.12.py)

Output
When F_D=1.4

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/3.18%20FD%3D1.4.png)

When F_D=1.44

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/3.18%20FD%3D1.44.png)

When F_D=1.465

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/3.18%20FD%3D1.465.png)

Thus, concluded from the figures, when F_D=1.4, there is only one point in the Poincare section. And as the period doubles with the change of F_D, the number of points in the Poincare section will double correspondingly.

Now, let us investigate if the point is exactly the same number as we see.
Expand the area around one point, we will see the following picture.

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/3.18%20e.png)

It not so strange that the points scatters like a line when the theta coodinate is in a very tiny space because there is always  deflections calculating by computer. Maybe is the value of pi not precise enough, maybe dt or anything. But in a relative large scale, it is one point and indistinguishable.
