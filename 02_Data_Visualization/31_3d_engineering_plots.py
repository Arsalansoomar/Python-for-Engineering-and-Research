"""
============================================================
Python for Engineering and Research
31 - 3D Engineering Plots
============================================================

Purpose:
    Demonstrate how three-dimensional plots can be used to
    visualize engineering parameter spaces, response
    surfaces, scattered design points, operating
    trajectories, optimization results, and relationships
    among three numerical variables.

Topics:
    1. What is a 3D engineering plot?
    2. Creating a 3D axis
    3. 3D line plots
    4. 3D scatter plots
    5. Color-coded 3D scatter plots
    6. np.meshgrid()
    7. Engineering response surfaces
    8. plot_surface()
    9. Surface colormaps
    10. Surface colorbars
    11. plot_wireframe()
    12. Surface + wireframe concepts
    13. Parameter-sweep surfaces
    14. Efficiency surfaces
    15. Power-loss surfaces
    16. Temperature surfaces
    17. Surface + sampled points
    18. Finding best sampled point
    19. Marking optimum candidates
    20. Difference surfaces
    21. Diverging colormaps
    22. Camera/view angles
    23. Elevation and azimuth
    24. Axis limits
    25. 3D box aspect
    26. Multiple 3D panels
    27. 3D contour projections
    28. Surface + projected contours
    29. Irregular DOE data
    30. plot_trisurf()
    31. DataFrame to 3D surface
    32. Long-form parameter data
    33. Multiple engineering objectives
    34. 3D operating trajectory
    35. 3D vs contour plot
    36. 3D vs heatmap
    37. Publication limitations
    38. Reusable plotting functions
    39. Saving PNG / PDF / SVG
    40. Common mistakes
    41. Key takeaways

Important:
    A 3D surface can provide useful qualitative insight into
    a multidimensional engineering response.

    However:

    3D perspective, occlusion, viewing angle, and projection
    can make precise quantitative comparisons harder than in
    2D contour or heatmap figures.

    Therefore 3D figures should normally complement rather
    than automatically replace quantitative 2D plots.

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. REQUIRED LIBRARIES
# ============================================================

import matplotlib.pyplot as plt
import matplotlib as mpl

import numpy as np
import pandas as pd

from pathlib import Path


# ============================================================
# 2. WHAT IS A 3D ENGINEERING PLOT?
# ============================================================

"""
A typical 2D plot contains:

X
vs
Y


Example:

Load [%]
vs
Efficiency [%]


A 3D plot can represent:

X Parameter
        +
Y Parameter
        +
Z Response


Example:

Switching Frequency [kHz]
        ×
Load [%]
        ↓
Efficiency [%]


Conceptually:


                   Efficiency
                       Z
                       ↑
                       |
                _______|______
              /              /|
            /              /  |
          /______________/    |
         |              |     |
         |              |    /
         |              |  /
         |______________|/
        /
       X
Switching Frequency

              Y = Load


This can reveal the overall shape of an engineering
response surface.
"""


# ============================================================
# 3. ENGINEERING APPLICATIONS
# ============================================================

"""
3D plots can be useful for:

- Converter efficiency maps
- Power-loss surfaces
- Temperature surfaces
- Parameter sweeps
- Design optimization
- Control tuning
- Parasitic sensitivity
- EMI-response surfaces
- Component-tolerance studies
- Monte Carlo visualization
- DOE results
- ML surrogate-model predictions
- Experimental parameter studies
- Battery / fuel-cell operating maps
- Renewable-energy performance analysis
"""


# ============================================================
# 4. WHEN 3D IS USEFUL
# ============================================================

"""
3D visualization is most useful when:

Two independent parameters

influence:

One response variable.


Example:

Switching Frequency
        ×
Load
        ↓
Efficiency


It provides an intuitive picture of:

Peaks

Valleys

Slopes

Plateaus

Operating regions
"""


# ============================================================
# 5. WHEN 3D MAY NOT BE THE BEST CHOICE
# ============================================================

"""
A 3D figure may NOT be ideal when:

Exact values must be compared

Several surfaces overlap

The figure will be printed very small

Important regions are hidden behind the surface

The viewing angle strongly changes interpretation

A contour map communicates the same result more clearly


Always ask:

Does 3D add information,

or only visual complexity?
"""


# ============================================================
# 6. PROJECT PATHS
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


output_figure_folder = (
    script_folder
    / "output_figures"
    / "3d_engineering"
)


output_data_folder = (
    script_folder
    / "output_data"
)


output_figure_folder.mkdir(
    parents=True,
    exist_ok=True
)


output_data_folder.mkdir(
    parents=True,
    exist_ok=True
)


print(
    "\n--- Output Figure Folder ---"
)


print(
    output_figure_folder
)


# ============================================================
# 7. CREATE A BASIC 3D AXIS
# ============================================================

"""
Basic syntax:

fig = plt.figure()

ax = fig.add_subplot(
    111,
    projection="3d"
)


The:

projection="3d"

argument creates a three-dimensional Matplotlib axis.
"""


fig = plt.figure(
    figsize=(7, 5)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


ax.set_xlabel(
    "X"
)

ax.set_ylabel(
    "Y"
)

ax.set_zlabel(
    "Z"
)


plt.show()


# ============================================================
# 8. BASIC 3D LINE PLOT
# ============================================================

"""
A 3D line requires:

X values

Y values

Z values
"""


parameter = np.linspace(
    0,
    10,
    500
)


x_line = parameter


y_line = np.sin(
    parameter
)


z_line = np.cos(
    parameter
)


fig = plt.figure(
    figsize=(7, 5)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


ax.plot(

    x_line,

    y_line,

    z_line,

    linewidth=1.5

)


ax.set_xlabel(
    "Parameter X [-]"
)

ax.set_ylabel(
    "Parameter Y [-]"
)

ax.set_zlabel(
    "Response Z [-]"
)


ax.set_title(
    "Basic 3D Line"
)


plt.show()


# ============================================================
# 9. WHAT DOES A 3D LINE REPRESENT?
# ============================================================

"""
A 3D line is useful when all three variables change along
one ordered trajectory.

Example:

Time
    ↓
Load
    ↓
Switching Frequency
    ↓
Efficiency


or:

Operating Point
    ↓
Voltage
Current
Temperature


A 3D line is different from a response surface.

LINE:

One trajectory


SURFACE:

Many combinations of X and Y
"""


# ============================================================
# 10. BASIC 3D SCATTER PLOT
# ============================================================

rng = np.random.default_rng(
    42
)


x_scatter = rng.uniform(
    0,
    10,
    150
)


y_scatter = rng.uniform(
    0,
    5,
    150
)


z_scatter = (

    2

    + 0.8
    * x_scatter

    - 0.5
    * y_scatter

    + rng.normal(
        0,
        0.8,
        150
    )

)


fig = plt.figure(
    figsize=(7, 5)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


ax.scatter(

    x_scatter,

    y_scatter,

    z_scatter,

    s=25

)


ax.set_xlabel(
    "Parameter X [-]"
)

ax.set_ylabel(
    "Parameter Y [-]"
)

ax.set_zlabel(
    "Response Z [-]"
)


ax.set_title(
    "3D Scatter Plot"
)


plt.show()


# ============================================================
# 11. COLOR-CODED 3D SCATTER
# ============================================================

"""
Color can encode an additional numerical meaning.

In this example:

X
Y
Z

already provide three dimensions.

Color also represents:

Z


This does not add a fourth independent variable,

but it makes high and low Z regions easier to distinguish.
"""


fig = plt.figure(
    figsize=(7.5, 5.5)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


scatter = ax.scatter(

    x_scatter,

    y_scatter,

    z_scatter,

    c=z_scatter,

    cmap="viridis",

    s=30

)


colorbar = fig.colorbar(

    scatter,

    ax=ax,

    pad=0.10

)


colorbar.set_label(
    "Response Z [-]"
)


ax.set_xlabel(
    "Parameter X [-]"
)

ax.set_ylabel(
    "Parameter Y [-]"
)

ax.set_zlabel(
    "Response Z [-]"
)


plt.show()


# ============================================================
# 12. ENGINEERING PARAMETER SWEEP
# ============================================================

"""
Now create a realistic educational engineering example.

Parameter 1:

Switching Frequency [kHz]


Parameter 2:

Load [%]


Responses:

Efficiency [%]

Power Loss [W]

Temperature [°C]


The equations below generate synthetic teaching data.

