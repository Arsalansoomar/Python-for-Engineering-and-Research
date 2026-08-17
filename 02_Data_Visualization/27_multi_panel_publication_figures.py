"""
============================================================
Python for Engineering and Research
27 - Multi-Panel Publication Figures
============================================================

Purpose:
    Demonstrate how multiple related engineering plots can
    be combined into one clear, consistent, publication-
    oriented figure using Matplotlib.

Topics:
    1. What is a multi-panel figure?
    2. 1 × 2 layout
    3. 2 × 1 layout
    4. 2 × 2 layout
    5. Flattening subplot arrays
    6. Shared X axes
    7. Shared Y axes
    8. Common axis limits
    9. Panel labels: (a), (b), (c), (d)
    10. Figure-level titles
    11. Common X and Y labels
    12. Common legends
    13. Removing unused axes
    14. Unequal panel sizes
    15. width_ratios
    16. height_ratios
    17. GridSpec
    18. Spanning rows and columns
    19. subplot_mosaic()
    20. Mixed plot types
    21. Line + bar + heatmap figures
    22. Shared colorbars
    23. Consistent color limits
    24. Time-domain engineering panels
    25. Frequency-domain panels
    26. Performance comparison panels
    27. Parameter-map panels
    28. Publication dimensions
    29. Constrained Layout
    30. Tight layout concept
    31. Reusable panel-label function
    32. Reusable formatting functions
    33. Complete 2 × 2 engineering figure
    34. PNG / PDF / SVG export
    35. Common mistakes
    36. Key takeaways

Sample File:
    sample_data/fft_example.csv

Important:
    A multi-panel figure should combine results that belong
    together scientifically.

    More panels do NOT automatically make a figure better.

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

from matplotlib.gridspec import GridSpec

from matplotlib.ticker import (
    FuncFormatter,
    MultipleLocator,
    LogLocator,
    NullFormatter
)


# ============================================================
# 2. WHAT IS A MULTI-PANEL FIGURE?
# ============================================================

"""
A multi-panel figure contains several related plots inside
one complete figure.

Example:

┌─────────────────┬─────────────────┐
│                 │                 │
│       (a)       │       (b)       │
│   Time Domain   │    FFT Result   │
│                 │                 │
├─────────────────┼─────────────────┤
│                 │                 │
│       (c)       │       (d)       │
│   Comparison    │ Parameter Map   │
│                 │                 │
└─────────────────┴─────────────────┘


The panels should support one scientific story.

For example:

(a) Experimental waveform

(b) Frequency-domain result

(c) Design comparison

(d) Parameter sensitivity
"""


# ============================================================
# 3. WHY MULTI-PANEL FIGURES ARE USEFUL
# ============================================================

"""
Multi-panel figures can:

- Combine related results
- Reduce repeated captions
- Compare operating cases
- Show different physical quantities
- Show full and processed results
- Compare simulation and experiment
- Combine time and frequency domains
- Show several parameter conditions
- Improve paper organization


However:

Too many panels can make a figure difficult to read.
"""


# ============================================================
# 4. PROJECT PATHS
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


sample_data_folder = (
    script_folder
    / "sample_data"
)


output_figure_folder = (
    script_folder
    / "output_figures"
    / "multi_panel"
)


output_figure_folder.mkdir(
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
# 5. CREATE SYNTHETIC TIME-DOMAIN DATA
# ============================================================

"""
Create simple educational converter-like data.

These values are synthetic and are used only to
demonstrate visualization techniques.
"""


time_ms = np.linspace(
    0,
    5,
    1200
)


time_s = (
    time_ms
    / 1000
)


voltage_v = (

    48

    * (
        1
        - np.exp(
            -time_s
            / 0.00055
        )
    )

    + 0.4
    * np.sin(
        2
        * np.pi
        * 20_000
        * time_s
    )

)


current_a = (

    2.4

    * (
        1
        - np.exp(
            -time_s
            / 0.00075
        )
    )

    + 0.08
    * np.sin(
        2
        * np.pi
        * 20_000
        * time_s
    )

)


power_w = (

    voltage_v

    * current_a

)


# ============================================================
# 6. BASIC 1 × 2 LAYOUT
# ============================================================

"""
Syntax:

fig, axes = plt.subplots(
    1,
    2
)


This creates:

1 row

2 columns
"""


fig, axes = plt.subplots(

    1,

    2,

    figsize=(10, 4)

)


axes[0].plot(
    time_ms,
    voltage_v
)


axes[0].set_xlabel(
    "Time [ms]"
)

axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].set_title(
    "Voltage"
)


axes[0].grid(
    True
)


axes[1].plot(
    time_ms,
    current_a
)


axes[1].set_xlabel(
    "Time [ms]"
)

axes[1].set_ylabel(
    "Current [A]"
)

axes[1].set_title(
    "Current"
)


axes[1].grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 7. BASIC 2 × 1 LAYOUT
# ============================================================

"""
2 rows

1 column
"""


fig, axes = plt.subplots(

    2,

    1,

    figsize=(7, 6)

)


axes[0].plot(
    time_ms,
    voltage_v
)


axes[0].set_ylabel(
    "Voltage [V]"
)


axes[0].grid(
    True
)


axes[1].plot(
    time_ms,
    current_a
)


axes[1].set_xlabel(
    "Time [ms]"
)

axes[1].set_ylabel(
    "Current [A]"
)


axes[1].grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 8. SHARE THE X-AXIS
# ============================================================

"""
If panels use the SAME X quantity:

Time [ms]


sharex=True

can synchronize their X-axis limits.
"""


fig, axes = plt.subplots(

    3,

    1,

    figsize=(7, 7),

    sharex=True

)


axes[0].plot(
    time_ms,
    voltage_v
)


axes[0].set_ylabel(
    "Voltage [V]"
)


axes[1].plot(
    time_ms,
    current_a
)


axes[1].set_ylabel(
    "Current [A]"
)


axes[2].plot(
    time_ms,
    power_w
)


axes[2].set_xlabel(
    "Time [ms]"
)

axes[2].set_ylabel(
    "Power [W]"
)


for ax in axes:

    ax.grid(
        True
    )


plt.tight_layout()

plt.show()


# ============================================================
# 9. WHY SHARE AXES?
# ============================================================

"""
Shared axes are useful when:

- Panels represent the same time range
- Several cases use the same frequency range
- Several experiments use the same load range


This improves visual alignment.


Example:

A voltage event at:

2 ms


will appear vertically aligned with:

Current

Power

Temperature

at:

2 ms.
"""


# ============================================================
# 10. SHARE Y-AXIS
# ============================================================

"""
sharey=True

can be useful when panels contain the SAME physical
quantity and should be compared using identical scale.
"""


case_a_voltage = voltage_v


case_b_voltage = (

    voltage_v

    * 0.985

    + 0.25

)


fig, axes = plt.subplots(

    1,

    2,

    figsize=(10, 4),

    sharey=True

)


axes[0].plot(
    time_ms,
    case_a_voltage
)


axes[0].set_title(
    "Case A"
)

axes[0].set_xlabel(
    "Time [ms]"
)

axes[0].set_ylabel(
    "Voltage [V]"
)


axes[1].plot(
    time_ms,
    case_b_voltage
)


axes[1].set_title(
    "Case B"
)

axes[1].set_xlabel(
    "Time [ms]"
)


for ax in axes:

    ax.grid(
        True
    )


plt.tight_layout()

plt.show()


# ============================================================
# 11. BASIC 2 × 2 FIGURE
# ============================================================

fig, axes = plt.subplots(

    2,

    2,

    figsize=(10, 7)

)


axes[0, 0].plot(
    time_ms,
    voltage_v
)


axes[0, 0].set_title(
    "Voltage"
)


axes[0, 1].plot(
    time_ms,
    current_a
)


axes[0, 1].set_title(
    "Current"
)


axes[1, 0].plot(
    time_ms,
    power_w
)


axes[1, 0].set_title(
    "Power"
)


axes[1, 1].plot(
    voltage_v,
    current_a
)


axes[1, 1].set_title(
    "Voltage vs Current"
)


plt.tight_layout()

plt.show()


# ============================================================
# 12. AXES ARRAY
# ============================================================

"""
For:

2 × 2


axes behaves approximately like:

axes[0, 0]

axes[0, 1]

axes[1, 0]

axes[1, 1]


This is useful when each panel requires different content.
"""


# ============================================================
# 13. FLATTEN AXES
# ============================================================

"""
For automatic processing:

axes.flatten()

can convert a 2D axes array into a 1D sequence.
"""


fig, axes = plt.subplots(

    2,

    2,

    figsize=(10, 7)

)


flat_axes = axes.flatten()


signals = [

    voltage_v,

    current_a,

    power_w,

    voltage_v
    - case_b_voltage

]


labels = [

    "Voltage [V]",

    "Current [A]",

    "Power [W]",

    "Voltage Difference [V]"

]


titles = [

    "Voltage",

    "Current",

    "Power",

    "Difference"

]


for ax, signal, y_label, title in zip(

    flat_axes,

    signals,

    labels,

    titles

):

    ax.plot(
        time_ms,
        signal
    )


    ax.set_xlabel(
        "Time [ms]"
    )


    ax.set_ylabel(
        y_label
    )


    ax.set_title(
        title
    )


    ax.grid(
        True
    )


plt.tight_layout()

plt.show()


# ============================================================
# 14. PANEL LABELS
# ============================================================

"""
Publication panels commonly use labels such as:

