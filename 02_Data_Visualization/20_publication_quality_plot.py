"""
============================================================
Python for Engineering and Research
20 - Publication-Quality Plot
============================================================

Purpose:
    Demonstrate how to create clear, consistent, and
    publication-oriented engineering figures using
    Matplotlib.

Topics:
    1. What is a publication-quality figure?
    2. Figure dimensions
    3. Millimeter-to-inch conversion
    4. Single-column and double-column layouts
    5. Font hierarchy
    6. Line widths
    7. Marker sizes
    8. Line styles
    9. Axis labels and engineering units
    10. Major and minor ticks
    11. Tick direction
    12. Axis limits
    13. Logarithmic frequency axes
    14. Engineering frequency labels
    15. Legend formatting
    16. Grid formatting
    17. Titles vs figure captions
    18. Annotations
    19. Grayscale-friendly differentiation
    20. rcParams and rc_context
    21. Single-column example
    22. Double-column example
    23. FFT / EMI-style publication example
    24. Reusable publication plotting function
    25. PNG / PDF / SVG export
    26. Publication checklist
    27. Common mistakes
    28. Key takeaways

Sample File:
    sample_data/fft_example.csv

Important:
    There is no universal "publication-quality" style.

    Always check the official requirements of the target:

    - Journal
    - Conference
    - Publisher
    - Thesis template

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. REQUIRED LIBRARIES
# ============================================================

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

from pathlib import Path

from matplotlib.ticker import (
    AutoMinorLocator,
    FuncFormatter,
    LogLocator,
    MultipleLocator,
    NullFormatter
)


# ============================================================
# 2. WHAT IS A PUBLICATION-QUALITY FIGURE?
# ============================================================

"""
A publication-quality figure is not simply:

A high-resolution image.


It should also be:

- Scientifically correct
- Easy to interpret
- Properly labeled
- Consistent
- Readable at final document size
- Appropriate for the target publication
- Reproducible from the original data


A useful concept is:

Correct Data
    +
Appropriate Figure Size
    +
Readable Fonts
    +
Visible Lines
    +
Useful Markers
    +
Correct Units
    +
Appropriate Axes
    +
Clear Legend
    +
Suitable Resolution
    +
Suitable File Format

        ↓

Publication-Oriented Figure
"""


# ============================================================
# 3. PROJECT PATHS
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


sample_data_folder = (
    script_folder
    / "sample_data"
)


output_folder = (
    script_folder
    / "output_figures"
    / "publication_quality"
)


output_folder.mkdir(
    parents=True,
    exist_ok=True
)


print(
    "\n--- Output Folder ---"
)


print(
    output_folder
)


# ============================================================
# 4. BASIC ENGINEERING DATA
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


baseline_efficiency = np.array(
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


design_a_efficiency = np.array(
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


design_b_efficiency = np.array(
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


# ============================================================
# 5. FIGURE DIMENSIONS
# ============================================================

"""
Matplotlib uses inches for:

figsize=(width, height)


Journal specifications may instead provide:

millimeters

or

centimeters.


Therefore conversion functions are useful.
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


def cm_to_inches(
    centimeters
):
    """
    Convert centimeters to inches.
    """

    return (
        centimeters
        / 2.54
    )


# ============================================================
# 6. EXAMPLE PUBLICATION WIDTHS
# ============================================================

"""
The following widths are EDUCATIONAL examples only.

Exact dimensions vary between journals.

Always check the target publication instructions.
"""


single_column_width_mm = 88

double_column_width_mm = 178


single_column_width_in = mm_to_inches(
    single_column_width_mm
)


double_column_width_in = mm_to_inches(
    double_column_width_mm
)


print(
    "\n--- Example Figure Widths ---"
)


print(
    f"Single column: "
    f"{single_column_width_mm} mm = "
    f"{single_column_width_in:.3f} in"
)


print(
    f"Double column: "
    f"{double_column_width_mm} mm = "
    f"{double_column_width_in:.3f} in"
)


# ============================================================
# 7. FIGURE ASPECT RATIO
# ============================================================

"""
A figure also needs an appropriate height.

Example:

height = width × 0.70


The best ratio depends on:

- Number of curves
- Legend
- Axis labels
- Subplots
- Data distribution
"""


single_column_height_in = (
    single_column_width_in
    * 0.75
)


double_column_height_in = (
    double_column_width_in
    * 0.55
)


# ============================================================
# 8. WHY FINAL SIZE MATTERS
# ============================================================

"""
Suppose a figure is created at:

200 mm width


but inserted into a paper at:

88 mm width.


Everything is reduced:

- Fonts
- Markers
- Lines
- Annotations
- Legend


Therefore publication figures should ideally be designed
close to their final physical dimensions.
"""


# ============================================================
# 9. FONT HIERARCHY
# ============================================================

"""
A publication-oriented figure may use a hierarchy such as:

Axis labels:
9-10 pt

Tick labels:
8-9 pt

Legend:
8-9 pt

Annotations:
8-9 pt


These are only examples.

The target publication requirements should take priority.
"""


AXIS_LABEL_SIZE = 9

TICK_LABEL_SIZE = 8

LEGEND_SIZE = 8

ANNOTATION_SIZE = 8


# ============================================================
# 10. LINE AND MARKER PARAMETERS
# ============================================================

LINE_WIDTH = 1.5

MARKER_SIZE = 4.5

AXIS_LINE_WIDTH = 0.8

MAJOR_TICK_WIDTH = 0.8

MINOR_TICK_WIDTH = 0.6


# ============================================================
# 11. SIMPLE PUBLICATION-STYLE FIGURE
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        single_column_width_in,
        single_column_height_in
    )
)


ax.plot(
    load_percent,
    baseline_efficiency,
    marker="o",
    markersize=MARKER_SIZE,
    linewidth=LINE_WIDTH,
    label="Baseline"
)


ax.plot(
    load_percent,
    design_a_efficiency,
    marker="s",
    markersize=MARKER_SIZE,
    linewidth=LINE_WIDTH,
    linestyle="--",
    label="Design A"
)


ax.plot(
    load_percent,
    design_b_efficiency,
    marker="^",
    markersize=MARKER_SIZE,
    linewidth=LINE_WIDTH,
    linestyle="-.",
    label="Design B"
)


ax.set_xlabel(
    "Load [%]",
    fontsize=AXIS_LABEL_SIZE
)


ax.set_ylabel(
    "Efficiency [%]",
    fontsize=AXIS_LABEL_SIZE
)


ax.tick_params(
    axis="both",
    which="major",
    labelsize=TICK_LABEL_SIZE
)


