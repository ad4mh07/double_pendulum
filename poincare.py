import numpy as np
import matplotlib.pyplot as plt

def poincare(pendulum):
    t = pendulum.time
    theta1 = pendulum.theta1
    theta2 = pendulum.theta2
    omega1 = pendulum.omega1
    omega2 = pendulum.omega2

    # Wrap theta1 into [-pi, pi] 
    # varibale_w indiactes it is wrapped, variable_s indicates it is a section/selection of points 
    theta1_w = np.mod(theta1 + np.pi, 2 * np.pi) - np.pi

    theta2_s, omega2_s= [], []

    #loop to find changes in sign, ie crossings
    for i in range(len(t) - 1):
        if theta1_w[i] == 0:
            crossing = True
            frac = 0.0
        elif theta1_w[i] < 0.0 and theta1_w[i + 1] > 0.0:
            crossing = True
            frac = -theta1_w[i] / (theta1_w[i + 1] - theta1_w[i])   # linear interpolation fraction
        else:
            crossing = False

        if crossing and omega1[i] > 0:  # only keep upward crossings
            th2 = theta2[i] + frac * (theta2[i + 1] - theta2[i])
            om2 = omega2[i] + frac * (omega2[i + 1] - omega2[i])
            theta2_s.append(th2)
            omega2_s.append(om2)

    theta2_s = np.array(theta2_s)
    omega2_s = np.array(omega2_s)

    theta2_w = np.mod(theta2_s + np.pi, 2 * np.pi) - np.pi

    fig, ax = plt.subplots(figsize=(7, 6))
    ax.scatter(theta2_w, omega2_s, s=2, c='k', alpha=0.6)
    ax.set_xlabel('theta_2')
    ax.set_ylabel('omega_2')
    ax.set_title('Poincaré section')
    plt.show()

    