(a)

(b)

(c)

(d)


These identify panels in:

Figure captions

Paper text

Reviewer comments
"""


panel_labels = [

    "(a)",

    "(b)",

    "(c)",

    "(d)"

]


fig, axes = plt.subplots(

    2,

    2,

    figsize=(10, 7)

)


flat_axes = axes.flatten()


for ax, signal, panel_label in zip(

    flat_axes,

    signals,

    panel_labels

):

    ax.plot(
        time_ms,
        signal
    )


    ax.text(

        0.03,

        0.95,

        panel_label,

        transform=ax.transAxes,

        va="top",

        ha="left",

        fontweight="bold"

    )


    ax.grid(
        True
    )


plt.tight_layout()

plt.show()


# ============================================================
# 15. REUSABLE PANEL-LABEL FUNCTION
# ============================================================

def add_panel_label(
    ax,
    label,
    x=0.02,
    y=0.97,
    fontsize=10
):
    """
    Add a publication-style panel label.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axis.

    label : str
        Example:
        "(a)"

    x, y : float
        Position in axis coordinates.

    fontsize : float
        Label font size.
    """

    ax.text(

        x,

        y,

        label,

        transform=ax.transAxes,

        ha="left",

        va="top",

        fontsize=fontsize,

        fontweight="bold"

    )


# ============================================================
# 16. USE PANEL-LABEL FUNCTION
# ============================================================

fig, axes = plt.subplots(

    2,

    2,

    figsize=(10, 7)

)


for ax, signal, label in zip(

    axes.flatten(),

    signals,

    panel_labels

):

    ax.plot(
        time_ms,
        signal
    )


    add_panel_label(

        ax,

        label

    )


    ax.grid(
        True
    )


plt.tight_layout()

plt.show()


# ============================================================
# 17. COMMON X LABEL
# ============================================================

"""
When all panels share one X quantity:

Time [ms]


repeating the same label four times may be unnecessary.

A figure-level X label can be used.
"""


fig, axes = plt.subplots(

    2,

    2,

    figsize=(10, 7),

    sharex=True

)


for ax, signal in zip(

    axes.flatten(),

    signals

):

    ax.plot(
        time_ms,
        signal
    )


    ax.grid(
        True
    )


fig.supxlabel(
    "Time [ms]"
)


plt.show()


# ============================================================
# 18. COMMON Y LABEL
# ============================================================

"""
A figure-level Y label is useful when every panel represents
the same quantity and unit.
"""


fig, axes = plt.subplots(

    2,

    2,

    figsize=(10, 7),

    sharex=True,

    sharey=True

)


for index, ax in enumerate(
    axes.flatten()
):

    ax.plot(

        time_ms,

        voltage_v
        + index
        * 0.3

    )


    ax.grid(
        True
    )


fig.supxlabel(
    "Time [ms]"
)


fig.supylabel(
    "Voltage [V]"
)


plt.show()


# ============================================================
# 19. FIGURE-LEVEL TITLE
# ============================================================

"""
Use:

fig.suptitle()


for a title covering the complete multi-panel figure.


For journal papers:

An internal figure title may often be unnecessary because
the caption already describes the complete figure.
"""


fig, axes = plt.subplots(

    1,

    2,

    figsize=(9, 4)

)


axes[0].plot(
    time_ms,
    voltage_v
)


axes[1].plot(
    time_ms,
    current_a
)


fig.suptitle(
    "Converter Time-Domain Performance"
)


plt.tight_layout()

plt.show()


# ============================================================
# 20. COMMON LEGEND
# ============================================================

"""
If several panels contain the same case definitions:

Baseline

Design A

Design B


a single figure-level legend may reduce repetition.
"""


design_a = voltage_v

design_b = voltage_v * 0.99 + 0.3

design_c = voltage_v * 1.005 - 0.15


comparison_cases = {

    "Baseline":
        design_a,

    "Design B":
        design_b,

    "Design C":
        design_c

}


fig, axes = plt.subplots(

    2,

    1,

    figsize=(8, 6),

    sharex=True,

    layout="constrained"

)


for case_name, values in comparison_cases.items():

    axes[0].plot(

        time_ms,

        values,

        label=case_name

    )


    axes[1].plot(

        time_ms,

        values
        - voltage_v,

        label=case_name

    )


axes[0].set_ylabel(
    "Voltage [V]"
)


axes[1].set_ylabel(
    "Difference [V]"
)


axes[1].set_xlabel(
    "Time [ms]"
)


for ax in axes:

    ax.grid(
        True
    )


handles, legend_labels = (
    axes[0].get_legend_handles_labels()
)


fig.legend(

    handles,

    legend_labels,

    loc="outside upper center",

    ncols=3

)


plt.show()


# ============================================================
# 21. COMMON LEGEND PRINCIPLE
# ============================================================

"""
If every panel repeats the same legend:

Case A
Case B
Case C


the figure may become visually crowded.


A common legend can save space.


However:

If different panels contain different datasets, individual
legends may still be clearer.
"""


# ============================================================
# 22. REMOVE UNUSED AXES
# ============================================================

"""
Suppose:

5 datasets

are arranged in:

2 × 3


This creates:

6 axes


The unused sixth axis should normally be removed.
"""


fig, axes = plt.subplots(

    2,

    3,

    figsize=(11, 6)

)


flat_axes = axes.flatten()


five_signals = [

    voltage_v,

    current_a,

    power_w,

    voltage_v
    - case_b_voltage,

    current_a ** 2

]


for ax, signal in zip(

    flat_axes,

    five_signals

):

    ax.plot(
        time_ms,
        signal
    )


    ax.grid(
        True
    )


# Remove unused axes

for ax in flat_axes[
    len(
        five_signals
    ):
]:

    fig.delaxes(
        ax
    )


plt.tight_layout()

plt.show()


# ============================================================
# 23. AUTOMATIC PANEL LABELS
# ============================================================

"""
Panel labels can be generated automatically.
"""


def generate_panel_labels(
    number_of_panels
):
    """
    Generate:

    (a), (b), (c), ...

    for up to 26 panels.
    """

    if number_of_panels < 1:

        raise ValueError(
            "number_of_panels must be positive."
        )


    if number_of_panels > 26:

        raise ValueError(
            "This simple function supports "
            "up to 26 panels."
        )


    return [

        f"({chr(97 + index)})"

        for index in range(
            number_of_panels
        )

    ]


print(
    "\n--- Automatic Panel Labels ---"
)


print(
    generate_panel_labels(
        6
    )
)


# ============================================================
# 24. UNEQUAL PANEL WIDTHS
# ============================================================

"""
Not every panel needs equal width.

Example:

Main waveform:
Large panel


Summary bar chart:
Smaller panel
"""


fig, axes = plt.subplots(

    1,

    2,

    figsize=(10, 4),

    width_ratios=[
        2,
        1
    ]

)


axes[0].plot(
    time_ms,
    voltage_v
)


axes[0].set_xlabel(
    "Time [ms]"
)

axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].set_title(
    "Main Waveform"
)


summary_values = [

    voltage_v.mean(),

    voltage_v.max(),

    voltage_v.min()

]


axes[1].bar(

    [
        "Mean",
        "Max",
        "Min"
    ],

    summary_values

)


axes[1].set_ylabel(
    "Voltage [V]"
)

axes[1].set_title(
    "Summary"
)


plt.tight_layout()

plt.show()


# ============================================================
# 25. UNEQUAL PANEL HEIGHTS
# ============================================================

fig, axes = plt.subplots(

    2,

    1,

    figsize=(8, 6),

    height_ratios=[
        2,
        1
    ],

    sharex=True

)


axes[0].plot(
    time_ms,
    voltage_v
)


axes[0].set_ylabel(
    "Voltage [V]"
)


axes[1].plot(
    time_ms,
    voltage_v
    - case_b_voltage
)


axes[1].set_ylabel(
    "Difference [V]"
)


axes[1].set_xlabel(
    "Time [ms]"
)


for ax in axes:

    ax.grid(
        True
    )


plt.tight_layout()

plt.show()


# ============================================================
# 26. WHAT IS GridSpec?
# ============================================================

"""
GridSpec provides more flexible control over the placement
and size of axes.

Example:

┌─────────────────────────────┐
│                             │
│           Panel A           │
│                             │
├──────────────┬──────────────┤
│              │              │
│   Panel B    │   Panel C    │
│              │              │
└──────────────┴──────────────┘


