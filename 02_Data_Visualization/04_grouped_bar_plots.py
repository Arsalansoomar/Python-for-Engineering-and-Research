"""
============================================================
Python for Engineering and Research
04 - Grouped Bar Plot
============================================================

Purpose:
    Demonstrate grouped bar plots using Matplotlib for
    comparing multiple datasets across the same discrete
    categories.

Topics:
    1. What is a grouped bar plot?
    2. When should it be used?
    3. Required imports
    4. Basic grouped bar plot
    5. Understanding bar positions
    6. Two groups
    7. Three groups
    8. Multiple engineering cases
    9. Frequency-point comparison
    10. Adding numerical labels
    11. Reference limits
    12. Automatic plotting with loops
    13. Saving figures
    14. Common mistakes
    15. Key takeaways

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT IS A GROUPED BAR PLOT?
# ============================================================

"""
A grouped bar plot compares multiple datasets within
the same category.

Example:

Efficiency [%]

        Case A   Case B   Case C

Load 1     |        |        |

Load 2     |        |        |

Load 3     |        |        |


Unlike a normal bar plot:

One category
    ↓
One value


A grouped bar plot provides:

One category
    ↓
Several values
"""


# ============================================================
# 2. WHEN SHOULD IT BE USED?
# ============================================================

"""
Grouped bar plots are useful when comparing several
methods or cases at the same discrete operating points.

Engineering examples:

- Different converter designs at several load levels
- Multiple EMI cases at selected frequencies
- Simulation vs experiment at several operating points
- Several control methods at different conditions
- Multiple materials at selected frequencies
- THD comparison at several load conditions
- Efficiency comparison across converter designs
- Different algorithms across several datasets
"""


# ============================================================
# 3. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path


# ============================================================
# 4. BASIC DATASET
# ============================================================

"""
Example:

Compare two converter designs at four load conditions.
"""


load_conditions = [
    "25%",
    "50%",
    "75%",
    "100%"
]


design_a = [
    91.5,
    93.2,
    94.1,
    93.8
]


design_b = [
    92.4,
    94.1,
    95.0,
    94.7
]


# ============================================================
# 5. CREATE CATEGORY POSITIONS
# ============================================================

"""
Grouped bar plots require numerical positions for each
category.

np.arange() creates those positions.

For four categories:

x = [0, 1, 2, 3]
"""


x = np.arange(
    len(load_conditions)
)


print(
    "--- Category Positions ---"
)

print(
    x
)


# ============================================================
# 6. DEFINE BAR WIDTH
# ============================================================

"""
The width controls how wide each bar appears.

Because two bars are placed inside each category,
the bars must be shifted slightly to the left and right.
"""


width = 0.35


# ============================================================
# 7. BASIC TWO-GROUP BAR PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.bar(
    x - width / 2,
    design_a,
    width,
    label="Design A"
)


ax.bar(
    x + width / 2,
    design_b,
    width,
    label="Design B"
)


ax.set_xlabel(
    "Load Condition"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Converter Efficiency Comparison"
)


# Replace numerical positions with category names

ax.set_xticks(
    x
)

ax.set_xticklabels(
    load_conditions
)


ax.grid(
    True,
    axis="y"
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 8. WHY ARE THE BARS SHIFTED?
# ============================================================

"""
Suppose the category center is:

x = 1


For Design A:

x - width / 2


For Design B:

x + width / 2


This places one bar slightly to the left and the other
slightly to the right of the category center.

Without these shifts, the bars would overlap.
"""


# ============================================================
# 9. ADD NUMERICAL VALUES
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars_a = ax.bar(
    x - width / 2,
    design_a,
    width,
    label="Design A"
)


bars_b = ax.bar(
    x + width / 2,
    design_b,
    width,
    label="Design B"
)


ax.set_xlabel(
    "Load Condition"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Converter Efficiency Comparison"
)


ax.set_xticks(
    x
)

ax.set_xticklabels(
    load_conditions
)


ax.grid(
    True,
    axis="y"
)

ax.legend()


ax.bar_label(
    bars_a,
    fmt="%.1f",
    padding=3
)


ax.bar_label(
    bars_b,
    fmt="%.1f",
    padding=3
)


plt.tight_layout()

plt.show()


# ============================================================
# 10. THREE-GROUP BAR PLOT
# ============================================================

"""
Now compare three converter designs.

With three datasets, the positions can be:

x - width

x

