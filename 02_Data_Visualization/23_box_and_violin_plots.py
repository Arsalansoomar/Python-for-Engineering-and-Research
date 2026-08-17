"""
============================================================
Python for Engineering and Research
23 - Box and Violin Plots
============================================================

Purpose:
    Demonstrate how box plots and violin plots can be used
    to compare distributions from repeated measurements,
    simulations, Monte Carlo studies, and engineering
    experiments.

Topics:
    1. What is a box plot?
    2. Median and quartiles
    3. Interquartile range
    4. Whiskers
    5. Potential outliers / fliers
    6. Single box plot
    7. Multiple engineering cases
    8. Displaying the mean
    9. Horizontal box plots
    10. Notched box plots
    11. Custom whiskers
    12. Showing and hiding fliers
    13. Raw measurements with box plots
    14. What is a violin plot?
    15. Kernel-density concept
    16. Multiple violin plots
    17. Mean and median in violin plots
    18. Quantiles in violin plots
    19. Bandwidth
    20. Horizontal violin plots
    21. Box plot vs violin plot
    22. Unequal sample sizes
    23. Skewed distributions
    24. Bimodal distributions
    25. Engineering design comparison
    26. Distribution summary table
    27. Reusable functions
    28. Publication-oriented comparison
    29. Saving PNG / PDF / SVG
    30. Common mistakes
    31. Key takeaways

Important:
    Box plots and violin plots summarize distributions.

    They do NOT replace the need to understand:

    - Sample size
    - Measurement conditions
    - Experimental design
    - Statistical assumptions
    - Engineering meaning

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
# 2. WHAT IS A BOX PLOT?
# ============================================================

"""
A box plot provides a compact statistical summary.

Typical structure:

          Potential Outlier
                o

                |
                |
        Upper Whisker
                |
          ┌───────────┐
          │    Q3     │
          │-----------│
          │  Median   │
          │-----------│
          │    Q1     │
          └───────────┘
                |
        Lower Whisker
                |

                o
          Potential Outlier


The main components are:

Q1
    25th percentile

Median
    50th percentile

Q3
    75th percentile

IQR
    Q3 - Q1

Whiskers
    Range defined by the box-plot rule

Fliers
    Observations beyond the whiskers
"""


# ============================================================
# 3. ENGINEERING APPLICATIONS
# ============================================================

"""
Box and violin plots are useful for:

Repeated measurements

Monte Carlo simulations

Efficiency distributions

Power-loss variation

Temperature variation

Component tolerance studies

Reliability results

Prediction errors

ML residuals

Experimental repeatability

Parameter sweeps

Manufacturing variation

Robustness studies
"""


# ============================================================
# 4. CREATE REPRODUCIBLE DATA
# ============================================================

rng = np.random.default_rng(
    42
)


baseline = rng.normal(

    loc=94.4,

    scale=0.60,

    size=300

)


design_a = rng.normal(

    loc=95.0,

    scale=0.45,

    size=300

)


design_b = rng.normal(

    loc=95.5,

    scale=0.30,

    size=300

)


design_c = rng.normal(

    loc=95.2,

    scale=0.75,

    size=300

)


engineering_cases = {

    "Baseline":
        baseline,

    "Design A":
        design_a,

    "Design B":
        design_b,

    "Design C":
        design_c

}


# ============================================================
# 5. INSPECT SAMPLE DATA
# ============================================================

print(
    "\n--- Example Engineering Data ---"
)


for case_name, values in engineering_cases.items():

    print(
        case_name
    )

    print(
        values[:5]
    )


# ============================================================
# 6. CALCULATE QUARTILES
# ============================================================

q1 = np.percentile(
    baseline,
    25
)


median = np.percentile(
    baseline,
    50
)


q3 = np.percentile(
    baseline,
    75
)


iqr = (
    q3
    - q1
)


print(
    "\n--- Baseline Quartiles ---"
)


print(
    f"Q1 = {q1:.3f}"
)


print(
    f"Median = {median:.3f}"
)


print(
    f"Q3 = {q3:.3f}"
)


print(
    f"IQR = {iqr:.3f}"
)


# ============================================================
# 7. INTERQUARTILE RANGE
# ============================================================

"""
The interquartile range is:

IQR = Q3 - Q1


It describes the spread of the central:

50%

of the observations.


Unlike the full range:

Maximum - Minimum


the IQR is less affected by extreme observations.
"""


# ============================================================
# 8. DEFAULT OUTLIER FENCES
# ============================================================

lower_fence = (
    q1
    - 1.5
    * iqr
)


upper_fence = (
    q3
    + 1.5
    * iqr
)


print(
    "\n--- Box-Plot Fences ---"
)


print(
    f"Lower Fence = "
    f"{lower_fence:.3f}"
)


print(
    f"Upper Fence = "
    f"{upper_fence:.3f}"
)


# ============================================================
# 9. POTENTIAL OUTLIERS
# ============================================================

potential_outliers = baseline[
    (
        baseline
        < lower_fence
    )
    |
    (
        baseline
        > upper_fence
    )
]


print(
    "\nPotential Baseline Outliers:"
)


print(
    potential_outliers
)


# ============================================================
# 10. IMPORTANT OUTLIER NOTE
# ============================================================

"""
A point displayed as a box-plot flier is NOT automatically:

Bad data

Measurement error

or

A point that should be deleted.


It only means that the observation lies beyond the chosen
box-plot whisker rule.

