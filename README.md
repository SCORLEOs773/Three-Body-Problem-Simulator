# Three-Body Problem Simulation

This repository contains Python implementations of the **Three-Body Problem**, a classical problem in celestial mechanics that involves predicting the motion of three bodies under mutual gravitational attraction. The simulations are available in both **2D** and **3D** versions.

## Features
- **2D Simulation**: Visualizes the orbits of three bodies in a 2D plane.
- **3D Simulation**: Adds depth and realism by simulating the bodies in three-dimensional space.
- **Custom Initial Conditions**: Modify mass, velocity, and starting positions for different scenarios.
- **Animated Trajectories**: Real-time visualization using `matplotlib.animation`.

---

## 🛠 Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/three-body-simulation.git
   cd three-body-simulation
Install the required dependencies:
sh
Copy
Edit
pip install numpy matplotlib scipy
Run the simulation:
2D Version:
sh
Copy
Edit
python three_body_2d.py
3D Version:
sh
Copy
Edit
python three_body_3d.py
📜 How It Works
Equations of Motion
The system is governed by Newton's law of universal gravitation:

𝐹
=
𝐺
𝑚
1
𝑚
2
𝑟
2
F=G 
r 
2
 
m 
1
​
 m 
2
​
 
​
 
For each body, acceleration is computed as:

𝑎
=
𝐹
𝑚
a= 
m
F
​
 
where 
𝐺
G is the gravitational constant, 
𝑚
m is mass, and 
𝑟
r is the distance between bodies.

Integration Method
The code uses scipy.integrate.solve_ivp with the RK45 method to numerically solve the system of differential equations.

📂 File Structure
bash
Copy
Edit
📦 three-body-simulation
 ┣ 📜 three_body_2d.py   # 2D simulation code
 ┣ 📜 three_body_3d.py   # 3D simulation code
 ┣ 📜 README.md          # Project documentation
🎮 Usage
Changing Initial Conditions
You can modify the starting positions and velocities of the bodies inside the Python files:

python
Copy
Edit
initial_conditions = [
    -1, 0, 0, 0, -0.5, 0,  # Body 1
    1, 0, 0, 0, 0.5, 0,    # Body 2
    0, 1, 0, 0.5, -0.5, 0  # Body 3
]
masses = [1, 1.5, 2]  # Different masses
Adjusting these values can create different orbital behaviors.

🎥 Demo
2D Version:

3D Version:

(Replace the image URLs with actual links if needed.)

📌 Todo / Future Improvements
Add energy conservation checks.
Implement a GUI for user-friendly interaction.
Optimize performance for longer simulations.
💡 References
Newtonian Mechanics & Three-Body Problem: Wikipedia
matplotlib animations: Matplotlib Docs
📜 License
This project is open-source and licensed under the MIT License.

📩 Feel free to contribute and improve this simulation!

vbnet
Copy
Edit

This README is fully formatted in Markdown and ready to be pasted into your repository! 🚀
