import matplotlib.pyplot as plt
import numpy as np

def trajectory(pendulum):
    #plots the trace of the end mass

    l1 = pendulum.l1
    l2 = pendulum.l2
    theta1 = pendulum.theta1
    theta2 = pendulum.theta2

    x1 = l1 * np.sin(theta1)
    y1 = -l1 * np.cos(theta1)
    x2 = x1 + l2 * np.sin(theta2)
    y2 = y1 - l2 * np.cos(theta2)

    plt.plot(x2,y2)

    plt.title("Trajectory: the trace of the end mass")
    plt.show()