ax.legend(
    fontsize=LEGEND_SIZE
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 12. WHY USE DIFFERENT LINE STYLES?
# ============================================================

"""
Do not rely only on color to distinguish cases.

Using:

Solid line

Dashed line

Dash-dot line


and different markers:

Circle

Square

Triangle


improves readability when figures are:

- Printed in grayscale
- Photocopied
- Viewed by readers with color-vision deficiencies
"""


# ============================================================
# 13. GRAYSCALE-FRIENDLY DIFFERENTIATION
# ============================================================

line_styles = [
    "-",
    "--",
    "-.",
    ":"
]


markers = [
    "o",
    "s",
    "^",
    "D"
]


fig, ax = plt.subplots(
    figsize=(
        single_column_width_in,
        single_column_height_in
    )
)


datasets = {

    "Baseline":
        baseline_efficiency,

    "Design A":
        design_a_efficiency,

    "Design B":
        design_b_efficiency

}


for (
    case_name,
    values
), line_style, marker in zip(

    datasets.items(),

    line_styles,

    markers

):

    ax.plot(
        load_percent,
        values,
        linestyle=line_style,
        marker=marker,
        markersize=MARKER_SIZE,
        linewidth=LINE_WIDTH,
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
# 14. AXIS LIMITS
# ============================================================

"""
Axis limits should support fair interpretation.

For the efficiency example:

X:

0 to 100% load


Y:

88 to 97% efficiency


A narrow Y-axis can reveal small changes, but it must not
be chosen simply to exaggerate differences.
"""


fig, ax = plt.subplots(
    figsize=(
        single_column_width_in,
        single_column_height_in
    )
)


for (
    case_name,
    values
), line_style, marker in zip(

    datasets.items(),

    line_styles,

    markers

):

    ax.plot(
        load_percent,
        values,
        linestyle=line_style,
        marker=marker,
        markersize=MARKER_SIZE,
        linewidth=LINE_WIDTH,
        label=case_name
    )


ax.set_xlim(
    0,
    100
)


ax.set_ylim(
    88,
    97
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
# 15. MAJOR TICKS
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        single_column_width_in,
        single_column_height_in
    )
)


ax.plot(
    load_percent,
    design_b_efficiency,
    marker="o",
    linewidth=LINE_WIDTH
)


ax.set_xlim(
    0,
    100
)


ax.set_ylim(
    88,
    97
)


ax.xaxis.set_major_locator(
    MultipleLocator(
        20
    )
)


ax.yaxis.set_major_locator(
    MultipleLocator(
        2
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
# 16. MINOR TICKS
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        single_column_width_in,
        single_column_height_in
    )
)


ax.plot(
    load_percent,
    design_b_efficiency,
    marker="o",
    linewidth=LINE_WIDTH
)


ax.set_xlim(
    0,
    100
)


ax.set_ylim(
    88,
    97
)


ax.xaxis.set_major_locator(
    MultipleLocator(
        20
    )
)


ax.xaxis.set_minor_locator(
    MultipleLocator(
        10
    )
)


ax.yaxis.set_major_locator(
    MultipleLocator(
        2
    )
)


ax.yaxis.set_minor_locator(
    MultipleLocator(
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
    True,
    which="major"
)


plt.tight_layout()

plt.show()


# ============================================================
# 17. INWARD TICKS
# ============================================================

"""
Inward ticks are common in many scientific figures.

Use:

direction="in"
"""


fig, ax = plt.subplots(
    figsize=(
        single_column_width_in,
        single_column_height_in
    )
)


ax.plot(
    load_percent,
    design_b_efficiency
)


ax.xaxis.set_minor_locator(
    AutoMinorLocator()
)


ax.yaxis.set_minor_locator(
    AutoMinorLocator()
)


ax.tick_params(
    axis="both",
    which="major",
    direction="in",
    top=True,
    right=True,
    length=4,
    width=MAJOR_TICK_WIDTH
)


ax.tick_params(
    axis="both",
    which="minor",
    direction="in",
    top=True,
    right=True,
    length=2,
    width=MINOR_TICK_WIDTH
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


plt.tight_layout()

plt.show()


# ============================================================
# 18. AXIS SPINE WIDTH
# ============================================================

"""
The four borders around a Matplotlib axis are called:

spines


They can be formatted consistently.
"""


fig, ax = plt.subplots(
    figsize=(
        single_column_width_in,
        single_column_height_in
    )
)


ax.plot(
    load_percent,
    design_b_efficiency
)


for spine in ax.spines.values():

    spine.set_linewidth(
        AXIS_LINE_WIDTH
    )


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


plt.tight_layout()

plt.show()


# ============================================================
# 19. GRID CONTROL
# ============================================================

"""
Grid lines should help interpretation without dominating
the figure.

For many publication figures:

Major grid only

can be sufficient.
"""


fig, ax = plt.subplots(
    figsize=(
        single_column_width_in,
        single_column_height_in
    )
)


ax.plot(
    load_percent,
    design_b_efficiency,
    marker="o"
)


ax.grid(
    True,
    which="major",
    linewidth=0.5,
    alpha=0.4
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


plt.tight_layout()

plt.show()


# ============================================================
# 20. GRID IS NOT ALWAYS REQUIRED
# ============================================================

"""
Some publication styles use:

No grid


Others use:

Light major grid lines


Choose according to:

- Data density
- Publication style
- Readability
- Figure purpose


Do not add visual elements merely because Matplotlib
supports them.
"""


# ============================================================
# 21. TITLES VS FIGURE CAPTIONS
# ============================================================

"""
For tutorials and presentations:

Plot titles can be useful.


For journal papers:

The figure caption usually provides the detailed
description.


Therefore a publication figure may omit:

ax.set_title(...)


to save space and avoid repeating information already
contained in the caption.
"""


# ============================================================
# 22. PUBLICATION FIGURE WITHOUT TITLE
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        single_column_width_in,
        single_column_height_in
    )
)


for (
    case_name,
    values
), line_style, marker in zip(

    datasets.items(),

    line_styles,

    markers

):

    ax.plot(
        load_percent,
        values,
        linestyle=line_style,
        marker=marker,
        markersize=MARKER_SIZE,
        linewidth=LINE_WIDTH,
        label=case_name
    )


ax.set_xlabel(
    "Load [%]",
    fontsize=AXIS_LABEL_SIZE
)


ax.set_ylabel(
    "Efficiency [%]",
    fontsize=AXIS_LABEL_SIZE
)


ax.tick_params(
    labelsize=TICK_LABEL_SIZE
)


ax.legend(
    fontsize=LEGEND_SIZE
)


ax.grid(
    True,
    alpha=0.4
)


plt.tight_layout()

plt.show()


# ============================================================
# 23. LEGEND POSITION
# ============================================================

"""
The legend should not hide important data.

Possible approaches:

loc="best"

loc="upper left"

loc="lower right"

or

place the legend outside the axis.


Compact publication figures often benefit from:

multiple legend columns.
"""


fig, ax = plt.subplots(
    figsize=(
        double_column_width_in,
        double_column_height_in
    )
)


for (
    case_name,
    values
), line_style, marker in zip(

    datasets.items(),

    line_styles,

    markers

):

    ax.plot(
        load_percent,
        values,
        linestyle=line_style,
        marker=marker,
        linewidth=LINE_WIDTH,
        markersize=MARKER_SIZE,
        label=case_name
    )


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.legend(
    ncol=3,
    loc="lower center"
)


ax.grid(
    True,
    alpha=0.4
)


plt.tight_layout()

plt.show()


# ============================================================
# 24. ANNOTATIONS
# ============================================================

"""
Annotations should be used only when they communicate
important scientific information.

Examples:

- Maximum efficiency
- Resonance frequency
- Operating limit
- Critical point
- Selected comparison
"""


maximum_index = np.argmax(
    design_b_efficiency
)


maximum_load = load_percent[
    maximum_index
]


maximum_efficiency = (
    design_b_efficiency[
        maximum_index
    ]
)


fig, ax = plt.subplots(
    figsize=(
        single_column_width_in,
        single_column_height_in
    )
)


ax.plot(
    load_percent,
    design_b_efficiency,
    marker="o",
    markersize=MARKER_SIZE,
    linewidth=LINE_WIDTH
)


ax.annotate(

    (
        f"Maximum\n"
        f"{maximum_efficiency:.1f}%"
    ),

    xy=(
        maximum_load,
        maximum_efficiency
    ),

    xytext=(
        -45,
        -30
    ),

    textcoords="offset points",

    fontsize=ANNOTATION_SIZE,

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
    True,
    alpha=0.4
)


plt.tight_layout()

plt.show()


# ============================================================
# 25. GLOBAL MATPLOTLIB SETTINGS
# ============================================================

"""
Matplotlib provides:

rcParams


for global formatting.

Example:

mpl.rcParams[
    "font.size"
] = 9


However, changing global rcParams affects all later plots
in the Python session.


For reusable research scripts:

mpl.rc_context()

can be safer.
"""


# ============================================================
# 26. PUBLICATION STYLE DICTIONARY
# ============================================================

publication_style = {

    "font.family":
        "DejaVu Sans",

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
        1.5,

    "lines.markersize":
        4.5,

    "savefig.bbox":
        "tight"
}


# ============================================================
# 27. USE rc_context()
# ============================================================

"""
rc_context():

temporarily applies formatting settings.


After leaving the:

with

block, normal Matplotlib settings are restored.
"""


with mpl.rc_context(
    publication_style
):

    fig, ax = plt.subplots(
        figsize=(
            single_column_width_in,
            single_column_height_in
        )
    )


    ax.plot(
        load_percent,
        baseline_efficiency,
        marker="o",
        label="Baseline"
    )


    ax.plot(
        load_percent,
        design_a_efficiency,
        marker="s",
        linestyle="--",
        label="Design A"
    )


    ax.plot(
        load_percent,
        design_b_efficiency,
        marker="^",
        linestyle="-.",
        label="Design B"
    )


    ax.set_xlabel(
        "Load [%]"
    )


    ax.set_ylabel(
        "Efficiency [%]"
    )


    ax.legend()


    ax.grid(
        True,
        alpha=0.35
    )


    plt.tight_layout()

    plt.show()


# ============================================================
# 28. WHY rc_context() IS USEFUL
# ============================================================

"""
A research project may contain:

Figure 1

Figure 2

Figure 3

...

Figure 20


Instead of manually setting fonts and line widths for every
figure, one publication style can be reused.

This improves:

- Consistency
- Maintainability
- Reproducibility
"""


# ============================================================
# 29. LOAD FFT / FREQUENCY-DOMAIN DATA
# ============================================================

fft_file = (
    sample_data_folder
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
    "\n--- FFT Columns ---"
)


print(
    fft_data.columns.tolist()
)


# ============================================================
# 30. EXPECTED FFT COLUMNS
# ============================================================

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


# ============================================================
# 31. CLEAN AND VALIDATE FREQUENCY DATA
# ============================================================

fft_data = fft_data.copy()


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
# 32. ENGINEERING FREQUENCY FORMATTER
# ============================================================

def format_frequency(
    value,
    position=None
):
    """
    Format frequency using engineering units.
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
# 33. FFT CASE DEFINITIONS
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


frequency_line_styles = [

    "-",

    "--",

    "-.",

    ":"

]


# ============================================================
# 34. AUTOMATIC Y-AXIS LIMITS
# ============================================================

"""
Rather than blindly selecting a fixed Y-axis range, we can
calculate a clean range from the data.

Example:

Minimum = 51.3

Maximum = 107.8


Rounded plotting range might become:

50 to 110
"""


all_magnitude_columns = list(
    frequency_cases.values()
)


minimum_magnitude = (
    fft_data[
        all_magnitude_columns
    ]
    .min()
    .min()
)


maximum_magnitude = (
    fft_data[
        all_magnitude_columns
    ]
    .max()
    .max()
)


y_minimum = (
    np.floor(
        minimum_magnitude
        / 10
    )
    * 10
)


y_maximum = (
    np.ceil(
        maximum_magnitude
        / 10
    )
    * 10
)


if y_minimum == y_maximum:

    y_minimum -= 10

    y_maximum += 10


print(
    "\n--- FFT Y-Axis Range ---"
)


print(
    y_minimum,
    "to",
    y_maximum,
    "dBµV"
)


# ============================================================
# 35. PUBLICATION-QUALITY FFT FIGURE
# ============================================================

with mpl.rc_context(
    publication_style
):

    fig, ax = plt.subplots(
        figsize=(
            double_column_width_in,
            double_column_height_in
        )
    )


    for (
        case_name,
        column_name
    ), line_style in zip(

        frequency_cases.items(),

        frequency_line_styles

    ):

        ax.plot(

            fft_data[
                "Frequency_Hz"
            ],

            fft_data[
                column_name
            ],

            linestyle=line_style,

            label=case_name

        )


    # Logarithmic frequency axis

    ax.set_xscale(
        "log"
    )


    # Frequency range

    ax.set_xlim(
        10e3,
        30e6
    )


    # Y-axis range

    ax.set_ylim(
        y_minimum,
        y_maximum
    )


    # Labels

    ax.set_xlabel(
        "Frequency"
    )


    ax.set_ylabel(
        "Magnitude [dBµV]"
    )


    # Major frequency ticks

    ax.set_xticks(
        [
            10e3,
            100e3,
            1e6,
            10e6
        ]
    )


    ax.xaxis.set_major_formatter(
        FuncFormatter(
            format_frequency
        )
    )


    # Minor logarithmic ticks

    ax.xaxis.set_minor_locator(
        LogLocator(
            base=10,
            subs=np.arange(
                2,
                10
            ) * 0.1
        )
    )


    # Do not label every minor tick.

    ax.xaxis.set_minor_formatter(
        NullFormatter()
    )


    # Y-axis ticks

    ax.yaxis.set_major_locator(
        MultipleLocator(
            10
        )
    )


    ax.yaxis.set_minor_locator(
        MultipleLocator(
            5
        )
    )


    # Major grid

    ax.grid(
        True,
        which="major",
        linewidth=0.5,
        alpha=0.4
    )


    # Optional light minor frequency grid

    ax.grid(
        True,
        which="minor",
        axis="x",
        linewidth=0.3,
        alpha=0.2
    )


    # Legend

    ax.legend(
        ncol=2,
        frameon=True,
        loc="best"
    )


    plt.tight_layout()

    plt.show()


# ============================================================
# 36. dBµV AXIS NOTE
# ============================================================

"""
The frequency axis is logarithmic:

Frequency [Hz]
       ↓
Logarithmic X-axis


The magnitude is already expressed in:

dBµV


Therefore the numerical dBµV Y-axis normally remains:

LINEAR


Do not automatically apply:

ax.set_yscale(
    "log"
)

to a dBµV axis.
"""


# ============================================================
# 37. AUTOMATIC PEAK DETECTION FOR ANNOTATION
# ============================================================

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
    "\n--- Unshielded Maximum ---"
)


print(
    format_frequency(
        peak_frequency
    )
)


print(
    f"{peak_magnitude:.2f} dBµV"
)


# ============================================================
# 38. PUBLICATION FFT WITH PEAK ANNOTATION
# ============================================================

with mpl.rc_context(
    publication_style
):

    fig, ax = plt.subplots(
        figsize=(
            double_column_width_in,
            double_column_height_in
        )
    )


    for (
        case_name,
        column_name
    ), line_style in zip(

        frequency_cases.items(),

        frequency_line_styles

    ):

        ax.plot(

            fft_data[
                "Frequency_Hz"
            ],

            fft_data[
                column_name
            ],

            linestyle=line_style,

            label=case_name

        )


    ax.set_xscale(
        "log"
    )


    ax.set_xlim(
        10e3,
        30e6
    )


    ax.set_ylim(
        y_minimum,
        y_maximum
    )


    ax.set_xlabel(
        "Frequency"
    )


    ax.set_ylabel(
        "Magnitude [dBµV]"
    )


    ax.set_xticks(
        [
            10e3,
            100e3,
            1e6,
            10e6
        ]
    )


    ax.xaxis.set_major_formatter(
        FuncFormatter(
            format_frequency
        )
    )


    ax.xaxis.set_minor_locator(
        LogLocator(
            base=10,
            subs=np.arange(
                2,
                10
            ) * 0.1
        )
    )


    ax.xaxis.set_minor_formatter(
        NullFormatter()
    )


    ax.yaxis.set_major_locator(
        MultipleLocator(
            10
        )
    )


    ax.scatter(
        peak_frequency,
        peak_magnitude,
        s=22
    )


    ax.annotate(

        (
            f"{format_frequency(peak_frequency)}\n"
            f"{peak_magnitude:.1f} dBµV"
        ),

        xy=(
            peak_frequency,
            peak_magnitude
        ),

        xytext=(
            20,
            -30
        ),

        textcoords="offset points",

        fontsize=ANNOTATION_SIZE,

        arrowprops={
            "arrowstyle":
                "->"
        }

    )


    ax.grid(
        True,
        which="major",
        linewidth=0.5,
        alpha=0.4
    )


    ax.legend(
        ncol=2
    )


    plt.tight_layout()

    plt.show()


# ============================================================
# 39. DO NOT OVER-ANNOTATE
# ============================================================

"""
Publication figures usually have limited space.

Avoid annotating:

Every sample

Every harmonic

Every local maximum

Every curve


unless those labels are essential to the scientific
interpretation.

Use the figure caption and main text for additional
explanation.
"""


# ============================================================
# 40. SINGLE-COLUMN PUBLICATION EXAMPLE
# ============================================================

with mpl.rc_context(
    publication_style
):

    fig, ax = plt.subplots(
        figsize=(
            single_column_width_in,
            single_column_height_in
        )
    )


    ax.plot(
        load_percent,
        baseline_efficiency,
        marker="o",
        linestyle="-",
        label="Baseline"
    )


    ax.plot(
        load_percent,
        design_a_efficiency,
        marker="s",
        linestyle="--",
        label="Design A"
    )


    ax.plot(
        load_percent,
        design_b_efficiency,
        marker="^",
        linestyle="-.",
        label="Design B"
    )


    ax.set_xlim(
        0,
        100
    )


    ax.set_ylim(
        88,
        97
    )


    ax.xaxis.set_major_locator(
        MultipleLocator(
            20
        )
    )


    ax.xaxis.set_minor_locator(
        MultipleLocator(
            10
        )
    )


    ax.yaxis.set_major_locator(
        MultipleLocator(
            2
        )
    )


    ax.yaxis.set_minor_locator(
        MultipleLocator(
            0.5
        )
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
        True,
        which="major",
        linewidth=0.5,
        alpha=0.35
    )


    plt.tight_layout()

    plt.show()


# ============================================================
# 41. DOUBLE-COLUMN PUBLICATION EXAMPLE
# ============================================================

with mpl.rc_context(
    publication_style
):

    fig, ax = plt.subplots(
        figsize=(
            double_column_width_in,
            double_column_height_in
        )
    )


    for (
        case_name,
        values
    ), line_style, marker in zip(

        datasets.items(),

        line_styles,

        markers

    ):

        ax.plot(
            load_percent,
            values,
            linestyle=line_style,
            marker=marker,
            label=case_name
        )


    ax.set_xlabel(
        "Load [%]"
    )


    ax.set_ylabel(
        "Efficiency [%]"
    )


    ax.legend(
        ncol=3
    )


    ax.grid(
        True,
        alpha=0.35
    )


    plt.tight_layout()

    plt.show()


# ============================================================
# 42. REUSABLE AXIS-FORMATTING FUNCTION
# ============================================================

def format_publication_axis(
    ax,
    x_label,
    y_label,
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None,
    x_major=None,
    y_major=None,
    x_minor=None,
    y_minor=None,
    grid=True
):
    """
    Apply reusable publication-oriented formatting to a
    linear Matplotlib axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to format.

    x_label : str
        X-axis label.

    y_label : str
        Y-axis label.

    x_min, x_max : float, optional
        X-axis limits.

    y_min, y_max : float, optional
        Y-axis limits.

    x_major, y_major : float, optional
        Major tick intervals.

    x_minor, y_minor : float, optional
        Minor tick intervals.

    grid : bool
        Enable major grid.
    """

    ax.set_xlabel(
        x_label
    )


    ax.set_ylabel(
        y_label
    )


    if (
        x_min is not None
        or x_max is not None
    ):

        ax.set_xlim(
            left=x_min,
            right=x_max
        )


    if (
        y_min is not None
        or y_max is not None
    ):

        ax.set_ylim(
            bottom=y_min,
            top=y_max
        )


    if x_major is not None:

        ax.xaxis.set_major_locator(
            MultipleLocator(
                x_major
            )
        )


    if y_major is not None:

        ax.yaxis.set_major_locator(
            MultipleLocator(
                y_major
            )
        )


    if x_minor is not None:

        ax.xaxis.set_minor_locator(
            MultipleLocator(
                x_minor
            )
        )


    if y_minor is not None:

        ax.yaxis.set_minor_locator(
            MultipleLocator(
                y_minor
            )
        )


    ax.tick_params(
        axis="both",
        which="major",
        direction="in",
        top=True,
        right=True
    )


    ax.tick_params(
        axis="both",
        which="minor",
        direction="in",
        top=True,
        right=True
    )


    if grid:

        ax.grid(
            True,
            which="major",
            linewidth=0.5,
            alpha=0.35
        )


# ============================================================
# 43. USE AXIS-FORMATTING FUNCTION
# ============================================================

with mpl.rc_context(
    publication_style
):

    fig, ax = plt.subplots(
        figsize=(
            single_column_width_in,
            single_column_height_in
        )
    )


    ax.plot(
        load_percent,
        design_b_efficiency,
        marker="o"
    )


    format_publication_axis(

        ax=ax,

        x_label="Load [%]",

        y_label="Efficiency [%]",

        x_min=0,

        x_max=100,

        y_min=88,

        y_max=97,

        x_major=20,

        y_major=2,

        x_minor=10,

        y_minor=0.5

    )


    plt.tight_layout()

    plt.show()


# ============================================================
# 44. REUSABLE FREQUENCY-AXIS FUNCTION
# ============================================================

def format_publication_frequency_axis(
    ax,
    frequency_min,
    frequency_max,
    y_min,
    y_max,
    y_major=10,
    y_minor=5
):
    """
    Configure a publication-oriented logarithmic
    frequency axis.
    """

    if frequency_min <= 0:

        raise ValueError(
            "Logarithmic frequency minimum "
            "must be greater than zero."
        )


    if frequency_max <= frequency_min:

        raise ValueError(
            "Maximum frequency must be greater "
            "than minimum frequency."
        )


    ax.set_xscale(
        "log"
    )


    ax.set_xlim(
        frequency_min,
        frequency_max
    )


    ax.set_ylim(
        y_min,
        y_max
    )


    ax.set_xlabel(
        "Frequency"
    )


    ax.set_ylabel(
        "Magnitude [dBµV]"
    )


    ax.set_xticks(
        [
            10e3,
            100e3,
            1e6,
            10e6
        ]
    )


    ax.xaxis.set_major_formatter(
        FuncFormatter(
            format_frequency
        )
    )


    ax.xaxis.set_minor_locator(
        LogLocator(
            base=10,
            subs=np.arange(
                2,
                10
            ) * 0.1
        )
    )


    ax.xaxis.set_minor_formatter(
        NullFormatter()
    )


    ax.yaxis.set_major_locator(
        MultipleLocator(
            y_major
        )
    )


    ax.yaxis.set_minor_locator(
        MultipleLocator(
            y_minor
        )
    )


    ax.grid(
        True,
        which="major",
        linewidth=0.5,
        alpha=0.4
    )


    ax.grid(
        True,
        which="minor",
        axis="x",
        linewidth=0.3,
        alpha=0.2
    )


# ============================================================
# 45. USE REUSABLE FREQUENCY FORMATTER
# ============================================================

with mpl.rc_context(
    publication_style
):

    fig, ax = plt.subplots(
        figsize=(
            double_column_width_in,
            double_column_height_in
        )
    )


    for (
        case_name,
        column_name
    ), line_style in zip(

        frequency_cases.items(),

        frequency_line_styles

    ):

        ax.plot(

            fft_data[
                "Frequency_Hz"
            ],

            fft_data[
                column_name
            ],

            linestyle=line_style,

            label=case_name

        )


    format_publication_frequency_axis(

        ax=ax,

        frequency_min=10e3,

        frequency_max=30e6,

        y_min=y_minimum,

        y_max=y_maximum

    )


    ax.legend(
        ncol=2
    )


    plt.tight_layout()

    plt.show()


# ============================================================
# 46. SAVE FUNCTION
# ============================================================

def save_publication_figure(
    fig,
    output_folder,
    filename,
    png_dpi=600,
    save_png=True,
    save_pdf=True,
    save_svg=True
):
    """
    Save publication figure in raster and vector formats.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to save.

    output_folder : str or Path
        Destination folder.

    filename : str
        Base filename without extension.

    png_dpi : int
        PNG resolution.

    save_png : bool
        Save PNG file.

    save_pdf : bool
        Save PDF file.

    save_svg : bool
        Save SVG file.

    Returns
    -------
    saved_files : list
        Generated file paths.
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
            "PNG DPI must be greater than zero."
        )


    saved_files = []


    if save_png:

        png_file = (
            output_folder
            / f"{filename}.png"
        )


        fig.savefig(
            png_file,
            dpi=png_dpi,
            bbox_inches="tight"
        )


        saved_files.append(
            png_file
        )


    if save_pdf:

        pdf_file = (
            output_folder
            / f"{filename}.pdf"
        )


        fig.savefig(
            pdf_file,
            bbox_inches="tight"
        )


        saved_files.append(
            pdf_file
        )


    if save_svg:

        svg_file = (
            output_folder
            / f"{filename}.svg"
        )


        fig.savefig(
            svg_file,
            bbox_inches="tight"
        )


        saved_files.append(
            svg_file
        )


    return saved_files


# ============================================================
# 47. FINAL PUBLICATION FFT FIGURE
# ============================================================

with mpl.rc_context(
    publication_style
):

    fig, ax = plt.subplots(
        figsize=(
            double_column_width_in,
            double_column_height_in
        )
    )


    for (
        case_name,
        column_name
    ), line_style in zip(

        frequency_cases.items(),

        frequency_line_styles

    ):

        ax.plot(

            fft_data[
                "Frequency_Hz"
            ],

            fft_data[
                column_name
            ],

            linestyle=line_style,

            label=case_name

        )


    format_publication_frequency_axis(

        ax=ax,

        frequency_min=10e3,

        frequency_max=30e6,

        y_min=y_minimum,

        y_max=y_maximum,

        y_major=10,

        y_minor=5

    )


    ax.legend(
        ncol=2,
        loc="best"
    )


    plt.tight_layout()


    final_files = save_publication_figure(

        fig=fig,

        output_folder=output_folder,

        filename=(
            "publication_frequency_comparison"
        ),

        png_dpi=600

    )


    print(
        "\n--- Final Publication Files ---"
    )


    for file_path in final_files:

        print(
            file_path
        )


    plt.show()


# ============================================================
# 48. FINAL SINGLE-COLUMN FIGURE
# ============================================================

with mpl.rc_context(
    publication_style
):

    fig, ax = plt.subplots(
        figsize=(
            single_column_width_in,
            single_column_height_in
        )
    )


    ax.plot(
        load_percent,
        baseline_efficiency,
        linestyle="-",
        marker="o",
        label="Baseline"
    )


    ax.plot(
        load_percent,
        design_a_efficiency,
        linestyle="--",
        marker="s",
        label="Design A"
    )


    ax.plot(
        load_percent,
        design_b_efficiency,
        linestyle="-.",
        marker="^",
        label="Design B"
    )


    format_publication_axis(

        ax=ax,

        x_label="Load [%]",

        y_label="Efficiency [%]",

        x_min=0,

        x_max=100,

        y_min=88,

        y_max=97,

        x_major=20,

        y_major=2,

        x_minor=10,

        y_minor=0.5

    )


    ax.legend(
        loc="lower right"
    )


    plt.tight_layout()


    efficiency_files = (
        save_publication_figure(

            fig=fig,

            output_folder=output_folder,

            filename=(
                "publication_efficiency_comparison"
            ),

            png_dpi=600

        )
    )


    plt.show()


# ============================================================
# 49. VERIFY SAVED FILES
# ============================================================

print(
    "\n--- Verify Saved Files ---"
)


for file_path in (
    final_files
    + efficiency_files
):

    if file_path.exists():

        size_kb = (
            file_path
            .stat()
            .st_size
            / 1024
        )


        print(
            file_path.name,
            "-",
            f"{size_kb:.2f} kB"
        )


# ============================================================
# 50. PNG VS PDF VS SVG
# ============================================================

"""
PNG

Raster

Useful for:

- Raster submission
- Presentations
- GitHub
- Web
- Preview


------------------------------------------------------------


PDF

Vector-oriented for many Matplotlib plots

Useful for:

- Papers
- Thesis
- Reports
- LaTeX workflows


------------------------------------------------------------


SVG

Vector-oriented

Useful for:

- Further editing
- Web
- Scalable graphics


Always check which formats the target publisher accepts.
"""


# ============================================================
# 51. WHY 600 DPI IS USED HERE
# ============================================================

"""
The final PNG examples use:

600 DPI


because this file demonstrates high-resolution publication
export.

However:

600 DPI is NOT a universal requirement.


A publication may request:

300 DPI

600 DPI

or another value depending on:

- Figure type
- Publisher
- Submission system


Always follow the actual instructions.
"""


# ============================================================
# 52. COLOR VS LINE STYLE
# ============================================================

"""
Color can improve interpretation on screen.

However, a publication figure should ideally remain
understandable when:

- Printed in grayscale
- Viewed with reduced color distinction


Therefore combine:

Color
+
Line style
+
Marker shape


rather than relying entirely on color.
"""


# ============================================================
# 53. TOO MANY CASES
# ============================================================

"""
Publication quality does NOT mean plotting every available
dataset.

Suppose an experiment contains:

25 configurations.


Putting all 25 curves on one figure may reduce clarity.

Consider:

- Selecting representative cases
- Multiple panels
- Summary metrics
- Separate figures
- Statistical summaries
"""


# ============================================================
# 54. TOO MANY MARKERS
# ============================================================

"""
For dense data, a marker on every sample may create clutter.

Options include:

- No markers
- Smaller markers
- markevery=
"""


dense_x = np.linspace(
    0,
    10,
    300
)


dense_y = np.sin(
    dense_x
)


fig, ax = plt.subplots(
    figsize=(
        single_column_width_in,
        single_column_height_in
    )
)


ax.plot(
    dense_x,
    dense_y,
    marker="o",
    markersize=3,
    markevery=25,
    linewidth=1.3
)


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Amplitude [-]"
)


