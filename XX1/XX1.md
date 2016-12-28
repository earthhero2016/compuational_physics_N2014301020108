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

As the picture shows, at low temperature, there is a spontaneous magnetization M>0. However, at high temperatures, the disordering effect of temperature dominates and the system is paramagnetic with M=0. The temperature of phase transition, namely, the critical temperature T_c is 4. However, although the mean theory can illustrate the phase transition of ferromagnetism, it failed to give the correct critical temperature. In addition, at critical temperature, dM/dT is infinite. The singular property predicted by the mean field theory is incorrect either.
##Monte Carlo Method
![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/2016-12-28_173902.png)
We investigate the variation of the magnetization as a function of Monte Carlo steps for specific temperatures.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/8.2.py)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/XX1/mc%20M_time.png)