They are NOT intended to model a specific converter.
"""


switching_frequency_khz = np.linspace(

    50,

    250,

    41

)


load_percent = np.linspace(

    20,

    100,

    33

)


# ============================================================
# 13. CREATE PARAMETER GRID
# ============================================================

frequency_grid, load_grid = np.meshgrid(

    switching_frequency_khz,

    load_percent

)


print(
    "\n--- Parameter Grid Shape ---"
)


print(
    frequency_grid.shape
)


print(
    load_grid.shape
)


# ============================================================
# 14. EFFICIENCY RESPONSE
# ============================================================

efficiency_percent = (

    96.2

    - 0.000050
    * (
        frequency_grid
        - 135
    ) ** 2

    - 0.00035
    * (
        load_grid
        - 75
    ) ** 2

    - 0.0010
    * np.abs(
        frequency_grid
        - 135
    )

)


print(
    "\n--- Efficiency Range ---"
)


print(
    f"Minimum = "
    f"{efficiency_percent.min():.3f}%"
)


print(
    f"Maximum = "
    f"{efficiency_percent.max():.3f}%"
)


# ============================================================
# 15. BASIC 3D SURFACE
# ============================================================

"""
Basic surface syntax:

ax.plot_surface(
    X,
    Y,
    Z
)
"""


fig = plt.figure(
    figsize=(8, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


surface = ax.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_percent

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.set_title(
    "Converter Efficiency Surface"
)


plt.show()


# ============================================================
# 16. SURFACE WITH COLORMAP
# ============================================================

"""
A colormap helps reveal:

Low regions

High regions

Gradients
"""


fig = plt.figure(
    figsize=(8, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


surface = ax.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_percent,

    cmap="viridis",

    edgecolor="none",

    antialiased=True

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


plt.show()


# ============================================================
# 17. ADD COLORBAR
# ============================================================

fig = plt.figure(
    figsize=(8.5, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


surface = ax.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_percent,

    cmap="viridis",

    edgecolor="none"

)


colorbar = fig.colorbar(

    surface,

    ax=ax,

    shrink=0.70,

    pad=0.10

)


colorbar.set_label(
    "Efficiency [%]"
)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.set_title(
    "Efficiency Response Surface"
)


plt.show()


# ============================================================
# 18. WHY HAVE BOTH Z-AXIS AND COLORBAR?
# ============================================================

"""
The surface height represents:

Efficiency


and the color also represents:

Efficiency.


This redundancy can improve visual interpretation.


However:

The colorbar should not be confused with an independent
fourth variable unless the figure intentionally uses color
for something different.
"""


# ============================================================
# 19. VIEW ANGLE
# ============================================================

"""
A 3D plot depends on the camera position.

Matplotlib allows control using:

ax.view_init(
    elev=...,
    azim=...
)


elev:

Elevation angle


azim:

Azimuth angle
"""


fig = plt.figure(
    figsize=(8, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


surface = ax.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_percent,

    cmap="viridis",

    edgecolor="none"

)


ax.view_init(

    elev=25,

    azim=-135

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


plt.show()


# ============================================================
# 20. DIFFERENT VIEW ANGLES
# ============================================================

view_angles = [

    (
        20,
        -120
    ),

    (
        30,
        -60
    ),

    (
        45,
        -135
    )

]


for view_index, (
    elevation,
    azimuth
) in enumerate(
    view_angles,
    start=1
):

    fig = plt.figure(
        figsize=(7.5, 5.5)
    )


    ax = fig.add_subplot(

        111,

        projection="3d"

    )


    ax.plot_surface(

        frequency_grid,

        load_grid,

        efficiency_percent,

        cmap="viridis",

        edgecolor="none"

    )


    ax.view_init(

        elev=elevation,

        azim=azimuth

    )


    ax.set_xlabel(
        "Switching Frequency [kHz]"
    )


    ax.set_ylabel(
        "Load [%]"
    )


    ax.set_zlabel(
        "Efficiency [%]"
    )


    ax.set_title(

        f"View {view_index}: "
        f"elev={elevation}°, "
        f"azim={azimuth}°"

    )


    plt.show()


# ============================================================
# 21. VIEW-ANGLE WARNING
# ============================================================

"""
The underlying data do NOT change when the camera rotates.

However:

The apparent slope

Shape

Overlap

and

relative prominence


can change significantly.


Choose a view angle that:

Shows the important response clearly

without hiding critical regions.
"""


# ============================================================
# 22. WIREFRAME PLOT
# ============================================================

"""
A wireframe represents the surface using mesh lines.

This can make the underlying parameter grid easier to see.
"""


fig = plt.figure(
    figsize=(8, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


wireframe = ax.plot_wireframe(

    frequency_grid,

    load_grid,

    efficiency_percent,

    rcount=18,

    ccount=18,

    linewidth=0.7

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.set_title(
    "Efficiency Wireframe"
)


ax.view_init(
    elev=25,
    azim=-130
)


plt.show()


# ============================================================
# 23. SURFACE VS WIREFRAME
# ============================================================

"""
SURFACE

Good for:

Continuous visual shape

Color mapping

Overall response


------------------------------------------------------------


WIREFRAME

Good for:

Showing parameter-grid structure

Surface geometry

Sampling density


------------------------------------------------------------


A wireframe can become visually busy for very dense grids.
"""


# ============================================================
# 24. SURFACE WITH SAMPLING POINTS
# ============================================================

"""
A smooth-looking 3D surface can give the impression that
every coordinate was evaluated.

Showing sampled points helps communicate the underlying
grid.
"""


fig = plt.figure(
    figsize=(8.5, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


surface = ax.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_percent,

    cmap="viridis",

    alpha=0.80,

    edgecolor="none"

)


# Plot only some points for readability

sampling_step = 4


ax.scatter(

    frequency_grid[
        ::sampling_step,
        ::sampling_step
    ],

    load_grid[
        ::sampling_step,
        ::sampling_step
    ],

    efficiency_percent[
        ::sampling_step,
        ::sampling_step
    ],

    s=10

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.view_init(
    elev=25,
    azim=-135
)


plt.show()


# ============================================================
# 25. FIND BEST SAMPLED EFFICIENCY POINT
# ============================================================

maximum_efficiency_index = np.unravel_index(

    np.argmax(
        efficiency_percent
    ),

    efficiency_percent.shape

)


best_frequency_khz = frequency_grid[
    maximum_efficiency_index
]


best_load_percent = load_grid[
    maximum_efficiency_index
]


best_efficiency_percent = efficiency_percent[
    maximum_efficiency_index
]


print(
    "\n--- Best Sampled Efficiency Point ---"
)


print(
    f"Switching Frequency = "
    f"{best_frequency_khz:.2f} kHz"
)


print(
    f"Load = "
    f"{best_load_percent:.2f}%"
)


print(
    f"Efficiency = "
    f"{best_efficiency_percent:.4f}%"
)


# ============================================================
# 26. MARK BEST SAMPLED POINT
# ============================================================

fig = plt.figure(
    figsize=(8.5, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


surface = ax.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_percent,

    cmap="viridis",

    edgecolor="none",

    alpha=0.90

)


ax.scatter(

    best_frequency_khz,

    best_load_percent,

    best_efficiency_percent,

    marker="*",

    s=180,

    label="Best sampled point"

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.legend()


ax.view_init(
    elev=25,
    azim=-135
)


plt.show()


# ============================================================
# 27. BEST SAMPLED POINT != GLOBAL OPTIMUM
# ============================================================

"""
The point identified using:

np.argmax()


is the:

BEST SAMPLED POINT


among the evaluated parameter combinations.


It does NOT automatically prove:

GLOBAL CONTINUOUS OPTIMUM.


A point between grid samples may provide a better result.

Formal optimization or a refined parameter sweep may be
needed.
"""


# ============================================================
# 28. POWER-LOSS RESPONSE
# ============================================================

"""
Now create a second engineering response.

For power loss:

LOWER is generally preferable.
"""


power_loss_w = (

    5.0

    + 0.00012
    * (
        frequency_grid
        - 80
    ) ** 2

    + 0.00070
    * (
        load_grid
        - 20
    ) ** 2

    + 0.015
    * load_grid

)


print(
    "\n--- Power Loss Range ---"
)


print(
    f"Minimum = "
    f"{power_loss_w.min():.3f} W"
)


print(
    f"Maximum = "
    f"{power_loss_w.max():.3f} W"
)


# ============================================================
# 29. POWER-LOSS SURFACE
# ============================================================

fig = plt.figure(
    figsize=(8.5, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


surface = ax.plot_surface(

    frequency_grid,

    load_grid,

    power_loss_w,

    cmap="viridis",

    edgecolor="none"

)


colorbar = fig.colorbar(

    surface,

    ax=ax,

    shrink=0.7,

    pad=0.10

)


colorbar.set_label(
    "Power Loss [W]"
)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Power Loss [W]"
)


ax.set_title(
    "Converter Power-Loss Surface"
)


ax.view_init(
    elev=25,
    azim=-135
)


plt.show()


# ============================================================
# 30. FIND MINIMUM LOSS POINT
# ============================================================

minimum_loss_index = np.unravel_index(

    np.argmin(
        power_loss_w
    ),

    power_loss_w.shape

)


minimum_loss_frequency = frequency_grid[
    minimum_loss_index
]


minimum_loss_load = load_grid[
    minimum_loss_index
]


minimum_loss_value = power_loss_w[
    minimum_loss_index
]


print(
    "\n--- Minimum Sampled Loss ---"
)


print(
    f"Frequency = "
    f"{minimum_loss_frequency:.2f} kHz"
)


print(
    f"Load = "
    f"{minimum_loss_load:.2f}%"
)


print(
    f"Loss = "
    f"{minimum_loss_value:.3f} W"
)


# ============================================================
# 31. TEMPERATURE RESPONSE
# ============================================================

"""
Create a synthetic thermal response based partly on loss.

This is an educational visualization example only.
"""


temperature_c = (

    28

    + 2.4
    * power_loss_w

    + 0.04
    * load_grid

)


print(
    "\n--- Temperature Range ---"
)


print(
    f"Minimum = "
    f"{temperature_c.min():.2f} °C"
)


print(
    f"Maximum = "
    f"{temperature_c.max():.2f} °C"
)


# ============================================================
# 32. TEMPERATURE SURFACE
# ============================================================

fig = plt.figure(
    figsize=(8.5, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


surface = ax.plot_surface(

    frequency_grid,

    load_grid,

    temperature_c,

    cmap="inferno",

    edgecolor="none"

)


colorbar = fig.colorbar(

    surface,

    ax=ax,

    shrink=0.70,

    pad=0.10

)


colorbar.set_label(
    "Temperature [°C]"
)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Temperature [°C]"
)


ax.view_init(
    elev=25,
    azim=-135
)


plt.show()


# ============================================================
# 33. DO NOT PUT DIFFERENT UNITS ON ONE Z-AXIS
# ============================================================

"""
Do NOT combine:

Efficiency [%]

Power Loss [W]

Temperature [°C]


as three overlapping surfaces on the same Z-axis.

They represent different physical quantities and units.


Better:

Separate 3D panels

or:

Separate figures.
"""


# ============================================================
# 34. MULTIPLE 3D PANELS
# ============================================================

fig = plt.figure(
    figsize=(12, 5.5)
)


# ------------------------------------------------------------
# Efficiency panel
# ------------------------------------------------------------

ax_efficiency = fig.add_subplot(

    121,

    projection="3d"

)


surface_efficiency = ax_efficiency.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_percent,

    cmap="viridis",

    edgecolor="none"

)


ax_efficiency.set_xlabel(
    "Frequency [kHz]"
)

ax_efficiency.set_ylabel(
    "Load [%]"
)

ax_efficiency.set_zlabel(
    "Efficiency [%]"
)

ax_efficiency.set_title(
    "(a) Efficiency"
)


# ------------------------------------------------------------
# Temperature panel
# ------------------------------------------------------------

ax_temperature = fig.add_subplot(

    122,

    projection="3d"

)


surface_temperature = ax_temperature.plot_surface(

    frequency_grid,

    load_grid,

    temperature_c,

    cmap="inferno",

    edgecolor="none"

)


ax_temperature.set_xlabel(
    "Frequency [kHz]"
)

ax_temperature.set_ylabel(
    "Load [%]"
)

ax_temperature.set_zlabel(
    "Temperature [°C]"
)

ax_temperature.set_title(
    "(b) Temperature"
)


# Use same viewing direction

for ax in [
    ax_efficiency,
    ax_temperature
]:

    ax.view_init(

        elev=25,

        azim=-135

    )


plt.tight_layout()

plt.show()


# ============================================================
# 35. WHY USE SAME VIEW ANGLE?
# ============================================================

"""
When two 3D surfaces are directly compared:

Using the same:

Elevation

Azimuth


can make structural comparison easier.


Changing the viewing angle between panels can make similar
surfaces appear more different than they actually are.
"""


# ============================================================
# 36. DESIGN A AND DESIGN B
# ============================================================

design_a_efficiency = (

    efficiency_percent

    - 0.15

    - 0.12
    * np.sin(
        frequency_grid
        / 35
    )

)


design_b_efficiency = (

    efficiency_percent

    + 0.20

    - 0.18
    * np.cos(
        load_grid
        / 20
    )

)


# ============================================================
# 37. EFFICIENCY DIFFERENCE SURFACE
# ============================================================

efficiency_difference = (

    design_b_efficiency

    - design_a_efficiency

)


maximum_absolute_difference = np.max(

    np.abs(
        efficiency_difference
    )

)


print(
    "\n--- Difference Range ---"
)


print(
    efficiency_difference.min()
)


print(
    efficiency_difference.max()
)


# ============================================================
# 38. DIVERGING 3D DIFFERENCE SURFACE
# ============================================================

"""
For:

Design B - Design A


Positive values:

Design B higher


Negative values:

Design A higher


A diverging colormap is appropriate because:

0

has physical meaning.
"""


fig = plt.figure(
    figsize=(8.5, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


surface = ax.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_difference,

    cmap="coolwarm",

    vmin=-maximum_absolute_difference,

    vmax=maximum_absolute_difference,

    edgecolor="none"

)


colorbar = fig.colorbar(

    surface,

    ax=ax,

    shrink=0.70,

    pad=0.10

)


colorbar.set_label(
    "B - A [percentage points]"
)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency Difference [percentage points]"
)


ax.set_title(
    "Design Difference Surface"
)


ax.view_init(
    elev=25,
    azim=-135
)


plt.show()


# ============================================================
# 39. PERCENTAGE POINTS VS RELATIVE PERCENT
# ============================================================

"""
Example:

Design A:

94% efficiency


Design B:

95% efficiency


Difference:

95 - 94

=

1 percentage point


Relative percentage change:

(95 - 94)
/
94
×
100

≈

1.06%


These are not the same quantity.
"""


# ============================================================
# 40. SET 3D AXIS LIMITS
# ============================================================

fig = plt.figure(
    figsize=(8, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


ax.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_percent,

    cmap="viridis",

    edgecolor="none"

)


ax.set_xlim(
    50,
    250
)


ax.set_ylim(
    20,
    100
)


ax.set_zlim(
    94,
    96.5
)


ax.set_xlabel(
    "Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


plt.show()


# ============================================================
# 41. AXIS-LIMIT WARNING
# ============================================================

"""
Narrow Z limits can make a small change appear visually
dramatic.

Example:

94.8%
to
95.2%


may look like a large 3D hill if the Z-axis covers only:

94.7
to
95.3


Always report numerical values and use physically
reasonable limits.
"""


# ============================================================
# 42. 3D BOX ASPECT
# ============================================================

"""
The physical display proportions of the 3D box can be
adjusted.

Example:

ax.set_box_aspect(
    (
        1.4,
        1.0,
        0.8
    )
)


This changes the displayed box proportions.

It does NOT change the engineering data.
"""


fig = plt.figure(
    figsize=(8, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


ax.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_percent,

    cmap="viridis",

    edgecolor="none"

)


ax.set_box_aspect(
    (
        1.4,
        1.0,
        0.8
    )
)


ax.set_xlabel(
    "Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.view_init(
    elev=25,
    azim=-135
)


plt.show()


# ============================================================
# 43. BOX ASPECT WARNING
# ============================================================

"""
Changing the 3D box aspect affects:

Visual proportions


not:

Physical numerical values.


Avoid using aspect manipulation to exaggerate:

Peaks

Valleys

Slopes
"""


# ============================================================
# 44. PROJECT CONTOURS ONTO 3D SURFACE
# ============================================================

"""
A useful combination is:

3D surface
        +
2D contour projection


