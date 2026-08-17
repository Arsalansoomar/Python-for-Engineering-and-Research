"""
============================================================
Python for Engineering and Research
15 - Axis Limits and Ticks
============================================================

Purpose:
    Demonstrate precise control of X-axis and Y-axis limits,
    major ticks, minor ticks, tick spacing, scientific
    notation, engineering-frequency labels, and subplot axes.

Topics:
    1. Why axis control matters
    2. Automatic vs manual limits
    3. set_xlim()
    4. set_ylim()
    5. axis()
    6. Major ticks
    7. Minor ticks
    8. MultipleLocator
    9. AutoMinorLocator
    10. Custom tick positions
    11. Custom tick labels
    12. Scientific notation
    13. ScalarFormatter
    14. Engineering frequency labels
    15. Logarithmic-axis ticks
    16. Tick direction and appearance
    17. Shared subplot limits
    18. Independent subplot limits
    19. Zooming vs filtering data
    20. Reusable axis-formatting function
    21. Saving figures
    22. Common mistakes
    23. Key takeaways

Sample File:
    sample_data/fft_example.csv

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHY AXIS CONTROL MATTERS
# ============================================================

"""
A technically correct plot can still be difficult to read
if its axes are poorly selected.

Axis control affects:

- Visible data range
- Comparison between cases
- Tick spacing
- Numerical readability
- Scientific notation
- Publication quality
- Interpretation


Example:

Automatic Y-axis:

93.72 to 95.64


Manual Y-axis:

90 to 100


Both may be valid, but they communicate the data differently.


Therefore axis limits should be selected based on:

- Physical meaning
- Engineering limits
- Comparison requirements
- Publication clarity
"""


# ============================================================
# 2. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pathlib import Path

from matplotlib.ticker import (
    MultipleLocator,
    AutoMinorLocator,
    FuncFormatter,
    ScalarFormatter,
    LogLocator
)


# ============================================================
# 3. BASIC EXAMPLE DATA
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


# ============================================================
# 4. AUTOMATIC AXIS LIMITS
# ============================================================

"""
By default, Matplotlib chooses axis limits automatically.

This is convenient for quick visualization.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage,
    marker="o",
    linewidth=2
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Automatic Axis Limits"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 5. CHECK CURRENT AXIS LIMITS
# ============================================================

"""
Matplotlib allows us to inspect the current limits.

Use:

ax.get_xlim()

ax.get_ylim()
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage
)


print(
    "\n--- Automatic Limits ---"
)


print(
    "X limits:",
    ax.get_xlim()
)


print(
    "Y limits:",
    ax.get_ylim()
)


plt.close(
    fig
)


# ============================================================
# 6. MANUAL X-AXIS LIMITS
# ============================================================

"""
Use:

ax.set_xlim(
    minimum,
    maximum
)
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage,
    marker="o"
)


ax.set_xlim(
    0,
    10
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Manual X-Axis Limits"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 7. MANUAL Y-AXIS LIMITS
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage,
    marker="o"
)


ax.set_ylim(
    0,
    105
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Manual Y-Axis Limits"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 8. SET BOTH X AND Y LIMITS
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage,
    marker="o",
    linewidth=2
)


ax.set_xlim(
    0,
    10
)


ax.set_ylim(
    0,
    105
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Controlled Axis Limits"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 9. SET ONLY LEFT / RIGHT LIMIT
# ============================================================

"""
You do not always need to specify both limits.

Examples:

ax.set_xlim(
    left=0
)

ax.set_xlim(
    right=10
)

ax.set_ylim(
    bottom=0
)

ax.set_ylim(
    top=100
)
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage
)


ax.set_xlim(
    left=0
)


ax.set_ylim(
    bottom=0
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


plt.tight_layout()

plt.show())


# ============================================================
# 10. axis()
# ============================================================

"""
Matplotlib also provides:

ax.axis(
    [
        xmin,
        xmax,
        ymin,
        ymax
    ]
)


Example:

ax.axis(
    [
        0,
        10,
        0,
        105
    ]
)


However, set_xlim() and set_ylim() are often clearer in
engineering code.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage
)


