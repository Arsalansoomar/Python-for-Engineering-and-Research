"""
============================================================
Python for Engineering and Research
25 - Contour and Parameter-Sweep Plots
============================================================

Purpose:
    Demonstrate how contour and filled-contour plots can be
    used to visualize multidimensional engineering response
    surfaces, parameter sweeps, operating limits, feasible
    regions, and optimization results.

Topics:
    1. What is a contour plot?
    2. Parameter-sweep concept
    3. np.meshgrid()
    4. Response matrices
    5. contour()
    6. contourf()
    7. Contour levels
    8. Contour labels
    9. Colorbars
    10. Sequential colormaps
    11. Diverging colormaps
    12. Heatmap vs contour plot
    13. Efficiency maps
    14. Power-loss maps
    15. Temperature maps
    16. Difference contour maps
    17. Threshold contours
    18. Engineering constraints
    19. Feasible regions
    20. Multiple-response overlays
    21. Optimum-point identification
    22. Best sampled point vs true optimum
    23. Fine vs coarse parameter sweeps
    24. Long-form DataFrame to contour grid
    25. Missing values
    26. Irregular scattered data
    27. tricontour()
    28. tricontourf()
    29. Reusable contour functions
    30. Saving processed sweep data
    31. Saving PNG / PDF / SVG
    32. Common mistakes
    33. Key takeaways

Important:
    A contour plot is a visualization of a numerical
    response surface.

    It does NOT automatically perform optimization or prove
    that the displayed best point is the global optimum.

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. REQUIRED LIBRARIES
# ============================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pathlib import Path


# ============================================================
# 2. WHAT IS A CONTOUR PLOT?
# ============================================================

"""
A contour plot represents a three-variable relationship:

X Parameter
    +
Y Parameter
    ↓
Response Z


Example:

Switching Frequency
        +
Load
        ↓
Efficiency


A contour line connects locations having approximately
the same response value.

Conceptually:

95.0% contour
-------------------

95.5% contour
-------------------

96.0% contour
-------------------


This is similar to elevation contours on a geographical
map.

Instead of elevation, engineering contours may represent:

Efficiency

Power loss

Temperature

Voltage ripple

THD

EMI magnitude

Control error

Prediction error
"""


# ============================================================
# 3. HEATMAP VS CONTOUR
# ============================================================

"""
HEATMAP

Represents values primarily through:

Color


------------------------------------------------------------


CONTOUR

Represents equal-value locations using:

Lines


------------------------------------------------------------


FILLED CONTOUR

Combines:

Color regions
+
Contour-level boundaries


These visualizations are complementary.
"""


# ============================================================
# 4. ENGINEERING PARAMETER-SWEEP WORKFLOW
# ============================================================

"""
Parameter X
    ↓
Select Values

Parameter Y
    ↓
Select Values

        ↓

Evaluate Every Combination

        ↓

Response Matrix

        ↓

Contour Plot

        ↓

Identify:

High-performance region

Low-performance region

Thresholds

Constraints

Candidate optimum

Design tradeoffs
"""


# ============================================================
# 5. PROJECT PATHS
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


output_figure_folder = (
    script_folder
    / "output_figures"
    / "contours"
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
# 6. DEFINE PARAMETER VALUES
# ============================================================

"""
Example engineering parameters:

X:

Switching frequency [kHz]


Y:

Load [%]
"""


switching_frequency_khz = np.linspace(

    50,

    250,

    41

)


load_percent = np.linspace(

    10,

    100,

    37

)


print(
    "\n--- Parameter Sweep ---"
)


print(
    "Switching Frequency Points:",
    len(
        switching_frequency_khz
    )
)


print(
    "Load Points:",
    len(
        load_percent
    )
)


# ============================================================
# 7. WHAT DOES meshgrid() DO?
# ============================================================

"""
The original arrays are one-dimensional:

switching_frequency_khz

and

load_percent


To evaluate a response at EVERY combination:

Frequency 1 × Load 1

Frequency 2 × Load 1

...

Frequency 1 × Load 2

...


we create coordinate matrices using:

np.meshgrid()
"""


frequency_grid, load_grid = np.meshgrid(

    switching_frequency_khz,

    load_percent

)


print(
    "\n--- Mesh Grid Shapes ---"
)


print(
    "Frequency Grid:",
    frequency_grid.shape
)


print(
    "Load Grid:",
    load_grid.shape
)


# ============================================================
# 8. MESHGRID INTERPRETATION
# ============================================================

"""
If:

X has N values

and:

Y has M values


the default 2D Cartesian meshgrid produces arrays with
shape approximately:

M × N


Therefore the response matrix Z should have the same
shape.
"""


# ============================================================
# 9. SYNTHETIC EFFICIENCY RESPONSE
# ============================================================

"""
Create a synthetic educational response surface.

The equation below is only for teaching visualization.

It is NOT intended as a physical converter model.
"""


efficiency_percent = (

    96.2

    - 0.00006
    * (
        frequency_grid
        - 135
    ) ** 2

    - 0.00038
    * (
        load_grid
        - 75
    ) ** 2

    - 0.0015
    * np.abs(
        frequency_grid
        - 135
    )

)


print(
    "\n--- Efficiency Response ---"
)


print(
    "Shape:",
    efficiency_percent.shape
)


print(
    "Minimum:",
    efficiency_percent.min()
)


print(
    "Maximum:",
    efficiency_percent.max()
)


# ============================================================
# 10. BASIC CONTOUR LINES
# ============================================================

"""
Basic syntax:

ax.contour(
    X,
    Y,
    Z
)


This produces contour lines.
"""


fig, ax = plt.subplots(
    figsize=(8, 5)
)


contours = ax.contour(

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

ax.set_title(
    "Efficiency Contour Lines"
)


plt.tight_layout()

plt.show()


# ============================================================
# 11. LABEL CONTOUR LINES
# ============================================================

"""
Use:

ax.clabel()

to display the numerical value of contour lines.
"""


fig, ax = plt.subplots(
    figsize=(8, 5)
)


contours = ax.contour(

    frequency_grid,

    load_grid,

    efficiency_percent

)


ax.clabel(

    contours,

    inline=True,

    fontsize=8,

    fmt="%.1f"

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_title(
    "Labeled Efficiency Contours"
)


plt.tight_layout()

plt.show()


# ============================================================
# 12. FILLED CONTOUR
# ============================================================

"""
Use:

contourf()

for filled contour regions.
"""


fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled_contours = ax.contourf(

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

ax.set_title(
    "Filled Efficiency Contours"
)


plt.tight_layout()

plt.show()


# ============================================================
# 13. ADD COLORBAR
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled_contours = ax.contourf(

    frequency_grid,

    load_grid,

    efficiency_percent

)


colorbar = fig.colorbar(

    filled_contours,

    ax=ax

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

ax.set_title(
    "Efficiency Parameter Map"
)


plt.tight_layout()

plt.show()


# ============================================================
# 14. NUMBER OF CONTOUR LEVELS
# ============================================================

"""
Contour density can be controlled using:

levels=


Example:

levels=12


requests a useful set of contour intervals around the
numerical range.
"""


fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled_contours = ax.contourf(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=12

)


colorbar = fig.colorbar(
    filled_contours,
    ax=ax
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


plt.tight_layout()

plt.show()


# ============================================================
# 15. EXPLICIT CONTOUR LEVELS
# ============================================================

"""
For engineering work, explicitly defined contour levels can
be more meaningful.

Example:

93.0%

93.5%

94.0%

...