x + width
"""


baseline = [
    90.0,
    92.0,
    92.8,
    92.5
]


design_a = [
    91.5,
    93.2,
    94.1,
    93.8
]


design_b = [
    92.4,
    94.1,
    95.0,
    94.7
]


width = 0.25


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars_1 = ax.bar(
    x - width,
    baseline,
    width,
    label="Baseline"
)


bars_2 = ax.bar(
    x,
    design_a,
    width,
    label="Design A"
)


bars_3 = ax.bar(
    x + width,
    design_b,
    width,
    label="Design B"
)


ax.set_xlabel(
    "Load Condition"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Efficiency Comparison at Different Loads"
)


ax.set_xticks(
    x
)

ax.set_xticklabels(
    load_conditions
)


ax.set_ylim(
    0,
    105
)


ax.grid(
    True,
    axis="y"
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 11. ENGINEERING EXAMPLE - FREQUENCY COMPARISON
# ============================================================

"""
Grouped bar plots are especially useful for comparing
selected frequency points.

Example:

Compare four configurations at:

100 kHz
1 MHz
10 MHz
20 MHz


The values below are synthetic and provided only
for demonstration.
"""


frequencies = [
    "100 kHz",
    "1 MHz",
    "10 MHz",
    "20 MHz"
]


unshielded = [
    104.5,
    97.2,
    89.8,
    83.5
]


case_a = [
    99.2,
    91.5,
    82.1,
    75.8
]


case_b = [
    96.4,
    88.0,
    77.5,
    71.2
]


case_c = [
    93.5,
    85.3,
    74.8,
    68.5
]


# ============================================================
# 12. FOUR-GROUP POSITIONING
# ============================================================

"""
For four datasets, we create symmetrical offsets
around each category center.
"""


x = np.arange(
    len(frequencies)
)


width = 0.20


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


bars_1 = ax.bar(
    x - 1.5 * width,
    unshielded,
    width,
    label="Unshielded"
)


bars_2 = ax.bar(
    x - 0.5 * width,
    case_a,
    width,
    label="Case A"
)


bars_3 = ax.bar(
    x + 0.5 * width,
    case_b,
    width,
    label="Case B"
)


bars_4 = ax.bar(
    x + 1.5 * width,
    case_c,
    width,
    label="Case C"
)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Frequency-Point Comparison"
)


ax.set_xticks(
    x
)

ax.set_xticklabels(
    frequencies
)


ax.grid(
    True,
    axis="y"
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 13. ADD LABELS TO FOUR GROUPS
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


bars_1 = ax.bar(
    x - 1.5 * width,
    unshielded,
    width,
    label="Unshielded"
)


bars_2 = ax.bar(
    x - 0.5 * width,
    case_a,
    width,
    label="Case A"
)


bars_3 = ax.bar(
    x + 0.5 * width,
    case_b,
    width,
    label="Case B"
)


bars_4 = ax.bar(
    x + 1.5 * width,
    case_c,
    width,
    label="Case C"
)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Frequency-Point Comparison"
)


ax.set_xticks(
    x
)

ax.set_xticklabels(
    frequencies
)


ax.grid(
    True,
    axis="y"
)

ax.legend()


for bars in [
    bars_1,
    bars_2,
    bars_3,
    bars_4
]:

    ax.bar_label(
        bars,
        fmt="%.1f",
        padding=2,
        fontsize=8
    )


plt.tight_layout()

plt.show()


# ============================================================
# 14. REDUCTION RELATIVE TO BASELINE
# ============================================================

"""
Instead of plotting the absolute spectral magnitude,
we can calculate the reduction relative to the baseline.

Because the original quantity is expressed in dBµV,
the direct difference is reported in dB.
"""


reduction_a = []
reduction_b = []
reduction_c = []


for baseline_value, value_a, value_b, value_c in zip(

    unshielded,
    case_a,
    case_b,
    case_c

):

    reduction_a.append(
        baseline_value
        - value_a
    )

    reduction_b.append(
        baseline_value
        - value_b
    )

    reduction_c.append(
        baseline_value
        - value_c
    )


print(
    "\n--- Reduction Relative to Baseline ---"
)

print(
    "Case A:",
    reduction_a
)

print(
    "Case B:",
    reduction_b
)

print(
    "Case C:",
    reduction_c
)


# ============================================================
# 15. GROUPED REDUCTION PLOT
# ============================================================

width = 0.25


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


bars_a = ax.bar(
    x - width,
    reduction_a,
    width,
    label="Case A"
)


bars_b = ax.bar(
    x,
    reduction_b,
    width,
    label="Case B"
)


bars_c = ax.bar(
    x + width,
    reduction_c,
    width,
    label="Case C"
)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Reduction Relative to Baseline [dB]"
)

ax.set_title(
    "Reduction at Selected Frequencies"
)


ax.set_xticks(
    x
)

ax.set_xticklabels(
    frequencies
)


ax.grid(
    True,
    axis="y"
)

ax.legend()


ax.bar_label(
    bars_a,
    fmt="%.1f",
    padding=3
)


ax.bar_label(
    bars_b,
    fmt="%.1f",
    padding=3
)


ax.bar_label(
    bars_c,
    fmt="%.1f",
    padding=3
)


plt.tight_layout()

plt.show()


# ============================================================
# 16. AUTOMATIC GROUPED BAR PLOTTING
# ============================================================

"""
Writing individual ax.bar() commands becomes repetitive
when many datasets are available.

