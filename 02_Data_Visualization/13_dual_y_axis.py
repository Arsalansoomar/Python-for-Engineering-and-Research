"""
============================================================
Python for Engineering and Research
13 - Dual Y-Axis Plot
============================================================

Purpose:
    Demonstrate how two engineering variables with different
    physical units can be plotted against the same X-axis
    using Matplotlib.

Topics:
    1. What is a dual Y-axis plot?
    2. When should it be used?
    3. When should it NOT be used?
    4. Required imports
    5. Basic twinx() example
    6. Voltage and Current
    7. Efficiency and Temperature
    8. Independent axis limits
    9. Line styles and markers
    10. Combined legends
    11. Reference limits
    12. Data from Excel
    13. Dual axis vs subplots
    14. Reusable plotting function
    15. Saving figures
    16. Common mistakes
    17. Key takeaways

Sample File:
    sample_data/converter_measurements.xlsx

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT IS A DUAL Y-AXIS PLOT?
# ============================================================

"""
A dual Y-axis plot uses:

ONE X-axis

but:

TWO independent Y-axes


Example:

Temperature [°C]                 Efficiency [%]
       ↑                               ↑
       │                               │
       │                               │
       └──────── Load [%] ─────────────┘


Typical structure:

             Left Y-axis
                  ↑
                  │
                  │
X-axis ───────────┼──────────→
                  │
                  │
                  ↓
             Right Y-axis


In Matplotlib, the second Y-axis is commonly created using:

ax.twinx()
"""


# ============================================================
# 2. WHEN SHOULD A DUAL Y-AXIS PLOT BE USED?
# ============================================================

"""
A dual Y-axis plot may be useful when:

- Two variables share the same X-axis
- The variables have different physical units
- Their relationship is important
- Direct visual comparison is useful
- Only a small number of variables are involved


Engineering examples:

Voltage [V]
and
Current [A]
vs
Time [s]


Efficiency [%]
and
Temperature [°C]
vs
Load [%]


Output Power [W]
and
Temperature [°C]
vs
Load [%]


Speed [rpm]
and
Torque [N·m]
vs
Time [s]
"""


# ============================================================
# 3. WHEN SHOULD IT NOT BE USED?
# ============================================================

"""
Dual Y-axis plots should be used carefully.

They may become misleading when:

- Axis limits are manipulated to create an apparent trend
- Too many variables are displayed
- The variables have no meaningful relationship
- The scales make unrelated curves look correlated
- The reader cannot easily determine which axis belongs
  to which variable


In many situations:

SUBPLOTS

are scientifically clearer.


Dual axis:

Best for focused comparison of TWO related variables.


Subplots:

Often better for three or more variables.
"""


# ============================================================
# 4. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pathlib import Path


# ============================================================
# 5. BASIC EXAMPLE DATA
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


voltage = np.array(
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


current = np.array(
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


# ============================================================
# 6. BASIC DUAL Y-AXIS PLOT
# ============================================================

"""
Step 1:

Create the first axis.

fig, ax1 = plt.subplots()


Step 2:

Create a second Y-axis sharing the same X-axis.

ax2 = ax1.twinx()
"""


fig, ax1 = plt.subplots(
    figsize=(7, 4.5)
)


ax2 = ax1.twinx()


# Plot voltage on the left Y-axis

line_voltage = ax1.plot(
    time_ms,
    voltage,
    linewidth=2,
    label="Voltage"
)


# Plot current on the right Y-axis

line_current = ax2.plot(
    time_ms,
    current,
    linestyle="--",
    linewidth=2,
    label="Current"
)


# X-axis

ax1.set_xlabel(
    "Time [ms]"
)


# Left Y-axis

ax1.set_ylabel(
    "Voltage [V]"
)


# Right Y-axis

ax2.set_ylabel(
    "Current [A]"
)


ax1.set_title(
    "Voltage and Current vs Time"
)


ax1.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 7. UNDERSTANDING ax1 AND ax2
# ============================================================

"""
ax1:

