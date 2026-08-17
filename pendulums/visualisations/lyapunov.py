from pendulums.double_pendulum import double_pendulum
import numpy as np
from scipy.integrate import solve_ivp
from pendulums.physics import system
import matplotlib.pyplot as plt

def solve_briefly(self, t_span, initial_conditions):
        n_points = int(100 * (t_span[1] - t_span[0]))
        t_eval = np.linspace(t_span[0], t_span[1], n_points)

        sol = solve_ivp(lambda t, y: system(t, y, self), t_span, initial_conditions, t_eval=t_eval, method=self.method, rtol=1e-8, atol=1e-8)
        
        return sol.y[:, -1]  # final [θ1, ω1, θ2, ω2]


def lyapunov(p1, N, dt=0.1, delta=1e-8):
    # p1: reference pendulum
    # N: number of renormalization steps
    # dt: duration of each step (seconds)
    # delta: initial θ1 offset

    #Initialisations:
    ratios=[]
    p2=double_pendulum(m1=p1.m1, m2=p1.m2, l1=p1.l1, l2=p1.l2, θ1_init=p1.θ1_init+delta, θ2_init=p1.θ2_init, time=p1.time) 

    

    #The first time, this the initial conditions.
    #During the loop, this saves the state of the pendulum, to be used as 'inital' conditions for the next call of briefly_solve()
    #Reference means p1, pertubation means p2
    state_ref = np.array([p1.θ1_init, 0.0, p1.θ2_init, 0.0])
    state_pert = np.array([p2.θ1_init, 0.0, p2.θ2_init, 0.0])

    for i in range(N):
        #This is the span were going from, ie from 0, in intervals of dt
        t_span = (i * dt, (i + 1) * dt)

        state_ref_new = solve_briefly(p1, t_span, state_ref)
        state_pert_new = solve_briefly(p2, t_span, state_pert)

        d1 = np.linalg.norm(state_pert_new - state_ref_new)
        ratios.append(np.log(d1 / delta))

        #Renormalisation: calulate the vector between the 2 states, direction.
        #Make the direction vector unit unit length by / by d1, then scale it up to delta. Add it onto the new reference state (/vector) to update the pertubation state
        #Update the reference state/vector

        direction = state_pert_new - state_ref_new
        state_pert = state_ref_new + direction * (delta / d1) 
        state_ref = state_ref_new

    lyapunov_exponent = np.sum(ratios) / (N * dt)
    print(f"Lyapunov's exponent is: {lyapunov_exponent}")

    #Plotting
    running_lambda = np.cumsum(ratios) / (dt * np.arange(1, N + 1))
    x_axis = np.linspace(dt, N * dt, N)

    fig, ax = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

    ax[0].plot(x_axis, ratios)
    ax[0].set_xlabel("Time")
    ax[0].set_ylabel("log(d1/delta) per step")
    ax[0].set_title("Raw (per-step) ratios")

    ax[1].plot(x_axis, running_lambda)
    ax[1].axhline(lyapunov_exponent, color='red', linestyle='dashed', label='Final estimate')
    ax[1].set_ylabel("λ estimate")
    ax[1].set_xlabel("Time")
    ax[1].set_title("Convergence of Lyapunov exponent estimate")
    ax[1].legend()
    
    plt.tight_layout()
    plt.show()

   

    return lyapunov_exponent, ratios
