#Homework 6 胡塾绪 2014301020108
##Level 1 Problem 2.10(introducing wind velocity)
Generalize the program developed for the previous problem so that it can deal with situations in which the target is at a different altitude than the cannon. Consider cases in which the target is higher than the cannon.
###Analysis

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-6/jjj210.png)

###Solution
Assume the wind welocity is a constant -10m/s and along the x axis. In addition, the initial velocity of  the shell is 700m/s. When given the position of the target, we seek to find the launching angle with which the shell can hit the target precisely.

Using the similar code of the cannon problem,however, we should stop the calculation at the target point. 

In order to achieve this goal, first, the statement while(y>y0）: is added, where y0 is the height of the target. 

Then, under this condition, we adjust the launching angle step by step to make the hitting point close to the target point. To reduce the operating time, we gradually decrease the scanning step of the launching angle while narrowing the error of the hitting point.


                                 | scanning step | uncertainty/m   | 
                                 | ------------- |:--------------: | 
                                 |       2       |      200        | 
                                 |      0.5      |       50        |   
                                 |      0.1      |        8        |    
                        
[Here is the code]{https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-6/2.10.py} 