Panel A spans both columns.
"""


# ============================================================
# 27. BASIC GridSpec
# ============================================================

fig = plt.figure(
    figsize=(9, 6)
)


grid = GridSpec(

    2,

    2,

    figure=fig

)


ax_a = fig.add_subplot(
    grid[
        0,
        :
    ]
)


ax_b = fig.add_subplot(
    grid[
        1,
        0
    ]
)


ax_c = fig.add_subplot(
    grid[
        1,
        1
    ]
)


ax_a.plot(
    time_ms,
    voltage_v
)


ax_b.plot(
    time_ms,
    current_a
)


ax_c.plot(
    time_ms,
    power_w
)


ax_a.set_title(
    "Voltage"
)


ax_b.set_title(
    "Current"
)


ax_c.set_title(
    "Power"
)


plt.tight_layout()

plt.show()


# ============================================================
# 28. GRID SPANNING MULTIPLE ROWS
# ============================================================

"""
GridSpec axes can span:

Multiple columns

Multiple rows
"""


fig = plt.figure(
    figsize=(10, 6)
)


grid = GridSpec(

    2,

    3,

    figure=fig

)


large_axis = fig.add_subplot(
    grid[
        :,
        :2
    ]
)


top_right = fig.add_subplot(
    grid[
        0,
        2
    ]
)


bottom_right = fig.add_subplot(
    grid[
        1,
        2
    ]
)


large_axis.plot(
    time_ms,
    voltage_v
)


large_axis.set_xlabel(
    "Time [ms]"
)

large_axis.set_ylabel(
    "Voltage [V]"
)


top_right.plot(
    time_ms,
    current_a
)


top_right.set_title(
    "Current"
)


bottom_right.plot(
    time_ms,
    power_w
)


bottom_right.set_title(
    "Power"
)


plt.tight_layout()

plt.show()


# ============================================================
# 29. GridSpec WIDTH RATIOS
# ============================================================

fig = plt.figure(
    figsize=(10, 5)
)


grid = GridSpec(

    1,

    2,

    figure=fig,

    width_ratios=[
        3,
        1
    ]

)


main_axis = fig.add_subplot(
    grid[
        0,
        0
    ]
)


side_axis = fig.add_subplot(
    grid[
        0,
        1
    ]
)


main_axis.plot(
    time_ms,
    voltage_v
)


main_axis.set_xlabel(
    "Time [ms]"
)

main_axis.set_ylabel(
    "Voltage [V]"
)


side_axis.bar(

    [
        "Mean",
        "Peak"
    ],

    [
        voltage_v.mean(),
        voltage_v.max()
    ]

)


side_axis.set_ylabel(
    "Voltage [V]"
)


plt.tight_layout()

plt.show()


# ============================================================
# 30. subplot_mosaic()
# ============================================================

"""
subplot_mosaic() allows a layout to be described using
meaningful labels.

Example:

A A B

C D B
"""


mosaic_layout = [

    [
        "waveform",
        "waveform",
        "summary"
    ],

    [
        "current",
        "power",
        "summary"
    ]

]


fig, axes = plt.subplot_mosaic(

    mosaic_layout,

    figsize=(10, 6),

    layout="constrained"

)


axes[
    "waveform"
].plot(
    time_ms,
    voltage_v
)


axes[
    "waveform"
].set_title(
    "Voltage"
)


axes[
    "current"
].plot(
    time_ms,
    current_a
)


axes[
    "current"
].set_title(
    "Current"
)


axes[
    "power"
].plot(
    time_ms,
    power_w
)


axes[
    "power"
].set_title(
    "Power"
)


axes[
    "summary"
].bar(

    [
        "Mean",
        "Max",
        "Min"
    ],

    [
        voltage_v.mean(),
        voltage_v.max(),
        voltage_v.min()
    ]

)


axes[
    "summary"
].set_title(
    "Voltage Summary"
)


plt.show()


# ============================================================
# 31. WHY subplot_mosaic() CAN HELP
# ============================================================

"""
Compare:

axes[0, 1]


with:

axes["frequency"]


Semantic names can make complex plotting scripts easier to
read.

This becomes useful when figures contain:

Time-domain panel

FFT panel

Heatmap panel

Summary panel
"""


# ============================================================
# 32. COMMON AXIS LIMITS FOR FAIR COMPARISON
# ============================================================

"""
If:

Panel A

and

Panel B


show the same quantity for different cases,

different automatic Y limits can make one case appear more
variable than another.


Use shared axes or explicit common limits where scientific
comparison requires them.
"""


common_y_min = min(

    case_a_voltage.min(),

    case_b_voltage.min()

)


common_y_max = max(

    case_a_voltage.max(),

    case_b_voltage.max()

)


fig, axes = plt.subplots(

    1,

    2,

    figsize=(10, 4)

)


axes[0].plot(
    time_ms,
    case_a_voltage
)


axes[1].plot(
    time_ms,
    case_b_voltage
)


for ax in axes:

    ax.set_ylim(
        common_y_min,
        common_y_max
    )


    ax.set_xlabel(
        "Time [ms]"
    )


    ax.set_ylabel(
        "Voltage [V]"
    )


    ax.grid(
        True
    )


axes[0].set_title(
    "Case A"
)


axes[1].set_title(
    "Case B"
)


plt.tight_layout()

plt.show()


# ============================================================
# 33. PERFORMANCE DATA
# ============================================================

load_percent = np.array(
    [
        20,
        40,
        60,
        80,
        100
    ]
)


baseline_efficiency = np.array(
    [
        90.8,
        93.0,
        94.2,
        94.5,
        94.1
    ]
)


design_a_efficiency = np.array(
    [
        91.7,
        94.0,
        95.0,
        95.4,
        95.0
    ]
)


design_b_efficiency = np.array(
    [
        92.1,
        94.4,
        95.4,
        95.8,
        95.5
    ]
)


# ============================================================
# 34. MIX LINE AND BAR PANELS
# ============================================================

fig, axes = plt.subplots(

    1,

    2,

    figsize=(10, 4.3)

)


# ------------------------------------------------------------
# Panel A: efficiency curves
# ------------------------------------------------------------

axes[0].plot(

    load_percent,

    baseline_efficiency,

    marker="o",

    label="Baseline"

)


axes[0].plot(

    load_percent,

    design_a_efficiency,

    marker="s",

    linestyle="--",

    label="Design A"

)


axes[0].plot(

    load_percent,

    design_b_efficiency,

    marker="^",

    linestyle="-.",

    label="Design B"

)


axes[0].set_xlabel(
    "Load [%]"
)


axes[0].set_ylabel(
    "Efficiency [%]"
)


axes[0].legend()


axes[0].grid(
    True
)


# ------------------------------------------------------------
# Panel B: full-load comparison
# ------------------------------------------------------------

full_load_efficiency = [

    baseline_efficiency[-1],

    design_a_efficiency[-1],

    design_b_efficiency[-1]

]


bars = axes[1].bar(

    [
        "Baseline",
        "Design A",
        "Design B"
    ],

    full_load_efficiency

)


axes[1].bar_label(
    bars,
    fmt="%.1f",
    padding=3
)


axes[1].set_ylabel(
    "Efficiency [%]"
)


axes[1].set_title(
    "100% Load"
)


axes[1].grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 35. PARAMETER-MAP DATA
# ============================================================

frequency_khz = np.linspace(
    50,
    250,
    25
)


parameter_load = np.linspace(
    20,
    100,
    21
)


frequency_grid, load_grid = np.meshgrid(

    frequency_khz,

    parameter_load

)


efficiency_map_a = (

    96.0

    - 0.000055
    * (
        frequency_grid
        - 130
    ) ** 2

    - 0.00040
    * (
        load_grid
        - 75
    ) ** 2

)


efficiency_map_b = (

    96.4

    - 0.000050
    * (
        frequency_grid
        - 140
    ) ** 2

    - 0.00036
    * (
        load_grid
        - 78
    ) ** 2

)


# ============================================================
# 36. MULTIPLE HEATMAP PANELS
# ============================================================

"""
When heatmaps are directly compared:

Use the same:

vmin

vmax

and colormap.
"""


shared_map_min = min(

    efficiency_map_a.min(),

    efficiency_map_b.min()

)


shared_map_max = max(

    efficiency_map_a.max(),

    efficiency_map_b.max()

)


fig, axes = plt.subplots(

    1,

    2,

    figsize=(10, 4),

    layout="constrained"

)


image_a = axes[0].imshow(

    efficiency_map_a,

    origin="lower",

    aspect="auto",

    extent=[
        frequency_khz.min(),
        frequency_khz.max(),
        parameter_load.min(),
        parameter_load.max()
    ],

    vmin=shared_map_min,

    vmax=shared_map_max,

    cmap="viridis"

)


image_b = axes[1].imshow(

    efficiency_map_b,

    origin="lower",

    aspect="auto",

    extent=[
        frequency_khz.min(),
        frequency_khz.max(),
        parameter_load.min(),
        parameter_load.max()
    ],

    vmin=shared_map_min,

    vmax=shared_map_max,

    cmap="viridis"

)


axes[0].set_title(
    "Design A"
)


axes[1].set_title(
    "Design B"
)


for ax in axes:

    ax.set_xlabel(
        "Switching Frequency [kHz]"
    )


    ax.set_ylabel(
        "Load [%]"
    )


# One common colorbar

colorbar = fig.colorbar(

    image_b,

    ax=axes,

    location="right"

)


colorbar.set_label(
    "Efficiency [%]"
)


plt.show()


# ============================================================
# 37. WHY USE ONE COMMON COLORBAR?
# ============================================================

"""
If two panels show the same physical response:

