"""
============================================================
Python for Engineering and Research
14 - Logarithmic Axis
============================================================

Purpose:
    Demonstrate linear and logarithmic axis scaling using
    Matplotlib for scientific and engineering data.

Topics:
    1. What is a logarithmic axis?
    2. Why use logarithmic scales?
    3. Linear vs logarithmic X-axis
    4. set_xscale("log")
    5. semilogx()
    6. Logarithmic Y-axis
    7. semilogy()
    8. Log-log plots
    9. loglog()
    10. Frequency-domain engineering data
    11. Plot FFT / EMI-style data from CSV
    12. Multiple frequency-domain cases
    13. Frequency-range selection
    14. Major and minor grid lines
    15. Frequency tick formatting
    16. Positive-value requirement
    17. Handling zero and negative values
    18. dB data and logarithmic axes
    19. Reusable plotting function
    20. Saving publication-quality figures
    21. Common mistakes
    22. Key takeaways

Sample File:
    sample_data/fft_example.csv

Expected Columns:
    Frequency_Hz
    Unshielded_dBuV
    Case_A_dBuV
    Case_B_dBuV
    Case_C_dBuV

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT IS A LOGARITHMIC AXIS?
# ============================================================

"""
A normal linear axis uses equal spacing for equal numerical
differences.

Example:

0
10
20
30
40


A logarithmic axis uses equal spacing for equal numerical
ratios.

Example:

10
100
1,000
10,000
100,000


Each step represents multiplication by 10.


These ranges are called:

DECADES


Example:

10 Hz to 100 Hz

100 Hz to 1 kHz

1 kHz to 10 kHz

10 kHz to 100 kHz

100 kHz to 1 MHz
"""


# ============================================================
# 2. WHY USE LOGARITHMIC AXES?
# ============================================================

"""
Logarithmic axes are useful when data span several orders
of magnitude.

Engineering examples:

- Frequency response
- FFT spectra
- EMI spectra
- Bode plots
- Impedance
- Gain
- Power spectral density
- Component frequency characteristics
- Switching-frequency analysis
- Filter response
- Device characteristics


Example frequency range:

10 kHz
to
30 MHz


Numerically:

10,000 Hz
to
30,000,000 Hz


This spans several orders of magnitude.
"""


# ============================================================
# 3. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pathlib import Path
from matplotlib.ticker import FuncFormatter


# ============================================================
# 4. SIMPLE FREQUENCY DATA
# ============================================================

frequency = np.array(
    [
        1e3,
        2e3,
        5e3,
        1e4,
        2e4,
        5e4,
        1e5,
        2e5,
        5e5,
        1e6,
        2e6,
        5e6,
        1e7
    ]
)


magnitude = np.array(
    [
        20,
        22,
        25,
        30,
        36,
        43,
        50,
        55,
        58,
        54,
        48,
        40,
        32
    ]
)


# ============================================================
# 5. LINEAR FREQUENCY AXIS
# ============================================================

"""
First plot the frequency data using a normal linear axis.

Notice that low-frequency values become compressed toward
the left side because the maximum frequency is much larger.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    frequency,
    magnitude,
    marker="o",
    linewidth=2
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dB]"
)

ax.set_title(
    "Frequency Response - Linear X-Axis"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 6. LOGARITHMIC X-AXIS
# ============================================================

"""
Use:

ax.set_xscale("log")


The plotted data remain unchanged.

Only the AXIS REPRESENTATION changes.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    frequency,
    magnitude,
    marker="o",
    linewidth=2
)


ax.set_xscale(
    "log"
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dB]"
)

ax.set_title(
    "Frequency Response - Logarithmic X-Axis"
)


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 7. LINEAR VS LOGARITHMIC
# ============================================================

"""
LINEAR AXIS

Equal distance means:

Equal DIFFERENCE


Example:

10 kHz → 20 kHz

has the same numerical difference as:

20 kHz → 30 kHz


------------------------------------------------------------


LOGARITHMIC AXIS

Equal distance means:

Equal RATIO


Example:

10 kHz → 100 kHz

100 kHz → 1 MHz

1 MHz → 10 MHz


Each interval represents:

×10
"""


# ============================================================
# 8. semilogx()
# ============================================================

"""
Instead of:

ax.plot(...)

ax.set_xscale("log")


Matplotlib also provides:

ax.semilogx()


Both approaches can create a logarithmic X-axis.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.semilogx(
    frequency,
    magnitude,
    marker="o",
    linewidth=2
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dB]"
)

