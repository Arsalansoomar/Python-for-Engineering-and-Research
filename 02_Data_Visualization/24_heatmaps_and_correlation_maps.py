"""
============================================================
Python for Engineering and Research
24 - Heatmaps and Correlation Maps
============================================================

Purpose:
    Demonstrate how heatmaps and correlation matrices can
    be used to visualize multidimensional engineering data,
    parameter sweeps, experimental matrices, and relationships
    between numerical variables.

Topics:
    1. What is a heatmap?
    2. Matrix representation
    3. imshow()
    4. Colorbars
    5. Axis labels
    6. Annotated heatmaps
    7. Sequential colormaps
    8. Diverging colormaps
    9. Fixed color limits
    10. Shared color scales
    11. pcolormesh()
    12. Physical X/Y coordinates
    13. Nonuniform grids
    14. Engineering parameter sweeps
    15. Optimum-point identification
    16. Missing values
    17. Correlation concept
    18. Pearson correlation
    19. Spearman correlation
    20. Kendall correlation
    21. Correlation matrix
    22. Annotated correlation heatmap
    23. Lower-triangle correlation map
    24. Selecting numerical DataFrame columns
    25. Correlation from CSV data
    26. Correlation does not imply causation
    27. Frequency × design heatmap
    28. Reusable heatmap functions
    29. Reusable correlation-map function
    30. Saving PNG / PDF / SVG
    31. Common mistakes
    32. Key takeaways

Sample Files:
    sample_data/voltage_current.csv
    sample_data/fft_example.csv

Important:
    Heatmap color is a numerical encoding.

    Color limits and colormap selection can strongly affect
    the visual interpretation of the data.

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

from matplotlib.ticker import FuncFormatter


# ============================================================
# 2. WHAT IS A HEATMAP?
# ============================================================

"""
A heatmap represents numerical values using color.

Example:

                      Switching Frequency
                  50    100    150    200 kHz

Load       25%     ●      ●      ●      ●

           50%     ●      ●      ●      ●

           75%     ●      ●      ●      ●

          100%     ●      ●      ●      ●


Each position contains one engineering result.

For example:

Efficiency [%]


Instead of displaying all values only as a numerical table,
the heatmap maps them to colors.


This can make patterns easier to identify.
"""


# ============================================================
# 3. ENGINEERING APPLICATIONS
# ============================================================

"""
Heatmaps are useful for:

- Parameter sweeps
- Converter efficiency maps
- Power-loss maps
- Temperature maps
- EMI magnitude maps
- Frequency-response comparisons
- Sensitivity studies
- Optimization studies
- Machine-learning datasets
- Correlation matrices
- Experimental design
- Reliability analysis
- Component tolerance studies
- Control parameter tuning
"""


# ============================================================
# 4. SIMPLE MATRIX
# ============================================================

efficiency_matrix = np.array(
    [
        [91.2, 92.0, 91.7, 90.9],
        [93.6, 94.5, 94.2, 93.4],
        [94.5, 95.4, 95.1, 94.3],
        [94.0, 95.0, 94.8, 93.9]
    ],
    dtype=float
)


print(
    "\n--- Efficiency Matrix ---"
)


print(
    efficiency_matrix
)


print(
    "\nMatrix Shape:"
)


print(
    efficiency_matrix.shape
)


# ============================================================
# 5. MATRIX INTERPRETATION
# ============================================================

"""
Rows:

Load conditions


Columns:

Switching frequencies


Example:

Rows:

25%
50%
75%
100%


Columns:

50 kHz
100 kHz
150 kHz
200 kHz


Each cell:

Efficiency [%]
"""


load_labels = [
    "25%",
    "50%",
    "75%",
    "100%"
]


frequency_labels = [
    "50 kHz",
    "100 kHz",
    "150 kHz",
    "200 kHz"
]


# ============================================================
# 6. BASIC HEATMAP USING imshow()
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


image = ax.imshow(
    efficiency_matrix
)


ax.set_title(
    "Converter Efficiency Map"
)


plt.tight_layout()

plt.show()


# ============================================================
# 7. ADD COLORBAR
# ============================================================

"""
A heatmap should normally include a colorbar when color
represents a quantitative physical variable.

The colorbar explains:

Color
   ↓
Numerical Value
"""


fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


image = ax.imshow(
    efficiency_matrix
)


colorbar = fig.colorbar(
    image,
    ax=ax
)


colorbar.set_label(
    "Efficiency [%]"
)


ax.set_title(
    "Converter Efficiency Map"
)


plt.tight_layout()

plt.show()


# ============================================================
# 8. ADD AXIS LABELS
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


image = ax.imshow(
    efficiency_matrix
)


ax.set_xticks(
    np.arange(
        len(
            frequency_labels
        )
    )
)


ax.set_xticklabels(
    frequency_labels
)


ax.set_yticks(
    np.arange(
        len(
            load_labels
        )
    )
)


ax.set_yticklabels(
    load_labels
)


ax.set_xlabel(
    "Switching Frequency"
)

ax.set_ylabel(
    "Load"
)


colorbar = fig.colorbar(
    image,
    ax=ax
)


colorbar.set_label(
    "Efficiency [%]"
)


ax.set_title(
    "Efficiency vs Load and Switching Frequency"
)


plt.tight_layout()

plt.show()


# ============================================================
# 9. ANNOTATED HEATMAP
# ============================================================

"""
Color shows the overall pattern.

Text annotations show the exact numerical values.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


image = ax.imshow(
    efficiency_matrix
)


ax.set_xticks(
    np.arange(
        len(
            frequency_labels
        )
    )
)


ax.set_xticklabels(
    frequency_labels
)


ax.set_yticks(
    np.arange(
        len(
            load_labels
        )
    )
)


ax.set_yticklabels(
    load_labels
)


for row in range(
    efficiency_matrix.shape[0]
):

    for column in range(
        efficiency_matrix.shape[1]
    ):

        ax.text(

            column,

            row,

            f"{efficiency_matrix[row, column]:.1f}",

            ha="center",

            va="center"

        )


colorbar = fig.colorbar(
    image,
    ax=ax
)


colorbar.set_label(
    "Efficiency [%]"
)


ax.set_xlabel(
    "Switching Frequency"
)

ax.set_ylabel(
    "Load"
)

ax.set_title(
    "Annotated Efficiency Heatmap"
)


plt.tight_layout()

plt.show()


# ============================================================
# 10. WHEN SHOULD A HEATMAP BE ANNOTATED?
# ============================================================

"""
Annotations are useful when:

The matrix is relatively small

and

exact values matter.


Example:

4 × 4

5 × 6


For:

100 × 100

or

1000 × 1000


text inside every cell would make the figure unreadable.


Use annotations selectively.
"""


# ============================================================
# 11. COLORMAP
# ============================================================

"""
The:

cmap=

parameter controls how numerical values are mapped to color.


The appropriate colormap depends on the meaning of the data.


Common categories:

SEQUENTIAL

Useful when values move from:

Low
to
High


Examples:

viridis

plasma

cividis


------------------------------------------------------------


DIVERGING

Useful when values vary around a meaningful center.

Example:

Negative
    ↓
Zero
    ↓
Positive


Examples:

coolwarm

RdBu
"""


# ============================================================
# 12. SEQUENTIAL COLORMAP EXAMPLE
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


image = ax.imshow(

    efficiency_matrix,

    cmap="viridis"

)


ax.set_xticks(
    np.arange(
        len(
            frequency_labels
        )
    )
)


ax.set_xticklabels(
    frequency_labels
)


ax.set_yticks(
    np.arange(
        len(
            load_labels
        )
    )
)


ax.set_yticklabels(
    load_labels
)


colorbar = fig.colorbar(
    image,
    ax=ax
)


colorbar.set_label(
    "Efficiency [%]"
)


ax.set_xlabel(
    "Switching Frequency"
)

ax.set_ylabel(
    "Load"
)


plt.tight_layout()

plt.show()