The contour projection can help readers estimate response
regions more easily.
"""


z_projection_level = (

    efficiency_percent.min()

    - 0.25

)


fig = plt.figure(
    figsize=(8.5, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


surface = ax.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_percent,

    cmap="viridis",

    edgecolor="none",

    alpha=0.90

)


contours = ax.contour(

    frequency_grid,

    load_grid,

    efficiency_percent,

    zdir="z",

    offset=z_projection_level,

    levels=10,

    cmap="viridis"

)


ax.set_zlim(

    z_projection_level,

    efficiency_percent.max()
    + 0.15

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.set_title(
    "Surface with Contour Projection"
)


ax.view_init(
    elev=28,
    azim=-135
)


plt.show()


# ============================================================
# 45. WHY PROJECT CONTOURS?
# ============================================================

"""
3D surface:

Shows shape.


Projected contour:

Shows equal-response regions.


Together they can improve interpretation.


However:

If the projected contour alone communicates the result
clearly enough,

a 2D contour figure may be simpler for publication.
"""


# ============================================================
# 46. IRREGULAR DOE / SCATTERED DATA
# ============================================================

"""
Engineering parameter studies are not always rectangular.

Examples:

Design of Experiments

Random search

Latin hypercube sampling

Optimization samples

Adaptive sampling


These produce scattered:

X

Y

Z


coordinates.
"""


number_of_doe_points = 180


doe_frequency_khz = rng.uniform(

    50,

    250,

    number_of_doe_points

)


doe_load_percent = rng.uniform(

    20,

    100,

    number_of_doe_points

)


doe_efficiency_percent = (

    96.2

    - 0.000050
    * (
        doe_frequency_khz
        - 135
    ) ** 2

    - 0.00035
    * (
        doe_load_percent
        - 75
    ) ** 2

    - 0.0010
    * np.abs(
        doe_frequency_khz
        - 135
    )

)


# ============================================================
# 47. 3D SCATTER OF DOE POINTS
# ============================================================

fig = plt.figure(
    figsize=(8, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


scatter = ax.scatter(

    doe_frequency_khz,

    doe_load_percent,

    doe_efficiency_percent,

    c=doe_efficiency_percent,

    cmap="viridis",

    s=30

)


colorbar = fig.colorbar(

    scatter,

    ax=ax,

    shrink=0.70,

    pad=0.10

)


colorbar.set_label(
    "Efficiency [%]"
)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.set_title(
    "DOE Samples in 3D Design Space"
)


ax.view_init(
    elev=25,
    azim=-135
)


plt.show()


# ============================================================
# 48. TRIANGULATED SURFACE
# ============================================================

"""
For scattered X-Y points:

plot_trisurf()

can create a triangulated surface.

This differs from:

plot_surface()

which is naturally suited to structured grid data.
"""


fig = plt.figure(
    figsize=(8.5, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


tri_surface = ax.plot_trisurf(

    doe_frequency_khz,

    doe_load_percent,

    doe_efficiency_percent,

    cmap="viridis",

    linewidth=0.2,

    antialiased=True

)


colorbar = fig.colorbar(

    tri_surface,

    ax=ax,

    shrink=0.70,

    pad=0.10

)


colorbar.set_label(
    "Efficiency [%]"
)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.set_title(
    "Triangulated DOE Response Surface"
)


ax.view_init(
    elev=25,
    azim=-135
)


plt.show()


# ============================================================
# 49. TRIANGULATION WARNING
# ============================================================

"""
A triangulated surface visually connects the scattered
sample points.

The resulting surface should not be interpreted as if:

Every displayed point was physically measured

or:

Every displayed point was directly simulated.


The original DOE samples remain the actual evaluated
locations.
"""


# ============================================================
# 50. SHOW TRIANGULATED SURFACE + ORIGINAL POINTS
# ============================================================

fig = plt.figure(
    figsize=(8.5, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


tri_surface = ax.plot_trisurf(

    doe_frequency_khz,

    doe_load_percent,

    doe_efficiency_percent,

    cmap="viridis",

    alpha=0.75,

    linewidth=0.2

)


ax.scatter(

    doe_frequency_khz,

    doe_load_percent,

    doe_efficiency_percent,

    s=10

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.view_init(
    elev=25,
    azim=-135
)


plt.show()


# ============================================================
# 51. LONG-FORM DATAFRAME
# ============================================================

"""
Research results are often stored in a long-form table:

Frequency | Load | Efficiency | Loss | Temperature
---------------------------------------------------
50        | 20   | ...
55        | 20   | ...
60        | 20   | ...
...
"""


parameter_dataframe = pd.DataFrame(
    {
        "Switching_Frequency_kHz":
            frequency_grid.ravel(),

        "Load_percent":
            load_grid.ravel(),

        "Efficiency_percent":
            efficiency_percent.ravel(),

        "Power_Loss_W":
            power_loss_w.ravel(),

        "Temperature_C":
            temperature_c.ravel()
    }
)


print(
    "\n--- Parameter DataFrame ---"
)


print(
    parameter_dataframe.head()
)


# ============================================================
# 52. SAVE PARAMETER DATA
# ============================================================

parameter_data_file = (
    output_data_folder
    / "3d_engineering_parameter_sweep.csv"
)


parameter_dataframe.to_csv(

    parameter_data_file,

    index=False

)


print(
    "\nParameter Data Saved:"
)


print(
    parameter_data_file
)


# ============================================================
# 53. DATAFRAME TO GRID
# ============================================================

"""
To use:

plot_surface()

the long-form parameter data can be pivoted into a 2D
matrix.
"""


efficiency_pivot = (
    parameter_dataframe
    .pivot(
        index="Load_percent",
        columns="Switching_Frequency_kHz",
        values="Efficiency_percent"
    )
)


pivot_load = (
    efficiency_pivot
    .index
    .to_numpy(
        dtype=float
    )
)


pivot_frequency = (
    efficiency_pivot
    .columns
    .to_numpy(
        dtype=float
    )
)


pivot_efficiency = (
    efficiency_pivot
    .to_numpy(
        dtype=float
    )
)


pivot_frequency_grid, pivot_load_grid = (
    np.meshgrid(

        pivot_frequency,

        pivot_load

    )
)


# ============================================================
# 54. SURFACE FROM DATAFRAME
# ============================================================

fig = plt.figure(
    figsize=(8.5, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


surface = ax.plot_surface(

    pivot_frequency_grid,

    pivot_load_grid,

    pivot_efficiency,

    cmap="viridis",

    edgecolor="none"

)


colorbar = fig.colorbar(

    surface,

    ax=ax,

    shrink=0.70,

    pad=0.10

)


colorbar.set_label(
    "Efficiency [%]"
)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.set_title(
    "3D Surface from Pandas DataFrame"
)


plt.show()


# ============================================================
# 55. DUPLICATE PARAMETER COMBINATIONS
# ============================================================

"""
pivot()

expects one response value for each:

X + Y

combination.


If repeated measurements exist at the same operating point:

Use:

pivot_table()


with an appropriate aggregation such as:

mean

median


Example:

dataframe.pivot_table(

    index="Load",

    columns="Frequency",

    values="Efficiency",

    aggfunc="mean"

)
"""


# ============================================================
# 56. MISSING PARAMETER POINTS
# ============================================================

"""
Real parameter studies may contain:

Failed simulations

Missing measurements

Unsafe operating points

Solver failures


Do not replace missing responses with:

0


unless zero is physically correct.


For incomplete rectangular grids, possible approaches
include:

Masked data

Interpolation

Triangulated plots

Scatter plots


depending on the research problem.
"""


# ============================================================
# 57. 3D OPERATING TRAJECTORY
# ============================================================

"""
A response surface shows all parameter combinations.