A dictionary and loop can automate the process.
"""


comparison_data = {

    "Unshielded": unshielded,

    "Case A": case_a,

    "Case B": case_b,

    "Case C": case_c

}


# ============================================================
# 17. AUTOMATIC BAR POSITIONING
# ============================================================

"""
General concept:

Number of groups
        ↓
Determine total bar width
        ↓
Calculate offset for each group
        ↓
Plot automatically


This is useful when the number of datasets may change.
"""


number_of_groups = len(
    comparison_data
)


total_group_width = 0.8


bar_width = (
    total_group_width
    / number_of_groups
)


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for group_index, (
    group_name,
    values
) in enumerate(
    comparison_data.items()
):

    offset = (

        group_index
        - (number_of_groups - 1) / 2

    ) * bar_width


    ax.bar(
        x + offset,
        values,
        bar_width,
        label=group_name
    )


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Automatic Grouped Bar Plot"
)


ax.set_xticks(
    x
)

ax.set_xticklabels(
    frequencies
)


ax.grid(
    True,
    axis="y"
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 18. WHY AUTOMATIC POSITIONING IS USEFUL
# ============================================================

"""
Suppose later the dataset contains:

3 cases
5 cases
8 cases

Instead of manually calculating:

x - 1.5 * width
x - 0.5 * width
x + 0.5 * width
x + 1.5 * width

Python calculates the offsets automatically.

This becomes particularly useful when reading data from:

CSV files

Excel files

simulation outputs

experimental datasets
"""


# ============================================================
# 19. ENGINEERING LIMIT LINE
# ============================================================

"""
A grouped bar plot can also include an engineering
specification or threshold.

Example:

Maximum allowed value = 90 dBµV

The value below is only for demonstration.
"""


limit = 90


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for group_index, (
    group_name,
    values
) in enumerate(
    comparison_data.items()
):

    offset = (

        group_index
        - (number_of_groups - 1) / 2

    ) * bar_width


    ax.bar(
        x + offset,
        values,
        bar_width,
        label=group_name
    )


ax.axhline(
    y=limit,
    linestyle="--",
    linewidth=1.5,
    label="Example Limit"
)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Comparison with Example Limit"
)


ax.set_xticks(
    x
)

ax.set_xticklabels(
    frequencies
)


ax.grid(
    True,
    axis="y"
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 20. SIMULATION VS EXPERIMENT
# ============================================================

"""
Grouped bars are also useful for direct comparison between
simulation and experimental results at discrete points.
"""


operating_points = [
    "25% Load",
    "50% Load",
    "75% Load",
    "100% Load"
]


simulation = [
    91.0,
    93.2,
    94.5,
    94.0
]


experiment = [
    90.6,
    92.9,
    94.1,
    93.6
]


x_sim = np.arange(
    len(operating_points)
)


width_sim = 0.35


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars_sim = ax.bar(
    x_sim - width_sim / 2,
    simulation,
    width_sim,
    label="Simulation"
)


bars_exp = ax.bar(
    x_sim + width_sim / 2,
    experiment,
    width_sim,
    label="Experiment"
)


ax.set_xlabel(
    "Operating Condition"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Simulation vs Experimental Results"
)


ax.set_xticks(
    x_sim
)

ax.set_xticklabels(
    operating_points
)


ax.grid(
    True,
    axis="y"
)

ax.legend()


ax.bar_label(
    bars_sim,
    fmt="%.1f",
    padding=3
)


ax.bar_label(
    bars_exp,
    fmt="%.1f",
    padding=3
)


plt.tight_layout()

plt.show()


# ============================================================
# 21. SAVE FINAL FIGURE
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


output_folder = (
    script_folder
    / "output_figures"
)


output_folder.mkdir(
    exist_ok=True
)


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for group_index, (
    group_name,
    values
) in enumerate(
    comparison_data.items()
):

    offset = (

        group_index
        - (number_of_groups - 1) / 2

    ) * bar_width


    bars = ax.bar(
        x + offset,
        values,
        bar_width,
        label=group_name
    )


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Engineering Case Comparison"
)


ax.set_xticks(
    x
)

ax.set_xticklabels(
    frequencies
)


ax.grid(
    True,
    axis="y"
)

ax.legend()


plt.tight_layout()


# ============================================================
# 22. SAVE PNG
# ============================================================

png_file = (
    output_folder
    / "grouped_bar_plot.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 23. SAVE PDF
# ============================================================

pdf_file = (
    output_folder
    / "grouped_bar_plot.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 24. SAVE SVG
# ============================================================

svg_file = (
    output_folder
    / "grouped_bar_plot.svg"
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
# 25. COMMON MISTAKE - BARS OVERLAPPING
# ============================================================

"""
Incorrect:

