#Homework 4 胡塾绪 2014301020108
##Problem
1.5.Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are
                                
  ![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Exercise-4/E1.png)

where for simplicity we have assumed that the two types of decay are characterized by the same time constant, tau. Solve this system of equation for the numbers of nuclei, NA and NB, as functions of time. Consider different initial conditions, such as NA=100, NB=0, etc, and take tau=1s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.
##Analysis
When the time interval is sufficiently small, we'll have the approximations

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Exercise-4/E2.png)

Substituting these approximations for the derivatives in the rate equations, we obtain

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Exercise-4/E3.png)

If we initialize NA,NB,tau and time interval delta t, we can design a program that add the increase of NA or NB every time interval. Then, we can obtain the value of NA and NB after a certain time period and plot the variation of them. In this way, it can be shown that whether the system reaches a stteady state in which NA and NB are invariable or not.
##Solution
1.Initialize NA,NB,dt,time constant, duration.


2.Calculate NA,NB step by step.

In order to plot the variation of NA and NB, we add the value of NA or NB every step into a list.

3.Plot

[Here is the code.](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/untitled0.py)

Output

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/figure_1.png)
##Exploration
Now, we change the intial values of NA, NB. For example, we set NA=100,NB=20 and NA=80, NB=20 at time zero. Just see what happens.

For NA=100 and NB=20,

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Exercise-4/figure_1-1.png)

For NA=80 and NB=20,

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Exercise-4/figure_1-2.png)

It seems that the system reaches a steay state according to these three pictures. Besides, if NA=a and NB=b at time zero, the final value of NA or NB seems to be (a+b)/2. So let make such an assumption

To prove this, take the first case for an example, we let the program output the final list of NA and NB.

Extending the time duration to 20 and adding the following words

        for self.nsteps in range(200,201):
          print(self.n_A)

we obtain

[100, 90.0, 82.0, 75.6, 70.47999999999999, 66.38399999999999, 63.107199999999985, 60.485759999999985, 58.388607999999984, 56.710886399999985, 55.368709119999984, 54.29496729599999, 53.43597383679999, 52.74877906943999, 52.19902325555199, 
... 50.00000000000028, 50.00000000000022, 50.00000000000018, 50.00000000000014, 50.000000000000114, 50.00000000000009, 50.00000000000007, 50.00000000000006, 50.00000000000004, 50.000000000000036, 50.00000000000003, 50.00000000000002, 50.000000000000014, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001, 50.00000000000001]

Next, adding 

        for self.nsteps in range(200,201):
          print(self.n_B)

we obtain

[0, 10.0, 18.0, 24.4, 29.52, 33.616, 36.8928, 39.51424, 41.611392, 43.2891136, 44.63129088, 45.705032704, 46.5640261632, 47.251220930559995, 47.80097674444799, 48.24078139555839, 48.59262511644671, 48.87410009315737, 49.09928007452589, 
... 49.99999999999955, 49.99999999999964, 49.99999999999971, 49.999999999999766, 49.99999999999981, 49.999999999999844, 49.99999999999987, 49.99999999999989, 49.999999999999915, 49.99999999999993, 49.99999999999994, 49.99999999999995, 49.99999999999996, 49.999999999999964, 49.99999999999997, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998, 49.99999999999998]

<font size="5">From this, we can believe that the assumption is highly precise. The deflection is because the time constant we set is too large. Alternatively, this is because we omit the higher oder term of the Taylor expansion.</font>

