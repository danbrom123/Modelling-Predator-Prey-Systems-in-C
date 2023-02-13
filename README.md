# Modelling-Predator-Prey-Systems-in-C

The aim of this project is to solve non-linear, differential equations (N-LDEs) using C. 

In order to make this project a little more interesting, we are going to solve a specific set of N-LDEs, namely the Lotka-Volterra equations. These equations are the basis for simulating a predator-prey system. The populations change with time and are expressed below as:

$\dot{x}\left ( x,y \right ) = \alpha x - \beta xy - \kappa x^2$

$\dot{y}\left ( x,y \right ) = \delta x - \gamma y - \lambda y^2$.

These express how the rate of change of population for both prey $(\dot{x})$ and predators $(\dot{y})$, within a binary-system, is dependant on a number of parameters, including, the prey's birth rate $(\alpha)$, predators eating prey $(\beta)$, predator death rate $(\gamma)$, the coupling relation between predator population growth and prey population size $(\delta x)$, the effects of the local environment on the prey population $(\kappa)$ and the effects of the local environment on the predator population $(\lambda)$.

As the Lotka-Volterra equations are first order N-LDEs, they cannot be solved directly when using computer code. They therefore have to be solved iteratively, in this case using the Runge-Kutta method (see Report.pdf).





