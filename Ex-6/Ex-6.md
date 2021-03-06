#Homework 6 胡塾绪 2014301020108
##Level 1 Problem 2.10(introducing wind velocity)
Generalize the program developed for the previous problem so that it can deal with situations in which the target is at a different altitude than the cannon. Consider cases in which the target is higher than the cannon.
###Analysis

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-6/jjj210.png)

###Solution with fixed initial velocity
Assume the wind velocity is a constant -10m/s and along the x axis. In addition, the initial velocity of  the shell is 700m/s. When given the position of the target, we seek to find the launching angle with which the shell can hit the target precisely.

Using the similar code of the cannon problem,however, we should stop the calculation at the target point. 

In order to achieve this goal, first, the statement while(y>y0）: is added, where y0 is the height of the target. 

Then, under this condition, we adjust the launching angle step by step to make the hitting point close to the target point. To reduce the operating time, we gradually decrease the scanning step of the launching angle while narrowing the error of the hitting point. Considering the real situation, we scan the angle from 30 to 60 degree.


                                 | scanning step | uncertainty/m   | 
                                 | ------------- |:--------------: | 
                                 |       2       |      200        | 
                                 |      0.5      |       50        |   
                                 |      0.1      |        8        |    
                        
[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-6/2.10.py)
####Output
Changing the x coodinate of the target.
![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-6/21000%202500%20(2).png)

The optimal angle is 35.4.

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-6/22000%202500%2B.png)

There are two allowed angles permitting the hitting poing to fall into (22000-8,22000+8).

Changing the x coodinate of the target.

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-6/initpintu_1.png)

The hitting points and launching angles are respectively

(22007.07, 2199.99, 38.5)  (21998.37, 2199.99, 52.8)

(21997.52, 2299.99, 39.0)  (21995.91, 2299.98, 52.5)

(22000.44, 2399.99, 39.6)  (22005.01, 2399.99, 52.1)

(21998.06, 2499.98, 40.2)  (21993.61, 2499.99, 51.8)
###Search for the minimum velocity.
Now, we should find the optimal firing angle with changing initial velocity simaltaneously. Only thing we have to do is scanning the velocity further.Choose (20000,3000)m as the target position and scan the initial velocity from 692m/s to 708m/s.
[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-6/2.10.v.py)

Output

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-6/mv.png)

Within the initial velocity interval (692,708)m/s, there are three trajectories responding to a launching angle that can hit the target with the uncertainty of 8m.
However, the minimum velocity is 692m/s responding to the firing angle of 35.4.
###Conclusion.
The writer designed a program to search for the launching angle to hit the target precisely and further the minimum firing velocity. Theoretically, the precision can be higher if the scanning step is much smaller, which, however, will noticeably increase the time of calculation. Although the precision is not too high, the operating time is still relatively a little long,which requires further improvement.












