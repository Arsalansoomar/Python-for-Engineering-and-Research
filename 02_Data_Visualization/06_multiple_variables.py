"""
============================================================
Python for Engineering and Research
06 - Multiple Variables
============================================================

Purpose:
    Demonstrate how several engineering variables can be
    visualized and compared using Matplotlib.

Topics:
    1. What does multiple-variable plotting mean?
    2. Same-unit variables
    3. Different-unit variables
    4. Automatic plotting using dictionaries
    5. Derived variables
    6. Selecting variables to plot
    7. Normalization
    8. Min-max scaling
    9. Relative values
    10. Engineering example
    11. Saving figures
    12. Common mistakes
    13. Key takeaways

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT IS MULTIPLE-VARIABLE PLOTTING?
# ============================================================

"""
Engineering datasets often contain several variables.

Example:

Time
Voltage
Current
Power
Temperature


The challenge is not simply:

"How do I plot all columns?"

The more important question is:

"Which variables should be displayed together so that
the figure remains scientifically meaningful?"


Typical dataset:

Time
 ↓
Input Voltage
Output Voltage
Current
Power
Temperature
Efficiency
"""


# ============================================================
# 2. WHEN SHOULD VARIABLES SHARE THE SAME AXIS?
# ============================================================

"""
Variables can usually share one Y-axis when:

- They have the same physical unit
- Their numerical ranges are reasonably similar
- Direct comparison is scientifically meaningful


Good example:

Input Voltage [V]
Output Voltage [V]


Both quantities:

- Have the same unit
- Represent voltage
- Can be directly compared


Less suitable example:

Voltage [V]
Current [A]
Temperature [°C]

These quantities have different units.

Placing all three on one ordinary Y-axis may produce a
misleading or difficult-to-read figure.
"""


# ============================================================
# 3. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path


# ============================================================
# 4. ENGINEERING DATASET
# ============================================================

"""
Consider several measurements from a DC-DC converter.
"""


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
        48.1,
        48.2,
        48.0,
        48.1,
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
# 5. TWO VARIABLES WITH THE SAME UNIT
# ============================================================

"""
Input Voltage and Output Voltage both use volts.

Therefore plotting them on the same Y-axis is meaningful.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    input_voltage,
    linewidth=2,
    label="Input Voltage"
)


ax.plot(
    time_ms,
    output_voltage,
    linewidth=2,
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
# 6. TWO CURRENT VARIABLES
# ============================================================

"""
Input Current and Output Current also share the same
physical unit.

Therefore they can reasonably share one Y-axis.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    input_current,
    linewidth=2,
    label="Input Current"
)


ax.plot(
    time_ms,
    output_current,
    linewidth=2,
    label="Output Current"
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Current [A]"
)

ax.set_title(
    "Input and Output Current"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 7. DERIVED VARIABLES
# ============================================================

"""
New engineering variables can be calculated from the
existing measurements.

Electrical power:

P = V * I
"""


input_power = (
    input_voltage
    * input_current
)


output_power = (
    output_voltage
    * output_current
)


power_loss = (
    input_power
    - output_power
)


print(
    "--- Derived Variables ---"
)

print(
    "Input Power:",
    input_power
)

print(
    "Output Power:",
    output_power
)

print(
    "Power Difference:",
    power_loss
)


# ============================================================
# 8. PLOT MULTIPLE POWER VARIABLES
# ============================================================

"""
Because all three variables are expressed in watts, they
may be displayed on the same axis.

Note:

During startup, the simple synthetic data may not represent
a complete physical converter-loss model. The purpose here
is to demonstrate plotting and data processing.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    input_power,
    linewidth=2,
    label="Input Power"
)


ax.plot(
    time_ms,
    output_power,
    linewidth=2,
    label="Output Power"
)


ax.plot(
    time_ms,
    power_loss,
    linestyle="--",
    linewidth=2,
    label="Power Difference"
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Power [W]"
)

