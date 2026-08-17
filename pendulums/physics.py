import numpy as np

def system(t, y, pendulum):
        m1 = pendulum.m1
        m2 = pendulum.m2
        l1 = pendulum.l1
        l2 = pendulum.l2
        g = pendulum.g
        
    
        θ1, ω1, θ2, ω2 = y #θ1, θ1', θ2, θ2'
        
        delta=θ1-θ2

        den1 = l1 * (2*m1 + m2 - m2*np.cos(2*delta))

        den2 = l2 * (2*m1 + m2 -m2*np.cos(2*delta))

        dθ1_dt = ω1
        dω1_dt = (-g*(2*m1 + m2)*np.sin(θ1) - m2*g*np.sin(θ1-2*θ2) - 2*m2*np.sin(delta)*(ω2**2 * l2 + ω1**2 *l1 *np.cos(delta))) / den1

        dθ2_dt = ω2
        dω2_dt = (2*np.sin(delta) * (ω1**2 *l1 *(m1+m2) + g*(m1+m2)*np.cos(θ1) + ω2**2 *l2 *m2 *np.cos(delta))) / den2

        return [dθ1_dt, dω1_dt, dθ2_dt, dω2_dt]
