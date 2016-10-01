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
