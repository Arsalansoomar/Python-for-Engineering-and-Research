"""
============================================================
Python for Engineering and Research
07 - Subplots
============================================================

Purpose:
    Demonstrate how multiple plots can be arranged inside
    one Matplotlib figure.

Topics:
    1. What is a subplot?
    2. When should subplots be used?
    3. Two vertical subplots
    4. Shared X-axis
    5. Three engineering variables
    6. Multiple variables in one subplot
    7. 2 x 2 subplot layout
    8. Accessing subplot axes
    9. Automatic subplot generation
    10. Removing unused axes
    11. Figure-level title
    12. Axis limits
    13. Saving subplot figures
    14. Common mistakes
    15. Key takeaways

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT IS A SUBPLOT?
# ============================================================

"""
A subplot is an individual plot placed inside a larger
Matplotlib figure.

Instead of creating several separate figures:

Figure 1
    Voltage

Figure 2
    Current

Figure 3
    Temperature


we can create:

One Figure

┌──────────────────────────────┐
│ Voltage vs Time              │
├──────────────────────────────┤
│ Current vs Time              │
├──────────────────────────────┤
│ Temperature vs Time          │
└──────────────────────────────┘


Each subplot has its own axes.
"""


# ============================================================
# 2. WHEN SHOULD SUBPLOTS BE USED?
# ============================================================

"""
Subplots are particularly useful when:

- Variables have different physical units
- Several related results must be shown together
- A common X-axis is shared
- Direct visual comparison is required
- Separate axes improve readability
- Several experimental responses are presented together


Engineering examples:

Voltage [V]
Current [A]
Temperature [°C]

all versus:

Time [s]


Another example:

VDS waveform
Gate voltage
Current
Power

versus:

Time
"""


# ============================================================
# 3. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path


# ============================================================
# 4. EXAMPLE ENGINEERING DATA
# ============================================================

time_ms = np.array(
    [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10
    ],
    dtype=float
)


input_voltage = np.array(
    [
        48.0,
        48.1,
        48.0,
        48.2,
        48.1,
        48.0,
        48.2,
        48.1,
        48.0,
        48.1,
        48.0
    ]
)


output_voltage = np.array(
    [
        0,
        18,
        35,
        52,
        67,
        78,
        86,
        91,
        94,
        95.5,
        96
    ]
)


input_current = np.array(
    [
        0.2,
        1.0,
        2.0,
        3.0,
        3.8,
        4.4,
        4.8,
        5.0,
        5.1,
        5.1,
        5.0
    ]
)


output_current = np.array(
    [
        0.0,
        0.3,
        0.7,
        1.1,
        1.5,
        1.8,
        2.0,
        2.2,
        2.3,
        2.35,
        2.4
    ]
)


temperature = np.array(
    [
        25,
        27,
        30,
        34,
        39,
        45,
        51,
        57,
        62,
        66,
        69
    ]
)


# ============================================================
# 5. BASIC TWO-SUBPLOT FIGURE
# ============================================================

"""
General syntax:

fig, axes = plt.subplots(
    nrows=2,
    ncols=1
)


This creates:

2 rows

1 column
"""


fig, axes = plt.subplots(
    nrows=2,
    ncols=1,
    figsize=(7, 6)
)


# First subplot

axes[0].plot(
    time_ms,
    output_voltage,
    linewidth=2
)


axes[0].set_xlabel(
    "Time [ms]"
)

axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].set_title(
    "Output Voltage"
)

axes[0].grid(
    True
)


# Second subplot

axes[1].plot(
    time_ms,
    output_current,
    linewidth=2
)


axes[1].set_xlabel(
    "Time [ms]"
)

axes[1].set_ylabel(
    "Current [A]"
)

axes[1].set_title(
    "Output Current"
)

axes[1].grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 6. UNDERSTANDING axes[]
# ============================================================

"""
For:

fig, axes = plt.subplots(
    2,
    1
)


Python creates two axes:

axes[0]
    First subplot

axes[1]
    Second subplot


Therefore:

axes[0].plot(...)

plots on the first subplot.


axes[1].plot(...)

plots on the second subplot.
"""


# ============================================================
# 7. SHARED X-AXIS
# ============================================================

"""
When all plots use the same X variable, such as time,
the X-axis can be shared.

Use:

sharex=True