plt.tight_layout()

plt.show()


# ============================================================
# 55. markevery
# ============================================================

"""
markevery=25

means:

Plot the continuous line normally,

but display a marker only approximately every 25 samples.


This can improve clarity in dense line plots.
"""


# ============================================================
# 56. PUBLICATION SUBPLOTS
# ============================================================

"""
Multi-panel figures are common in papers.

Example:

(a) Voltage

(b) Current

(c) Power


Panel labels can later be added when needed.

For multiple physical quantities, subplots are generally
clearer than forcing many Y-axes onto one panel.
"""


time = np.linspace(
    0,
    0.02,
    200
)


voltage = (
    48
    +
    2
    * np.sin(
        2
        * np.pi
        * 100
        * time
    )
)


current = (
    2
    +
    0.2
    * np.sin(
        2
        * np.pi
        * 100
        * time
    )
)


with mpl.rc_context(
    publication_style
):

    fig, axes = plt.subplots(

        2,

        1,

        figsize=(
            single_column_width_in,
            single_column_width_in
        ),

        sharex=True

    )


    axes[0].plot(
        time,
        voltage
    )


    axes[0].set_ylabel(
        "Voltage [V]"
    )


    axes[1].plot(
        time,
        current
    )


    axes[1].set_xlabel(
        "Time [s]"
    )


    axes[1].set_ylabel(
        "Current [A]"
    )


    for ax in axes:

        ax.grid(
            True,
            linewidth=0.5,
            alpha=0.35
        )


        ax.tick_params(
            direction="in",
            top=True,
            right=True
        )


    plt.tight_layout()

    plt.show()