96.0%
"""


efficiency_levels = np.arange(

    92.0,

    96.51,

    0.5

)


print(
    "\n--- Efficiency Contour Levels ---"
)


print(
    efficiency_levels
)


# ============================================================
# 16. EXPLICIT LEVEL PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled_contours = ax.contourf(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=efficiency_levels,

    cmap="viridis",

    extend="both"

)


line_contours = ax.contour(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=efficiency_levels,

    linewidths=0.7

)


ax.clabel(

    line_contours,

    inline=True,

    fontsize=7,

    fmt="%.1f"

)


colorbar = fig.colorbar(
    filled_contours,
    ax=ax
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

ax.set_title(
    "Efficiency Contour Map"
)


plt.tight_layout()

plt.show()


# ============================================================
# 17. WHY EXPLICIT LEVELS ARE USEFUL
# ============================================================

"""
Explicit contour levels can represent meaningful values.

Examples:

Efficiency:

94%

95%

96%


Temperature:

60 °C

80 °C

100 °C


Power Loss:

10 W

15 W

20 W


EMI Margin:

0 dB

3 dB

6 dB


This makes the contour map easier to connect to engineering
requirements.
"""


# ============================================================
# 18. CONTOUR LINE + FILLED CONTOUR
# ============================================================

"""
A common publication-style approach combines:

contourf()

for color regions

and:

contour()

for numerical boundaries.
"""


fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=20,

    cmap="viridis"

)


lines = ax.contour(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=np.arange(
        93,
        96.5,
        0.5
    ),

    linewidths=0.8

)


ax.clabel(

    lines,

    inline=True,

    fontsize=7,

    fmt="%.1f%%"

)


colorbar = fig.colorbar(
    filled,
    ax=ax
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


plt.tight_layout()

plt.show()


# ============================================================
# 19. POWER-LOSS RESPONSE
# ============================================================

"""
Create another synthetic engineering response.

For power loss:

LOWER is generally preferable.
"""


power_loss_w = (

    4.0

    + 0.00018
    * (
        frequency_grid
        - 80
    ) ** 2

    + 0.0012
    * (
        load_grid
        - 20
    ) ** 2

    + 0.025
    * load_grid

)


print(
    "\n--- Power Loss Range ---"
)


print(
    power_loss_w.min()
)


print(
    power_loss_w.max()
)


# ============================================================
# 20. POWER-LOSS CONTOUR MAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    frequency_grid,

    load_grid,

    power_loss_w,

    levels=18,

    cmap="viridis"

)


lines = ax.contour(

    frequency_grid,

    load_grid,

    power_loss_w,

    levels=8,

    linewidths=0.8

)


ax.clabel(

    lines,

    inline=True,

    fontsize=7,

    fmt="%.1f"

)


colorbar = fig.colorbar(
    filled,
    ax=ax
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

ax.set_title(
    "Power-Loss Parameter Map"
)


plt.tight_layout()

plt.show()


# ============================================================
# 21. TEMPERATURE RESPONSE
# ============================================================

"""
Temperature may depend on:

Power loss

Load

Cooling conditions

Ambient temperature


For teaching:

create a simple synthetic temperature map.
"""


temperature_c = (

    30

    + 2.15
    * power_loss_w

    + 0.06
    * load_grid

)


print(
    "\n--- Temperature Range ---"
)


print(
    temperature_c.min()
)


print(
    temperature_c.max()
)


# ============================================================
# 22. TEMPERATURE CONTOUR MAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    frequency_grid,

    load_grid,

    temperature_c,

    levels=18,

    cmap="inferno"

)


temperature_lines = ax.contour(

    frequency_grid,

    load_grid,

    temperature_c,

    levels=[
        60,
        80,
        100
    ],

    linewidths=1.0

)


ax.clabel(

    temperature_lines,

    inline=True,

    fontsize=8,

    fmt="%d °C"

)


colorbar = fig.colorbar(
    filled,
    ax=ax
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

ax.set_title(
    "Temperature Operating Map"
)


plt.tight_layout()

plt.show()


# ============================================================
# 23. DIFFERENCE CONTOUR MAP
# ============================================================

"""
Suppose two engineering designs produce different
efficiency surfaces.

A difference map can show where each design performs
better.
"""


design_a_efficiency = (

    efficiency_percent

    - 0.15

    - 0.15
    * np.sin(
        frequency_grid
        / 35
    )

)


design_b_efficiency = (

    efficiency_percent

    + 0.20

    - 0.20
    * np.cos(
        load_grid
        / 18
    )

)


efficiency_difference = (

    design_b_efficiency

    - design_a_efficiency

)


# ============================================================
# 24. SYMMETRIC DIFFERENCE LEVELS
# ============================================================

maximum_absolute_difference = np.max(

    np.abs(
        efficiency_difference
    )

)


difference_levels = np.linspace(

    -maximum_absolute_difference,

    maximum_absolute_difference,

    17

)


# ============================================================
# 25. DIVERGING CONTOUR MAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    frequency_grid,

    load_grid,

    efficiency_difference,

    levels=difference_levels,

    cmap="coolwarm",

    extend="both"

)


zero_contour = ax.contour(

    frequency_grid,

    load_grid,

    efficiency_difference,

    levels=[
        0
    ],

    linewidths=1.5

)


ax.clabel(

    zero_contour,

    fmt="Equal",

    inline=True,

    fontsize=8

)


colorbar = fig.colorbar(
    filled,
    ax=ax
)


colorbar.set_label(
    "Design B - Design A [percentage points]"
)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_title(
    "Efficiency Difference Map"
)


plt.tight_layout()

plt.show()


# ============================================================
# 26. INTERPRET DIFFERENCE MAP
# ============================================================

"""
For:

Design B - Design A


Positive region:

Design B has higher efficiency.


Negative region:

Design A has higher efficiency.


Zero contour:

Both designs have equal efficiency according to the
sampled response surfaces.


Remember:

Percentage-point difference

is different from:

Relative percentage improvement.
"""


# ============================================================
# 27. ENGINEERING THRESHOLD CONTOUR
# ============================================================

"""
Suppose the design objective requires:

Efficiency >= 95%


The:

95% contour

becomes an engineering boundary.
"""


efficiency_requirement = 95.0


fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=20,

    cmap="viridis"

)


requirement_line = ax.contour(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=[
        efficiency_requirement
    ],

    linewidths=2.0

)


ax.clabel(

    requirement_line,

    fmt={
        efficiency_requirement:
            "95% requirement"
    },

    inline=True,

    fontsize=8

)


colorbar = fig.colorbar(
    filled,
    ax=ax
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


plt.tight_layout()

plt.show()


# ============================================================
# 28. TEMPERATURE LIMIT CONTOUR
# ============================================================

"""
Now add another engineering requirement:

Temperature <= 80 °C
"""


temperature_limit = 80.0


fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=20,

    cmap="viridis"

)


efficiency_boundary = ax.contour(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=[
        efficiency_requirement
    ],

    linewidths=2

)


temperature_boundary = ax.contour(

    frequency_grid,

    load_grid,

    temperature_c,

    levels=[
        temperature_limit
    ],

    linewidths=2,

    linestyles="--"

)


ax.clabel(

    efficiency_boundary,

    fmt={
        efficiency_requirement:
            "η = 95%"
    },

    fontsize=8

)


ax.clabel(

    temperature_boundary,

    fmt={
        temperature_limit:
            "T = 80°C"
    },

    fontsize=8

)


colorbar = fig.colorbar(
    filled,
    ax=ax
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

ax.set_title(
    "Efficiency with Thermal Constraint"
)


plt.tight_layout()

plt.show()


# ============================================================
# 29. FEASIBLE REGION
# ============================================================

"""
Define a feasible operating point as:

Efficiency >= 95%

AND