Engineering investigation is still required.
"""


# ============================================================
# 11. BASIC SINGLE BOX PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(5, 4.5)
)


ax.boxplot(
    baseline
)


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Baseline Efficiency Distribution"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 12. LABEL A SINGLE BOX
# ============================================================

fig, ax = plt.subplots(
    figsize=(5, 4.5)
)


ax.boxplot(

    baseline,

    tick_labels=[
        "Baseline"
    ]

)


ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 13. MULTIPLE BOX PLOTS
# ============================================================

case_names = list(
    engineering_cases.keys()
)


case_values = list(
    engineering_cases.values()
)


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.boxplot(

    case_values,

    tick_labels=case_names

)


ax.set_xlabel(
    "Design"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Engineering Design Distribution Comparison"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 14. INTERPRETING MULTIPLE BOX PLOTS
# ============================================================

"""
A box plot allows several features to be compared quickly:

Median
    Typical central value


Box height
    Central 50% spread


Whiskers
    Broader spread


Fliers
    Unusual observations


Example interpretation:

Design B may show:

Higher median
        +
Smaller IQR


which can indicate:

Higher central performance
        +
Lower variability


However:

Engineering conclusions should be based on the actual
data and experimental context.
"""


# ============================================================
# 15. DISPLAY THE MEAN
# ============================================================

"""
The mean is not normally the main central marker of a box
plot.

It can be added using:

showmeans=True
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.boxplot(

    case_values,

    tick_labels=case_names,

    showmeans=True

)