# ============================================================
# 57. PANEL LABELS
# ============================================================

"""
Multi-panel figures may use labels such as:

(a)

(b)

(c)


Example:

ax.text(
    0.02,
    0.95,
    "(a)",
    transform=ax.transAxes
)


Exact formatting depends on the publication style.
"""


# ============================================================
# 58. EXAMPLE PANEL LABELS
# ============================================================

with mpl.rc_context(
    publication_style
):

    fig, axes = plt.subplots(

        2,

        1,

        figsize=(
            single_column_width_in,
            single_column_width_in
        ),

        sharex=True

    )


    axes[0].plot(
        time,
        voltage
    )


    axes[1].plot(
        time,
        current
    )


    axes[0].set_ylabel(
        "Voltage [V]"
    )


    axes[1].set_ylabel(
        "Current [A]"
    )


    axes[1].set_xlabel(
        "Time [s]"
    )


    panel_labels = [
        "(a)",
        "(b)"
    ]


    for ax, panel_label in zip(
        axes,
        panel_labels
    ):

        ax.text(

            0.02,

            0.93,

            panel_label,

            transform=ax.transAxes,

            va="top"

        )


        ax.grid(
            True,
            linewidth=0.5,
            alpha=0.35
        )


    plt.tight_layout()

    plt.show()