Efficiency [%]


using one shared colorbar can emphasize that both panels
use the same numerical color scale.


This can improve direct visual comparison.
"""


# ============================================================
# 38. DIFFERENCE MAP PANEL
# ============================================================

difference_map = (

    efficiency_map_b

    - efficiency_map_a

)


maximum_abs_difference = np.max(

    np.abs(
        difference_map
    )

)


fig, axes = plt.subplots(

    1,

    3,

    figsize=(13, 4),

    layout="constrained"

)


image_a = axes[0].imshow(

    efficiency_map_a,

    origin="lower",

    aspect="auto",

    extent=[
        frequency_khz.min(),
        frequency_khz.max(),
        parameter_load.min(),
        parameter_load.max()
    ],

    cmap="viridis",

    vmin=shared_map_min,

    vmax=shared_map_max

)


image_b = axes[1].imshow(

    efficiency_map_b,

    origin="lower",

    aspect="auto",

    extent=[
        frequency_khz.min(),
        frequency_khz.max(),
        parameter_load.min(),
        parameter_load.max()
    ],

    cmap="viridis",

    vmin=shared_map_min,

    vmax=shared_map_max

)


difference_image = axes[2].imshow(

    difference_map,

    origin="lower",

    aspect="auto",

    extent=[
        frequency_khz.min(),
        frequency_khz.max(),
        parameter_load.min(),
        parameter_load.max()
    ],

    cmap="coolwarm",

    vmin=-maximum_abs_difference,

    vmax=maximum_abs_difference

)


axes[0].set_title(
    "Design A"
)


axes[1].set_title(
    "Design B"
)


axes[2].set_title(
    "B - A"
)


for ax in axes:

    ax.set_xlabel(
        "Switching Frequency [kHz]"
    )


    ax.set_ylabel(
        "Load [%]"
    )


performance_colorbar = fig.colorbar(

    image_b,

    ax=[
        axes[0],
        axes[1]
    ],

    location="bottom",

    shrink=0.75

)


performance_colorbar.set_label(
    "Efficiency [%]"
)


difference_colorbar = fig.colorbar(

    difference_image,

    ax=axes[2],

    location="bottom",

    shrink=0.75

)


difference_colorbar.set_label(
    "Difference [percentage points]"
)


plt.show()


# ============================================================
# 39. LOAD FFT DATA
# ============================================================

fft_file = (
    sample_data_folder
    / "fft_example.csv"
)


if fft_file.exists():

    fft_data = pd.read_csv(
        fft_file
    )


    required_fft_columns = [

        "Frequency_Hz",

        "Unshielded_dBuV",

        "Case_A_dBuV",

        "Case_B_dBuV",

        "Case_C_dBuV"

    ]


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


else:

    # --------------------------------------------------------
    # Synthetic fallback data
    # --------------------------------------------------------

    print(
        "\nFFT sample file not found."
    )


    print(
        "Using synthetic frequency-domain data."
    )


    synthetic_frequency = np.logspace(

        4,

        np.log10(
            30e6
        ),

        500

    )


    log_frequency = np.log10(
        synthetic_frequency
    )


    synthetic_unshielded = (

        105

        - 8
        * (
            log_frequency
            - 4
        )

        + 7
        * np.sin(
            5
            * log_frequency
        )

    )


    synthetic_case_a = (

        synthetic_unshielded

        - 4

        - 2
        * np.sin(
            2
            * log_frequency
        )

    )


    synthetic_case_b = (

        synthetic_unshielded

        - 8

        - 3
        * np.cos(
            2.5
            * log_frequency
        )

    )


    synthetic_case_c = (

        synthetic_unshielded

        - 5

        + 2
        * np.sin(
            3
            * log_frequency
        )

    )


    fft_data = pd.DataFrame(
        {
            "Frequency_Hz":
                synthetic_frequency,

            "Unshielded_dBuV":
                synthetic_unshielded,

            "Case_A_dBuV":
                synthetic_case_a,

            "Case_B_dBuV":
                synthetic_case_b,

            "Case_C_dBuV":
                synthetic_case_c
        }
    )


# ============================================================
# 40. FFT CASES
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


fft_line_styles = {

    "Unshielded":
        "-",

    "Case A":
        "--",

    "Case B":
        "-.",

    "Case C":
        ":"

}


# ============================================================
# 41. FREQUENCY FORMATTER
# ============================================================

def format_frequency(
    value,
    position=None
):
    """
    Format frequency using engineering notation.
    """

    if value >= 1e9:

        return (
            f"{value / 1e9:g} GHz"
        )


    if value >= 1e6:

        return (
            f"{value / 1e6:g} MHz"
        )


    if value >= 1e3:

        return (
            f"{value / 1e3:g} kHz"
        )


    return (
        f"{value:g} Hz"
    )


# ============================================================
# 42. FREQUENCY PANEL
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.5)
)


for case_name, column_name in fft_cases.items():

    ax.plot(

        fft_data[
            "Frequency_Hz"
        ],

        fft_data[
            column_name
        ],

        linestyle=fft_line_styles[
            case_name
        ],

        label=case_name

    )


ax.set_xscale(
    "log"
)


ax.set_xlim(
    fft_data[
        "Frequency_Hz"
    ].min(),

    fft_data[
        "Frequency_Hz"
    ].max()
)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.xaxis.set_major_formatter(
    FuncFormatter(
        format_frequency
    )
)


ax.legend()


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 43. PUBLICATION DIMENSIONS
# ============================================================

"""
Matplotlib figsize uses inches.

A helper function makes it easier to work with dimensions
given in millimeters.
"""


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


# ============================================================
# 44. EXAMPLE DOUBLE-COLUMN WIDTH
# ============================================================

"""
The following width is an educational example.

Exact journal dimensions vary.

Always check the actual publisher instructions.
"""


publication_width_mm = 178


publication_width_in = mm_to_inches(
    publication_width_mm
)


publication_height_in = (

    publication_width_in

    * 0.78

)


print(
    "\n--- Example Publication Size ---"
)


print(
    f"Width = "
    f"{publication_width_in:.3f} in"
)


print(
    f"Height = "
    f"{publication_height_in:.3f} in"
)


# ============================================================
# 45. PUBLICATION STYLE
# ============================================================

publication_style = {

    "font.size":
        8,

    "axes.labelsize":
        9,

    "axes.titlesize":
        9,

    "axes.linewidth":
        0.8,

    "xtick.labelsize":
        8,

    "ytick.labelsize":
        8,

    "xtick.direction":
        "in",

    "ytick.direction":
        "in",

    "xtick.top":
        True,

    "ytick.right":
        True,

    "legend.fontsize":
        8,

    "lines.linewidth":
        1.3,

    "lines.markersize":
        4

}


# ============================================================
# 46. PANEL-FORMATTING FUNCTION
# ============================================================

def format_panel(
    ax,
    panel_label=None,
    grid=True
):
    """
    Apply basic publication-oriented formatting.
    """

    ax.tick_params(

        axis="both",

        which="both",

        direction="in",

        top=True,

        right=True

    )


    if grid:

        ax.grid(

            True,

            which="major",

            linewidth=0.45,

            alpha=0.35

        )


    if panel_label is not None:

        add_panel_label(

            ax,

            panel_label,

            x=0.02,

            y=0.97,

            fontsize=9

        )


# ============================================================
# 47. COMPLETE 2 × 2 ENGINEERING FIGURE
# ============================================================

"""
Final example:

(a)
Time-domain voltage


(b)
Frequency-domain comparison


(c)
Efficiency comparison


(d)
Parameter map


