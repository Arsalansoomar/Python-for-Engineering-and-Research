"""
============================================================
Python for Engineering and Research
02 - Multiple Line Plots
============================================================

Purpose:
    Demonstrate how two, three, or many datasets can be
    compared on the same figure using Matplotlib.

Topics:
    1. What is a multiple-line plot?
    2. When should it be used?
    3. Two-line comparison
    4. Three-line comparison
    5. Legends
    6. Line styles and markers
    7. Plotting many cases manually
    8. Plotting many cases using loops
    9. Dictionary-based plotting
    10. Engineering comparison example
    11. Saving the figure
    12. Common mistakes
    13. Key takeaways

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT IS A MULTIPLE-LINE PLOT?
# ============================================================

"""
A multiple-line plot displays two or more datasets on the
same axes.

All datasets normally share the same independent variable.

Example:

                    Case A
                  /
Voltage          / Case B
                /
              / Case C
             /
             --------------------------> Time


Typical structure:

One X variable

        +

Several Y variables
"""


# ============================================================
# 2. WHEN SHOULD IT BE USED?
# ============================================================

"""
Multiple-line plots are useful when several datasets should
be directly compared.

Engineering examples:

- Input Voltage vs Output Voltage
- Simulation vs Experiment
- Different converter configurations
- Different control methods
- Different temperatures
- Different load conditions
- Several EMI mitigation cases
- Multiple FFT spectra
- Parameter-sweep results

The datasets should normally have a meaningful relationship
that makes comparison on the same axes useful.
"""


# ============================================================
# 3. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt

from pathlib import Path


# ============================================================
# 4. EXAMPLE DATASET
# ============================================================

"""
One X variable:

Time

Two Y variables:

Input Voltage
Output Voltage
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


input_voltage = [
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48,
    48
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
# 5. TWO-LINE PLOT
# ============================================================

"""
The simplest method is to call:

ax.plot()

once for each variable.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    input_voltage,
    label="Input Voltage"
)


ax.plot(
    time_ms,
    output_voltage,
    label="Output Voltage"
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Input and Output Voltage"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 6. WHY IS label IMPORTANT?
# ============================================================

"""
When several lines are plotted, the reader must know which
line represents each dataset.

The label parameter assigns a name:

ax.plot(
    x,
    y,
    label="Case A"
)

Then:

ax.legend()

displays the labels.
"""


# ============================================================
# 7. THREE-LINE PLOT
# ============================================================

"""
Now add another variable.

Example:

Input Voltage
Output Voltage
Reference Voltage
"""


reference_voltage = [
    96,
    96,
    96,
    96,
    96,
    96,
    96,
    96,
    96,
    96,
    96
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    input_voltage,
    label="Input Voltage"
)


ax.plot(
    time_ms,
    output_voltage,
    label="Output Voltage"
)


ax.plot(
    time_ms,
    reference_voltage,
    linestyle="--",
    label="Reference Voltage"
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Converter Voltage Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 8. LINE STYLES
# ============================================================

"""
Different line styles can help distinguish datasets.

Common styles:

"-"     Solid

"--"    Dashed

"-."    Dash-dot

":"     Dotted


Example:

ax.plot(
    x,
    y,
    linestyle="--"
)
"""


# ============================================================
# 9. MARKERS
# ============================================================

"""
Markers indicate individual data points.

Common examples:

"o"     Circle

"s"     Square

"^"     Triangle

"x"     Cross


Example:

ax.plot(
    x,
    y,
    marker="o"
)
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    output_voltage,
    marker="o",
    linewidth=2,
    label="Output Voltage"
)


