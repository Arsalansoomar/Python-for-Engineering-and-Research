"""
============================================================
Python for Engineering and Research
16 - Legends, Labels, and Annotations
============================================================

Purpose:
    Demonstrate how to clearly label engineering figures,
    create and customize legends, annotate important points,
    mark operating limits, identify peaks, and highlight
    important regions using Matplotlib.

Topics:
    1. Why labels and annotations matter
    2. Axis labels and engineering units
    3. Figure titles
    4. Basic legends
    5. Legend locations
    6. Multiple-column legends
    7. Custom legend names
    8. Legend formatting
    9. Text annotations
    10. Arrow annotations
    11. Horizontal reference lines
    12. Vertical reference lines
    13. Highlighted regions
    14. Engineering operating limits
    15. Automatic maximum detection
    16. Automatic minimum detection
    17. Frequency peak detection
    18. Multiple peak labels
    19. Text boxes
    20. Annotation placement
    21. Reusable annotation functions
    22. Saving figures
    23. Common mistakes
    24. Key takeaways

Sample File:
    sample_data/fft_example.csv

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHY LABELS AND ANNOTATIONS MATTER
# ============================================================

"""
A scientific figure should communicate its meaning without
requiring the reader to inspect the source code.

A useful engineering figure should normally make clear:

WHAT is plotted?

WHAT does the X-axis represent?

WHAT does the Y-axis represent?

WHAT are the units?

WHICH curve represents which case?

WHERE are the important operating points?

ARE any engineering limits exceeded?


A good figure therefore combines:

Data
 +
Labels
 +
Units
 +
Legend
 +
Important annotations
 +
Scientific interpretation
"""


# ============================================================
# 2. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pathlib import Path
from matplotlib.ticker import FuncFormatter


# ============================================================
# 3. BASIC ENGINEERING DATA
# ============================================================

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
    ],
    dtype=float
)


efficiency_baseline = np.array(
    [
        88.5,
        90.5,
        92.0,
        93.0,
        93.8,
        94.2,
        94.4,
        94.3,
        94.0,
        93.6
    ]
)


efficiency_design_a = np.array(
    [
        89.3,
        91.4,
        93.0,
        94.0,
        94.8,
        95.2,
        95.5,
        95.4,
        95.1,
        94.8
    ]
)


efficiency_design_b = np.array(
    [
        90.0,
        92.0,
        93.6,
        94.6,
        95.3,
        95.7,
        95.9,
        95.8,
        95.6,
        95.3
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
        73,
        78
    ]
)


# ============================================================
# 4. AXIS LABELS
# ============================================================

"""
A figure should normally include meaningful axis labels.

Good:

Load [%]

Efficiency [%]

Temperature [°C]

Voltage [V]

Current [A]

Frequency [Hz]


Less informative:

X

Y

Value

Result
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_a,
    marker="o"
)


ax.set_xlabel(
    "Load [%]"
)


ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 5. ENGINEERING UNITS
# ============================================================

"""
Always include units when the plotted quantity has a
physical unit.

Examples:

Voltage [V]

Current [A]

Power [W]

Energy [Wh]

Temperature [°C]

Frequency [Hz]

Magnitude [dBµV]


Dimensionless values may use:

Gain [-]

Normalized Value [-]


Do not write:

Voltage

when the reader needs to know whether the values are:

V

mV

kV
"""


# ============================================================
# 6. FIGURE TITLE
# ============================================================

"""
Use:

ax.set_title()


Titles are useful for:

Tutorials

Reports

Presentations

Exploratory analysis


In journal papers, the detailed explanation is often
provided by the figure caption instead, so a title inside
the plot may not always be necessary.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_a
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Converter Efficiency vs Load"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 7. BASIC LEGEND
# ============================================================

"""
A legend identifies different plotted datasets.

Each plotted line should first receive:

label=
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_baseline,
    marker="o",
    label="Baseline"
)


ax.plot(
    load_percent,
    efficiency_design_a,
    marker="s",
    label="Design A"
)


ax.plot(
    load_percent,
    efficiency_design_b,
    marker="^",
    label="Design B"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Converter Efficiency Comparison"
)


ax.grid(
    True
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 8. LEGEND LOCATION
# ============================================================

"""
Common legend locations include:

"best"

"upper right"

"upper left"

"lower right"

"lower left"

"center"

"center right"

"center left"


Example:

ax.legend(
    loc="lower right"
)
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_baseline,
    label="Baseline"
)


ax.plot(
    load_percent,
    efficiency_design_a,
    label="Design A"
)


ax.plot(
    load_percent,
    efficiency_design_b,
    label="Design B"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.legend(
    loc="lower right"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 9. loc="best"
# ============================================================

"""
Using:

loc="best"

allows Matplotlib to automatically choose a location that
attempts to minimize overlap with plotted data.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_baseline,
    label="Baseline"
)


