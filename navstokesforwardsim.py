#Navier-Stokes forward simulation using Phiflow
from phi.flow import *  
import pylab

#caps for constants
DT = 1.5 #times step
NU = 0.01 #kinematic viscosity

INFLOW = CenteredGrid(Sphere(center=tensor([30,15], channel(vector='x,y')), radius=10), extrapolation.BOUNDARY, x=32, y=40, bounds=Box(x=(0,80),y=(0,100))) * 0.2

#creating staggered grids
smoke = CenteredGrid(0, extrapolation.BOUNDARY, x=32, y=40, bounds=Box(x=(0,80),y=(0,100)))  # sampled at cell centers
velocity = StaggeredGrid(0, extrapolation.ZERO, x=32, y=40, bounds=Box(x=(0,80),y=(0,100)))  # sampled in staggered form at face centers 

#state of fluid system advances by dt
def step(velocity, smoke, pressure, dt=1.0, zhi =1.0): #zhi=buoyancy factor
    smoke = advect.semi_lagrangian(smoke, velocity, dt) + INFLOW
    buoyant_force = (smoke * (0, zhi)).at(velocity)  # resamples smoke to velocity sample points
    velocity = advect.semi_lagrangian(velocity, velocity, dt) + dt * buoyant_force
    velocity = diffuse.explicit(velocity, NU, dt)
    velocity, pressure = fluid.make_incompressible(velocity)
    return velocity, smoke, pressure

velocity, smoke, pressure = step(velocity, smoke, None, dt=DT)

print("Max. velocity and mean marker density: " + format([math.max(velocity.values),math.mean(smoke.values)]))

pylab.imshow(np.asarray(smoke.values.numpy('y,x')), origin='lower', cmap='magma')

#time evolution
for time_step in range(10):
    velocity, smoke, pressure = step(velocity, smoke, pressure, dt=DT)
    print('Computed frame {}, max velocity {}'.format(time_step , np.asarray(math.max(velocity.values))))

pylab.imshow(smoke.values.numpy('y,x'), origin='lower', cmap='Spectral')

steps = [[smoke.values, velocity.values.vector[0], velocity.values.vector[1]]]
for time_step in range(20):
  if time_step<3 or time_step%10==0: 
    print('Computing time step %d' % time_step)
  velocity, smoke, pressure = step(velocity, smoke, pressure, dt=DT)
  if time_step%5==0:
    steps.append([smoke.values, velocity.values.vector[0], velocity.values.vector[1]])

fig, axes = pylab.subplots(1, len(steps), figsize=(16, 5))
for i in range(len(steps)):
    axes[i].imshow(steps[i][0].numpy('y,x'), origin='lower', cmap='Spectral')
    axes[i].set_title(f"d at t={i*5}")

#2D flow
fig, axes = pylab.subplots(1, len(steps), figsize=(16, 5))
for i in range(len(steps)):
    axes[i].imshow(steps[i][1].numpy('y,x'), origin='lower', cmap='Spectral')
    axes[i].set_title(f"$v_x$ at t={i*5}") #x component of velocity
    
fig, axes = pylab.subplots(1, len(steps), figsize=(16, 5))
for i in range(len(steps)):
    axes[i].imshow(steps[i][2].numpy('y,x'), origin='lower', cmap='Spectral')
    axes[i].set_title(f"$v_y$ at t={i*5}") #y component of velocity