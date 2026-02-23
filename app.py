import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# --- PAGE CONFIG ---
st.set_page_config(page_title="Lake Eutrophication Analysis", layout="wide")

st.title("🌊 Lake Eutrophication: Bifurcation & Stability Analysis")
st.markdown("""
This tool simulates **regime shifts** in freshwater ecosystems. Using Non-Linear Dynamics specifically focused the Carpenter Lake Eutrophication Model which was developed by Stephen Carpenter, 
we model the phosphorus concentration ($P$) and identify the critical loading points where 
a lake "flips" from a healthy state to a polluted (eutrophic) state.
""")

# --- SIDEBAR PARAMETERS ---
st.sidebar.header("Model Parameters")
L = st.sidebar.slider("Nutrient Loading (L)", 0.0, 2.0, 0.45, help="Nutrient input from surroundings")
r = st.sidebar.slider("Recycling Rate (r)", 0.0, 1.5, 1.0, help="Max rate of P release from sediment")
s = st.sidebar.slider("Sedimentation Rate (s)", 0.1, 1.0, 0.7, help="Rate of P removal/outflow")
m = st.sidebar.number_input("Half-saturation (m)", value=1.0)
q = st.sidebar.number_input("Hill Coefficient (q)", value=8)

# --- MATHEMATICAL CORE ---
def dP_dt(P, L, s, r, m, q):
    return L - s*P + r * (P**q / (m**q + P**q))

def stability_derivative(P, s, r, m, q):
    # Derivative of growth function for stability check
    recycling_deriv = r * (q * P**(q-1) * (m**q) / (m**q + P**q)**2)
    return -s + recycling_deriv

# --- ROOT FINDING & STABILITY ---
P_range = np.linspace(0, 4, 1000)
roots = []
# Numerical root detection
for i in range(len(P_range)-1):
    if dP_dt(P_range[i], L, s, r, m, q) * dP_dt(P_range[i+1], L, s, r, m, q) < 0:
        root = fsolve(dP_dt, (P_range[i] + P_range[i+1])/2, args=(L, s, r, m, q))[0]
        roots.append(root)

fixed_points = sorted(list(set(np.round(roots, 4))))

# --- VISUALIZATION ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("System Dynamics ($dP/dt$)")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(P_range, dP_dt(P_range, L, s, r, m, q), label="Rate of Change", color='#1f77b4', lw=2)
    ax.axhline(0, color='black', linestyle='-', alpha=0.3)
    
    # Plotting Fixed Points with Stability color-coding
    for p in fixed_points:
        slope = stability_derivative(p, s, r, m, q)
        is_stable = slope < 0
        color = 'green' if is_stable else 'red'
        marker = 'o' if is_stable else 'X'
        label = "Stable" if is_stable else "Unstable"
        
        ax.plot(p, 0, marker=marker, color=color, markersize=10)
        ax.annotate(f"{label}\nP={p:.2f}", (p, 0.2), ha='center', fontweight='bold', color=color)

    ax.set_xlabel("Phosphorus Concentration (P)")
    ax.set_ylabel("dP/dt")
    ax.grid(True, alpha=0.2)
    st.pyplot(fig)

with col2:
    st.subheader("Current State")
    if fixed_points:
        for p in fixed_points:
            slope = stability_derivative(p, s, r, m, q)
            if slope < 0:
                state_type = "Healthy (Oligotrophic)" if p < m else "Collapsed (Eutrophic)"
                st.success(f"**Stable State at P = {p:.3f}**\n\nCondition: {state_type}")
            else:
                st.error(f"**Unstable Point at P = {p:.3f}**")
    else:
        st.warning("No equilibria found.")

# --- BIFURCATION MAP ---
st.divider()
st.subheader("Bifurcation & Hysteresis Analysis")
L_axis = np.linspace(0, 2.0, 250)
bif_l, bif_p = [], []

for l_val in L_axis:
    for i in range(len(P_range)-1):
        if dP_dt(P_range[i], l_val, s, r, m, q) * dP_dt(P_range[i+1], l_val, s, r, m, q) < 0:
            root = fsolve(dP_dt, (P_range[i] + P_range[i+1])/2, args=(l_val, s, r, m, q))[0]
            bif_l.append(l_val)
            bif_p.append(root)

fig2, ax2 = plt.subplots(figsize=(12, 4))
ax2.scatter(bif_l, bif_p, s=1, color='purple', alpha=0.5)
ax2.axvline(L, color='orange', linestyle='--', label=f"Current Loading (L={L})")
ax2.set_xlabel("Loading (L)")
ax2.set_ylabel("Equilibrium P*")
ax2.set_title("Bifurcation Diagram: Fixed Points vs Loading")
ax2.legend()
st.pyplot(fig2)
