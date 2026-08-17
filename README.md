# Double Pendulum Simulator

Short description of what the project does and what makes it interesting.

My project numerically approximates the behaviour of a customisable double pendulum, and uses this solution to create various visualisations. This project interests me as it covers new visualisation techniques, and has expanded my knowledge on integrators in python and file structures and backend systems for GitHub.

## Overview

A double pendulum has a fixed end point at the centre, attached to a  (weightless) rod attached to a mass / pivot, attached to another weightless rod attached to a mass at the end. This is a great example of chaos theory, as a tiny change in the starting conditions creates massive and unpredictable changes in motion. 

My simulation uses 'solve_ivp' to numerically solve the equations, finding approximations for the angle and angular velocities for both pivots. 

## Physics

### Equations of Motion

Explain the state vector:

y = [θ₁, ω₁, θ₂, ω₂]

Then include the two equations of motion, preferably using LaTeX.

### Numerical Method

Explain:
- ODE solver used (`RK45`)
- Integration time
- Tolerances (`rtol`, `atol`)
- Why numerical methods are required

## Project Structure

```text
double_pendulum/
|
|-- pendulums/
|   |-- __init__.py
|   |-- double_pendulum.py
|   |-- physics.py
|   |-- animation.py
|   
|-- visualisations/
|   |--__init__.py
|   |--angles.py
|   |-- animate.py
|   |-- energy.py
|   |-- lyapunov.py
|   |-- phase_portrait.py
|   |--poincare.py
|   |-- trajectory.py
|
|-- examples/
|   |-- example1.py
|
|-- figures/
|   |--angles.png
|   |-- animate.gif
|   |-- energy.png
|   |-- lyapunov.png
|   |-- phase_portrait.png
|   |--poincare.png
|   |-- trajectory.png
|
|-- README.md
|-- pyproject.toml
|-- requirements.txt
```text

##Running the 
