"""
============================================================
Python for Engineering and Research
01 - Basic Line Plot
============================================================

Purpose:
    Introduce basic line plotting using Matplotlib and
    demonstrate how a line plot can be used to visualize
    engineering data.

Topics:
    1. What is a line plot?
    2. When should it be used?
    3. Required import
    4. X and Y variables
    5. Basic line plot
    6. Axis labels and units
    7. Title and grid
    8. Engineering example
    9. Plot customization
    10. Saving the figure
    11. Common mistakes
    12. Key takeaways

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT IS A LINE PLOT?
# ============================================================

"""
A line plot displays the relationship between two variables
by connecting data points with a continuous line.

General relationship:

        Y
        ↑
        |
        |       ●
        |     / 
        |   ●
        | /
        ●
        +--------------------→ X


The horizontal axis normally represents the independent
variable.

Examples:

Time
Frequency
Load
Temperature
Distance

The vertical axis normally represents the measured or
calculated dependent variable.

Examples:

Voltage
Current
Power
Efficiency
Magnitude
"""


# ============================================================
# 2. WHEN SHOULD A LINE PLOT BE USED?
# ============================================================

"""
Line plots are especially useful when the X variable has
a meaningful order or represents a continuous quantity.

Typical engineering examples:

Voltage vs Time

Current vs Time

Temperature vs Time

Efficiency vs Load

Power vs Time

Magnitude vs Frequency

Converter Output Voltage vs Load


A line plot is generally suitable when the objective is
to visualize:

- Trends
- Changes with time
- Continuous measurements
- Simulation responses
- Experimental responses
- Frequency-dependent behavior
"""


# ============================================================
# 3. REQUIRED IMPORT
# ============================================================

"""
Matplotlib is one of the most widely used plotting
libraries in scientific Python.

The pyplot module is conventionally imported as:

plt
"""

import matplotlib.pyplot as plt

from pathlib import Path


# ============================================================
# 4. SIMPLE DATASET
# ============================================================

"""
Consider a simple measurement containing:

Time [s]

and

Voltage [V]


Both lists must contain the same number of values because
each time value corresponds to one voltage value.
"""


time = [
    0,
    1,
    2,
    3,
    4,
    5
]


voltage = [
    0,
    18,
    32,
    42,
    47,
    48
]


# ============================================================
# 5. BASIC LINE PLOT
# ============================================================

"""
The simplest Matplotlib line plot is:

plt.plot(x, y)

where:

x = horizontal-axis data

y = vertical-axis data
"""


plt.figure()

plt.plot(
    time,
    voltage
)


plt.show()


# ============================================================
# 6. ADD AXIS LABELS
# ============================================================

"""
Scientific and engineering plots should clearly identify
both the variable and its physical unit.

Good:

Time [s]

Voltage [V]


Less useful:

X

Y
"""


plt.figure()

plt.plot(
    time,
    voltage
)


plt.xlabel(
    "Time [s]"
)

plt.ylabel(
    "Voltage [V]"
)


plt.show()


# ============================================================
# 7. ADD TITLE AND GRID
# ============================================================

"""
A title describes the purpose of the figure.

A grid can help the reader estimate numerical values.
"""


plt.figure()

plt.plot(
    time,
    voltage
)


plt.xlabel(
    "Time [s]"
)

plt.ylabel(
    "Voltage [V]"
)

plt.title(
    "Voltage vs Time"
)

plt.grid(
    True
)


plt.show()


# ============================================================
# 8. ENGINEERING EXAMPLE
# ============================================================

"""
Example:

Visualize the output-voltage response of a DC-DC converter
during startup.

The converter output voltage gradually approaches its
steady-state value.
"""


time_ms = [
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
]


output_voltage = [
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


# ============================================================
# 9. RECOMMENDED FIGURE STRUCTURE
# ============================================================

"""
For research and engineering scripts, the following
object-oriented Matplotlib structure is recommended:

fig, ax = plt.subplots()

Instead of relying entirely on:

plt.plot()
plt.xlabel()
plt.ylabel()

Using:

fig

and

ax

provides better control when figures become more complex.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    output_voltage
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Output Voltage [V]"
)

ax.set_title(
    "DC-DC Converter Startup Response"
)

ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 10. LINE CUSTOMIZATION
# ============================================================

"""
A line can be customized using parameters such as:

linewidth

linestyle

marker

markersize


Example:

linewidth=2

linestyle="-"

marker="o"


Common line styles:

"-"     Solid

"--"    Dashed

"-."    Dash-dot

":"     Dotted


Common markers:

"o"     Circle

"s"     Square

"^"     Triangle

"x"     Cross

"."     Point


Colors are intentionally not fixed in these examples so
Matplotlib can use its default plotting cycle.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    output_voltage,
    linewidth=2,
    marker="o",
    markersize=5,
    label="Output Voltage"
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Output Voltage [V]"
)

ax.set_title(
    "DC-DC Converter Startup Response"
)

ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 11. AXIS LIMITS
# ============================================================

"""
Axis limits can be specified when the region of interest
is known.

Example:

X axis:

0 to 10 ms

Y axis:

0 to 105 V


Axis limits should be selected carefully and should not
misrepresent the data.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    output_voltage,
    linewidth=2,
    marker="o",
    label="Output Voltage"
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Output Voltage [V]"
)

ax.set_title(
    "DC-DC Converter Startup Response"
)


ax.set_xlim(
    0,
    10
)

ax.set_ylim(
    0,
    105
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 12. SAVE FIGURE
# ============================================================

"""
Figures can be saved using:

fig.savefig()


Common formats:

PNG
PDF
SVG


For example:

figure.png

figure.pdf

figure.svg


PNG is a raster format.

PDF and SVG can preserve vector graphics, which is useful
for scientific documents and publications.
"""


# Create an output folder relative to this Python file.

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


# Create final figure

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    output_voltage,
    linewidth=2,
    marker="o",
    label="Output Voltage"
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Output Voltage [V]"
)

ax.set_title(
    "DC-DC Converter Startup Response"
)


ax.set_xlim(
    0,
    10
)