# ============================================================
# 13. COLOR LIMITS
# ============================================================

"""
Use:

vmin=

and:

vmax=


to control the numerical range represented by the
colormap.


Example:

Efficiency range:

90% to 96%
"""


fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


image = ax.imshow(

    efficiency_matrix,

    cmap="viridis",

    vmin=90,

    vmax=96

)


colorbar = fig.colorbar(
    image,
    ax=ax
)


colorbar.set_label(
    "Efficiency [%]"
)


ax.set_xticks(
    np.arange(
        len(
            frequency_labels
        )
    )
)


ax.set_xticklabels(
    frequency_labels
)


ax.set_yticks(
    np.arange(
        len(
            load_labels
        )
    )
)


ax.set_yticklabels(
    load_labels
)


ax.set_xlabel(
    "Switching Frequency"
)

ax.set_ylabel(
    "Load"
)


plt.tight_layout()

plt.show()


# ============================================================
# 14. WHY COLOR LIMITS MATTER
# ============================================================

"""
Suppose two heatmaps represent:

Design A

and

Design B.


Design A automatically uses:

90 to 96


while Design B automatically uses:

94 to 95.


The same visual color may represent different values.

This can make direct comparison misleading.


For comparable heatmaps:

Use the SAME:

vmin

vmax

and usually the same:

cmap
"""


# ============================================================
# 15. TWO CASES WITH SHARED COLOR LIMITS
# ============================================================

design_a_matrix = np.array(
    [
        [91.0, 91.8, 91.4, 90.8],
        [93.1, 94.0, 93.6, 92.9],
        [94.1, 94.8, 94.6, 93.9],
        [93.7, 94.4, 94.1, 93.5]
    ]
)


design_b_matrix = np.array(
    [
        [91.5, 92.4, 92.1, 91.4],
        [93.8, 94.8, 94.5, 93.9],
        [94.8, 95.8, 95.5, 94.9],
        [94.3, 95.2, 95.0, 94.3]
    ]
)


shared_minimum = min(

    design_a_matrix.min(),

    design_b_matrix.min()

)


shared_maximum = max(

    design_a_matrix.max(),

    design_b_matrix.max()

)


print(
    "\n--- Shared Color Limits ---"
)


print(
    shared_minimum,
    shared_maximum
)


# ============================================================
# 16. SHARED-COLOR-SCALE COMPARISON
# ============================================================

fig, axes = plt.subplots(

    1,

    2,

    figsize=(10, 4.5),

    sharex=True,

    sharey=True

)


image_a = axes[0].imshow(

    design_a_matrix,

    cmap="viridis",

    vmin=shared_minimum,

    vmax=shared_maximum

)


image_b = axes[1].imshow(

    design_b_matrix,

    cmap="viridis",

    vmin=shared_minimum,

    vmax=shared_maximum

)


axes[0].set_title(
    "Design A"
)


axes[1].set_title(
    "Design B"
)


for ax in axes:

    ax.set_xticks(
        np.arange(
            len(
                frequency_labels
            )
        )
    )


    ax.set_xticklabels(
        frequency_labels,
        rotation=20
    )


    ax.set_yticks(
        np.arange(
            len(
                load_labels
            )
        )
    )


    ax.set_yticklabels(
        load_labels
    )


    ax.set_xlabel(
        "Switching Frequency"
    )


axes[0].set_ylabel(
    "Load"
)


colorbar = fig.colorbar(

    image_b,

    ax=axes,

    shrink=0.85

)


colorbar.set_label(
    "Efficiency [%]"
)


plt.show()


# ============================================================
# 17. DIFFERENCE HEATMAP
# ============================================================

"""
Now calculate:

Design B
-
Design A


For efficiency:

Positive value
    ↓
Design B is higher


Negative value
    ↓
Design B is lower


Because the data are differences around zero, a diverging
colormap is useful.
"""


difference_matrix = (

    design_b_matrix

    - design_a_matrix

)


print(
    "\n--- Difference Matrix ---"
)


print(
    difference_matrix
)


# ============================================================
# 18. SYMMETRIC DIFFERENCE LIMIT
# ============================================================

maximum_absolute_difference = np.max(

    np.abs(
        difference_matrix
    )

)


# ============================================================
# 19. DIVERGING HEATMAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


image = ax.imshow(

    difference_matrix,

    cmap="coolwarm",

    vmin=-maximum_absolute_difference,

    vmax=maximum_absolute_difference

)


ax.set_xticks(
    np.arange(
        len(
            frequency_labels
        )
    )
)


ax.set_xticklabels(
    frequency_labels
)


ax.set_yticks(
    np.arange(
        len(
            load_labels
        )
    )
)


ax.set_yticklabels(
    load_labels
)


for row in range(
    difference_matrix.shape[0]
):

    for column in range(
        difference_matrix.shape[1]
    ):

        ax.text(

            column,

            row,

            f"{difference_matrix[row, column]:+.2f}",

            ha="center",

            va="center"

        )


colorbar = fig.colorbar(
    image,
    ax=ax
)


colorbar.set_label(
    "Efficiency Difference [percentage points]"
)


ax.set_xlabel(
    "Switching Frequency"
)

ax.set_ylabel(
    "Load"
)

ax.set_title(
    "Design B - Design A"
)


plt.tight_layout()

plt.show()


# ============================================================
# 20. PERCENTAGE POINTS VS PERCENT
# ============================================================

"""
Suppose:

Design A efficiency = 94%

Design B efficiency = 95%


Absolute efficiency difference:

95 - 94

=

1 percentage point


Relative percentage improvement:

(95 - 94) / 94 × 100

≈

1.06%


These are different quantities.

Do not label an efficiency difference in percentage points
as a relative percentage improvement.
"""


# ============================================================
# 21. imshow() VS pcolormesh()
# ============================================================

"""
imshow()

is convenient when the data naturally form a regular
matrix.


pcolormesh()

is useful when actual physical X and Y coordinates should
be represented directly.


Examples:

Switching Frequency [kHz]

Load [%]

Temperature [°C]

Gate Resistance [ohm]
"""


# ============================================================
# 22. PHYSICAL COORDINATES
# ============================================================

switching_frequency_khz = np.array(
    [
        50,
        100,
        150,
        200
    ],
    dtype=float
)


load_percent = np.array(
    [
        25,
        50,
        75,
        100
    ],
    dtype=float
)


# ============================================================
# 23. pcolormesh() EXAMPLE
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


mesh = ax.pcolormesh(

    switching_frequency_khz,

    load_percent,

    efficiency_matrix,

    shading="auto",

    cmap="viridis"

)