# ============================================================
# 59. REPRODUCIBLE FIGURE PARAMETERS
# ============================================================

"""
Avoid manually adjusting every figure until it "looks
right" without recording the settings.

Instead define parameters:

FIGURE_WIDTH

FONT_SIZE

LINE_WIDTH

MARKER_SIZE

AXIS_LIMITS

DPI


inside the code.

This makes the figure reproducible.
"""


# ============================================================
# 60. PUBLICATION FIGURE CONFIGURATION EXAMPLE
# ============================================================

publication_config = {

    "single_column_width_mm":
        88,

    "double_column_width_mm":
        178,

    "axis_label_size":
        9,

    "tick_label_size":
        8,

    "legend_size":
        8,

    "line_width":
        1.5,

    "marker_size":
        4.5,

    "png_dpi":
        600

}


print(
    "\n--- Publication Configuration ---"
)


for key, value in publication_config.items():

    print(
        key,
        "=",
        value
    )


# ============================================================
# 61. PUBLICATION QUALITY IS NOT DECORATION
# ============================================================

"""
Avoid thinking:

More formatting
       =
Better figure


A publication figure should be:

Simple

Clear

Accurate

Readable


Not:

Decorative

Overloaded

Visually distracting
"""


# ============================================================
# 62. COMMON MISTAKE - VERY LARGE TITLE
# ============================================================

