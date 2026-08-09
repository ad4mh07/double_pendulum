import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(pendulum, fade=100):
    theta1 = pendulum.theta1
    theta2 = pendulum.theta2
    l1 = pendulum.l1
    l2 = pendulum.l2
    
    x1 = l1 * np.sin(theta1)
    y1 = -l1 * np.cos(theta1)
    x2 = x1 + l2 * np.sin(theta2)
    y2 = y1 - l2 * np.cos(theta2)

    fig1, ax1 = plt.subplots()
    ax1.set_xlim(-l1 - l2 - 0.5, l1 + l2 + 0.5)
    ax1.set_ylim(-l1 - l2 - 0.5, l1 + l2 + 0.5)
    ax1.set_aspect('equal')

    rod1,   = ax1.plot([], [], color='black')
    rod2,   = ax1.plot([], [], color='black')
    trace,  = ax1.plot([], [], color='blue', alpha=0.3, linewidth=0.8)
    pivot,  = ax1.plot([0], [0], color='black', marker='o')
    bob1,   = ax1.plot([], [], color='black', marker='x')
    bob2,   = ax1.plot([], [], color='black', marker='x')
    timer   = ax1.text(0.02, 0.95, '', transform=ax1.transAxes, fontsize=10)

    def update1(frame):
        rod1.set_data([0, x1[frame]], [0, y1[frame]])
        rod2.set_data([x1[frame], x2[frame]], [y1[frame], y2[frame]])
        trace.set_data(x2[max(0, frame-fade):frame+1], y2[max(0, frame-fade):frame+1])
        bob1.set_data([x1[frame]], [y1[frame]])
        bob2.set_data([x2[frame]], [y2[frame]])
        timer.set_text(f"t = {pendulum.time[frame]:.2f}s") #pendulun.time = sol.t = t_eval
        return rod1, rod2, trace, bob1, bob2, timer

    ani1 = animation.FuncAnimation(fig=fig1, func=update1, frames=len(theta1), interval=10, blit=True)

    plt.show()