colorbar = fig.colorbar(
    mesh,
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
# 24. NONUNIFORM GRID
# ============================================================

"""
Physical parameter sweeps are not always equally spaced.

Example switching-frequency samples:

50 kHz

75 kHz

100 kHz

150 kHz

250 kHz


pcolormesh() is convenient for coordinate-based grids.
"""


nonuniform_frequency_khz = np.array(
    [
        50,
        75,
        100,
        150,
        250
    ],
    dtype=float
)


nonuniform_load_percent = np.array(
    [
        20,
        40,
        70,
        100
    ],
    dtype=float
)


nonuniform_efficiency = np.array(
    [
        [90.5, 91.2, 91.8, 91.3, 90.4],
        [92.7, 93.4, 94.0, 93.7, 92.8],
        [94.0, 94.8, 95.5, 95.2, 94.3],
        [93.5, 94.3, 95.0, 94.7, 93.8]
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


mesh = ax.pcolormesh(

    nonuniform_frequency_khz,

    nonuniform_load_percent,

    nonuniform_efficiency,

    shading="auto",

    cmap="viridis"

)


colorbar = fig.colorbar(
    mesh,
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
# 25. PARAMETER-SWEEP EXAMPLE
# ============================================================

"""
Now create a larger synthetic engineering parameter sweep.

Parameters:

X:
Switching Frequency [kHz]


Y:
Load [%]


Response:

Efficiency [%]
"""


frequency_sweep_khz = np.linspace(
    50,
    250,
    21
)


load_sweep_percent = np.linspace(
    10,
    100,
    19
)


frequency_grid, load_grid = np.meshgrid(

    frequency_sweep_khz,

    load_sweep_percent

)


# ============================================================
# 26. SYNTHETIC ENGINEERING RESPONSE
# ============================================================

"""
The following equation creates a synthetic teaching
dataset.

It is not intended to model one specific physical
converter.
"""


efficiency_sweep = (

    95.8

    - 0.000055
    * (
        frequency_grid
        - 130
    ) ** 2

    - 0.00042
    * (
        load_grid
        - 75
    ) ** 2

    - 0.002
    * np.abs(
        frequency_grid
        - 130
    )

)


# ============================================================
# 27. PARAMETER-SWEEP HEATMAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


mesh = ax.pcolormesh(

    frequency_grid,

    load_grid,

    efficiency_sweep,

    shading="auto",

    cmap="viridis"

)


colorbar = fig.colorbar(
    mesh,
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
    "Engineering Parameter Sweep"
)


plt.tight_layout()

plt.show()


# ============================================================
# 28. FIND OPTIMUM POINT
# ============================================================

maximum_index = np.unravel_index(

    np.argmax(
        efficiency_sweep
    ),

    efficiency_sweep.shape

)


optimum_load = load_grid[
    maximum_index
]


optimum_frequency = frequency_grid[
    maximum_index
]


optimum_efficiency = efficiency_sweep[
    maximum_index
]


print(
    "\n--- Optimum Point ---"
)


print(
    f"Frequency = "
    f"{optimum_frequency:.1f} kHz"
)


print(
    f"Load = "
    f"{optimum_load:.1f}%"
)


print(
    f"Efficiency = "
    f"{optimum_efficiency:.3f}%"
)


# ============================================================
# 29. MARK OPTIMUM ON HEATMAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


mesh = ax.pcolormesh(

    frequency_grid,

    load_grid,

    efficiency_sweep,

    shading="auto",

    cmap="viridis"

)


ax.scatter(

    optimum_frequency,

    optimum_load,

    marker="*",

    s=130,

    label="Maximum"

)


ax.annotate(

    (
        f"{optimum_efficiency:.2f}%\n"
        f"{optimum_frequency:.0f} kHz, "
        f"{optimum_load:.0f}% load"
    ),

    xy=(
        optimum_frequency,
        optimum_load
    ),

    xytext=(
        25,
        -35
    ),

    textcoords="offset points",

    arrowprops={
        "arrowstyle":
            "->"
    }

)


colorbar = fig.colorbar(
    mesh,
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
# 30. IMPORTANT OPTIMUM WARNING
# ============================================================

"""
The maximum point in a sampled parameter sweep means:

Best value among the evaluated samples.


It does NOT automatically prove:

Global mathematical optimum


unless the search space and optimization methodology
justify that conclusion.


A finer sweep could reveal another point with better
performance.
"""


# ============================================================
# 31. MISSING DATA IN HEATMAP
# ============================================================

"""
Engineering sweeps may contain missing simulations or
failed measurements.

Example:

NaN
"""


matrix_with_missing = efficiency_matrix.copy()


matrix_with_missing[
    1,
    2
] = np.nan


matrix_with_missing[
    3,
    0
] = np.nan


print(
    "\n--- Matrix with Missing Values ---"
)


print(
    matrix_with_missing
)


# ============================================================
# 32. MASK MISSING VALUES
# ============================================================

masked_matrix = np.ma.masked_invalid(
    matrix_with_missing
)


fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


image = ax.imshow(

    masked_matrix,

    cmap="viridis"

)


ax.set_xticks(
    np.arange(
        len(
            frequency_labels
        )
    )
)


ax.set_xticklabels(
    frequency_labels
)


ax.set_yticks(
    np.arange(
        len(
            load_labels
        )
    )
)


ax.set_yticklabels(
    load_labels
)


colorbar = fig.colorbar(
    image,
    ax=ax
)


colorbar.set_label(
    "Efficiency [%]"
)


ax.set_xlabel(
    "Switching Frequency"
)

ax.set_ylabel(
    "Load"
)

ax.set_title(
    "Heatmap with Missing Measurements"
)


plt.tight_layout()

plt.show()


# ============================================================
# 33. MISSING-DATA WARNING
# ============================================================

"""
Do not silently replace missing engineering results with:

0


unless zero is physically the correct value.


NaN may mean:

Simulation failed

Measurement unavailable

Sensor disconnected

Operating condition invalid

Data intentionally not collected


The distinction matters.
"""


# ============================================================
# 34. WHAT IS CORRELATION?
# ============================================================

"""
Correlation describes statistical association between
variables.

For Pearson correlation:

r ≈ +1
    Strong positive linear relationship


r ≈ 0
    Weak or no linear relationship


r ≈ -1
    Strong negative linear relationship


Examples:

Temperature ↑
Power Loss ↑

may produce positive correlation.


Efficiency ↑
Power Loss ↓

may produce negative correlation.


But correlation alone does NOT establish causation.
"""


# ============================================================
# 35. SYNTHETIC ENGINEERING DATAFRAME
# ============================================================

number_of_samples = 300


rng = np.random.default_rng(
    42
)


load_data = rng.uniform(
    20,
    100,
    number_of_samples
)


switching_frequency_data = rng.uniform(
    50,
    250,
    number_of_samples
)


temperature_data = (

    30

    + 0.25
    * load_data

    + 0.025
    * switching_frequency_data

    + rng.normal(
        0,
        2.0,
        number_of_samples
    )

)


power_loss_data = (

    4

    + 0.08
    * load_data

    + 0.025
    * switching_frequency_data

    + rng.normal(
        0,
        1.0,
        number_of_samples
    )

)


efficiency_data = (

    97

    - 0.09
    * power_loss_data

    + rng.normal(
        0,
        0.15,
        number_of_samples
    )

)


output_power_data = (

    5.0
    * load_data

    + rng.normal(
        0,
        8,
        number_of_samples
    )

)


engineering_data = pd.DataFrame(
    {
        "Load_percent":
            load_data,

        "Switching_Frequency_kHz":
            switching_frequency_data,

        "Temperature_C":
            temperature_data,

        "Power_Loss_W":
            power_loss_data,

        "Efficiency_percent":
            efficiency_data,

        "Output_Power_W":
            output_power_data
    }
)


print(
    "\n--- Engineering DataFrame ---"
)


print(
    engineering_data.head()
)


# ============================================================
# 36. CORRELATION MATRIX
# ============================================================

correlation_matrix = engineering_data.corr(

    method="pearson",

    numeric_only=True

)


print(
    "\n--- Pearson Correlation Matrix ---"
)


print(
    correlation_matrix
)


# ============================================================
# 37. CORRELATION RANGE
# ============================================================

"""
Correlation coefficients lie between:

-1

and

+1


Therefore a correlation heatmap should normally use a
fixed symmetric scale:

vmin=-1

vmax=1


This makes color interpretation consistent.
"""


# ============================================================
# 38. BASIC CORRELATION HEATMAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 6)
)


image = ax.imshow(

    correlation_matrix,

    cmap="coolwarm",

    vmin=-1,

    vmax=1

)


ax.set_xticks(
    np.arange(
        len(
            correlation_matrix.columns
        )
    )
)


ax.set_xticklabels(

    correlation_matrix.columns,

    rotation=45,

    ha="right"

)


ax.set_yticks(
    np.arange(
        len(
            correlation_matrix.index
        )
    )
)


ax.set_yticklabels(
    correlation_matrix.index
)


colorbar = fig.colorbar(
    image,
    ax=ax
)


colorbar.set_label(
    "Pearson Correlation Coefficient"
)


ax.set_title(
    "Engineering Correlation Matrix"
)


plt.tight_layout()

plt.show()


# ============================================================
# 39. ANNOTATED CORRELATION MATRIX
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 6)
)


image = ax.imshow(

    correlation_matrix,

    cmap="coolwarm",

    vmin=-1,

    vmax=1

)


variable_names = (
    correlation_matrix.columns
)


ax.set_xticks(
    np.arange(
        len(
            variable_names
        )
    )
)


ax.set_xticklabels(

    variable_names,

    rotation=45,

    ha="right"

)


ax.set_yticks(
    np.arange(
        len(
            variable_names
        )
    )
)


ax.set_yticklabels(
    variable_names
)


for row in range(
    correlation_matrix.shape[0]
):

    for column in range(
        correlation_matrix.shape[1]
    ):

        value = correlation_matrix.iloc[
            row,
            column
        ]


        ax.text(

            column,

            row,

            f"{value:.2f}",

            ha="center",

            va="center"

        )


colorbar = fig.colorbar(
    image,
    ax=ax
)


colorbar.set_label(
    "Pearson r"
)


ax.set_title(
    "Annotated Correlation Matrix"
)


plt.tight_layout()

plt.show()


# ============================================================
# 40. WHY DIAGONAL VALUES ARE 1
# ============================================================

"""
Every numerical variable is perfectly correlated with
itself.

Therefore:

Correlation(
    X,
    X
)

=

1


This produces the diagonal line of:

1.00

in the correlation matrix.
"""


# ============================================================
# 41. PEARSON CORRELATION
# ============================================================

"""
Pearson correlation primarily describes:

LINEAR association.


Example:

Y ≈ aX + b


can produce a large absolute Pearson correlation.
"""


pearson_matrix = engineering_data.corr(

    method="pearson",

    numeric_only=True

)


# ============================================================
# 42. SPEARMAN CORRELATION
# ============================================================

"""
Spearman correlation is based on ranked values.

It can capture monotonic relationships that are not
necessarily linear.
"""


spearman_matrix = engineering_data.corr(

    method="spearman",

    numeric_only=True

)


print(
    "\n--- Spearman Correlation ---"
)


print(
    spearman_matrix
)


# ============================================================
# 43. KENDALL CORRELATION
# ============================================================

"""
Kendall correlation is another rank-based association
measure.
"""


kendall_matrix = engineering_data.corr(

    method="kendall",

    numeric_only=True

)


print(
    "\n--- Kendall Correlation ---"
)


print(
    kendall_matrix
)


# ============================================================
# 44. PEARSON VS SPEARMAN
# ============================================================

"""
PEARSON

Primarily measures:

Linear association


------------------------------------------------------------


SPEARMAN

Measures:

Monotonic rank association


------------------------------------------------------------


KENDALL

Also evaluates:

Rank association


The appropriate method depends on:

Data behavior

Research question

Statistical assumptions
"""


# ============================================================
# 45. SIMPLE NONLINEAR EXAMPLE
# ============================================================

x_nonlinear = np.linspace(
    0,
    5,
    200
)


y_nonlinear = np.exp(
    0.8
    * x_nonlinear
)


nonlinear_data = pd.DataFrame(
    {
        "X":
            x_nonlinear,

        "Y":
            y_nonlinear
    }
)


print(
    "\n--- Nonlinear Example ---"
)


print(
    "Pearson:"
)


print(
    nonlinear_data.corr(
        method="pearson"
    )
)


print(
    "\nSpearman:"
)


print(
    nonlinear_data.corr(
        method="spearman"
    )
)


# ============================================================
# 46. CORRELATION IS NOT CAUSATION
# ============================================================

"""
Suppose:

Temperature

and

Power Loss


are strongly correlated.


This does NOT by itself prove:

Temperature causes power loss

or

Power loss causes temperature.


Possible explanations include:

Direct causal relationship

Reverse causal relationship

Common dependence on load

Common dependence on switching frequency

Measurement artifact

Confounding variable


Correlation identifies association.

Physical interpretation requires engineering reasoning.
"""


# ============================================================
# 47. LOWER-TRIANGLE CORRELATION MAP
# ============================================================

"""
The correlation matrix is symmetric.

Therefore:

Upper Triangle

contains the same pairwise information as:

Lower Triangle


A triangular map can reduce visual repetition.
"""


correlation_values = (
    correlation_matrix.to_numpy()
)


upper_triangle_mask = np.triu(

    np.ones_like(
        correlation_values,
        dtype=bool
    ),

    k=1

)


lower_triangle_matrix = np.ma.array(

    correlation_values,

    mask=upper_triangle_mask

)


fig, ax = plt.subplots(
    figsize=(8, 6)
)


image = ax.imshow(

    lower_triangle_matrix,

    cmap="coolwarm",

    vmin=-1,

    vmax=1

)


variable_names = (
    correlation_matrix.columns.tolist()
)


ax.set_xticks(
    np.arange(
        len(
            variable_names
        )
    )
)


ax.set_xticklabels(

    variable_names,

    rotation=45,

    ha="right"

)


ax.set_yticks(
    np.arange(
        len(
            variable_names
        )
    )
)


ax.set_yticklabels(
    variable_names
)


for row in range(
    len(
        variable_names
    )
):

    for column in range(
        len(
            variable_names
        )
    ):

        if not upper_triangle_mask[
            row,
            column
        ]:

            ax.text(

                column,

                row,

                (
                    f"{correlation_values[row, column]:.2f}"
                ),

                ha="center",

                va="center"

            )


colorbar = fig.colorbar(
    image,
    ax=ax
)


colorbar.set_label(
    "Pearson r"
)


ax.set_title(
    "Lower-Triangle Correlation Matrix"
)


plt.tight_layout()

plt.show()


# ============================================================
# 48. SELECT NUMERICAL COLUMNS ONLY
# ============================================================

"""
Real research DataFrames may also contain:

Case names

Dates

Comments

Test IDs

Operating mode


Correlation should normally be calculated using relevant
numerical columns.
"""


mixed_data = engineering_data.copy()


mixed_data[
    "Case_Name"
] = "Experiment"


mixed_data[
    "Test_ID"
] = [

    f"Test_{index + 1}"

    for index in range(
        len(
            mixed_data
        )
    )

]


numerical_data = mixed_data.select_dtypes(
    include="number"
)


print(
    "\n--- Numerical Columns ---"
)


print(
    numerical_data.columns.tolist()
)


# ============================================================
# 49. CORRELATION OF SELECTED VARIABLES
# ============================================================

selected_variables = [

    "Load_percent",

    "Temperature_C",

    "Power_Loss_W",

    "Efficiency_percent"

]


selected_correlation = engineering_data[
    selected_variables
].corr(
    method="pearson"
)


print(
    "\n--- Selected Variable Correlation ---"
)


print(
    selected_correlation
)


# ============================================================
# 50. MISSING VALUES AND CORRELATION
# ============================================================

"""
Real datasets often contain missing values.

Pandas correlation methods calculate pairwise relationships
using available non-missing observations.

Researchers should still inspect:

How much data are missing?

Why are values missing?

How many paired observations remain?


Do not treat missingness as irrelevant.
"""


correlation_missing_data = engineering_data.copy()


correlation_missing_data.loc[
    0:20,
    "Temperature_C"
] = np.nan


correlation_missing_data.loc[
    40:60,
    "Power_Loss_W"
] = np.nan


missing_correlation = (
    correlation_missing_data.corr(

        method="pearson",

        numeric_only=True

    )
)


print(
    "\n--- Correlation with Missing Values ---"
)


print(
    missing_correlation
)


# ============================================================
# 51. COUNT VALID OBSERVATIONS
# ============================================================

print(
    "\n--- Valid Numerical Observations ---"
)


print(
    correlation_missing_data.count()
)


# ============================================================
# 52. CORRELATION FROM CSV DATA
# ============================================================

csv_file = (
    Path(
        __file__
    )
    .resolve()
    .parent
    / "sample_data"
    / "voltage_current.csv"
)


if not csv_file.exists():

    raise FileNotFoundError(
        f"\nCSV sample file not found:\n"
        f"{csv_file}"
    )


csv_data = pd.read_csv(
    csv_file
)


print(
    "\n--- CSV Dataset Columns ---"
)


print(
    csv_data.columns.tolist()
)


# ============================================================
# 53. CSV NUMERICAL CORRELATION
# ============================================================

csv_numeric = csv_data.select_dtypes(
    include="number"
)


csv_correlation = csv_numeric.corr(
    method="pearson"
)


print(
    "\n--- CSV Correlation Matrix ---"
)


print(
    csv_correlation
)


# ============================================================
# 54. CSV CORRELATION HEATMAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 5.5)
)


image = ax.imshow(

    csv_correlation,

    cmap="coolwarm",

    vmin=-1,

    vmax=1

)


csv_labels = csv_correlation.columns.tolist()


ax.set_xticks(
    np.arange(
        len(
            csv_labels
        )
    )
)


ax.set_xticklabels(

    csv_labels,

    rotation=45,

    ha="right"

)


ax.set_yticks(
    np.arange(
        len(
            csv_labels
        )
    )
)


ax.set_yticklabels(
    csv_labels
)


for row in range(
    csv_correlation.shape[0]
):

    for column in range(
        csv_correlation.shape[1]
    ):

        ax.text(

            column,

            row,

            f"{csv_correlation.iloc[row, column]:.2f}",

            ha="center",

            va="center"

        )


colorbar = fig.colorbar(
    image,
    ax=ax
)


colorbar.set_label(
    "Pearson r"
)


ax.set_title(
    "CSV Variable Correlation"
)


plt.tight_layout()

plt.show()


# ============================================================
# 55. CORRELATION WITH DERIVED VARIABLES
# ============================================================

"""
The sample dataset contains:

Voltage

Current

Power


If:

Power = Voltage × Current


then strong correlations may appear because one variable
is mathematically derived from the others.


This is an important research consideration.

Correlation may result from:

Physical relationships

or

Mathematical construction.
"""


# ============================================================
# 56. MULTICOLLINEARITY CONCEPT
# ============================================================

"""
When several input variables are strongly correlated,
machine-learning or regression analysis may require
additional consideration.

Examples:

Voltage

Current

Power = Voltage × Current


or:

Temperature

Load

Power Loss


Correlation maps are useful for identifying such
relationships before modeling.

However:

Correlation alone is not a complete multicollinearity
diagnostic.
"""


# ============================================================
# 57. LOAD FFT DATA
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


fft_file = (
    script_folder
    / "sample_data"
    / "fft_example.csv"
)


if not fft_file.exists():

    raise FileNotFoundError(
        f"\nFFT sample file not found:\n"
        f"{fft_file}"
    )


fft_data = pd.read_csv(
    fft_file
)


# ============================================================
# 58. FFT CASE DEFINITIONS
# ============================================================

fft_cases = {

    "Unshielded":
        "Unshielded_dBuV",

    "Case A":
        "Case_A_dBuV",

    "Case B":
        "Case_B_dBuV",

    "Case C":
        "Case_C_dBuV"

}


required_fft_columns = [

    "Frequency_Hz"

] + list(
    fft_cases.values()
)


missing_fft_columns = [

    column

    for column in required_fft_columns

    if column not in fft_data.columns

]


if missing_fft_columns:

    raise KeyError(
        f"Missing FFT columns: "
        f"{missing_fft_columns}"
    )


# ============================================================
# 59. CLEAN FFT DATA
# ============================================================

for column in required_fft_columns:

    fft_data[
        column
    ] = pd.to_numeric(

        fft_data[
            column
        ],

        errors="coerce"

    )


fft_data = fft_data.dropna(
    subset=required_fft_columns
)


fft_data = fft_data[
    fft_data[
        "Frequency_Hz"
    ] > 0
]


fft_data = fft_data.sort_values(
    "Frequency_Hz"
)


# ============================================================
# 60. FREQUENCY × CASE HEATMAP
# ============================================================

"""
Rows:

Engineering cases


Columns:

Frequency samples


Cell value:

Magnitude [dBµV]


This provides another way to compare many spectra.
"""


fft_matrix = np.vstack(
    [
        fft_data[
            column_name
        ].to_numpy()

        for column_name in fft_cases.values()
    ]
)


print(
    "\n--- FFT Heatmap Shape ---"
)


print(
    fft_matrix.shape
)


# ============================================================
# 61. FREQUENCY FORMATTER
# ============================================================

def format_frequency(
    frequency
):
    """
    Convert frequency to compact engineering notation.
    """

    if frequency >= 1e9:

        return (
            f"{frequency / 1e9:g} GHz"
        )


    if frequency >= 1e6:

        return (
            f"{frequency / 1e6:g} MHz"
        )


    if frequency >= 1e3:

        return (
            f"{frequency / 1e3:g} kHz"
        )


    return (
        f"{frequency:g} Hz"
    )


# ============================================================
# 62. SELECT FREQUENCY TICK LOCATIONS
# ============================================================

"""
The FFT data may contain many columns in the heatmap.

Do not label every frequency sample.

Select a manageable number of representative positions.
"""


number_of_frequency_ticks = min(
    7,
    len(
        fft_data
    )
)


frequency_tick_positions = np.linspace(

    0,

    len(
        fft_data
    )
    - 1,

    number_of_frequency_ticks,

    dtype=int

)


frequency_tick_labels = [

    format_frequency(

        fft_data[
            "Frequency_Hz"
        ].iloc[
            index
        ]

    )

    for index in frequency_tick_positions

]


# ============================================================
# 63. FFT HEATMAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(10, 4.5)
)