Temperature <= 80 °C
"""


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

)


print(
    "\n--- Number of Feasible Grid Points ---"
)


print(
    feasible_region.sum()
)


print(
    "Total Grid Points:"
)


print(
    feasible_region.size
)


# ============================================================
# 30. FEASIBLE PERCENTAGE OF SAMPLED GRID
# ============================================================

feasible_sample_percentage = (

    feasible_region.mean()

    * 100

)


print(
    "\nFeasible Sampled Grid Points:"
)


print(
    f"{feasible_sample_percentage:.2f}%"
)


# ============================================================
# 31. FEASIBLE-REGION MAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=20,

    cmap="viridis"

)


# Efficiency boundary

ax.contour(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=[
        efficiency_requirement
    ],

    linewidths=1.8

)


# Temperature boundary

ax.contour(

    frequency_grid,

    load_grid,

    temperature_c,

    levels=[
        temperature_limit
    ],

    linewidths=1.8,

    linestyles="--"

)


# Feasible-region hatch

ax.contourf(

    frequency_grid,

    load_grid,

    feasible_region.astype(
        float
    ),

    levels=[
        0.5,
        1.5
    ],

    colors="none",

    hatches=[
        "////"
    ]

)


colorbar = fig.colorbar(
    filled,
    ax=ax
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

ax.set_title(
    "Feasible Engineering Operating Region"
)


plt.tight_layout()

plt.show()


# ============================================================
# 32. FEASIBLE REGION INTERPRETATION
# ============================================================

"""
The feasible region answers:

Where do ALL specified constraints hold?


Example:

Efficiency >= 95%

AND

Temperature <= 80 °C


Additional constraints could include:

Power Loss <= Limit

Voltage Ripple <= Limit

THD <= Limit

EMI <= Limit

Current <= Device Rating
"""


# ============================================================
# 33. ADD POWER-LOSS CONSTRAINT
# ============================================================

power_loss_limit = 15.0


three_constraint_region = (

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
        <= power_loss_limit
    )

)


print(
    "\n--- Three-Constraint Feasible Points ---"
)


print(
    three_constraint_region.sum()
)


# ============================================================
# 34. MULTIPLE CONSTRAINT OVERLAY
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=20,

    cmap="viridis"

)


efficiency_line = ax.contour(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=[
        efficiency_requirement
    ],

    linewidths=1.7

)


temperature_line = ax.contour(

    frequency_grid,

    load_grid,

    temperature_c,

    levels=[
        temperature_limit
    ],

    linewidths=1.7,

    linestyles="--"

)


loss_line = ax.contour(

    frequency_grid,

    load_grid,

    power_loss_w,

    levels=[
        power_loss_limit
    ],

    linewidths=1.7,

    linestyles="-."

)


ax.clabel(

    efficiency_line,

    fmt={
        efficiency_requirement:
            "η ≥ 95%"
    },

    fontsize=8

)


ax.clabel(

    temperature_line,

    fmt={
        temperature_limit:
            "T ≤ 80°C"
    },

    fontsize=8

)


ax.clabel(

    loss_line,

    fmt={
        power_loss_limit:
            "Loss ≤ 15 W"
    },

    fontsize=8

)


ax.contourf(

    frequency_grid,

    load_grid,

    three_constraint_region.astype(
        float
    ),

    levels=[
        0.5,
        1.5
    ],

    colors="none",

    hatches=[
        "////"
    ]

)


colorbar = fig.colorbar(
    filled,
    ax=ax
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

ax.set_title(
    "Multi-Constraint Operating Map"
)


plt.tight_layout()

plt.show()


# ============================================================
# 35. FIND BEST SAMPLED EFFICIENCY POINT
# ============================================================

maximum_index = np.unravel_index(

    np.argmax(
        efficiency_percent
    ),

    efficiency_percent.shape

)


best_frequency = frequency_grid[
    maximum_index
]


best_load = load_grid[
    maximum_index
]


best_efficiency = efficiency_percent[
    maximum_index
]


print(
    "\n--- Best Sampled Efficiency Point ---"
)


print(
    f"Frequency = "
    f"{best_frequency:.2f} kHz"
)


print(
    f"Load = "
    f"{best_load:.2f}%"
)


print(
    f"Efficiency = "
    f"{best_efficiency:.4f}%"
)


# ============================================================
# 36. MARK BEST POINT
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=20,

    cmap="viridis"

)


ax.contour(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=np.arange(
        93,
        96.5,
        0.5
    ),

    linewidths=0.7

)


ax.scatter(

    best_frequency,

    best_load,

    marker="*",

    s=150,

    label="Best sampled point"

)


ax.annotate(

    (
        f"{best_efficiency:.2f}%\n"
        f"{best_frequency:.0f} kHz, "
        f"{best_load:.0f}%"
    ),

    xy=(
        best_frequency,
        best_load
    ),

    xytext=(
        25,
        -40
    ),

    textcoords="offset points",

    arrowprops={
        "arrowstyle":
            "->"
    }

)


colorbar = fig.colorbar(
    filled,
    ax=ax
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


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 37. BEST SAMPLED POINT != GLOBAL OPTIMUM
# ============================================================

"""
The best point from:

np.argmax(
    sampled_response
)

means:

Best point in the evaluated grid.


It does NOT automatically prove:

Global optimum


between grid points.


A finer sweep or formal optimization method may identify a
different optimum.
"""


# ============================================================
# 38. BEST FEASIBLE POINT
# ============================================================

"""
The highest-efficiency point may violate other constraints.

Therefore optimization often needs to search only inside
the feasible region.
"""


feasible_efficiency = np.where(

    three_constraint_region,

    efficiency_percent,

    np.nan

)


if np.any(
    np.isfinite(
        feasible_efficiency
    )
):

    feasible_max_index = np.unravel_index(

        np.nanargmax(
            feasible_efficiency
        ),

        feasible_efficiency.shape

    )


    best_feasible_frequency = (
        frequency_grid[
            feasible_max_index
        ]
    )


    best_feasible_load = (
        load_grid[
            feasible_max_index
        ]
    )


    best_feasible_efficiency = (
        efficiency_percent[
            feasible_max_index
        ]
    )


    print(
        "\n--- Best Feasible Point ---"
    )


    print(
        f"Frequency = "
        f"{best_feasible_frequency:.2f} kHz"
    )


    print(
        f"Load = "
        f"{best_feasible_load:.2f}%"
    )


    print(
        f"Efficiency = "
        f"{best_feasible_efficiency:.4f}%"
    )

else:

    print(
        "\nNo feasible sampled point "
        "satisfies all constraints."
    )


# ============================================================
# 39. MARK BEST FEASIBLE POINT
# ============================================================

if np.any(
    np.isfinite(
        feasible_efficiency
    )
):

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )


    filled = ax.contourf(

        frequency_grid,

        load_grid,

        efficiency_percent,

        levels=20,

        cmap="viridis"

    )


    ax.contourf(

        frequency_grid,

        load_grid,

        three_constraint_region.astype(
            float
        ),

        levels=[
            0.5,
            1.5
        ],

        colors="none",

        hatches=[
            "////"
        ]

    )


    ax.scatter(

        best_feasible_frequency,

        best_feasible_load,

        marker="*",

        s=150,

        label="Best feasible point"

    )


    colorbar = fig.colorbar(
        filled,
        ax=ax
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


    ax.legend()


    plt.tight_layout()

    plt.show()


# ============================================================
# 40. MAXIMUM EFFICIENCY VS MINIMUM LOSS
# ============================================================

"""
Different objectives may produce different preferred
operating points.

Example:

Objective 1:

Maximize efficiency


Objective 2:

Minimize power loss


These objectives should not automatically be assumed to
produce the same operating point.
"""


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
    "\n--- Minimum Sampled Loss Point ---"
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
    f"Power Loss = "
    f"{minimum_loss_value:.3f} W"
)


# ============================================================
# 41. TWO OBJECTIVES ON ONE MAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=20,

    cmap="viridis"

)


ax.scatter(

    best_frequency,

    best_load,

    marker="*",

    s=130,

    label="Maximum efficiency"

)


ax.scatter(

    minimum_loss_frequency,

    minimum_loss_load,

    marker="X",

    s=90,

    label="Minimum loss"

)


colorbar = fig.colorbar(
    filled,
    ax=ax
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


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 42. MULTI-OBJECTIVE CONCEPT
# ============================================================

"""
Engineering optimization may involve conflicting goals.