ax.set_xlabel(
    "Design"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Box Plot with Mean Markers"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 16. MEAN VS MEDIAN
# ============================================================

"""
Mean and median answer different questions.

Mean:

Arithmetic average


Median:

Middle observation after sorting


For symmetric distributions they may be similar.

For:

Skewed data

or

Data containing extreme values


they may differ noticeably.
"""


# ============================================================
# 17. HORIZONTAL BOX PLOT
# ============================================================

"""
Horizontal box plots are useful when:

Case names are long

Many cases exist

The numerical axis is easier to read horizontally
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.boxplot(

    case_values,

    tick_labels=case_names,

    orientation="horizontal"

)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Design"
)

ax.set_title(
    "Horizontal Engineering Box Plot"
)


ax.grid(
    True,
    axis="x"
)


plt.tight_layout()

plt.show()


# ============================================================
# 18. NOTCHED BOX PLOT
# ============================================================

"""
Use:

notch=True


to display notches around the median.

Notches relate to uncertainty around the median according
to the box-plot calculation.

They should not be treated as a substitute for a complete
statistical comparison.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.boxplot(

    case_values,

    tick_labels=case_names,

    notch=True

)


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Notched Box Plot"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 19. CUSTOM WHISKER RANGE
# ============================================================

"""
Default box plots commonly use:

1.5 × IQR


Matplotlib also allows other definitions.

Example:

5th to 95th percentile:

whis=(5, 95)
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.boxplot(

    case_values,

    tick_labels=case_names,

    whis=(
        5,
        95
    )

)


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Whiskers at 5th and 95th Percentiles"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 20. FULL DATA RANGE WHISKERS
# ============================================================

"""
To make whiskers cover the full data range:

whis=(0, 100)


This changes the interpretation of the box plot.

Therefore the whisker definition should be stated when it
differs from the normal convention.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.boxplot(

    case_values,

    tick_labels=case_names,

    whis=(
        0,
        100
    )

)


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Full-Range Whiskers"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 21. SHOW OR HIDE FLIERS
# ============================================================

"""
Use:

showfliers=False


to hide points beyond the whiskers.


Important:

Hiding them visually does NOT remove them from the data.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.boxplot(

    case_values,

    tick_labels=case_names,

    showfliers=False

)


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Box Plot Without Displayed Fliers"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 22. HIDING FLIERS WARNING
# ============================================================

"""
Hiding fliers can make a figure cleaner.

However:

If unusual observations are scientifically important,
hiding them may conceal relevant information.


Use:

showfliers=False


only when it supports the intended presentation and the
handling of extreme observations remains transparent.
"""


# ============================================================
# 23. RAW DATA + BOX PLOT
# ============================================================

"""
For small or moderate datasets, showing raw observations
together with the box plot can be very informative.

The box plot summarizes the data.

The individual points show the actual observations.
"""


small_cases = {

    "Baseline":
        rng.normal(
            94.4,
            0.6,
            30
        ),

    "Design A":
        rng.normal(
            95.0,
            0.45,
            30
        ),

    "Design B":
        rng.normal(
            95.5,
            0.30,
            30
        )

}


small_case_names = list(
    small_cases.keys()
)


small_case_values = list(
    small_cases.values()
)


fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


positions = np.arange(
    1,
    len(
        small_case_names
    )
    + 1
)


ax.boxplot(

    small_case_values,

    positions=positions,

    tick_labels=small_case_names,

    widths=0.5

)


for position, values in zip(
    positions,
    small_case_values
):

    jitter = rng.normal(

        loc=0,

        scale=0.04,

        size=len(
            values
        )

    )


    ax.scatter(

        position
        + jitter,

        values,

        alpha=0.55,

        s=18

    )


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Box Plot with Raw Measurements"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 24. WHY ADD RAW POINTS?
# ============================================================

"""
Box plots compress information.

Two datasets can produce similar:

Median

Q1

Q3


while having different detailed distributions.


Raw points can reveal:

Clusters

Gaps

Outliers

Small sample sizes

Repeated values
"""


# ============================================================
# 25. WHAT IS A VIOLIN PLOT?
# ============================================================

"""
A violin plot combines distribution information with a
compact categorical comparison.

Conceptually:

Thin Region
    ↓
Lower estimated density


Wide Region
    ↓
Higher estimated density


Unlike a box plot, the violin shows an estimated
distribution shape.
"""


# ============================================================
# 26. BASIC VIOLIN PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.violinplot(

    case_values,

    positions=np.arange(
        1,
        len(
            case_names
        )
        + 1
    )

)


ax.set_xticks(
    np.arange(
        1,
        len(
            case_names
        )
        + 1
    )
)


ax.set_xticklabels(
    case_names
)


ax.set_xlabel(
    "Design"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Engineering Violin Plot"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 27. VIOLIN DENSITY CONCEPT
# ============================================================

"""
The width of the violin represents an estimated
probability-density shape.

It is NOT simply:

Number of observations


The shape is estimated using:

Kernel Density Estimation

KDE


Therefore violin appearance depends partly on the density
estimation method and bandwidth.
"""


# ============================================================
# 28. VIOLIN WITH MEDIAN
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.violinplot(

    case_values,

    showmedians=True

)


ax.set_xticks(
    np.arange(
        1,
        len(
            case_names
        )
        + 1
    )
)


ax.set_xticklabels(
    case_names
)


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Violin Plot with Median"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 29. VIOLIN WITH MEAN AND MEDIAN
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.violinplot(

    case_values,

    showmeans=True,

    showmedians=True,

    showextrema=True

)


ax.set_xticks(
    np.arange(
        1,
        len(
            case_names
        )
        + 1
    )
)


ax.set_xticklabels(
    case_names
)


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Violin Plot with Mean and Median"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 30. EXTREMA
# ============================================================

"""
showextrema=True

can display information about the minimum and maximum
range represented by the violin.


Remember:

Minimum and maximum can be strongly influenced by rare
observations.
"""


# ============================================================
# 31. VIOLIN QUANTILES
# ============================================================

"""
Violin plots can also display selected quantiles.

Example:

25%

50%

75%
"""


quantiles = [

    [
        0.25,
        0.50,
        0.75
    ]

    for _ in case_values

]


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.violinplot(

    case_values,

    quantiles=quantiles,

    showextrema=True

)


ax.set_xticks(
    np.arange(
        1,
        len(
            case_names
        )
        + 1
    )
)


ax.set_xticklabels(
    case_names
)


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Violin Plot with Quartiles"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 32. BANDWIDTH
# ============================================================

"""
The KDE bandwidth controls how smooth the violin appears.

Smaller effective bandwidth:

More local detail


Larger effective bandwidth:

Smoother distribution


Matplotlib supports examples such as:

bw_method="scott"

bw_method="silverman"


Do not change bandwidth only to create a preferred visual
shape.
"""


# ============================================================
# 33. SCOTT BANDWIDTH
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.violinplot(

    case_values,

    showmedians=True,

    bw_method="scott"

)


ax.set_xticks(
    np.arange(
        1,
        len(
            case_names
        )
        + 1
    )
)


ax.set_xticklabels(
    case_names
)


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Violin Plot - Scott Bandwidth"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 34. SILVERMAN BANDWIDTH
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.violinplot(

    case_values,

    showmedians=True,

    bw_method="silverman"

)


ax.set_xticks(
    np.arange(
        1,
        len(
            case_names
        )
        + 1
    )
)


ax.set_xticklabels(
    case_names
)


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Violin Plot - Silverman Bandwidth"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 35. BANDWIDTH WARNING
# ============================================================

"""
A violin plot is not the raw distribution itself.

It is a smoothed estimate.

Therefore apparent:

Peaks

Valleys

Shoulders


can change with bandwidth.


Check raw data or histograms before making strong
conclusions from small density features.
"""


# ============================================================
# 36. HORIZONTAL VIOLIN PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


positions = np.arange(
    1,
    len(
        case_names
    )
    + 1
)


ax.violinplot(

    case_values,

    positions=positions,

    orientation="horizontal",

    showmedians=True

)


ax.set_yticks(
    positions
)


ax.set_yticklabels(
    case_names
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Design"
)

ax.set_title(
    "Horizontal Violin Plot"
)


ax.grid(
    True,
    axis="x"
)


plt.tight_layout()

plt.show()


# ============================================================
# 37. BOX PLOT VS VIOLIN PLOT
# ============================================================

"""
BOX PLOT

Best for compactly showing:

Median

Quartiles

IQR

Whiskers

Potential outliers


------------------------------------------------------------


VIOLIN PLOT

Best for visualizing:

Distribution shape

Density

Possible asymmetry

Multiple peaks


------------------------------------------------------------


Neither is universally better.

They answer slightly different questions.
"""


# ============================================================
# 38. SIDE-BY-SIDE BOX AND VIOLIN
# ============================================================

fig, axes = plt.subplots(

    1,

    2,

    figsize=(11, 4.8),

    sharey=True

)


# ------------------------------------------------------------
# Box plot
# ------------------------------------------------------------

axes[0].boxplot(

    case_values,

    tick_labels=case_names,

    showmeans=True

)


axes[0].set_ylabel(
    "Efficiency [%]"
)


axes[0].set_title(
    "Box Plot"
)


axes[0].grid(
    True,
    axis="y"
)


# ------------------------------------------------------------
# Violin plot
# ------------------------------------------------------------

axes[1].violinplot(

    case_values,

    showmedians=True

)


axes[1].set_xticks(
    np.arange(
        1,
        len(
            case_names
        )
        + 1
    )
)


axes[1].set_xticklabels(
    case_names
)


axes[1].set_title(
    "Violin Plot"
)


axes[1].grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 39. SKEWED DISTRIBUTION EXAMPLE
# ============================================================

"""
Box and violin plots become particularly useful when the
distribution is not symmetric.
"""


symmetric_data = rng.normal(

    loc=50,

    scale=5,

    size=500

)


skewed_data = (

    40

    + rng.exponential(

        scale=5,

        size=500

    )

)


distribution_examples = [

    symmetric_data,

    skewed_data

]


distribution_names = [

    "Symmetric",

    "Skewed"

]


# ============================================================
# 40. SKEWED BOX PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(6.5, 4.5)
)


ax.boxplot(

    distribution_examples,

    tick_labels=distribution_names,

    showmeans=True

)


ax.set_ylabel(
    "Measured Value [-]"
)

ax.set_title(
    "Symmetric vs Skewed Distribution"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 41. SKEWED VIOLIN PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(6.5, 4.5)
)


ax.violinplot(

    distribution_examples,

    showmeans=True,

    showmedians=True

)


ax.set_xticks(
    [
        1,
        2
    ]
)


ax.set_xticklabels(
    distribution_names
)


ax.set_ylabel(
    "Measured Value [-]"
)

ax.set_title(
    "Distribution Shape Comparison"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 42. BIMODAL DISTRIBUTION
# ============================================================

"""
A violin plot can reveal distribution structure that may
not be obvious from a box plot.

Example:

Two operating populations

or

Two process states
"""


bimodal_data = np.concatenate(
    [
        rng.normal(
            47,
            1.5,
            250
        ),

        rng.normal(
            55,
            1.5,
            250
        )
    ]
)


unimodal_data = rng.normal(

    51,

    3,

    500

)


# ============================================================
# 43. BOX PLOT OF UNI- AND BIMODAL DATA
# ============================================================

fig, ax = plt.subplots(
    figsize=(6.5, 4.5)
)


ax.boxplot(

    [
        unimodal_data,
        bimodal_data
    ],

    tick_labels=[
        "Unimodal",
        "Bimodal"
    ]

)


ax.set_ylabel(
    "Measured Value [-]"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 44. VIOLIN PLOT OF UNI- AND BIMODAL DATA
# ============================================================

fig, ax = plt.subplots(
    figsize=(6.5, 4.5)
)


ax.violinplot(

    [
        unimodal_data,
        bimodal_data
    ],

    showmedians=True

)


ax.set_xticks(
    [
        1,
        2
    ]
)


ax.set_xticklabels(
    [
        "Unimodal",
        "Bimodal"
    ]
)


ax.set_ylabel(
    "Measured Value [-]"
)

ax.set_title(
    "Violin Plot Revealing Distribution Shape"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 45. IMPORTANT BIMODAL NOTE
# ============================================================

"""
If a violin appears to contain two modes, investigate the
engineering cause.

Possible explanations include:

Two operating states

Different environmental conditions

Mixed experiments

Different populations

Control-mode transitions

Different parameter groups


Do not interpret a density feature without checking the
underlying observations.
"""


# ============================================================
# 46. UNEQUAL SAMPLE SIZES
# ============================================================

unequal_cases = {

    "Case A":
        rng.normal(
            95.0,
            0.4,
            50
        ),

    "Case B":
        rng.normal(
            95.2,
            0.4,
            500
        ),

    "Case C":
        rng.normal(
            95.4,
            0.4,
            5000
        )

}


# ============================================================
# 47. SAMPLE SIZE SUMMARY
# ============================================================

print(
    "\n--- Unequal Sample Sizes ---"
)


for case_name, values in unequal_cases.items():

    print(
        case_name,
        ":",
        len(
            values
        )
    )


# ============================================================
# 48. VIOLIN WIDTH DOES NOT MEAN SAMPLE SIZE
# ============================================================

"""
Standard violin width should not automatically be
interpreted as:

Larger violin
=
More observations


Sample size should be reported explicitly.

Example legend/caption:

Case A:
n = 50

Case B:
n = 500

Case C:
n = 5000
"""


# ============================================================
# 49. BOXPLOT WITH SAMPLE SIZE LABELS
# ============================================================

unequal_names = [

    (
        f"{case_name}\n"
        f"n={len(values)}"
    )

    for case_name, values
    in unequal_cases.items()

]


fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


ax.boxplot(

    list(
        unequal_cases.values()
    ),

    tick_labels=unequal_names

)


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Distribution Comparison with Sample Size"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 50. ENGINEERING POWER-LOSS EXAMPLE
# ============================================================

"""
Now consider a metric where:

LOWER is better.

Example:

Power loss.
"""


baseline_loss = rng.normal(

    loc=18.0,

    scale=1.5,

    size=400

)


design_a_loss = rng.normal(

    loc=15.5,

    scale=1.1,

    size=400

)


design_b_loss = rng.normal(

    loc=13.8,

    scale=0.8,

    size=400

)


loss_cases = {

    "Baseline":
        baseline_loss,

    "Design A":
        design_a_loss,

    "Design B":
        design_b_loss

}


# ============================================================
# 51. POWER-LOSS BOX PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.8)
)


ax.boxplot(

    list(
        loss_cases.values()
    ),

    tick_labels=list(
        loss_cases.keys()
    ),

    showmeans=True

)


ax.set_xlabel(
    "Design"
)

ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Power-Loss Distribution"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 52. HIGHER / LOWER ENGINEERING MEANING
# ============================================================

"""
Plot interpretation depends on the metric.

Efficiency:

Higher may be better.


Power loss:

Lower may be better.


Temperature:

Often lower may be preferable.


Prediction error:

Lower is generally preferable.


Do not interpret position on the plot without knowing the
engineering objective.
"""


# ============================================================
# 53. DISTRIBUTION SUMMARY FUNCTION
# ============================================================

def summarize_distribution(
    values
):
    """
    Return common descriptive statistics for a numerical
    distribution.
    """

    values = np.asarray(
        values,
        dtype=float
    )


    values = values[
        np.isfinite(
            values
        )
    ]


    if len(
        values
    ) == 0:

        raise ValueError(
            "No valid numerical observations."
        )


    q1 = np.percentile(
        values,
        25
    )


    q3 = np.percentile(
        values,
        75
    )


    return {

        "Samples":
            len(
                values
            ),

        "Mean":
            np.mean(
                values
            ),

        "Median":
            np.median(
                values
            ),

        "Standard_Deviation":
            (
                np.std(
                    values,
                    ddof=1
                )

                if len(
                    values
                ) > 1

                else np.nan
            ),

        "Minimum":
            np.min(
                values
            ),

        "Q1":
            q1,

        "Q3":
            q3,

        "IQR":
            (
                q3
                - q1
            ),

        "Maximum":
            np.max(
                values
            ),

        "5th_Percentile":
            np.percentile(
                values,
                5
            ),

        "95th_Percentile":
            np.percentile(
                values,
                95
            )

    }


# ============================================================
# 54. CREATE SUMMARY TABLE
# ============================================================

summary_rows = []


for case_name, values in engineering_cases.items():

    statistics = summarize_distribution(
        values
    )


    statistics[
        "Case"
    ] = case_name


    summary_rows.append(
        statistics
    )


summary_data = pd.DataFrame(
    summary_rows
)


column_order = [

    "Case",

    "Samples",

    "Mean",

    "Median",

    "Standard_Deviation",

    "Minimum",

    "Q1",

    "Q3",

    "IQR",

    "Maximum",

    "5th_Percentile",

    "95th_Percentile"

]


summary_data = summary_data[
    column_order
]


print(
    "\n--- Engineering Distribution Summary ---"
)


print(
    summary_data
)


# ============================================================
# 55. SAVE SUMMARY TABLE
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


output_data_folder = (
    script_folder
    / "output_data"
)


output_data_folder.mkdir(
    parents=True,
    exist_ok=True
)


summary_file = (
    output_data_folder
    / "box_violin_distribution_summary.csv"
)


summary_data.to_csv(
    summary_file,
    index=False
)


print(
    "\nSummary saved:"
)


print(
    summary_file
)


# ============================================================
# 56. REUSABLE BOX-PLOT FUNCTION
# ============================================================

def plot_box_comparison(
    datasets,
    y_label,
    title=None,
    showmeans=False,
    showfliers=True,
    orientation="vertical"
):
    """
    Create a box-plot comparison for several datasets.

    Parameters
    ----------
    datasets : dict
        Mapping:
        display label -> numerical observations

    y_label : str
        Numerical axis label.

    title : str, optional
        Figure title.

    showmeans : bool
        Show arithmetic means.

    showfliers : bool
        Display observations beyond whiskers.

    orientation : str
        "vertical" or "horizontal"

    Returns
    -------
    fig, ax
        Matplotlib figure and axis.
    """

    if not datasets:

        raise ValueError(
            "At least one dataset is required."
        )


    if orientation not in {
        "vertical",
        "horizontal"
    }:

        raise ValueError(
            "orientation must be "
            "'vertical' or 'horizontal'."
        )


    cleaned_data = []

    labels = []


    for case_name, values in datasets.items():

        values = np.asarray(
            values,
            dtype=float
        )


        values = values[
            np.isfinite(
                values
            )
        ]


        if len(
            values
        ) == 0:

            raise ValueError(
                f"No valid values for "
                f"{case_name}."
            )


        cleaned_data.append(
            values
        )


        labels.append(
            case_name
        )


    fig, ax = plt.subplots(
        figsize=(8, 4.8)
    )


    ax.boxplot(

        cleaned_data,

        tick_labels=labels,

        showmeans=showmeans,

        showfliers=showfliers,

        orientation=orientation

    )


    if orientation == "vertical":

        ax.set_ylabel(
            y_label
        )


        ax.grid(
            True,
            axis="y"
        )

    else:

        ax.set_xlabel(
            y_label
        )


        ax.grid(
            True,
            axis="x"
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
# 57. USE BOX-PLOT FUNCTION
# ============================================================

fig, ax = plot_box_comparison(

    datasets=engineering_cases,

    y_label="Efficiency [%]",

    title="Engineering Efficiency Comparison",

    showmeans=True,

    showfliers=True

)


plt.show()


# ============================================================
# 58. REUSABLE VIOLIN FUNCTION
# ============================================================

def plot_violin_comparison(
    datasets,
    y_label,
    title=None,
    showmeans=False,
    showmedians=True,
    orientation="vertical",
    bw_method="scott"
):
    """
    Create a violin-plot comparison.

    Parameters
    ----------
    datasets : dict
        Mapping:
        display label -> observations

    y_label : str
        Numerical axis label.

    title : str, optional
        Figure title.

    showmeans : bool
        Display mean.

    showmedians : bool
        Display median.

    orientation : str
        "vertical" or "horizontal"

    bw_method : str or float
        KDE bandwidth method.

    Returns
    -------
    fig, ax
        Matplotlib figure and axis.
    """

    if not datasets:

        raise ValueError(
            "At least one dataset is required."
        )


    if orientation not in {
        "vertical",
        "horizontal"
    }:

        raise ValueError(
            "orientation must be "
            "'vertical' or 'horizontal'."
        )


    labels = []

    cleaned_data = []


    for case_name, values in datasets.items():

        values = np.asarray(
            values,
            dtype=float
        )


        values = values[
            np.isfinite(
                values
            )
        ]


        if len(
            values
        ) < 2:

            raise ValueError(
                f"Violin plot requires sufficient "
                f"numerical observations for "
                f"{case_name}."
            )


        labels.append(
            case_name
        )


        cleaned_data.append(
            values
        )


    positions = np.arange(
        1,
        len(
            labels
        )
        + 1
    )


    fig, ax = plt.subplots(
        figsize=(8, 4.8)
    )


    ax.violinplot(

        cleaned_data,

        positions=positions,

        showmeans=showmeans,

        showmedians=showmedians,

        orientation=orientation,

        bw_method=bw_method

    )


    if orientation == "vertical":

        ax.set_xticks(
            positions
        )


        ax.set_xticklabels(
            labels
        )


        ax.set_ylabel(
            y_label
        )


        ax.grid(
            True,
            axis="y"
        )

    else:

        ax.set_yticks(
            positions
        )


        ax.set_yticklabels(
            labels
        )


        ax.set_xlabel(
            y_label
        )


        ax.grid(
            True,
            axis="x"
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
# 59. USE VIOLIN FUNCTION
# ============================================================

fig, ax = plot_violin_comparison(

    datasets=engineering_cases,

    y_label="Efficiency [%]",

    title="Engineering Efficiency Distributions",

    showmeans=False,

    showmedians=True,

    bw_method="scott"

)


plt.show()


# ============================================================
# 60. BOX PLOT + VIOLIN OVERLAY
# ============================================================

"""
A violin plot can be combined with a narrow box plot.

This provides:

Distribution shape
        +
Quartile summary


Use carefully to avoid visual clutter.
"""


positions = np.arange(
    1,
    len(
        case_values
    )
    + 1
)


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.violinplot(

    case_values,

    positions=positions,

    widths=0.8,

    showextrema=False

)


ax.boxplot(

    case_values,

    positions=positions,

    widths=0.18,

    showfliers=False

)


ax.set_xticks(
    positions
)


ax.set_xticklabels(
    case_names
)


ax.set_xlabel(
    "Design"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Violin + Box Plot"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 61. WHY COMBINE BOX AND VIOLIN?
# ============================================================

"""
VIOLIN

shows:

Estimated distribution shape


BOX

shows:

Median

Quartiles

IQR


Together they can provide a compact research figure.

However:

Do not combine them when the result becomes visually
overloaded.
"""


# ============================================================
# 62. PUBLICATION-ORIENTED FINAL FIGURE
# ============================================================

"""
For a paper, the most useful layout may be:

(a) Box plot

(b) Violin plot


This lets readers see both:

Summary statistics

and

Distribution shape.
"""


fig, axes = plt.subplots(

    1,

    2,

    figsize=(10, 4.5),

    sharey=True

)


# ------------------------------------------------------------
# Panel (a): Box plot
# ------------------------------------------------------------

axes[0].boxplot(

    case_values,

    tick_labels=case_names,

    showmeans=True

)


axes[0].set_ylabel(
    "Efficiency [%]"
)


axes[0].set_title(
    "(a) Box Plot"
)


axes[0].grid(
    True,
    axis="y"
)


# ------------------------------------------------------------
# Panel (b): Violin plot
# ------------------------------------------------------------

axes[1].violinplot(

    case_values,

    showmedians=True

)


axes[1].set_xticks(
    positions
)


axes[1].set_xticklabels(
    case_names
)


axes[1].set_title(
    "(b) Violin Plot"
)


axes[1].grid(
    True,
    axis="y"
)


plt.tight_layout()


# ============================================================
# 63. OUTPUT FOLDER
# ============================================================

output_figure_folder = (
    script_folder
    / "output_figures"
    / "box_violin"
)


output_figure_folder.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 64. SAVE PNG
# ============================================================

png_file = (
    output_figure_folder
    / "box_violin_engineering_comparison.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 65. SAVE PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "box_violin_engineering_comparison.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 66. SAVE SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "box_violin_engineering_comparison.svg"
)


fig.savefig(
    svg_file,
    bbox_inches="tight"
)


print(
    "\n--- Figures Saved ---"
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
# 67. BOX PLOT VS HISTOGRAM
# ============================================================

"""
HISTOGRAM

Shows:

Distribution through frequency bins


Advantages:

Detailed distribution view


Disadvantages:

Requires bin selection

Several cases may overlap badly


------------------------------------------------------------


BOX PLOT

Shows:

Median
Quartiles
IQR
Whiskers
Fliers


Advantages:

Compact comparison


Disadvantages:

Hides detailed distribution shape
"""


# ============================================================
# 68. VIOLIN VS HISTOGRAM
# ============================================================

"""
HISTOGRAM

Uses:

Discrete bins


VIOLIN

Uses:

Smoothed density estimation


Histogram shape depends on:

Bin width


Violin shape depends on:

KDE bandwidth


Both require thoughtful interpretation.
"""


# ============================================================
# 69. BOX PLOT VS ERROR BAR
# ============================================================

"""
ERROR BAR

May represent:

SD

SEM

Confidence interval

Measurement uncertainty


------------------------------------------------------------


BOX PLOT

Typically represents:

Median

Quartiles

IQR

Whisker rule

Potential outliers


Therefore:

Box plots

and

Mean ± error bars


do NOT communicate the same information.
"""


# ============================================================
# 70. SMALL SAMPLE WARNING
# ============================================================

"""
For very small datasets:

n = 3

n = 5

n = 6


a violin plot can create a smooth-looking distribution that
suggests more information than actually exists.


For small n, consider showing:

Raw points

+
Box plot

or simply:

Raw measurements.
"""


# ============================================================
# 71. LARGE SAMPLE DATA
# ============================================================

"""
For:

Thousands

or

Millions


of Monte Carlo observations, plotting every individual
point may be unnecessary.

Box and violin plots provide compact distribution
summaries.

Histograms may also remain useful.
"""


# ============================================================
# 72. COMMON MISTAKE - WHISKERS = MIN/MAX
# ============================================================

"""
Do not automatically interpret the default whiskers as:

Minimum

and

Maximum.


Default box-plot whiskers use a statistical rule based on
the IQR.

Observations outside the whiskers may be displayed
separately as fliers.
"""


# ============================================================
# 73. COMMON MISTAKE - FLIER = ERROR
# ============================================================

"""
A flier is not automatically:

Bad measurement

Sensor failure

Data-entry error


It is a statistical position relative to the chosen
whisker rule.

Investigate the physical reason before removing data.
"""


# ============================================================
# 74. COMMON MISTAKE - HIDING FLIERS WITHOUT EXPLANATION
# ============================================================

"""
showfliers=False

can improve readability.

But if extreme observations affect the scientific
conclusion, hiding them can be misleading.

The full data should remain available for analysis.
"""


# ============================================================
# 75. COMMON MISTAKE - VIOLIN WIDTH = SAMPLE SIZE
# ============================================================

"""
Do not interpret a standard violin width as:

Number of observations.


If sample sizes differ substantially, report:

n = ...


for each case.
"""


# ============================================================
# 76. COMMON MISTAKE - OVERINTERPRETING KDE PEAKS
# ============================================================

"""
Small peaks in a violin plot may depend on:

Sample size

Bandwidth

Random variation


Confirm important structures using:

Raw data

Histograms

Engineering understanding
"""


# ============================================================
# 77. COMMON MISTAKE - COMPARING DIFFERENT CONDITIONS
# ============================================================

"""
Example:

Baseline measured at:

25 °C


Design A measured at:

80 °C


A box plot may visually compare them, but the engineering
comparison may not be fair if temperature was not intended
as the experimental variable.


Keep operating conditions controlled.
"""


# ============================================================
# 78. COMMON MISTAKE - MIXED UNITS
# ============================================================

"""
Do not place:

Voltage [V]

Current [A]

Temperature [°C]


into the same box-plot numerical axis merely because they
are all numerical variables.


Compare quantities with compatible meaning and units.
"""


# ============================================================
# 79. COMMON MISTAKE - NO SAMPLE SIZE
# ============================================================

"""
A box plot does not automatically communicate:

n


Report sample size when it matters.

Example:

Baseline:

n = 20


Design A:

n = 2000


The statistical confidence and visual interpretation may
differ considerably.
"""


# ============================================================
# 80. COMMON MISTAKE - BOX PLOT AS SIGNIFICANCE TEST
# ============================================================

"""
Different medians or non-overlapping boxes do NOT
automatically prove statistical significance.

Formal statistical comparison requires an appropriate
analysis based on:

Experimental design

Distribution assumptions

Sample size

Research question
"""


# ============================================================
# 81. COMMON MISTAKE - NOTCHES AS UNIVERSAL SIGNIFICANCE
# ============================================================

"""
Notches visualize uncertainty around the median according
to the box-plot procedure.

Do not convert visual notch overlap into an automatic
universal hypothesis-test conclusion.
"""


# ============================================================
# 82. COMMON MISTAKE - VIOLIN FOR TWO DATA POINTS
# ============================================================

"""
A violin plot estimates a density.

Very small datasets provide limited information for such
an estimate.

Show raw observations for small experimental datasets.
"""


# ============================================================
# 83. COMMON MISTAKE - ONLY PLOT DISTRIBUTION
# ============================================================

"""
A distribution plot may show:

Design B has lower variability.


But the research should also quantify results.

Useful statistics include:

Mean

Median

SD

IQR

Percentiles

Sample size
"""


# ============================================================
# 84. BOX-PLOT WORKFLOW
# ============================================================

"""
Repeated Measurements
        ↓
Clean Data
        ↓
Check Sample Size
        ↓
Calculate:
Q1
Median
Q3
IQR
        ↓
Create Box Plot
        ↓
Inspect Whiskers
        ↓
Inspect Fliers
        ↓
Compare Cases
        ↓
Engineering Interpretation
"""


# ============================================================
# 85. VIOLIN-PLOT WORKFLOW
# ============================================================

"""
Repeated / Population Data
        ↓
Check Sample Size
        ↓
Check Distribution
        ↓
Choose KDE Bandwidth
        ↓
Create Violin Plot
        ↓
Show Median / Quantiles
        ↓
Compare Distribution Shape
        ↓
Check Raw Data
        ↓
Engineering Interpretation
"""


# ============================================================
# 86. ENGINEERING DECISION GUIDE
# ============================================================

"""
Need exact waveform?
        ↓
LINE PLOT


Need numerical relationship?
        ↓
SCATTER PLOT


Need distribution using bins?
        ↓
HISTOGRAM


Need compact quartile comparison?
        ↓
BOX PLOT


Need compact distribution-shape comparison?
        ↓
VIOLIN PLOT


Need uncertainty of mean or measurement?
        ↓
ERROR BARS / CONFIDENCE BANDS
"""


# ============================================================
# 87. PUBLICATION CHECKLIST
# ============================================================

"""
Before publishing box or violin plots, check:

What does each observation represent?

Are all cases measured under comparable conditions?

Are units clearly shown?

What is the sample size?

Is the box-plot whisker definition clear?

Are fliers shown or hidden?

Are unusual observations investigated?

For violin plots:

Is the sample size sufficient?

Is bandwidth reasonable?

Are KDE features being overinterpreted?

Would raw points improve clarity?

Would a histogram provide useful supporting information?

Are summary statistics reported?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
BOX AND VIOLIN PLOTS


1. BASIC BOX PLOT

ax.boxplot(
    data
)


------------------------------------------------------------


2. MULTIPLE BOX PLOTS

ax.boxplot(

    [
        case_a,
        case_b,
        case_c
    ],

    tick_labels=[
        "A",
        "B",
        "C"
    ]

)


------------------------------------------------------------


3. BOX CONTENT

Box:

Q1 to Q3


Middle line:

Median


IQR:

Q3 - Q1


------------------------------------------------------------


4. DEFAULT WHISKER CONCEPT

Default whiskers are based on:

1.5 × IQR


They are NOT automatically:

Minimum and Maximum


------------------------------------------------------------


5. SHOW MEAN

ax.boxplot(

    data,

    showmeans=True

)


------------------------------------------------------------


6. HIDE FLIERS

ax.boxplot(

    data,

    showfliers=False

)


This hides them visually.

It does NOT delete them.


------------------------------------------------------------


7. CUSTOM WHISKERS

ax.boxplot(

    data,

    whis=(
        5,
        95
    )

)


------------------------------------------------------------


8. FULL-RANGE WHISKERS

whis=(
    0,
    100
)


------------------------------------------------------------


9. HORIZONTAL BOX PLOT

ax.boxplot(

    data,

    orientation="horizontal"

)


------------------------------------------------------------


10. NOTCHED BOX PLOT

ax.boxplot(

    data,

    notch=True

)


------------------------------------------------------------


11. BASIC VIOLIN PLOT

ax.violinplot(
    data
)


------------------------------------------------------------


12. SHOW MEDIAN

ax.violinplot(

    data,

    showmedians=True

)


------------------------------------------------------------


13. SHOW MEAN

ax.violinplot(

    data,

    showmeans=True

)


------------------------------------------------------------


14. SHOW QUANTILES

ax.violinplot(

    data,

    quantiles=[
        [
            0.25,
            0.50,
            0.75
        ]
    ]

)


------------------------------------------------------------


15. KDE BANDWIDTH

Examples:

bw_method="scott"

bw_method="silverman"


Bandwidth affects smoothness.


------------------------------------------------------------


16. BOX PLOT

Best for:

Median

Quartiles

IQR

Outlier screening

Compact case comparison


------------------------------------------------------------


17. VIOLIN PLOT

Best for:

Distribution shape

Density

Skewness

Possible multiple modes


------------------------------------------------------------


18. HISTOGRAM

Best for:

Direct binned distribution visualization


------------------------------------------------------------


19. ERROR BARS

Best for representing a specifically defined:

SD

SEM

CI

Measurement uncertainty


They are not equivalent to box plots.


------------------------------------------------------------


20. SAMPLE SIZE

Always consider:

n


A smooth violin generated from a very small dataset may be
misleading.


------------------------------------------------------------


21. FLIERS

Box-plot fliers are:

Statistically unusual observations


not automatically:

Invalid data.


------------------------------------------------------------


22. RAW DATA

For small samples:

Raw Points
    +
Box Plot


can be especially informative.


------------------------------------------------------------


23. DISTRIBUTION COMPARISON

Useful combination:

Box Plot
+
Violin Plot
+
Summary Statistics


------------------------------------------------------------


24. ENGINEERING APPLICATIONS

Useful for:

Repeated experiments

Monte Carlo analysis

Efficiency variation

Power-loss variation

Thermal studies

Component tolerance

ML residuals

Prediction errors

Reliability

Robustness


------------------------------------------------------------


25. MOST IMPORTANT PRINCIPLE

Do not ask only:

"Which box is higher?"


Ask:

What does the median indicate?

How large is the variability?

How wide is the IQR?

Are there unusual observations?

Is the distribution symmetric?

Are there multiple populations?

What is the sample size?

What does this mean physically?


------------------------------------------------------------


26. COMPLETE WORKFLOW

Engineering Measurements
        ↓
Validate Conditions
        ↓
Clean Data
        ↓
Check Sample Size
        ↓
Histogram
        ↓
Box Plot
        ↓
Violin Plot
        ↓
Mean / Median
        ↓
IQR / SD
        ↓
Percentiles
        ↓
Outliers
        ↓
Compare Cases
        ↓
Engineering Interpretation
        ↓
Publication Figure


------------------------------------------------------------


NEXT:

24_heatmaps_and_correlation_maps.py


The next file will cover:

2D matrix visualization

Heatmaps

imshow()

pcolormesh()

Colorbars

Engineering units

Annotated heatmaps

Correlation matrices

Pearson correlation concept

Positive / negative correlation

Selecting numerical DataFrame columns

Masking redundant correlation values

Parameter-vs-operating-condition maps

Load × switching-frequency maps

Temperature maps

Efficiency maps

Frequency × design comparison maps

Custom tick labels

NaN handling

Color-scale limits

Sequential vs diverging color scales

Why inappropriate color scaling can mislead

and publication-quality engineering heatmaps.
"""
