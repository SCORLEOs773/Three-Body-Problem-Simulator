Three-Body Problem Simulation

This repository contains Python implementations of the Three-Body Problem, a classic problem in celestial mechanics where three bodies interact under Newtonian gravity. The project includes both 2D and 3D simulations, visualizing the chaotic motion of three gravitationally bound objects.

Features

2D Simulation: Visualizes the movement of three bodies in a plane.

3D Simulation: Fully animated 3D motion of the three bodies.

Real-time Animation: Uses matplotlib.animation to display dynamic movement.

Numerical Integration: Uses solve_ivp from SciPy to solve the equations of motion.

Customizable Initial Conditions: Allows tweaking masses, positions, and velocities.

Prerequisites

Ensure you have Python installed (>=3.7). Install required dependencies using:

pip install numpy matplotlib scipy

Running the Simulations

1. Run the 2D Simulation

python three_body_2d.py

This will open a 2D animation showing the orbits of the three bodies.

2. Run the 3D Simulation

python three_body_3d.py

This will generate a 3D visualization of the three-body motion.

File Structure

📂 Three-Body-Problem-Simulation
├── three_body_2d.py   # 2D Simulation Code
├── three_body_3d.py   # 3D Simulation Code
├── README.md          # Project Documentation

Explanation of the Code

Equations of Motion

The equations governing the motion of the three bodies are based on Newton’s law of universal gravitation:



where:

 is the gravitational force,

 is the gravitational constant,

 are the masses,

 is the distance between two bodies.

The acceleration due to gravity is computed as:



Numerical Integration

The system of differential equations is solved using the Runge-Kutta method (RK45) from SciPy:

solution = solve_ivp(three_body_equations, t_span, initial_conditions, t_eval=t_eval, args=(masses,), method='RK45')

Visualization

2D Example Output:

The 2D simulation plots the orbits of the three bodies, showing their paths over time.

3D Example Output:

The 3D simulation shows the motion in space with animated movement and trailing paths.

Customization

You can modify the initial conditions (positions, velocities, and masses) in the three_body_2d.py and three_body_3d.py files to explore different scenarios.

Example:

initial_conditions = [
    -1, 0, 1, 0, -0.5, 0,  # Body 1 (x, y, z, vx, vy, vz)
    1, 0, 1, 0, 0.5, 0,    # Body 2
    0, 1, 0, 0.5, -0.5, 0  # Body 3
]

Contributions

Feel free to fork this repository and submit pull requests with improvements or new features!

License

This project is open-source and available under the MIT License.

Acknowledgments

Isaac Newton for formulating classical gravity.

Henri Poincaré for pioneering chaos theory and celestial mechanics.

SciPy & Matplotlib for making numerical integration and visualization easier.

Happy coding! 🚀
