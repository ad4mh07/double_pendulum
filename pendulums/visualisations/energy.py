
import numpy as np
import matplotlib.pyplot as plt

def energy(pendulum):
    theta1 = pendulum.theta1
    theta2 = pendulum.theta2
    l1 = pendulum.l1
    l2 = pendulum.l2
    omega1 = pendulum.omega1
    omega2 = pendulum.omega2
    m1 = pendulum.m1
    m2 = pendulum.m2
    g = pendulum.g
    t = pendulum.time

    #calulating v^2 of both masses- resolving horiz. and vert. coponents, sqr then add them 
    #mass 2 (the end mass) moves beyong v1, so need to add v1 on.

    v1sq = (l1 * omega1 * np.cos(theta1) ) **2 + (l1 * omega1 * np.sin(theta1)) **2

    v2sq = (l1 * omega1 * np.cos(theta1) + l2 * omega2 * np.cos(theta2)) **2 + \
    (l1 * omega1 * np.sin(theta1) + l2 * omega2 * np.sin(theta2)) **2


    E_K1 = 0.5 * m1 * v1sq
    E_K2 = 0.5 * m2 * v2sq

    y1 = -l1 * np.cos(theta1)
    y2 = y1 - l2 * np.cos(theta2)
    
    E_GP1 = m1 * g * y1
    E_GP2 = m2 * g * y2

    E_total = E_K1 + E_K2 + E_GP1 + E_GP2
 
    plt.plot(t,E_K1, color='orange', label='Kinetic energy, pivot 1')
    plt.plot(t,E_K2, color='pink', label='Kinetic energy, pivot 2')

    plt.plot(t,E_GP1, color='lime', label='Grav. pot. energy, pivot 1')
    plt.plot(t,E_GP2, color='cyan', label='Grav. pot. energy, pivot 2')

    plt.plot(t,E_total, color='white', label='Total energy')

    plt.title('Energy stores over time')
    plt.xlabel("Time (s)")
    plt.ylabel("Angle (rad)")

    plt.legend()
    plt.tight_layout()
    plt.show()