Controls:

X-axis

Left Y-axis

Voltage


ax2:

Controls:

Right Y-axis

Current


Both share:

The same X-axis


Therefore:

ax1.set_xlabel(...)

is normally sufficient.
"""


# ============================================================
# 8. INDEPENDENT Y-AXIS LIMITS
# ============================================================

"""
Each Y-axis has independent limits.

Voltage:

0 to 105 V


Current:

0 to 3 A
"""


fig, ax1 = plt.subplots(
    figsize=(7, 4.5)
)


ax2 = ax1.twinx()


ax1.plot(
    time_ms,
    voltage,
    linewidth=2,
    label="Voltage"
)


ax2.plot(
    time_ms,
    current,
    linestyle="--",
    linewidth=2,
    label="Current"
)


ax1.set_xlabel(
    "Time [ms]"
)


ax1.set_ylabel(
    "Voltage [V]"
)


ax2.set_ylabel(
    "Current [A]"
)


ax1.set_ylim(
    0,
    105
)


ax2.set_ylim(
    0,
    3
)


ax1.set_title(
    "Converter Voltage and Current"
)


ax1.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 9. IMPORTANT NOTE ABOUT AXIS LIMITS
# ============================================================

"""
Dual Y-axis plots can become misleading if axis limits are
selected only to make two curves appear similar.

For example:

Changing:

Voltage axis:
0 to 100

and:

Current axis:
0 to 2.5


may visually align two curves even when the apparent
relationship is partly caused by axis scaling.


Therefore axis limits should be based on:

- Physical meaning
- Data range
- Engineering limits
- Consistent comparison requirements

rather than visual convenience.
"""


# ============================================================
# 10. ADD MARKERS AND DIFFERENT LINE STYLES
# ============================================================

"""
Different line styles help distinguish the variables.

This is especially useful when figures are printed in
grayscale.
"""


fig, ax1 = plt.subplots(
    figsize=(7, 4.5)
)


ax2 = ax1.twinx()


line1 = ax1.plot(
    time_ms,
    voltage,
    marker="o",
    linewidth=2,
    label="Voltage"
)


line2 = ax2.plot(
    time_ms,
    current,
    marker="s",
    linestyle="--",
    linewidth=2,
    label="Current"
)


ax1.set_xlabel(
    "Time [ms]"
)


ax1.set_ylabel(
    "Voltage [V]"
)


ax2.set_ylabel(
    "Current [A]"
)


ax1.set_title(
    "Voltage and Current"
)


ax1.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 11. LEGEND PROBLEM WITH twinx()
# ============================================================

"""
ax1 and ax2 are separate axes.

Therefore:

ax1.legend()

only knows about lines plotted on ax1.


Likewise:

ax2.legend()

only knows about lines plotted on ax2.


To create ONE combined legend, the line objects from both
axes must be combined.
"""


# ============================================================
# 12. COMBINED LEGEND
# ============================================================

fig, ax1 = plt.subplots(
    figsize=(7, 4.5)
)


ax2 = ax1.twinx()


line1 = ax1.plot(
    time_ms,
    voltage,
    marker="o",
    linewidth=2,
    label="Voltage"
)


line2 = ax2.plot(
    time_ms,
    current,
    marker="s",
    linestyle="--",
    linewidth=2,
    label="Current"
)


# Combine line objects

all_lines = (
    line1
    + line2
)


# Extract labels

all_labels = [

    line.get_label()

    for line in all_lines

]


ax1.legend(
    all_lines,
    all_labels
)


ax1.set_xlabel(
    "Time [ms]"
)


ax1.set_ylabel(
    "Voltage [V]"
)


ax2.set_ylabel(
    "Current [A]"
)


ax1.set_title(
    "Voltage and Current with Combined Legend"
)


ax1.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 13. ALTERNATIVE LEGEND METHOD
# ============================================================

"""
Another useful method is:

handles1, labels1 = ax1.get_legend_handles_labels()

handles2, labels2 = ax2.get_legend_handles_labels()


Then combine them.
"""


fig, ax1 = plt.subplots(
    figsize=(7, 4.5)
)


ax2 = ax1.twinx()


ax1.plot(
    time_ms,
    voltage,
    linewidth=2,
    label="Voltage"
)


ax2.plot(
    time_ms,
    current,
    linestyle="--",
    linewidth=2,
    label="Current"
)


handles1, labels1 = (
    ax1.get_legend_handles_labels()
)


handles2, labels2 = (
    ax2.get_legend_handles_labels()
)


ax1.legend(

    handles1
    + handles2,

    labels1
    + labels2

)


ax1.set_xlabel(
    "Time [ms]"
)


ax1.set_ylabel(
    "Voltage [V]"
)


ax2.set_ylabel(
    "Current [A]"
)


ax1.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 14. ENGINEERING EXAMPLE - EFFICIENCY AND TEMPERATURE
# ============================================================

"""
A common engineering application:

Load [%]

vs

Efficiency [%]

and

Temperature [°C]
"""


load_percent = np.array(
    [
        10,
        20,
        30,
        40,
        50,
        60,
        70,
        80,
        90,
        100
    ]
)


efficiency = np.array(
    [
        88.5,
        91.0,
        92.8,
        94.0,
        94.8,
        95.3,
        95.6,
        95.5,
        95.2,
        94.8
    ]
)


temperature = np.array(
    [
        34,
        38,
        42,
        47,
        52,
        58,
        63,
        68,
        72,
        76
    ]
)


fig, ax1 = plt.subplots(
    figsize=(7, 4.5)
)


ax2 = ax1.twinx()


line1 = ax1.plot(
    load_percent,
    efficiency,
    marker="o",
    linewidth=2,
    label="Efficiency"
)


line2 = ax2.plot(
    load_percent,
    temperature,
    marker="s",
    linestyle="--",
    linewidth=2,
    label="Temperature"
)


ax1.set_xlabel(
    "Load [%]"
)


ax1.set_ylabel(
    "Efficiency [%]"
)


ax2.set_ylabel(
    "Temperature [°C]"
)


ax1.set_title(
    "Efficiency and Temperature vs Load"
)


ax1.grid(
    True
)


all_lines = (
    line1
    + line2
)


all_labels = [

    line.get_label()

    for line in all_lines

]


ax1.legend(
    all_lines,
    all_labels
)


plt.tight_layout()

plt.show()


# ============================================================
# 15. ENGINEERING LIMIT ON SECOND AXIS
# ============================================================

"""
Suppose the device temperature limit is:

80 °C