This reduces repeated tick labels and improves alignment.
"""


fig, axes = plt.subplots(
    nrows=2,
    ncols=1,
    figsize=(7, 6),
    sharex=True
)


axes[0].plot(
    time_ms,
    output_voltage,
    linewidth=2
)

axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].set_title(
    "Output Voltage"
)

axes[0].grid(
    True
)


axes[1].plot(
    time_ms,
    output_current,
    linewidth=2
)

axes[1].set_xlabel(
    "Time [ms]"
)

axes[1].set_ylabel(
    "Current [A]"
)

axes[1].set_title(
    "Output Current"
)

axes[1].grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 8. WHY sharex=True IS USEFUL
# ============================================================

"""
Suppose all plots represent:

0 to 10 ms


Without shared axes:

Each subplot independently displays its own X ticks.


With:

sharex=True


the subplots remain aligned and the final X label only
needs to appear on the bottom plot.

This is common in engineering waveform figures.
"""


# ============================================================
# 9. THREE DIFFERENT PHYSICAL VARIABLES
# ============================================================

"""
Now display:

Voltage [V]

Current [A]

Temperature [°C]


Each variable receives its own Y-axis.

This is normally clearer than putting all three variables
on one mixed-unit axis.
"""


fig, axes = plt.subplots(
    nrows=3,
    ncols=1,
    figsize=(7, 8),
    sharex=True
)


# Voltage

axes[0].plot(
    time_ms,
    output_voltage,
    linewidth=2
)

axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].set_title(
    "Output Voltage"
)

axes[0].grid(
    True
)


# Current

axes[1].plot(
    time_ms,
    output_current,
    linewidth=2
)

axes[1].set_ylabel(
    "Current [A]"
)

axes[1].set_title(
    "Output Current"
)

axes[1].grid(
    True
)


# Temperature

axes[2].plot(
    time_ms,
    temperature,
    linewidth=2
)

axes[2].set_xlabel(
    "Time [ms]"
)

axes[2].set_ylabel(
    "Temperature [°C]"
)

axes[2].set_title(
    "Device Temperature"
)

axes[2].grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 10. MULTIPLE VARIABLES INSIDE ONE SUBPLOT
# ============================================================

"""
A subplot can still contain several curves when those
variables have compatible units.

Example:

First subplot:

Input Voltage
Output Voltage


Second subplot:

Input Current
Output Current
"""


fig, axes = plt.subplots(
    nrows=2,
    ncols=1,
    figsize=(7, 6),
    sharex=True
)


# Voltage subplot

axes[0].plot(
    time_ms,
    input_voltage,
    linewidth=2,
    label="Input Voltage"
)

axes[0].plot(
    time_ms,
    output_voltage,
    linewidth=2,
    label="Output Voltage"
)


axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].set_title(
    "Converter Voltages"
)

axes[0].grid(
    True
)

axes[0].legend()


# Current subplot

axes[1].plot(
    time_ms,
    input_current,
    linewidth=2,
    label="Input Current"
)

axes[1].plot(
    time_ms,
    output_current,
    linewidth=2,
    label="Output Current"
)


axes[1].set_xlabel(
    "Time [ms]"
)

axes[1].set_ylabel(
    "Current [A]"
)

axes[1].set_title(
    "Converter Currents"
)

axes[1].grid(
    True
)

axes[1].legend()


plt.tight_layout()

plt.show()


# ============================================================
# 11. ADD DERIVED POWER VARIABLES
# ============================================================

input_power = (
    input_voltage
    * input_current
)


output_power = (
    output_voltage
    * output_current
)


# ============================================================
# 12. FOUR ENGINEERING SUBPLOTS
# ============================================================

"""
A four-panel figure can show:

Voltage

Current

Power

