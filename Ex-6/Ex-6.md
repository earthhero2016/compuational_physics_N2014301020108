#Homework 6 胡塾绪 2014301020108
##Level 1 Problem 2.10(introducing wind velocity)
Generalize the program developed for the previous problem so that it can deal with situations in which the target is at a different altitude than the cannon. Consider cases in which the target is higher than the cannon.
###Analysis

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-6/jjj210.png)

###Solution
Assume the wind welocity is a constant -10m/s and along the x axis. In addition, the initial velocity of  the shell is 700m/s. When given the position of the target, we seek to find the launching angle with which the shell can hit the target precisely.

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

(22007.069791934664, 2199.990569664962, 38.50000000000001)

(21998.375745949616, 2199.9914725933477, 52.800000000000026)

(21997.5249834822, 2299.999928827686, 39.00000000000001)

(21995.908382689377, 2299.9811403432805, 52.50000000000002)

(22000.439049324148, 2399.9911853285794, 39.60000000000001)

(22005.005283922666, 2399.999078566599, 52.10000000000002)

(21998.062279150137, 2499.9818107184888, 40.20000000000003)

(21993.613363877, 2499.992924428236, 51.80000000000008)