ax.bar(
    x,
    case_a
)

ax.bar(
    x,
    case_b
)


Both datasets use exactly the same positions.

Therefore the second set of bars may cover the first.


Correct:

ax.bar(
    x - width / 2,
    case_a,
    width
)

ax.bar(
    x + width / 2,
    case_b,
    width
)
"""


# ============================================================
# 26. COMMON MISTAKE - TOO MANY GROUPS
# ============================================================

"""
Grouped bar plots work well when the number of cases is
reasonably small.

For example:

3 categories × 4 cases

can be easy to interpret.


But:

20 categories × 15 cases

may become visually confusing.

Consider alternatives such as:

- Heatmaps
- Separate figures
- Selected representative cases
- Tables
- Line plots
"""


# ============================================================
# 27. COMMON MISTAKE - TOO MANY BAR LABELS
# ============================================================

"""
Numerical labels are useful for small figures.

However, adding values to dozens of bars may make the
figure difficult to read.

Use labels when they improve interpretation.

Do not add labels only because the function exists.
"""


# ============================================================
# 28. COMMON MISTAKE - WRONG CATEGORY ALIGNMENT
# ============================================================

"""
The X tick must represent the CENTER of each category.

Example:

ax.set_xticks(
    x
)

ax.set_xticklabels(
    frequencies
)


Do not place category names according to one individual
bar group instead of the group center.
"""


# ============================================================
# 29. NORMAL BAR VS GROUPED BAR
# ============================================================

"""
NORMAL BAR PLOT

One value per category.

Example:

Case A → 10 W

Case B → 15 W

Case C → 20 W


------------------------------------------------------------


GROUPED BAR PLOT

Several values per category.

Example:

             Simulation    Experiment

25% Load        91.0          90.6

50% Load        93.2          92.9

75% Load        94.5          94.1

100% Load       94.0          93.6
"""


# ============================================================
# 30. GROUPED BAR PLOT PIPELINE
# ============================================================

"""
Define Categories
       ↓
Define Multiple Datasets
       ↓
Create Numerical X Positions
       ↓
Define Bar Width
       ↓
Calculate Group Offsets
       ↓
Plot Each Dataset
       ↓
Set Category Tick Labels
       ↓
Add Legend
       ↓
Add Values if Useful
       ↓
Check Readability
       ↓
Save Figure
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
GROUPED BAR PLOTS


1. CREATE CATEGORY POSITIONS

x = np.arange(
    len(categories)
)


------------------------------------------------------------


2. DEFINE BAR WIDTH

width = 0.35


------------------------------------------------------------


3. TWO GROUPS

ax.bar(
    x - width / 2,
    data_a,
    width,
    label="A"
)


ax.bar(
    x + width / 2,
    data_b,
    width,
    label="B"
)


------------------------------------------------------------


4. SET CATEGORY LABELS

ax.set_xticks(
    x
)

ax.set_xticklabels(
    categories
)


------------------------------------------------------------


5. ADD LEGEND

ax.legend()


------------------------------------------------------------


6. THREE GROUPS

ax.bar(
    x - width,
    data_a,
    width
)

ax.bar(
    x,
    data_b,
    width
)

ax.bar(
    x + width,
    data_c,
    width
)


------------------------------------------------------------


7. MANY GROUPS

Store datasets in a dictionary:

data = {

    "Case A": values_a,

    "Case B": values_b,

    "Case C": values_c

}


Then calculate the position automatically inside a loop.


------------------------------------------------------------


8. COMMON ENGINEERING APPLICATIONS

- Frequency-point comparison
- Simulation vs Experiment
- Efficiency comparison
- Power-loss comparison
- THD comparison
- Different converter designs
- Different control algorithms
- Material comparison
- Experimental operating points


------------------------------------------------------------


9. IMPORTANT PRINCIPLE

A grouped bar plot answers questions such as:

Which method performs best at each operating point?

Does the best method remain consistent across conditions?

How closely does simulation match experiment?

Does a design satisfy the required limit?


------------------------------------------------------------


10. USE ANOTHER PLOT WHEN

The X variable is continuous.

Example:

Frequency from:

10 kHz
to
30 MHz

with thousands of data points.

Use a line plot or logarithmic frequency plot instead.

Grouped bars are better for selected discrete points such as:

100 kHz
1 MHz
10 MHz
20 MHz


------------------------------------------------------------


NEXT:

05_scatter_plot.py

will introduce relationships between two numerical
variables such as:

Temperature vs Efficiency

Load Current vs Power Loss

Parasitic Capacitance vs Magnitude

Measured vs Predicted Values
"""