Temperature
"""


fig, axes = plt.subplots(
    nrows=4,
    ncols=1,
    figsize=(7, 10),
    sharex=True
)


# ------------------------------------------------------------
# Voltage
# ------------------------------------------------------------

axes[0].plot(
    time_ms,
    input_voltage,
    label="Input Voltage"
)

axes[0].plot(
    time_ms,
    output_voltage,
    label="Output Voltage"
)

axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].legend()

axes[0].grid(
    True
)


# ------------------------------------------------------------
# Current
# ------------------------------------------------------------

axes[1].plot(
    time_ms,
    input_current,
    label="Input Current"
)

axes[1].plot(
    time_ms,
    output_current,
    label="Output Current"
)

axes[1].set_ylabel(
    "Current [A]"
)

axes[1].legend()

axes[1].grid(
    True
)


# ------------------------------------------------------------
# Power
# ------------------------------------------------------------

axes[2].plot(
    time_ms,
    input_power,
    label="Input Power"
)

axes[2].plot(
    time_ms,
    output_power,
    label="Output Power"
)

axes[2].set_ylabel(
    "Power [W]"
)

axes[2].legend()

axes[2].grid(
    True
)


# ------------------------------------------------------------
# Temperature
# ------------------------------------------------------------

axes[3].plot(
    time_ms,
    temperature
)

axes[3].set_xlabel(
    "Time [ms]"
)

axes[3].set_ylabel(
    "Temperature [°C]"
)

axes[3].grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 13. FIGURE-LEVEL TITLE
# ============================================================

"""
Instead of giving every subplot a long title, the complete
figure can have one overall title.

Use:

fig.suptitle()
"""


fig, axes = plt.subplots(
    3,
    1,
    figsize=(7, 8),
    sharex=True
)


fig.suptitle(
    "DC-DC Converter Operating Variables"
)


axes[0].plot(
    time_ms,
    output_voltage
)

axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].grid(
    True
)


axes[1].plot(
    time_ms,
    output_current
)

axes[1].set_ylabel(
    "Current [A]"
)

axes[1].grid(
    True
)


axes[2].plot(
    time_ms,
    temperature
)

axes[2].set_xlabel(
    "Time [ms]"
)

axes[2].set_ylabel(
    "Temperature [°C]"
)

axes[2].grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 14. 2 x 2 SUBPLOT LAYOUT
# ============================================================

"""
Subplots do not need to be vertically stacked.

Example:

2 rows
2 columns


┌──────────────┬──────────────┐
│ Voltage      │ Current      │
├──────────────┼──────────────┤
│ Power        │ Temperature  │
└──────────────┴──────────────┘
"""


fig, axes = plt.subplots(
    nrows=2,
    ncols=2,
    figsize=(10, 7)
)


# ============================================================
# 15. ACCESS 2D AXES
# ============================================================

"""
For a 2 x 2 subplot:

axes[0, 0]
    Top-left

axes[0, 1]
    Top-right

axes[1, 0]
    Bottom-left

axes[1, 1]
    Bottom-right
"""


# Top-left

axes[0, 0].plot(
    time_ms,
    output_voltage
)

axes[0, 0].set_xlabel(
    "Time [ms]"
)

axes[0, 0].set_ylabel(
    "Voltage [V]"
)

axes[0, 0].set_title(
    "Output Voltage"
)

axes[0, 0].grid(
    True
)


# Top-right

axes[0, 1].plot(
    time_ms,
    output_current
)

axes[0, 1].set_xlabel(
    "Time [ms]"
)

axes[0, 1].set_ylabel(
    "Current [A]"
)

axes[0, 1].set_title(
    "Output Current"
)

axes[0, 1].grid(
    True
)


# Bottom-left

axes[1, 0].plot(
    time_ms,
    output_power
)

axes[1, 0].set_xlabel(
    "Time [ms]"
)

axes[1, 0].set_ylabel(
    "Power [W]"
)

axes[1, 0].set_title(
    "Output Power"
)

axes[1, 0].grid(
    True
)


# Bottom-right

axes[1, 1].plot(
    time_ms,
    temperature
)

axes[1, 1].set_xlabel(
    "Time [ms]"
)

axes[1, 1].set_ylabel(
    "Temperature [°C]"
)

axes[1, 1].set_title(
    "Temperature"
)

axes[1, 1].grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 16. FLATTEN 2D AXES
# ============================================================

"""
For automatic subplot processing, a 2D axes array can be
converted into a one-dimensional array.

Use:

axes = axes.flatten()


Then:

axes[0]
axes[1]
axes[2]
axes[3]

can be used instead of:

axes[0, 0]
axes[0, 1]
axes[1, 0]
axes[1, 1]
"""


fig, axes = plt.subplots(
    2,
    2,
    figsize=(10, 7)
)


axes = axes.flatten()


axes[0].plot(
    time_ms,
    output_voltage
)

axes[0].set_title(
    "Voltage"
)


axes[1].plot(
    time_ms,
    output_current
)

axes[1].set_title(
    "Current"
)


axes[2].plot(
    time_ms,
    output_power
)

axes[2].set_title(
    "Power"
)


axes[3].plot(
    time_ms,
    temperature
)

axes[3].set_title(
    "Temperature"
)


for ax in axes:

    ax.set_xlabel(
        "Time [ms]"
    )

    ax.grid(
        True
    )


plt.tight_layout()

plt.show()


# ============================================================
# 17. AUTOMATIC SUBPLOT DATA STRUCTURE
# ============================================================

"""
A dictionary can contain:

Data
Y-axis label
Title


This allows subplot generation to be automated.
"""


subplot_data = {

    "Voltage": {

        "values": output_voltage,

        "ylabel": "Voltage [V]",

        "title": "Output Voltage"

    },

    "Current": {

        "values": output_current,

        "ylabel": "Current [A]",

        "title": "Output Current"

    },

    "Power": {

        "values": output_power,

        "ylabel": "Power [W]",

        "title": "Output Power"

    },

    "Temperature": {

        "values": temperature,

        "ylabel": "Temperature [°C]",

        "title": "Device Temperature"

    }

}


# ============================================================
# 18. AUTOMATIC 2 x 2 SUBPLOT GENERATION
# ============================================================

fig, axes = plt.subplots(
    2,
    2,
    figsize=(10, 7)
)


axes = axes.flatten()


for ax, (
    variable_name,
    information
) in zip(
    axes,
    subplot_data.items()
):

    ax.plot(
        time_ms,
        information[
            "values"
        ],
        linewidth=2
    )


    ax.set_xlabel(
        "Time [ms]"
    )

    ax.set_ylabel(
        information[
            "ylabel"
        ]
    )

    ax.set_title(
        information[
            "title"
        ]
    )

    ax.grid(
        True
    )


plt.tight_layout()

plt.show()


# ============================================================
# 19. WHY AUTOMATIC SUBPLOTS ARE USEFUL
# ============================================================

"""
Imagine having:

8 variables

12 variables

20 measurement channels


Instead of manually writing:

axes[0].plot(...)
axes[1].plot(...)
axes[2].plot(...)
...


the variables can be stored inside a dictionary and
processed automatically with a loop.

This becomes particularly useful later when data are loaded
from CSV or Excel files.
"""


# ============================================================
# 20. AUTOMATIC NUMBER OF SUBPLOTS
# ============================================================

"""
The number of subplot rows can also be determined from
the number of variables.
"""


selected_data = {

    "Output Voltage": {

        "values": output_voltage,

        "ylabel": "Voltage [V]"

    },

    "Output Current": {

        "values": output_current,

        "ylabel": "Current [A]"

    },

    "Output Power": {

        "values": output_power,

        "ylabel": "Power [W]"

    },

    "Temperature": {

        "values": temperature,

        "ylabel": "Temperature [°C]"

    }

}


number_of_plots = len(
    selected_data
)


fig, axes = plt.subplots(
    number_of_plots,
    1,
    figsize=(
        7,
        2.5 * number_of_plots
    ),
    sharex=True
)


# ============================================================
# 21. HANDLE SINGLE SUBPLOT CASE
# ============================================================

"""
When only one subplot exists, Matplotlib may return one
Axes object instead of an array.

np.atleast_1d() makes the structure consistent.
"""


axes = np.atleast_1d(
    axes
)


for ax, (
    variable_name,
    information
) in zip(
    axes,
    selected_data.items()
):

    ax.plot(
        time_ms,
        information[
            "values"
        ],
        linewidth=2
    )


    ax.set_ylabel(
        information[
            "ylabel"
        ]
    )

    ax.set_title(
        variable_name
    )

    ax.grid(
        True
    )


axes[-1].set_xlabel(
    "Time [ms]"
)


plt.tight_layout()

plt.show()


# ============================================================
# 22. AXIS LIMITS FOR INDIVIDUAL SUBPLOTS
# ============================================================

"""
Each subplot can have independent Y-axis limits.

Example:

Voltage:

0 to 105 V

Current:

0 to 3 A

Temperature:

20 to 80 °C
"""


fig, axes = plt.subplots(
    3,
    1,
    figsize=(7, 8),
    sharex=True
)


axes[0].plot(
    time_ms,
    output_voltage
)

axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].set_ylim(
    0,
    105
)

axes[0].grid(
    True
)


axes[1].plot(
    time_ms,
    output_current
)

axes[1].set_ylabel(
    "Current [A]"
)

axes[1].set_ylim(
    0,
    3
)

axes[1].grid(
    True
)


axes[2].plot(
    time_ms,
    temperature
)

axes[2].set_xlabel(
    "Time [ms]"
)

axes[2].set_ylabel(
    "Temperature [°C]"
)

axes[2].set_ylim(
    20,
    80
)

axes[2].grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 23. SHARE BOTH X AND Y AXES
# ============================================================

"""
sharex=True

is useful when subplots use the same X-axis.

sharey=True

can be useful when all subplots display the same type of
quantity and should use identical Y-axis scaling.


Example:

Four voltage cases.

For Voltage / Current / Temperature, however, sharey=True
would normally NOT be appropriate because their units differ.
"""


# ============================================================
# 24. MULTIPLE CASES IN EACH SUBPLOT
# ============================================================

"""
Subplots can also compare multiple engineering cases.

Example:

Top:

Input and Output Voltage

Middle:

Input and Output Current

Bottom:

Input and Output Power
"""


fig, axes = plt.subplots(
    3,
    1,
    figsize=(7, 8),
    sharex=True
)


# Voltage

axes[0].plot(
    time_ms,
    input_voltage,
    label="Input"
)

axes[0].plot(
    time_ms,
    output_voltage,
    label="Output"
)

axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].legend()

axes[0].grid(
    True
)


# Current

axes[1].plot(
    time_ms,
    input_current,
    label="Input"
)

axes[1].plot(
    time_ms,
    output_current,
    label="Output"
)

axes[1].set_ylabel(
    "Current [A]"
)

axes[1].legend()

axes[1].grid(
    True
)


# Power

axes[2].plot(
    time_ms,
    input_power,
    label="Input"
)

axes[2].plot(
    time_ms,
    output_power,
    label="Output"
)

axes[2].set_xlabel(
    "Time [ms]"
)

axes[2].set_ylabel(
    "Power [W]"
)

axes[2].legend()

axes[2].grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 25. UNUSED SUBPLOTS
# ============================================================

"""
Sometimes the subplot grid contains more axes than the
number of available variables.

Example:

2 x 2 grid

but only:

3 variables


The unused axis can be removed using:

fig.delaxes()
"""


three_variables = {

    "Voltage": output_voltage,

    "Current": output_current,

    "Temperature": temperature

}


fig, axes = plt.subplots(
    2,
    2,
    figsize=(10, 7)
)


axes = axes.flatten()


for ax, (
    variable_name,
    values
) in zip(
    axes,
    three_variables.items()
):

    ax.plot(
        time_ms,
        values
    )

    ax.set_title(
        variable_name
    )

    ax.set_xlabel(
        "Time [ms]"
    )

    ax.grid(
        True
    )


# Remove unused axes

for unused_ax in axes[
    len(
        three_variables
    ):
]:

    fig.delaxes(
        unused_ax
    )


plt.tight_layout()

plt.show()


# ============================================================
# 26. GLOBAL X AND Y LABELS
# ============================================================

"""
Matplotlib can also provide figure-level labels.

For example:

fig.supxlabel()

fig.supylabel()