Examples:

Maximize:

Efficiency


while minimizing:

Power loss

Temperature

EMI

Cost

Volume


A contour plot helps visualize tradeoffs,

but formal multi-objective optimization requires additional
methods.
"""


# ============================================================
# 43. COARSE PARAMETER SWEEP
# ============================================================

coarse_frequency = np.linspace(

    50,

    250,

    6

)


coarse_load = np.linspace(

    10,

    100,

    6

)


coarse_frequency_grid, coarse_load_grid = (
    np.meshgrid(

        coarse_frequency,

        coarse_load

    )
)


coarse_efficiency = (

    96.2

    - 0.00006
    * (
        coarse_frequency_grid
        - 135
    ) ** 2

    - 0.00038
    * (
        coarse_load_grid
        - 75
    ) ** 2

    - 0.0015
    * np.abs(
        coarse_frequency_grid
        - 135
    )

)


# ============================================================
# 44. COARSE CONTOUR MAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    coarse_frequency_grid,

    coarse_load_grid,

    coarse_efficiency,

    levels=15,

    cmap="viridis"

)


ax.scatter(

    coarse_frequency_grid,

    coarse_load_grid,

    s=15,

    label="Evaluated points"

)


colorbar = fig.colorbar(
    filled,
    ax=ax
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


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 45. FINE VS COARSE SWEEP
# ============================================================

"""
A smooth-looking contour does NOT automatically mean that
many physical simulations or measurements were performed.

Contour algorithms can visually connect available points.

Therefore researchers should report:

Parameter ranges

Step sizes

Number of evaluated cases

Interpolation method if used
"""


# ============================================================
# 46. SAVE PARAMETER SWEEP IN LONG-FORM DATAFRAME
# ============================================================

parameter_sweep_dataframe = pd.DataFrame(
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
            temperature_c.ravel(),

        "Feasible":
            three_constraint_region.ravel()
    }
)


print(
    "\n--- Long-Form Parameter Sweep ---"
)


print(
    parameter_sweep_dataframe.head()
)


# ============================================================
# 47. SAVE LONG-FORM DATA
# ============================================================

parameter_sweep_file = (
    output_data_folder
    / "contour_parameter_sweep.csv"
)


parameter_sweep_dataframe.to_csv(

    parameter_sweep_file,

    index=False

)


print(
    "\nParameter Sweep Saved:"
)


print(
    parameter_sweep_file
)


# ============================================================
# 48. DATAFRAME TO GRID USING pivot()
# ============================================================

"""
Real simulation results are often stored in long form:

Frequency | Load | Efficiency
--------------------------------
50        | 10   | ...
55        | 10   | ...
60        | 10   | ...
...


For contour plotting:

pivot()

can convert this into a 2D response matrix.
"""


efficiency_pivot = parameter_sweep_dataframe.pivot(

    index="Load_percent",

    columns="Switching_Frequency_kHz",

    values="Efficiency_percent"

)


print(
    "\n--- Pivoted Efficiency Matrix ---"
)


print(
    efficiency_pivot.iloc[
        :5,
        :5
    ]
)


# ============================================================
# 49. EXTRACT GRID FROM PIVOT TABLE
# ============================================================

pivot_load = efficiency_pivot.index.to_numpy(
    dtype=float
)


pivot_frequency = (
    efficiency_pivot.columns.to_numpy(
        dtype=float
    )
)


pivot_efficiency = efficiency_pivot.to_numpy(
    dtype=float
)


# ============================================================
# 50. CONTOUR FROM DATAFRAME
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    pivot_frequency,

    pivot_load,

    pivot_efficiency,

    levels=20,

    cmap="viridis"

)


colorbar = fig.colorbar(
    filled,
    ax=ax
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

ax.set_title(
    "Contour Plot from DataFrame"
)


plt.tight_layout()

plt.show()


# ============================================================
# 51. DUPLICATE PARAMETER COMBINATIONS
# ============================================================

"""
pivot() expects each:

X + Y

combination to map to one response value.


If repeated measurements exist at the same operating point,
you may need to calculate:

Mean

Median

Minimum

Maximum


before constructing the contour grid.


Example:

groupby()

or

pivot_table()
"""


# ============================================================
# 52. PIVOT TABLE WITH REPEATED DATA
# ============================================================

repeated_sweep_data = pd.concat(
    [
        parameter_sweep_dataframe,

        parameter_sweep_dataframe.assign(
            Efficiency_percent=(
                parameter_sweep_dataframe[
                    "Efficiency_percent"
                ]
                + 0.05
            )
        )
    ],

    ignore_index=True

)


average_pivot = repeated_sweep_data.pivot_table(

    index="Load_percent",

    columns="Switching_Frequency_kHz",

    values="Efficiency_percent",

    aggfunc="mean"

)


print(
    "\n--- Averaged Repeated Sweep ---"
)


print(
    average_pivot.iloc[
        :4,
        :4
    ]
)


# ============================================================
# 53. MISSING GRID VALUES
# ============================================================

"""
Real parameter sweeps may contain missing cases.

Possible reasons:

Simulation failure

Measurement failure

Unsafe operating point

Solver convergence problem

Data unavailable


Do not automatically replace missing values with zero.
"""


missing_efficiency = efficiency_percent.copy()


missing_efficiency[
    8:13,
    12:18
] = np.nan


masked_efficiency = np.ma.masked_invalid(
    missing_efficiency
)


# ============================================================
# 54. CONTOUR WITH MASKED DATA
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


filled = ax.contourf(

    frequency_grid,

    load_grid,

    masked_efficiency,

    levels=20,

    cmap="viridis"

)


colorbar = fig.colorbar(
    filled,
    ax=ax
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

ax.set_title(
    "Contour Map with Missing Region"
)


plt.tight_layout()

plt.show()


# ============================================================
# 55. MISSING DATA WARNING
# ============================================================

"""
Missing parameter points should remain traceable.

Do not make a missing simulation appear to be:

0% efficiency

0 W loss

0 °C


unless zero is physically correct.
"""


# ============================================================
# 56. IRREGULAR SCATTERED PARAMETER DATA
# ============================================================

"""
Not every engineering dataset is measured on a perfect
rectangular grid.

Example:

Randomly selected parameter combinations

Adaptive DOE

Experimental limitations

Optimization samples


Such datasets contain:

X point

Y point

Z response


without a complete rectangular matrix.
"""


rng = np.random.default_rng(
    42
)


irregular_frequency = rng.uniform(

    50,

    250,

    180

)


irregular_load = rng.uniform(

    10,

    100,

    180

)


irregular_efficiency = (

    96.2

    - 0.00006
    * (
        irregular_frequency
        - 135
    ) ** 2

    - 0.00038
    * (
        irregular_load
        - 75
    ) ** 2

    - 0.0015
    * np.abs(
        irregular_frequency
        - 135
    )

)


# ============================================================
# 57. SHOW IRREGULAR SAMPLE LOCATIONS
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


scatter = ax.scatter(

    irregular_frequency,

    irregular_load,

    c=irregular_efficiency,

    s=25,

    cmap="viridis"

)


colorbar = fig.colorbar(
    scatter,
    ax=ax
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

ax.set_title(
    "Irregular Parameter Samples"
)


plt.tight_layout()

plt.show()


# ============================================================
# 58. tricontourf() FOR IRREGULAR DATA
# ============================================================

"""
For scattered points:

tricontourf()

