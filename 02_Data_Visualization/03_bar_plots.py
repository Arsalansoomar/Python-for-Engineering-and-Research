"""
============================================================
Python for Engineering and Research
03 - Bar Plot
============================================================

Purpose:
    Introduce bar plots using Matplotlib and demonstrate how
    discrete engineering categories can be compared clearly.

Topics:
    1. What is a bar plot?
    2. When should it be used?
    3. Required imports
    4. Basic bar plot
    5. Engineering example
    6. Adding values above bars
    7. Horizontal bar plot
    8. Axis limits
    9. Reference lines
    10. Saving figures
    11. Common mistakes
    12. Key takeaways

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT IS A BAR PLOT?
# ============================================================

"""
A bar plot compares numerical values associated with
discrete categories.

Example:

Efficiency [%]

100 |             █
 95 |      █      █
 90 | █    █      █
    +---------------------
      A    B      C


X-axis:

Categories


Y-axis:

Numerical value
"""


# ============================================================
# 2. WHEN SHOULD A BAR PLOT BE USED?
# ============================================================

"""
Bar plots are useful when comparing separate categories.

Typical engineering examples:

- Efficiency of different converters
- Power loss of different designs
- Maximum temperature of different cases
- Peak EMI magnitude of different configurations
- THD comparison
- Control-method performance
- Material comparison
- Algorithm accuracy
- Experimental case comparison


Bar plots are NOT usually appropriate for continuous
time-series data.

For example:

Voltage vs Time

should normally use a line plot.
"""


# ============================================================
# 3. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt

from pathlib import Path


# ============================================================
# 4. BASIC DATASET
# ============================================================

"""
Suppose three converter designs have the following
efficiencies.
"""


converter_cases = [
    "Case A",
    "Case B",
    "Case C"
]


efficiency = [
    91.5,
    94.2,
    96.0
]


# ============================================================
# 5. BASIC BAR PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.bar(
    converter_cases,
    efficiency
)


ax.set_xlabel(
    "Converter Case"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Converter Efficiency Comparison"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 6. WHY GRID ONLY ON Y-AXIS?
# ============================================================

"""
For vertical bar plots, horizontal grid lines are often
more useful than a full grid.

Using:

axis="y"

helps estimate the bar height while keeping the figure
visually clean.
"""


# ============================================================
# 7. ADD VALUES ABOVE THE BARS
# ============================================================

"""
Displaying numerical values above bars can improve
interpretation when the number of categories is small.

Matplotlib provides:

ax.bar_label()
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(
    converter_cases,
    efficiency
)


ax.set_xlabel(
    "Converter Case"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Converter Efficiency Comparison"
)


ax.grid(
    True,
    axis="y"
)


ax.bar_label(
    bars,
    fmt="%.1f%%",
    padding=3
)


plt.tight_layout()

plt.show()


# ============================================================
# 8. ENGINEERING EXAMPLE - POWER LOSS
# ============================================================

"""
Example:

Compare the power losses of four converter designs.

Lower values represent better performance.
"""


designs = [
    "Baseline",
    "Design A",
    "Design B",
    "Design C"
]


power_loss = [
    24.5,
    20.2,
    17.8,
    15.4
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(
    designs,
    power_loss
)


ax.set_xlabel(
    "Converter Design"
)

ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Converter Power-Loss Comparison"
)


ax.grid(
    True,
    axis="y"
)


ax.bar_label(
    bars,
    fmt="%.1f W",
    padding=3
)


plt.tight_layout()

plt.show()


# ============================================================
# 9. ENGINEERING EXAMPLE - TEMPERATURE
# ============================================================

"""
Bar plots are also useful for comparing maximum operating
temperature across several cases.
"""


cases = [
    "Case A",
    "Case B",
    "Case C",
    "Case D"
]