A trajectory shows how one operating point moves through
the design space over time.
"""


trajectory_time_s = np.linspace(
    0,
    5,
    500
)


trajectory_frequency_khz = (

    120

    + 30
    * np.sin(
        2
        * np.pi
        * trajectory_time_s
        / 5
    )

)


trajectory_load_percent = (

    60

    + 30
    * np.sin(
        2
        * np.pi
        * trajectory_time_s
        / 5
        + 0.7
    )

)


trajectory_efficiency = (

    96.2

    - 0.000050
    * (
        trajectory_frequency_khz
        - 135
    ) ** 2

    - 0.00035
    * (
        trajectory_load_percent
        - 75
    ) ** 2

    - 0.0010
    * np.abs(
        trajectory_frequency_khz
        - 135
    )

)


# ============================================================
# 58. PLOT OPERATING TRAJECTORY
# ============================================================

fig = plt.figure(
    figsize=(8, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


ax.plot(

    trajectory_frequency_khz,

    trajectory_load_percent,

    trajectory_efficiency,

    linewidth=2,

    label="Operating trajectory"

)


ax.scatter(

    trajectory_frequency_khz[
        0
    ],

    trajectory_load_percent[
        0
    ],

    trajectory_efficiency[
        0
    ],

    marker="o",

    s=50,

    label="Start"

)


ax.scatter(

    trajectory_frequency_khz[
        -1
    ],

    trajectory_load_percent[
        -1
    ],

    trajectory_efficiency[
        -1
    ],

    marker="X",

    s=60,

    label="End"

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.legend()


ax.view_init(
    elev=25,
    azim=-135
)


plt.show()


# ============================================================
# 59. TRAJECTORY OVER RESPONSE SURFACE
# ============================================================

fig = plt.figure(
    figsize=(8.5, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


ax.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_percent,

    cmap="viridis",

    edgecolor="none",

    alpha=0.60

)


ax.plot(

    trajectory_frequency_khz,

    trajectory_load_percent,

    trajectory_efficiency
    + 0.02,

    linewidth=2,

    label="Operating trajectory"

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.legend()


ax.view_init(
    elev=25,
    azim=-135
)


plt.show()


# ============================================================
# 60. TRAJECTORY INTERPRETATION
# ============================================================

"""
The response surface represents:

Available parameter space.


The trajectory represents:

Actual operating evolution through that space.


This can be useful for:

Adaptive control

Variable-frequency operation

Dynamic loading

Energy-management studies
"""


# ============================================================
# 61. 3D SURFACE VS 2D CONTOUR
# ============================================================

"""
The same dataset can also be visualized as a 2D contour
map.

This is important because 2D contour figures often allow
more precise quantitative interpretation.
"""


fig, axes = plt.subplots(

    1,

    2,

    figsize=(12, 5),

    layout="constrained"

)


# ------------------------------------------------------------
# 2D contour
# ------------------------------------------------------------

contour = axes[
    0
].contourf(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=20,

    cmap="viridis"

)


axes[
    0
].set_xlabel(
    "Switching Frequency [kHz]"
)


axes[
    0
].set_ylabel(
    "Load [%]"
)


axes[
    0
].set_title(
    "(a) 2D Contour"
)


colorbar = fig.colorbar(

    contour,

    ax=axes[
        0
    ]

)


colorbar.set_label(
    "Efficiency [%]"
)


# ------------------------------------------------------------
# We cannot place a true 3D projection into the existing
# 2D axis, so create a separate comparison below.
# ------------------------------------------------------------

plt.show()


# ============================================================
# 62. SEPARATE 3D VERSION OF SAME DATA
# ============================================================

fig = plt.figure(
    figsize=(7.5, 5.5)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


surface = ax.plot_surface(

    frequency_grid,

    load_grid,

    efficiency_percent,

    cmap="viridis",

    edgecolor="none"

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.set_title(
    "3D View of Same Response"
)


plt.show()


# ============================================================
# 63. 3D VS CONTOUR DECISION
# ============================================================

"""
3D SURFACE

Useful for:

Overall shape

Peaks

Valleys

Slope intuition

Presentations


------------------------------------------------------------


2D CONTOUR

Useful for:

Exact operating regions

Threshold boundaries

Publication figures

Optimization constraints

Comparing several designs


------------------------------------------------------------


Often the strongest workflow is:

3D during exploration

+
2D contour in the final quantitative analysis.
"""


# ============================================================
# 64. 3D VS HEATMAP
# ============================================================

"""
HEATMAP

Good for:

Large matrices

Cell-level comparisons

Correlation matrices

Compact publication figures


------------------------------------------------------------


3D SURFACE

Good for:

Showing response geometry


------------------------------------------------------------


The choice depends on the question,

not on which plot looks more impressive.
"""


# ============================================================
# 65. MULTI-OBJECTIVE ENGINEERING INTERPRETATION
# ============================================================

"""
Suppose the design objectives are:

Maximize:

Efficiency


Minimize:

Power Loss

Temperature


The preferred region may not be identical for all three
responses.


Therefore:

Maximum efficiency

does NOT automatically mean:

Best overall design.


This is a multi-objective engineering problem.
"""


# ============================================================
# 66. FEASIBLE REGION CONCEPT
# ============================================================

efficiency_requirement = 95.0

temperature_limit = 55.0

loss_limit = 10.0


feasible_region = (

    (
        efficiency_percent
        >= efficiency_requirement
    )

    &

    (
        temperature_c
        <= temperature_limit
    )

    &

    (
        power_loss_w
        <= loss_limit
    )

)


print(
    "\n--- Feasible Grid Points ---"
)


print(
    feasible_region.sum()
)


print(
    "of"
)


print(
    feasible_region.size
)


# ============================================================
# 67. FEASIBLE POINTS IN 3D
# ============================================================

"""
Instead of trying to represent several constraints as
different overlapping surfaces,

plot the feasible sampled points.
"""


fig = plt.figure(
    figsize=(8, 6)
)


ax = fig.add_subplot(

    111,

    projection="3d"

)


feasible_frequency = frequency_grid[
    feasible_region
]


feasible_load = load_grid[
    feasible_region
]


feasible_efficiency = efficiency_percent[
    feasible_region
]


scatter = ax.scatter(

    feasible_frequency,

    feasible_load,

    feasible_efficiency,

    c=feasible_efficiency,

    cmap="viridis",

    s=20

)


colorbar = fig.colorbar(

    scatter,

    ax=ax,

    shrink=0.70,

    pad=0.10

)


colorbar.set_label(
    "Efficiency [%]"
)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_zlabel(
    "Efficiency [%]"
)


ax.set_title(
    "Feasible Design Points"
)


plt.show()


# ============================================================
# 68. 3D DOES NOT REPLACE CONSTRAINT MAPS
# ============================================================

"""
For exact feasible-region interpretation:

A 2D contour or boolean map is often clearer.


3D can provide complementary geometric insight,

