# Solving differential equations in C

The aim of this project is to solve <strong>non-linear, differential equations</strong> (N-LDEs) using C. 

In order to make this project a little more interesting, we are going to solve a specific set of N-LDEs, namely the <strong>Lotka-Volterra</strong> equations. These are the basis for simulating a predator-prey system where the populations change with time, as seen below:

$\dot{x}\left ( x,y \right ) = \alpha x - \beta xy - \kappa x^2$

$\dot{y}\left ( x,y \right ) = \delta x - \gamma y - \lambda y^2$

The equations above express how the rate of change of population for both prey $(\dot{x})$ and predators $(\dot{y})$, within a binary-system, is dependant on a number of parameters, including, the prey's birth rate $(\alpha)$, predators eating prey $(\beta)$, predator death rate $(\gamma)$, the coupling relation between predator population growth and prey population size $(\delta x)$, the effects of the local environment on the prey population $(\kappa)$ and the effects of the local environment on the predator population $(\lambda)$.

As the Lotka-Volterra equations are first order N-LDEs, they cannot be solved directly when using computer code. Therefore, they have to be solved iteratively, in this case using the <strong>Runge-Kutta method</strong> written in C (equations and code in Report.pdf).

In order to validate the C code and determine validity of the model, predetermined values for the $\alpha$, $\beta$, $\delta$, $\gamma$ coefficients and the initial population values were derived from actual data taken on the populations of the Canadian lynx and snowshoe hares in the boreal forests of North America. Below are some of the results from the report:

<img src="/latex_docs/figure1_time.png"/><img src="/latex_docs/figure1_phase.png"/>
<p align="center"><i>Figure 1. Model of the Canadian lynx-snowshoe hare preditor-prey system using scientific data. The left hand side shows the populations of both animals as a function of time. The right hand side shows the phase diagram of both populations. The closed loop indicates the system is in a stable state. Note $\kappa = \lambda = 0$ </i></p>

<img src="/latex_docs/figure3_time.png"/><img src="/latex_docs/figure3_phase.png"/>
<p align="center"><i>Figure 3. Here we have set $\kappa$ and $\lambda$ to positive values in order to produce a model which is biased in favour of the predator.</i></p>

To summarise, this project succesfully 