can construct filled contours on a triangulated
unstructured grid.
"""


fig, ax = plt.subplots(
    figsize=(8, 5)
)


tri_filled = ax.tricontourf(

    irregular_frequency,

    irregular_load,

    irregular_efficiency,

    levels=20,

    cmap="viridis"

)


colorbar = fig.colorbar(
    tri_filled,
    ax=ax
)


colorbar.set_label(
    "Efficiency [%]"
)


ax.scatter(

    irregular_frequency,

    irregular_load,

    s=8,

    alpha=0.4

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_title(
    "Filled Contours from Irregular Samples"
)


plt.tight_layout()

plt.show()


# ============================================================
# 59. tricontour() LINES
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


tri_lines = ax.tricontour(

    irregular_frequency,

    irregular_load,

    irregular_efficiency,

    levels=np.arange(
        93,
        96.5,
        0.5
    )

)


ax.clabel(

    tri_lines,

    inline=True,

    fontsize=8,

    fmt="%.1f"

)


ax.scatter(

    irregular_frequency,

    irregular_load,

    s=10

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)

ax.set_title(
    "Contour Lines from Irregular Data"
)


plt.tight_layout()

plt.show()


# ============================================================
# 60. IRREGULAR-DATA WARNING
# ============================================================

"""
A triangulated contour contains interpolated visual
regions between measured or simulated points.

Therefore the contour surface should not be interpreted as
if every displayed location was actually evaluated.

Show or document the original sample points when that
distinction matters.
"""


# ============================================================
# 61. DESIGN OF EXPERIMENTS CONNECTION
# ============================================================

"""
Irregular parameter samples are common in:

DOE

Latin hypercube sampling

Optimization algorithms

Adaptive sampling

Machine-learning datasets


In such cases, useful visualizations include:

Scatter maps

tricontour()

tricontourf()

Surrogate-model predictions


The appropriate visualization depends on how the response
surface was obtained.
"""


# ============================================================
# 62. REUSABLE CONTOUR FUNCTION
# ============================================================

def plot_contour_map(
    x,
    y,
    z,
    x_label,
    y_label,
    colorbar_label,
    title=None,
    levels=20,
    cmap="viridis",
    show_lines=True,
    line_levels=None
):
    """
    Create a reusable filled contour map.

    Parameters
    ----------
    x : array-like
        X coordinates.

    y : array-like
        Y coordinates.

    z : 2D array-like
        Response matrix.

    x_label : str
        X-axis label including units.

    y_label : str
        Y-axis label including units.

    colorbar_label : str
        Response variable and units.

    title : str, optional
        Figure title.

    levels : int or array-like
        Filled contour levels.

    cmap : str
        Matplotlib colormap.

    show_lines : bool
        Overlay contour lines.

    line_levels : int or array-like, optional
        Line contour levels.

    Returns
    -------
    fig, ax
        Matplotlib figure and axis.
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


    if z.ndim != 2:

        raise ValueError(
            "Z must be a two-dimensional "
            "response matrix."
        )


    if x.ndim == 1 and y.ndim == 1:

        expected_shape = (

            len(
                y
            ),

            len(
                x
            )

        )


        if z.shape != expected_shape:

            raise ValueError(
                "For 1D X and Y arrays, "
                "Z must have shape "
                "(len(y), len(x))."
            )


    fig, ax = plt.subplots(
        figsize=(8, 5)
    )


    filled = ax.contourf(

        x,

        y,

        np.ma.masked_invalid(
            z
        ),

        levels=levels,

        cmap=cmap

    )


    colorbar = fig.colorbar(
        filled,
        ax=ax
    )


    colorbar.set_label(
        colorbar_label
    )


    if show_lines:

        if line_levels is None:

            line_levels = levels


        lines = ax.contour(

            x,

            y,

            np.ma.masked_invalid(
                z
            ),

            levels=line_levels,

            linewidths=0.7

        )


        ax.clabel(

            lines,

            inline=True,

            fontsize=7,

            fmt="%.2g"

        )


    ax.set_xlabel(
        x_label
    )


    ax.set_ylabel(
        y_label
    )


    if title is not None:

        ax.set_title(
            title
        )


    plt.tight_layout()


    return (
        fig,
        ax
    )


# ============================================================
# 63. USE REUSABLE CONTOUR FUNCTION
# ============================================================

fig, ax = plot_contour_map(

    x=switching_frequency_khz,

    y=load_percent,

    z=efficiency_percent,

    x_label=(
        "Switching Frequency [kHz]"
    ),

    y_label="Load [%]",

    colorbar_label="Efficiency [%]",

    title="Reusable Efficiency Contour Map",

    levels=20,

    cmap="viridis",

    show_lines=True,

    line_levels=np.arange(
        93,
        96.5,
        0.5
    )

)


plt.show()


# ============================================================
# 64. REUSABLE IRREGULAR-CONTOUR FUNCTION
# ============================================================