This is representative of the type of composite figure
commonly needed in engineering research.
"""


with mpl.rc_context(
    publication_style
):

    fig, axes = plt.subplots(

        2,

        2,

        figsize=(
            publication_width_in,
            publication_height_in
        ),

        layout="constrained"

    )


    # ========================================================
    # PANEL (a) - TIME-DOMAIN SIGNAL
    # ========================================================

    ax_a = axes[
        0,
        0
    ]


    ax_a.plot(

        time_ms,

        voltage_v,

        label="Output Voltage"

    )


    ax_a.set_xlabel(
        "Time [ms]"
    )


    ax_a.set_ylabel(
        "Voltage [V]"
    )


    format_panel(

        ax_a,

        "(a)"

    )


    # ========================================================
    # PANEL (b) - FFT COMPARISON
    # ========================================================

    ax_b = axes[
        0,
        1
    ]


    for (
        case_name,
        column_name
    ) in fft_cases.items():

        ax_b.plot(

            fft_data[
                "Frequency_Hz"
            ],

            fft_data[
                column_name
            ],

            linestyle=fft_line_styles[
                case_name
            ],

            label=case_name

        )


    ax_b.set_xscale(
        "log"
    )


    ax_b.set_xlabel(
        "Frequency"
    )


    ax_b.set_ylabel(
        "Magnitude [dBµV]"
    )


    ax_b.xaxis.set_major_formatter(
        FuncFormatter(
            format_frequency
        )
    )


    ax_b.xaxis.set_minor_locator(
        LogLocator(
            base=10,

            subs=np.arange(
                2,
                10
            )
            * 0.1
        )
    )


    ax_b.xaxis.set_minor_formatter(
        NullFormatter()
    )


    ax_b.legend(
        ncols=2
    )


    format_panel(

        ax_b,

        "(b)"

    )


    # ========================================================
    # PANEL (c) - EFFICIENCY COMPARISON
    # ========================================================

    ax_c = axes[
        1,
        0
    ]


    ax_c.plot(

        load_percent,

        baseline_efficiency,

        marker="o",

        linestyle="-",

        label="Baseline"

    )


    ax_c.plot(

        load_percent,

        design_a_efficiency,

        marker="s",

        linestyle="--",

        label="Design A"

    )


    ax_c.plot(

        load_percent,

        design_b_efficiency,

        marker="^",

        linestyle="-.",

        label="Design B"

    )


    ax_c.set_xlabel(
        "Load [%]"
    )


    ax_c.set_ylabel(
        "Efficiency [%]"
    )


    ax_c.xaxis.set_major_locator(
        MultipleLocator(
            20
        )
    )


    ax_c.legend(
        ncols=1
    )


    format_panel(

        ax_c,

        "(c)"

    )


    # ========================================================
    # PANEL (d) - PARAMETER MAP
    # ========================================================

    ax_d = axes[
        1,
        1
    ]


    parameter_image = ax_d.pcolormesh(

        frequency_grid,

        load_grid,

        efficiency_map_b,

        shading="auto",

        cmap="viridis"

    )


    ax_d.set_xlabel(
        "Switching Frequency [kHz]"
    )


    ax_d.set_ylabel(
        "Load [%]"
    )


    format_panel(

        ax_d,

        "(d)",

        grid=False

    )


    # ========================================================
    # COLORBAR FOR PANEL (d)
    # ========================================================

    colorbar = fig.colorbar(

        parameter_image,

        ax=ax_d

    )


    colorbar.set_label(
        "Efficiency [%]"
    )


    # ========================================================
    # SAVE FIGURE
    # ========================================================

    final_png = (
        output_figure_folder
        / "multi_panel_engineering_figure.png"
    )


    final_pdf = (
        output_figure_folder
        / "multi_panel_engineering_figure.pdf"
    )


    final_svg = (
        output_figure_folder
        / "multi_panel_engineering_figure.svg"
    )


    fig.savefig(

        final_png,

        dpi=300

    )


    fig.savefig(
        final_pdf
    )


    fig.savefig(
        final_svg
    )


    print(
        "\n--- Final Multi-Panel Files ---"
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
# 48. COMPLETE GridSpec PUBLICATION EXAMPLE
# ============================================================

"""
Sometimes:

Time-domain result

deserves more visual space than:

Summary metrics.


GridSpec makes such layouts possible.
"""


with mpl.rc_context(
    publication_style
):

    fig = plt.figure(

        figsize=(
            publication_width_in,
            publication_height_in
        ),

        layout="constrained"

    )


    grid = fig.add_gridspec(

        2,

        3,

        width_ratios=[
            1.3,
            1.3,
            1
        ],

        height_ratios=[
            1,
            1
        ]

    )


    # --------------------------------------------------------
    # Large left panel
    # --------------------------------------------------------

    ax_main = fig.add_subplot(

        grid[
            :,
            :2
        ]

    )


    ax_main.plot(

        time_ms,

        voltage_v,

        label="Voltage"

    )


    ax_main.set_xlabel(
        "Time [ms]"
    )


    ax_main.set_ylabel(
        "Voltage [V]"
    )


    format_panel(

        ax_main,

        "(a)"

    )


    # --------------------------------------------------------
    # Upper-right panel
    # --------------------------------------------------------

    ax_top_right = fig.add_subplot(

        grid[
            0,
            2
        ]

    )


    ax_top_right.plot(

        load_percent,

        design_b_efficiency,

        marker="o"

    )


    ax_top_right.set_xlabel(
        "Load [%]"
    )


    ax_top_right.set_ylabel(
        "Efficiency [%]"
    )


    format_panel(

        ax_top_right,

        "(b)"

    )


    # --------------------------------------------------------
    # Lower-right panel
    # --------------------------------------------------------

    ax_bottom_right = fig.add_subplot(

        grid[
            1,
            2
        ]

    )


    bars = ax_bottom_right.bar(

        [
            "Base",
            "A",
            "B"
        ],

        [
            baseline_efficiency[-1],
            design_a_efficiency[-1],
            design_b_efficiency[-1]
        ]

    )


    ax_bottom_right.bar_label(

        bars,

        fmt="%.1f",

        fontsize=7

    )


    ax_bottom_right.set_ylabel(
        "Efficiency [%]"
    )


    format_panel(

        ax_bottom_right,

        "(c)"

    )


    plt.show()


# ============================================================
# 49. COMPLEX MOSAIC EXAMPLE
# ============================================================

"""
A semantic mosaic can represent:

FFT FFT SUMMARY

TIME MAP SUMMARY
"""


mosaic = [

    [
        "fft",
        "fft",
        "summary"
    ],

    [
        "time",
        "map",
        "summary"
    ]

]


with mpl.rc_context(
    publication_style
):

    fig, axes = plt.subplot_mosaic(

        mosaic,

        figsize=(
            publication_width_in,
            publication_height_in
        ),

        layout="constrained"

    )


    # --------------------------------------------------------
    # FFT
    # --------------------------------------------------------

    for (
        case_name,
        column_name
    ) in fft_cases.items():

        axes[
            "fft"
        ].plot(

            fft_data[
                "Frequency_Hz"
            ],

            fft_data[
                column_name
            ],

            linestyle=fft_line_styles[
                case_name
            ],

            label=case_name

        )


    axes[
        "fft"
    ].set_xscale(
        "log"
    )


    axes[
        "fft"
    ].set_xlabel(
        "Frequency [Hz]"
    )


    axes[
        "fft"
    ].set_ylabel(
        "Magnitude [dBµV]"
    )


    axes[
        "fft"
    ].legend(
        ncols=2
    )


    add_panel_label(

        axes[
            "fft"
        ],

        "(a)"

    )


    # --------------------------------------------------------
    # Time
    # --------------------------------------------------------

    axes[
        "time"
    ].plot(
        time_ms,
        voltage_v
    )


    axes[
        "time"
    ].set_xlabel(
        "Time [ms]"
    )


    axes[
        "time"
    ].set_ylabel(
        "Voltage [V]"
    )


    add_panel_label(

        axes[
            "time"
        ],

        "(b)"

    )


    # --------------------------------------------------------
    # Parameter map
    # --------------------------------------------------------

    map_image = axes[
        "map"
    ].pcolormesh(

        frequency_grid,

        load_grid,

        efficiency_map_b,

        shading="auto",

        cmap="viridis"

    )


    axes[
        "map"
    ].set_xlabel(
        "Frequency [kHz]"
    )


    axes[
        "map"
    ].set_ylabel(
        "Load [%]"
    )


    add_panel_label(

        axes[
            "map"
        ],

        "(c)"

    )


    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    summary_bars = axes[
        "summary"
    ].bar(

        [
            "Base",
            "A",
            "B"
        ],

        [
            baseline_efficiency[-1],
            design_a_efficiency[-1],
            design_b_efficiency[-1]
        ]

    )


    axes[
        "summary"
    ].bar_label(

        summary_bars,

        fmt="%.1f",

        fontsize=7

    )


    axes[
        "summary"
    ].set_ylabel(
        "Efficiency [%]"
    )


    add_panel_label(

        axes[
            "summary"
        ],

        "(d)"

    )


    colorbar = fig.colorbar(

        map_image,

        ax=axes[
            "map"
        ]

    )


    colorbar.set_label(
        "Efficiency [%]"
    )


    plt.show()


# ============================================================
# 50. CONSTRAINED LAYOUT
# ============================================================

"""
For complex figures containing:

Axis labels

Panel labels

Legends

Colorbars

Multiple rows and columns


automatic layout management can greatly reduce manual
spacing work.


Example:

layout="constrained"
"""


# ============================================================
# 51. TIGHT LAYOUT
# ============================================================

"""
Another common approach is:

plt.tight_layout()


It can still be useful for many simple figures.


However:

Do not combine several competing layout approaches
without understanding their interaction.


For new complex figures, choose one clear layout strategy.
"""


# ============================================================
# 52. DO NOT APPLY tight_layout() AFTER CONSTRAINED LAYOUT
# ============================================================

"""
Example workflow:

fig, axes = plt.subplots(
    ...,
    layout="constrained"
)


Then simply:

fig.savefig(...)


Do not automatically add:

plt.tight_layout()


afterward.


Use one deliberate layout engine for the final figure.
"""


# ============================================================
# 53. CONSISTENT TYPOGRAPHY
# ============================================================

"""
All panels should normally use consistent:

Font family

Axis-label size

Tick-label size

Legend size

Panel-label size


A multi-panel figure can look unprofessional if every
panel uses unrelated typography.
"""


# ============================================================
# 54. CONSISTENT LINE WIDTHS
# ============================================================

"""
Related cases should also use consistent:

Line widths

Line styles

Marker sizes


Example:

Baseline = solid

Design A = dashed

Design B = dash-dot


The same case should not change visual identity between
panels without a reason.
"""


# ============================================================
# 55. CONSISTENT CASE STYLE
# ============================================================

case_styles = {

    "Baseline":
        {
            "linestyle":
                "-",

            "marker":
                "o"
        },

    "Design A":
        {
            "linestyle":
                "--",

            "marker":
                "s"
        },

    "Design B":
        {
            "linestyle":
                "-.",

            "marker":
                "^"
        }

}


# ============================================================
# 56. USE SAME CASE STYLE ACROSS PANELS
# ============================================================

fig, axes = plt.subplots(

    1,

    2,

    figsize=(10, 4)

)


efficiency_cases = {

    "Baseline":
        baseline_efficiency,

    "Design A":
        design_a_efficiency,

    "Design B":
        design_b_efficiency

}


for case_name, values in efficiency_cases.items():

    style = case_styles[
        case_name
    ]


    axes[0].plot(

        load_percent,

        values,

        linestyle=style[
            "linestyle"
        ],

        marker=style[
            "marker"
        ],

        label=case_name

    )


    axes[1].plot(

        load_percent,

        values
        - baseline_efficiency,

        linestyle=style[
            "linestyle"
        ],

        marker=style[
            "marker"
        ],

        label=case_name

    )


axes[0].set_ylabel(
    "Efficiency [%]"
)


axes[1].set_ylabel(
    "Difference [percentage points]"
)


for ax in axes:

    ax.set_xlabel(
        "Load [%]"
    )


    ax.grid(
        True
    )


axes[0].legend()


plt.tight_layout()

plt.show()


# ============================================================
# 57. PANEL LABEL POSITION
# ============================================================

"""
Panel labels may be placed:

Inside the upper-left corner

or

Outside the axes


depending on:

Journal style

Available space

Data location


The important requirement is:

Consistency.
"""


# ============================================================
# 58. PANEL TITLES VS PANEL LABELS
# ============================================================

"""
These are different:

(a)

is a panel identifier.


"Voltage Response"

is a panel title.


For papers:

The caption may already explain:

(a) Voltage response

(b) Current response


Therefore internal subplot titles may not always be needed.
"""


# ============================================================
# 59. COMMON X LIMITS
# ============================================================

"""
When comparing equivalent signals:

Panel (a):

Simulation


Panel (b):

Experiment


use common X limits when appropriate.
"""


# ============================================================
# 60. COMMON Y LIMITS
# ============================================================

"""
Common Y limits make visual amplitude comparison easier.

However:

Do not force unrelated physical quantities such as:

Voltage [V]

and

Current [A]


onto the same Y range merely for symmetry.
"""


# ============================================================
# 61. DIFFERENT PHYSICAL VARIABLES
# ============================================================

"""
Example:

(a) Voltage [V]

(b) Current [A]

(c) Temperature [°C]

(d) Efficiency [%]


These panels need independent Y-axis units.


The multi-panel layout provides visual organization without
pretending the variables have the same scale.
"""


# ============================================================
# 62. COMMON COLORBAR REQUIREMENT
# ============================================================

"""
A shared colorbar is appropriate when panels represent the
same response quantity using the same color mapping.

Example:

Panel A:

Design A temperature


Panel B:

Design B temperature


Both:

Temperature [°C]


Then:

Common vmin

Common vmax

Common colormap

Common colorbar


supports direct comparison.
"""


# ============================================================
# 63. DO NOT SHARE COLORBAR ACROSS DIFFERENT QUANTITIES
# ============================================================

"""
Example:

Panel A:

Efficiency [%]


Panel B:

Temperature [°C]


A single shared colorbar would be physically ambiguous.

Use separate colorbars.
"""


# ============================================================
# 64. BAR + LINE + HEATMAP + FFT
# ============================================================

"""
A multi-panel figure does NOT require every panel to use
the same plot type.

A single figure may contain:

Line plot

Bar plot

Heatmap

Contour map

FFT spectrum


when all panels answer parts of the same engineering
question.
"""


# ============================================================
# 65. REUSABLE MULTI-PANEL FORMAT FUNCTION
# ============================================================

def format_multi_panel_axes(
    axes,
    panel_labels=None,
    grid=True
):
    """
    Apply common formatting to several axes.

    Parameters
    ----------
    axes : iterable of matplotlib axes
        Axes to format.

    panel_labels : list, optional
        Example:
        ["(a)", "(b)", "(c)"]

    grid : bool
        Apply major grid.
    """

    axes = np.asarray(
        axes,
        dtype=object
    ).ravel()


    if panel_labels is not None:

        if len(
            panel_labels
        ) != len(
            axes
        ):

            raise ValueError(
                "Number of panel labels must "
                "match number of axes."
            )


    for index, ax in enumerate(
        axes
    ):

        ax.tick_params(

            axis="both",

            which="both",

            direction="in",

            top=True,

            right=True

        )


        if grid:

            ax.grid(

                True,

                which="major",

                linewidth=0.45,

                alpha=0.35

            )


        if panel_labels is not None:

            add_panel_label(

                ax,

                panel_labels[
                    index
                ]

            )


# ============================================================
# 66. USE FORMAT FUNCTION
# ============================================================

fig, axes = plt.subplots(

    2,

    2,

    figsize=(9, 6)

)


for ax, signal in zip(

    axes.flatten(),

    signals

):

    ax.plot(
        time_ms,
        signal
    )


format_multi_panel_axes(

    axes,

    panel_labels=[
        "(a)",
        "(b)",
        "(c)",
        "(d)"
    ]

)


plt.tight_layout()

plt.show()


# ============================================================
# 67. ALIGN Y LABELS
# ============================================================

"""
When labels have different lengths, their alignment can
look uneven.