image = ax.imshow(

    fft_matrix,

    aspect="auto",

    cmap="viridis"

)


ax.set_yticks(
    np.arange(
        len(
            fft_cases
        )
    )
)


ax.set_yticklabels(
    list(
        fft_cases.keys()
    )
)


ax.set_xticks(
    frequency_tick_positions
)


ax.set_xticklabels(

    frequency_tick_labels,

    rotation=25,

    ha="right"

)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Configuration"
)

ax.set_title(
    "Frequency × Configuration Heatmap"
)


colorbar = fig.colorbar(
    image,
    ax=ax
)


colorbar.set_label(
    "Magnitude [dBµV]"
)


plt.tight_layout()

plt.show()


# ============================================================
# 64. IMPORTANT FFT HEATMAP NOTE
# ============================================================

"""
The heatmap columns represent sampled frequencies.

If the original frequencies are logarithmically spaced,
imshow() still displays matrix columns with equal visual
width.

Therefore:

imshow()

is useful for a case × sample-index overview.


For exact physical frequency spacing on the X-axis,
coordinate-based plotting such as:

pcolormesh()

may be preferable.
"""


# ============================================================
# 65. REUSABLE ANNOTATED HEATMAP FUNCTION
# ============================================================

def plot_annotated_heatmap(
    matrix,
    row_labels,
    column_labels,
    colorbar_label,
    title=None,
    cmap="viridis",
    vmin=None,
    vmax=None,
    annotation_format=".2f"
):
    """
    Create an annotated heatmap.

    Parameters
    ----------
    matrix : 2D array-like
        Numerical heatmap values.

    row_labels : list
        Labels for matrix rows.

    column_labels : list
        Labels for matrix columns.

    colorbar_label : str
        Label describing the color variable.

    title : str, optional
        Figure title.

    cmap : str
        Matplotlib colormap.

    vmin, vmax : float, optional
        Color-scale limits.

    annotation_format : str
        Numerical text format.

    Returns
    -------
    fig, ax
        Matplotlib objects.
    """

    matrix = np.asarray(
        matrix,
        dtype=float
    )


    if matrix.ndim != 2:

        raise ValueError(
            "Heatmap matrix must be two-dimensional."
        )


    if matrix.shape[0] != len(
        row_labels
    ):

        raise ValueError(
            "Number of row labels must match "
            "matrix row count."
        )


    if matrix.shape[1] != len(
        column_labels
    ):

        raise ValueError(
            "Number of column labels must match "
            "matrix column count."
        )


    masked_matrix = np.ma.masked_invalid(
        matrix
    )


    fig, ax = plt.subplots(
        figsize=(8, 5)
    )


    image = ax.imshow(

        masked_matrix,

        cmap=cmap,

        vmin=vmin,

        vmax=vmax

    )


    ax.set_xticks(
        np.arange(
            len(
                column_labels
            )
        )
    )


    ax.set_xticklabels(

        column_labels,

        rotation=30,

        ha="right"

    )


    ax.set_yticks(
        np.arange(
            len(
                row_labels
            )
        )
    )


    ax.set_yticklabels(
        row_labels
    )


    for row in range(
        matrix.shape[0]
    ):

        for column in range(
            matrix.shape[1]
        ):

            value = matrix[
                row,
                column
            ]


            if np.isfinite(
                value
            ):

                ax.text(

                    column,

                    row,

                    format(
                        value,
                        annotation_format
                    ),

                    ha="center",

                    va="center"

                )


    colorbar = fig.colorbar(
        image,
        ax=ax
    )


    colorbar.set_label(
        colorbar_label
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
# 66. USE ANNOTATED HEATMAP FUNCTION
# ============================================================

fig, ax = plot_annotated_heatmap(

    matrix=efficiency_matrix,

    row_labels=load_labels,

    column_labels=frequency_labels,

    colorbar_label="Efficiency [%]",

    title="Reusable Engineering Heatmap",

    cmap="viridis",

    vmin=90,

    vmax=96,

    annotation_format=".1f"

)


ax.set_xlabel(
    "Switching Frequency"
)


ax.set_ylabel(
    "Load"
)


plt.show()


# ============================================================
# 67. REUSABLE CORRELATION HEATMAP FUNCTION
# ============================================================

def plot_correlation_heatmap(
    dataframe,
    columns=None,
    method="pearson",
    lower_triangle=False,
    annotate=True,
    title=None
):
    """
    Create a correlation heatmap from numerical data.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Source dataset.

    columns : list, optional
        Numerical columns to include.

    method : str
        "pearson", "spearman", or "kendall".

    lower_triangle : bool
        Hide repeated upper-triangle values.

    annotate : bool
        Display correlation coefficients.

    title : str, optional
        Figure title.

    Returns
    -------
    correlation : pandas.DataFrame
        Calculated correlation matrix.

    fig, ax
        Matplotlib objects.
    """

    supported_methods = {
        "pearson",
        "spearman",
        "kendall"
    }


    if method not in supported_methods:

        raise ValueError(
            "method must be "
            "'pearson', 'spearman', or 'kendall'."
        )


    if columns is None:

        numerical_data = (
            dataframe
            .select_dtypes(
                include="number"
            )
        )

    else:

        missing_columns = [

            column

            for column in columns

            if column not in dataframe.columns

        ]


        if missing_columns:

            raise KeyError(
                f"Missing columns: "
                f"{missing_columns}"
            )


        numerical_data = dataframe[
            columns
        ].select_dtypes(
            include="number"
        )


    if numerical_data.shape[1] < 2:

        raise ValueError(
            "At least two numerical variables "
            "are required."
        )


    correlation = numerical_data.corr(
        method=method
    )


    values = correlation.to_numpy()


    if lower_triangle:

        mask = np.triu(

            np.ones_like(
                values,
                dtype=bool
            ),

            k=1

        )


        display_values = np.ma.array(

            values,

            mask=mask

        )

    else:

        mask = np.zeros_like(
            values,
            dtype=bool
        )


        display_values = values


    fig, ax = plt.subplots(
        figsize=(8, 6)
    )


    image = ax.imshow(

        display_values,

        cmap="coolwarm",

        vmin=-1,

        vmax=1

    )


    labels = correlation.columns.tolist()


    ax.set_xticks(
        np.arange(
            len(
                labels
            )
        )
    )


    ax.set_xticklabels(

        labels,

        rotation=45,

        ha="right"

    )


    ax.set_yticks(
        np.arange(
            len(
                labels
            )
        )
    )


    ax.set_yticklabels(
        labels
    )


    if annotate:

        for row in range(
            len(
                labels
            )
        ):

            for column in range(
                len(
                    labels
                )
            ):

                if not mask[
                    row,
                    column
                ]:

                    value = values[
                        row,
                        column
                    ]


                    if np.isfinite(
                        value
                    ):

                        ax.text(

                            column,

                            row,

                            f"{value:.2f}",

                            ha="center",

                            va="center"

                        )


    colorbar = fig.colorbar(
        image,
        ax=ax
    )


    colorbar.set_label(
        f"{method.capitalize()} Correlation"
    )


    if title is not None:

        ax.set_title(
            title
        )


    plt.tight_layout()


    return (
        correlation,
        fig,
        ax
    )


# ============================================================
# 68. USE CORRELATION FUNCTION
# ============================================================

correlation_result, fig, ax = (
    plot_correlation_heatmap(

        dataframe=engineering_data,

        method="pearson",

        lower_triangle=True,

        annotate=True,

        title=(
            "Engineering Variable Correlation"
        )

    )
)


plt.show()


# ============================================================
# 69. SAVE OUTPUT FOLDERS
# ============================================================

output_figure_folder = (
    script_folder
    / "output_figures"
    / "heatmaps"
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


# ============================================================
# 70. FINAL PARAMETER-SWEEP FIGURE
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


mesh = ax.pcolormesh(

    frequency_grid,

    load_grid,

    efficiency_sweep,

    shading="auto",

    cmap="viridis"

)


ax.scatter(

    optimum_frequency,

    optimum_load,

    marker="*",

    s=120,

    label="Best sampled point"

)


ax.annotate(

    (
        f"{optimum_efficiency:.2f}%"
    ),

    xy=(
        optimum_frequency,
        optimum_load
    ),

    xytext=(
        20,
        -30
    ),

    textcoords="offset points",

    arrowprops={
        "arrowstyle":
            "->"
    }

)


colorbar = fig.colorbar(
    mesh,
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
    "Engineering Parameter-Sweep Heatmap"
)


ax.legend()


plt.tight_layout()


# ============================================================
# 71. SAVE HEATMAP PNG
# ============================================================

heatmap_png = (
    output_figure_folder
    / "engineering_parameter_heatmap.png"
)


fig.savefig(
    heatmap_png,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 72. SAVE HEATMAP PDF
# ============================================================

heatmap_pdf = (
    output_figure_folder
    / "engineering_parameter_heatmap.pdf"
)


fig.savefig(
    heatmap_pdf,
    bbox_inches="tight"
)


# ============================================================
# 73. SAVE HEATMAP SVG
# ============================================================

heatmap_svg = (
    output_figure_folder
    / "engineering_parameter_heatmap.svg"
)


fig.savefig(
    heatmap_svg,
    bbox_inches="tight"
)


print(
    "\n--- Heatmap Figures Saved ---"
)


print(
    heatmap_png
)


print(
    heatmap_pdf
)


print(
    heatmap_svg
)


plt.show()


# ============================================================
# 74. FINAL CORRELATION FIGURE
# ============================================================

correlation_result, fig, ax = (
    plot_correlation_heatmap(

        dataframe=engineering_data,

        columns=[
            "Load_percent",
            "Switching_Frequency_kHz",
            "Temperature_C",
            "Power_Loss_W",
            "Efficiency_percent",
            "Output_Power_W"
        ],

        method="pearson",

        lower_triangle=True,

        annotate=True,

        title=(
            "Engineering Correlation Map"
        )

    )
)


# ============================================================
# 75. SAVE CORRELATION PNG
# ============================================================

correlation_png = (
    output_figure_folder
    / "engineering_correlation_map.png"
)


fig.savefig(
    correlation_png,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 76. SAVE CORRELATION PDF
# ============================================================

correlation_pdf = (
    output_figure_folder
    / "engineering_correlation_map.pdf"
)


fig.savefig(
    correlation_pdf,
    bbox_inches="tight"
)


# ============================================================
# 77. SAVE CORRELATION SVG
# ============================================================

correlation_svg = (
    output_figure_folder
    / "engineering_correlation_map.svg"
)


fig.savefig(
    correlation_svg,
    bbox_inches="tight"
)


print(
    "\n--- Correlation Figures Saved ---"
)


print(
    correlation_png
)


print(
    correlation_pdf
)


print(
    correlation_svg
)


plt.show()


# ============================================================
# 78. SAVE CORRELATION MATRIX AS CSV
# ============================================================

correlation_csv = (
    output_data_folder
    / "engineering_correlation_matrix.csv"
)


correlation_result.to_csv(
    correlation_csv
)


print(
    "\nCorrelation matrix saved:"
)


print(
    correlation_csv
)


# ============================================================
# 79. SAVE PARAMETER-SWEEP DATA
# ============================================================

parameter_sweep_data = pd.DataFrame(
    {
        "Switching_Frequency_kHz":
            frequency_grid.ravel(),

        "Load_percent":
            load_grid.ravel(),

        "Efficiency_percent":
            efficiency_sweep.ravel()
    }
)


parameter_sweep_csv = (
    output_data_folder
    / "engineering_parameter_sweep.csv"
)


parameter_sweep_data.to_csv(
    parameter_sweep_csv,
    index=False
)


print(
    "\nParameter sweep saved:"
)


print(
    parameter_sweep_csv
)


# ============================================================
# 80. COMMON MISTAKE - NO COLORBAR
# ============================================================

"""
If color represents a physical value, a heatmap without a
colorbar may leave the reader unable to interpret the
numerical meaning.

Use:

fig.colorbar(...)
"""


# ============================================================
# 81. COMMON MISTAKE - WRONG COLORBAR UNIT
# ============================================================

"""
Weak:

Colorbar:

Value


Better:

Efficiency [%]

Temperature [°C]

Power Loss [W]

Magnitude [dBµV]

Correlation Coefficient [-]
"""


# ============================================================
# 82. COMMON MISTAKE - DIFFERENT COLOR LIMITS
# ============================================================

"""
Two heatmaps intended for direct comparison should normally
use consistent color limits.

Otherwise:

The same color

may represent:

Different numerical values.
"""


# ============================================================
# 83. COMMON MISTAKE - NARROW COLOR RANGE
# ============================================================

"""
Suppose values range from:

94.91

to:

95.05


Choosing a color scale covering only:

94.90

to:

95.06


may make very small differences appear visually dramatic.


This may be useful for detailed analysis,

but the numerical range must remain clear.


Do not use color scaling to exaggerate engineering
improvements.
"""


# ============================================================
# 84. COMMON MISTAKE - EXCESSIVELY WIDE COLOR RANGE
# ============================================================

"""
The opposite problem also exists.

Suppose temperature varies:

70 to 90 °C


but the color scale is:

0 to 1000 °C


Nearly all cells may appear visually identical.


Choose meaningful and transparent color limits.
"""


# ============================================================
# 85. COMMON MISTAKE - WRONG COLORMAP TYPE
# ============================================================

"""
For quantities increasing from:

Low
to
High


a sequential colormap is usually intuitive.


For signed differences around:

0


a diverging colormap is often more informative.


The colormap should support the numerical meaning.
"""


# ============================================================
# 86. COMMON MISTAKE - COLOR WITHOUT NUMERICAL CONTEXT
# ============================================================

"""
Do not write:

"The red area is better."


Instead interpret:

Which numerical values?

Which physical quantity?

Which operating conditions?

How large is the difference?
"""


# ============================================================
# 87. COMMON MISTAKE - TOO MANY ANNOTATIONS
# ============================================================

"""
A:

5 × 5

heatmap may work well with numerical annotations.


A:

100 × 100

heatmap generally will not.


Too much text can hide the color pattern.
"""


# ============================================================
# 88. COMMON MISTAKE - CORRELATION = CAUSATION
# ============================================================

"""
Strong correlation does NOT prove:

X causes Y.


Correlation identifies association.

Physical causality requires:

Engineering theory

Controlled experiments

System modeling

and/or

appropriate causal analysis.
"""


# ============================================================
# 89. COMMON MISTAKE - r = 0 MEANS NO RELATIONSHIP
# ============================================================

"""
Pearson:

r ≈ 0


means:

Little or no LINEAR association.


A nonlinear relationship may still exist.


Therefore:

Plot the variables

and

understand the physics.
"""


# ============================================================
# 90. COMMON MISTAKE - ONLY LOOKING AT CORRELATION MATRIX
# ============================================================

"""
A correlation matrix should usually be followed by:

Scatter plots

Physical interpretation

Statistical analysis

Engineering reasoning


The heatmap is a screening and visualization tool.
"""


# ============================================================
# 91. COMMON MISTAKE - MIXING CATEGORICAL VARIABLES
# ============================================================

"""
Correlation matrices are designed primarily for numerical
variables.

Do not automatically convert:

Case A = 1

Case B = 2

Case C = 3


and then interpret Pearson correlation as physically
meaningful.

Categorical variables require appropriate methods.
"""


# ============================================================
# 92. COMMON MISTAKE - MATHEMATICALLY DERIVED FEATURES
# ============================================================

"""
Suppose:

Power = Voltage × Current


Strong correlation between:

Voltage

Current

Power


may partly reflect the mathematical definition of power.


Do not interpret every strong correlation as a newly
discovered physical mechanism.
"""


# ============================================================
# 93. COMMON MISTAKE - IGNORING SAMPLE SIZE
# ============================================================

"""
A correlation calculated from:

n = 5


should not be interpreted with the same confidence as one
based on a much larger, well-designed dataset.


Always consider:

Sample size

Measurement quality

Operating range

Experimental structure
"""


# ============================================================
# 94. COMMON MISTAKE - MIXING OPERATING REGIMES
# ============================================================

"""
Suppose one dataset contains:

Startup

Steady state

Shutdown


A single correlation matrix may combine physically
different regimes.


Consider whether separate analyses are more meaningful.
"""


# ============================================================
# 95. COMMON MISTAKE - MISSING VALUES IGNORED
# ============================================================

"""
Pandas may calculate pairwise correlations using available
observations.

However:

Different correlation pairs may then be based on different
numbers of samples.


Investigate missing data before drawing conclusions.
"""


# ============================================================
# 96. COMMON MISTAKE - imshow PHYSICAL SPACING
# ============================================================

"""
imshow() displays matrix cells on a regular image grid.

If the actual physical X-values are:

10

20

100

1000


their spacing is not automatically represented
proportionally.


For physical coordinates consider:

pcolormesh()

or another coordinate-aware plot.
"""


# ============================================================
# 97. COMMON MISTAKE - HEATMAP WITHOUT RAW VALUES
# ============================================================

"""
Heatmaps are excellent for identifying patterns.

But important results should often also be available as:

Numerical tables

CSV data

Summary metrics


Color alone is not sufficient for reproducible analysis.
"""


# ============================================================
# 98. HEATMAP WORKFLOW
# ============================================================

"""
Engineering Parameter Sweep
          ↓
Select X Parameter
          ↓
Select Y Parameter
          ↓
Select Response Variable
          ↓
Create Matrix / Grid
          ↓
Check Units
          ↓
Check Missing Data
          ↓
Select Colormap
          ↓
Select Color Limits
          ↓
Create Heatmap
          ↓
Add Colorbar
          ↓
Add Labels
          ↓
Optional Annotations
          ↓
Identify Regions / Optimum
          ↓
Engineering Interpretation
"""


# ============================================================
# 99. CORRELATION WORKFLOW
# ============================================================

"""
Research Dataset
      ↓
Inspect Columns
      ↓
Select Numerical Variables
      ↓
Check Missing Values
      ↓
Understand Physical Variables
      ↓
Choose:
Pearson / Spearman / Kendall
      ↓
Calculate Correlation Matrix
      ↓
Use Symmetric Color Scale:
-1 to +1
      ↓
Create Heatmap
      ↓
Identify Strong Associations
      ↓
Create Supporting Scatter Plots
      ↓
Engineering Interpretation
      ↓
Do NOT Claim Causation Automatically
"""


# ============================================================
# 100. PARAMETER-SWEEP WORKFLOW
# ============================================================

"""
Parameter 1
    ×
Parameter 2
        ↓
Simulation / Experiment
        ↓
Response Matrix
        ↓
Heatmap
        ↓
Identify:
Low Region
High Region
Transition
Optimum Candidate
        ↓
Validate Candidate
        ↓
Engineering Decision
"""


# ============================================================
# 101. HEATMAP DECISION GUIDE
# ============================================================

"""
Small Regular Matrix
        ↓
imshow()


Physical X/Y Coordinates
        ↓
pcolormesh()


Need Equal-Value Curves?
        ↓
contour()
or
contourf()


Many Numerical Variables?
        ↓
Correlation Heatmap


Need Individual Relationship?
        ↓
Scatter Plot


Need Distribution?
        ↓
Histogram / Box / Violin
"""


# ============================================================
# 102. PUBLICATION CHECKLIST
# ============================================================

"""
Before publishing a heatmap, check:

What does X represent?

What does Y represent?

What does color represent?

Are all units shown?

Is a colorbar present?

Is the colormap appropriate?

Are color limits justified?

If comparing heatmaps:

Are color limits identical?

Are missing values visible?

Are annotations readable?

Is the matrix orientation correct?

Does the optimum correspond to an actual sampled point?

Does the caption explain the operating conditions?


For correlation maps:

Which correlation method was used?

What is the sample size?

Were missing values present?

Are variables mathematically related?

Are operating regimes mixed?

Has correlation been confused with causation?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
HEATMAPS AND CORRELATION MAPS


1. BASIC HEATMAP

image = ax.imshow(
    matrix
)


------------------------------------------------------------


2. COLORBAR

colorbar = fig.colorbar(

    image,

    ax=ax

)


colorbar.set_label(
    "Efficiency [%]"
)


------------------------------------------------------------


3. AXIS LABELS

ax.set_xticks(...)

ax.set_xticklabels(...)

ax.set_yticks(...)

ax.set_yticklabels(...)


------------------------------------------------------------


4. ANNOTATED HEATMAP

for row in range(
    matrix.shape[0]
):

    for column in range(
        matrix.shape[1]
    ):

        ax.text(

            column,

            row,

            f"{matrix[row, column]:.2f}",

            ha="center",

            va="center"

        )


------------------------------------------------------------


5. SEQUENTIAL COLORMAP

Useful for:

Low
→
High


Examples:

viridis

cividis


------------------------------------------------------------


6. DIVERGING COLORMAP

Useful for:

Negative
→
Zero
→
Positive


Example:

coolwarm


------------------------------------------------------------


7. FIXED COLOR LIMITS

image = ax.imshow(

    matrix,

    vmin=minimum,

    vmax=maximum

)


Especially important when comparing multiple heatmaps.


------------------------------------------------------------


8. DIFFERENCE HEATMAP

difference = (

    design_b

    - design_a

)


For signed data:

Use a symmetric color range around zero.


------------------------------------------------------------


9. pcolormesh()

mesh = ax.pcolormesh(

    x,

    y,

    matrix,

    shading="auto"

)


Useful for physical X/Y coordinates.


------------------------------------------------------------


10. PARAMETER SWEEP

Parameter X
    ×
Parameter Y
        ↓
Response Matrix
        ↓
Heatmap


------------------------------------------------------------


11. FIND MAXIMUM

index = np.unravel_index(

    np.argmax(
        matrix
    ),

    matrix.shape

)


------------------------------------------------------------


12. MISSING DATA

Use:

np.nan

and optionally:

np.ma.masked_invalid()


Do not automatically replace missing measurements with
zero.


------------------------------------------------------------


13. BASIC CORRELATION MATRIX

correlation = dataframe.corr(

    method="pearson",

    numeric_only=True

)


------------------------------------------------------------


14. PEARSON

Useful primarily for:

Linear association


------------------------------------------------------------


15. SPEARMAN

correlation = dataframe.corr(

    method="spearman",

    numeric_only=True

)


Useful for:

Monotonic rank association


------------------------------------------------------------


16. KENDALL

correlation = dataframe.corr(

    method="kendall",

    numeric_only=True

)


Another rank-based association measure.


------------------------------------------------------------


17. CORRELATION RANGE

-1
to
+1


Therefore use:

vmin=-1

vmax=1


for comparable correlation maps.


------------------------------------------------------------


18. POSITIVE CORRELATION

As X increases:

Y tends to increase.


------------------------------------------------------------


19. NEGATIVE CORRELATION

As X increases:

Y tends to decrease.


------------------------------------------------------------


20. NEAR-ZERO PEARSON CORRELATION

Does NOT automatically mean:

No relationship.


A nonlinear relationship may exist.


------------------------------------------------------------


21. CORRELATION != CAUSATION

Strong correlation does not prove a causal mechanism.


------------------------------------------------------------


22. NUMERICAL COLUMNS

numeric_data = dataframe.select_dtypes(

    include="number"

)


------------------------------------------------------------


23. TRIANGULAR CORRELATION MAP

Useful because the correlation matrix is symmetric.

The upper and lower triangles contain repeated pairwise
information.


------------------------------------------------------------


24. imshow()

Best for:

Regular matrix visualization


------------------------------------------------------------


25. pcolormesh()

Best for:

Coordinate-based parameter maps

including nonuniform grids.


------------------------------------------------------------


26. COLOR SCALE MATTERS

Do not manipulate:

vmin

vmax


to visually exaggerate small differences.


------------------------------------------------------------


27. PHYSICAL INTERPRETATION

Do not say only:

"The red region is best."


Report:

Parameter values

Physical response

Numerical difference

Engineering significance


------------------------------------------------------------


28. CORRELATION ANALYSIS

Correlation Map
        ↓
Identify Association
        ↓
Supporting Scatter Plot
        ↓
Physical Explanation
        ↓
Statistical Validation if Required


------------------------------------------------------------


29. ENGINEERING APPLICATIONS

Heatmaps are especially useful for:

Efficiency maps

Loss maps

Temperature maps

Parameter sweeps

EMI maps

Optimization

Sensitivity analysis

ML feature analysis

Correlation analysis

Robustness studies


------------------------------------------------------------


30. MOST IMPORTANT PRINCIPLE

A heatmap converts:

Numbers
    ↓
Colors


The color representation must preserve the scientific
meaning of those numbers.


------------------------------------------------------------


31. COMPLETE WORKFLOW

Engineering Dataset
        ↓
Select Dimensions
        ↓
Construct Matrix
        ↓
Select Physical Color Variable
        ↓
Choose Appropriate Colormap
        ↓
Set Honest Color Limits
        ↓
Heatmap
        ↓
Colorbar
        ↓
Annotations if Useful
        ↓
Identify Patterns
        ↓
Quantify Result
        ↓
Engineering Interpretation
        ↓
Publication Figure


------------------------------------------------------------


NEXT:

25_contour_and_parameter_sweep_plots.py


The next file will extend the same parameter-sweep concept
into:

Mesh grids

contour()

contourf()

Contour levels

Filled contours

Contour labels

Colorbars

Parameter-response surfaces

Efficiency maps

Power-loss maps

Temperature maps

Design constraints

Feasible / infeasible regions

Threshold contours

Optimum points

Multiple response overlays

2D optimization visualization

Irregular sampling considerations

Contour vs heatmap

and publication-quality parameter-sweep figures.
"""
