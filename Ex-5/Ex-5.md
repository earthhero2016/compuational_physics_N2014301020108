#Homework 5 胡塾绪 2014301020108
##Problem 2.7
Use the adiabatic model of the air density (2.24) to calculate the cannon shell trajectory, and compare with the results found using (2.23). Also, one can further incorpotate the effects of the variation of the ground temperature(seasonal changes) by replacing B_2 by B_2^ref(T_0/T_ref)^alpha, where B^ref is the value of B_2 at a reference temperature T_ref and T_0 is the actual 
ground temperature. The value quoted in the text is appropriate for T=300K. In particular, how much effect will the adiabatic model have on the maximum range and the launch angle to achive it? How much do they vary from a cold day in winter to a hot summer day?
###1.Comparing adiabatic model with isothermal model
####Analysis
![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-5/2.7.png)
####Solution
Plot the trajectories of the cannon shell with an initial velocity 700m/s and projecting angle 35,45,50 degree respectively at temperature T=300K for both isothermal model and adiabatic model.

[Code for isothermal model](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-5/2.7.py)

[Code for adiabatic model](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-5/untitled1.py)

Output

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-5/figure_3.png)

where 'i' represents isothermal and 'a' represents adiabatic.

From this figure, we find that the projecting range of adiabatic model is generally smaller than that of isothermal one. Using method of dichotomy(二分法),we find the maximum range of adiabatic model is about 19232.62m with a projecting angle 36.95 degree and the maximum range of the isothermal model is about 21394.665m with a projecting angle 42.23 degree.
####Conclusion
The maximum range of the adiabatic model and corresponding optimal angle is smaller than those of isothermal model
###Seasonal difference
![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-5/QQ%E6%88%AA%E5%9B%BE20161016160728.png)

####Solution
First, plot the trajectories of the cannon shell with an initial velocity 700m/s and projecting angle 40,45,50 degree respectively for adiabatic model. Choose T=273K as the winter temperature and T=303K as the summer temperature.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-5/untitled2.py)

Output

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-5/figure_4.png)