ax.plot(
    time_ms,
    reference_voltage,
    linestyle="--",
    linewidth=2,
    label="Reference Voltage"
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Output and Reference Voltage"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 10. MULTIPLE ENGINEERING CASES
# ============================================================

"""
Consider four different converter cases.

Each case has the same time axis but a different voltage
response.
"""


case_a = [
    0,
    20,
    37,
    54,
    68,
    79,
    87,
    92,
    94.5,
    95.5,
    96
]


case_b = [
    0,
    19,
    36,
    53,
    67,
    78,
    86,
    91,
    94,
    95,
    95.8
]


case_c = [
    0,
    18,
    34,
    51,
    66,
    77,
    85,
    90,
    93,
    94.5,
    95.5
]


case_d = [
    0,
    17,
    33,
    50,
    65,
    76,
    84,
    89,
    92,
    94,
    95
]


# ============================================================
# 11. MANUAL MULTIPLE-CASE PLOT
# ============================================================

"""
This method is perfectly acceptable when only a few
datasets are involved.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    case_a,
    label="Case A"
)


ax.plot(
    time_ms,
    case_b,
    label="Case B"
)


ax.plot(
    time_ms,
    case_c,
    label="Case C"
)


ax.plot(
    time_ms,
    case_d,
    label="Case D"
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Output Voltage [V]"
)

ax.set_title(
    "Comparison of Four Converter Cases"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 12. WHY MANUAL PLOTTING BECOMES INEFFICIENT
# ============================================================

"""
For four cases, writing four ax.plot() commands is manageable.

But imagine:

10 cases
20 cases
50 simulation results

Writing one plotting command for every case becomes
unnecessarily repetitive.

A loop provides a cleaner solution.
"""


# ============================================================
# 13. STORE MULTIPLE CASES IN A LIST
# ============================================================

datasets = [
    case_a,
    case_b,
    case_c,
    case_d
]


case_names = [
    "Case A",
    "Case B",
    "Case C",
    "Case D"
]


# ============================================================
# 14. PLOT MULTIPLE CASES USING A LOOP
# ============================================================

"""
zip() allows each dataset to be paired with its case name.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, dataset in zip(
    case_names,
    datasets
):

    ax.plot(
        time_ms,
        dataset,
        linewidth=2,
        label=case_name
    )


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Output Voltage [V]"
)

ax.set_title(
    "Converter Case Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 15. WHY THE LOOP APPROACH IS BETTER
# ============================================================

"""
Without loop:

ax.plot(time, case_a)
ax.plot(time, case_b)
ax.plot(time, case_c)
ax.plot(time, case_d)


With loop:

for case_name, dataset in zip(
    case_names,
    datasets
):

    ax.plot(
        time,
        dataset,
        label=case_name
    )


The loop approach becomes especially useful when the number
of cases increases.
"""


# ============================================================
# 16. DICTIONARY-BASED PLOTTING
# ============================================================

"""
A dictionary is often an even cleaner way to organize
engineering datasets.

Key:

Case Name

Value:

Case Dataset
"""


converter_cases = {

    "Case A": case_a,

    "Case B": case_b,

    "Case C": case_c,

    "Case D": case_d

}


# ============================================================
# 17. LOOP THROUGH DICTIONARY
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, dataset in converter_cases.items():

    ax.plot(
        time_ms,
        dataset,
        linewidth=2,
        label=case_name
    )


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Output Voltage [V]"
)