ax.set_ylim(
    0,
    105
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()


# ============================================================
# 13. SAVE AS PNG
# ============================================================

png_file = (
    output_folder
    / "basic_line_plot.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 14. SAVE AS PDF
# ============================================================

pdf_file = (
    output_folder
    / "basic_line_plot.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 15. SAVE AS SVG
# ============================================================

svg_file = (
    output_folder
    / "basic_line_plot.svg"
)


fig.savefig(
    svg_file,
    bbox_inches="tight"
)


print(
    "\n--- Figure Files Created ---"
)

print(
    "PNG:",
    png_file
)

print(
    "PDF:",
    pdf_file
)

print(
    "SVG:",
    svg_file
)


# Show the figure after saving it.

plt.show()


# ============================================================
# 16. IMPORTANT: SAVE BEFORE show()
# ============================================================

"""
A useful plotting sequence is:

1. Create figure

2. Plot data

3. Add labels

4. Format figure

5. Save figure

6. Display figure


Example:

fig.savefig(
    "figure.png",
    dpi=300
)

plt.show()


Saving before plt.show() is a safe practice because some
environments may close or clear the figure after display.
"""


# ============================================================
# 17. USING sample_data
# ============================================================

"""
This repository also contains:

sample_data/voltage_current.csv


That dataset will be used in a later example:

08_plot_from_csv.py


The purpose of the current file is first to understand how
a line plot works when X and Y values are already available.

The learning progression is therefore:

Manual Python Data
        ↓
Basic Line Plot
        ↓
CSV Data
        ↓
Pandas
        ↓
Automatic Column Selection
        ↓
Scientific Plot
"""


# ============================================================
# 18. COMMON MISTAKE - UNEQUAL DATA LENGTH
# ============================================================

"""
Incorrect:

time = [
    0,
    1,
    2
]

voltage = [
    10,
    20
]


plt.plot(
    time,
    voltage
)


The X and Y datasets must normally have equal lengths.

Correct:

time = [
    0,
    1,
    2
]

voltage = [
    10,
    20,
    30
]
"""


# ============================================================
# 19. COMMON MISTAKE - MISSING UNITS
# ============================================================

"""
Avoid:

ax.set_xlabel(
    "Time"
)

ax.set_ylabel(
    "Voltage"
)


Prefer:

ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


Physical units are especially important in engineering
and scientific figures.
"""


# ============================================================
# 20. COMMON MISTAKE - WRONG X AND Y ORDER
# ============================================================

"""
Remember:

ax.plot(
    x,
    y
)


For:

Voltage vs Time


Time belongs on the X-axis.

Voltage belongs on the Y-axis.


Correct:

ax.plot(
    time,
    voltage
)


Incorrect interpretation:

ax.plot(
    voltage,
    time
)
"""


# ============================================================
# 21. COMMON MISTAKE - TOO MANY DECORATIONS
# ============================================================

"""
Scientific plots should prioritize clarity.

Avoid unnecessary:

- Large titles
- Excessive markers
- Decorative effects
- Heavy grids
- Unnecessary annotations

The data should remain the main focus of the figure.
"""


# ============================================================
# 22. BASIC PLOTTING PIPELINE
# ============================================================

"""
Data
 ↓
Choose X Variable
 ↓
Choose Y Variable
 ↓
Create Figure
 ↓
Plot X vs Y
 ↓
Add Axis Labels
 ↓
Add Units
 ↓
Add Grid if Useful
 ↓
Set Limits if Required
 ↓
Add Legend if Required
 ↓
Apply tight_layout()
 ↓
Save Figure
 ↓
Display Figure
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
BASIC LINE PLOT


1. IMPORT MATPLOTLIB

import matplotlib.pyplot as plt


------------------------------------------------------------


2. CREATE DATA

x = [
    0,
    1,
    2,
    3
]

y = [
    0,
    10,
    20,
    30
]


------------------------------------------------------------


3. SIMPLE PLOT

plt.plot(
    x,
    y
)

plt.show()


------------------------------------------------------------


4. RECOMMENDED STRUCTURE

fig, ax = plt.subplots()


ax.plot(
    x,
    y
)


ax.set_xlabel(
    "X Variable [unit]"
)

ax.set_ylabel(
    "Y Variable [unit]"
)


plt.tight_layout()

plt.show()


------------------------------------------------------------


5. ENGINEERING EXAMPLE

Time [ms]
     ↓
Output Voltage [V]


ax.plot(
    time_ms,
    output_voltage
)


------------------------------------------------------------


6. SAVE FIGURE

fig.savefig(
    "figure.png",
    dpi=300,
    bbox_inches="tight"
)


------------------------------------------------------------


7. LINE PLOTS ARE USEFUL FOR

- Time-series data
- Voltage waveforms
- Current waveforms
- Temperature trends
- Converter responses
- Efficiency curves
- Frequency-dependent measurements
- Simulation outputs
- Experimental measurements


------------------------------------------------------------


8. EVERY SCIENTIFIC PLOT SHOULD CONSIDER

X variable

Y variable

Physical units

Axis labels

Appropriate limits

Readable formatting

Legend when necessary

Correct interpretation


------------------------------------------------------------


9. CORE WORKFLOW

Data
 ↓
Plot
 ↓
Label
 ↓
Format
 ↓
Validate
 ↓
Save
 ↓
Interpret


------------------------------------------------------------


NEXT:

02_multiple_line_plots.py

will extend the same concept from:

ONE Y VARIABLE

to:

TWO
THREE
OR MANY

variables/cases on the same figure.
"""