"""
Large titles consume valuable space in compact journal
figures.

Often the figure caption already provides the title and
description.

Consider omitting the internal plot title for papers.
"""


# ============================================================
# 63. COMMON MISTAKE - NO UNITS
# ============================================================

"""
Weak:

Frequency

Magnitude


Better:

Frequency [Hz]

Magnitude [dBµV]


or:

Frequency

with tick labels clearly expressed as:

kHz

MHz
"""


# ============================================================
# 64. COMMON MISTAKE - TINY TEXT
# ============================================================

"""
A 600 DPI figure can still contain unreadable text.

Resolution and text size are independent.

Always check the figure at final publication dimensions.
"""


# ============================================================
# 65. COMMON MISTAKE - TOO THICK LINES
# ============================================================

"""
Very thick lines can hide:

- Small variations
- Nearby curves
- Markers
- Error bars


Choose line width according to:

- Figure dimensions
- Number of curves
- Data density
"""


# ============================================================
# 66. COMMON MISTAKE - TOO THIN LINES
# ============================================================

"""
Lines that appear visible in a large interactive window may
become difficult to see after publication scaling.

Always inspect the final exported figure.
"""


# ============================================================
# 67. COMMON MISTAKE - ONLY COLOR DIFFERENTIATION
# ============================================================

