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

2. Install the required dependencies:
   ```sh
   pip install numpy matplotlib scipy

3. Run the simulation:
      a. 2D Version:
      ```sh
      python three_body_2d.py
      ```
      b. 3D Version:
      ```sh
      python three_body_3d.py
      
---

## 📜 How It Works

### Equations of Motion
The system is governed by Newton's law of universal gravitation:
F = $\frac{G m_1 m_2}{r^2}

For each body, acceleration is computed as:
a = $\frac{F}{m}

Where G is the gravitational constant, 𝑚 is mass, and 𝑟 is the distance between bodies.

### Integration Method
The code uses scipy.integrate.solve_ivp with the RK45 method to numerically solve the system of differential equations.

---

## 🎮 Usage

### Changing Initial Conditions
You can modify the starting positions and velocities of the bodies inside the Python files:

```sh
initial_conditions = [
    -1, 0, 0, 0, -0.5, 0,  # Body 1
    1, 0, 0, 0, 0.5, 0,    # Body 2
    0, 1, 0, 0.5, -0.5, 0  # Body 3
]
masses = [1, 1.5, 2]  # Different masses
```
Adjusting these values can create different orbital behaviors.

---

## 📌 Todo / Future Improvements
1. Add energy conservation checks.
2. Implement a GUI for user-friendly interaction.
3. Optimize performance for longer simulations.

---

## 💡 References
1. Newtonian Mechanics & Three-Body Problem: Wikipedia
2. matplotlib animations: Matplotlib Do

---

## 📜 License

This project is open-source and licensed under the MIT License.
📩 Feel free to contribute and improve this simulation!

