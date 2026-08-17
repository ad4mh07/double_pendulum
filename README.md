# Double Pendulum Simulator

Short description of what the project does and what makes it interesting.

## Overview

Brief explanation of a double pendulum and why it is a useful example of
nonlinear dynamics and chaotic behaviour.

Mention that the simulator:
- Numerically solves the equations of motion
- Uses `solve_ivp`
- Produces animations and visualisations
- Demonstrates chaotic behaviour
- Allows different physical parameters and initial conditions

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
double-pendulum/
│
├── pendulums/
│   ├── __init__.py
│   ├── double_pendulum.py
│   ├── physics.py
│   ├── animation.py
│   │
│   └── visualisations/
│       ├── angles.py
│       ├── energy.py
│       ├── phase.py
│       ├── poincare.py
│       └── trajectory.py
│
├── examples/
│   └── example1.py
│
├── images/
│   ├── animation.gif
│   ├── phase_portrait.png
│   ├── poincare_section.png
│   └── trajectory.png
│
├── requirements.txt
├── README.md
└── LICENSE