def plot_irregular_contour(
    x,
    y,
    z,
    x_label,
    y_label,
    colorbar_label,
    title=None,
    levels=20,
    cmap="viridis",
    show_points=True
):
    """
    Create a filled contour map from scattered data using
    triangulation.

    Parameters
    ----------
    x, y : array-like
        Scattered coordinates.

    z : array-like
        Response at each coordinate pair.

    x_label, y_label : str
        Axis labels.

    colorbar_label : str
        Response label.

    title : str, optional
        Figure title.

    levels : int or array-like
        Contour levels.

    cmap : str
        Colormap.

    show_points : bool
        Display original sample locations.

    Returns
    -------
    fig, ax
        Matplotlib figure and axis.
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
        len(
            x
        )
        ==
        len(
            y
        )
        ==
        len(
            z
        )
    ):

        raise ValueError(
            "X, Y, and Z must contain "
            "the same number of points."
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
        z
    ) < 3:

        raise ValueError(
            "At least three valid scattered "
            "points are required."
        )


    fig, ax = plt.subplots(
        figsize=(8, 5)
    )


    filled = ax.tricontourf(

        x,

        y,

        z,

        levels=levels,

        cmap=cmap

    )


    colorbar = fig.colorbar(
        filled,
        ax=ax
    )


    colorbar.set_label(
        colorbar_label
    )


    if show_points:

        ax.scatter(

            x,

            y,

            s=8,

            alpha=0.4

        )


    ax.set_xlabel(
        x_label
    )


    ax.set_ylabel(
        y_label
    )


    if title is not None:

        ax.set_title(
            title
        )


    plt.tight_layout()


    return (
        fig,
        ax
    )


# ============================================================
# 65. USE IRREGULAR-CONTOUR FUNCTION
# ============================================================

fig, ax = plot_irregular_contour(

    x=irregular_frequency,

    y=irregular_load,

    z=irregular_efficiency,

    x_label=(
        "Switching Frequency [kHz]"
    ),

    y_label="Load [%]",

    colorbar_label="Efficiency [%]",

    title=(
        "Irregular Engineering Parameter Sweep"
    ),

    levels=20,

    cmap="viridis",

    show_points=True

)


plt.show()


# ============================================================
# 66. REUSABLE OPTIMUM FINDER
# ============================================================

def find_grid_optimum(
    x_grid,
    y_grid,
    response,
    objective="maximum",
    valid_mask=None
):
    """
    Find the best sampled point on a response grid.

    Parameters
    ----------
    x_grid : 2D array
        X coordinates.

    y_grid : 2D array
        Y coordinates.

    response : 2D array
        Numerical response.

    objective : str
        "maximum" or "minimum".

    valid_mask : 2D bool array, optional
        Restrict search to valid/feasible points.

    Returns
    -------
    result : dict
        X, Y, response value, and matrix index.
    """

    x_grid = np.asarray(
        x_grid,
        dtype=float
    )


    y_grid = np.asarray(
        y_grid,
        dtype=float
    )


    response = np.asarray(
        response,
        dtype=float
    )


    if not (
        x_grid.shape
        ==
        y_grid.shape
        ==
        response.shape
    ):

        raise ValueError(
            "X grid, Y grid, and response "
            "must have identical shapes."
        )


    if objective not in {
        "maximum",
        "minimum"
    }:

        raise ValueError(
            "objective must be "
            "'maximum' or 'minimum'."
        )


    search_response = response.copy()


    finite_mask = np.isfinite(
        search_response
    )


    if valid_mask is not None:

        valid_mask = np.asarray(
            valid_mask,
            dtype=bool
        )


        if valid_mask.shape != response.shape:

            raise ValueError(
                "valid_mask must match "
                "response shape."
            )


        finite_mask = (

            finite_mask

            & valid_mask

        )


    if not np.any(
        finite_mask
    ):

        raise ValueError(
            "No valid points available "
            "for optimization."
        )


    if objective == "maximum":

        working = np.where(

            finite_mask,

            search_response,

            np.nan

        )


        index = np.unravel_index(

            np.nanargmax(
                working
            ),

            working.shape

        )

    else:

        working = np.where(

            finite_mask,

            search_response,

            np.nan

        )


        index = np.unravel_index(

            np.nanargmin(
                working
            ),

            working.shape

        )


    return {

        "index":
            index,

        "x":
            x_grid[
                index
            ],

        "y":
            y_grid[
                index
            ],

        "response":
            response[
                index
            ]

    }


# ============================================================
# 67. USE OPTIMUM FINDER
# ============================================================

optimum_result = find_grid_optimum(

    x_grid=frequency_grid,

    y_grid=load_grid,

    response=efficiency_percent,

    objective="maximum"

)


print(
    "\n--- Reusable Optimum Function ---"
)


print(
    optimum_result
)


# ============================================================
# 68. FEASIBLE OPTIMUM
# ============================================================

feasible_optimum_result = find_grid_optimum(

    x_grid=frequency_grid,

    y_grid=load_grid,

    response=efficiency_percent,

    objective="maximum",

    valid_mask=three_constraint_region

)


print(
    "\n--- Feasible Optimum Function ---"
)


print(
    feasible_optimum_result
)


# ============================================================
# 69. REUSABLE FEASIBILITY FUNCTION
# ============================================================

def calculate_feasible_region(
    efficiency,
    temperature,
    power_loss,
    minimum_efficiency,
    maximum_temperature,
    maximum_power_loss
):
    """
    Calculate a boolean engineering feasibility map.
    """

    efficiency = np.asarray(
        efficiency,
        dtype=float
    )


    temperature = np.asarray(
        temperature,
        dtype=float
    )


    power_loss = np.asarray(
        power_loss,
        dtype=float
    )


    if not (
        efficiency.shape
        ==
        temperature.shape
        ==
        power_loss.shape
    ):

        raise ValueError(
            "All response matrices must "
            "have the same shape."
        )


    return (

        (
            efficiency
            >= minimum_efficiency
        )

        &

        (
            temperature
            <= maximum_temperature
        )

        &

        (
            power_loss
            <= maximum_power_loss
        )

    )


# ============================================================
# 70. USE FEASIBILITY FUNCTION
# ============================================================

automatic_feasible_region = (
    calculate_feasible_region(

        efficiency=efficiency_percent,

        temperature=temperature_c,

        power_loss=power_loss_w,

        minimum_efficiency=95.0,

        maximum_temperature=80.0,

        maximum_power_loss=15.0

    )
)


print(
    "\nAutomatic Feasible Points:"
)


print(
    automatic_feasible_region.sum()
)


# ============================================================
# 71. FINAL PUBLICATION-STYLE CONTOUR FIGURE
# ============================================================

"""
Final figure:

Background:

Efficiency


Contour 1:

95% efficiency requirement


Contour 2:

80 °C thermal limit


Contour 3:

15 W loss limit


Hatching:

Feasible region


Star:

Best feasible sampled point
"""


fig, ax = plt.subplots(
    figsize=(8, 5.5)
)


filled = ax.contourf(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=np.linspace(
        efficiency_percent.min(),
        efficiency_percent.max(),
        18
    ),

    cmap="viridis"

)


# ------------------------------------------------------------
# Efficiency threshold
# ------------------------------------------------------------

efficiency_line = ax.contour(

    frequency_grid,

    load_grid,

    efficiency_percent,

    levels=[
        efficiency_requirement
    ],

    linewidths=1.7

)


# ------------------------------------------------------------
# Temperature threshold
# ------------------------------------------------------------

temperature_line = ax.contour(

    frequency_grid,

    load_grid,

    temperature_c,

    levels=[
        temperature_limit
    ],

    linewidths=1.7,

    linestyles="--"

)


# ------------------------------------------------------------
# Power-loss threshold
# ------------------------------------------------------------

loss_line = ax.contour(

    frequency_grid,

    load_grid,

    power_loss_w,

    levels=[
        power_loss_limit
    ],

    linewidths=1.7,

    linestyles="-."

)


# ------------------------------------------------------------
# Feasible region
# ------------------------------------------------------------

ax.contourf(

    frequency_grid,

    load_grid,

    three_constraint_region.astype(
        float
    ),

    levels=[
        0.5,
        1.5
    ],

    colors="none",

    hatches=[
        "////"
    ]

)


# ------------------------------------------------------------
# Best feasible point
# ------------------------------------------------------------

ax.scatter(

    feasible_optimum_result[
        "x"
    ],

    feasible_optimum_result[
        "y"
    ],

    marker="*",

    s=150,

    label="Best feasible sampled point"

)


# ------------------------------------------------------------
# Labels
# ------------------------------------------------------------

ax.clabel(

    efficiency_line,

    fmt={
        efficiency_requirement:
            "η = 95%"
    },

    fontsize=8

)


ax.clabel(

    temperature_line,

    fmt={
        temperature_limit:
            "T = 80°C"
    },

    fontsize=8

)


ax.clabel(

    loss_line,

    fmt={
        power_loss_limit:
            "Loss = 15 W"
    },

    fontsize=8

)


# ------------------------------------------------------------
# Colorbar
# ------------------------------------------------------------

colorbar = fig.colorbar(
    filled,
    ax=ax
)


colorbar.set_label(
    "Efficiency [%]"
)


# ------------------------------------------------------------
# Axis formatting
# ------------------------------------------------------------

ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)


ax.legend(
    loc="best"
)


plt.tight_layout()


# ============================================================
# 72. SAVE FINAL PNG
# ============================================================

png_file = (
    output_figure_folder
    / "engineering_contour_parameter_sweep.png"
)


fig.savefig(

    png_file,

    dpi=300,

    bbox_inches="tight"

)


# ============================================================
# 73. SAVE FINAL PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "engineering_contour_parameter_sweep.pdf"
)


fig.savefig(

    pdf_file,

    bbox_inches="tight"

)


# ============================================================
# 74. SAVE FINAL SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "engineering_contour_parameter_sweep.svg"
)


fig.savefig(

    svg_file,

    bbox_inches="tight"

)


print(
    "\n--- Final Contour Figures Saved ---"
)


print(
    png_file
)


print(
    pdf_file
)


print(
    svg_file
)


plt.show()


# ============================================================
# 75. SAVE OPTIMUM SUMMARY
# ============================================================

optimum_summary = pd.DataFrame(
    [
        {
            "Metric":
                "Maximum Efficiency",

            "Switching_Frequency_kHz":
                optimum_result[
                    "x"
                ],

            "Load_percent":
                optimum_result[
                    "y"
                ],

            "Response":
                optimum_result[
                    "response"
                ]
        },

        {
            "Metric":
                "Maximum Feasible Efficiency",

            "Switching_Frequency_kHz":
                feasible_optimum_result[
                    "x"
                ],

            "Load_percent":
                feasible_optimum_result[
                    "y"
                ],

            "Response":
                feasible_optimum_result[
                    "response"
                ]
        },

        {
            "Metric":
                "Minimum Power Loss",

            "Switching_Frequency_kHz":
                minimum_loss_frequency,

            "Load_percent":
                minimum_loss_load,

            "Response":
                minimum_loss_value
        }
    ]
)


optimum_summary_file = (
    output_data_folder
    / "contour_optimum_summary.csv"
)


optimum_summary.to_csv(

    optimum_summary_file,

    index=False

)


print(
    "\n--- Optimum Summary ---"
)


print(
    optimum_summary
)


print(
    "\nSummary Saved:"
)


print(
    optimum_summary_file
)


# ============================================================
# 76. COMMON MISTAKE - CONTOUR = MEASURED EVERYWHERE
# ============================================================

"""
A contour plot may visually display a continuous surface.