but should not make the engineering constraints harder to
understand.
"""


# ============================================================
# 69. REUSABLE SURFACE FUNCTION
# ============================================================

def plot_3d_surface(
    x,
    y,
    z,
    x_label,
    y_label,
    z_label,
    title=None,
    cmap="viridis",
    elevation=25,
    azimuth=-135,
    show_colorbar=True,
    edgecolor="none"
):
    """
    Create a reusable structured 3D surface plot.

    Parameters
    ----------
    x, y : 1D or 2D array-like
        Parameter coordinates.

    z : 2D array-like
        Response matrix.

    x_label : str
        X-axis label including units.

    y_label : str
        Y-axis label including units.

    z_label : str
        Z-axis / response label including units.

    title : str, optional
        Figure title.

    cmap : str
        Matplotlib colormap.

    elevation : float
        Viewing elevation in degrees.

    azimuth : float
        Viewing azimuth in degrees.

    show_colorbar : bool
        Add response colorbar.

    edgecolor : str
        Surface edge style.

    Returns
    -------
    fig, ax, surface
    """

    x = np.asarray(
        x,
        dtype=float
    )


    y = np.asarray(
        y,
        dtype=float
    )


    z = np.asarray(
        z,
        dtype=float
    )


    if x.ndim == 1 and y.ndim == 1:

        x_grid, y_grid = np.meshgrid(

            x,

            y

        )

    elif (
        x.ndim == 2
        and
        y.ndim == 2
    ):

        x_grid = x

        y_grid = y

    else:

        raise ValueError(
            "X and Y must both be 1D arrays "
            "or both be 2D grids."
        )


    if not (
        x_grid.shape
        ==
        y_grid.shape
        ==
        z.shape
    ):

        raise ValueError(
            "X grid, Y grid, and Z must have "
            "identical shapes."
        )


    if not np.any(
        np.isfinite(
            z
        )
    ):

        raise ValueError(
            "Z contains no valid numerical values."
        )


    fig = plt.figure(
        figsize=(8.5, 6)
    )


    ax = fig.add_subplot(

        111,

        projection="3d"

    )


    surface = ax.plot_surface(

        x_grid,

        y_grid,

        np.ma.masked_invalid(
            z
        ),

        cmap=cmap,

        edgecolor=edgecolor,

        antialiased=True

    )


    if show_colorbar:

        colorbar = fig.colorbar(

            surface,

            ax=ax,

            shrink=0.70,

            pad=0.10

        )


        colorbar.set_label(
            z_label
        )


    ax.set_xlabel(
        x_label
    )


    ax.set_ylabel(
        y_label
    )


    ax.set_zlabel(
        z_label
    )


    if title is not None:

        ax.set_title(
            title
        )


    ax.view_init(

        elev=elevation,

        azim=azimuth

    )


    return (
        fig,
        ax,
        surface
    )


# ============================================================
# 70. USE REUSABLE SURFACE FUNCTION
# ============================================================

fig, ax, surface = plot_3d_surface(

    x=switching_frequency_khz,

    y=load_percent,

    z=efficiency_percent,

    x_label=(
        "Switching Frequency [kHz]"
    ),

    y_label="Load [%]",

    z_label="Efficiency [%]",

    title=(
        "Reusable Engineering Surface"
    ),

    cmap="viridis",

    elevation=25,

    azimuth=-135

)


plt.show()


# ============================================================
# 71. REUSABLE 3D SCATTER FUNCTION
# ============================================================

def plot_3d_scatter(
    x,
    y,
    z,
    x_label,
    y_label,
    z_label,
    title=None,
    color_values=None,
    colorbar_label=None,
    cmap="viridis",
    elevation=25,
    azimuth=-135,
    marker_size=30
):
    """
    Create a reusable 3D scatter plot.
    """

    x = np.asarray(
        x,
        dtype=float
    )


    y = np.asarray(
        y,
        dtype=float
    )


    z = np.asarray(
        z,
        dtype=float
    )


    if not (
        x.shape
        ==
        y.shape
        ==
        z.shape
    ):

        raise ValueError(
            "X, Y, and Z must have identical shapes."
        )


    finite_mask = (

        np.isfinite(
            x
        )

        &

        np.isfinite(
            y
        )

        &

        np.isfinite(
            z
        )

    )


    if color_values is not None:

        color_values = np.asarray(
            color_values,
            dtype=float
        )


        if color_values.shape != x.shape:

            raise ValueError(
                "color_values must match X shape."
            )


        finite_mask = (

            finite_mask

            & np.isfinite(
                color_values
            )

        )


    x = x[
        finite_mask
    ]


    y = y[
        finite_mask
    ]


    z = z[
        finite_mask
    ]


    if len(
        x
    ) == 0:

        raise ValueError(
            "No valid data points remain."
        )


    fig = plt.figure(
        figsize=(8, 6)
    )


    ax = fig.add_subplot(

        111,

        projection="3d"

    )


    if color_values is None:

        scatter = ax.scatter(

            x,

            y,

            z,

            s=marker_size

        )

    else:

        color_values = color_values[
            finite_mask
        ]


        scatter = ax.scatter(

            x,

            y,

            z,

            c=color_values,

            cmap=cmap,

            s=marker_size

        )


        colorbar = fig.colorbar(

            scatter,

            ax=ax,

            shrink=0.70,

            pad=0.10

        )


        if colorbar_label is not None:

            colorbar.set_label(
                colorbar_label
            )


    ax.set_xlabel(
        x_label
    )


    ax.set_ylabel(
        y_label
    )


    ax.set_zlabel(
        z_label
    )


    if title is not None:

        ax.set_title(
            title
        )


    ax.view_init(

        elev=elevation,

        azim=azimuth

    )


    return (
        fig,
        ax,
        scatter
    )


# ============================================================
# 72. USE REUSABLE SCATTER FUNCTION
# ============================================================

fig, ax, scatter = plot_3d_scatter(

    x=doe_frequency_khz,

    y=doe_load_percent,

    z=doe_efficiency_percent,

    x_label=(
        "Switching Frequency [kHz]"
    ),

    y_label="Load [%]",

    z_label="Efficiency [%]",

    title="DOE Response Points",

    color_values=doe_efficiency_percent,

    colorbar_label="Efficiency [%]"

)


plt.show()


# ============================================================
# 73. REUSABLE TRIANGULATED SURFACE
# ============================================================

def plot_3d_trisurface(
    x,
    y,
    z,
    x_label,
    y_label,
    z_label,
    title=None,
    cmap="viridis",
    show_points=True,
    elevation=25,
    azimuth=-135
):
    """
    Plot scattered X-Y-Z samples as a triangulated surface.
    """

    x = np.asarray(
        x,
        dtype=float
    )


    y = np.asarray(
        y,
        dtype=float
    )


    z = np.asarray(
        z,
        dtype=float
    )


    if not (
        x.shape
        ==
        y.shape
        ==
        z.shape
    ):

        raise ValueError(
            "X, Y, and Z must have identical shapes."
        )


    finite_mask = (

        np.isfinite(
            x
        )

        &

        np.isfinite(
            y
        )

        &

        np.isfinite(
            z
        )

    )


    x = x[
        finite_mask
    ]


    y = y[
        finite_mask
    ]


    z = z[
        finite_mask
    ]


    if len(
        x
    ) < 3:

        raise ValueError(
            "At least three valid points are required."
        )


    fig = plt.figure(
        figsize=(8.5, 6)
    )


    ax = fig.add_subplot(

        111,

        projection="3d"

    )


    surface = ax.plot_trisurf(

        x,

        y,

        z,

        cmap=cmap,

        linewidth=0.2,

        antialiased=True,

        alpha=0.85

    )


    if show_points:

        ax.scatter(

            x,

            y,

            z,

            s=8

        )


    colorbar = fig.colorbar(

        surface,

        ax=ax,

        shrink=0.70,

        pad=0.10

    )


    colorbar.set_label(
        z_label
    )


    ax.set_xlabel(
        x_label
    )


    ax.set_ylabel(
        y_label
    )


    ax.set_zlabel(
        z_label
    )


    if title is not None:

        ax.set_title(
            title
        )


    ax.view_init(

        elev=elevation,

        azim=azimuth

    )


    return (
        fig,
        ax,
        surface
    )


# ============================================================
# 74. USE TRI-SURFACE FUNCTION
# ============================================================

fig, ax, surface = plot_3d_trisurface(

    x=doe_frequency_khz,

    y=doe_load_percent,

    z=doe_efficiency_percent,

    x_label=(
        "Switching Frequency [kHz]"
    ),

    y_label="Load [%]",

    z_label="Efficiency [%]",

    title="Irregular DOE Triangulated Surface"

)


plt.show()


# ============================================================
# 75. PUBLICATION SIZE
# ============================================================

def mm_to_inches(
    millimeters
):
    """
    Convert millimeters to inches.
    """

    return (

        millimeters

        / 25.4

    )


publication_width_mm = 178


publication_width_in = (
    mm_to_inches(
        publication_width_mm
    )
)


publication_height_in = (

    publication_width_in

    * 0.75

)


# ============================================================
# 76. PUBLICATION STYLE
# ============================================================

publication_style = {

    "font.size":
        8,

    "axes.labelsize":
        9,

    "axes.titlesize":
        9,

    "xtick.labelsize":
        8,

    "ytick.labelsize":
        8,

    "legend.fontsize":
        8,

    "axes.linewidth":
        0.8

}


# ============================================================
# 77. FINAL PUBLICATION-ORIENTED 3D FIGURE
# ============================================================

with mpl.rc_context(
    publication_style
):

    fig = plt.figure(

        figsize=(
            publication_width_in,
            publication_height_in
        )

    )


    ax = fig.add_subplot(

        111,

        projection="3d"

    )


    surface = ax.plot_surface(

        frequency_grid,

        load_grid,

        efficiency_percent,

        cmap="viridis",

        edgecolor="none",

        antialiased=True

    )


    ax.scatter(

        best_frequency_khz,

        best_load_percent,

        best_efficiency_percent,

        marker="*",

        s=120,

        label="Best sampled point"

    )


    ax.set_xlabel(
        "Switching Frequency [kHz]"
    )


    ax.set_ylabel(
        "Load [%]"
    )


    ax.set_zlabel(
        "Efficiency [%]"
    )


    ax.view_init(

        elev=25,

        azim=-135

    )


    ax.set_box_aspect(
        (
            1.4,
            1.0,
            0.8
        )
    )


    colorbar = fig.colorbar(

        surface,

        ax=ax,

        shrink=0.65,

        pad=0.10

    )


    colorbar.set_label(
        "Efficiency [%]"
    )


    ax.legend(
        loc="best"
    )


    # --------------------------------------------------------
    # Save PNG
    # --------------------------------------------------------

    final_png = (
        output_figure_folder
        / "engineering_3d_surface.png"
    )


    fig.savefig(

        final_png,

        dpi=300,

        bbox_inches="tight"

    )


    # --------------------------------------------------------
    # Save PDF
    # --------------------------------------------------------

    final_pdf = (
        output_figure_folder
        / "engineering_3d_surface.pdf"
    )


    fig.savefig(

        final_pdf,

        bbox_inches="tight"

    )


    # --------------------------------------------------------
    # Save SVG
    # --------------------------------------------------------

    final_svg = (
        output_figure_folder
        / "engineering_3d_surface.svg"
    )


    fig.savefig(

        final_svg,

        bbox_inches="tight"

    )


    print(
        "\n--- 3D Figures Saved ---"
    )


    print(
        final_png
    )


    print(
        final_pdf
    )


    print(
        final_svg
    )


    plt.show()


# ============================================================
# 78. SAVE OPTIMUM SUMMARY
# ============================================================

optimization_summary = pd.DataFrame(
    [
        {
            "Objective":
                "Maximum Efficiency",

            "Switching_Frequency_kHz":
                best_frequency_khz,

            "Load_percent":
                best_load_percent,

            "Response_Value":
                best_efficiency_percent,

            "Response_Unit":
                "%"
        },

        {
            "Objective":
                "Minimum Power Loss",

            "Switching_Frequency_kHz":
                minimum_loss_frequency,

            "Load_percent":
                minimum_loss_load,

            "Response_Value":
                minimum_loss_value,

            "Response_Unit":
                "W"
        }
    ]
)


optimization_summary_file = (
    output_data_folder
    / "3d_engineering_optimum_summary.csv"
)


optimization_summary.to_csv(

    optimization_summary_file,

    index=False

)


print(
    "\n--- Optimum Summary ---"
)


print(
    optimization_summary
)


# ============================================================
# 79. COMMON MISTAKE - USING 3D BECAUSE IT LOOKS IMPRESSIVE
# ============================================================

"""
A plot should answer an engineering question.

