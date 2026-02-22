

<body>

<h1>The Dynamics of Lake Eutrophication </h1>

<h2>Overview</h2>

<p>
This repository contains a numerical implementation of a lake eutrophication model.
The model describes how phosphorus concentration in a lake changes over time due to external input,
natural removal, and internal recycling.
</p>

<p>
This system demonstrates important nonlinear dynamics concepts including:
</p>

<ul>
<li>Multiple steady states</li>
<li>Stability and instability</li>
<li>Saddle-node bifurcation</li>
<li>Environmental tipping points</li>
<li>Hysteresis</li>
</ul>

<p>
This project is intended for students studying nonlinear dynamics, environmental science, or applied mathematics.
</p>


<h2>Scientific Background</h2>

<p>
Eutrophication is the process by which a lake becomes enriched with nutrients, especially phosphorus.
This often happens due to agricultural runoff, wastewater discharge, or urban pollution.
</p>

<p>
When phosphorus levels increase, excessive algal growth can occur. This can reduce oxygen levels and harm aquatic life.
A clear lake may suddenly become polluted and turbid.
</p>

<p>
Scientific research has shown that this transition is not always gradual.
Instead, lakes can undergo sudden changes due to nonlinear internal recycling of phosphorus from sediments.
This feedback creates tipping points in the system.
</p>


<h2>Model Equation</h2>

<p>The governing differential equation is:</p>

<p>
dP/dt = L − sP + rP<sup>q</sup> / (m<sup>q</sup> + P<sup>q</sup>)
</p>

<p>Where:</p>

<ul>

<li><b>P</b> = phosphorus concentration in the lake</li>

<li><b>L</b> = external phosphorus loading (control parameter)</li>

<li><b>s</b> = phosphorus removal rate</li>

<li><b>r</b> = recycling strength</li>

<li><b>m</b> = half-saturation constant</li>

<li><b>q</b> = nonlinearity exponent</li>

</ul>


<h2>Meaning of Parameters</h2>

<h3>External Loading (L)</h3>

<p>
Represents nutrient input from agricultural runoff, wastewater, and pollution.
This is the main bifurcation parameter of the system.
</p>


<h3>Removal Rate (s)</h3>

<p>
Represents natural phosphorus removal through sediment burial and water outflow.
Higher values make the lake cleaner and more stable.
</p>


<h3>Recycling Strength (r)</h3>

<p>
Represents internal recycling of phosphorus from lake sediments.
Higher values increase pollution feedback.
</p>


<h3>Half-Saturation Constant (m)</h3>

<p>
Controls when recycling becomes significant.
</p>


<h3>Nonlinearity Exponent (q)</h3>

<p>
Controls how strong the nonlinear feedback is.
Higher values produce sharper tipping points.
</p>


<h2>Fixed Points</h2>

<p>
Fixed points are found by solving:
</p>

<p>dP/dt = 0</p>

<p>
These points represent equilibrium phosphorus levels.
</p>

<p>
The system may have:
</p>

<ul>

<li>One equilibrium</li>

<li>Or three equilibria</li>

</ul>

<p>
When three exist:
</p>

<ul>

<li>Lower equilibrium is stable (clear lake)</li>

<li>Middle equilibrium is unstable</li>

<li>Upper equilibrium is stable (polluted lake)</li>

</ul>


<h2>Stability Analysis</h2>

<p>
Stability is determined using the derivative of the equation.
</p>

<p>
If derivative is negative → stable
</p>

<p>
If derivative is positive → unstable
</p>


<h2>Bifurcation Analysis</h2>

<p>
The bifurcation parameter is the external loading L.
</p>

<p>
As L increases:
</p>

<ul>

<li>The lake remains clear at first</li>

<li>Then multiple states appear</li>

<li>Finally, the clear state disappears</li>

<li>The lake suddenly becomes polluted</li>

</ul>

<p>
This sudden change is called a saddle-node bifurcation.
</p>


<h2>Environmental Meaning</h2>

<p>
The bifurcation shows that environmental change can be sudden and irreversible.
</p>

<p>
Reducing pollution after collapse may not immediately restore the lake.
</p>

<p>
This effect is called hysteresis.
</p>


<h2>Numerical Method</h2>

<p>
The model is solved using numerical methods in Python.
</p>

<ul>

<li>Root finding to find equilibrium points</li>

<li>Derivative calculation for stability</li>

<li>Numerical simulation for time evolution</li>

<li>Parameter sweep for bifurcation diagram</li>

</ul>


<h2>Educational Importance</h2>

<p>
This model demonstrates how nonlinear mathematics explains real environmental tipping points.
</p>

<p>
It connects theory with real-world environmental systems.
</p>


<h2>Conclusion</h2>

<p>
The lake eutrophication model is a classic example of nonlinear dynamics in environmental science.
</p>

<p>
It shows how small changes in pollution can cause sudden ecological collapse.
</p>

<p>
Understanding these dynamics is important for environmental protection and management.
</p>


</body>
</html>
