from pendulums.double_pendulum import double_pendulum

from ..visualisations.animate import animate
from ..visualisations.trajectory import trajectory
from ..visualisations.angles import angles
from ..visualisations.angles import omegas
from ..visualisations.energy import energy
from ..visualisations.phase_portrait import phase_portrait
from ..visualisations.poincare import poincare
from ..visualisations.lyapunov import lyapunov

import numpy as np

model = double_pendulum(m1=5, m2=5, l1=3, l2=3, θ1_init=3/2 * np.pi, θ2_init=np.pi/2, time=[0,30])

model.solve()

animate(model)

trajectory(model)

angles(model)

omegas(model)

energy(model)

phase_portrait(model)

poincare(model)

lyapunov(model, 100)