Matplotlib figures provide label-alignment helpers.
"""


fig, axes = plt.subplots(

    3,

    1,

    figsize=(7, 6),

    sharex=True

)


axes[0].plot(
    time_ms,
    voltage_v
)


axes[0].set_ylabel(
    "Voltage [V]"
)


axes[1].plot(
    time_ms,
    current_a
)


axes[1].set_ylabel(
    "Output Current [A]"
)


axes[2].plot(
    time_ms,
    power_w
)


axes[2].set_ylabel(
    "Instantaneous Power [W]"
)


axes[2].set_xlabel(
    "Time [ms]"
)


fig.align_ylabels(
    axes
)


plt.tight_layout()

plt.show()


# ============================================================
# 68. PUBLICATION EXPORT FUNCTION
# ============================================================

def save_multi_panel_figure(
    fig,
    output_folder,
    filename,
    png_dpi=300,
    save_png=True,
    save_pdf=True,
    save_svg=True
):
    """
    Save a multi-panel figure in several formats.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to export.

    output_folder : str or Path
        Destination folder.

    filename : str
        Base filename.

    png_dpi : int
        PNG resolution.

    save_png : bool
        Save PNG.

    save_pdf : bool
        Save PDF.

    save_svg : bool
        Save SVG.

    Returns
    -------
    saved_files : list
        Paths of generated files.
    """

    output_folder = Path(
        output_folder
    )


    output_folder.mkdir(
        parents=True,
        exist_ok=True
    )


    if png_dpi <= 0:

        raise ValueError(
            "png_dpi must be greater than zero."
        )


    saved_files = []


    if save_png:

        png_path = (
            output_folder
            / f"{filename}.png"
        )


        fig.savefig(

            png_path,

            dpi=png_dpi

        )


        saved_files.append(
            png_path
        )


    if save_pdf:

        pdf_path = (
            output_folder
            / f"{filename}.pdf"
        )


        fig.savefig(
            pdf_path
        )


        saved_files.append(
            pdf_path
        )


    if save_svg:

        svg_path = (
            output_folder
            / f"{filename}.svg"
        )


        fig.savefig(
            svg_path
        )


        saved_files.append(
            svg_path
        )


    return saved_files


# ============================================================
# 69. FINAL REUSABLE PUBLICATION EXAMPLE
# ============================================================

with mpl.rc_context(
    publication_style
):

    fig, axes = plt.subplots(

        2,

        2,

        figsize=(
            publication_width_in,
            publication_height_in
        ),

        layout="constrained"

    )


    # --------------------------------------------------------
    # A - Voltage
    # --------------------------------------------------------

    axes[0, 0].plot(
        time_ms,
        voltage_v
    )


    axes[0, 0].set_xlabel(
        "Time [ms]"
    )


    axes[0, 0].set_ylabel(
        "Voltage [V]"
    )


    # --------------------------------------------------------
    # B - Current
    # --------------------------------------------------------

    axes[0, 1].plot(
        time_ms,
        current_a
    )


    axes[0, 1].set_xlabel(
        "Time [ms]"
    )


    axes[0, 1].set_ylabel(
        "Current [A]"
    )


    # --------------------------------------------------------
    # C - Efficiency
    # --------------------------------------------------------

    for case_name, values in efficiency_cases.items():

        style = case_styles[
            case_name
        ]


        axes[1, 0].plot(

            load_percent,

            values,

            linestyle=style[
                "linestyle"
            ],

            marker=style[
                "marker"
            ],

            label=case_name

        )


    axes[1, 0].set_xlabel(
        "Load [%]"
    )


    axes[1, 0].set_ylabel(
        "Efficiency [%]"
    )


    axes[1, 0].legend()


    # --------------------------------------------------------
    # D - Parameter map
    # --------------------------------------------------------

    final_map = axes[1, 1].pcolormesh(

        frequency_grid,

        load_grid,

        efficiency_map_b,

        shading="auto",

        cmap="viridis"

    )


    axes[1, 1].set_xlabel(
        "Switching Frequency [kHz]"
    )


    axes[1, 1].set_ylabel(
        "Load [%]"
    )


    # --------------------------------------------------------
    # Common formatting
    # --------------------------------------------------------

    format_multi_panel_axes(

        axes,

        panel_labels=[
            "(a)",
            "(b)",
            "(c)",
            "(d)"
        ],

        grid=False

    )


    axes[0, 0].grid(
        True,
        alpha=0.35
    )


    axes[0, 1].grid(
        True,
        alpha=0.35
    )


    axes[1, 0].grid(
        True,
        alpha=0.35
    )


    # --------------------------------------------------------
    # Colorbar
    # --------------------------------------------------------

    colorbar = fig.colorbar(

        final_map,

        ax=axes[
            1,
            1
        ]

    )


    colorbar.set_label(
        "Efficiency [%]"
    )


    # --------------------------------------------------------
    # Save
    # --------------------------------------------------------

    saved_files = (
        save_multi_panel_figure(

            fig=fig,

            output_folder=output_figure_folder,

            filename=(
                "final_multi_panel_publication_figure"
            ),

            png_dpi=300

        )
    )


    print(
        "\n--- Reusable Publication Files ---"
    )


    for file_path in saved_files:

        print(
            file_path
        )


    plt.show()


# ============================================================
# 70. PANEL ORDER
# ============================================================

"""
A common reading order is:

(a)  (b)

(c)  (d)


That is:

Left to right

then:

Top to bottom


Keep panel labeling consistent with the figure caption.
"""


# ============================================================
# 71. FIGURE CAPTION CONNECTION
# ============================================================

"""
Example caption structure:

Fig. X. Comparison of converter performance:
(a) output voltage,
(b) common-mode spectrum,
(c) efficiency versus load, and
(d) efficiency parameter map.


The caption should explain:

What each panel represents

Operating conditions

Important abbreviations

Relevant processing details
"""


# ============================================================
# 72. COMMON MISTAKE - TOO MANY PANELS
# ============================================================

"""
A figure containing:

12 very small panels


may technically fit on one page but become unreadable.


Consider:

Two separate figures

or

A main figure plus supplementary material.
"""


# ============================================================
# 73. COMMON MISTAKE - UNRELATED PANELS
# ============================================================

"""
Do not combine plots merely to save figure numbers.

The panels should contribute to one coherent technical
message.
"""


# ============================================================
# 74. COMMON MISTAKE - INCONSISTENT PANEL LABELS
# ============================================================

"""
Weak:

(a)

B

Plot 3

(iv)


Better:

(a)

(b)

(c)

(d)
"""


# ============================================================
# 75. COMMON MISTAKE - WRONG CAPTION ORDER
# ============================================================

"""
If the figure uses:

(a) Voltage

(b) Current

(c) FFT


the caption should use the same order.

Do not accidentally describe:

(b)

before:

(a).
"""


# ============================================================
# 76. COMMON MISTAKE - DIFFERENT FONT SIZES
# ============================================================

"""
Panel A:

14-point labels


Panel B:

8-point labels


Panel C:

11-point labels


creates an inconsistent publication figure.


Use a common style configuration.
"""


# ============================================================
# 77. COMMON MISTAKE - DIFFERENT CASE STYLES
# ============================================================

"""
Suppose:

Baseline

is solid in Panel A


but dashed in Panel C.


The reader may assume the styles represent different
cases.


Use consistent visual identities.
"""


# ============================================================
# 78. COMMON MISTAKE - DIFFERENT AXIS LIMITS
# ============================================================

"""
Two panels comparing the same variable may use:

Panel A:

0 to 100


Panel B:

90 to 100


The visual difference can become misleading.


Use shared or clearly justified limits.
"""


# ============================================================
# 79. COMMON MISTAKE - SHARED AXIS FOR DIFFERENT UNITS
# ============================================================

"""
Do not use:

sharey=True


for:

Voltage [V]

and:

Temperature [°C]


simply because both are numerical values.
"""


# ============================================================
# 80. COMMON MISTAKE - DIFFERENT HEATMAP COLOR LIMITS
# ============================================================

"""
When comparing:

Design A

and

Design B


the same color should represent the same numerical value.

Use:

common vmin

common vmax

common cmap
"""


# ============================================================
# 81. COMMON MISTAKE - ONE COLORBAR FOR DIFFERENT VARIABLES
# ============================================================

"""
Do not use one colorbar for:

Efficiency [%]

and:

Temperature [°C]


These require separate scales.
"""


# ============================================================
# 82. COMMON MISTAKE - LARGE TITLES IN EVERY PANEL
# ============================================================

"""
For journal figures:

Panel labels

+
Caption


may already provide sufficient identification.


Large titles in every panel can consume valuable space.
"""


# ============================================================
# 83. COMMON MISTAKE - PANEL LABEL COVERS DATA
# ============================================================

"""
The panel identifier:

(a)


should not hide:

Peak

Important measurement

Annotation

Legend


Move it slightly if necessary.
"""


# ============================================================
# 84. COMMON MISTAKE - LEGEND IN EVERY PANEL
# ============================================================

"""
Four identical legends may unnecessarily occupy a large
portion of the figure.

Consider:

fig.legend()


for a common legend when appropriate.
"""


# ============================================================
# 85. COMMON MISTAKE - TINY COLORBAR TEXT
# ============================================================

"""
A colorbar belongs to the figure's quantitative
communication.

Its:

Label

Ticks

Units


must remain readable after publication scaling.
"""


# ============================================================
# 86. COMMON MISTAKE - NO PANEL UNITS
# ============================================================

"""
Panel labels such as:

Voltage

Current

Power


should normally include engineering units:

Voltage [V]

Current [A]

Power [W]
"""


# ============================================================
# 87. COMMON MISTAKE - OVERUSING GridSpec
# ============================================================

"""
For a simple:

2 × 2


figure:

plt.subplots()


is often easier and clearer.


Use:

GridSpec


when the layout actually needs unequal or spanning panels.
"""


# ============================================================
# 88. COMMON MISTAKE - MANUAL PIXEL POSITIONING
# ============================================================

"""
Manually positioning every axis using arbitrary coordinates
can make the figure difficult to maintain.

Prefer:

subplots()

GridSpec

subplot_mosaic()

Constrained Layout


when possible.
"""


# ============================================================
# 89. COMMON MISTAKE - FIGURE TOO WIDE
# ============================================================

"""
A large 15-inch figure may look excellent on a monitor but
become unreadable after shrinking into a journal column.

Design close to final physical dimensions.
"""


# ============================================================
# 90. COMMON MISTAKE - FIGURE TOO SMALL
# ============================================================

"""
Packing:

Four complex panels

into a:

3-inch-wide figure


may make labels and data unreadable.


Use a larger publication layout when required.
"""


# ============================================================
# 91. COMMON MISTAKE - LOW RESOLUTION
# ============================================================

"""
A multi-panel figure contains more graphical information.

For raster output:

Use an appropriate DPI.


For vector-compatible line plots:

PDF / SVG

may be useful when accepted by the workflow.
"""


# ============================================================
# 92. MULTI-PANEL DECISION GUIDE
# ============================================================

"""
One Result?
        ↓
Single Plot


One Result + Small Detail?
        ↓
Inset


Two Related Results?
        ↓
1 × 2
or
2 × 1


Four Related Results?
        ↓
2 × 2


Unequal Panel Importance?
        ↓
GridSpec


Complex Semantic Layout?
        ↓
subplot_mosaic()


Many Independent Results?
        ↓