ax.plot(
    load_percent,
    efficiency_design_a,
    label="Design A"
)


ax.legend(
    loc="best"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 10. MULTIPLE-COLUMN LEGEND
# ============================================================

"""
When several cases exist, the legend can use multiple
columns.

Use:

ncol=
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    load_percent,
    efficiency_baseline,
    label="Baseline"
)


ax.plot(
    load_percent,
    efficiency_design_a,
    label="Design A"
)


ax.plot(
    load_percent,
    efficiency_design_b,
    label="Design B"
)


ax.legend(
    ncol=3,
    loc="lower center"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 11. LEGEND OUTSIDE THE PLOT
# ============================================================

"""
Sometimes the legend covers important data.

It can be positioned outside the main plotting region using:

bbox_to_anchor=
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    load_percent,
    efficiency_baseline,
    label="Baseline"
)


ax.plot(
    load_percent,
    efficiency_design_a,
    label="Design A"
)


ax.plot(
    load_percent,
    efficiency_design_b,
    label="Design B"
)


ax.legend(
    loc="center left",
    bbox_to_anchor=(
        1.02,
        0.5
    )
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 12. CUSTOM LEGEND NAMES
# ============================================================

"""
Do not necessarily use raw programming variable names in a
final figure.

Raw data column:

Case_A_dBuV


Better legend label:

Case A


Raw data column:

Unshielded_dBuV


Better legend label:

Unshielded
"""


case_data = {

    "Baseline":
        efficiency_baseline,

    "Design A":
        efficiency_design_a,

    "Design B":
        efficiency_design_b

}


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, values in case_data.items():

    ax.plot(
        load_percent,
        values,
        linewidth=2,
        label=case_name
    )


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 13. LEGEND FRAME
# ============================================================

"""
Legend frame visibility can be controlled using:

frameon=
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, values in case_data.items():

    ax.plot(
        load_percent,
        values,
        label=case_name
    )


ax.legend(
    frameon=True
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 14. LEGEND TITLE
# ============================================================

"""
A legend can also have a title.

Example:

Case

Configuration

Material

Experiment
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, values in case_data.items():

    ax.plot(
        load_percent,
        values,
        label=case_name
    )


ax.legend(
    title="Configuration"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 15. SIMPLE TEXT ANNOTATION
# ============================================================

"""
Text can be placed inside a figure using:

ax.text()
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_b,
    marker="o"
)


ax.text(
    20,
    97,
    "High-efficiency region"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.set_ylim(
    88,
    100
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 16. TEXT POSITION USING AXIS COORDINATES
# ============================================================

"""
Instead of positioning text using data values, text can be
positioned relative to the plotting area.

Use:

transform=ax.transAxes


Coordinates:

(0, 0)

bottom-left


(1, 1)

top-right


(0.5, 0.5)

center
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_b
)


ax.text(
    0.05,
    0.90,
    "Experimental Case",
    transform=ax.transAxes
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 17. TEXT BOX
# ============================================================

"""
A text box can highlight important information.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_b,
    marker="o"
)


text_information = (
    "Operating Range\n"
    "Load: 10-100%\n"
    "Efficiency > 90%"
)


ax.text(

    0.05,

    0.80,

    text_information,

    transform=ax.transAxes,

    bbox={
        "boxstyle":
            "round",

        "alpha":
            0.8
    }

)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 18. ANNOTATE A SPECIFIC POINT
# ============================================================

"""
Use:

ax.annotate()


to connect text with a specific data point.
"""


selected_load = 70


selected_index = np.where(
    load_percent
    == selected_load
)[0][0]


selected_efficiency = (
    efficiency_design_b[
        selected_index
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_b,
    marker="o"
)


ax.annotate(

    (
        f"Load = "
        f"{selected_load:.0f}%\n"

        f"Efficiency = "
        f"{selected_efficiency:.1f}%"
    ),

    xy=(
        selected_load,
        selected_efficiency
    ),

    xytext=(
        20,
        -40
    ),

    textcoords="offset points",

    arrowprops={
        "arrowstyle":
            "->"
    }

)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show())


# ============================================================
# 19. AUTOMATIC MAXIMUM VALUE
# ============================================================

"""
Instead of manually selecting an important point, Python
can automatically find the maximum.

NumPy:

np.argmax()

returns the index of the maximum value.
"""


maximum_index = np.argmax(
    efficiency_design_b
)


maximum_efficiency = (
    efficiency_design_b[
        maximum_index
    ]
)


maximum_efficiency_load = (
    load_percent[
        maximum_index
    ]
)


print(
    "\n--- Maximum Efficiency ---"
)


print(
    "Load:",
    maximum_efficiency_load,
    "%"
)


print(
    "Efficiency:",
    maximum_efficiency,
    "%"
)


# ============================================================
# 20. ANNOTATE AUTOMATIC MAXIMUM
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_b,
    marker="o",
    label="Design B"
)


ax.scatter(
    maximum_efficiency_load,
    maximum_efficiency,
    s=70,
    label="Maximum"
)


ax.annotate(

    (
        f"Maximum\n"
        f"{maximum_efficiency:.1f}% "
        f"at "
        f"{maximum_efficiency_load:.0f}% load"
    ),

    xy=(
        maximum_efficiency_load,
        maximum_efficiency
    ),

    xytext=(
        -90,
        -45
    ),

    textcoords="offset points",

    arrowprops={
        "arrowstyle":
            "->"
    }

)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 21. AUTOMATIC MINIMUM
# ============================================================

"""
Use:

np.argmin()

to locate the minimum value.
"""


minimum_index = np.argmin(
    efficiency_design_b
)


minimum_efficiency = (
    efficiency_design_b[
        minimum_index
    ]
)


minimum_efficiency_load = (
    load_percent[
        minimum_index
    ]
)


print(
    "\n--- Minimum Efficiency ---"
)


print(
    "Load:",
    minimum_efficiency_load,
    "%"
)


print(
    "Efficiency:",
    minimum_efficiency,
    "%"
)


# ============================================================
# 22. HORIZONTAL REFERENCE LINE
# ============================================================

"""
Engineering limits are often represented using:

ax.axhline()


Examples:

Temperature limit

Voltage limit

Efficiency target

EMI limit

Maximum allowed current
"""


efficiency_target = 95


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_b,
    marker="o",
    label="Efficiency"
)


ax.axhline(
    y=efficiency_target,
    linestyle="--",
    linewidth=1.5,
    label="95% Target"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 23. TEMPERATURE LIMIT
# ============================================================

temperature_limit = 80


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    temperature,
    marker="o",
    label="Temperature"
)


ax.axhline(
    y=temperature_limit,
    linestyle="--",
    label="Temperature Limit"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Temperature [°C]"
)


ax.set_ylim(
    20,
    90
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 24. VERTICAL REFERENCE LINE
# ============================================================

"""
Use:

ax.axvline()


to mark important X-axis locations.

Examples:

Switching event

Nominal frequency

Resonance

Full-load operating point

Trigger position
"""


nominal_load = 80


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_b
)


ax.axvline(
    x=nominal_load,
    linestyle="--",
    label="Nominal Operating Point"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 25. HIGHLIGHT X-AXIS REGION
# ============================================================

"""
Use:

ax.axvspan()


to highlight a range on the X-axis.

Example:

Recommended operating range:

50% to 80% load
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_b,
    marker="o",
    label="Efficiency"
)


ax.axvspan(
    50,
    80,
    alpha=0.2,
    label="Preferred Operating Range"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 26. HIGHLIGHT Y-AXIS REGION
# ============================================================

"""
Use:

ax.axhspan()


to highlight a Y-axis range.

Example:

Efficiency above 95%
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_b,
    marker="o"
)


ax.axhspan(
    95,
    100,
    alpha=0.2
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.set_ylim(
    88,
    100
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 27. ANNOTATE ENGINEERING LIMIT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    temperature,
    marker="o"
)


ax.axhline(
    y=80,
    linestyle="--"
)


ax.text(
    15,
    81,
    "Maximum Recommended Temperature = 80 °C"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Temperature [°C]"
)


ax.set_ylim(
    20,
    90
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 28. LOAD FREQUENCY-DOMAIN DATA
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


print(
    "\n--- Frequency Data Columns ---"
)


print(
    fft_data.columns.tolist()
)


# ============================================================
# 29. FREQUENCY FORMATTER
# ============================================================

def format_frequency(
    value,
    position=None
):
    """
    Format frequency values using Hz, kHz, MHz, or GHz.
    """

    if value >= 1e9:

        return (
            f"{value / 1e9:g} GHz"
        )


    elif value >= 1e6:

        return (
            f"{value / 1e6:g} MHz"
        )


    elif value >= 1e3:

        return (
            f"{value / 1e3:g} kHz"
        )


    else:

        return (
            f"{value:g} Hz"
        )


# ============================================================
# 30. BASIC FREQUENCY-DOMAIN LEGEND
# ============================================================

frequency_cases = {

    "Unshielded":
        "Unshielded_dBuV",

    "Case A":
        "Case_A_dBuV",

    "Case B":
        "Case_B_dBuV",

    "Case C":
        "Case_C_dBuV"

}


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for case_name, column_name in frequency_cases.items():

    ax.plot(

        fft_data[
            "Frequency_Hz"
        ],

        fft_data[
            column_name
        ],

        linewidth=2,

        label=case_name

    )


ax.set_xscale(
    "log"
)


ax.set_xlim(
    10e3,
    30e6
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


ax.legend(
    ncol=2
)


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 31. AUTOMATIC FREQUENCY PEAK DETECTION
# ============================================================

"""
Suppose we want the largest magnitude in the Unshielded
case.

Pandas:

idxmax()

returns the index of the maximum value.
"""


peak_index = fft_data[
    "Unshielded_dBuV"
].idxmax()


peak_frequency = fft_data.loc[
    peak_index,
    "Frequency_Hz"
]


peak_magnitude = fft_data.loc[
    peak_index,
    "Unshielded_dBuV"
]


print(
    "\n--- Maximum Spectrum Point ---"
)


print(
    "Frequency:",
    format_frequency(
        peak_frequency
    )
)


print(
    f"Magnitude = "
    f"{peak_magnitude:.2f} dBµV"
)


# ============================================================
# 32. ANNOTATE FREQUENCY PEAK
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    fft_data["Frequency_Hz"],
    fft_data["Unshielded_dBuV"],
    linewidth=2,
    label="Unshielded"
)


ax.scatter(
    peak_frequency,
    peak_magnitude,
    s=70
)


ax.annotate(

    (
        f"Peak\n"
        f"{format_frequency(peak_frequency)}\n"
        f"{peak_magnitude:.1f} dBµV"
    ),

    xy=(
        peak_frequency,
        peak_magnitude
    ),

    xytext=(
        25,
        25
    ),

    textcoords="offset points",

    arrowprops={
        "arrowstyle":
            "->"
    }

)


ax.set_xscale(
    "log"
)


ax.set_xlim(
    10e3,
    30e6
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
# 33. FIND PEAK IN SELECTED FREQUENCY BAND
# ============================================================

"""
Sometimes the global maximum is not the quantity of
interest.

Example:

Find maximum magnitude only between:

100 kHz

and

10 MHz
"""


frequency_min = 100e3

frequency_max = 10e6


selected_band = fft_data[
    (
        fft_data[
            "Frequency_Hz"
        ] >= frequency_min
    )
    &
    (
        fft_data[
            "Frequency_Hz"
        ] <= frequency_max
    )
]


selected_peak_index = (
    selected_band[
        "Unshielded_dBuV"
    ]
    .idxmax()
)


selected_peak_frequency = (
    selected_band.loc[
        selected_peak_index,
        "Frequency_Hz"
    ]
)


selected_peak_magnitude = (
    selected_band.loc[
        selected_peak_index,
        "Unshielded_dBuV"
    ]
)


print(
    "\n--- Peak Between 100 kHz and 10 MHz ---"
)


print(
    "Frequency:",
    format_frequency(
        selected_peak_frequency
    )
)


print(
    f"Magnitude = "
    f"{selected_peak_magnitude:.2f} dBµV"
)


# ============================================================
# 34. ANNOTATE SELECTED-BAND PEAK
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    fft_data["Frequency_Hz"],
    fft_data["Unshielded_dBuV"],
    linewidth=2
)


ax.scatter(
    selected_peak_frequency,
    selected_peak_magnitude,
    s=70
)


ax.annotate(

    (
        f"Band Peak\n"
        f"{format_frequency(selected_peak_frequency)}\n"
        f"{selected_peak_magnitude:.1f} dBµV"
    ),

    xy=(
        selected_peak_frequency,
        selected_peak_magnitude
    ),

    xytext=(
        20,
        -50
    ),

    textcoords="offset points",

    arrowprops={
        "arrowstyle":
            "->"
    }

)


ax.set_xscale(
    "log"
)


ax.set_xlim(
    10e3,
    30e6
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


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 35. TOP THREE HIGHEST DATA POINTS
# ============================================================

"""
Pandas:

nlargest()


can find several high-value data points.

Important:

These are simply the largest sampled values.

They are not necessarily three independent physical peaks.

Formal peak detection will be covered later in the
Signal Processing section.
"""


top_three = fft_data.nlargest(
    3,
    "Unshielded_dBuV"
)


print(
    "\n--- Three Highest Spectrum Samples ---"
)


print(
    top_three[
        [
            "Frequency_Hz",
            "Unshielded_dBuV"
        ]
    ]
)


# ============================================================
# 36. ANNOTATE MULTIPLE HIGH POINTS
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    fft_data["Frequency_Hz"],
    fft_data["Unshielded_dBuV"],
    linewidth=2
)


for _, row in top_three.iterrows():

    frequency_value = row[
        "Frequency_Hz"
    ]


    magnitude_value = row[
        "Unshielded_dBuV"
    ]


    ax.scatter(
        frequency_value,
        magnitude_value,
        s=50
    )


    ax.annotate(

        format_frequency(
            frequency_value
        ),

        xy=(
            frequency_value,
            magnitude_value
        ),

        xytext=(
            5,
            8
        ),

        textcoords="offset points"

    )


ax.set_xscale(
    "log"
)


ax.set_xlim(
    10e3,
    30e6
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


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 37. MARK SELECTED FREQUENCIES
# ============================================================

"""
Researchers may want to highlight specific frequencies.

Example:

100 kHz

1 MHz

10 MHz
"""


important_frequencies = [

    100e3,

    1e6,

    10e6

]


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    fft_data["Frequency_Hz"],
    fft_data["Unshielded_dBuV"],
    linewidth=2
)


for frequency_value in important_frequencies:

    ax.axvline(
        x=frequency_value,
        linestyle="--",
        linewidth=1
    )


    ax.text(

        frequency_value,

        ax.get_ylim()[1],

        format_frequency(
            frequency_value
        ),

        rotation=90,

        va="top",

        ha="right"

    )


ax.set_xscale(
    "log"
)


ax.set_xlim(
    10e3,
    30e6
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


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 38. HIGHLIGHT FREQUENCY BAND
# ============================================================

"""
A frequency region can be highlighted using:

ax.axvspan()


Example:

100 kHz to 1 MHz
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    fft_data["Frequency_Hz"],
    fft_data["Unshielded_dBuV"],
    linewidth=2
)


ax.axvspan(
    100e3,
    1e6,
    alpha=0.2,
    label="Selected Frequency Band"
)


ax.set_xscale(
    "log"
)


ax.set_xlim(
    10e3,
    30e6
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
# 39. ANNOTATE DIFFERENCE BETWEEN TWO CASES
# ============================================================

"""
Another useful research annotation is the difference
between two configurations at a selected operating point.
"""


selected_load = 70


index = np.where(
    load_percent
    == selected_load
)[0][0]


baseline_value = (
    efficiency_baseline[
        index
    ]
)


design_value = (
    efficiency_design_b[
        index
    ]
)


difference = (
    design_value
    - baseline_value
)


print(
    "\n--- Efficiency Difference ---"
)


print(
    f"At {selected_load:.0f}% load:"
)


print(
    f"Baseline = "
    f"{baseline_value:.2f}%"
)


print(
    f"Design B = "
    f"{design_value:.2f}%"
)


print(
    f"Difference = "
    f"{difference:.2f} percentage points"
)


# ============================================================
# 40. PLOT DIFFERENCE ANNOTATION
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_baseline,
    marker="o",
    label="Baseline"
)


ax.plot(
    load_percent,
    efficiency_design_b,
    marker="s",
    label="Design B"
)


ax.annotate(

    (
        f"Difference = "
        f"{difference:.2f}\n"
        f"percentage points"
    ),

    xy=(
        selected_load,
        design_value
    ),

    xytext=(
        25,
        25
    ),

    textcoords="offset points",

    arrowprops={
        "arrowstyle":
            "->"
    }

)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 41. PERCENTAGE POINTS VS PERCENT CHANGE
# ============================================================

"""
Be careful with percentage quantities.

Example:

Baseline efficiency:

94%


New efficiency:

96%


Difference:

2 percentage points


Relative percentage increase:

(96 - 94) / 94 × 100

≈ 2.13%


These are NOT the same statement.
"""


relative_improvement = (

    difference
    / baseline_value

) * 100


print(
    "\nRelative Improvement:"
)


print(
    f"{relative_improvement:.2f}%"
)


# ============================================================
# 42. REUSABLE POINT-ANNOTATION FUNCTION
# ============================================================

def annotate_point(
    ax,
    x,
    y,
    text,
    x_offset=10,
    y_offset=10
):
    """
    Add an arrow annotation to a selected point.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis containing the plotted data.

    x : float
        X-coordinate.

    y : float
        Y-coordinate.

    text : str
        Annotation text.

    x_offset : float
        Horizontal text offset in points.

    y_offset : float
        Vertical text offset in points.
    """

    ax.scatter(
        x,
        y,
        s=60
    )


    ax.annotate(

        text,

        xy=(
            x,
            y
        ),

        xytext=(
            x_offset,
            y_offset
        ),

        textcoords="offset points",

        arrowprops={
            "arrowstyle":
                "->"
        }

    )


# ============================================================
# 43. USE ANNOTATION FUNCTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_b,
    marker="o"
)