This does NOT mean every displayed coordinate was
physically measured or simulated.

The surface may contain visual interpolation between
sampled points.
"""


# ============================================================
# 77. COMMON MISTAKE - TOO COARSE PARAMETER GRID
# ============================================================

"""
Suppose only:

4 frequency points

and:

4 load points


were evaluated.


A smooth contour map may look detailed,

but the underlying dataset contains only:

16 parameter combinations.


Always report the actual parameter resolution.
"""


# ============================================================
# 78. COMMON MISTAKE - TOO MANY CONTOUR LEVELS
# ============================================================

"""
Too many levels can produce:

Crowded labels

Visual noise

False sense of numerical precision


Use contour intervals appropriate to:

Measurement precision

Simulation accuracy

Engineering significance
"""


# ============================================================
# 79. COMMON MISTAKE - TOO FEW LEVELS
# ============================================================

"""
Too few levels may hide:

Local variations

Transition regions

Operating boundaries


Choose levels according to the research question.
"""


# ============================================================
# 80. COMMON MISTAKE - NON-MONOTONIC LEVELS
# ============================================================

"""
If explicit contour levels are supplied, they should be in
increasing numerical order.

Example:

Correct:

[
    90,
    92,
    94,
    96
]
"""


# ============================================================
# 81. COMMON MISTAKE - NO COLORBAR
# ============================================================

"""
For filled contours:

Color should normally have a clearly defined numerical
meaning.

Use a colorbar with:

Variable name

and

Unit.
"""


# ============================================================
# 82. COMMON MISTAKE - NO UNITS
# ============================================================

"""
Weak:

Frequency

Load

Value


Better:

Switching Frequency [kHz]

Load [%]

Efficiency [%]
"""


# ============================================================
# 83. COMMON MISTAKE - OPTIMUM WITHOUT CONSTRAINTS
# ============================================================

"""
The maximum efficiency point may violate:

Temperature limit

Current limit

Power-loss limit

EMI requirement

Device rating


Optimization should reflect all relevant engineering
constraints.
"""


# ============================================================
# 84. COMMON MISTAKE - GLOBAL OPTIMUM CLAIM
# ============================================================

"""
Finding:

np.argmax(
    sampled_response
)


identifies:

Best sampled point


It does not automatically identify the global optimum
between evaluated points.
"""


# ============================================================
# 85. COMMON MISTAKE - WRONG OBJECTIVE DIRECTION
# ============================================================

"""
For:

Efficiency

you may want:

Maximum


For:

Power loss

you may want:

Minimum


For:

Temperature

you may want:

Minimum or below a threshold


Define the objective before searching for an optimum.
"""


# ============================================================
# 86. COMMON MISTAKE - IGNORING TRADEOFFS
# ============================================================

"""
A point with:

Maximum efficiency


may not provide:

Minimum EMI

Minimum temperature

Minimum cost

Minimum volume


Engineering design often requires multiple objectives.
"""


# ============================================================
# 87. COMMON MISTAKE - DIFFERENT COLOR SCALES
# ============================================================

"""
When comparing contour maps:

Design A

vs

Design B


different color scales can make differences appear larger
or smaller than they actually are.

Use common scales where direct visual comparison is
intended.
"""


# ============================================================
# 88. COMMON MISTAKE - DIVERGING DATA WITH SEQUENTIAL SCALE
# ============================================================

"""
For signed differences around:

0


a diverging colormap can help distinguish:

Negative

Zero

Positive


Use a symmetric numerical color range when appropriate.
"""


# ============================================================
# 89. COMMON MISTAKE - MASKED DATA AS ZERO
# ============================================================

"""
Missing simulation:

NaN


should not automatically become:

0


Zero may have a completely different physical meaning.
"""


# ============================================================
# 90. COMMON MISTAKE - IRREGULAR DATA AS RECTANGULAR GRID
# ============================================================

"""
Scattered DOE or optimization samples do not automatically
form a complete rectangular matrix.

Use appropriate methods such as:

tricontour()

tricontourf()

or justified interpolation.
"""


# ============================================================
# 91. COMMON MISTAKE - OVERINTERPRETING TRIANGULATION
# ============================================================

"""
A triangulated contour estimates the visual surface between
sample locations.

Sparse regions should not be interpreted with the same
confidence as densely sampled regions without additional
validation.
"""


# ============================================================
# 92. COMMON MISTAKE - CONTOUR LINE = CONSTRAINT SATISFIED
# ============================================================

"""
A contour line such as:

T = 80 °C


represents the boundary.


You must still determine which side corresponds to:

T < 80 °C


and which side corresponds to:

T > 80 °C.


Check the underlying values.
"""


# ============================================================
# 93. COMMON MISTAKE - NO RAW DATA SAVED
# ============================================================

"""
The final contour image is not a replacement for the
numerical parameter-sweep data.

Preserve:

CSV

Excel

Database

or other numerical data files


for reproducibility.
"""


# ============================================================
# 94. COMMON MISTAKE - CONFUSING RESPONSE AND PARAMETER
# ============================================================

"""
X-axis:

Parameter


Y-axis:

Parameter


Color / contour:

Response


Example:

Frequency [kHz]
        ×
Load [%]
        ↓
Efficiency [%]


Do not mix these roles accidentally.
"""


# ============================================================
# 95. CONTOUR DECISION GUIDE
# ============================================================

"""
Need raw matrix colors?
        ↓
HEATMAP


Need equal-value boundaries?
        ↓
CONTOUR


Need continuous colored regions?
        ↓
CONTOURF


Need exact physical grid cells?
        ↓
PCOLORMESH


Need irregular scattered samples?
        ↓
TRICONTOUR / TRICONTOURF


Need 3D response surface?
        ↓
3D SURFACE PLOT
        ↓
Covered Later
"""


# ============================================================
# 96. ENGINEERING CONSTRAINT WORKFLOW
# ============================================================

"""
Parameter Sweep
        ↓
Calculate Response 1:
Efficiency
        ↓
Calculate Response 2:
Temperature
        ↓
Calculate Response 3:
Power Loss
        ↓
Define Requirements
        ↓
Efficiency >= Limit
Temperature <= Limit
Loss <= Limit
        ↓
Boolean Feasible Region
        ↓
Contour Boundaries
        ↓
Find Best Feasible Sample
        ↓
Validate Design
"""


# ============================================================
# 97. OPTIMIZATION VISUALIZATION WORKFLOW
# ============================================================

"""
Define Parameters
        ↓
Select Ranges
        ↓
Generate Parameter Combinations
        ↓
Simulation / Experiment
        ↓
Build Response Surface
        ↓
Contour Map
        ↓
Find Candidate Optimum
        ↓
Apply Constraints
        ↓
Find Feasible Optimum
        ↓
Refine Parameter Sweep
        ↓
Validate Selected Design
"""


# ============================================================
# 98. PARAMETRIC RESEARCH WORKFLOW
# ============================================================

"""
Engineering Model
      ↓