ax.set_title(
    "Dictionary-Based Case Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 18. ENGINEERING EXAMPLE
# ============================================================

"""
Example:

Compare converter efficiency at several load conditions
for three different design cases.
"""


load_percent = [
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


baseline_efficiency = [
    88.5,
    90.2,
    91.8,
    92.8,
    93.5,
    94.0,
    94.2,
    94.0,
    93.7,
    93.2
]


design_a_efficiency = [
    89.0,
    91.0,
    92.5,
    93.5,
    94.3,
    94.8,
    95.0,
    94.9,
    94.6,
    94.2
]


design_b_efficiency = [
    89.5,
    91.5,
    93.0,
    94.0,
    94.8,
    95.3,
    95.5,
    95.4,
    95.1,
    94.7
]


efficiency_cases = {

    "Baseline": baseline_efficiency,

    "Design A": design_a_efficiency,

    "Design B": design_b_efficiency

}


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, efficiency in efficiency_cases.items():

    ax.plot(
        load_percent,
        efficiency,
        marker="o",
        linewidth=2,
        label=case_name
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


ax.set_xlim(
    10,
    100
)

ax.set_ylim(
    85,
    100
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 19. SIMULATION VS EXPERIMENT
# ============================================================

"""
A common engineering use case is comparing numerical
simulation results against experimental measurements.
"""


time_us = [
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


simulation_voltage = [
    0,
    20,
    38,
    55,
    70,
    81,
    88,
    92,
    94,
    95,
    96
]


experimental_voltage = [
    0,
    19,
    36,
    53,
    68,
    79,
    86,
    91,
    93.5,
    94.8,
    95.5
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_us,
    simulation_voltage,
    linewidth=2,
    label="Simulation"
)


ax.plot(
    time_us,
    experimental_voltage,
    linestyle="--",
    marker="o",
    linewidth=2,
    label="Experiment"
)


ax.set_xlabel(
    "Time [µs]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Simulation and Experimental Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 20. MANY CASES
# ============================================================

"""
The same loop-based method can scale to many datasets.

For demonstration, create several synthetic operating cases.
"""


many_cases = {}


for case_number in range(
    1,
    7
):

    values = []

    for voltage in output_voltage:

        adjusted_voltage = (
            voltage
            - case_number * 0.5
        )

        values.append(
            adjusted_voltage
        )

    case_name = (
        f"Case {case_number}"
    )

    many_cases[
        case_name
    ] = values


# ============================================================
# 21. PLOT MANY CASES AUTOMATICALLY
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, values in many_cases.items():

    ax.plot(
        time_ms,
        values,
        label=case_name
    )


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Output Voltage [V]"
)

ax.set_title(
    "Automatic Multiple-Case Plot"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 22. WHEN ARE TOO MANY LINES A PROBLEM?
# ============================================================

"""
Although Python can plot many curves, more curves do not
always produce a better scientific figure.

If a figure contains too many lines:

- Curves may overlap
- Legends become large
- Interpretation becomes difficult
- Important results may be hidden


Possible alternatives:

1. Plot only representative cases

2. Use subplots

3. Use separate figures

4. Normalize data

5. Use a heatmap for appropriate datasets

6. Highlight only selected cases

The objective should always be scientific clarity rather
than displaying every available dataset.
"""


# ============================================================
# 23. SAVE FINAL COMPARISON FIGURE
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


for case_name, efficiency in efficiency_cases.items():

    ax.plot(
        load_percent,
        efficiency,
        marker="o",
        linewidth=2,
        label=case_name
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


ax.set_xlim(
    10,
    100
)

ax.set_ylim(
    85,
    100
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()


# Save PNG

png_file = (
    output_folder
    / "multiple_line_comparison.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# Save PDF

pdf_file = (
    output_folder
    / "multiple_line_comparison.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# Save SVG

svg_file = (
    output_folder
    / "multiple_line_comparison.svg"
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
# 24. COMMON MISTAKE - NO LABELS
# ============================================================

"""
Incorrect:

ax.plot(
    time,
    case_a
)

ax.plot(
    time,
    case_b
)


The reader cannot determine which line represents
which case.


Better:

ax.plot(
    time,
    case_a,
    label="Case A"
)

ax.plot(
    time,
    case_b,
    label="Case B"
)

ax.legend()
"""


# ============================================================
# 25. COMMON MISTAKE - DIFFERENT X LENGTHS
# ============================================================

"""
Each X and Y pair must normally have matching lengths.

Example:

Time:

10 values

Case A:

10 values


Correct.


Time:

10 values

Case B:

8 values


Incorrect for a direct plot using the same time vector.
"""


# ============================================================
# 26. COMMON MISTAKE - MIXING DIFFERENT PHYSICAL UNITS
# ============================================================

"""
Suppose we plot:

Voltage [V]

and

Current [A]

on exactly the same Y-axis.

Although Python allows it, interpretation may be poor
because the variables have different units and scales.

Better options may include:

- Separate subplots
- Dual Y-axis
- Normalized variables

These approaches will be covered later.
"""


# ============================================================
# 27. COMMON MISTAKE - TOO MANY LEGEND ITEMS
# ============================================================

"""
A legend containing 20 or 30 cases may dominate the figure.

Possible solutions:

- Reduce the number of displayed cases
- Use subplots
- Place the legend outside the plot
- Use representative cases
- Use another visualization method
"""


# ============================================================
# 28. MULTIPLE-LINE PLOTTING PIPELINE
# ============================================================

"""
Shared X Variable
       ↓
Dataset 1
Dataset 2
Dataset 3
...
       ↓
Organize Data
       ↓
List / Dictionary
       ↓
Loop Through Datasets
       ↓
Plot Each Dataset
       ↓
Assign Meaningful Label
       ↓
Add Legend
       ↓
Format Figure
       ↓
Validate Comparison
       ↓
Save Figure
"""


# ============================================================
# 29. MANUAL VS AUTOMATIC PLOTTING
# ============================================================

"""
MANUAL METHOD

Good for:

2 or 3 datasets


Example:

ax.plot(
    x,
    y1
)

ax.plot(
    x,
    y2
)


------------------------------------------------------------


LOOP METHOD

Good for:

Many datasets


Example:

for name, values in datasets.items():

    ax.plot(
        x,
        values,
        label=name
    )


This becomes particularly useful later when datasets
come automatically from:

CSV files
Excel files
Simulation outputs
Measurement files
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
MULTIPLE LINE PLOTS


1. TWO VARIABLES

ax.plot(
    x,
    y1,
    label="Variable 1"
)

ax.plot(
    x,
    y2,
    label="Variable 2"
)


------------------------------------------------------------


2. THREE VARIABLES

ax.plot(
    x,
    y1,
    label="Case A"
)

ax.plot(
    x,
    y2,
    label="Case B"
)

ax.plot(
    x,
    y3,
    label="Case C"
)


------------------------------------------------------------


3. ALWAYS ADD LEGEND WHEN REQUIRED

ax.legend()


------------------------------------------------------------


4. LOOP FOR MANY CASES

datasets = {

    "Case A": case_a,

    "Case B": case_b,

    "Case C": case_c

}


for name, values in datasets.items():

    ax.plot(
        x,
        values,
        label=name
    )


------------------------------------------------------------


5. COMMON ENGINEERING APPLICATIONS

- Simulation vs Experiment
- Converter Case Comparison
- Control Method Comparison
- Voltage Waveforms
- Current Waveforms
- Efficiency Curves
- Temperature Curves
- Parameter Sweeps
- Frequency Response
- FFT Spectrum Comparison


------------------------------------------------------------


6. GOOD PRACTICE

Use:

Meaningful labels

Correct physical units

Readable legends

Consistent X variable

Appropriate axis limits

Clear scientific comparison


------------------------------------------------------------


7. DO NOT ASSUME

More curves = better figure

Scientific figures should prioritize:

Clarity

Comparison

Interpretability


------------------------------------------------------------


8. SCALABLE PLOTTING

2 cases
    ↓
Manual plotting is fine

5 cases
    ↓
Loop becomes useful

20 cases
    ↓
Consider automation and visualization clarity

100 cases
    ↓
A different visualization may be more appropriate


------------------------------------------------------------


NEXT:

03_bar_plot.py

will introduce comparison of discrete categories such as:

Case A
Case B
Case C

with values such as:

Efficiency
Power Loss
Peak Magnitude
Temperature
"""