annotate_point(

    ax=ax,

    x=maximum_efficiency_load,

    y=maximum_efficiency,

    text=(
        f"Maximum = "
        f"{maximum_efficiency:.1f}%"
    ),

    x_offset=-80,

    y_offset=-40

)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 44. REUSABLE MAXIMUM-ANNOTATION FUNCTION
# ============================================================

def annotate_maximum(
    ax,
    x,
    y,
    label="Maximum"
):
    """
    Automatically find and annotate the maximum Y value.
    """

    x = np.asarray(
        x
    )


    y = np.asarray(
        y
    )


    maximum_index = np.argmax(
        y
    )


    x_maximum = x[
        maximum_index
    ]


    y_maximum = y[
        maximum_index
    ]


    annotation_text = (
        f"{label}\n"
        f"x = {x_maximum:g}\n"
        f"y = {y_maximum:.2f}"
    )


    annotate_point(

        ax=ax,

        x=x_maximum,

        y=y_maximum,

        text=annotation_text,

        x_offset=15,

        y_offset=-50

    )


    return (
        x_maximum,
        y_maximum
    )


# ============================================================
# 45. USE AUTOMATIC MAXIMUM FUNCTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency_design_b,
    marker="o"
)


annotate_maximum(

    ax=ax,

    x=load_percent,

    y=efficiency_design_b,

    label="Peak Efficiency"

)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 46. REUSABLE HORIZONTAL LIMIT FUNCTION
# ============================================================