"""
Example:

Four solid lines

distinguished only by color


may become difficult to interpret in grayscale.

Use combinations of:

- Color
- Line style
- Marker shape
"""


# ============================================================
# 68. COMMON MISTAKE - OVERLOADED LEGEND
# ============================================================

"""
A legend containing 20 entries can dominate the figure.

If too many cases exist, reconsider the visualization
strategy.
"""


# ============================================================
# 69. COMMON MISTAKE - LEGEND COVERS RESULT
# ============================================================

"""
Check whether the legend hides:

Peaks

Transitions

Important differences

Annotations


Move the legend if necessary.
"""


# ============================================================
# 70. COMMON MISTAKE - EXCESSIVE GRID
# ============================================================

"""
Dark major and minor grid lines can dominate the data.

Use grid lines only when they support interpretation.
"""


# ============================================================
# 71. COMMON MISTAKE - AUTOMATIC AXIS LIMITS FOR ALL FIGURES
# ============================================================

"""
Automatic limits are useful during exploration.

For final comparisons, manually controlled limits may
provide fairer and more consistent comparison between
cases.

Do not use manual limits to hide inconvenient data.
"""


# ============================================================
# 72. COMMON MISTAKE - DIFFERENT AXES FOR COMPARISON FIGURES
# ============================================================

"""
If:

Case A

and

Case B


are shown in separate figures but represent the same
physical quantity, inconsistent axis ranges can create a
misleading visual comparison.

Use common limits when scientifically appropriate.
"""


# ============================================================
# 73. COMMON MISTAKE - EXCESSIVE DECIMAL PLACES
# ============================================================

"""
Avoid tick labels such as:

94.000000

95.000000

96.000000


unless that precision is scientifically meaningful.

Displayed precision should reflect the data and
measurement context.
"""


# ============================================================
# 74. COMMON MISTAKE - TOO MANY ANNOTATIONS
# ============================================================

"""
A figure should not contain an explanation for every data
point.

Use annotations for:

- Key result
- Important peak
- Engineering limit
- Critical transition
"""


# ============================================================
# 75. COMMON MISTAKE - HIGH DPI = PUBLICATION QUALITY
# ============================================================

"""
Incorrect concept:

1200 DPI
      ↓
Publication Quality


Better concept:

Correct Data
+
Good Layout
+
Correct Units
+
Readable Text
+
Appropriate Axes
+
Clear Legend
+
Correct Figure Size
+
Suitable Resolution
      ↓
Publication-Oriented Quality
"""


# ============================================================
# 76. COMMON MISTAKE - NOT CHECKING PUBLISHER REQUIREMENTS
# ============================================================

"""
Different journals may require different:

- Dimensions
- Resolution
- File formats
- Fonts
- Color mode
- Line thickness
- File sizes


Never assume one universal Matplotlib configuration works
for every publication.
"""


# ============================================================
# 77. COMMON MISTAKE - EDITING RESULTS MANUALLY AFTER EXPORT
# ============================================================

"""
Minor graphical editing may sometimes be required.

However, the research figure should ideally be reproducible
directly from Python.

Avoid workflows where:

Python
    ↓
Export
    ↓
Manually move data points
    ↓
Manually change numerical values


The plotted scientific data should remain traceable to the
analysis code.
"""


# ============================================================
# 78. PUBLICATION FIGURE CHECKLIST
# ============================================================

"""
Before exporting a final research figure, check:

DATA
------------------------------------------------------------

Correct dataset?

Correct processing?

Correct units?

Correct comparison?


AXES
------------------------------------------------------------

Correct scale?

Correct limits?

Correct ticks?

Logarithmic axis justified?


LABELS
------------------------------------------------------------

X label?

Y label?

Units?

Readable font?


LINES
------------------------------------------------------------

Visible?

Distinguishable?

Not too thick?

Not too thin?


MARKERS
------------------------------------------------------------

Necessary?

Visible?

Not overcrowded?


LEGEND
------------------------------------------------------------

Clear case names?

Does not hide data?

Readable?


ANNOTATIONS
------------------------------------------------------------

Necessary?

Correct?

Concise?


OUTPUT
------------------------------------------------------------

Correct physical dimensions?

Correct DPI?

Correct format?

PDF / PNG / SVG?


FINAL CHECK
------------------------------------------------------------

Open exported file.

Check at final document size.
"""


