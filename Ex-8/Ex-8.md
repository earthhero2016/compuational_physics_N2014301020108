#Homework 8 胡塾绪 2014301020108
##Abstract
This article mainly discusses chaos in thee driven nonlinear pendulum and involves the solutions of exerciseS 3.18,3.20, which focus on Poincare section and bifurcation diagrams.
##Background
[![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/20140708131201_7154.gif)](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/pendulum.py)

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
###Exercise 3.20 Bifurcation Diagram
From the former problem, we have seen that as the period doubles the number of the points in Poincare section doubles. So if th e period keeps on doubling, what about the transition to chaos? A nice way to appreciate how this transition comes about is with what is known as a bifurcation diagram. In bifurcation, we show theta as a each value F_D.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/3.201.py)

Output

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/figure_3.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/4%20%201.459%201.476.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/1112.png)

We magnify the plot to find more transition points. 

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-8/3.212.png)

They are 1.47619, 1.47643, 1.47648, 1.47649.Considering the memory of the computer, these are all values of F_n we can find, n=1,2,3,4,5,6,7. So the number transitions we find is 128.

The corresponding values of Feigenbaum \delta are 2.1739,14.7706,4.5417,4.8,5. They are not so close to the limit value 4.669 since n here is not too large.
##Conclusions
By doing these exercise, we find that when the system is not in chaos, as the period doubles with the increase of the diving force amplitude, points in Poincare section doubles. This can be shown by doubling transitions in the bifurcation. As the order  of transitions becomes very large, the Feigenbaum \delta approaches to a fixed value.
##References
1.Giodano, N.J., Nakanishi, H. Computational Physics. Tsinghua University Press, December 2007

2.[S.Tan The eighth homework-Routes to Chaos: Period Doubling](http://www.jianshu.com/p/b141af43e303)

3.[Wu Yuqiao Exercise 9](https://github.com/wuyuqiao/computationalphysics_N2013301020142/blob/master/Chapter3---2/Exercise%209.md)