Parameter A Sweep
      ×
Parameter B Sweep
      ↓
Run Cases
      ↓
Collect Results
      ↓
Pandas DataFrame
      ↓
pivot()
      ↓
Response Matrix
      ↓
Contourf()
      ↓
Threshold Contours
      ↓
Feasible Region
      ↓
Engineering Interpretation
      ↓
Publication Figure
"""


# ============================================================
# 99. PUBLICATION CHECKLIST
# ============================================================

"""
Before publishing a contour figure, check:

PARAMETERS
------------------------------------------------------------

Are X and Y parameters clearly defined?

Are units shown?

Are ranges stated?

Are sweep step sizes known?


RESPONSE
------------------------------------------------------------

What physical quantity does color represent?

Is the response unit shown?


CONTOURS
------------------------------------------------------------

Are contour intervals meaningful?

Are labels readable?

Are there too many levels?


COLOR
------------------------------------------------------------

Is the colormap appropriate?

Is a colorbar included?

Are limits honest and understandable?


OPTIMUM
------------------------------------------------------------

Is it called:

Best sampled point

or:

Global optimum?


Do the data justify the terminology?


CONSTRAINTS
------------------------------------------------------------

Are threshold definitions clear?

Is the feasible side of each boundary understood?


SAMPLING
------------------------------------------------------------

Regular grid?

Irregular DOE?

Interpolated?

Surrogate prediction?


MISSING DATA
------------------------------------------------------------

Are failed or unavailable points visible?


REPRODUCIBILITY
------------------------------------------------------------

Is the numerical sweep data preserved?


FINAL FIGURE
------------------------------------------------------------

Readable at publication size?

PNG / PDF / SVG exported?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
CONTOUR AND PARAMETER-SWEEP PLOTS


1. CREATE PARAMETER VECTORS

x = np.linspace(
    minimum,
    maximum,
    number_of_points
)


y = np.linspace(
    minimum,
    maximum,
    number_of_points
)


------------------------------------------------------------


2. CREATE GRID

X, Y = np.meshgrid(
    x,
    y
)


------------------------------------------------------------


3. RESPONSE MATRIX

Z = function(
    X,
    Y
)


Z should match the grid shape.


------------------------------------------------------------


4. BASIC CONTOUR

ax.contour(

    X,

    Y,

    Z

)


------------------------------------------------------------


5. FILLED CONTOUR

ax.contourf(

    X,

    Y,

    Z

)


------------------------------------------------------------


6. CONTOUR LEVELS

ax.contourf(

    X,

    Y,

    Z,

    levels=20

)


------------------------------------------------------------


7. EXPLICIT LEVELS

levels = np.arange(

    90,

    97,

    0.5

)


------------------------------------------------------------


8. LABEL CONTOURS

contours = ax.contour(
    X,
    Y,
    Z
)


ax.clabel(

    contours,

    inline=True

)


------------------------------------------------------------


9. COLORBAR

filled = ax.contourf(
    X,
    Y,
    Z
)


colorbar = fig.colorbar(

    filled,

    ax=ax

)


------------------------------------------------------------


10. ENGINEERING THRESHOLD

ax.contour(

    X,

    Y,

    Z,

    levels=[
        threshold
    ]

)


------------------------------------------------------------


11. FEASIBLE REGION

feasible = (

    condition_1

    & condition_2

    & condition_3

)


------------------------------------------------------------


12. BEST SAMPLED POINT

index = np.unravel_index(

    np.argmax(
        Z
    ),

    Z.shape

)


------------------------------------------------------------


13. MINIMUM RESPONSE

index = np.unravel_index(

    np.argmin(
        Z
    ),

    Z.shape

)


------------------------------------------------------------


14. CONSTRAINED SEARCH

masked_response = np.where(

    feasible,

    response,

    np.nan

)


------------------------------------------------------------


15. LONG-FORM DATA TO GRID

grid = dataframe.pivot(

    index="Parameter_Y",

    columns="Parameter_X",

    values="Response"

)


------------------------------------------------------------


16. REPEATED PARAMETER COMBINATIONS

Use:

pivot_table(
    aggfunc="mean"
)


when multiple observations exist at the same operating
point.


------------------------------------------------------------


17. MISSING DATA

Use:

NaN

or:

np.ma.masked_invalid()


Do not replace missing engineering results with zero
without justification.


------------------------------------------------------------


18. IRREGULAR DATA

Use:

ax.tricontour(
    x,
    y,
    z
)


or:

ax.tricontourf(
    x,
    y,
    z
)


for scattered parameter samples.


------------------------------------------------------------


19. DIFFERENCE MAP

difference = (

    design_b

    - design_a

)


For signed differences:

A diverging colormap and symmetric limits can be useful.


------------------------------------------------------------


20. EFFICIENCY DIFFERENCE

95%

vs

94%


=

1 percentage point


not automatically:

1% relative improvement.


------------------------------------------------------------


21. CONTOUR MAP

Useful for:

Efficiency

Temperature

Loss

EMI

Ripple

THD

Control Error

Prediction Error


------------------------------------------------------------


22. MULTIPLE CONSTRAINTS

Example:

Efficiency >= 95%

AND

Temperature <= 80 °C

AND

Power Loss <= 15 W


        ↓

Feasible Operating Region


------------------------------------------------------------


23. BEST POINT TERMINOLOGY

If only a discrete parameter sweep was evaluated:

Prefer:

Best sampled point


rather than automatically claiming:

Global optimum.


------------------------------------------------------------


24. COARSE SWEEP

Smooth contour appearance does not mean the underlying
parameter sweep was dense.


Report:

Ranges

Step sizes

Number of cases


------------------------------------------------------------


25. RAW DATA

Always preserve:

Numerical parameter-sweep results

alongside:

Contour figures.


------------------------------------------------------------


26. HEATMAP VS CONTOUR

HEATMAP

Best for:

Matrix / cell values


CONTOUR

Best for:

Equal-value boundaries


CONTOURF

Best for:

Continuous-looking response regions


------------------------------------------------------------


27. ENGINEERING APPLICATIONS

Contour plots are especially useful for:

Converter efficiency maps

Loss maps

Thermal maps

Control tuning

Parameter sensitivity

Design optimization

Operating envelopes

Constraint visualization

Robustness studies

DOE results

ML surrogate-response maps


------------------------------------------------------------


28. MOST IMPORTANT PRINCIPLE

A contour plot should not only look attractive.

It should answer:

Which parameters were varied?

What response was calculated?

Where is performance high or low?

Where are the engineering boundaries?

Which operating region is feasible?

Which sampled point is best?

How dense was the parameter sweep?

What physical conclusion follows?


------------------------------------------------------------


29. COMPLETE WORKFLOW

Parameter X
     ×
Parameter Y
     ↓
Generate Grid
     ↓
Evaluate Response
     ↓
Build Matrix
     ↓
Contour / Contourf
     ↓
Add Colorbar
     ↓
Add Equal-Value Lines
     ↓
Add Engineering Limits
     ↓
Identify Feasible Region
     ↓
Locate Best Sampled Point
     ↓
Check Tradeoffs
     ↓
Refine Sweep
     ↓
Validate
     ↓
Publication Figure


------------------------------------------------------------


NEXT:

26_inset_and_zoomed_plots.py


The next file will focus on one of the most useful
publication techniques for engineering papers:

Full waveform
        +
Zoomed region


including:

Inset axes

zoomed_inset_axes()

inset_axes()

indicate_inset_zoom()

Switching transient zoom

Small voltage-ripple zoom

FFT resonance zoom

Frequency-band inset

Selecting zoom ranges

Automatic zoom region

Annotations

Multiple inset locations

Inset vs subplot

Inset vs axis-limit manipulation

Keeping identical physical units

Publication-quality inset figures

and avoiding misleading magnification.
"""
