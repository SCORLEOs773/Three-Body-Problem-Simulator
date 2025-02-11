import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import matplotlib.animation as animation

# Gravitational constant (normalized)
G = 1

# Function to compute derivatives
def three_body_equations(t, state, masses):
    x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3 = state
    m1, m2, m3 = masses
    
    r12 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2) + 1e-5  # Avoid division by zero
    r13 = np.sqrt((x3 - x1)**2 + (y3 - y1)**2) + 1e-5
    r23 = np.sqrt((x3 - x2)**2 + (y3 - y2)**2) + 1e-5
    
    ax1 = G * (m2 * (x2 - x1) / r12**3 + m3 * (x3 - x1) / r13**3)
    ay1 = G * (m2 * (y2 - y1) / r12**3 + m3 * (y3 - y1) / r13**3)
    
    ax2 = G * (m1 * (x1 - x2) / r12**3 + m3 * (x3 - x2) / r23**3)
    ay2 = G * (m1 * (y1 - y2) / r12**3 + m3 * (y3 - y2) / r23**3)
    
    ax3 = G * (m1 * (x1 - x3) / r13**3 + m2 * (x2 - x3) / r23**3)
    ay3 = G * (m1 * (y1 - y3) / r13**3 + m2 * (y2 - y3) / r23**3)
    
    return [vx1, vy1, ax1, ay1, vx2, vy2, ax2, ay2, vx3, vy3, ax3, ay3]

# Initial conditions: positions (x, y) and velocities (vx, vy)
initial_conditions = [-1, 0, 0, -0.5, 1, 0, 0, 0.5, 0, 1, 0.5, -0.5]
masses = [1, 1.5, 2]  # Different masses

t_span = (0, 10)  # Time range
t_eval = np.linspace(0, 10, 1000)  # Time steps

# Solve the system
solution = solve_ivp(three_body_equations, t_span, initial_conditions, t_eval=t_eval, args=(masses,), method='RK45')

# Extract positions
x1_sol, y1_sol = solution.y[0], solution.y[1]
x2_sol, y2_sol = solution.y[4], solution.y[5]
x3_sol, y3_sol = solution.y[8], solution.y[9]

# Create 2D animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")
ax.set_title("Three-Body Simulation in 2D")
body1, = ax.plot([], [], 'ro', markersize=8)
body2, = ax.plot([], [], 'bo', markersize=8)
body3, = ax.plot([], [], 'go', markersize=8)
traj1, = ax.plot([], [], 'r-', alpha=0.5)
traj2, = ax.plot([], [], 'b-', alpha=0.5)
traj3, = ax.plot([], [], 'g-', alpha=0.5)

def init():
    body1.set_data([], [])
    body2.set_data([], [])
    body3.set_data([], [])
    traj1.set_data([], [])
    traj2.set_data([], [])
    traj3.set_data([], [])
    return body1, body2, body3, traj1, traj2, traj3

def update(frame):
    body1.set_data([x1_sol[frame]], [y1_sol[frame]])
    body2.set_data([x2_sol[frame]], [y2_sol[frame]])
    body3.set_data([x3_sol[frame]], [y3_sol[frame]])
    traj1.set_data(x1_sol[:frame], y1_sol[:frame])
    traj2.set_data(x2_sol[:frame], y2_sol[:frame])
    traj3.set_data(x3_sol[:frame], y3_sol[:frame])
    return body1, body2, body3, traj1, traj2, traj3

ani = animation.FuncAnimation(fig, update, frames=len(t_eval), init_func=init, interval=20, blit=False)
plt.show()
