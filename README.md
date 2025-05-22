# Computational Fluid Dynamics

There are various programs I wrote for simulating different problems in Fluid Dynamics, mostly based on numerical simulation of the Navier-Stokes equations in simplified scenarios like incompressible flows. I use MATLAB and Python for writing these codes. 

## 1. 2D smoke flow using Python

This Python code uses the phiflow model and the Boussinesq approximation. The Boussinesq approximation is a simplifying assumption often used in fluid dynamics, particularly in the study of buoyancy-driven flows such as convection. It assumes that the density variations in the fluid are negligible so that the fluid can be considered incompressible. This allows for the simplification of the Navier-Stokes equations, making them more amenable to numerical solution. The code solves a Poisson equation with the boundary conditions of the domain, and updates the old velocity field with the computed pressure gradient.

All the differentiable operators used in the Navier-Stokes equation are already available in [phiflow](https://tum-pbs.github.io/PhiFlow/) package.

The incompressible form of **Navier-Stokes equation** is given by:\
\
$$\rho \frac{d \mathbf{v}}{dt} = - \mathbf{\nabla} P + \rho \textbf{g} + \mu \nabla^2 \mathbf{v}$$

### Step 0: Installing phiflow

Run this command in the Python interface you're using:
```
!pip install --upgrade --quiet phiflow==3.1
#!pip install --upgrade --quiet git+https://github.com/tum-pbs/PhiFlow@develop
```

### Step 1: Setting up the domain and Marker Grid
\
I'm creating a first CenteredGrid here, which is initialized by a Sphere geometry object. This will represent the inflow region where hot smoke is generated. I have defined a Box of size 160 x 128. This is the physical scale in terms of spatial units in the simulation, i.e., a velocity of magnitude 1 will move the smoke density by 1 unit per 1 time unit.

Below are the different kinds of extrapolation schemes used in the code. Please look into this in details from [here](https://tum-pbs.github.io/PhiFlow/Staggered_Grids.html).

![Extrapolation](extrapolation.png)

The inflow sphere is located at x = 30 along the first axis, and y = 15 (within the domain box).

Next, create grids for the quantities you want to simulate (velocity and smoke density).

### Step 2: Forward Flow Time Step
\
By repeatedly calling the step function, the time evolution of the hot smoke can be studied.

![Smokerise](markergrid.png)


The hot plume is starting to rise. Because of the inflow being located off-center to the left (with x position 30), the plume will curve towards the right when it hits the top wall of the domain.


![Forward Flow Time evolution of the Smoke](forward_flow_time_step.png)


This is the time evolution (over 20 secs) of the hot smoke that moves upwards.

### Step 3: Velocity Field
\
You can also take a look at the velocities.

![x-component of velocity field](v_x_profile.png)


![y-component of velocity field](v_y_profile.png)