Consider Multiple Figures
"""


# ============================================================
# 93. TIME-DOMAIN MULTI-PANEL WORKFLOW
# ============================================================

"""
Raw Time Data
      ↓
Voltage
Current
Power
Temperature
      ↓
Shared Time Axis
      ↓
2 × 2 Figure
      ↓
Common Panel Labels
      ↓
Engineering Interpretation
"""


# ============================================================
# 94. SIMULATION / EXPERIMENT WORKFLOW
# ============================================================

"""
Simulation
     +
Experiment
        ↓
Panel (a)
Full Waveform
        ↓
Panel (b)
Zoomed Transition
        ↓
Panel (c)
Difference
        ↓
Panel (d)
Summary Metric
        ↓
One Validation Figure
"""


# ============================================================
# 95. FREQUENCY-DOMAIN WORKFLOW
# ============================================================

"""
Panel (a)

Full Spectrum


Panel (b)

Reduction Spectrum


Panel (c)

Selected Frequencies


Panel (d)

Summary Statistics


        ↓

Complete Frequency-Domain Comparison
"""


# ============================================================
# 96. PARAMETER-STUDY WORKFLOW
# ============================================================

"""
Panel (a)

Efficiency Map


Panel (b)

Loss Map


Panel (c)

Temperature Map


Panel (d)

Feasible Region


        ↓

Complete Design-Space Figure
"""


# ============================================================
# 97. COMPLETE PUBLICATION WORKFLOW
# ============================================================

"""
Define Scientific Message
        ↓
Choose Required Results
        ↓
Decide Number of Panels
        ↓
Choose Layout
        ↓
subplots()
GridSpec
subplot_mosaic()
        ↓
Set Final Figure Dimensions
        ↓
Plot Data
        ↓
Use Consistent Styles
        ↓
Set Shared Axes Where Appropriate
        ↓
Add Panel Labels
        ↓
Add Common Legend if Appropriate
        ↓
Add Shared Colorbar if Appropriate
        ↓
Check Alignment
        ↓
Check Final Size
        ↓
Export
        ↓
Write Caption
"""


# ============================================================
# 98. PUBLICATION CHECKLIST
# ============================================================

"""
Before publishing a multi-panel figure, check:


SCIENTIFIC STORY
------------------------------------------------------------

Do the panels belong together?


ORDER
------------------------------------------------------------

Is the reading order clear?

(a)
(b)
(c)
(d)


LABELS
------------------------------------------------------------

Are panel labels visible?

Do they match the caption?


AXES
------------------------------------------------------------

Are units correct?

Are shared axes physically justified?

Are equivalent cases using common limits?


STYLES
------------------------------------------------------------

Are the same cases represented consistently?


LEGEND
------------------------------------------------------------

Is one common legend better?

Does the legend hide data?


COLORBAR
------------------------------------------------------------

Do comparable heatmaps use the same scale?

Does one shared colorbar make physical sense?


LAYOUT
------------------------------------------------------------

Are panels large enough?

Are labels clipped?

Are spaces balanced?


TYPOGRAPHY
------------------------------------------------------------

Are all fonts readable at final publication size?


FIGURE SIZE
------------------------------------------------------------

Was the figure designed near its intended final width?


OUTPUT
------------------------------------------------------------

PNG generated?

PDF generated?

SVG generated?


FINAL CHECK
------------------------------------------------------------

Open the exported figure.

Check it at approximately the size readers will see.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
MULTI-PANEL PUBLICATION FIGURES


1. BASIC 1 × 2

fig, axes = plt.subplots(

    1,

    2

)


------------------------------------------------------------


2. BASIC 2 × 1

fig, axes = plt.subplots(

    2,

    1

)


------------------------------------------------------------


3. BASIC 2 × 2

fig, axes = plt.subplots(

    2,

    2

)


------------------------------------------------------------


4. ACCESS AXES

axes[0, 0]

axes[0, 1]

axes[1, 0]

axes[1, 1]


------------------------------------------------------------


5. FLATTEN

flat_axes = axes.flatten()


Useful for automatic processing.


------------------------------------------------------------


6. SHARED X AXIS

plt.subplots(

    ...,

    sharex=True

)


Useful when panels share:

Time

Frequency

Load

etc.


------------------------------------------------------------


7. SHARED Y AXIS

sharey=True


Use only when the panels represent compatible physical
quantities.


------------------------------------------------------------


8. PANEL LABELS

(a)

(b)

(c)

(d)


Use:

ax.text(
    ...,
    transform=ax.transAxes
)


------------------------------------------------------------


9. COMMON X LABEL

fig.supxlabel(
    "Time [ms]"
)


------------------------------------------------------------


10. COMMON Y LABEL

fig.supylabel(
    "Voltage [V]"
)


------------------------------------------------------------


11. FIGURE TITLE

fig.suptitle(
    "..."
)


Often useful for:

Tutorials

Reports

Presentations


but may be unnecessary in a journal figure.


------------------------------------------------------------


12. COMMON LEGEND

handles, labels = (
    ax.get_legend_handles_labels()
)


fig.legend(

    handles,

    labels

)


------------------------------------------------------------


13. REMOVE UNUSED AXES

fig.delaxes(
    ax
)


------------------------------------------------------------


14. WIDTH RATIOS

plt.subplots(

    1,

    2,

    width_ratios=[
        2,
        1
    ]

)


------------------------------------------------------------


15. HEIGHT RATIOS

plt.subplots(

    2,

    1,

    height_ratios=[
        2,
        1
    ]

)


------------------------------------------------------------


16. GridSpec

grid = GridSpec(

    rows,

    columns,

    figure=fig

)


Useful when panels need:

Different sizes

Row spanning

Column spanning


------------------------------------------------------------


17. SPANNING COLUMNS

ax = fig.add_subplot(

    grid[
        0,
        :
    ]

)


------------------------------------------------------------


18. SPANNING ROWS

ax = fig.add_subplot(

    grid[
        :,
        0
    ]

)


------------------------------------------------------------


19. subplot_mosaic()

Useful for semantic layouts:

axes[
    "fft"
]

axes[
    "time"
]

axes[
    "summary"
]


------------------------------------------------------------


20. COMMON COLOR SCALE

For directly comparable heatmaps:

same cmap

same vmin

same vmax


------------------------------------------------------------


21. COMMON COLORBAR

fig.colorbar(

    image,

    ax=axes

)


Useful when several panels use the same response scale.


------------------------------------------------------------


22. DIFFERENT PHYSICAL COLOR VARIABLES

Efficiency [%]

and

Temperature [°C]


should not share one numerical colorbar.


------------------------------------------------------------


23. CONSISTENT CASE STYLES

Baseline:

Solid


Design A:

Dashed


Design B:

Dash-dot


Keep these meanings consistent across panels.


------------------------------------------------------------


24. PUBLICATION SIZE

Design the whole composite figure near its final physical
dimensions.


------------------------------------------------------------


25. CONSTRAINED LAYOUT

Example:

fig, axes = plt.subplots(

    2,

    2,

    layout="constrained"

)


Useful for complex layouts involving labels, legends, and
colorbars.


------------------------------------------------------------


26. DO NOT OVERLOAD

More panels

does NOT automatically mean:

Better paper figure.


------------------------------------------------------------


27. INSET vs MULTI-PANEL

INSET

Small detail of one result


MULTI-PANEL

Several related results


------------------------------------------------------------


28. GRID SPECIFICATION

Simple figure:

subplots()


Complex unequal figure:

GridSpec


Semantic complex figure:

subplot_mosaic()


------------------------------------------------------------


29. MULTI-PANEL APPLICATIONS

Especially useful for:

Simulation vs experiment

Voltage / current / power

Time + FFT

Absolute + difference

Efficiency + loss + temperature

Parameter sweeps

EMI comparisons

ML results

Experimental validation


------------------------------------------------------------


30. MOST IMPORTANT PRINCIPLE

A multi-panel figure should answer:

Why do these results belong together?


Every panel should contribute to the same technical
message.


------------------------------------------------------------


31. COMPLETE WORKFLOW

Scientific Question
        ↓
Select Related Results
        ↓
Choose Panel Count
        ↓
Choose Layout
        ↓
Set Final Figure Size
        ↓
Plot Panels
        ↓
Synchronize Appropriate Axes
        ↓
Use Consistent Styles
        ↓
Add (a), (b), (c), (d)
        ↓
Add Legend / Colorbar
        ↓
Check Layout
        ↓
Check Final Size
        ↓
Export PNG / PDF / SVG
        ↓
Write Caption


------------------------------------------------------------


NEXT:

28_confidence_bands_and_shaded_regions.py


The next file will extend the earlier:

17_error_bars.py


into continuous uncertainty visualization using:

fill_between()

Mean ± standard deviation bands

Mean ± SEM bands

Confidence bands

Min-max envelopes

Percentile bands

Monte Carlo envelopes

Experimental variability

Simulation uncertainty

Operating regions

Safe / unsafe regions

Target bands

Vertical operating zones

Multiple uncertainty bands

and publication-quality engineering uncertainty plots.
"""
