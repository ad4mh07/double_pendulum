import matplotlib.pyplot as plt
import numpy as np

def angles(pendulum):
    theta1 = pendulum.theta1 
    theta2 = pendulum.theta2
    t=pendulum.time
    
    plt.style.use("dark_background") 
    plt.plot(t,theta1, color='orange', label='theta1')
    plt.plot(t,theta2, color= 'cyan', label='theta2')

    plt.title('Angles over time')
    plt.xlabel("Time (s)")
    plt.ylabel("Angle (rad)")

    plt.legend()
    plt.tight_layout()
    plt.show()

def omegas(pendulum):
    omega1 = pendulum.omega1
    omega2 = pendulum.omega2
    t=pendulum.time

    plt.plot(t,omega1, color='pink', label='omega1')
    plt.plot(t,omega2, color= 'cyan', label='omega2')

    plt.title('Angular velecities over time')
    plt.xlabel("Time (s)")
    plt.ylabel("Angular velecity (rad/s)")

    plt.legend()
    plt.tight_layout()
    plt.show()