def add_horizontal_limit(
    ax,
    value,
    label
):
    """
    Add a horizontal engineering-limit line.
    """

    ax.axhline(
        y=value,
        linestyle="--",
        linewidth=1.5,
        label=label
    )


# ============================================================
# 47. USE LIMIT FUNCTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    temperature,
    marker="o",
    label="Temperature"
)


add_horizontal_limit(

    ax=ax,

    value=80,

    label="Maximum Temperature"

)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Temperature [°C]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 48. AUTOMATIC LEGEND FROM MANY CASES
# ============================================================

"""
Dictionaries are useful for automated engineering
comparison figures.
"""


comparison_cases = {

    "Baseline":
        efficiency_baseline,

    "Design A":
        efficiency_design_a,

    "Design B":
        efficiency_design_b

}


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, values in comparison_cases.items():

    ax.plot(
        load_percent,
        values,
        linewidth=2,
        label=case_name
    )


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.legend(
    title="Case",
    ncol=3
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 49. KEEP ANNOTATIONS LIMITED
# ============================================================

"""
Not every point needs a label.

Example:

500 frequency samples
        ↓
500 annotations

would make the figure unreadable.


Annotate only important features such as:

Maximum

Minimum

Resonance

Nominal operating point

Engineering limit

Important switching harmonic

Selected comparison point
"""


# ============================================================
# 50. SAVE FINAL ANNOTATED FIGURE
# ============================================================

output_figure_folder = (
    script_folder
    / "output_figures"
)


output_figure_folder.mkdir(
    exist_ok=True
)


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for case_name, column_name in frequency_cases.items():

    ax.plot(

        fft_data[
            "Frequency_Hz"
        ],

        fft_data[
            column_name
        ],

        linewidth=2,

        label=case_name

    )


# Mark maximum of unshielded spectrum

ax.scatter(
    peak_frequency,
    peak_magnitude,
    s=60
)


ax.annotate(

    (
        f"Maximum\n"
        f"{format_frequency(peak_frequency)}\n"
        f"{peak_magnitude:.1f} dBµV"
    ),

    xy=(
        peak_frequency,
        peak_magnitude
    ),

    xytext=(
        25,
        25
    ),

    textcoords="offset points",

    arrowprops={
        "arrowstyle":
            "->"
    }

)


ax.set_xscale(
    "log"
)


ax.set_xlim(
    10e3,
    30e6
)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.set_title(
    "Frequency-Domain Case Comparison"
)


ax.xaxis.set_major_formatter(
    FuncFormatter(
        format_frequency
    )
)


ax.legend(
    ncol=2
)


ax.grid(
    True,
    which="both"
)


plt.tight_layout()


# ============================================================
# 51. SAVE PNG
# ============================================================

png_file = (
    output_figure_folder
    / "legends_labels_annotations.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 52. SAVE PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "legends_labels_annotations.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 53. SAVE SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "legends_labels_annotations.svg"
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
# 54. COMMON MISTAKE - NO UNITS
# ============================================================

"""
Weak:

X-axis:

Frequency


Y-axis:

Magnitude


Better:

Frequency [Hz]

Magnitude [dBµV]


or engineering-formatted frequency labels with the unit
clearly communicated.
"""


# ============================================================
# 55. COMMON MISTAKE - RAW COLUMN NAMES IN LEGEND
# ============================================================

"""
Raw CSV column:

Case_A_dBuV


Final legend:

Case_A_dBuV


may be less readable than:

Case A


Keep raw column names useful for programming while using
clean labels for communication.
"""


# ============================================================
# 56. COMMON MISTAKE - LEGEND COVERS DATA
# ============================================================

"""
If the legend covers an important peak or transition:

Move it.

Possible options:

loc="best"

loc="upper left"

loc="lower right"

or place it outside using:

bbox_to_anchor=
"""


# ============================================================
# 57. COMMON MISTAKE - TOO MANY LEGEND ITEMS
# ============================================================

"""
A figure containing:

30 curves

and

30 legend entries

may be difficult to interpret.

Possible alternatives:

- Select representative cases
- Split into several figures
- Use subplots
- Group similar cases
- Use another visualization technique
"""


# ============================================================
# 58. COMMON MISTAKE - ANNOTATE EVERYTHING
# ============================================================

"""
Annotations should emphasize important information.

Do not label every sample unless the dataset is extremely
small and there is a clear reason.
"""


# ============================================================
# 59. COMMON MISTAKE - ARROW POINTS TO WRONG LOCATION
# ============================================================

"""
Always verify that:

xy=(x, y)

matches the intended data point.


The annotation text location:

xytext=

is independent from the actual point location.
"""


# ============================================================
# 60. COMMON MISTAKE - HARD-CODED PEAK
# ============================================================

"""
Instead of manually writing:

Peak = 95.9


calculate it:

maximum = data.max()


or:

index = data.idxmax()


This ensures the annotation updates if the underlying data
change.
"""


# ============================================================
# 61. COMMON MISTAKE - MAXIMUM SAMPLE IS NOT ALWAYS A PEAK
# ============================================================

"""
The largest sampled value is easy to identify using:

max()

argmax()

idxmax()


However, proper signal peak detection is a different task.

For signals containing:

Noise

Many oscillations

Multiple resonances

Harmonics


we may need methods such as:

scipy.signal.find_peaks()


That topic belongs to the Signal Processing section.
"""


# ============================================================
# 62. COMMON MISTAKE - LABELING PERCENTAGE DIFFERENCE
# ============================================================

"""
Example:

Baseline = 94%

New = 96%


Difference:

2 percentage points


Relative increase:

(96 - 94) / 94 × 100

≈ 2.13%


Do not automatically describe both quantities as:

"2% improvement"
"""


# ============================================================
# 63. COMMON MISTAKE - TOO MUCH TEXT
# ============================================================

"""
A figure should not become a paragraph.

Annotations should usually be concise.

Good:

Peak
1 MHz
92.4 dBµV


Less useful:

This is the point at which the maximum measured magnitude
was observed during this particular experiment...
"""


# ============================================================
# 64. COMMON MISTAKE - TITLE REPEATS CAPTION
# ============================================================

"""
For reports and tutorials:

Plot titles are useful.


For journal papers:

The figure caption may already describe the plot.

A redundant title inside the figure can consume valuable
space.

Use titles according to the final publication format.
"""


# ============================================================
# 65. LABELING DECISION WORKFLOW
# ============================================================

"""
Create Plot
    ↓
Add X Label
    ↓
Add X Unit
    ↓
Add Y Label
    ↓
Add Y Unit
    ↓
Several Curves?
   / \
 Yes  No
 ↓     ↓
Legend  No legend required
    ↓
Any Important Limit?
   / \
 Yes  No
 ↓     ↓
Reference Line
    ↓
Any Important Point?
   / \
 Yes  No
 ↓     ↓
Annotate
    ↓
Any Important Region?
   / \
 Yes  No
 ↓
Highlight Region
    ↓
Check Clutter
    ↓
Save Figure
"""


# ============================================================
# 66. ENGINEERING FIGURE EXAMPLE
# ============================================================

"""
A complete engineering figure may communicate:


X-axis:

Frequency


Y-axis:

Magnitude [dBµV]


Legend:

Unshielded
Case A
Case B
Case C


Annotation:

Peak = 96.2 dBµV
at 1 MHz


Highlighted region:

100 kHz to 1 MHz


Reference line:

Engineering limit


The reader can then understand:

WHAT was measured

WHICH cases were compared

WHERE the important event occurred

and

WHAT limit or operating region matters
"""


# ============================================================
# 67. PUBLICATION FIGURE CHECKLIST
# ============================================================

"""
Before exporting a research figure, check:

X-axis label?

X-axis unit?

Y-axis label?

Y-axis unit?

Legend readable?

Legend not covering data?

Case names understandable?

Important points annotated?

Annotations necessary?

Reference limits correct?

No excessive text?

Font readable?

Axis limits appropriate?

Figure understandable without source code?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
LEGENDS, LABELS, AND ANNOTATIONS


1. X-AXIS LABEL

ax.set_xlabel(
    "Time [s]"
)


------------------------------------------------------------


2. Y-AXIS LABEL

ax.set_ylabel(
    "Voltage [V]"
)


------------------------------------------------------------


3. TITLE

ax.set_title(
    "Converter Response"
)


------------------------------------------------------------


4. LINE LABEL

ax.plot(
    x,
    y,
    label="Case A"
)


------------------------------------------------------------


5. LEGEND

ax.legend()


------------------------------------------------------------


6. LEGEND LOCATION

ax.legend(
    loc="upper right"
)


------------------------------------------------------------


7. MULTIPLE LEGEND COLUMNS

ax.legend(
    ncol=3
)


------------------------------------------------------------


8. LEGEND OUTSIDE

ax.legend(

    loc="center left",

    bbox_to_anchor=(
        1.02,
        0.5
    )

)


------------------------------------------------------------


9. BASIC TEXT

ax.text(
    x,
    y,
    "Text"
)


------------------------------------------------------------


10. AXIS-RELATIVE TEXT

ax.text(

    0.05,

    0.90,

    "Text",

    transform=ax.transAxes

)


------------------------------------------------------------


11. ANNOTATION

ax.annotate(

    "Peak",

    xy=(
        x_peak,
        y_peak
    ),

    xytext=(
        20,
        20
    ),

    textcoords="offset points",

    arrowprops={
        "arrowstyle":
            "->"
    }

)


------------------------------------------------------------


12. HORIZONTAL LIMIT

ax.axhline(
    y=limit,
    linestyle="--"
)


------------------------------------------------------------


13. VERTICAL MARKER

ax.axvline(
    x=value,
    linestyle="--"
)


------------------------------------------------------------


14. HIGHLIGHT X RANGE

ax.axvspan(
    xmin,
    xmax,
    alpha=0.2
)


------------------------------------------------------------


15. HIGHLIGHT Y RANGE

ax.axhspan(
    ymin,
    ymax,
    alpha=0.2
)


------------------------------------------------------------


16. FIND MAXIMUM WITH NumPy

index = np.argmax(
    y
)


x_max = x[
    index
]


y_max = y[
    index
]


------------------------------------------------------------


17. FIND MAXIMUM WITH PANDAS

index = data[
    "Magnitude"
].idxmax()


------------------------------------------------------------


18. TOP VALUES

data.nlargest(
    3,
    "Magnitude"
)


Remember:

Largest samples are not necessarily independent physical
peaks.


------------------------------------------------------------


19. FREQUENCY PEAK WORKFLOW

Frequency Data
      ↓
Select Frequency Band
      ↓
Find Maximum
      ↓
Determine Peak Frequency
      ↓
Annotate
      ↓
Interpret


------------------------------------------------------------


20. ENGINEERING LIMITS

Use reference lines for:

Temperature limits

Voltage limits

Current limits

Performance targets

Frequency boundaries


------------------------------------------------------------


21. CLEAN LEGEND NAMES

Programming:

Case_A_dBuV


Presentation:

Case A


------------------------------------------------------------


22. DO NOT OVER-ANNOTATE

Highlight only information that helps explain the result.


------------------------------------------------------------


23. IMPORTANT RESEARCH PRINCIPLE

Annotations should explain the data.

They should not be used to distract from unwanted results
or exaggerate a conclusion.


------------------------------------------------------------


24. COMPLETE WORKFLOW

Raw Plot
   ↓
Labels
   ↓
Units
   ↓
Legend
   ↓
Important Limits
   ↓
Important Points
   ↓
Annotations
   ↓
Check Clutter
   ↓
Save
   ↓
Publication / Report


------------------------------------------------------------


NEXT:

17_error_bars.py


The next file will introduce uncertainty and variability:

Mean values

Standard deviation

Standard error

Measurement uncertainty

Error bars

Symmetric uncertainty

Asymmetric uncertainty

Repeated experiments

Multiple cases with error bars

Error bars on line plots

Error bars on bar plots

capsize

elinewidth

yerr

xerr

and the important distinction between:

Standard deviation

Standard error

Confidence interval

Measurement uncertainty
"""