These are useful when all subplots share the same
physical axis meaning.
"""


fig, axes = plt.subplots(
    2,
    2,
    figsize=(10, 7)
)


axes = axes.flatten()


voltage_cases = {

    "Input Voltage": input_voltage,

    "Output Voltage": output_voltage,

    "Scaled Input Voltage": (
        input_voltage
        * 1.5
    ),

    "Scaled Output Voltage": (
        output_voltage
        * 0.8
    )

}


for ax, (
    name,
    values
) in zip(
    axes,
    voltage_cases.items()
):

    ax.plot(
        time_ms,
        values
    )

    ax.set_title(
        name
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


plt.tight_layout()

plt.show()


# ============================================================
# 27. SAVE FINAL SUBPLOT FIGURE
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


fig, axes = plt.subplots(
    3,
    1,
    figsize=(7, 8),
    sharex=True
)


fig.suptitle(
    "Converter Measurement Summary"
)


# Voltage

axes[0].plot(
    time_ms,
    output_voltage,
    linewidth=2
)

axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].grid(
    True
)


# Current

axes[1].plot(
    time_ms,
    output_current,
    linewidth=2
)

axes[1].set_ylabel(
    "Current [A]"
)

axes[1].grid(
    True
)


# Temperature

axes[2].plot(
    time_ms,
    temperature,
    linewidth=2
)

axes[2].set_xlabel(
    "Time [ms]"
)

axes[2].set_ylabel(
    "Temperature [°C]"
)

axes[2].grid(
    True
)


plt.tight_layout()


# ============================================================
# 28. SAVE PNG
# ============================================================

png_file = (
    output_folder
    / "subplots_example.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 29. SAVE PDF
# ============================================================

pdf_file = (
    output_folder
    / "subplots_example.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 30. SAVE SVG
# ============================================================

svg_file = (
    output_folder
    / "subplots_example.svg"
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
# 31. COMMON MISTAKE - MIXING axes AND ax
# ============================================================

"""
For one plot:

fig, ax = plt.subplots()


Use:

ax.plot(...)


For several plots:

fig, axes = plt.subplots(
    3,
    1
)


Use:

axes[0].plot(...)
axes[1].plot(...)
axes[2].plot(...)


Be careful not to confuse:

ax

with:

axes
"""


# ============================================================
# 32. COMMON MISTAKE - TOO MANY SUBPLOTS
# ============================================================

"""
Subplots improve organization, but a figure containing:

15 tiny panels

may be difficult to read.

Possible alternatives:

- Separate figures
- Multiple figure groups
- Select representative variables
- Larger figure dimensions
- Interactive visualization
"""


# ============================================================
# 33. COMMON MISTAKE - DUPLICATE X LABELS
# ============================================================

"""
For vertically stacked plots sharing the same X variable:

Time [ms]

it is usually unnecessary to label the X-axis on every
subplot.

Prefer:

sharex=True


and place the X label on the bottom subplot.
"""


# ============================================================
# 34. COMMON MISTAKE - INCONSISTENT TIME AXES
# ============================================================

"""
If multiple signals represent the same measurement window,
their X-axis limits should normally align.

For example:

Voltage:
0 to 10 ms

Current:
2 to 8 ms

Temperature:
0 to 20 ms


would make visual comparison difficult unless those
different windows are intentional.
"""


# ============================================================
# 35. COMMON MISTAKE - INCOMPATIBLE sharey
# ============================================================

"""
Avoid:

sharey=True


for variables such as:

Voltage [V]

Current [A]

Temperature [°C]


because their Y-axis meanings are different.

sharey=True is more appropriate for:

Case A Voltage

Case B Voltage

Case C Voltage
"""


# ============================================================
# 36. COMMON MISTAKE - NO SPACE BETWEEN PANELS
# ============================================================

"""
Without layout management, subplot labels may overlap.

Use:

plt.tight_layout()


or, when creating the figure:

plt.subplots(
    ...,
    constrained_layout=True
)


Both approaches help organize subplot spacing.
"""


# ============================================================
# 37. tight_layout VS constrained_layout
# ============================================================

"""
Common approach:

fig, axes = plt.subplots(...)

...

plt.tight_layout()


Alternative:

fig, axes = plt.subplots(
    ...,
    constrained_layout=True
)


Both help prevent:

Axis-label overlap

Title overlap

Tick-label clipping


Avoid unnecessarily using both approaches in the same
figure unless you understand the layout interaction.
"""


# ============================================================
# 38. SUBPLOT DECISION WORKFLOW
# ============================================================

"""
Several Variables
       ↓
Do they have different units?
       / \
     Yes  No
     ↓     ↓
Subplots  Could share one axis
     ↓
Do they share the same X variable?
       / \
     Yes  No
     ↓     ↓
sharex=True   Independent axes
     ↓
Choose layout
     ↓
Vertical
Horizontal
2 x 2
Automatic
     ↓
Add labels
     ↓
Check readability
     ↓
Save figure
"""


# ============================================================
# 39. ENGINEERING EXAMPLE DECISION
# ============================================================

"""
Dataset:

Time
Input Voltage
Output Voltage
Input Current
Output Current
Temperature


Possible layout:


SUBPLOT 1

