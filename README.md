# Dynamics of Lake Eutrophication: A Bifurcation Analysis
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jkkvqncndtkmc7bdvwwtm2.streamlit.app/)

## 📌 Project Overview
This repository provides a numerical and analytical investigation into **regime shifts** within freshwater ecosystems. Based on the **Carpenter Lake Eutrophication Model**, the project explores how phosphorus concentration ($P$) responds to external stressors and internal feedback loops.

The study demonstrates the application of **Non-Linear Dynamics (NLD)** to solve **Societal Challenges**, specifically focusing on:
* **Stability Analysis:** Classifying fixed points via the sign of the derivative (linear stability).
* **Bifurcation Theory:** Identifying saddle-node points and ecological tipping points.
* **Hysteresis:** Mathematically demonstrating the irreversibility of environmental collapse.

---

## 🔬 Mathematical Framework
The phosphorus concentration $P$ over time is governed by the following Ordinary Differential Equation (ODE):

$$\frac{dP}{dt} = (L + b) - sP + r \frac{P^q}{m^q + P^q}$$

### Physical Meaning of Parameters
| Parameter | Symbol | Meaning |
| :--- | :--- | :--- |
| **Phosphorus** | $P$ | Concentration of nutrients in the water column. |
| **External Loading** | $L$ | Nutrient input from agricultural runoff (Bifurcation Parameter). |
| **Background Loading**| $b$ | Constant basal input (e.g., atmospheric deposition). |
| **Removal Rate** | $s$ | Rate of phosphorus loss through burial or outflow. |
| **Recycling Rate** | $r$ | Maximum rate of P release from sediments back into the water. |
| **Half-saturation** | $m$ | The P-level at which recycling is at 50% capacity. |
| **Hill Coefficient** | $q$ | The sigmoid exponent representing the "sharpness" of feedback. |

---

## 📈 Analysis & Insights

### 1. Equilibrium and Stability
Equilibrium states ($P^*$) occur when the rate of change is zero: $f(P) = 0$. 
The stability of these states is determined by the derivative $f'(P^*)$:
* **Stable ($f'(P^*) < 0$):** The system is resilient to small perturbations. 
* **Unstable ($f'(P^*) > 0$):** This represents a "tipping point" or threshold.



### 2. The Hysteresis Loop
Because of the non-linear recycling term, the system exhibits **Hysteresis**. If a lake collapses from an *Oligotrophic* (healthy) state to a *Eutrophic* (polluted) state, simply reducing the loading $L$ to pre-collapse levels is often insufficient for recovery.



---

## 💻 Interactive Dashboard (Streamlit)
I have developed a **Decision Support System** to bridge the gap between abstract mathematical theory and environmental management.

**[Launch the Live App]((https://jkkvqncndtkmc7bdvwwtm2.streamlit.app/))**

* **Real-time ODE Solving:** Uses `scipy.optimize.fsolve` to locate fixed points dynamically.
* **Stability Classification:** Automatically detects and labels stable vs. unstable equilibria.
* **Bifurcation Mapping:** Visualizes the current state of the lake relative to its critical tipping points.

---

## 🚀 Technical Implementation
* **Language:** Python 3.x
* **Core Libraries:** `NumPy` (Vectorized math), `SciPy` (Numerical root finding), `Matplotlib` (Scientific visualization).
* **Deployment:** Deployed via Streamlit Cloud for real-time interactivity.

---

### Reference
Carpenter, S. R., Ludwig, D., & Brock, W. A. (1999). *Management of Eutrophication for Lakes Subject to Potentially Irreversible Change.* Ecological Applications.