Do not choose:

3D


only because it appears more sophisticated.


Ask:

Can the reader interpret the result more easily?
"""


# ============================================================
# 80. COMMON MISTAKE - NO Z-AXIS UNIT
# ============================================================

"""
Weak:

Response


Better:

Efficiency [%]

Power Loss [W]

Temperature [°C]

EMI Magnitude [dBµV]
"""


# ============================================================
# 81. COMMON MISTAKE - NO COLORBAR
# ============================================================

"""
If surface color represents a numerical quantity:

Include a colorbar when it improves interpretation.
"""


# ============================================================
# 82. COMMON MISTAKE - COLOR AND Z REPRESENT DIFFERENT VARIABLES
# ============================================================

"""
A surface may use:

Z = Efficiency

Color = Temperature


This is possible,

but creates a four-variable figure.


It can become difficult to interpret.


Use only when the extra encoding genuinely adds value and
is explained clearly.
"""


# ============================================================
# 83. COMMON MISTAKE - TOO MANY OVERLAPPING SURFACES
# ============================================================

"""
Three overlapping surfaces can hide one another because of
occlusion.

Better options:

Separate 3D panels

2D contour maps

Difference surfaces

Multi-panel figures
"""


# ============================================================
# 84. COMMON MISTAKE - VIEW ANGLE HIDES THE OPTIMUM
# ============================================================

"""
A surface peak may be hidden behind another region.

Rotate the figure during analysis.

For the final static figure:

Choose a reproducible:

Elevation

and

Azimuth


and store them in code.
"""


# ============================================================
# 85. COMMON MISTAKE - DIFFERENT VIEWS FOR DIRECT COMPARISON
# ============================================================

"""
If comparing:

Design A

and

Design B


different camera angles can make the surfaces appear more
different.


Use identical view settings whenever direct visual
comparison is intended.
"""


# ============================================================
# 86. COMMON MISTAKE - EXAGGERATED Z SCALE
# ============================================================

"""
A small change such as:

95.0%

to:

95.2%


can look like a dramatic mountain if the Z-axis is heavily
magnified.


Always check the actual numerical magnitude.
"""


# ============================================================
# 87. COMMON MISTAKE - SURFACE HIDES SAMPLING DENSITY
# ============================================================

"""
A smooth surface may visually imply dense simulation.

If only:

5 × 5

cases were evaluated,

the figure should not imply that hundreds of operating
points were measured.


Consider showing:

Sampling points

Wireframe

or reporting grid resolution.
"""


# ============================================================
# 88. COMMON MISTAKE - TRI-SURFACE = MEASURED EVERYWHERE
# ============================================================

"""
plot_trisurf()

creates a triangulated surface between scattered points.

Those interpolated-looking regions are not themselves
additional measurements.
"""


# ============================================================
# 89. COMMON MISTAKE - WRONG OBJECTIVE DIRECTION
# ============================================================

"""
Efficiency:

Usually maximize


Power loss:

Usually minimize


Temperature:

Often minimize or constrain


Prediction error:

Usually minimize


Define the engineering objective explicitly.
"""


# ============================================================
# 90. COMMON MISTAKE - GLOBAL OPTIMUM CLAIM
# ============================================================

"""
np.argmax()

on a finite grid finds:

Maximum sampled point.


It does not prove:

Global optimum of the continuous design space.
"""


# ============================================================
# 91. COMMON MISTAKE - ONE RESPONSE DEFINES BEST DESIGN
# ============================================================

"""
Maximum efficiency alone may not provide:

Lowest EMI

Lowest temperature

Lowest cost

Highest reliability

Smallest volume


Real engineering optimization is often multi-objective.
"""


# ============================================================
# 92. COMMON MISTAKE - 3D FOR CORRELATION MATRIX
# ============================================================

"""
A 3D bar or surface representation of a correlation matrix
may look attractive,

but a standard 2D correlation heatmap is usually much
easier to compare quantitatively.
"""


# ============================================================
# 93. COMMON MISTAKE - TOO MANY GRID LINES
# ============================================================

"""
A dense wireframe may obscure the surface.

Reduce:

rcount

ccount


or use:

plot_surface()
"""


# ============================================================
# 94. COMMON MISTAKE - TINY 3D FIGURE
# ============================================================

"""
3D figures require room for:

X label

Y label

Z label

Ticks

Colorbar

Perspective


A very small journal column can make them difficult to
read.


Check at the final publication dimensions.
"""


# ============================================================
# 95. COMMON MISTAKE - SCREENSHOT INSTEAD OF EXPORT
# ============================================================

"""
Do not rotate a 3D plot interactively and then take a
screen capture.

Store the view in code:

ax.view_init(
    elev=...,
    azim=...
)


then use:

fig.savefig(...)
"""


# ============================================================
# 96. COMMON MISTAKE - NONREPRODUCIBLE CAMERA
# ============================================================

"""
Final 3D figures should specify:

Elevation

Azimuth

Axis limits

Aspect

Figure size


inside the Python script.
"""


# ============================================================
# 97. COMMON MISTAKE - 3D REPLACES NUMERICAL RESULTS
# ============================================================

"""
A surface may show the design landscape.

But important results should still be reported numerically:

Maximum efficiency

Best sampled frequency

Best sampled load

Minimum loss

Constraint values
"""


# ============================================================
# 98. 3D SURFACE WORKFLOW
# ============================================================

"""
Parameter X
      ↓
Parameter Y
      ↓
np.meshgrid()
      ↓
Response Z
      ↓
plot_surface()
      ↓
Colormap
      ↓
Colorbar
      ↓
Select Camera Angle
      ↓
Mark Important Point
      ↓
Engineering Interpretation
"""


# ============================================================
# 99. DOE WORKFLOW
# ============================================================

"""
DOE Samples
    ↓
X
Y
Response Z
    ↓
3D Scatter
    ↓
Inspect Sampling Coverage
    ↓
Optional:
plot_trisurf()
    ↓
Compare with Surrogate Model
    ↓
Validate Predictions
"""


# ============================================================
# 100. OPTIMIZATION WORKFLOW
# ============================================================

"""
Parameter Space
      ↓
Response Surface
      ↓
Find Best Sampled Point
      ↓
Apply Constraints
      ↓
Check Other Objectives
      ↓
Refine Parameter Region
      ↓
Run Additional Cases
      ↓
Validate Optimum Candidate
"""


# ============================================================
# 101. 3D PLOT DECISION GUIDE
# ============================================================

"""
Three scattered numerical variables?
        ↓
3D SCATTER


One ordered trajectory in X-Y-Z?
        ↓
3D LINE


Regular parameter grid?
        ↓
plot_surface()


Need grid structure?
        ↓
plot_wireframe()


Irregular scattered X-Y samples?
        ↓
