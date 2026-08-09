#from pendulums.double_pendulum import double_pendulum
import matplotlib.pyplot as plt
import numpy as np

def trajectory(pendulum):
    l1 = pendulum.l1
    l2 = pendulum.l2
    theta1 = pendulum.theta1
    theta2 = pendulum.theta2

    x = l1 * np.sin(theta1) + l2 *np.sin(theta2)

    y = l2 * np.cos(theta1) + l2 * np.cos(theta2)

    plt.plot(x,y)
    plt.show()

