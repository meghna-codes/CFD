# Computational Fluid Dynamics

There are various programs I wrote for simulating different problems in Fluid Dynamics, mostly based on numerical simulation of the Navier-Stokes equations in simplified scenarios like incompressible flows. I use MATLAB and Python for writing these codes. 

## 1. 2D smoke flow using Python

The incompressible form of **Navier-Stokes equation** is given by:\
\
$$\rho \frac{d \mathbf{v}}{dt} = - \mathbf{\nabla} P + \rho \textbf{g} + \mu \nabla^2 \mathbf{v}$$

![Forward Flow Time evolution of the Smoke](/assets/images/forward_flow_time_step.png)

This is the time evolution of a hot plume of viscous gas that moves upwards. This Python code uses the phiflow model and the Boussinesq approximation. The Boussinesq approximation is a simplifying assumption often used in fluid dynamics, particularly in the study of
buoyancy-driven flows such as convection. It assumes that the density variations in the fluid are relatively small compared to a reference density. This allows for the simplification of the Navier-Stokes equations, making them more amenable to numerical solution. 

Code solves a Poisson equation with the boundary conditions of the domain, and updates the old velocity field with the computed pressure gradient.