Because temperature belongs to ax2, the reference line
should also be added to ax2.
"""


temperature_limit = 80


fig, ax1 = plt.subplots(
    figsize=(7, 4.5)
)


ax2 = ax1.twinx()


line1 = ax1.plot(
    load_percent,
    efficiency,
    marker="o",
    linewidth=2,
    label="Efficiency"
)


line2 = ax2.plot(
    load_percent,
    temperature,
    marker="s",
    linestyle="--",
    linewidth=2,
    label="Temperature"
)


limit_line = ax2.axhline(
    y=temperature_limit,
    linestyle=":",
    linewidth=1.5,
    label="Temperature Limit"
)


ax1.set_xlabel(
    "Load [%]"
)


ax1.set_ylabel(
    "Efficiency [%]"
)


ax2.set_ylabel(
    "Temperature [°C]"
)


ax1.set_title(
    "Efficiency and Temperature with Limit"
)


ax1.grid(
    True
)


# Combine all legend entries

handles1, labels1 = (
    ax1.get_legend_handles_labels()
)


handles2, labels2 = (
    ax2.get_legend_handles_labels()
)


ax1.legend(

    handles1
    + handles2,

    labels1
    + labels2

)


plt.tight_layout()

plt.show()


# ============================================================
# 16. POWER AND TEMPERATURE EXAMPLE
# ============================================================

output_power = np.array(
    [
        25,
        50,
        75,
        100,
        125,
        150,
        175,
        200,
        225,
        250
    ]
)


device_temperature = np.array(
    [
        32,
        36,
        40,
        45,
        50,
        56,
        62,
        67,
        72,
        78
    ]
)


fig, ax1 = plt.subplots(
    figsize=(7, 4.5)
)


ax2 = ax1.twinx()


line1 = ax1.plot(
    load_percent,
    output_power,
    linewidth=2,
    marker="o",
    label="Output Power"
)


line2 = ax2.plot(
    load_percent,
    device_temperature,
    linewidth=2,
    linestyle="--",
    marker="s",
    label="Temperature"
)


ax1.set_xlabel(
    "Load [%]"
)


ax1.set_ylabel(
    "Output Power [W]"
)


ax2.set_ylabel(
    "Temperature [°C]"
)


ax1.set_title(
    "Output Power and Temperature"
)


ax1.grid(
    True
)


ax1.legend(
    line1 + line2,
    [
        line.get_label()
        for line in line1 + line2
    ]
)


plt.tight_layout()

plt.show()


# ============================================================
# 17. DUAL Y-AXIS USING EXCEL DATA
# ============================================================

"""
Now use the sample Excel workbook:

sample_data/converter_measurements.xlsx


Worksheet:

Load_Sweep


Columns include:

Load_percent

Efficiency_percent

Temperature_C
"""


script_folder = Path(
    __file__
).resolve().parent


excel_file = (
    script_folder
    / "sample_data"
    / "converter_measurements.xlsx"
)


# ============================================================
# 18. CHECK EXCEL FILE
# ============================================================

if not excel_file.exists():

    raise FileNotFoundError(
        f"\nExcel file not found:\n"
        f"{excel_file}"
    )


# ============================================================
# 19. READ LOAD-SWEEP DATA
# ============================================================

load_data = pd.read_excel(

    excel_file,

    sheet_name="Load_Sweep"

)


print(
    "\n--- Load Sweep Columns ---"
)


print(
    load_data.columns.tolist()
)


# ============================================================
# 20. PLOT EXCEL DATA WITH TWO Y-AXES
# ============================================================

fig, ax1 = plt.subplots(
    figsize=(7, 4.5)
)


ax2 = ax1.twinx()


line1 = ax1.plot(

    load_data[
        "Load_percent"
    ],

    load_data[
        "Efficiency_percent"
    ],

    marker="o",

    linewidth=2,

    label="Efficiency"

)


line2 = ax2.plot(

    load_data[
        "Load_percent"
    ],

    load_data[
        "Temperature_C"
    ],

    marker="s",

    linestyle="--",

    linewidth=2,

    label="Temperature"

)


ax1.set_xlabel(
    "Load [%]"
)


ax1.set_ylabel(
    "Efficiency [%]"
)


ax2.set_ylabel(
    "Temperature [°C]"
)


ax1.set_title(
    "Converter Performance from Excel"
)


ax1.grid(
    True
)


all_lines = (
    line1
    + line2
)


all_labels = [

    line.get_label()

    for line in all_lines

]


ax1.legend(
    all_lines,
    all_labels
)


plt.tight_layout()

plt.show()


# ============================================================
# 21. DUAL AXIS VS SUBPLOTS
# ============================================================

"""
The same data can also be displayed using subplots.