ax.axis(
    [
        0,
        10,
        0,
        105
    ]
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


plt.tight_layout()

plt.show()


# ============================================================
# 11. WHAT ARE TICKS?
# ============================================================

"""
Ticks are the numerical positions shown along an axis.

Example:

0
2
4
6
8
10


A tick usually consists of:

Tick position
      +
Tick mark
      +
Tick label


Engineering figures often require controlled tick spacing.
"""


# ============================================================
# 12. CUSTOM X-TICK POSITIONS
# ============================================================

"""
Use:

ax.set_xticks()
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage
)


ax.set_xticks(
    [
        0,
        2,
        4,
        6,
        8,
        10
    ]
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


plt.tight_layout()

plt.show()


# ============================================================
# 13. CUSTOM Y-TICK POSITIONS
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage
)


ax.set_yticks(
    [
        0,
        20,
        40,
        60,
        80,
        100
    ]
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


plt.tight_layout()

plt.show()


# ============================================================
# 14. NumPy arange() FOR TICKS
# ============================================================

"""
Instead of manually listing every tick:

np.arange(
    start,
    stop,
    step
)


can generate regular tick locations.
"""


x_ticks = np.arange(
    0,
    11,
    2
)


y_ticks = np.arange(
    0,
    101,
    20
)


print(
    "\n--- X Ticks ---"
)


print(
    x_ticks
)


print(
    "\n--- Y Ticks ---"
)


print(
    y_ticks
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage
)


ax.set_xlim(
    0,
    10
)

ax.set_ylim(
    0,
    100
)


ax.set_xticks(
    x_ticks
)

ax.set_yticks(
    y_ticks
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


plt.tight_layout()

plt.show()


# ============================================================
# 15. MultipleLocator
# ============================================================

"""
MultipleLocator provides another convenient way to control
regular tick spacing.

Example:

Major X ticks every:

2 ms


Major Y ticks every:

20 V
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage
)


ax.set_xlim(
    0,
    10
)

ax.set_ylim(
    0,
    100
)


ax.xaxis.set_major_locator(
    MultipleLocator(
        2
    )
)


ax.yaxis.set_major_locator(
    MultipleLocator(
        20
    )
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


plt.tight_layout()

plt.show()


# ============================================================
# 16. MAJOR VS MINOR TICKS
# ============================================================

"""
MAJOR TICKS

Main labeled divisions.

Example:

0
20
40
60
80
100


MINOR TICKS

Smaller divisions between major ticks.

Example:

10
30
50
70
90


Minor ticks improve detailed reading without adding too
many numerical labels.
"""


# ============================================================
# 17. AutoMinorLocator
# ============================================================

"""
AutoMinorLocator automatically adds minor divisions between
major ticks.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage
)


ax.set_xlim(
    0,
    10
)

ax.set_ylim(
    0,
    100
)


ax.xaxis.set_major_locator(
    MultipleLocator(
        2
    )
)


ax.yaxis.set_major_locator(
    MultipleLocator(
        20
    )
)


ax.xaxis.set_minor_locator(
    AutoMinorLocator(
        2
    )
)


ax.yaxis.set_minor_locator(
    AutoMinorLocator(
        2
    )
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True,
    which="major"
)


ax.grid(
    True,
    which="minor",
    alpha=0.4
)


plt.tight_layout()

plt.show()


# ============================================================
# 18. EXPLICIT MINOR TICK SPACING
# ============================================================

"""
Instead of AutoMinorLocator, minor tick spacing can be
specified explicitly.

Example:

Major X:

2 ms

Minor X:

0.5 ms
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage
)


ax.xaxis.set_major_locator(
    MultipleLocator(
        2
    )
)


ax.xaxis.set_minor_locator(
    MultipleLocator(
        0.5
    )
)


ax.yaxis.set_major_locator(
    MultipleLocator(
        20
    )
)


ax.yaxis.set_minor_locator(
    MultipleLocator(
        5
    )
)


ax.set_xlim(
    0,
    10
)

ax.set_ylim(
    0,
    100
)


ax.grid(
    True,
    which="major"
)