ax.set_title(
    "Frequency Response Using semilogx()"
)


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 9. set_xscale("log") VS semilogx()
# ============================================================

"""
METHOD 1

ax.plot(
    x,
    y
)

ax.set_xscale(
    "log"
)


------------------------------------------------------------


METHOD 2

ax.semilogx(
    x,
    y
)


Both are valid.


Using:

set_xscale()

can sometimes be clearer when the plotting code is already
built around:

ax.plot()
"""


# ============================================================
# 10. LOGARITHMIC Y-AXIS
# ============================================================

"""
Sometimes the dependent variable spans several orders of
magnitude.

Example:

Impedance

Current

Power spectral density

Error

Loss


Use:

ax.set_yscale("log")
"""


x = np.array(
    [
        1,
        2,
        3,
        4,
        5,
        6
    ]
)


y = np.array(
    [
        1,
        10,
        100,
        1000,
        10000,
        100000
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    x,
    y,
    marker="o"
)


ax.set_yscale(
    "log"
)


ax.set_xlabel(
    "Sample"
)

ax.set_ylabel(
    "Magnitude [-]"
)

ax.set_title(
    "Logarithmic Y-Axis"
)


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 11. semilogy()
# ============================================================

"""
Equivalent shorthand:

ax.semilogy(
    x,
    y
)
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.semilogy(
    x,
    y,
    marker="o"
)


ax.set_xlabel(
    "Sample"
)

ax.set_ylabel(
    "Magnitude [-]"
)

ax.set_title(
    "Logarithmic Y-Axis Using semilogy()"
)


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 12. LOG-LOG PLOT
# ============================================================

"""
Sometimes BOTH X and Y span several orders of magnitude.

Use:

ax.set_xscale("log")

and:

ax.set_yscale("log")


or:

ax.loglog()
"""


frequency_log = np.logspace(
    1,
    6,
    100
)


impedance = (
    1e5
    / frequency_log
)


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    frequency_log,
    impedance
)


ax.set_xscale(
    "log"
)

ax.set_yscale(
    "log"
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Impedance [Ω]"
)

ax.set_title(
    "Log-Log Engineering Plot"
)


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 13. loglog()
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.loglog(
    frequency_log,
    impedance,
    linewidth=2
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Impedance [Ω]"
)

ax.set_title(
    "Impedance Using loglog()"
)


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 14. QUICK SCALE SUMMARY
# ============================================================

"""
LINEAR X + LINEAR Y

ax.plot(
    x,
    y
)


------------------------------------------------------------


LOG X + LINEAR Y

ax.semilogx(
    x,
    y
)


------------------------------------------------------------


LINEAR X + LOG Y

ax.semilogy(
    x,
    y
)


------------------------------------------------------------


LOG X + LOG Y

ax.loglog(
    x,
    y
)
"""


# ============================================================
# 15. USE SAMPLE FREQUENCY DATA
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


csv_file = (
    script_folder
    / "sample_data"
    / "fft_example.csv"
)


if not csv_file.exists():

    raise FileNotFoundError(
        f"\nFrequency-domain sample file not found:\n"
        f"{csv_file}"
    )


# ============================================================
# 16. READ FFT / FREQUENCY DATA
# ============================================================

fft_data = pd.read_csv(
    csv_file
)


print(
    "\n--- FFT Dataset ---"
)


print(
    fft_data.head()
)


print(
    "\n--- FFT Columns ---"
)


print(
    fft_data.columns.tolist()
)


# ============================================================
# 17. EXPECTED COLUMNS
# ============================================================

"""
Frequency_Hz

Unshielded_dBuV

Case_A_dBuV

Case_B_dBuV

Case_C_dBuV
"""


# ============================================================
# 18. CHECK FREQUENCY RANGE
# ============================================================

minimum_frequency = fft_data[
    "Frequency_Hz"
].min()


maximum_frequency = fft_data[
    "Frequency_Hz"
].max()


print(
    "\n--- Frequency Range ---"
)


print(
    f"Minimum Frequency = "
    f"{minimum_frequency:.0f} Hz"
)


print(
    f"Maximum Frequency = "
    f"{maximum_frequency:.0f} Hz"
)


# ============================================================
# 19. LINEAR FFT PLOT
# ============================================================

"""
First demonstrate why a linear X-axis is less useful for
a broad frequency range.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    fft_data[
        "Frequency_Hz"
    ],

    fft_data[
        "Unshielded_dBuV"
    ],

    linewidth=2

)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Frequency Spectrum - Linear Axis"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 20. LOGARITHMIC FFT / EMI-STYLE PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    fft_data[
        "Frequency_Hz"
    ],

    fft_data[
        "Unshielded_dBuV"
    ],

    linewidth=2,

    label="Unshielded"

)