This is often easier to interpret.
"""


fig, axes = plt.subplots(
    2,
    1,
    figsize=(7, 6),
    sharex=True
)


axes[0].plot(
    load_percent,
    efficiency,
    marker="o",
    linewidth=2
)


axes[0].set_ylabel(
    "Efficiency [%]"
)


axes[0].grid(
    True
)


axes[1].plot(
    load_percent,
    temperature,
    marker="s",
    linewidth=2
)


axes[1].set_xlabel(
    "Load [%]"
)


axes[1].set_ylabel(
    "Temperature [°C]"
)


axes[1].grid(
    True
)


fig.suptitle(
    "Efficiency and Temperature Using Subplots"
)


plt.tight_layout()

plt.show()


# ============================================================
# 22. WHICH APPROACH SHOULD I USE?
# ============================================================

"""
DUAL Y-AXIS

Useful when:

- Exactly two variables are important
- They share the same X-axis
- Direct relationship is important
- The figure must remain compact


Example:

Efficiency + Temperature vs Load


------------------------------------------------------------


SUBPLOTS

Often better when:

- Variables require independent visual interpretation
- More than two variables exist
- Axis scaling may create confusion
- Publication clarity is more important than compactness


Example:

Voltage
Current
Power
Temperature

vs Time
"""


# ============================================================
# 23. THREE Y-AXES?
# ============================================================

"""
Matplotlib can technically create more than two Y-axes.

However, this is normally NOT recommended for basic
scientific figures.

Example:

Voltage
Current
Temperature
Power

all using separate Y-axes

can become difficult to interpret.


Prefer:

Subplots

for three or more different physical quantities.
"""


# ============================================================
# 24. REUSABLE DUAL-AXIS FUNCTION
# ============================================================

def plot_dual_y_axis(
    x,
    y1,
    y2,
    x_label,
    y1_label,
    y2_label,
    y1_name,
    y2_name,
    title
):
    """
    Create a dual Y-axis plot.

    Parameters
    ----------
    x : array-like
        Shared X-axis data.

    y1 : array-like
        Left Y-axis data.

    y2 : array-like
        Right Y-axis data.

    x_label : str
        X-axis label.

    y1_label : str
        Left Y-axis label.

    y2_label : str
        Right Y-axis label.

    y1_name : str
        Legend name for first variable.

    y2_name : str
        Legend name for second variable.

    title : str
        Figure title.

    Returns
    -------
    fig, ax1, ax2
        Matplotlib figure and axes.
    """

    if not (
        len(x)
        == len(y1)
        == len(y2)
    ):

        raise ValueError(
            "x, y1 and y2 must contain "
            "the same number of observations."
        )


    fig, ax1 = plt.subplots(
        figsize=(7, 4.5)
    )


    ax2 = ax1.twinx()


    line1 = ax1.plot(
        x,
        y1,
        marker="o",
        linewidth=2,
        label=y1_name
    )


    line2 = ax2.plot(
        x,
        y2,
        marker="s",
        linestyle="--",
        linewidth=2,
        label=y2_name
    )


    ax1.set_xlabel(
        x_label
    )


    ax1.set_ylabel(
        y1_label
    )


    ax2.set_ylabel(
        y2_label
    )


    ax1.set_title(
        title
    )


    ax1.grid(
        True
    )


    lines = (
        line1
        + line2
    )


    labels = [

        line.get_label()

        for line in lines

    ]


    ax1.legend(
        lines,
        labels
    )


    plt.tight_layout()


    return (
        fig,
        ax1,
        ax2
    )


# ============================================================
# 25. USE REUSABLE FUNCTION
# ============================================================

fig, ax1, ax2 = plot_dual_y_axis(

    x=load_percent,

    y1=efficiency,

    y2=temperature,

    x_label="Load [%]",

    y1_label="Efficiency [%]",

    y2_label="Temperature [°C]",

    y1_name="Efficiency",

    y2_name="Temperature",

    title="Converter Efficiency and Temperature"

)


plt.show()


# ============================================================
# 26. SET AXIS LIMITS AFTER FUNCTION CALL
# ============================================================

"""
Because the function returns:

ax1

and

ax2


the user can still customize the axes afterwards.
"""


fig, ax1, ax2 = plot_dual_y_axis(

    x=load_percent,

    y1=efficiency,

    y2=temperature,

    x_label="Load [%]",

    y1_label="Efficiency [%]",

    y2_label="Temperature [°C]",

    y1_name="Efficiency",

    y2_name="Temperature",

    title="Converter Performance"

)


ax1.set_xlim(
    10,
    100
)


ax1.set_ylim(
    85,
    100
)


ax2.set_ylim(
    30,
    85
)


plt.show()


# ============================================================
# 27. SECONDARY AXIS VS twinx()
# ============================================================

"""
Do not confuse:

twinx()

with:

secondary_yaxis()


twinx():

Used when displaying TWO DIFFERENT VARIABLES.

Example:

Efficiency [%]
and
Temperature [°C]


------------------------------------------------------------


secondary_yaxis():

Often used when displaying the SAME physical quantity
using another unit or mathematical transformation.


Example:

Temperature [°C]

and

Temperature [°F]


These are conceptually different use cases.
"""


# ============================================================
# 28. UNIT-CONVERSION SECONDARY AXIS EXAMPLE
# ============================================================

"""
For completeness:

Suppose the primary Y-axis is temperature in °C and we
want the same temperature scale in °F.

Conversion:

°F = °C × 9/5 + 32


Inverse:

°C = (°F - 32) × 5/9
"""


def celsius_to_fahrenheit(
    temperature_c
):

    return (
        temperature_c
        * 9 / 5
        + 32
    )


def fahrenheit_to_celsius(
    temperature_f
):

    return (
        temperature_f
        - 32
    ) * 5 / 9


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    temperature,
    marker="o"
)


ax.set_xlabel(
    "Load [%]"
)


ax.set_ylabel(
    "Temperature [°C]"
)


secondary_axis = ax.secondary_yaxis(

    "right",

    functions=(
        celsius_to_fahrenheit,
        fahrenheit_to_celsius
    )

)


secondary_axis.set_ylabel(
    "Temperature [°F]"
)


ax.set_title(
    "Temperature with Celsius and Fahrenheit Scales"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 29. SAVE FINAL DUAL-AXIS FIGURE
# ============================================================

output_figure_folder = (
    script_folder
    / "output_figures"
)


output_figure_folder.mkdir(
    exist_ok=True
)


fig, ax1 = plt.subplots(
    figsize=(7, 4.5)
)


ax2 = ax1.twinx()


line1 = ax1.plot(

    load_data[
        "Load_percent"
    ],

    load_data[
        "Efficiency_percent"
    ],

    marker="o",

    linewidth=2,

    label="Efficiency"

)


line2 = ax2.plot(

    load_data[
        "Load_percent"
    ],

    load_data[
        "Temperature_C"
    ],

    marker="s",

    linestyle="--",

    linewidth=2,

    label="Temperature"

)


ax1.set_xlabel(
    "Load [%]"
)


ax1.set_ylabel(
    "Efficiency [%]"
)


ax2.set_ylabel(
    "Temperature [°C]"
)


ax1.set_title(
    "Converter Efficiency and Temperature"
)


ax1.grid(
    True
)


handles1, labels1 = (
    ax1.get_legend_handles_labels()
)


handles2, labels2 = (
    ax2.get_legend_handles_labels()
)


ax1.legend(

    handles1
    + handles2,

    labels1
    + labels2

)


plt.tight_layout()


# ============================================================
# 30. SAVE PNG
# ============================================================

png_file = (
    output_figure_folder
    / "dual_y_axis.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 31. SAVE PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "dual_y_axis.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 32. SAVE SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "dual_y_axis.svg"
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
# 33. COMMON MISTAKE - USING SAME AXIS FOR DIFFERENT UNITS
# ============================================================

"""
Avoid:

ax.plot(
    load,
    efficiency
)

ax.plot(
    load,
    temperature
)

ax.set_ylabel(
    "Efficiency / Temperature"
)


because:

Efficiency [%]

and

Temperature [°C]

are different physical quantities.


Use:

twinx()

or:

subplots.
"""


# ============================================================
# 34. COMMON MISTAKE - FORGETTING WHICH AXIS IS WHICH
# ============================================================

"""
Remember:

ax1

normally represents the LEFT Y-axis.


ax2 = ax1.twinx()

normally represents the RIGHT Y-axis.


Therefore:

ax1.set_ylabel(
    "Efficiency [%]"
)


ax2.set_ylabel(
    "Temperature [°C]"
)
"""


# ============================================================
# 35. COMMON MISTAKE - WRONG REFERENCE AXIS
# ============================================================

"""
Suppose:

Temperature Limit = 80 °C


Temperature is plotted using:

ax2


Then the reference line should also use:

ax2.axhline(
    y=80
)


not:

ax1.axhline(
    y=80
)


because the numerical Y scales are different.
"""


# ============================================================
# 36. COMMON MISTAKE - TWO SEPARATE LEGENDS
# ============================================================

"""
Using:

ax1.legend()

and:

ax2.legend()

may produce two separate legend boxes.


A cleaner approach is often to combine:

handles1 + handles2

and:

labels1 + labels2
"""


# ============================================================
# 37. COMMON MISTAKE - MANIPULATING AXIS LIMITS
# ============================================================

"""
Dual-axis plots are particularly vulnerable to misleading
scale choices.

Two unrelated datasets can be made to appear strongly
correlated simply by adjusting both Y-axis ranges.

Therefore:

Do not choose axis limits only to force visual alignment.
"""


# ============================================================
# 38. COMMON MISTAKE - THREE OR MORE Y-AXES
# ============================================================

"""
Avoid unnecessarily creating:

Left Y-axis

Right Y-axis 1

Right Y-axis 2

Right Y-axis 3


For several different physical variables:

Use subplots.
"""


# ============================================================
# 39. COMMON MISTAKE - ASSUMING VISUAL CORRELATION
# ============================================================

"""
Suppose:

Efficiency increases

and

Temperature increases


because both curves appear to move upward, this does NOT
automatically prove:

Temperature causes higher efficiency.


Scientific interpretation may require:

Correlation analysis

Physical modeling

Controlled experiments

Statistical validation
"""


# ============================================================
# 40. COMMON MISTAKE - NO UNITS
# ============================================================

"""
Avoid:

Left Y-axis:

Efficiency


Right Y-axis:

Temperature


Prefer:

Efficiency [%]

Temperature [°C]
"""


# ============================================================
# 41. DUAL Y-AXIS DECISION WORKFLOW
# ============================================================

"""
Two Variables
      ↓
Same X-axis?
     / \
   Yes  No
   ↓     ↓
Continue   Separate figures
   ↓
Same physical unit?
     / \
   Yes  No
   ↓     ↓
Same axis   Are exactly two
may work    related variables?
              / \
            Yes  No
            ↓     ↓
         Dual Axis   Subplots
            ↓
Check:
Units
Scales
Limits
Legend
Interpretability
            ↓
Plot
"""


# ============================================================
# 42. PRACTICAL ENGINEERING DECISIONS
# ============================================================

"""
CASE 1

Input Voltage [V]

Output Voltage [V]

vs Time


Use:

ONE Y-AXIS

because both are voltage.


------------------------------------------------------------


CASE 2

Voltage [V]

Current [A]

vs Time


Possible:

DUAL Y-AXIS


------------------------------------------------------------


CASE 3

Efficiency [%]

Temperature [°C]

vs Load


Possible:

DUAL Y-AXIS


------------------------------------------------------------


CASE 4

Voltage [V]

Current [A]

Power [W]

