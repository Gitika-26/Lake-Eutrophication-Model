# Dynamics of Lake Eutrophication: A Bifurcation Analysis
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_DEPLOYED_LINK_HERE)

## 📌 Project Overview
This repository presents a rigorous numerical and analytical study of **regime shifts** in freshwater ecosystems. Using nonlinear differential equations, the model simulates how phosphorus levels ($P$) respond to external loading and internal recycling. 

This project serves as a practical application of **Dynamical Systems** to solve **Societal Challenges**, demonstrating:
* **Bifurcation Theory:** Identifying saddle-node points where ecosystems collapse.
* **Stability Analysis:** Classifying equilibria via linear stability (Jacobian/Derivative analysis).
* **Hysteresis & Irreversibility:** Mathematically proving why "cleaning up" is harder than "polluting."

---

## 🔬 Mathematical Formulation
The phosphorus concentration $P(t)$ is governed by the following Ordinary Differential Equation (ODE):

$$\frac{dP}{dt} = L - sP + r \frac{P^q}{m^q + P^q}$$

### Parameter Definitions
| Parameter | Definition | Significance |
| :--- | :--- | :--- |
| **$L$** | External Loading | Nutrient input (The primary **Bifurcation Parameter**) |
| **$s$** | Removal Rate | Sediment burial and water outflow |
| **$r$** | Recycling Strength | Maximum internal release from sediments |
| **$m$** | Half-saturation | Threshold where recycling reaches 50% capacity |
| **$q$** | Hill Coefficient | Sigmoid nonlinearity (Feedback strength) |

---

## 📈 Key Findings

### 1. Stability & Equilibrium Analysis
Equilibria are identified where $\frac{dP}{dt} = 0$. The local stability is determined by the derivative $f'(P^*)$:
* **Stable ($f'(P^*) < 0$):** The lake is resilient to perturbations (Healthy or Eutrophic states).
* **Unstable ($f'(P^*) > 0$):** The threshold between recovery and collapse.



### 2. Saddle-Node Bifurcation & Hysteresis
As loading $L$ increases, the system hits a tipping point where the stable "healthy" state vanishes. Due to **Hysteresis**, once a lake collapses into a eutrophic state, the loading must be reduced significantly below the initial tipping point to restore clarity.



---

## 💻 Interactive Deployment (Streamlit)
I have developed a **Decision Support System** to bridge the gap between abstract NLD (Non-Linear Dynamics) and environmental policy.

**Features of the [Live App](YOUR_DEPLOYED_LINK_HERE):**
* **Dynamic Root-Finding:** Real-time numerical solution of fixed points as parameters vary.
* **Automated Stability Classification:** Visual indicators for stable vs. unstable equilibria.
* **Live Bifurcation Mapping:** Visualizes the system's position relative to the tipping point.

---

## 📓 Notebook Implementation
The `Lake_Eutrophication_Model.ipynb` contains the research-grade implementation:
1. **Numerical Integration:** Using `scipy.optimize.fsolve` for precise root detection.
2. **Phase Portrait Analysis:** Visualizing the rate of change across the state space.
3. **Sensitivity Testing:** Exploring how the Hill coefficient $q$ affects the "sharpness" of ecological transitions.

---

## 🚀 How to Run Locally
1. Clone the repo: 
   ```bash
   git clone [https://github.com/YourUsername/Lake-Eutrophication-Model.git](https://github.com/YourUsername/Lake-Eutrophication-Model.git)