ax.grid(
    True,
    which="minor",
    alpha=0.4
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


plt.tight_layout()

plt.show()


# ============================================================
# 19. CUSTOM TICK LABELS
# ============================================================

"""
Tick positions and displayed labels do not have to be
identical.

Example:

Positions:

0
25
50
75
100


Labels:

No Load
25%
50%
75%
Full Load
"""


load_percent = np.array(
    [
        0,
        25,
        50,
        75,
        100
    ]
)


efficiency = np.array(
    [
        0,
        91.5,
        94.0,
        95.2,
        94.8
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency,
    marker="o"
)


ax.set_xticks(
    [
        0,
        25,
        50,
        75,
        100
    ]
)


ax.set_xticklabels(
    [
        "No Load",
        "25%",
        "50%",
        "75%",
        "Full Load"
    ]
)


ax.set_xlabel(
    "Operating Condition"
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
# 20. NOTE ABOUT CUSTOM LABELS
# ============================================================

"""
Custom labels can improve readability.

However, do not replace meaningful numerical values with
descriptive labels if the numerical scale itself is
important to interpretation.
"""


# ============================================================
# 21. ROTATE TICK LABELS
# ============================================================

"""
Long category labels may overlap.

Use:

rotation=
"""


categories = [

    "Unshielded Baseline",

    "Optimized Design",

    "Localized Design",

    "Extended Design"

]


values = [

    102,

    88,

    94,

    91

]


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.bar(
    categories,
    values
)


ax.tick_params(
    axis="x",
    labelrotation=20
)


ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 22. tick_params()
# ============================================================

"""
tick_params() controls tick appearance.

Useful parameters include:

axis

which

direction

length

width

labelsize

labelrotation
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage
)


ax.tick_params(
    axis="both",
    which="major",
    direction="in",
    length=6,
    width=1
)


ax.tick_params(
    axis="both",
    which="minor",
    direction="in",
    length=3
)


ax.xaxis.set_minor_locator(
    AutoMinorLocator()
)


ax.yaxis.set_minor_locator(
    AutoMinorLocator()
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


plt.tight_layout()

plt.show()


# ============================================================
# 23. TICKS ON BOTH SIDES
# ============================================================

"""
Research figures sometimes use inward ticks on all sides.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage
)


ax.tick_params(
    axis="both",
    which="both",
    direction="in",
    top=True,
    right=True
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


plt.tight_layout()

plt.show()


# ============================================================
# 24. SCIENTIFIC NOTATION
# ============================================================

"""
Large or very small values can make axes difficult to read.

Example:

0
1000000
2000000
3000000


Scientific notation may display:

0
1
2
3

×10^6
"""


frequency = np.array(
    [
        1e6,
        2e6,
        3e6,
        4e6,
        5e6
    ]
)


magnitude = np.array(
    [
        80,
        84,
        78,
        72,
        68
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    frequency,
    magnitude,
    marker="o"
)


ax.ticklabel_format(
    axis="x",
    style="sci",
    scilimits=(
        0,
        0
    )
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 25. CONTROL SCIENTIFIC NOTATION RANGE
# ============================================================

"""
scilimits determines when scientific notation is used.

Example:

scilimits=(-3, 3)


means scientific notation may be used when values are
outside approximately:

10^-3 to 10^3
"""


# ============================================================
# 26. ScalarFormatter
# ============================================================

"""
ScalarFormatter provides more detailed numerical-format
control.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    frequency,
    magnitude
)


formatter = ScalarFormatter(
    useMathText=True
)


formatter.set_scientific(
    True
)


formatter.set_powerlimits(
    (
        0,
        0
    )
)


ax.xaxis.set_major_formatter(
    formatter
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 27. ENGINEERING FREQUENCY LABELS
# ============================================================

"""
For frequency-domain engineering plots, labels such as:

10 kHz

100 kHz

1 MHz

10 MHz


can be easier to read than:

10000

100000

1000000

10000000
"""


def format_frequency(
    value,
    position=None
):
    """
    Convert frequency into engineering notation.
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
# 28. LOAD SAMPLE FFT DATA
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
# 29. LOG-FREQUENCY PLOT WITH CUSTOM TICKS
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    fft_data["Frequency_Hz"],
    fft_data["Unshielded_dBuV"],
    linewidth=2
)


ax.set_xscale(
    "log"
)


major_frequencies = [

    10e3,

    100e3,

    1e6,

    10e6

]


ax.set_xticks(
    major_frequencies
)


ax.xaxis.set_major_formatter(
    FuncFormatter(
        format_frequency
    )
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


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 30. LOG AXIS MAJOR TICK LOCATOR
# ============================================================

"""
LogLocator can automatically place logarithmic ticks.

base=10

means decades are based on powers of ten.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    fft_data["Frequency_Hz"],
    fft_data["Unshielded_dBuV"]
)


ax.set_xscale(
    "log"
)


ax.xaxis.set_major_locator(
    LogLocator(
        base=10.0
    )
)


ax.set_xlim(
    10e3,
    30e6
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 31. LOG AXIS MINOR TICKS
# ============================================================

"""
Minor logarithmic ticks can be placed between decades.

Example:

Between:

100 kHz
and
1 MHz


minor ticks can correspond to:

200 kHz
300 kHz
...
900 kHz
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    fft_data["Frequency_Hz"],
    fft_data["Unshielded_dBuV"]
)


ax.set_xscale(
    "log"
)


ax.xaxis.set_major_locator(
    LogLocator(
        base=10.0
    )
)


ax.xaxis.set_minor_locator(
    LogLocator(
        base=10.0,
        subs=np.arange(
            2,
            10
        ) * 0.1
    )
)


ax.set_xlim(
    10e3,
    30e6
)


ax.grid(
    True,
    which="major"
)


ax.grid(
    True,
    which="minor",
    alpha=0.4
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


plt.tight_layout()

plt.show()


# ============================================================
# 32. CUSTOM Y-AXIS TICKS FOR SPECTRUM
# ============================================================

"""
Suppose a spectrum plot should use:

0 to 120 dBµV

with major ticks every:

20 dB
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    fft_data["Frequency_Hz"],
    fft_data["Unshielded_dBuV"]
)


ax.set_xscale(
    "log"
)


ax.set_xlim(
    10e3,
    30e6
)


ax.set_ylim(
    0,
    120
)


ax.yaxis.set_major_locator(
    MultipleLocator(
        20
    )
)


ax.yaxis.set_minor_locator(
    MultipleLocator(
        5
    )
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.grid(
    True,
    which="major"
)


ax.grid(
    True,
    which="minor",
    alpha=0.3
)


plt.tight_layout()

plt.show()


# ============================================================
# 33. COMPARE MULTIPLE FREQUENCY CASES
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


ax.set_ylim(
    0,
    120
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


ax.yaxis.set_major_locator(
    MultipleLocator(
        20
    )
)


ax.yaxis.set_minor_locator(
    MultipleLocator(
        5
    )
)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.grid(
    True,
    which="major"
)


ax.grid(
    True,
    which="minor",
    alpha=0.3
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 34. AUTOMATIC LIMITS WITH MARGIN
# ============================================================

"""
Sometimes we want the limits to follow the data but include
some additional space.

Matplotlib provides:

ax.margins()
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage,
    marker="o"
)


ax.margins(
    x=0.05,
    y=0.10
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


plt.tight_layout()

plt.show()


# ============================================================
# 35. REMOVE X MARGINS
# ============================================================

"""
For time-domain plots, it can be useful to make the data
start exactly at the left and right boundaries.

Use:

ax.margins(
    x=0
)
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage
)


ax.margins(
    x=0
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


plt.tight_layout()

plt.show()


# ============================================================
# 36. ZOOM INTO A DATA REGION
# ============================================================

"""
Suppose only:

5 ms to 10 ms

is visually important.

Use:

set_xlim()
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage,
    marker="o"
)


ax.set_xlim(
    5,
    10
)


ax.set_ylim(
    70,
    100
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Zoomed Operating Region"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 37. ZOOMING DOES NOT FILTER DATA
# ============================================================

"""
Important:

ax.set_xlim(
    5,
    10
)


changes only the visible plot area.

The original arrays still contain all values.


If calculations should use only:

5 <= Time <= 10


the data must be filtered separately.
"""


# ============================================================
# 38. FILTER DATA FOR CALCULATION
# ============================================================

mask = (
    (
        time_ms
        >= 5
    )
    &
    (
        time_ms
        <= 10
    )
)


selected_time = time_ms[
    mask
]


selected_voltage = voltage[
    mask
]


print(
    "\n--- Filtered Time ---"
)


print(
    selected_time
)


print(
    "\n--- Filtered Voltage ---"
)


print(
    selected_voltage
)


# ============================================================
# 39. FIXED LIMITS FOR FAIR CASE COMPARISON
# ============================================================

"""
When several figures compare similar cases, identical axis
limits can improve fairness.

Example:

Figure A:

0 to 100 V


Figure B:

0 to 100 V


Figure C:

0 to 100 V


If every figure uses a different automatic Y-axis range,
small differences may appear larger or smaller than they
really are.
"""


case_a = np.array(
    [
        90,
        92,
        94,
        96,
        95
    ]
)


case_b = np.array(
    [
        91,
        93,
        95,
        97,
        96
    ]
)


x_case = np.array(
    [
        1,
        2,
        3,
        4,
        5
    ]
)


fig, axes = plt.subplots(
    2,
    1,
    figsize=(7, 6),
    sharex=True,
    sharey=True
)


axes[0].plot(
    x_case,
    case_a
)

axes[0].set_title(
    "Case A"
)


axes[1].plot(
    x_case,
    case_b
)

axes[1].set_title(
    "Case B"
)


for ax in axes:

    ax.set_ylim(
        85,
        100
    )

    ax.grid(
        True
    )


axes[1].set_xlabel(
    "Sample"
)


fig.supylabel(
    "Voltage [V]"
)


plt.tight_layout()

plt.show()


# ============================================================
# 40. DIFFERENT LIMITS FOR DIFFERENT PHYSICAL VARIABLES
# ============================================================

"""
For variables with different units, independent Y-axis
limits are usually appropriate.
"""


current = np.array(
    [
        0,
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


fig, axes = plt.subplots(
    3,
    1,
    figsize=(7, 8),
    sharex=True
)


axes[0].plot(
    time_ms,
    voltage
)

axes[0].set_ylim(
    0,
    105
)

axes[0].set_ylabel(
    "Voltage [V]"
)


axes[1].plot(
    time_ms,
    current
)

axes[1].set_ylim(
    0,
    3
)

axes[1].set_ylabel(
    "Current [A]"
)


axes[2].plot(
    time_ms,
    temperature
)

axes[2].set_ylim(
    20,
    80
)

axes[2].set_ylabel(
    "Temperature [°C]"
)

axes[2].set_xlabel(
    "Time [ms]"
)


for ax in axes:

    ax.grid(
        True
    )


plt.tight_layout()

plt.show()


# ============================================================
# 41. DECIMAL TICK SPACING
# ============================================================

"""
MultipleLocator also works with decimal values.

Example:

Efficiency:

90.0
90.5
91.0
91.5
...
"""


load = np.array(
    [
        20,
        40,
        60,
        80,
        100
    ]
)


efficiency_data = np.array(
    [
        91.2,
        93.1,
        94.6,
        95.3,
        94.9
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load,
    efficiency_data,
    marker="o"
)


ax.set_ylim(
    90,
    96
)


ax.yaxis.set_major_locator(
    MultipleLocator(
        1
    )
)


ax.yaxis.set_minor_locator(
    MultipleLocator(
        0.25
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


ax.grid(
    True,
    which="minor",
    alpha=0.3
)


plt.tight_layout()

plt.show()


# ============================================================
# 42. CUSTOM NUMERIC FORMATTER
# ============================================================

"""
FuncFormatter can control exactly how tick labels appear.
"""


def one_decimal(
    value,
    position
):

    return (
        f"{value:.1f}"
    )


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load,
    efficiency_data,
    marker="o"
)


ax.yaxis.set_major_formatter(
    FuncFormatter(
        one_decimal
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
# 43. PERCENTAGE FORMATTER
# ============================================================

"""
If raw values are:

0.90

0.95

1.00


they can be displayed as:

90%

95%

100%
"""


normalized_efficiency = np.array(
    [
        0.91,
        0.93,
        0.95,
        0.96,
        0.95
    ]
)


def percentage_formatter(
    value,
    position
):

    return (
        f"{value * 100:.0f}%"
    )


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load,
    normalized_efficiency,
    marker="o"
)


ax.yaxis.set_major_formatter(
    FuncFormatter(
        percentage_formatter
    )
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 44. REUSABLE AXIS-FORMATTING FUNCTION
# ============================================================

def configure_linear_axes(
    ax,
    x_min=None,
    x_max=None,
    y_min=None,
    y_max=None,
    x_major=None,
    y_major=None,
    x_minor=None,
    y_minor=None
):
    """
    Configure axis limits and regular tick spacing.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to configure.

    x_min, x_max : float, optional
        X-axis limits.

    y_min, y_max : float, optional
        Y-axis limits.

    x_major : float, optional
        Major X tick interval.

    y_major : float, optional
        Major Y tick interval.

    x_minor : float, optional
        Minor X tick interval.

    y_minor : float, optional
        Minor Y tick interval.
    """

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


    ax.grid(
        True,
        which="major"
    )


    ax.grid(
        True,
        which="minor",
        alpha=0.3
    )


# ============================================================
# 45. USE REUSABLE FUNCTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    voltage,
    linewidth=2
)


configure_linear_axes(

    ax=ax,

    x_min=0,

    x_max=10,

    y_min=0,

    y_max=100,

    x_major=2,

    y_major=20,

    x_minor=0.5,

    y_minor=5

)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Reusable Axis Configuration"
)


plt.tight_layout()

plt.show()


# ============================================================
# 46. REUSABLE FREQUENCY-AXIS FUNCTION
# ============================================================

def configure_frequency_axis(
    ax,
    frequency_min,
    frequency_max,
    major_ticks=None
):
    """
    Configure an engineering logarithmic frequency axis.
    """

    if frequency_min <= 0:

        raise ValueError(
            "Minimum frequency must be greater than zero "
            "for a logarithmic axis."
        )


    if frequency_max <= frequency_min:

        raise ValueError(
            "Maximum frequency must be greater than "
            "minimum frequency."
        )


    ax.set_xscale(
        "log"
    )


    ax.set_xlim(
        frequency_min,
        frequency_max
    )


    if major_ticks is not None:

        ax.set_xticks(
            major_ticks
        )


    ax.xaxis.set_major_formatter(
        FuncFormatter(
            format_frequency
        )
    )


    ax.grid(
        True,
        which="major"
    )


    ax.grid(
        True,
        which="minor",
        alpha=0.3
    )


# ============================================================
# 47. USE FREQUENCY-AXIS FUNCTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for case_name, column_name in frequency_cases.items():

    ax.plot(
        fft_data["Frequency_Hz"],
        fft_data[column_name],
        linewidth=2,
        label=case_name
    )


configure_frequency_axis(

    ax=ax,

    frequency_min=10e3,

    frequency_max=30e6,

    major_ticks=[
        10e3,
        100e3,
        1e6,
        10e6
    ]

)


ax.set_ylim(
    0,
    120
)


ax.yaxis.set_major_locator(
    MultipleLocator(
        20
    )
)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 48. SAVE FINAL FIGURE
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


configure_frequency_axis(

    ax=ax,

    frequency_min=10e3,

    frequency_max=30e6,

    major_ticks=[
        10e3,
        100e3,
        1e6,
        10e6
    ]

)


ax.set_ylim(
    0,
    120
)


ax.yaxis.set_major_locator(
    MultipleLocator(
        20
    )
)


ax.yaxis.set_minor_locator(
    MultipleLocator(
        5
    )
)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Controlled Frequency-Domain Axes"
)


ax.legend()


plt.tight_layout()


# ============================================================
# 49. SAVE PNG
# ============================================================

png_file = (
    output_figure_folder
    / "axis_limits_and_ticks.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 50. SAVE PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "axis_limits_and_ticks.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 51. SAVE SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "axis_limits_and_ticks.svg"
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
# 52. COMMON MISTAKE - LIMITS THAT HIDE DATA
# ============================================================

"""
Suppose data contain values up to:

110 V


but:

ax.set_ylim(
    0,
    100
)


is used.


Values above 100 V will not be visible.

Always check the actual data range before setting limits.
"""


# ============================================================
# 53. COMMON MISTAKE - TRUNCATED BAR-PLOT AXIS
# ============================================================

"""
Bar plots usually communicate absolute magnitude.

Example:

Values:

95
96


Using:

Y-axis:
94.5 to 96.5


can visually exaggerate the difference.


For many bar plots, starting at:

0

is generally safer.


Line and scatter plots do not always require a zero
baseline because they often emphasize trends rather than
absolute bar lengths.
"""


# ============================================================
# 54. COMMON MISTAKE - DIFFERENT LIMITS BETWEEN CASES
# ============================================================

"""
Suppose:

Case A figure:

Y-axis = 90 to 100


Case B figure:

Y-axis = 0 to 100


The apparent variation will look very different.


For fair case comparisons, use consistent limits whenever
the quantities and context are comparable.
"""


# ============================================================
# 55. COMMON MISTAKE - TOO MANY TICKS
# ============================================================

"""
Example:

0
0.1
0.2
0.3
...
100


would produce hundreds of labels.


Use a tick interval that supports interpretation without
cluttering the figure.
"""


# ============================================================
# 56. COMMON MISTAKE - TOO FEW TICKS
# ============================================================

"""
An axis containing only:

0

and

100


may make intermediate values difficult to estimate.

Choose meaningful major intervals.
"""


# ============================================================
# 57. COMMON MISTAKE - MANUAL LABELS WITHOUT POSITIONS
# ============================================================

"""
Avoid changing only tick labels without controlling the
corresponding tick positions.

Prefer:

ax.set_xticks(
    positions
)

ax.set_xticklabels(
    labels
)


This ensures each label corresponds to a known location.
"""


# ============================================================
# 58. COMMON MISTAKE - USING LINEAR TICK LOCATOR ON LOG AXIS
# ============================================================

"""
MultipleLocator works naturally on linear axes.

For logarithmic axes, use logarithmic tick logic such as:

LogLocator

or explicit log-spaced tick values.
"""


# ============================================================
# 59. COMMON MISTAKE - MIXING Hz AND MHz
# ============================================================

"""
Suppose the data are stored in:

Hz


but axis ticks are manually entered as:

1
5
10


while the label says:

Frequency [MHz]


Then the numerical scale is incorrect.


Either:

Convert data:

Frequency_MHz = Frequency_Hz / 1e6


or:

Keep data in Hz and format the displayed tick labels.
"""


# ============================================================
# 60. COMMON MISTAKE - OVER-ZOOMING
# ============================================================

"""
Excessively narrow axis limits can visually exaggerate
small differences.

Example:

Efficiency varies:

95.1%
to
95.3%


Y-axis:

95.05
to
95.35


may make a 0.2 percentage-point change appear very large.

Sometimes this zoom is scientifically useful, but it should
be clearly justified and interpreted carefully.
"""


# ============================================================
# 61. COMMON MISTAKE - CONFUSING ZOOM WITH DATA SELECTION
# ============================================================

"""
set_xlim()

and

set_ylim()


change what is VISIBLE.


They do NOT remove data.


For calculations, explicitly filter the dataset.
"""


# ============================================================
# 62. AXIS-LIMIT DECISION WORKFLOW
# ============================================================

"""
Create Plot
    ↓
Inspect Data Range
    ↓
Are Automatic Limits Clear?
      / \
    Yes  No
    ↓     ↓
Keep     Choose Manual Limits
          ↓
Check Physical Limits
          ↓
Check Comparison Requirements
          ↓
Set X / Y Limits
          ↓
Choose Major Tick Interval
          ↓
Choose Minor Tick Interval
          ↓
Check Labels
          ↓
Check Clutter
          ↓
Validate Figure
"""


# ============================================================
# 63. ENGINEERING EXAMPLES
# ============================================================

"""
TIME-DOMAIN VOLTAGE

X:

0 to 10 ms


Y:

0 to 100 V


Possible settings:

ax.set_xlim(
    0,
    10
)

ax.set_ylim(
    0,
    100
)

ax.xaxis.set_major_locator(
    MultipleLocator(
        2
    )
)


------------------------------------------------------------


EFFICIENCY

X:

0 to 100% load


Y:

90 to 100% efficiency


Possible settings:

ax.set_xlim(
    0,
    100
)

ax.set_ylim(
    90,
    100
)


------------------------------------------------------------


FFT / EMI

X:

10 kHz to 30 MHz

LOGARITHMIC


Y:

0 to 120 dBµV


Possible settings:

ax.set_xscale(
    "log"
)

ax.set_xlim(
    10e3,
    30e6
)

ax.set_ylim(
    0,
    120
)
"""


# ============================================================
# 64. PUBLICATION FIGURE PRINCIPLE
# ============================================================

"""
Axis limits and ticks should help the reader understand
the result.

They should NOT be selected merely to:

- Make differences look larger
- Hide unwanted values
- Force curves to appear similar
- Make results appear better


Scientific figures should remain visually fair and
traceable to the underlying data.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
AXIS LIMITS AND TICKS


1. SET X LIMIT

ax.set_xlim(
    xmin,
    xmax
)


------------------------------------------------------------


2. SET Y LIMIT

ax.set_ylim(
    ymin,
    ymax
)


------------------------------------------------------------


3. CHECK CURRENT LIMITS

ax.get_xlim()

ax.get_ylim()


------------------------------------------------------------


4. MAJOR TICKS

ax.xaxis.set_major_locator(
    MultipleLocator(
        2
    )
)


------------------------------------------------------------


5. MINOR TICKS

ax.xaxis.set_minor_locator(
    MultipleLocator(
        0.5
    )
)


or:

ax.xaxis.set_minor_locator(
    AutoMinorLocator()
)


------------------------------------------------------------


6. CUSTOM TICK POSITIONS

ax.set_xticks(
    [
        0,
        2,
        4,
        6,
        8,
        10
    ]
)


------------------------------------------------------------


7. CUSTOM TICK LABELS

ax.set_xticklabels(
    [
        "A",
        "B",
        "C"
    ]
)


Use with matching tick positions.


------------------------------------------------------------


8. SCIENTIFIC NOTATION

ax.ticklabel_format(
    axis="x",
    style="sci",
    scilimits=(
        0,
        0
    )
)


------------------------------------------------------------


9. LOG FREQUENCY TICKS

Use:

LogLocator

or explicit:

10 kHz
100 kHz
1 MHz
10 MHz


------------------------------------------------------------


10. ENGINEERING FREQUENCY FORMAT

10e3
    ↓
10 kHz


1e6
    ↓
1 MHz


------------------------------------------------------------


11. GRID CONTROL

ax.grid(
    True,
    which="major"
)


ax.grid(
    True,
    which="minor"
)


------------------------------------------------------------


12. TICK APPEARANCE

ax.tick_params(
    direction="in",
    top=True,
    right=True
)


------------------------------------------------------------


13. ZOOMING

ax.set_xlim(
    minimum,
    maximum
)


only changes the visible region.


------------------------------------------------------------


14. FILTERING

Filtering changes the actual dataset used for calculations.


------------------------------------------------------------


15. FAIR COMPARISON

When comparing cases:

Use consistent axis limits whenever appropriate.


------------------------------------------------------------


16. BAR PLOTS

A zero baseline is often preferable because bar length
represents magnitude.


------------------------------------------------------------


17. LINE / SCATTER PLOTS

A zero baseline is not always required, but narrow limits
should not be used misleadingly.


------------------------------------------------------------


18. IMPORTANT RESEARCH PRINCIPLE

Axis control is part of scientific communication.

Limits and ticks should improve interpretation without
distorting the result.


------------------------------------------------------------


NEXT:

16_legends_labels_annotations.py


The next file will focus on:

Axis labels

Engineering units

Titles

Legends

Legend position

Multiple legend columns

Custom legend names

Annotations

Arrows

Peak labels

Reference lines

Operating limits

Text boxes

Highlighting important points

Frequency peak annotation

Automatic peak detection

Research/publication figure labeling
"""