# ============================================================
# 79. COMPLETE PUBLICATION WORKFLOW
# ============================================================

"""
Raw Experimental / Simulation Data
              ↓
Validate Data
              ↓
Select Required Variables
              ↓
Process Data
              ↓
Determine Final Figure Purpose
              ↓
Journal / Thesis / Conference
              ↓
Check Publication Requirements
              ↓
Set Physical Dimensions
              ↓
Create Figure
              ↓
Plot Data
              ↓
Set Axis Scale
              ↓
Set Limits
              ↓
Set Ticks
              ↓
Add Labels + Units
              ↓
Add Legend
              ↓
Add Necessary Annotations
              ↓
Check Grayscale Readability
              ↓
Check Final Size
              ↓
Export PNG / PDF / SVG
              ↓
Open Exported Files
              ↓
Insert into Document
              ↓
Check Again
"""


# ============================================================
# 80. ENGINEERING PUBLICATION WORKFLOW
# ============================================================

"""
Example:

Frequency-domain converter comparison


CSV / Measurement Data
        ↓
Frequency [Hz]
Magnitude [dBµV]
        ↓
Validate Data
        ↓
Select Cases
        ↓
10 kHz to 30 MHz
        ↓
Logarithmic X-axis
        ↓
Linear dBµV Y-axis
        ↓
Different Line Styles
        ↓
Engineering Frequency Labels
        ↓
Readable Legend
        ↓
Publication-Sized Figure
        ↓
PDF
+
High-Resolution PNG
+
SVG
        ↓
Paper / Thesis / Report
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
PUBLICATION-QUALITY PLOTS


1. PUBLICATION QUALITY IS NOT ONLY DPI

A strong figure requires:

Correct data

Readable text

Correct units

Appropriate axes

Clear legend

Appropriate figure dimensions

Suitable resolution


------------------------------------------------------------


2. PHYSICAL FIGURE SIZE

Matplotlib uses inches:

fig, ax = plt.subplots(
    figsize=(
        width,
        height
    )
)


------------------------------------------------------------


3. MM TO INCHES

inches = mm / 25.4


------------------------------------------------------------


4. EXAMPLE COLUMN WIDTHS

Educational examples:

Single column:

~88 mm


Double column:

~178 mm


These are NOT universal requirements.


------------------------------------------------------------


5. DESIGN NEAR FINAL SIZE

Avoid:

Huge Plot
    ↓
Shrink Dramatically


Prefer:

Create Near Final Width
    ↓
Export


------------------------------------------------------------


6. FONT SIZE

Use readable:

Axis labels

Tick labels

Legend

Annotations


DPI does not control font size.


------------------------------------------------------------


7. LINE WIDTH

Use:

linewidth=


Choose according to final figure size.


------------------------------------------------------------


8. MARKER SIZE

Use:

markersize=


For dense data:

markevery=


may improve readability.


------------------------------------------------------------


9. DO NOT RELY ONLY ON COLOR

Combine:

Color

Line Style

Marker Shape


------------------------------------------------------------


10. AXIS LIMITS

Use scientifically justified:

set_xlim()

set_ylim()


Do not manipulate limits to exaggerate results.


------------------------------------------------------------


11. MAJOR TICKS

MultipleLocator()


Example:

ax.yaxis.set_major_locator(
    MultipleLocator(
        10
    )
)


------------------------------------------------------------


12. MINOR TICKS

MultipleLocator()

AutoMinorLocator()

LogLocator()


depending on the axis type.


------------------------------------------------------------


13. FREQUENCY PLOT

Frequency [Hz]

    ↓

Logarithmic X-axis


Magnitude [dBµV]

    ↓

Linear numerical Y-axis


------------------------------------------------------------


14. ENGINEERING FREQUENCY LABELS

Examples:

10 kHz

100 kHz

1 MHz

10 MHz


------------------------------------------------------------


15. LEGEND

Keep it:

Readable

Compact

Away from important data


------------------------------------------------------------


16. TITLES

Useful for:

Tutorials

Reports

Presentations


For journal figures, the caption may make an internal
title unnecessary.


------------------------------------------------------------


17. ANNOTATIONS

Use only when they add scientific value.


Examples:

Maximum

Resonance

Operating limit

Important comparison


------------------------------------------------------------


18. rcParams

Useful for global styling.


------------------------------------------------------------


19. rc_context()

Useful for temporarily applying a publication style:

with mpl.rc_context(
    publication_style
):

    ...


This avoids permanently changing all later Matplotlib
figures.


------------------------------------------------------------


20. PNG

Useful raster output.

Example:

fig.savefig(
    "figure.png",
    dpi=600,
    bbox_inches="tight"
)


------------------------------------------------------------


21. PDF

Useful vector-oriented output for scientific line plots.


------------------------------------------------------------


22. SVG

Useful scalable vector-oriented output.


------------------------------------------------------------


23. FINAL EXPORT

Recommended flexible workflow:

PNG
+
PDF
+
SVG


when appropriate.


------------------------------------------------------------


24. GRAYSCALE TEST

A figure should ideally remain understandable without
depending entirely on color.


------------------------------------------------------------


25. FINAL-SIZE TEST

Do not evaluate the figure only in a large Python window.

Inspect it at approximately:

Final Paper Size


------------------------------------------------------------


26. PUBLICATION CHECK

Always check:

Journal instructions

Conference instructions

Publisher instructions

Thesis requirements


before final submission.


------------------------------------------------------------


27. REPRODUCIBILITY

Keep formatting parameters in Python.

Avoid unnecessary manual modification after export.


------------------------------------------------------------


28. MOST IMPORTANT PRINCIPLE

Publication-quality plotting is scientific communication.

The objective is not to make the figure:

Decorative


The objective is to make the result:

Correct

Clear

Readable

Reproducible

and

Scientifically interpretable.


------------------------------------------------------------


NEXT:

21_fft_frequency_plot.py


The next file will focus specifically on a complete
frequency-domain workflow:

Time-domain signal concept

Sampling frequency

FFT concept

Frequency vector

Positive-frequency spectrum

Magnitude calculation

Amplitude normalization

Frequency selection

10 kHz to 30 MHz example

Linear vs logarithmic frequency axis

dB and dBµV concepts

CSV-based FFT data

Multiple-case FFT comparison

Switching-frequency harmonics

Selected-frequency extraction

Automatic peak identification

Frequency-band analysis

and engineering interpretation.
"""