ax.set_xscale(
    "log"
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Frequency Spectrum - Logarithmic Axis"
)


ax.grid(
    True,
    which="both"
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 21. IMPORTANT: dB DATA
# ============================================================

"""
The X-axis is logarithmic because frequency spans several
orders of magnitude.

However, the Y-axis contains:

dBµV


dB values already represent a logarithmic quantity.

Therefore it is normally NOT appropriate to additionally
apply:

ax.set_yscale("log")


to a dBµV axis.


Typical engineering spectrum:

Frequency [Hz]
    → logarithmic X-axis

Magnitude [dBµV]
    → linear numerical Y-axis


This is an important distinction.
"""


# ============================================================
# 22. MULTIPLE FFT CASES
# ============================================================

frequency_columns = {

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


for case_name, column_name in frequency_columns.items():

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


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Frequency-Domain Case Comparison"
)


ax.grid(
    True,
    which="both"
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 23. SELECT FREQUENCY RANGE
# ============================================================

"""
Suppose only:

100 kHz to 20 MHz

is required.

Filtering should normally be performed on the DATA rather
than only visually changing the X-axis limits when the
subset will also be used for calculations.
"""


frequency_min = 100e3

frequency_max = 20e6


selected_frequency_data = fft_data[
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


print(
    "\n--- Selected Frequency Data ---"
)


print(
    selected_frequency_data
)


# ============================================================
# 24. PLOT SELECTED FREQUENCY RANGE
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for case_name, column_name in frequency_columns.items():

    ax.plot(

        selected_frequency_data[
            "Frequency_Hz"
        ],

        selected_frequency_data[
            column_name
        ],

        linewidth=2,

        label=case_name

    )


ax.set_xscale(
    "log"
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Selected Frequency Range"
)


ax.grid(
    True,
    which="both"
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 25. AXIS LIMITS WITHOUT FILTERING
# ============================================================

"""
If the objective is only to visually zoom into a region:

ax.set_xlim()


can be used.

This does NOT remove data from the DataFrame.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for case_name, column_name in frequency_columns.items():

    ax.plot(

        fft_data[
            "Frequency_Hz"
        ],

        fft_data[
            column_name
        ],

        label=case_name

    )


ax.set_xscale(
    "log"
)


ax.set_xlim(
    100e3,
    20e6
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


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 26. FILTERING VS AXIS LIMIT
# ============================================================

"""
FILTER DATA

selected = data[
    (
        frequency >= minimum
    )
    &
    (
        frequency <= maximum
    )
]


Use when:

- Performing calculations
- Computing peaks
- Calculating averages
- Saving selected data
- Processing only a defined band


------------------------------------------------------------


AXIS LIMIT

ax.set_xlim(
    minimum,
    maximum
)


Use when:

- Only changing the visible plot region
- Keeping the full dataset unchanged
"""


# ============================================================
# 27. MAJOR AND MINOR GRID LINES
# ============================================================

"""
On logarithmic axes, Matplotlib distinguishes:

Major ticks

and

Minor ticks


Use:

which="both"

to display both.
"""


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


ax.grid(
    True,
    which="major",
    linewidth=0.8
)


ax.grid(
    True,
    which="minor",
    linewidth=0.4,
    alpha=0.5
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Major and Minor Logarithmic Grid"
)


plt.tight_layout()

plt.show()


# ============================================================
# 28. WHY MINOR TICKS MATTER
# ============================================================

"""
Between:

100 kHz

and

1 MHz


minor ticks may represent:

200 kHz

300 kHz

400 kHz

...

900 kHz


This helps readers estimate frequencies between major
decades.
"""


# ============================================================
# 29. ENGINEERING FREQUENCY FORMATTER
# ============================================================

"""
Scientific plots are often easier to read using:

10 kHz

100 kHz

1 MHz

10 MHz


instead of:

10000

100000

1000000

10000000
"""


def format_frequency(
    value,
    position
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
# 30. APPLY FREQUENCY FORMATTER
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for case_name, column_name in frequency_columns.items():

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


ax.xaxis.set_major_formatter(
    FuncFormatter(
        format_frequency
    )
)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Engineering Frequency Labels"
)


ax.grid(
    True,
    which="both"
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 31. CUSTOM MAJOR FREQUENCY TICKS
# ============================================================

"""
Sometimes specific major ticks are required.

Example:

10 kHz

100 kHz

1 MHz

10 MHz
"""


major_frequencies = [

    10e3,

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


ax.set_xscale(
    "log"
)


ax.set_xticks(
    major_frequencies
)


ax.xaxis.set_major_formatter(
    FuncFormatter(
        format_frequency
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
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 32. POSITIVE-VALUE REQUIREMENT
# ============================================================

"""
A conventional logarithmic axis cannot represent:

0

or

negative values


because:

log(0)

is undefined


and the real logarithm of a negative value is not defined.


Therefore, before using:

ax.set_xscale("log")


check that:

X > 0
"""


test_frequency = np.array(
    [
        0,
        100,
        1000,
        10000
    ]
)


print(
    "\n--- Positive Frequency Check ---"
)


print(
    test_frequency > 0
)


# ============================================================
# 33. FILTER NON-POSITIVE VALUES
# ============================================================

valid_frequency_mask = (
    test_frequency
    > 0
)


valid_frequency = test_frequency[
    valid_frequency_mask
]


print(
    "\nValid Frequencies:"
)


print(
    valid_frequency
)


# ============================================================
# 34. GENERAL POSITIVE-DATA FILTER
# ============================================================

"""
For logarithmic X data:
"""


example_x = np.array(
    [
        -10,
        0,
        1,
        10,
        100,
        1000
    ]
)


example_y = np.array(
    [
        3,
        4,
        5,
        6,
        7,
        8
    ]
)


valid = (
    example_x
    > 0
)


clean_x = example_x[
    valid
]


clean_y = example_y[
    valid
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.semilogx(
    clean_x,
    clean_y,
    marker="o"
)


ax.set_xlabel(
    "X"
)

ax.set_ylabel(
    "Y"
)


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show()


# ============================================================
# 35. LOGARITHMIC Y-AXIS POSITIVE REQUIREMENT
# ============================================================

"""
Likewise, if:

ax.set_yscale("log")


is used:

Y values must normally be positive.


Before plotting:

valid = y > 0


Then use:

x[valid]

y[valid]
"""


# ============================================================
# 36. WHAT ABOUT DATA CROSSING ZERO?
# ============================================================

"""
Some datasets contain:

Positive values

Zero

Negative values


Examples:

Current waveform

Voltage waveform

Residual error


A standard logarithmic axis is not appropriate for these
signals.


Possible alternatives include:

- Linear scale
- Absolute magnitude, when scientifically justified
- Symmetrical logarithmic scale using "symlog"


However, taking the absolute value changes the meaning of
signed data and should never be done automatically.
"""


# ============================================================
# 37. SYMMETRICAL LOG SCALE
# ============================================================

"""
Matplotlib provides:

symlog


for data containing both positive and negative values.

Example:

ax.set_yscale(
    "symlog"
)


This is more advanced and should only be used when the
scientific interpretation is clear.
"""


signed_x = np.linspace(
    -1000,
    1000,
    200
)


signed_y = signed_x


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    signed_x,
    signed_y
)


ax.set_yscale(
    "symlog"
)


ax.set_xlabel(
    "X"
)

ax.set_ylabel(
    "Y"
)

ax.set_title(
    "Symmetrical Logarithmic Scale"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 38. LOG SPACING WITH NumPy
# ============================================================

"""
NumPy can generate logarithmically spaced numerical values.

Use:

np.logspace()


Example:

10^1
to
10^6
"""


log_frequencies = np.logspace(
    1,
    6,
    10
)


print(
    "\n--- Log-Spaced Frequencies ---"
)


print(
    log_frequencies
)


# ============================================================
# 39. linspace() VS logspace()
# ============================================================

"""
np.linspace()

Creates evenly spaced VALUES.

Example:

0
25
50
75
100


------------------------------------------------------------


np.logspace()

Creates logarithmically spaced values.

Example:

10
100
1000
10000
100000
"""


linear_values = np.linspace(
    10,
    100000,
    6
)


log_values = np.logspace(
    1,
    5,
    6
)


print(
    "\nLinear Spacing:"
)


print(
    linear_values
)


print(
    "\nLogarithmic Spacing:"
)


print(
    log_values
)


# ============================================================
# 40. FREQUENCY-DECADE EXAMPLE
# ============================================================

"""
Engineering frequency ranges are often discussed by decade.

Example:

10 kHz → 100 kHz

100 kHz → 1 MHz

1 MHz → 10 MHz


Each interval is one decade.
"""


frequency_decades = np.array(
    [
        10e3,
        100e3,
        1e6,
        10e6
    ]
)


print(
    "\n--- Frequency Decades ---"
)


for value in frequency_decades:

    print(
        format_frequency(
            value,
            None
        )
    )


# ============================================================
# 41. CALCULATE PEAK WITHIN FREQUENCY BAND
# ============================================================

"""
Logarithmic visualization can be combined with numerical
analysis.

Example:

Find the maximum magnitude between:

100 kHz

and

10 MHz
"""


band_min = 100e3

band_max = 10e6


band_data = fft_data[
    (
        fft_data[
            "Frequency_Hz"
        ] >= band_min
    )
    &
    (
        fft_data[
            "Frequency_Hz"
        ] <= band_max
    )
]


peak_magnitude = band_data[
    "Unshielded_dBuV"
].max()


peak_index = band_data[
    "Unshielded_dBuV"
].idxmax()


peak_frequency = band_data.loc[
    peak_index,
    "Frequency_Hz"
]


print(
    "\n--- Peak in Selected Frequency Band ---"
)


print(
    "Peak Frequency:",
    format_frequency(
        peak_frequency,
        None
    )
)


print(
    f"Peak Magnitude = "
    f"{peak_magnitude:.2f} dBµV"
)


# ============================================================
# 42. ANNOTATE FREQUENCY PEAK
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
    s=60
)


ax.annotate(

    (
        f"Peak\n"
        f"{format_frequency(peak_frequency, None)}\n"
        f"{peak_magnitude:.1f} dBµV"
    ),

    xy=(
        peak_frequency,
        peak_magnitude
    ),

    xytext=(
        20,
        20
    ),

    textcoords="offset points"

)


ax.set_xscale(
    "log"
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


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 43. REUSABLE LOG-FREQUENCY FUNCTION
# ============================================================

def plot_log_frequency(
    dataframe,
    frequency_column,
    y_columns,
    labels,
    y_label,
    title,
    frequency_min=None,
    frequency_max=None
):
    """
    Plot one or more datasets against a logarithmic
    frequency axis.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Input dataset.

    frequency_column : str
        Column containing frequency values.

    y_columns : list
        Columns containing Y data.

    labels : list
        Legend labels.

    y_label : str
        Y-axis label.

    title : str
        Figure title.

    frequency_min : float, optional
        Minimum displayed frequency.

    frequency_max : float, optional
        Maximum displayed frequency.

    Returns
    -------
    fig, ax
        Matplotlib figure and axis.
    """

    required_columns = [

        frequency_column

    ] + y_columns


    missing_columns = [

        column

        for column in required_columns

        if column not in dataframe.columns

    ]


    if missing_columns:

        raise KeyError(
            f"Missing columns: "
            f"{missing_columns}"
        )


    if len(
        y_columns
    ) != len(
        labels
    ):

        raise ValueError(
            "Number of Y columns must match "
            "number of labels."
        )


    working_data = dataframe.copy()


    # Remove non-positive frequencies

    working_data = working_data[
        working_data[
            frequency_column
        ] > 0
    ]


    fig, ax = plt.subplots(
        figsize=(8, 4.8)
    )


    for column, label in zip(
        y_columns,
        labels
    ):

        ax.plot(

            working_data[
                frequency_column
            ],

            working_data[
                column
            ],

            linewidth=2,

            label=label

        )


    ax.set_xscale(
        "log"
    )


    if frequency_min is not None:

        if frequency_max is not None:

            ax.set_xlim(
                frequency_min,
                frequency_max
            )

        else:

            ax.set_xlim(
                left=frequency_min
            )


    elif frequency_max is not None:

        ax.set_xlim(
            right=frequency_max
        )


    ax.set_xlabel(
        "Frequency"
    )


    ax.set_ylabel(
        y_label
    )


    ax.set_title(
        title
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


    ax.legend()


    plt.tight_layout()


    return (
        fig,
        ax
    )


# ============================================================
# 44. USE REUSABLE FUNCTION
# ============================================================

fig, ax = plot_log_frequency(

    dataframe=fft_data,

    frequency_column="Frequency_Hz",

    y_columns=[
        "Unshielded_dBuV",
        "Case_A_dBuV",
        "Case_B_dBuV",
        "Case_C_dBuV"
    ],

    labels=[
        "Unshielded",
        "Case A",
        "Case B",
        "Case C"
    ],

    y_label="Magnitude [dBµV]",

    title="Engineering Frequency Comparison",

    frequency_min=10e3,

    frequency_max=30e6

)


plt.show()


# ============================================================
# 45. SAVE FINAL FREQUENCY-DOMAIN FIGURE
# ============================================================

output_figure_folder = (
    script_folder
    / "output_figures"
)


output_figure_folder.mkdir(
    exist_ok=True
)


fig, ax = plot_log_frequency(

    dataframe=fft_data,

    frequency_column="Frequency_Hz",

    y_columns=[
        "Unshielded_dBuV",
        "Case_A_dBuV",
        "Case_B_dBuV",
        "Case_C_dBuV"
    ],

    labels=[
        "Unshielded",
        "Case A",
        "Case B",
        "Case C"
    ],

    y_label="Magnitude [dBµV]",

    title="Frequency-Domain Case Comparison",

    frequency_min=10e3,

    frequency_max=30e6

)


# ============================================================
# 46. SAVE PNG
# ============================================================

png_file = (
    output_figure_folder
    / "logarithmic_frequency_plot.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 47. SAVE PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "logarithmic_frequency_plot.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 48. SAVE SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "logarithmic_frequency_plot.svg"
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
# 49. COMMON MISTAKE - ZERO ON LOG AXIS
# ============================================================

"""
Incorrect:

frequency = [
    0,
    1000,
    10000
]


ax.set_xscale(
    "log"
)


A standard logarithmic axis cannot properly represent zero.


Check:

frequency > 0
"""


# ============================================================
# 50. COMMON MISTAKE - NEGATIVE VALUES
# ============================================================

"""
A conventional logarithmic scale cannot directly represent
negative values.

Do not automatically use:

abs(data)


because converting:

-10

to:

+10


changes the physical meaning.

Only transform data when scientifically justified.
"""


# ============================================================
# 51. COMMON MISTAKE - LOG Y-AXIS FOR dB
# ============================================================

"""
Suppose the Y-axis contains:

Magnitude [dBµV]


Do NOT automatically use:

ax.set_yscale(
    "log"
)


dB is already a logarithmic representation.

Typical spectrum plot:

X:
Frequency [Hz]
LOGARITHMIC

Y:
Magnitude [dBµV]
LINEAR numerical axis
"""


# ============================================================
# 52. COMMON MISTAKE - THINKING LOG AXIS CHANGES DATA
# ============================================================

"""
This:

ax.set_xscale(
    "log"
)


changes the AXIS REPRESENTATION.

It does NOT replace:

10,000 Hz

with:

log10(10,000)


inside the original DataFrame.

Your dataset remains unchanged.
"""


# ============================================================
# 53. COMMON MISTAKE - MANUALLY LOGGING AND LOG AXIS
# ============================================================

"""
Be careful not to accidentally apply logarithmic
transformation twice.

Example:

x_log = np.log10(
    frequency
)


and then:

ax.set_xscale(
    "log"
)


This usually does NOT represent the original frequency
correctly.

Choose either:

Plot original frequency on a log axis

OR

Transform the numerical variable for a specific analytical
reason.

Do not do both automatically.
"""


# ============================================================
# 54. COMMON MISTAKE - USE LOG AXIS FOR SMALL RANGE
# ============================================================

"""
A logarithmic axis is not necessary for every frequency
dataset.

Example:

95 kHz
100 kHz
105 kHz


This covers only a narrow range.

A linear axis may provide clearer interpretation.


Use log scaling when the frequency range spans meaningful
orders of magnitude.
"""


# ============================================================
# 55. COMMON MISTAKE - NO MINOR GRID
# ============================================================

"""
A logarithmic frequency plot may be difficult to read
without appropriate grid lines.

Useful:

ax.grid(
    True,
    which="both"
)


This shows major and minor log-grid locations.
"""


# ============================================================
# 56. COMMON MISTAKE - TOO MANY TICK LABELS
# ============================================================

"""
Do not label every frequency sample.

For example:

10 kHz

11 kHz

12 kHz

13 kHz

...

30 MHz


would make the axis unreadable.

Prefer meaningful decade-based or selected engineering
frequency ticks.
"""


# ============================================================
# 57. COMMON MISTAKE - CONFUSING FILTERING AND ZOOMING
# ============================================================

"""
ax.set_xlim(
    100e3,
    10e6
)


only changes what is displayed.


It does NOT remove data outside that range.


For calculations:

Filter the DataFrame first.
"""


# ============================================================
# 58. LINEAR VS LOG DECISION
# ============================================================

"""
Does X span several orders of magnitude?
          |
        Yes
          ↓
Consider logarithmic X-axis


Example:

10 kHz → 30 MHz


------------------------------------------------------------


Does Y span several orders of magnitude?
          |
        Yes
          ↓
Consider logarithmic Y-axis


but only if:

Y > 0

and Y is NOT already represented logarithmically.


------------------------------------------------------------


Do both X and Y span several orders?
          |
        Yes
          ↓
Consider log-log plot
"""


# ============================================================
# 59. ENGINEERING EXAMPLES
# ============================================================

"""
EXAMPLE 1

Time [s]
vs
Voltage [V]

Usually:

LINEAR X
LINEAR Y


------------------------------------------------------------


EXAMPLE 2

Frequency [Hz]
vs
Magnitude [dBµV]

Usually:

LOG X
LINEAR Y


------------------------------------------------------------


EXAMPLE 3

Frequency [Hz]
vs
Impedance [Ω]

Potentially:

LOG X
LOG Y


depending on the analysis.


------------------------------------------------------------


EXAMPLE 4

Load [%]
vs
Efficiency [%]

Usually:

LINEAR X
LINEAR Y
"""


# ============================================================
# 60. FREQUENCY-DOMAIN WORKFLOW
# ============================================================

"""
Frequency Data
      ↓
Check Frequency > 0
      ↓
Check Frequency Range
      ↓
Does Range Span Decades?
      ↓
Use Log X-axis
      ↓
Plot Magnitude
      ↓
Add Major / Minor Grid
      ↓
Format Frequency Labels
      ↓
Select Frequency Range
      ↓
Find Peaks if Required
      ↓
Compare Engineering Cases
      ↓
Save Figure
"""


# ============================================================
# 61. IMPORTANT FFT / EMI WORKFLOW
# ============================================================

"""
Time-Domain Signal
        ↓
FFT
        ↓
Frequency Vector
        ↓
Magnitude
        ↓
Convert to Required Unit
        ↓
Select Frequency Range
        ↓
Frequency > 0
        ↓
Logarithmic Frequency Axis
        ↓
Compare Cases
        ↓
Identify Peaks
        ↓
Scientific Interpretation
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
LOGARITHMIC AXES


1. LOGARITHMIC X-AXIS

ax.set_xscale(
    "log"
)


or:

ax.semilogx(
    x,
    y
)


------------------------------------------------------------


2. LOGARITHMIC Y-AXIS

ax.set_yscale(
    "log"
)


or:

ax.semilogy(
    x,
    y
)


------------------------------------------------------------


3. LOG-LOG PLOT

ax.set_xscale(
    "log"
)

ax.set_yscale(
    "log"
)


or:

ax.loglog(
    x,
    y
)


------------------------------------------------------------


4. COMMON FREQUENCY-DOMAIN FORMAT

Frequency [Hz]
    ↓
LOG X-axis


Magnitude [dBµV]
    ↓
LINEAR numerical Y-axis


------------------------------------------------------------


5. WHY LOG FREQUENCY?

10 kHz

100 kHz

1 MHz

10 MHz


Each frequency decade receives comparable visual space.


------------------------------------------------------------


6. MAJOR AND MINOR GRID

ax.grid(
    True,
    which="both"
)


------------------------------------------------------------


7. SET FREQUENCY RANGE

ax.set_xlim(
    10e3,
    30e6
)


This changes only the displayed region.


------------------------------------------------------------


8. FILTER DATA

selected = data[
    (
        data["Frequency_Hz"] >= 10e3
    )
    &
    (
        data["Frequency_Hz"] <= 30e6
    )
]


Use filtering when the selected frequency band will also
be used for calculations.


------------------------------------------------------------


9. LOG AXES REQUIRE POSITIVE VALUES

For log X:

X > 0


For log Y:

Y > 0


------------------------------------------------------------


10. DO NOT LOG dB AGAIN

Magnitude [dB]

or

Magnitude [dBµV]


already represents a logarithmic quantity.

Do not automatically apply logarithmic Y-axis scaling to
dB values.


------------------------------------------------------------


11. DO NOT LOG TWICE

Avoid:

np.log10(
    frequency
)

followed by:

ax.set_xscale(
    "log"
)


unless there is a very specific analytical reason.


------------------------------------------------------------


12. NUMPY LOG-SPACED DATA

np.logspace(
    start,
    stop,
    number
)


Example:

np.logspace(
    3,
    7,
    100
)


creates values approximately spanning:

1 kHz

to

10 MHz


------------------------------------------------------------


13. FREQUENCY LABELS

Engineering figures may use:

10 kHz

100 kHz

1 MHz

10 MHz

instead of long numerical Hz values.


------------------------------------------------------------


14. COMMON APPLICATIONS

- FFT spectra
- EMI spectra
- Frequency response
- Bode plots
- Impedance
- Filter response
- Power spectral density
- Device frequency characteristics
- Parasitic-frequency analysis


------------------------------------------------------------


15. CORE DECISION

Narrow numerical range
        ↓
Linear axis may be sufficient


Several orders of magnitude
        ↓
Logarithmic axis may provide better interpretation


------------------------------------------------------------


16. MOST IMPORTANT RESEARCH PRINCIPLE

Do not use logarithmic scaling simply because a figure
looks better.

Use it when the numerical range and physical interpretation
justify it.


------------------------------------------------------------


17. COMPLETE WORKFLOW

Raw Frequency Data
        ↓
Check Values
        ↓
Check Units
        ↓
Check Range
        ↓
Choose Linear / Log Scale
        ↓
Select Frequency Band
        ↓
Plot
        ↓
Format Ticks
        ↓
Add Grid
        ↓
Identify Important Features
        ↓
Save
        ↓
Interpret


------------------------------------------------------------


NEXT:

15_axis_limits_and_ticks.py


The next file will focus on precise control of:

X-axis minimum / maximum

Y-axis minimum / maximum

Major ticks

Minor ticks

Tick spacing

Scientific notation

Engineering frequency ticks

Custom tick labels

Automatic vs manual limits

Zooming into data

Multiple subplot axis limits

Research/publication figure axis control
"""
