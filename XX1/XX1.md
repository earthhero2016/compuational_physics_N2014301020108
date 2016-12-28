#Final thesis: Phase Transitions, and the Ising Model
##胡塾绪 2014301020108
##Abstract
This article mainly discusses the phase transitions of ferromagnetism illustrated by the 2D-Ising model by using mean field theory and Monte Carlo method.The variation of magnetization with temperature and magnetic field is demostrated dominantly.
##Background
###Ferromagnetism
Ferromagnetism discribes the spontaneous magnetization of some materials,that is, a net magnetic moment in the absence of an external magnetic field. As the temperature increases, thermal motion, or entropy, competes with the ferromagnetic tendency. When the temperature rises beyond a certain point, called the Curie temperature, there is a second-order **phase transition** and the system can no longer maintain a spontaneous magnetization.
This phenomenon can be explained by the quantum mechanics. One of the fundamental properties of an electron is that it has a spin, which causes a magnetic dipole moment. If an atom has unpaired electron, it will has a net magnetic moment. Because of the **exchange interaction**,the distributions of the electric charge of twp nearby atoms with unpaired electrons in space are farther apart when the electrons have parallel spins than when they have opposite spins. This reduces the electrostatic energy of the electrons when their spins are parallel compared to their energy when the spins are anti-parallel, so the parallel-spin state is more stable. Therefore, there is a spontaneous magnetization.
However, if the temperature surpasses the **critical temperature**, the thermal motion, or entropy, competes with the ferromagnetic tendency for dipoles to align and the system can no longer maintain a spontaneous magnetization.
###Ising model 
![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/Ising.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/2016-12-28_110633.png)
##Mean Field Theory
![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/2016-12-28_153747.png)

[Here is te code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/8.1.py)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/Mean%20field.png)

As the picture shows, at low temperature, there is a spontaneous magnetization M>0. However, at high temperatures, the disordering effect of temperature dominates and the system is paramagnetic with M=0. The temperature of phase transition, namely, the critical temperature T_c is 4. However, although the mean theory can illustrate the phase transition of ferromagnetism, it failed to give the correct critical temperature. In addition, at critical temperature, the velocity of M going  to zero at T_c is incorrect too.
##Monte Carlo Method
![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/2016-12-28_173902.png)
We investigate the variation of the magnetization as a function of Monte Carlo steps for specific temperatures.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/8.2.py)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/mc%20M_time.png)

This picture shows the ferromagnetism phenomenon. However, there are statistical fluctuations so we need to average the magnetization over time(Monte Carlo step) and investigate its variation with temperature. Our code needs a few changes.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/8.3.py)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/mc%20M_T%201.png)

We find that the critical temperature predicts by the Monte Carlo method is less than the one mean theory did. In addtion, although this picture cannot show the velocity of M approaching to zero, large-scale Monte Carlo simulations yield a more exact value than the mean field theory did.

Besides magnetization, we can also investigate other properties of the system.
###Energy and specific heat.
Energy can be easily obtained from the energy function while specific heat can be calculated from the relation C=dE/dT.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/energy.py)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/E_T.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/specific%20heat.png)

At low temperatures, with the spins fully aligned, every spin has an interaction energy of -J with each of its four nearest neighbors. The total energy at T=0 should thus be -4NJ/2, where N is the number of spins and the factor 2 is inserted since we have counted each pair of spins twice. On the other hand, at very high temperatures the spins will be randomly oriented, so on average each spin will have two neighbors that are alighed parallel and two are antiparallel. The thermal average of the total energy in this limit will thus be zero. The temperature in our solution is not such high so the energy is far from 0. As we can anticipate, the specific heat C exhibits a large peak in the vicinity of T_c where the energy changes fastest.
###Correlation function
When we considered the variation of the energy with temperature, we noted that the behavior of <.E> above T_c implies that there must be significant correlations in the relative alignment of neighboring spins since for one spin, two of its neighboring spins are parallel and others are antiparallel with the center spin on average.

Consider a paricular spin, call it s_0, and assume that it points up. Let us examine the alignment of the four neighbors of s_0. Since s_0=+1, the neighbors will have a lower energy if they also point up. Even though the temperature may be above T_c so that the average alignment over the entire system is zero, these four neighbors will still have a higher probability of being aligned parallel to s_0, as opposed to being antiparallel. The degree to which they are parallel will depend on temperature, but it will not be zero even above T_c

The tendency to be correlated can be measured using the correlation function

f(i)=<.s_0 s_i>
 
where s_i is a spin that is located i lattice sites away from s_0, and the angular brackets again denote a thermal average that can be computed by averageing over the microstates generated by the Monta Carlo method. For a 20 times 20 lattice, we select a spin at the center and calculated the correlation function up to i=  at different temperatures.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/si.py)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/Correlations.png)

From this picture, we find that at low temperatures, the direction of the spins are highly correlated or paralleled even not neighboring spins. As the temperature increases, the correlation function decreases but the value for neighboring spins does not vanish.
##Cases with external magnetic field.
In this section, we include the effect of a magnetic field. The Monte Carlo method can be used as described above, the only difference being that the energy for flipping a spin must include the energy gained or lost to the field. So changing the program, we investigate the magnetization as a function of H with fixed temperatures.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/H1.py)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/1.0%202.0%202.25.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/3%205.png)

At T=1.0 and with H<.0 ,the magnetization is large and negative. We already know that at this temperature the spins will be nearly fully aligned even without the field. Here the field serves only to determine the direction of M and this is why M changes sign abruptly when H is increased through zero. This dicontinuous change of M is an indicator of a *first-order transition*. Above T_c the spontaneous magnetization vanishes, so there can be no discontinuity in M as the field is swept through zero, and hence no first-order phase transition. At a very high temperature, the spins show paramagnetism and the magnetic field has a very limited effect.

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/T%3D100.png)

Next, we study the behavior of magnetization as a function of temperature with external magnetic field.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/H2.py)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/T_M%20H%20new.png)

From this, we find that the appearance of external magnetic field will erase the discontinuity of M. This is because the spins have a tendency to be paralleled with the direction of the magnetic field. So there won't be an abrupt transition at critical temperature. We can speculate that in a strong magnetic field the magnetization will be stable at low temperatures.

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/T_M%20H.png)

With a very strong field, the spin will align to according to the direction of the field, which requires a high temperature to disturb the ordering alignment.
##Conclusion
Ising model is a simple but effective model to illustrate the ferromanetism. Plus, the mean field theory and the Monte Carlo mothod can both predict a phase transition for Ising model. However, the mean field theory failed to give an exact value of the critical temperature where the transition occurs and the exact velocity of M approaching 0, while the Monte Carlo succeeded doing these. In addition, other quantities such as internal energy and specific heat and the magnetization and magnetic field relation can also be investigated by Monte Carlo method.
##Reference