Temperature [°C]

vs Time


Prefer:

SUBPLOTS


------------------------------------------------------------


CASE 5

Temperature [°C]

Temperature [°F]


Use:

SECONDARY AXIS

because these are two representations of the SAME
physical quantity.
"""


# ============================================================
# 43. COMPLETE DUAL-AXIS WORKFLOW
# ============================================================

"""
Shared X Data
      ↓
Variable 1
Variable 2
      ↓
Check Physical Meaning
      ↓
Create ax1
      ↓
Create ax2 = ax1.twinx()
      ↓
Plot Variable 1 on ax1
      ↓
Plot Variable 2 on ax2
      ↓
Set Separate Y Labels
      ↓
Check Independent Scales
      ↓
Combine Legend
      ↓
Check for Misleading Alignment
      ↓
Save Figure
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
DUAL Y-AXIS PLOTS


1. CREATE FIRST AXIS

fig, ax1 = plt.subplots()


------------------------------------------------------------


2. CREATE SECOND Y-AXIS

ax2 = ax1.twinx()


------------------------------------------------------------


3. FIRST VARIABLE

ax1.plot(
    x,
    y1
)


------------------------------------------------------------


4. SECOND VARIABLE

ax2.plot(
    x,
    y2
)


------------------------------------------------------------


5. SHARED X-AXIS

ax1.set_xlabel(
    "Load [%]"
)


------------------------------------------------------------


6. LEFT Y-AXIS

ax1.set_ylabel(
    "Efficiency [%]"
)


------------------------------------------------------------


7. RIGHT Y-AXIS

ax2.set_ylabel(
    "Temperature [°C]"
)


------------------------------------------------------------


8. INDEPENDENT LIMITS

ax1.set_ylim(
    85,
    100
)


ax2.set_ylim(
    30,
    85
)


------------------------------------------------------------


9. COMBINED LEGEND

handles1, labels1 = (
    ax1.get_legend_handles_labels()
)


handles2, labels2 = (
    ax2.get_legend_handles_labels()
)


ax1.legend(

    handles1
    + handles2,

    labels1
    + labels2

)


------------------------------------------------------------


10. ENGINEERING LIMIT

If Temperature belongs to ax2:

ax2.axhline(
    y=80
)


------------------------------------------------------------


11. GOOD APPLICATIONS

Voltage + Current vs Time

Efficiency + Temperature vs Load

Power + Temperature vs Load

Speed + Torque vs Time


------------------------------------------------------------


12. USE SUBPLOTS WHEN

Three or more variables are involved

Scales are difficult to interpret

The figure becomes crowded

Independent interpretation is important


------------------------------------------------------------


13. twinx() VS secondary_yaxis()

twinx():

Two DIFFERENT variables

Example:

Efficiency [%]
Temperature [°C]


secondary_yaxis():

Same physical quantity represented differently

Example:

Temperature [°C]
Temperature [°F]


------------------------------------------------------------


14. MOST IMPORTANT WARNING

Dual-axis plots can create misleading visual relationships
because each Y-axis has its own scale.

Always choose axis limits based on:

Data

Physics

Engineering requirements

and scientific clarity


not merely to make two curves visually align.


------------------------------------------------------------


15. DECISION SUMMARY

Same X + Same Units
        ↓
One Y-axis

Same X + Two Different Units
        ↓
Dual Y-axis may be useful

Same X + Several Different Units
        ↓
Subplots usually better


------------------------------------------------------------


NEXT:

14_logarithmic_axis.py


This will be particularly important for engineering and
research because it will cover:

Linear axis

Logarithmic X-axis

Logarithmic Y-axis

Log-log plots

semilogx()

semilogy()

loglog()

Frequency from 10 kHz to 30 MHz

FFT / EMI spectra

Frequency response

Positive-value requirement

Major and minor grid lines

Engineering frequency labels

When log scale should and should not be used
"""