maximum_temperature = [
    78,
    72,
    69,
    65
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(
    cases,
    maximum_temperature
)


ax.set_xlabel(
    "Operating Case"
)

ax.set_ylabel(
    "Maximum Temperature [°C]"
)

ax.set_title(
    "Maximum Temperature Comparison"
)


ax.grid(
    True,
    axis="y"
)


ax.bar_label(
    bars,
    fmt="%.0f °C",
    padding=3
)


plt.tight_layout()

plt.show()


# ============================================================
# 10. ADD ENGINEERING LIMIT / REFERENCE LINE
# ============================================================

"""
Sometimes a specification or engineering limit should be
shown on the figure.

Example:

Maximum allowable temperature = 80 °C


A horizontal reference line can be added using:

ax.axhline()
"""


temperature_limit = 80


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(
    cases,
    maximum_temperature
)


ax.axhline(
    y=temperature_limit,
    linestyle="--",
    linewidth=1.5,
    label="Temperature Limit"
)


ax.set_xlabel(
    "Operating Case"
)

ax.set_ylabel(
    "Maximum Temperature [°C]"
)

ax.set_title(
    "Temperature Comparison with Operating Limit"
)


ax.grid(
    True,
    axis="y"
)


ax.bar_label(
    bars,
    fmt="%.0f",
    padding=3
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 11. AXIS LIMITS
# ============================================================

"""
Axis limits can be adjusted using:

ax.set_ylim()


For a bar plot, however, the Y-axis should normally start
at zero because bar height represents magnitude.

Starting the axis at a large non-zero value can exaggerate
small differences between categories.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(
    designs,
    power_loss
)


ax.set_ylim(
    0,
    30
)


ax.set_xlabel(
    "Converter Design"
)

ax.set_ylabel(
    "Power Loss [W]"
)


ax.grid(
    True,
    axis="y"
)


ax.bar_label(
    bars,
    fmt="%.1f",
    padding=3
)


plt.tight_layout()

plt.show()


# ============================================================
# 12. HORIZONTAL BAR PLOT
# ============================================================

"""
Horizontal bar plots can be useful when:

- Category names are long
- Many categories are compared
- Horizontal reading is easier


Use:

ax.barh()
"""


methods = [
    "Conventional Method",
    "Improved Method",
    "Optimized Method",
    "Proposed Method"
]


accuracy = [
    88.2,
    91.5,
    94.3,
    96.1
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.barh(
    methods,
    accuracy
)


ax.set_xlabel(
    "Accuracy [%]"
)

ax.set_ylabel(
    "Method"
)

ax.set_title(
    "Method Accuracy Comparison"
)


ax.grid(
    True,
    axis="x"
)


ax.bar_label(
    bars,
    fmt="%.1f%%",
    padding=3
)


plt.tight_layout()

plt.show()


# ============================================================
# 13. ENGINEERING EXAMPLE - PEAK MAGNITUDE
# ============================================================

"""
Example:

Compare peak measured spectral magnitude for several
engineering configurations.

These values are synthetic and used only for demonstration.
"""


emi_cases = [
    "Baseline",
    "Case A",
    "Case B",
    "Case C"
]


peak_magnitude = [
    96.5,
    89.8,
    84.2,
    80.5
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(
    emi_cases,
    peak_magnitude
)


ax.set_xlabel(
    "Configuration"
)

ax.set_ylabel(
    "Peak Magnitude [dBµV]"
)

ax.set_title(
    "Peak Spectral Magnitude Comparison"
)


ax.grid(
    True,
    axis="y"
)


ax.bar_label(
    bars,
    fmt="%.1f",
    padding=3
)


plt.tight_layout()

plt.show()


# ============================================================
# 14. SORTING DATA BEFORE PLOTTING
# ============================================================

"""
Sometimes it is useful to sort categories by their
numerical result.

Example:

Power-loss values from lowest to highest.
"""


design_results = {

    "Baseline": 24.5,

    "Design A": 20.2,

    "Design B": 17.8,

    "Design C": 15.4

}


sorted_results = sorted(
    design_results.items(),
    key=lambda item: item[1]
)


sorted_names = [
    item[0]
    for item in sorted_results
]


sorted_values = [
    item[1]
    for item in sorted_results
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(
    sorted_names,
    sorted_values
)


ax.set_xlabel(
    "Converter Design"
)

ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Power Loss Ranked from Lowest to Highest"
)


ax.grid(
    True,
    axis="y"
)


ax.bar_label(
    bars,
    fmt="%.1f",
    padding=3
)


plt.tight_layout()

plt.show()


# ============================================================
# 15. PERCENTAGE REDUCTION EXAMPLE
# ============================================================

"""
Bar plots can also summarize calculated improvement.

Suppose the baseline peak magnitude is:

96.5 dBµV

For demonstration, calculate numerical reduction relative
to the baseline.

Note:

A difference expressed in dB is already a logarithmic
difference and should not automatically be interpreted as
a simple linear percentage reduction.

Here we therefore display the reduction in dB.
"""


baseline_value = peak_magnitude[0]


reduction_db = []


for value in peak_magnitude:

    reduction = (
        baseline_value
        - value
    )

    reduction_db.append(
        reduction
    )


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(
    emi_cases,
    reduction_db
)


ax.set_xlabel(
    "Configuration"
)

ax.set_ylabel(
    "Reduction Relative to Baseline [dB]"
)

ax.set_title(
    "Relative Reduction Comparison"
)


ax.grid(
    True,
    axis="y"
)


ax.bar_label(
    bars,
    fmt="%.1f dB",
    padding=3
)


plt.tight_layout()

plt.show())


# ============================================================
# 16. IMPORTANT NOTE ABOUT dB DATA
# ============================================================

"""
Be careful when working with logarithmic quantities.

For example:

96 dBµV

and

80 dBµV

differ by:

16 dB


It is usually clearer to report:

16 dB reduction

rather than calculating:

(96 - 80) / 96 * 100

because dB values represent logarithmic quantities.

Conversion to linear amplitude or power should be performed
first when a true linear percentage comparison is required.
"""


# ============================================================
# 17. SAVE FINAL FIGURE
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
    figsize=(7, 4.5)
)


bars = ax.bar(
    designs,
    power_loss
)


ax.set_xlabel(
    "Converter Design"
)

ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Converter Power-Loss Comparison"
)


ax.set_ylim(
    0,
    30
)


ax.grid(
    True,
    axis="y"
)


ax.bar_label(
    bars,
    fmt="%.1f W",
    padding=3
)


plt.tight_layout()


# PNG

png_file = (
    output_folder
    / "bar_plot_power_loss.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# PDF

pdf_file = (
    output_folder
    / "bar_plot_power_loss.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# SVG

svg_file = (
    output_folder
    / "bar_plot_power_loss.svg"
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
# 18. COMMON MISTAKE - USING BAR PLOT FOR TIME DATA
# ============================================================

"""
For continuous signals such as:

Time vs Voltage

a line plot is normally more appropriate.

Avoid using hundreds or thousands of bars for waveform
data.

Use:

ax.plot(
    time,
    voltage
)

instead.
"""


# ============================================================
# 19. COMMON MISTAKE - TRUNCATED Y-AXIS
# ============================================================

"""
Suppose:

Case A = 94 %

Case B = 95 %

Case C = 96 %


Using:

ax.set_ylim(
    93,
    97
)

can visually exaggerate the difference because bar lengths
are interpreted relative to a baseline.

For bar charts, a zero baseline is usually preferable.


For line plots, non-zero limits may be more acceptable when
the selected range is scientifically justified.
"""


# ============================================================
# 20. COMMON MISTAKE - TOO MANY CATEGORIES
# ============================================================

"""
A bar plot containing 50 categories can become difficult
to read.

Possible alternatives:

- Sort categories
- Use horizontal bars
- Select representative cases
- Split into multiple figures
- Use another visualization method
"""


# ============================================================
# 21. COMMON MISTAKE - UNCLEAR CATEGORY NAMES
# ============================================================

"""
Avoid:

A
B
C
D


when the reader does not know what those names mean.

Prefer:

Baseline
Design A
Design B
Proposed Method


Category names should communicate the physical or
experimental meaning of the data.
"""


# ============================================================
# 22. BAR PLOT VS LINE PLOT
# ============================================================

"""
LINE PLOT

Best for:

Continuous relationships


Examples:

Time vs Voltage

Frequency vs Magnitude

Load vs Efficiency


------------------------------------------------------------


BAR PLOT

Best for:

Discrete comparisons


Examples:

Efficiency of Method A / B / C

Maximum Temperature of Case A / B / C

Power Loss of Design A / B / C
"""


# ============================================================
# 23. BAR PLOT WORKFLOW
# ============================================================

"""
Define Categories
       ↓
Define Numerical Values
       ↓
Check Units
       ↓
Create Figure
       ↓
Create Bars
       ↓
Add Axis Labels
       ↓
Add Numerical Labels if Useful
       ↓
Add Engineering Limit if Required
       ↓
Check Y-axis Baseline
       ↓
Validate Interpretation
       ↓
Save Figure
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
BAR PLOTS


1. BASIC BAR PLOT

categories = [
    "A",
    "B",
    "C"
]

values = [
    10,
    20,
    30
]


fig, ax = plt.subplots()


ax.bar(
    categories,
    values
)


------------------------------------------------------------


2. ADD LABELS

ax.set_xlabel(
    "Case"
)

ax.set_ylabel(
    "Efficiency [%]"
)


------------------------------------------------------------


3. ADD VALUES ABOVE BARS

bars = ax.bar(
    categories,
    values
)


ax.bar_label(
    bars
)


------------------------------------------------------------


4. HORIZONTAL BAR

ax.barh(
    categories,
    values
)


------------------------------------------------------------


5. REFERENCE LIMIT

ax.axhline(
    y=80,
    linestyle="--"
)


------------------------------------------------------------


6. GOOD APPLICATIONS

- Efficiency comparison
- Power-loss comparison
- Temperature comparison
- Peak magnitude comparison
- Algorithm accuracy
- THD comparison
- Material comparison
- Discrete operating conditions


------------------------------------------------------------


7. BAR PLOTS ARE NOT IDEAL FOR

Continuous waveforms

Long time-series datasets

FFT spectra

Frequency response


Use line plots for those applications.


------------------------------------------------------------


8. IMPORTANT BAR-PLOT PRINCIPLE

Because bar length communicates magnitude, the numerical
axis should normally begin at zero unless there is a
strong and clearly communicated reason to do otherwise.


------------------------------------------------------------


9. SCIENTIFIC FIGURE PRINCIPLE

A bar plot should answer a clear question such as:

Which case is highest?

Which case is lowest?

Which design has the smallest loss?

Which method exceeds the specification?


------------------------------------------------------------


NEXT:

04_grouped_bar_plot.py

will extend:

ONE numerical value per category

into:

MULTIPLE numerical values per category.


Example:

             100 kHz   1 MHz   10 MHz

Baseline        |        |        |
Case A          |        |        |
Case B          |        |        |
Case C          |        |        |
"""
