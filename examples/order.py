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

model = b = double_pendulum(m1=1, m2=1, l1=1, l2=1, θ1_init=np.pi/6, θ2_init=np.pi/6, time=[0,1000])
model.solve()

"""animate(model)

trajectory(model)

angles(model)

omegas(model)

energy(model)

phase_portrait(model)

poincare(model)

lyapunov(model, 100)
"""

poincare(model)