plot_trisurf()


Need exact response regions?
        ↓
2D CONTOUR


Need matrix overview?
        ↓
HEATMAP


Need statistical relationships?
        ↓
CORRELATION MAP
"""


# ============================================================
# 102. PUBLICATION CHECKLIST
# ============================================================

"""
Before publishing a 3D engineering figure, check:


SCIENTIFIC NEED
------------------------------------------------------------

Does 3D improve understanding?


PARAMETERS
------------------------------------------------------------

What does X represent?

What does Y represent?

What does Z represent?


UNITS
------------------------------------------------------------

Are all three units visible?


COLOR
------------------------------------------------------------

What does surface color represent?

Is a colorbar required?


SAMPLING
------------------------------------------------------------

How many parameter combinations were evaluated?

Is the grid regular or irregular?


SURFACE
------------------------------------------------------------

Measured?

Simulated?

Interpolated?

Triangulated?

ML predicted?


CAMERA
------------------------------------------------------------

Are elevation and azimuth reproducible?

Does the view hide important regions?


SCALE
------------------------------------------------------------

Does the Z scale exaggerate small changes?


OPTIMUM
------------------------------------------------------------

Is the point:

Best sampled point

or

True optimized point?


COMPARISON
------------------------------------------------------------

Are directly compared surfaces using similar views?


ALTERNATIVE
------------------------------------------------------------

Would a 2D contour plot be clearer?


OUTPUT
------------------------------------------------------------

PNG generated?

PDF generated?

SVG generated?


FINAL TEST
------------------------------------------------------------

Can a reader understand the engineering conclusion without
interactively rotating the figure?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
3D ENGINEERING PLOTS


1. CREATE 3D AXIS

fig = plt.figure()


ax = fig.add_subplot(

    111,

    projection="3d"

)


------------------------------------------------------------


2. 3D LINE

ax.plot(

    x,

    y,

    z

)


Useful for:

Operating trajectories

Dynamic paths

Parametric curves


------------------------------------------------------------


3. 3D SCATTER

ax.scatter(

    x,

    y,

    z

)


Useful for:

DOE samples

Experiments

Optimization samples

ML datasets


------------------------------------------------------------


4. COLOR-CODED SCATTER

scatter = ax.scatter(

    x,

    y,

    z,

    c=response,

    cmap="viridis"

)


------------------------------------------------------------


5. PARAMETER GRID

X, Y = np.meshgrid(

    x,

    y

)


------------------------------------------------------------


6. RESPONSE SURFACE

Z = response_function(

    X,

    Y

)


------------------------------------------------------------


7. SURFACE PLOT

surface = ax.plot_surface(

    X,

    Y,

    Z

)


------------------------------------------------------------


8. COLORMAP

surface = ax.plot_surface(

    X,

    Y,

    Z,

    cmap="viridis"

)


------------------------------------------------------------


9. COLORBAR

colorbar = fig.colorbar(

    surface,

    ax=ax

)


colorbar.set_label(
    "Efficiency [%]"
)


------------------------------------------------------------


10. WIREFRAME

ax.plot_wireframe(

    X,

    Y,

    Z

)


Useful for:

Grid structure

Sampling visualization


------------------------------------------------------------


11. VIEW ANGLE

ax.view_init(

    elev=25,

    azim=-135

)


------------------------------------------------------------


12. AXIS LIMITS

ax.set_xlim(...)

ax.set_ylim(...)

ax.set_zlim(...)


------------------------------------------------------------


13. BOX ASPECT

ax.set_box_aspect(

    (
        1.4,
        1.0,
        0.8
    )

)


This changes:

Display geometry


not:

Engineering data.


------------------------------------------------------------


14. BEST SAMPLED POINT

index = np.unravel_index(

    np.argmax(
        Z
    ),

    Z.shape

)


------------------------------------------------------------


15. MINIMUM SAMPLED POINT

index = np.unravel_index(

    np.argmin(
        Z
    ),

    Z.shape

)


------------------------------------------------------------


16. IMPORTANT TERMINOLOGY

Finite parameter sweep:

Best sampled point


Do not automatically call it:

Global optimum.


------------------------------------------------------------


17. DIFFERENCE SURFACE

difference = (

    design_b

    - design_a

)


Use a diverging colormap when:

0

is a meaningful reference.


------------------------------------------------------------


18. TRIANGULATED SURFACE

ax.plot_trisurf(

    x,

    y,

    z

)


Useful for:

Irregular scattered samples.


------------------------------------------------------------


19. TRIANGULATION WARNING

A triangulated surface contains visual connections between
sampled points.


It does not mean every displayed location was directly
evaluated.


------------------------------------------------------------


20. SURFACE + SAMPLE POINTS

Useful for showing:

Smooth response

and

Actual evaluated locations.


------------------------------------------------------------


21. DATAFRAME TO SURFACE

Long-form data:

Frequency
Load
Efficiency


        ↓

pivot()


        ↓

2D matrix


        ↓

plot_surface()


------------------------------------------------------------


22. MULTIPLE PHYSICAL RESPONSES

Efficiency [%]

Power Loss [W]

Temperature [°C]


should normally use:

Separate panels

or:

Separate figures.


------------------------------------------------------------


23. 3D CONTOUR PROJECTION

A surface can be combined with:

Projected contour lines


to improve equal-value interpretation.


------------------------------------------------------------


24. 3D vs CONTOUR

3D:

Good for geometric intuition


2D contour:

Good for quantitative operating regions


Often use both during analysis.


------------------------------------------------------------


25. 3D vs HEATMAP

3D:

Response geometry


Heatmap:

Compact matrix comparison


------------------------------------------------------------


26. DOE VISUALIZATION

DOE Points
        ↓
3D Scatter
        ↓
Optional Tri-Surface
        ↓
Sampling-Coverage Analysis


------------------------------------------------------------


27. OPERATING TRAJECTORY

Frequency
        +
Load
        +
Efficiency
        ↓
3D Line


Useful for:

Dynamic operation

Adaptive control

Energy management


------------------------------------------------------------


28. MULTI-OBJECTIVE DESIGN

Maximum Efficiency
        ≠
Minimum Loss
        ≠
Minimum Temperature


The best overall design may require:

Tradeoff analysis.


------------------------------------------------------------


29. PUBLICATION LIMITATION

Static 3D figures can suffer from:

Perspective

Occlusion

Hidden regions

Viewing-angle dependence

Small labels


Therefore:

Do not automatically prefer 3D over a good 2D contour
figure.


------------------------------------------------------------


30. REPRODUCIBILITY

Store:

Camera angle

Axis limits

Figure size

Colormap

Parameter ranges

Sampling resolution


inside the code.


------------------------------------------------------------


31. ENGINEERING APPLICATIONS

Especially useful for:

Power electronics

Converter efficiency

Loss analysis

Thermal design

EMI parameter sweeps

Control tuning

Renewable-energy systems

DOE studies

Robustness analysis

ML surrogate models

Optimization


------------------------------------------------------------


32. MOST IMPORTANT PRINCIPLE

Do not ask:

"How can I make this result 3D?"


Ask:

"Does the third dimension help the reader understand the
engineering relationship?"


------------------------------------------------------------


33. COMPLETE WORKFLOW

Engineering Parameters
        ↓
Choose X
        ↓
Choose Y
        ↓
Calculate / Measure Z
        ↓
Validate Data
        ↓
Regular Grid?
    ↙           ↘
 YES            NO
 ↓               ↓
Surface        Scatter
Wireframe      Tri-Surface
    ↘           ↙
       3D View
          ↓
Select Camera
          ↓
Add Units
          ↓
Add Colorbar
          ↓
Mark Important Points
          ↓
Compare with 2D Contour
          ↓
Quantify Results
          ↓
Engineering Interpretation
          ↓
Publication Figure


------------------------------------------------------------


NEXT:

32_interactive_plotting.py


The next file will introduce interactive engineering
visualization while keeping the core workflow practical.

Topics will include:

Matplotlib interactive concepts

Interactive figure windows

Zoom / pan

Data cursors and point inspection concepts

Slider widgets

Button widgets

Radio buttons

Check buttons

Interactive parameter selection

Frequency-range sliders

Load-selection sliders

Updating curves dynamically

Interactive parameter sweeps

Interactive FFT case selection

Interactive engineering dashboards

Saving static snapshots from interactive analyses

When interactive plots are useful

When they are unsuitable for journal publication

and how interactive exploration should lead to a
reproducible static final figure.
"""
