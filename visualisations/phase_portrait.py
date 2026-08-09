import matplotlib.pyplot as plt
import numpy as np

def phase_portrait(pendulum):
    theta1 = pendulum.theta1
    theta2 = pendulum.theta2
    omega1 = pendulum.omega1
    omega2 = pendulum.omega2

    fig, ax = plt.subplots(2, 1, figsize=(9, 6))
    fig.suptitle('Phase Portraits')

    ax[0].plot(theta1, omega1)
    ax[0].set_xlabel('theta1')
    ax[0].set_ylabel('omega1')

    ax[1].plot(theta2, omega2)
    ax[1].set_xlabel('theta2')
    ax[1].set_ylabel('omega2')

    plt.tight_layout()
    plt.show()

    
