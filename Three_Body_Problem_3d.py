import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Gravitational constant (normalized)
G = 1

# Function to compute derivatives
def three_body_equations(t, state, masses):
    x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2, x3, y3, z3, vx3, vy3, vz3 = state
    m1, m2, m3 = masses
    
    r12 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) + 1e-5  # Avoid division by zero
    r13 = np.sqrt((x3 - x1)**2 + (y3 - y1)**2 + (z3 - z1)**2) + 1e-5
    r23 = np.sqrt((x3 - x2)**2 + (y3 - y2)**2 + (z3 - z2)**2) + 1e-5
    
    ax1 = G * (m2 * (x2 - x1) / r12**3 + m3 * (x3 - x1) / r13**3)
    ay1 = G * (m2 * (y2 - y1) / r12**3 + m3 * (y3 - y1) / r13**3)
    az1 = G * (m2 * (z2 - z1) / r12**3 + m3 * (z3 - z1) / r13**3)
    
    ax2 = G * (m1 * (x1 - x2) / r12**3 + m3 * (x3 - x2) / r23**3)
    ay2 = G * (m1 * (y1 - y2) / r12**3 + m3 * (y3 - y2) / r23**3)
    az2 = G * (m1 * (z1 - z2) / r12**3 + m3 * (z3 - z2) / r23**3)
    
    ax3 = G * (m1 * (x1 - x3) / r13**3 + m2 * (x2 - x3) / r23**3)
    ay3 = G * (m1 * (y1 - y3) / r13**3 + m2 * (y2 - y3) / r23**3)
    az3 = G * (m1 * (z1 - z3) / r13**3 + m2 * (z2 - z3) / r23**3)
    
    return [vx1, vy1, vz1, ax1, ay1, az1, vx2, vy2, vz2, ax2, ay2, az2, vx3, vy3, vz3, ax3, ay3, az3]

# Initial conditions: positions (x, y, z) and velocities (vx, vy, vz)
# initial_conditions = [
#                       -1, 0, 0, 0, -0.5, 0, # Body 1
#                       1, 0, 0, 0, 0.5, 0,   # Body 2
#                       0, 1, 0, 0.5, -0.5, 0 # Body 3
#                       ]

# initial_conditions = [
#                       -2, 0, 0, 0, -0.5, 0, # Body 1
#                       2, 0, 0, 0, 0.5, 0,   # Body 2
#                       0, 2, 0, 0.5, -0.5, 0 # Body 3
#                       ]

# #Triangle Formation
# initial_conditions = [
#                       -1, -1, 0, 0.2, 0.3, 0, # Body 1
#                       1, -1, 0, -0.2, -0.3, 0,   # Body 2
#                       0, 1, 0, 0, -0.5, 0 # Body 3
#                       ]

#z-axis offset
initial_conditions = [
                      -1, 0, 1, 0, -0.5, 0, # Body 1
                      1, 0, 1, 0, 0.5, 0,   # Body 2
                      0, 1, 0, 0.5, -0.5, 0 # Body 3
                      ]

masses = [1, 1.5, 2]  # Different masses

t_span = (0, 10)  # Time range
t_eval = np.linspace(0, 10, 1000)  # Time steps

# Solve the system
solution = solve_ivp(three_body_equations, t_span, initial_conditions, t_eval=t_eval, args=(masses,), method='RK45')

# Extract positions
x1_sol, y1_sol, z1_sol = solution.y[0], solution.y[1], solution.y[2]
x2_sol, y2_sol, z2_sol = solution.y[6], solution.y[7], solution.y[8]
x3_sol, y3_sol, z3_sol = solution.y[12], solution.y[13], solution.y[14]

# Create 3D animation
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_zlim(-2.5, 2.5)
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")
ax.set_zlabel("Z Position")
ax.set_title("Three-Body Simulation in 3D")
body1, = ax.plot([], [], [], 'ro', markersize=8)
body2, = ax.plot([], [], [], 'bo', markersize=8)
body3, = ax.plot([], [], [], 'go', markersize=8)
traj1, = ax.plot([], [], [], 'r-', alpha=0.5)
traj2, = ax.plot([], [], [], 'b-', alpha=0.5)
traj3, = ax.plot([], [], [], 'g-', alpha=0.5)

def init():
    body1.set_data([], [])
    body1.set_3d_properties([])
    body2.set_data([], [])
    body2.set_3d_properties([])
    body3.set_data([], [])
    body3.set_3d_properties([])
    traj1.set_data([], [])
    traj1.set_3d_properties([])
    traj2.set_data([], [])
    traj2.set_3d_properties([])
    traj3.set_data([], [])
    traj3.set_3d_properties([])
    return body1, body2, body3, traj1, traj2, traj3

def update(frame):
    print(f"Updating frame {frame}")
    body1.set_data([x1_sol[frame]], [y1_sol[frame]])
    body1.set_3d_properties([z1_sol[frame]])
    body2.set_data([x2_sol[frame]], [y2_sol[frame]])
    body2.set_3d_properties([z2_sol[frame]])
    body3.set_data([x3_sol[frame]], [y3_sol[frame]])
    body3.set_3d_properties([z3_sol[frame]])

    traj1.set_data(x1_sol[:frame], y1_sol[:frame])
    traj1.set_3d_properties(z1_sol[:frame])
    traj2.set_data(x2_sol[:frame], y2_sol[:frame])
    traj2.set_3d_properties(z2_sol[:frame])
    traj3.set_data(x3_sol[:frame], y3_sol[:frame])
    traj3.set_3d_properties(z3_sol[:frame])

    return body1, body2, body3, traj1, traj2, traj3


ani = animation.FuncAnimation(fig, update, frames=len(t_eval), init_func=init, interval=10, blit=False)
plt.pause(0.01)
plt.show()