Input Voltage
Output Voltage

Y-axis:
Voltage [V]


SUBPLOT 2

Input Current
Output Current

Y-axis:
Current [A]


SUBPLOT 3

Temperature

Y-axis:
Temperature [°C]


Shared X-axis:

Time [ms]


This is usually more scientifically interpretable than
placing all five curves on one mixed-unit Y-axis.
"""


# ============================================================
# 40. CONNECTION TO CSV AND EXCEL
# ============================================================

"""
Later, the same concept will be applied to external data.

Example:

data = pd.read_csv(
    "measurement.csv"
)


Then:

axes[0].plot(
    data["Time"],
    data["Voltage"]
)

axes[1].plot(
    data["Time"],
    data["Current"]
)

axes[2].plot(
    data["Time"],
    data["Temperature"]
)


Eventually, even the subplot variables can be selected
automatically from column names.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
SUBPLOTS


1. BASIC STRUCTURE

fig, axes = plt.subplots(
    2,
    1
)


------------------------------------------------------------


2. ACCESS SUBPLOTS

axes[0]

axes[1]


------------------------------------------------------------


3. SHARED X-AXIS

fig, axes = plt.subplots(
    3,
    1,
    sharex=True
)


Useful for:

Voltage vs Time

Current vs Time

Temperature vs Time


------------------------------------------------------------


4. 2 x 2 LAYOUT

fig, axes = plt.subplots(
    2,
    2
)


Access:

axes[0, 0]

axes[0, 1]

axes[1, 0]

axes[1, 1]


------------------------------------------------------------


5. FLATTEN AXES

axes = axes.flatten()


Then:

axes[0]

axes[1]

axes[2]

axes[3]


This simplifies loops.


------------------------------------------------------------


6. DIFFERENT UNITS

Subplots are useful for:

Voltage [V]

Current [A]

Power [W]

Temperature [°C]


because each quantity retains its own physical axis.


------------------------------------------------------------


7. SAME UNIT INSIDE A SUBPLOT

One subplot may contain:

Input Voltage

Output Voltage


Another may contain:

Input Current

Output Current


------------------------------------------------------------


8. AUTOMATIC SUBPLOTS

Store information in a dictionary:

subplot_data = {

    "Voltage": {
        "values": voltage,
        "ylabel": "Voltage [V]"
    },

    "Current": {
        "values": current,
        "ylabel": "Current [A]"
    }

}


Then loop through the structure.


------------------------------------------------------------


9. REMOVE UNUSED AXES

fig.delaxes(
    unused_ax
)


Useful when the subplot grid contains more panels than
available datasets.


------------------------------------------------------------


10. FIGURE TITLE

fig.suptitle(
    "Engineering Measurement Results"
)


------------------------------------------------------------


11. GLOBAL LABELS

fig.supxlabel(
    "Time [ms]"
)

fig.supylabel(
    "Voltage [V]"
)


Use global Y labels only when subplot Y variables share
the same physical quantity.


------------------------------------------------------------


12. SAVE FIGURE

fig.savefig(
    "subplots.png",
    dpi=300,
    bbox_inches="tight"
)


------------------------------------------------------------


13. WHEN SUBPLOTS ARE USEFUL

- Voltage / Current / Temperature
- Input / Output measurements
- Several converter waveforms
- Simulation variables
- Experimental channels
- Signal-processing results
- Machine-learning diagnostics
- Multiple engineering metrics


------------------------------------------------------------


14. IMPORTANT PRINCIPLE

Subplots should improve interpretation.

Do not create multiple panels simply because the data
contain many columns.


Each panel should contribute to the scientific question.


------------------------------------------------------------


15. PRACTICAL DECISION

Same units
    ↓
Multiple lines may work

Different units
    ↓
Subplots are often clearer

Two different units only
    ↓
Dual Y-axis may sometimes be appropriate

Many different variables
    ↓
Subplots / separate figures


------------------------------------------------------------


NEXT:

08_plot_from_csv.py


This will begin one of the most practical parts of this
repository:

CSV File
   ↓
Pandas
   ↓
Inspect Columns
   ↓
Choose X
   ↓
Choose Y
   ↓
Plot
   ↓
Multiple Columns
   ↓
Save Figure


We will use:

sample_data/voltage_current.csv

so the example can be executed directly after cloning
the repository.
"""