ax.set_title(
    "Converter Power Variables"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 9. STORE VARIABLES IN A DICTIONARY
# ============================================================

"""
A dictionary is useful when several related datasets
need to be processed automatically.
"""


voltage_data = {

    "Input Voltage": input_voltage,

    "Output Voltage": output_voltage

}


# ============================================================
# 10. AUTOMATIC MULTIPLE-VARIABLE PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for variable_name, values in voltage_data.items():

    ax.plot(
        time_ms,
        values,
        linewidth=2,
        label=variable_name
    )


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Automatic Voltage Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 11. WHY DICTIONARIES ARE USEFUL
# ============================================================

"""
Instead of writing:

ax.plot(time, voltage_1)
ax.plot(time, voltage_2)
ax.plot(time, voltage_3)
ax.plot(time, voltage_4)


we can store:

variables = {

    "Voltage 1": voltage_1,

    "Voltage 2": voltage_2,

    "Voltage 3": voltage_3,

    "Voltage 4": voltage_4

}


Then:

for name, values in variables.items():

    ax.plot(
        time,
        values,
        label=name
    )


This becomes especially useful later when columns are read
automatically from CSV or Excel files.
"""


# ============================================================
# 12. SELECT ONLY REQUIRED VARIABLES
# ============================================================

"""
A dataset may contain many variables, but a figure does
not need to display all of them.

Suppose the available data are stored as:
"""


all_measurements = {

    "Input Voltage": input_voltage,

    "Output Voltage": output_voltage,

    "Input Current": input_current,

    "Output Current": output_current,

    "Temperature": temperature

}


"""
We may only want:

Input Voltage

and

Output Voltage
"""


selected_variables = [
    "Input Voltage",
    "Output Voltage"
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for variable_name in selected_variables:

    ax.plot(
        time_ms,
        all_measurements[
            variable_name
        ],
        linewidth=2,
        label=variable_name
    )


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Selected Measurement Variables"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 13. DIFFERENT PHYSICAL UNITS
# ============================================================

"""
Now consider:

Voltage [V]

Current [A]

Temperature [°C]


These variables have different units.

Simply plotting all of them on the same ordinary Y-axis
can be misleading.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    output_voltage,
    label="Voltage [V]"
)


ax.plot(
    time_ms,
    output_current,
    label="Current [A]"
)


ax.plot(
    time_ms,
    temperature,
    label="Temperature [°C]"
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Mixed Units"
)

ax.set_title(
    "Different Variables on One Axis - Use with Caution"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 14. WHY THIS CAN BE MISLEADING
# ============================================================

"""
The previous plot is technically valid Python code.

However:

Voltage may vary from:

0 to 100 V

Current may vary from:

0 to 3 A

Temperature may vary from:

25 to 70 °C


Because the scales differ significantly, current may appear
almost flat even if its relative variation is important.

The problem is therefore not Python.

The problem is scientific interpretation.
"""


# ============================================================
# 15. POSSIBLE SOLUTIONS
# ============================================================

"""
When variables have different physical units or scales,
possible visualization strategies include:

1. Separate figures

2. Subplots

3. Dual Y-axis

4. Normalization

5. Plot only the variables relevant to the question


Subplots and dual-axis figures are covered in later files.

This example focuses on normalization.
"""


# ============================================================
# 16. WHAT IS NORMALIZATION?
# ============================================================

"""
Normalization transforms variables to a common numerical
scale.

One common method is min-max normalization:

                  x - x_min
x_normalized = ----------------
                x_max - x_min


The resulting values usually range from:

0 to 1


This allows variables with different units to be compared
in terms of their relative behavior.
"""


# ============================================================
# 17. CREATE NORMALIZATION FUNCTION
# ============================================================

def min_max_normalize(
    data
):
    """
    Normalize numerical data between 0 and 1.

    Parameters
    ----------
    data : array-like
        Numerical dataset.

    Returns
    -------
    numpy.ndarray
        Normalized values.
    """

    data = np.asarray(
        data,
        dtype=float
    )


    minimum = np.min(
        data
    )

    maximum = np.max(
        data
    )


    if maximum == minimum:

        return np.zeros_like(
            data
        )


    normalized = (

        data
        - minimum

    ) / (

        maximum
        - minimum

    )


    return normalized


# ============================================================
# 18. NORMALIZE DIFFERENT VARIABLES
# ============================================================

normalized_voltage = min_max_normalize(
    output_voltage
)


normalized_current = min_max_normalize(
    output_current
)


normalized_temperature = min_max_normalize(
    temperature
)


# ============================================================
# 19. PLOT NORMALIZED VARIABLES
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_ms,
    normalized_voltage,
    linewidth=2,
    label="Voltage"
)


ax.plot(
    time_ms,
    normalized_current,
    linewidth=2,
    label="Current"
)


ax.plot(
    time_ms,
    normalized_temperature,
    linewidth=2,
    label="Temperature"
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Normalized Value [-]"
)

ax.set_title(
    "Normalized Variable Comparison"
)


ax.set_ylim(
    0,
    1.05
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 20. IMPORTANT NORMALIZATION NOTE
# ============================================================

"""
After normalization:

Voltage

Current

Temperature

no longer appear in their original engineering units.

Therefore the Y-axis must NOT be labeled:

Voltage [V]

or:

Current [A]


Instead use something such as:

Normalized Value [-]


The symbol:

[-]

indicates a dimensionless quantity.
"""


# ============================================================
# 21. NORMALIZATION DOES NOT REPLACE ORIGINAL DATA
# ============================================================

"""
Normalization helps compare trends.

It does not replace the original physical measurements.

For example:

Normalized Voltage = 0.8

does not directly tell the reader whether the actual
voltage was:

48 V

96 V

400 V


Therefore original-unit figures are still needed when
physical magnitude matters.
"""


# ============================================================
# 22. AUTOMATIC NORMALIZATION
# ============================================================

"""
Several variables can be normalized automatically.
"""


different_variables = {

    "Output Voltage": output_voltage,

    "Output Current": output_current,

    "Temperature": temperature

}


normalized_variables = {}


for variable_name, values in different_variables.items():

    normalized_variables[
        variable_name
    ] = min_max_normalize(
        values
    )


# ============================================================
# 23. AUTOMATIC NORMALIZED PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for variable_name, values in normalized_variables.items():

    ax.plot(
        time_ms,
        values,
        linewidth=2,
        label=variable_name
    )


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Normalized Value [-]"
)

ax.set_title(
    "Automatic Normalized Comparison"
)


ax.set_ylim(
    0,
    1.05
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 24. RELATIVE CHANGE
# ============================================================

"""
Another useful comparison is relative change.

For example:

                x
Relative Value = -----
                x_ref


where x_ref is a selected reference value.


This is useful when we want to compare changes relative
to a baseline.
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


design_a_loss = np.array(
    [
        4.0,
        5.5,
        7.0,
        9.0,
        11.5,
        14.0,
        17.0,
        20.5,
        24.0,
        28.0
    ]
)


design_b_loss = np.array(
    [
        3.5,
        4.8,
        6.2,
        7.8,
        9.8,
        12.0,
        14.5,
        17.2,
        20.0,
        23.0
    ]
)


# ============================================================
# 25. ABSOLUTE COMPARISON
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    design_a_loss,
    marker="o",
    label="Design A"
)


ax.plot(
    load_percent,
    design_b_loss,
    marker="o",
    label="Design B"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Absolute Power-Loss Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 26. CALCULATE REDUCTION
# ============================================================

"""
Calculate how much Design B reduces the loss relative to
Design A.

Percentage reduction:

                    A - B
Reduction [%] = ------------- × 100
                      A
"""


loss_reduction_percent = (

    (
        design_a_loss
        - design_b_loss
    )

    / design_a_loss

) * 100


# ============================================================
# 27. PLOT RELATIVE IMPROVEMENT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    loss_reduction_percent,
    marker="o",
    linewidth=2
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Power-Loss Reduction [%]"
)

ax.set_title(
    "Relative Performance Improvement"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 28. ENGINEERING EXAMPLE - MULTIPLE CASES
# ============================================================

"""
Suppose three converter designs are evaluated using
efficiency versus load.
"""


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
        89.2,
        91.3,
        92.9,
        94.0,
        94.7,
        95.1,
        95.3,
        95.2,
        95.0,
        94.7
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


efficiency_data = {

    "Baseline": baseline_efficiency,

    "Design A": design_a_efficiency,

    "Design B": design_b_efficiency

}


# ============================================================
# 29. AUTOMATIC ENGINEERING CASE PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, values in efficiency_data.items():

    ax.plot(
        load_percent,
        values,
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
# 30. SELECTING VARIABLES PROGRAMMATICALLY
# ============================================================

"""
Suppose a dictionary contains many datasets.
"""


measurement_database = {

    "Input Voltage": input_voltage,

    "Output Voltage": output_voltage,

    "Input Current": input_current,

    "Output Current": output_current,

    "Temperature": temperature,

    "Input Power": input_power,

    "Output Power": output_power

}


"""
We can create different figures by selecting specific
variables.
"""


voltage_selection = [
    "Input Voltage",
    "Output Voltage"
]


current_selection = [
    "Input Current",
    "Output Current"
]


power_selection = [
    "Input Power",
    "Output Power"
]


# ============================================================
# 31. REUSABLE PLOTTING FUNCTION
# ============================================================

def plot_selected_variables(
    x,
    data_dictionary,
    selected_variables,
    x_label,
    y_label,
    title
):
    """
    Plot selected variables from a dictionary.

    Parameters
    ----------
    x : array-like
        X-axis data.

    data_dictionary : dict
        Dictionary containing datasets.

    selected_variables : list
        Names of datasets to plot.

    x_label : str
        X-axis label.

    y_label : str
        Y-axis label.

    title : str
        Figure title.
    """

    fig, ax = plt.subplots(
        figsize=(7, 4.5)
    )


    for variable_name in selected_variables:

        ax.plot(
            x,
            data_dictionary[
                variable_name
            ],
            linewidth=2,
            label=variable_name
        )


    ax.set_xlabel(
        x_label
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

    ax.legend()


    plt.tight_layout()

    plt.show()


# ============================================================
# 32. USE REUSABLE FUNCTION - VOLTAGE
# ============================================================

plot_selected_variables(

    time_ms,

    measurement_database,

    voltage_selection,

    "Time [ms]",

    "Voltage [V]",

    "Voltage Comparison"

)


# ============================================================
# 33. USE REUSABLE FUNCTION - CURRENT
# ============================================================

plot_selected_variables(

    time_ms,

    measurement_database,

    current_selection,

    "Time [ms]",

    "Current [A]",

    "Current Comparison"

)


# ============================================================
# 34. USE REUSABLE FUNCTION - POWER
# ============================================================

plot_selected_variables(

    time_ms,

    measurement_database,

    power_selection,

    "Time [ms]",

    "Power [W]",

    "Power Comparison"

)


# ============================================================
# 35. WHY REUSABLE FUNCTIONS MATTER
# ============================================================

"""
Instead of repeatedly writing:

fig, ax = plt.subplots()

ax.plot(...)

ax.set_xlabel(...)

ax.set_ylabel(...)

ax.legend()

...


we can create the plotting structure once and reuse it.


This becomes especially powerful when we later work with:

CSV files

Excel files

Multiple simulation files

Experimental datasets

Parameter sweeps
"""


# ============================================================
# 36. SAVE FINAL FIGURE
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


for case_name, values in efficiency_data.items():

    ax.plot(
        load_percent,
        values,
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


# ============================================================
# 37. SAVE PNG
# ============================================================

png_file = (
    output_folder
    / "multiple_variables.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 38. SAVE PDF
# ============================================================

pdf_file = (
    output_folder
    / "multiple_variables.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 39. SAVE SVG
# ============================================================

svg_file = (
    output_folder
    / "multiple_variables.svg"
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
# 40. COMMON MISTAKE - PLOT EVERYTHING
# ============================================================

"""
A dataset containing 15 columns does NOT mean that all
15 variables should be shown on one figure.

Before plotting, ask:

What scientific question does this figure answer?


For example:

Question:

How do input and output voltages compare?


Required variables:

Input Voltage

Output Voltage


Not necessarily:

Current
Temperature
Power
Efficiency
Frequency
etc.
"""


# ============================================================
# 41. COMMON MISTAKE - MIXING UNITS
# ============================================================

"""
Avoid treating:

Voltage [V]

Current [A]

Temperature [°C]

as though they represented the same quantity.


Possible solutions:

Subplots

Dual Y-axis

Normalization

Separate figures


These methods are covered in later examples.
"""


# ============================================================
# 42. COMMON MISTAKE - NORMALIZED DATA WITH PHYSICAL UNITS
# ============================================================

"""
Incorrect:

Normalized values

Y-axis label:

Voltage [V]


Correct:

Normalized Value [-]


Once data have been normalized, the numerical values are
dimensionless.
"""


# ============================================================
# 43. COMMON MISTAKE - TOO MANY CURVES
# ============================================================

"""
Even when all variables have the same unit, too many curves
can make interpretation difficult.

For example:

20 voltage waveforms

may require:

- Selected representative cases
- Subplots
- Separate figures
- Automated filtering
- Another visualization method
"""


# ============================================================
# 44. COMMON MISTAKE - UNNECESSARY NORMALIZATION
# ============================================================

"""
Do not normalize data when absolute engineering magnitude
is important.

Example:

Maximum device temperature = 85 °C


A normalized temperature value:

0.92

does not directly indicate whether the device exceeded
the 85 °C operating limit.

Always preserve physical values when engineering limits
matter.
"""


# ============================================================
# 45. MULTIPLE-VARIABLE DECISION WORKFLOW
# ============================================================

"""
I have several variables
        ↓
Do they have the same unit?
       / \
     Yes  No
     ↓     ↓
Same     Are relative trends
Axis     being compared?
          / \
        Yes  No
        ↓     ↓
     Normalize   Separate Figures
                  / Subplots
                  / Dual Axis


Then ask:

Do all variables answer the same scientific question?

If NO:

Do not place them all on one figure.
"""


# ============================================================
# 46. PRACTICAL EXAMPLE
# ============================================================

"""
Dataset:

Time
Voltage
Current
Power
Temperature


Question 1:

How do input and output voltages compare?

Plot:

Input Voltage
Output Voltage


Question 2:

How do input and output currents compare?

Plot:

Input Current
Output Current


Question 3:

How do voltage, current and temperature evolve relatively?

Normalize
        ↓
Plot normalized variables


Question 4:

What are the absolute voltage, current and temperature
values simultaneously?

Use:

Subplots

or carefully designed multiple axes.


The next tutorials cover those approaches.
"""


# ============================================================
# 47. CONNECTION TO CSV AND EXCEL
# ============================================================

"""
Later, instead of manually defining:

measurement_database = {
    ...
}


Pandas may load columns directly from a file:

data = pd.read_csv(
    "measurement.csv"
)


Then:

selected_columns = [
    "Voltage",
    "Current",
    "Temperature"
]


The same selection and plotting concepts demonstrated in
this file can then be applied directly to external datasets.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
MULTIPLE VARIABLES


1. SAME UNIT + SIMILAR SCALE

Usually suitable for one Y-axis.

Example:

Input Voltage [V]

Output Voltage [V]


------------------------------------------------------------


2. DIFFERENT UNITS

Example:

Voltage [V]

Current [A]

Temperature [°C]


Do not automatically place them on one ordinary axis.


Consider:

Normalization

Subplots

Dual Y-axis

Separate figures


------------------------------------------------------------


3. DICTIONARY-BASED DATA

variables = {

    "Case A": values_a,

    "Case B": values_b

}


Then:

for name, values in variables.items():

    ax.plot(
        x,
        values,
        label=name
    )


------------------------------------------------------------


4. SELECT ONLY REQUIRED VARIABLES

selected = [
    "Input Voltage",
    "Output Voltage"
]


Plot only data relevant to the research question.


------------------------------------------------------------


5. MIN-MAX NORMALIZATION

                  x - min(x)
x_normalized = ----------------
                max(x) - min(x)


Python:

normalized = (
    data - np.min(data)
) / (
    np.max(data) - np.min(data)
)


------------------------------------------------------------


6. NORMALIZED VARIABLES

Normally use:

Normalized Value [-]


Do NOT assign the original engineering unit.


------------------------------------------------------------


7. RELATIVE IMPROVEMENT

Example:

                Baseline - New
Reduction = ---------------------- × 100
                   Baseline


Useful for:

Power-loss reduction

Efficiency improvement

Error reduction

Performance comparison


------------------------------------------------------------


8. REUSABLE FUNCTION

A plotting function can reduce repeated code:

plot_selected_variables(
    x,
    data,
    selected,
    xlabel,
    ylabel,
    title
)


------------------------------------------------------------


9. MOST IMPORTANT QUESTION

Do not ask only:

"How many variables can Python plot?"


Ask:

"Which variables should be shown together to communicate
the engineering result correctly?"


------------------------------------------------------------


10. MULTIPLE-VARIABLE WORKFLOW

Dataset
   ↓
Identify Research Question
   ↓
Select Relevant Variables
   ↓
Check Units
   ↓
Check Numerical Scale
   ↓
Choose Visualization Method
   ↓
Plot
   ↓
Validate Scientific Meaning
   ↓
Save Figure


------------------------------------------------------------


NEXT:

07_subplots.py

will address:

Voltage [V]
Current [A]
Temperature [°C]

without mixing their physical units on the same Y-axis.

Example:

┌─────────────────────────┐
│ Voltage vs Time         │
├─────────────────────────┤
│ Current vs Time         │
├─────────────────────────┤
│ Temperature vs Time     │
└─────────────────────────┘

This is often one of the clearest approaches for
multi-variable engineering datasets.
"""
