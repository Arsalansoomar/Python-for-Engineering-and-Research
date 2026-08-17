"""
============================================================
Python for Engineering and Research
21 - Engineering Comparison Plot
============================================================

Purpose:
    Demonstrate a complete engineering comparison workflow
    for evaluating several designs, experiments, simulations,
    or operating cases against a common baseline.

Topics:
    1. What is an engineering comparison?
    2. Baseline/reference definition
    3. Comparing several cases
    4. Absolute differences
    5. Relative percentage differences
    6. Improvement and reduction
    7. Mean, minimum, maximum, and peak values
    8. Ranking cases
    9. Time-domain comparison
    10. Selected operating-point comparison
    11. Grouped bar plots
    12. Difference plots
    13. Normalized comparison
    14. Frequency-domain comparison
    15. dB reduction calculations
    16. Selected-frequency comparison
    17. Summary tables
    18. Automatic case processing
    19. Subplots
    20. Reusable comparison functions
    21. Publication-oriented final figure
    22. PNG / PDF / SVG export
    23. Common mistakes
    24. Key takeaways

Sample Files:
    sample_data/multiple_cases.csv
    sample_data/fft_example.csv

Important:
    Comparisons are meaningful only when the cases use
    consistent operating conditions, units, processing,
    sampling, and measurement definitions.

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. REQUIRED LIBRARIES
# ============================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pathlib import Path

from matplotlib.ticker import (
    FuncFormatter,
    MultipleLocator,
    LogLocator,
    NullFormatter
)


# ============================================================
# 2. WHAT IS AN ENGINEERING COMPARISON?
# ============================================================

"""
Engineering research often asks questions such as:

Which design performs better?

How much improvement was achieved?

At which operating condition is the improvement largest?

Does one design improve one region but worsen another?

Is the improvement broadband or localized?

Which case has the lowest loss?

Which configuration provides the highest efficiency?

Which design gives the lowest frequency-domain magnitude?


A useful comparison workflow is:

Reference Case
      ↓
Alternative Cases
      ↓
Same Operating Conditions
      ↓
Calculate Metrics
      ↓
Plot Comparison
      ↓
Quantify Difference
      ↓
Interpret Result
"""


# ============================================================
# 3. COMPARISON MUST BE FAIR
# ============================================================

"""
Before comparing two engineering datasets, verify:

- Same physical quantity
- Same units
- Same operating conditions
- Same sampling method
- Same processing method
- Same measurement window
- Same reference definition
- Same axis convention
- Same normalization method


Example:

Comparing converter efficiencies measured at:

Different input voltages

Different loads

Different temperatures

or

different measurement procedures

may not provide a fair design comparison.
"""


# ============================================================
# 4. PROJECT PATHS
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


sample_data_folder = (
    script_folder
    / "sample_data"
)


output_figure_folder = (
    script_folder
    / "output_figures"
    / "engineering_comparison"
)


output_data_folder = (
    script_folder
    / "output_data"
)


output_figure_folder.mkdir(
    parents=True,
    exist_ok=True
)


output_data_folder.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 5. LOAD TIME-DOMAIN COMPARISON DATA
# ============================================================

time_domain_file = (
    sample_data_folder
    / "multiple_cases.csv"
)


if not time_domain_file.exists():

    raise FileNotFoundError(
        f"\nComparison file not found:\n"
        f"{time_domain_file}"
    )


time_data = pd.read_csv(
    time_domain_file
)


print(
    "\n--- Time-Domain Dataset ---"
)


print(
    time_data.head()
)


print(
    "\nColumns:"
)


print(
    time_data.columns.tolist()
)


# ============================================================
# 6. EXPECTED COLUMNS
# ============================================================

"""
Expected structure:

Time_s

Case_A_V

Case_B_V

Case_C_V

Case_D_V
"""


required_time_columns = [

    "Time_s",

    "Case_A_V",

    "Case_B_V",

    "Case_C_V",

    "Case_D_V"

]


missing_columns = [

    column

    for column in required_time_columns

    if column not in time_data.columns

]


if missing_columns:

    raise KeyError(
        f"Missing columns: "
        f"{missing_columns}"
    )


# ============================================================
# 7. CLEAN NUMERIC DATA
# ============================================================

for column in required_time_columns:

    time_data[
        column
    ] = pd.to_numeric(

        time_data[
            column
        ],

        errors="coerce"

    )


time_data = time_data.dropna(
    subset=required_time_columns
)


time_data = time_data.sort_values(
    "Time_s"
)


# ============================================================
# 8. DEFINE CASES
# ============================================================

"""
Use a dictionary to separate:

Human-readable case name

from:

Raw DataFrame column name.
"""


time_cases = {

    "Case A":
        "Case_A_V",

    "Case B":
        "Case_B_V",

    "Case C":
        "Case_C_V",

    "Case D":
        "Case_D_V"

}


# ============================================================
# 9. DEFINE BASELINE / REFERENCE CASE
# ============================================================

"""
Most engineering comparisons require a reference.

Example:

Baseline
vs
Optimized Design


For this tutorial:

Case A

is treated as the reference.
"""


REFERENCE_NAME = "Case A"

REFERENCE_COLUMN = time_cases[
    REFERENCE_NAME
]


print(
    "\nReference Case:"
)


print(
    REFERENCE_NAME
)


# ============================================================
# 10. BASIC MULTIPLE-CASE COMPARISON
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, column_name in time_cases.items():

    ax.plot(

        time_data[
            "Time_s"
        ],

        time_data[
            column_name
        ],

        linewidth=2,

        label=case_name

    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Engineering Case Comparison"
)


ax.grid(
    True
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 11. USE DIFFERENT LINE STYLES
# ============================================================

"""
Different line styles help identify cases even if the
figure is printed in grayscale.
"""


line_styles = {

    "Case A":
        "-",

    "Case B":
        "--",

    "Case C":
        "-.",

    "Case D":
        ":"

}


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, column_name in time_cases.items():

    ax.plot(

        time_data[
            "Time_s"
        ],

        time_data[
            column_name
        ],

        linestyle=line_styles[
            case_name
        ],

        linewidth=2,

        label=case_name

    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 12. ABSOLUTE DIFFERENCE
# ============================================================

"""
A direct engineering comparison can calculate:

Difference
=
Case
-
Reference


Example:

Case B - Case A


Interpretation depends on the physical quantity.

For voltage:

Positive difference
    ↓
Case value is higher


Negative difference
    ↓
Case value is lower
"""


reference_voltage = time_data[
    REFERENCE_COLUMN
]


for case_name, column_name in time_cases.items():

    if case_name == REFERENCE_NAME:

        continue


    difference_column = (

        case_name
        .replace(
            " ",
            "_"
        )

        + "_Difference_V"

    )


    time_data[
        difference_column
    ] = (

        time_data[
            column_name
        ]

        - reference_voltage

    )


# ============================================================
# 13. INSPECT DIFFERENCE DATA
# ============================================================

difference_columns = [

    column

    for column in time_data.columns

    if "Difference_V" in column

]


print(
    "\n--- Difference Columns ---"
)


print(
    difference_columns
)


print(
    time_data[
        [
            "Time_s"
        ]
        + difference_columns
    ].head()
)


# ============================================================
# 14. DIFFERENCE PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for column_name in difference_columns:

    label = (

        column_name

        .replace(
            "_Difference_V",
            ""
        )

        .replace(
            "_",
            " "
        )

    )


    ax.plot(

        time_data[
            "Time_s"
        ],

        time_data[
            column_name
        ],

        linewidth=2,

        label=label

    )


ax.axhline(
    y=0,
    linestyle="--",
    linewidth=1
)


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Difference from Case A [V]"
)

ax.set_title(
    "Difference Relative to Reference"
)


ax.grid(
    True
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 15. RELATIVE PERCENTAGE DIFFERENCE
# ============================================================

"""
For LINEAR quantities, relative percentage difference may
be useful.

Formula:

Relative Change [%]

=

(Case - Reference)
------------------
    Reference

× 100


Important:

The reference must not be zero.
"""


def calculate_relative_change(
    new_values,
    reference_values
):
    """
    Calculate percentage change relative to a reference.

    Undefined locations where reference = 0 are returned
    as NaN.
    """

    new_values = np.asarray(
        new_values,
        dtype=float
    )


    reference_values = np.asarray(
        reference_values,
        dtype=float
    )


    if (
        new_values.shape
        != reference_values.shape
    ):

        raise ValueError(
            "New and reference arrays must have "
            "the same shape."
        )


    result = np.full(
        reference_values.shape,
        np.nan,
        dtype=float
    )


    valid = (

        reference_values
        != 0

    )


    result[
        valid
    ] = (

        (
            new_values[
                valid
            ]

            - reference_values[
                valid
            ]
        )

        / reference_values[
            valid
        ]

    ) * 100


    return result


# ============================================================
# 16. CALCULATE RELATIVE CHANGES
# ============================================================

for case_name, column_name in time_cases.items():

    if case_name == REFERENCE_NAME:

        continue


    relative_column = (

        case_name
        .replace(
            " ",
            "_"
        )

        + "_Relative_Change_percent"

    )


    time_data[
        relative_column
    ] = calculate_relative_change(

        time_data[
            column_name
        ],

        reference_voltage

    )


# ============================================================
# 17. PLOT RELATIVE CHANGE
# ============================================================

relative_columns = [

    column

    for column in time_data.columns

    if "Relative_Change_percent"
    in column

]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for column_name in relative_columns:

    label = (

        column_name

        .replace(
            "_Relative_Change_percent",
            ""
        )

        .replace(
            "_",
            " "
        )

    )


    ax.plot(

        time_data[
            "Time_s"
        ],

        time_data[
            column_name
        ],

        linewidth=2,

        label=label

    )


ax.axhline(
    y=0,
    linestyle="--",
    linewidth=1
)


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Relative Change [%]"
)


ax.grid(
    True
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 18. IMPORTANT: IMPROVEMENT DEPENDS ON THE METRIC
# ============================================================

"""
Do not assume:

Higher = Better


For some quantities:

Higher is better:

- Efficiency
- Output power
- Accuracy


For others:

Lower is better:

- Power loss
- Temperature
- Error
- EMI magnitude
- THD
- Overshoot


Therefore the mathematical definition of:

"Improvement"

depends on the physical metric.
"""


# ============================================================
# 19. LOWER-IS-BETTER REDUCTION
# ============================================================

"""
For a quantity where LOWER is better:

Reduction [%]

=

Reference - New
---------------
   Reference

× 100
"""


def calculate_reduction_percent(
    new_values,
    reference_values
):
    """
    Calculate percentage reduction for a linear quantity
    where lower values indicate improvement.
    """

    new_values = np.asarray(
        new_values,
        dtype=float
    )


    reference_values = np.asarray(
        reference_values,
        dtype=float
    )


    if (
        new_values.shape
        != reference_values.shape
    ):

        raise ValueError(
            "New and reference arrays must have "
            "the same shape."
        )


    result = np.full(
        reference_values.shape,
        np.nan,
        dtype=float
    )


    valid = (

        reference_values
        != 0

    )


    result[
        valid
    ] = (

        (
            reference_values[
                valid
            ]

            - new_values[
                valid
            ]
        )

        / reference_values[
            valid
        ]

    ) * 100


    return result


# ============================================================
# 20. HIGHER-IS-BETTER IMPROVEMENT
# ============================================================

"""
For a quantity where HIGHER is better:

Improvement [%]

=

New - Reference
---------------
   Reference

× 100
"""


def calculate_improvement_percent(
    new_values,
    reference_values
):
    """
    Calculate percentage improvement for a linear quantity
    where higher values indicate improvement.
    """

    return calculate_relative_change(
        new_values,
        reference_values
    )


# ============================================================
# 21. SUMMARY STATISTICS
# ============================================================

"""
Engineering comparison frequently uses summary metrics.

Examples:

Mean

Minimum

Maximum

Peak-to-peak

Final value

Number of samples
"""


summary_results = []


for case_name, column_name in time_cases.items():

    values = time_data[
        column_name
    ]


    summary_results.append(
        {
            "Case":
                case_name,

            "Samples":
                len(
                    values
                ),

            "Mean_V":
                values.mean(),

            "Minimum_V":
                values.min(),

            "Maximum_V":
                values.max(),

            "Peak_to_Peak_V":
                (
                    values.max()
                    - values.min()
                ),

            "Final_V":
                values.iloc[
                    -1
                ]
        }
    )


summary_data = pd.DataFrame(
    summary_results
)


print(
    "\n--- Time-Domain Summary ---"
)


print(
    summary_data
)


# ============================================================
# 22. SAVE SUMMARY DATA
# ============================================================

summary_file = (
    output_data_folder
    / "engineering_comparison_summary.csv"
)


summary_data.to_csv(
    summary_file,
    index=False
)


print(
    "\nSummary saved to:"
)


print(
    summary_file
)


# ============================================================
# 23. RANK CASES
# ============================================================

"""
Suppose the engineering objective is:

Highest final voltage.


Cases can be ranked automatically.
"""


ranked_final_voltage = (

    summary_data

    .sort_values(
        "Final_V",
        ascending=False
    )

    .reset_index(
        drop=True
    )

)


ranked_final_voltage[
    "Rank"
] = np.arange(
    1,
    len(
        ranked_final_voltage
    )
    + 1
)


print(
    "\n--- Ranking by Final Voltage ---"
)


print(
    ranked_final_voltage[
        [
            "Rank",
            "Case",
            "Final_V"
        ]
    ]
)


# ============================================================
# 24. RANKING DIRECTION MATTERS
# ============================================================

"""
For:

Efficiency

higher may be better.

Use:

ascending=False


For:

Loss

Temperature

EMI

Error

lower may be better.

Use:

ascending=True


The code cannot determine engineering meaning
automatically.
"""


# ============================================================
# 25. BAR PLOT OF FINAL VALUES
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(

    summary_data[
        "Case"
    ],

    summary_data[
        "Final_V"
    ]

)


ax.bar_label(
    bars,
    fmt="%.2f",
    padding=3
)


ax.set_xlabel(
    "Case"
)

ax.set_ylabel(
    "Final Voltage [V]"
)

ax.set_title(
    "Final Value Comparison"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 26. BAR PLOT OF MAXIMUM VALUES
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(

    summary_data[
        "Case"
    ],

    summary_data[
        "Maximum_V"
    ]

)


ax.bar_label(
    bars,
    fmt="%.2f",
    padding=3
)


ax.set_ylabel(
    "Maximum Voltage [V]"
)

ax.set_title(
    "Maximum Voltage Comparison"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 27. SELECTED OPERATING POINTS
# ============================================================

"""
Sometimes researchers do not need every sample.

Instead they compare selected points.

Example:

5 ms

10 ms

15 ms

20 ms
"""


selected_times = np.array(
    [
        0.005,
        0.010,
        0.015,
        0.020
    ]
)


# ============================================================
# 28. FIND NEAREST AVAILABLE SAMPLE
# ============================================================

def find_nearest_row(
    dataframe,
    x_column,
    target_value
):
    """
    Return the row nearest to a requested X value.
    """

    index = (

        dataframe[
            x_column
        ]

        .sub(
            target_value
        )

        .abs()

        .idxmin()

    )


    return dataframe.loc[
        index
    ]


# ============================================================
# 29. EXTRACT SELECTED OPERATING POINTS
# ============================================================

selected_rows = []


for requested_time in selected_times:

    row = find_nearest_row(

        dataframe=time_data,

        x_column="Time_s",

        target_value=requested_time

    )


    selected_rows.append(
        row
    )


selected_data = pd.DataFrame(
    selected_rows
)


print(
    "\n--- Selected Operating Points ---"
)


print(
    selected_data[
        required_time_columns
    ]
)


# ============================================================
# 30. GROUPED BAR COMPARISON
# ============================================================

"""
Grouped bar plots are useful when comparing several cases
at selected operating points.
"""


number_of_cases = len(
    time_cases
)


number_of_points = len(
    selected_data
)


x_positions = np.arange(
    number_of_points
)


total_group_width = 0.8


bar_width = (

    total_group_width

    / number_of_cases

)


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for case_index, (
    case_name,
    column_name
) in enumerate(
    time_cases.items()
):

    offset = (

        (
            case_index
            - (
                number_of_cases
                - 1
            )
            / 2
        )

        * bar_width

    )


    ax.bar(

        x_positions
        + offset,

        selected_data[
            column_name
        ],

        width=bar_width,

        label=case_name

    )


time_labels = [

    f"{value * 1000:.0f} ms"

    for value in selected_data[
        "Time_s"
    ]

]


ax.set_xticks(
    x_positions
)


ax.set_xticklabels(
    time_labels
)


ax.set_xlabel(
    "Time"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Selected Operating-Point Comparison"
)


ax.legend()


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 31. NORMALIZED COMPARISON
# ============================================================

"""
Normalization is useful when curves have different
absolute magnitudes but their SHAPES need comparison.

One common normalization is:

Normalized Value
=
Value / Maximum Value


This scales each case approximately between:

0 and 1


Normalization changes the physical representation.

Therefore the axis should not still be labeled:

Voltage [V]


Instead:

Normalized Voltage [-]
"""


normalized_data = pd.DataFrame(
    {
        "Time_s":
            time_data[
                "Time_s"
            ]
    }
)


for case_name, column_name in time_cases.items():

    maximum_value = time_data[
        column_name
    ].abs().max()


    if maximum_value == 0:

        normalized_values = np.zeros(
            len(
                time_data
            )
        )

    else:

        normalized_values = (

            time_data[
                column_name
            ]

            / maximum_value

        )


    normalized_data[
        case_name
    ] = normalized_values


# ============================================================
# 32. NORMALIZED PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name in time_cases:

    ax.plot(

        normalized_data[
            "Time_s"
        ],

        normalized_data[
            case_name
        ],

        linewidth=2,

        label=case_name

    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Normalized Voltage [-]"
)


ax.grid(
    True
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 33. RAW VS NORMALIZED
# ============================================================

"""
RAW DATA

Answers:

What are the actual physical values?


Example:

Voltage [V]


------------------------------------------------------------


NORMALIZED DATA

Answers:

How do relative shapes or trends compare?


Example:

Normalized Voltage [-]


Do not replace raw engineering results with normalized
results unless normalization supports the research
question.
"""


# ============================================================
# 34. COMPARISON SUBPLOTS
# ============================================================

"""
A useful engineering figure can show:

Top:

Absolute values


Bottom:

Difference from reference
"""


fig, axes = plt.subplots(

    2,

    1,

    figsize=(8, 7),

    sharex=True

)


# Absolute comparison

for case_name, column_name in time_cases.items():

    axes[0].plot(

        time_data[
            "Time_s"
        ],

        time_data[
            column_name
        ],

        linewidth=2,

        label=case_name

    )


axes[0].set_ylabel(
    "Voltage [V]"
)


axes[0].set_title(
    "Absolute Comparison"
)


axes[0].legend()


axes[0].grid(
    True
)


# Difference comparison

for column_name in difference_columns:

    label = (

        column_name

        .replace(
            "_Difference_V",
            ""
        )

        .replace(
            "_",
            " "
        )

    )


    axes[1].plot(

        time_data[
            "Time_s"
        ],

        time_data[
            column_name
        ],

        linewidth=2,

        label=label

    )


axes[1].axhline(
    y=0,
    linestyle="--"
)


axes[1].set_xlabel(
    "Time [s]"
)


axes[1].set_ylabel(
    "Difference [V]"
)


axes[1].set_title(
    "Difference Relative to Case A"
)


axes[1].legend()


axes[1].grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 35. LOAD FREQUENCY-DOMAIN DATA
# ============================================================

fft_file = (
    sample_data_folder
    / "fft_example.csv"
)


if not fft_file.exists():

    raise FileNotFoundError(
        f"\nFFT comparison file not found:\n"
        f"{fft_file}"
    )


fft_data = pd.read_csv(
    fft_file
)


print(
    "\n--- Frequency Dataset ---"
)


print(
    fft_data.head()
)


# ============================================================
# 36. DEFINE FREQUENCY CASES
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


frequency_required_columns = [

    "Frequency_Hz"

] + list(
    frequency_cases.values()
)


missing_frequency_columns = [

    column

    for column in frequency_required_columns

    if column not in fft_data.columns

]


if missing_frequency_columns:

    raise KeyError(
        f"Missing frequency columns: "
        f"{missing_frequency_columns}"
    )


# ============================================================
# 37. CLEAN FREQUENCY DATA
# ============================================================

for column in frequency_required_columns:

    fft_data[
        column
    ] = pd.to_numeric(

        fft_data[
            column
        ],

        errors="coerce"

    )


fft_data = fft_data.dropna(
    subset=frequency_required_columns
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
# 38. FREQUENCY FORMATTER
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
# 39. FREQUENCY-DOMAIN CASE COMPARISON
# ============================================================

frequency_line_styles = {

    "Unshielded":
        "-",

    "Case A":
        "--",

    "Case B":
        "-.",

    "Case C":
        ":"

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

        linestyle=frequency_line_styles[
            case_name
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


ax.grid(
    True,
    which="both"
)


ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 40. IMPORTANT: dB COMPARISON
# ============================================================

"""
dB and dBµV are logarithmic quantities.

Therefore do NOT calculate:

Percentage Reduction

directly from:

dB values


For example:

100 dBµV

to:

90 dBµV


should not automatically be described as:

10% reduction.


The direct and meaningful comparison in the dB domain is:

Difference
=
100 dBµV - 90 dBµV
=
10 dB


This is a:

10 dB reduction.
"""


# ============================================================
# 41. DEFINE FREQUENCY BASELINE
# ============================================================

frequency_reference_name = (
    "Unshielded"
)


frequency_reference_column = (
    frequency_cases[
        frequency_reference_name
    ]
)


# ============================================================
# 42. CALCULATE dB REDUCTION
# ============================================================

"""
For an attenuation problem where lower dBµV is better:

Reduction [dB]

=

Reference [dBµV]
-
Case [dBµV]


Positive:

Improvement / reduction


Negative:

The new case has a higher magnitude than reference.
"""


for case_name, column_name in frequency_cases.items():

    if case_name == frequency_reference_name:

        continue


    reduction_column = (

        case_name
        .replace(
            " ",
            "_"
        )

        + "_Reduction_dB"

    )


    fft_data[
        reduction_column
    ] = (

        fft_data[
            frequency_reference_column
        ]

        - fft_data[
            column_name
        ]

    )


# ============================================================
# 43. INSPECT dB REDUCTION
# ============================================================

db_reduction_columns = [

    column

    for column in fft_data.columns

    if "Reduction_dB"
    in column

]


print(
    "\n--- dB Reduction Columns ---"
)


print(
    fft_data[
        [
            "Frequency_Hz"
        ]
        + db_reduction_columns
    ].head()
)


# ============================================================
# 44. PLOT dB REDUCTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for column_name in db_reduction_columns:

    label = (

        column_name

        .replace(
            "_Reduction_dB",
            ""
        )

        .replace(
            "_",
            " "
        )

    )


    ax.plot(

        fft_data[
            "Frequency_Hz"
        ],

        fft_data[
            column_name
        ],

        linewidth=2,

        label=label

    )


ax.axhline(
    y=0,
    linestyle="--"
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
    "Reduction Relative to Unshielded [dB]"
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
# 45. INTERPRET dB REDUCTION SIGN
# ============================================================

"""
With:

Reduction
=
Reference - Case


Positive value:

Case magnitude is lower than reference.


Example:

Reference = 100 dBµV

Case = 88 dBµV

Reduction = +12 dB


------------------------------------------------------------


Negative value:

Case magnitude is higher than reference.


Example:

Reference = 90 dBµV

Case = 94 dBµV

Reduction = -4 dB


This indicates a local increase of 4 dB.
"""


# ============================================================
# 46. SELECTED FREQUENCIES
# ============================================================

"""
Engineering papers often summarize performance at
selected frequencies.

Example:

100 kHz

500 kHz

1 MHz

5 MHz

10 MHz

20 MHz

30 MHz
"""


selected_frequencies = [

    100e3,

    500e3,

    1e6,

    5e6,

    10e6,

    20e6,

    30e6

]


# ============================================================
# 47. EXTRACT NEAREST FREQUENCY SAMPLES
# ============================================================

frequency_rows = []


for target_frequency in selected_frequencies:

    row = find_nearest_row(

        dataframe=fft_data,

        x_column="Frequency_Hz",

        target_value=target_frequency

    )


    frequency_rows.append(
        row
    )


selected_frequency_data = pd.DataFrame(
    frequency_rows
)


print(
    "\n--- Selected Frequency Data ---"
)


print(
    selected_frequency_data[
        frequency_required_columns
    ]
)


# ============================================================
# 48. SELECTED-FREQUENCY GROUPED BAR PLOT
# ============================================================

number_of_cases = len(
    frequency_cases
)


x_positions = np.arange(
    len(
        selected_frequency_data
    )
)


bar_width = (

    0.8

    / number_of_cases

)


fig, ax = plt.subplots(
    figsize=(10, 5)
)


for case_index, (
    case_name,
    column_name
) in enumerate(
    frequency_cases.items()
):

    offset = (

        (
            case_index

            - (
                number_of_cases
                - 1
            )
            / 2
        )

        * bar_width

    )


    ax.bar(

        x_positions
        + offset,

        selected_frequency_data[
            column_name
        ],

        width=bar_width,

        label=case_name

    )


frequency_labels = [

    format_frequency(
        value
    )

    for value in selected_frequency_data[
        "Frequency_Hz"
    ]

]


ax.set_xticks(
    x_positions
)


ax.set_xticklabels(
    frequency_labels,
    rotation=20
)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Selected-Frequency Comparison"
)


ax.legend()


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 49. SELECTED-FREQUENCY REDUCTION BAR PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(10, 5)
)


reduction_cases = {

    "Case A":
        "Case_A_Reduction_dB",

    "Case B":
        "Case_B_Reduction_dB",

    "Case C":
        "Case_C_Reduction_dB"

}


number_of_reduction_cases = len(
    reduction_cases
)


reduction_bar_width = (

    0.75

    / number_of_reduction_cases

)


for case_index, (
    case_name,
    column_name
) in enumerate(
    reduction_cases.items()
):

    offset = (

        (
            case_index

            - (
                number_of_reduction_cases
                - 1
            )
            / 2
        )

        * reduction_bar_width

    )


    ax.bar(

        x_positions
        + offset,

        selected_frequency_data[
            column_name
        ],

        width=reduction_bar_width,

        label=case_name

    )


ax.axhline(
    y=0,
    linestyle="--"
)


ax.set_xticks(
    x_positions
)


ax.set_xticklabels(
    frequency_labels,
    rotation=20
)


ax.set_xlabel(
    "Frequency"
)

ax.set_ylabel(
    "Reduction Relative to Unshielded [dB]"
)

ax.set_title(
    "Selected-Frequency Reduction"
)


ax.legend()


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 50. MAXIMUM REDUCTION FOR EACH CASE
# ============================================================

frequency_summary_results = []


for case_name, reduction_column in reduction_cases.items():

    maximum_index = fft_data[
        reduction_column
    ].idxmax()


    maximum_reduction = fft_data.loc[
        maximum_index,
        reduction_column
    ]


    maximum_reduction_frequency = (
        fft_data.loc[
            maximum_index,
            "Frequency_Hz"
        ]
    )


    minimum_reduction = fft_data[
        reduction_column
    ].min()


    mean_reduction = fft_data[
        reduction_column
    ].mean()


    frequency_summary_results.append(
        {
            "Case":
                case_name,

            "Maximum_Reduction_dB":
                maximum_reduction,

            "Frequency_at_Maximum_Hz":
                maximum_reduction_frequency,

            "Mean_Reduction_dB":
                mean_reduction,

            "Minimum_Reduction_dB":
                minimum_reduction
        }
    )


frequency_summary = pd.DataFrame(
    frequency_summary_results
)


print(
    "\n--- Frequency Reduction Summary ---"
)


print(
    frequency_summary
)


# ============================================================
# 51. FORMAT FREQUENCY SUMMARY
# ============================================================

frequency_summary[
    "Frequency_at_Maximum"
] = [

    format_frequency(
        value
    )

    for value in frequency_summary[
        "Frequency_at_Maximum_Hz"
    ]

]


print(
    "\n--- Formatted Frequency Summary ---"
)


print(
    frequency_summary[
        [
            "Case",

            "Maximum_Reduction_dB",

            "Frequency_at_Maximum",

            "Mean_Reduction_dB",

            "Minimum_Reduction_dB"
        ]
    ]
)


# ============================================================
# 52. NEGATIVE REDUCTION CHECK
# ============================================================

"""
A useful engineering comparison should also report whether
a design becomes WORSE anywhere.

Example:

Case may provide strong attenuation at high frequency

but:

increase magnitude at another frequency.
"""


for case_name, reduction_column in reduction_cases.items():

    worse_points = fft_data[
        fft_data[
            reduction_column
        ] < 0
    ]


    print(
        f"\n{case_name}:"
    )


    print(
        "Number of frequency points "
        "with negative reduction:",
        len(
            worse_points
        )
    )


# ============================================================
# 53. PERCENT OF FREQUENCY POINTS IMPROVED
# ============================================================

improvement_coverage_results = []


for case_name, reduction_column in reduction_cases.items():

    improved_points = (

        fft_data[
            reduction_column
        ] > 0

    ).sum()


    total_points = len(
        fft_data
    )


    improvement_coverage = (

        improved_points

        / total_points

        * 100

    )


    improvement_coverage_results.append(
        {
            "Case":
                case_name,

            "Improved_Points":
                improved_points,

            "Total_Points":
                total_points,

            "Improved_Frequency_Points_percent":
                improvement_coverage
        }
    )


coverage_summary = pd.DataFrame(
    improvement_coverage_results
)


print(
    "\n--- Improvement Coverage ---"
)


print(
    coverage_summary
)


# ============================================================
# 54. IMPORTANT COVERAGE NOTE
# ============================================================

"""
The percentage of frequency SAMPLES improved is not
automatically equivalent to:

Percentage of physical bandwidth improved.


Why?

Frequency samples may not be uniformly spaced.


For example:

A logarithmic frequency sweep

contains samples according to a log-frequency grid.


Therefore this metric should be described precisely as:

"Percentage of sampled frequency points showing reduction"


not automatically:

"Percentage of bandwidth reduced."
"""


# ============================================================
# 55. COMBINE FREQUENCY SUMMARIES
# ============================================================

frequency_summary = frequency_summary.merge(

    coverage_summary[
        [
            "Case",
            "Improved_Frequency_Points_percent"
        ]
    ],

    on="Case",

    how="left"

)


# ============================================================
# 56. SAVE FREQUENCY SUMMARY
# ============================================================

frequency_summary_file = (
    output_data_folder
    / "frequency_engineering_comparison_summary.csv"
)


frequency_summary.to_csv(
    frequency_summary_file,
    index=False
)


print(
    "\nFrequency summary saved to:"
)


print(
    frequency_summary_file
)


# ============================================================
# 57. COMPARISON METRIC BAR PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(

    frequency_summary[
        "Case"
    ],

    frequency_summary[
        "Maximum_Reduction_dB"
    ]

)


ax.bar_label(
    bars,
    fmt="%.1f dB",
    padding=3
)


ax.set_xlabel(
    "Case"
)

ax.set_ylabel(
    "Maximum Reduction [dB]"
)

ax.set_title(
    "Maximum Reduction Comparison"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 58. COMPARISON METRIC SELECTION
# ============================================================

"""
Be careful when ranking engineering designs using only one
number.

A design may have:

Largest maximum reduction

but poor broadband behavior.


Another may have:

Lower maximum reduction

but consistent improvement across the full frequency range.


Therefore consider multiple metrics:

- Maximum improvement
- Mean improvement
- Minimum improvement
- Number of worsened points
- Operating range
- Efficiency
- Cost
- Complexity
- Thermal effect

depending on the research problem.
"""


# ============================================================
# 59. MULTI-METRIC COMPARISON
# ============================================================

fig, axes = plt.subplots(

    2,

    1,

    figsize=(8, 7)

)


# Maximum reduction

axes[0].bar(

    frequency_summary[
        "Case"
    ],

    frequency_summary[
        "Maximum_Reduction_dB"
    ]

)


axes[0].set_ylabel(
    "Maximum Reduction [dB]"
)


axes[0].grid(
    True,
    axis="y"
)


# Mean reduction

axes[1].bar(

    frequency_summary[
        "Case"
    ],

    frequency_summary[
        "Mean_Reduction_dB"
    ]

)


axes[1].set_xlabel(
    "Case"
)


axes[1].set_ylabel(
    "Mean Reduction [dB]"
)


axes[1].grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 60. REUSABLE SUMMARY FUNCTION
# ============================================================

def summarize_cases(
    dataframe,
    case_columns
):
    """
    Calculate basic summary statistics for several columns.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Input dataset.

    case_columns : dict
        Mapping:
        display name -> column name

    Returns
    -------
    summary : pandas.DataFrame
    """

    results = []


    for case_name, column_name in case_columns.items():

        if column_name not in dataframe.columns:

            raise KeyError(
                f"Column not found: "
                f"{column_name}"
            )


        values = pd.to_numeric(

            dataframe[
                column_name
            ],

            errors="coerce"

        ).dropna()


        if values.empty:

            raise ValueError(
                f"No valid numerical data "
                f"for {case_name}."
            )


        results.append(
            {
                "Case":
                    case_name,

                "Mean":
                    values.mean(),

                "Minimum":
                    values.min(),

                "Maximum":
                    values.max(),

                "Standard_Deviation":
                    values.std(
                        ddof=1
                    )
                    if len(values) > 1
                    else np.nan
            }
        )


    return pd.DataFrame(
        results
    )


# ============================================================
# 61. USE SUMMARY FUNCTION
# ============================================================

automatic_summary = summarize_cases(

    dataframe=time_data,

    case_columns=time_cases

)


print(
    "\n--- Automatic Case Summary ---"
)


print(
    automatic_summary
)


# ============================================================
# 62. REUSABLE COMPARISON PLOT FUNCTION
# ============================================================

def plot_engineering_comparison(
    dataframe,
    x_column,
    case_columns,
    x_label,
    y_label,
    title=None,
    x_scale="linear"
):
    """
    Plot multiple engineering cases consistently.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Input dataset.

    x_column : str
        X-axis column.

    case_columns : dict
        Mapping:
        display label -> Y column

    x_label : str
        X-axis label.

    y_label : str
        Y-axis label.

    title : str, optional
        Figure title.

    x_scale : str
        "linear" or "log"

    Returns
    -------
    fig, ax
        Matplotlib objects.
    """

    if x_column not in dataframe.columns:

        raise KeyError(
            f"X column not found: "
            f"{x_column}"
        )


    if x_scale not in {
        "linear",
        "log"
    }:

        raise ValueError(
            "x_scale must be "
            "'linear' or 'log'."
        )


    fig, ax = plt.subplots(
        figsize=(8, 4.8)
    )


    styles = [
        "-",
        "--",
        "-.",
        ":"
    ]


    for index, (
        case_name,
        column_name
    ) in enumerate(
        case_columns.items()
    ):

        if column_name not in dataframe.columns:

            raise KeyError(
                f"Column not found: "
                f"{column_name}"
            )


        style = styles[
            index
            % len(
                styles
            )
        ]


        ax.plot(

            dataframe[
                x_column
            ],

            dataframe[
                column_name
            ],

            linestyle=style,

            linewidth=2,

            label=case_name

        )


    ax.set_xscale(
        x_scale
    )


    ax.set_xlabel(
        x_label
    )


    ax.set_ylabel(
        y_label
    )


    if title is not None:

        ax.set_title(
            title
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
# 63. USE COMPARISON FUNCTION
# ============================================================

fig, ax = plot_engineering_comparison(

    dataframe=time_data,

    x_column="Time_s",

    case_columns=time_cases,

    x_label="Time [s]",

    y_label="Voltage [V]",

    title="Automatic Engineering Comparison",

    x_scale="linear"

)


plt.show()


# ============================================================
# 64. USE FUNCTION FOR FREQUENCY DATA
# ============================================================

fig, ax = plot_engineering_comparison(

    dataframe=fft_data,

    x_column="Frequency_Hz",

    case_columns=frequency_cases,

    x_label="Frequency",

    y_label="Magnitude [dBµV]",

    title="Frequency-Domain Engineering Comparison",

    x_scale="log"

)


ax.set_xlim(
    10e3,
    30e6
)


ax.xaxis.set_major_formatter(
    FuncFormatter(
        format_frequency
    )
)


plt.show()


# ============================================================
# 65. REUSABLE dB REDUCTION FUNCTION
# ============================================================

def calculate_db_reduction(
    dataframe,
    reference_column,
    case_columns
):
    """
    Calculate dB-domain reduction relative to a reference.

    Reduction [dB]
    =
    Reference [dB]
    -
    Case [dB]

    Parameters
    ----------
    dataframe : pandas.DataFrame

    reference_column : str
        Reference dB column.

    case_columns : dict
        Mapping:
        case name -> dB column

    Returns
    -------
    reduction_data : pandas.DataFrame
    """

    if reference_column not in dataframe.columns:

        raise KeyError(
            f"Reference column not found: "
            f"{reference_column}"
        )


    reduction_data = pd.DataFrame(
        index=dataframe.index
    )


    for case_name, column_name in case_columns.items():

        if column_name not in dataframe.columns:

            raise KeyError(
                f"Column not found: "
                f"{column_name}"
            )


        reduction_data[
            case_name
        ] = (

            dataframe[
                reference_column
            ]

            - dataframe[
                column_name
            ]

        )


    return reduction_data


# ============================================================
# 66. USE dB REDUCTION FUNCTION
# ============================================================

comparison_frequency_cases = {

    "Case A":
        "Case_A_dBuV",

    "Case B":
        "Case_B_dBuV",

    "Case C":
        "Case_C_dBuV"

}


db_reduction_data = calculate_db_reduction(

    dataframe=fft_data,

    reference_column="Unshielded_dBuV",

    case_columns=comparison_frequency_cases

)


db_reduction_data.insert(

    0,

    "Frequency_Hz",

    fft_data[
        "Frequency_Hz"
    ].to_numpy()

)


print(
    "\n--- Reusable dB Reduction Result ---"
)


print(
    db_reduction_data.head()
)


# ============================================================
# 67. PLOT REUSABLE dB REDUCTION DATA
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for case_name in comparison_frequency_cases:

    ax.plot(

        db_reduction_data[
            "Frequency_Hz"
        ],

        db_reduction_data[
            case_name
        ],

        linewidth=2,

        label=case_name

    )


ax.axhline(
    y=0,
    linestyle="--"
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
    "Reduction [dB]"
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
# 68. FINAL COMPARISON FIGURE
# ============================================================

"""
The final figure combines:

Absolute spectrum

and

Reduction relative to baseline.


This provides both:

Original engineering result

and

Quantified improvement.
"""


fig, axes = plt.subplots(

    2,

    1,

    figsize=(9, 7),

    sharex=True

)


# ------------------------------------------------------------
# TOP: Absolute magnitude
# ------------------------------------------------------------

for case_name, column_name in frequency_cases.items():

    axes[0].plot(

        fft_data[
            "Frequency_Hz"
        ],

        fft_data[
            column_name
        ],

        linestyle=frequency_line_styles[
            case_name
        ],

        linewidth=1.8,

        label=case_name

    )


axes[0].set_ylabel(
    "Magnitude [dBµV]"
)


axes[0].legend(
    ncol=2
)


axes[0].grid(
    True,
    which="both"
)


# ------------------------------------------------------------
# BOTTOM: Reduction
# ------------------------------------------------------------

for case_name in comparison_frequency_cases:

    axes[1].plot(

        db_reduction_data[
            "Frequency_Hz"
        ],

        db_reduction_data[
            case_name
        ],

        linewidth=1.8,

        label=case_name

    )


axes[1].axhline(
    y=0,
    linestyle="--",
    linewidth=1
)


axes[1].set_xlabel(
    "Frequency"
)


axes[1].set_ylabel(
    "Reduction [dB]"
)


axes[1].legend(
    ncol=3
)


axes[1].grid(
    True,
    which="both"
)


# ------------------------------------------------------------
# Shared logarithmic frequency scale
# ------------------------------------------------------------

for ax in axes:

    ax.set_xscale(
        "log"
    )


    ax.set_xlim(
        10e3,
        30e6
    )


    ax.xaxis.set_major_locator(
        LogLocator(
            base=10
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


axes[1].xaxis.set_major_formatter(
    FuncFormatter(
        format_frequency
    )
)


plt.tight_layout()

plt.show()


# ============================================================
# 69. FINAL SELECTED-FREQUENCY SUMMARY FIGURE
# ============================================================

fig, axes = plt.subplots(

    2,

    1,

    figsize=(10, 7),

    sharex=True

)


# ------------------------------------------------------------
# Absolute dBµV
# ------------------------------------------------------------

for case_index, (
    case_name,
    column_name
) in enumerate(
    frequency_cases.items()
):

    offset = (

        (
            case_index

            - (
                len(
                    frequency_cases
                )
                - 1
            )
            / 2
        )

        * bar_width

    )


    axes[0].bar(

        x_positions
        + offset,

        selected_frequency_data[
            column_name
        ],

        width=bar_width,

        label=case_name

    )


axes[0].set_ylabel(
    "Magnitude [dBµV]"
)


axes[0].legend(
    ncol=2
)


axes[0].grid(
    True,
    axis="y"
)


# ------------------------------------------------------------
# Reduction dB
# ------------------------------------------------------------

for case_index, (
    case_name,
    column_name
) in enumerate(
    reduction_cases.items()
):

    offset = (

        (
            case_index

            - (
                len(
                    reduction_cases
                )
                - 1
            )
            / 2
        )

        * reduction_bar_width

    )


    axes[1].bar(

        x_positions
        + offset,

        selected_frequency_data[
            column_name
        ],

        width=reduction_bar_width,

        label=case_name

    )


axes[1].axhline(
    y=0,
    linestyle="--"
)


axes[1].set_ylabel(
    "Reduction [dB]"
)


axes[1].set_xlabel(
    "Frequency"
)


axes[1].legend(
    ncol=3
)


axes[1].grid(
    True,
    axis="y"
)


axes[1].set_xticks(
    x_positions
)


axes[1].set_xticklabels(
    frequency_labels,
    rotation=20
)


plt.tight_layout()

plt.show()


# ============================================================
# 70. SAVE FINAL FIGURE
# ============================================================

fig, axes = plt.subplots(

    2,

    1,

    figsize=(9, 7),

    sharex=True

)


for case_name, column_name in frequency_cases.items():

    axes[0].plot(

        fft_data[
            "Frequency_Hz"
        ],

        fft_data[
            column_name
        ],

        linestyle=frequency_line_styles[
            case_name
        ],

        linewidth=1.8,

        label=case_name

    )


axes[0].set_ylabel(
    "Magnitude [dBµV]"
)


axes[0].legend(
    ncol=2
)


axes[0].grid(
    True,
    which="both"
)


for case_name in comparison_frequency_cases:

    axes[1].plot(

        db_reduction_data[
            "Frequency_Hz"
        ],

        db_reduction_data[
            case_name
        ],

        linewidth=1.8,

        label=case_name

    )


axes[1].axhline(
    y=0,
    linestyle="--",
    linewidth=1
)


axes[1].set_xlabel(
    "Frequency"
)


axes[1].set_ylabel(
    "Reduction [dB]"
)


axes[1].legend(
    ncol=3
)


axes[1].grid(
    True,
    which="both"
)


for ax in axes:

    ax.set_xscale(
        "log"
    )


    ax.set_xlim(
        10e3,
        30e6
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


axes[1].xaxis.set_major_formatter(
    FuncFormatter(
        format_frequency
    )
)


plt.tight_layout()


# ============================================================
# 71. SAVE PNG
# ============================================================

png_file = (
    output_figure_folder
    / "engineering_comparison.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 72. SAVE PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "engineering_comparison.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 73. SAVE SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "engineering_comparison.svg"
)


fig.savefig(
    svg_file,
    bbox_inches="tight"
)


print(
    "\n--- Final Figures Saved ---"
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
# 74. SAVE PROCESSED COMPARISON DATA
# ============================================================

processed_time_file = (
    output_data_folder
    / "processed_time_comparison.csv"
)


time_data.to_csv(
    processed_time_file,
    index=False
)


processed_frequency_file = (
    output_data_folder
    / "processed_frequency_comparison.csv"
)


fft_data.to_csv(
    processed_frequency_file,
    index=False
)


print(
    "\n--- Processed Data Saved ---"
)


print(
    processed_time_file
)


print(
    processed_frequency_file
)


# ============================================================
# 75. RAW DATA VS PROCESSED DATA
# ============================================================

"""
A reproducible research workflow may preserve:

RAW DATA

multiple_cases.csv

fft_example.csv


and separately create:

PROCESSED DATA

processed_time_comparison.csv

processed_frequency_comparison.csv


This prevents accidental modification of the original
measurement or simulation data.
"""


# ============================================================
# 76. COMMON MISTAKE - NO REFERENCE DEFINITION
# ============================================================

"""
A statement such as:

"Design B improved by 15%"


is incomplete unless the reference is clear.

Always identify:

Compared with what?


Example:

"Design B reduced the measured value by 15% relative to
the baseline configuration."
"""


# ============================================================
# 77. COMMON MISTAKE - HIGHER ALWAYS MEANS BETTER
# ============================================================

"""
For:

Efficiency

higher may be better.


For:

Loss

Temperature

EMI

Error

THD


lower may be better.


Define the engineering objective before calculating
"improvement."
"""


# ============================================================
# 78. COMMON MISTAKE - PERCENTAGE REDUCTION OF dB
# ============================================================

"""
Do NOT calculate:

(reference_dB - case_dB)
------------------------
      reference_dB

× 100


and call this:

"percentage EMI reduction"


without a specific physical derivation.


For dB-domain comparison:

Reference = 100 dBµV

Case = 88 dBµV


directly report:

12 dB reduction.
"""


# ============================================================
# 79. COMMON MISTAKE - DIFFERENT OPERATING CONDITIONS
# ============================================================

"""
Example:

Case A:

400 V input
2 kW load


Case B:

300 V input
1 kW load


A direct performance comparison may be misleading unless
the different conditions are explicitly part of the
research question.
"""


# ============================================================
# 80. COMMON MISTAKE - DIFFERENT UNITS
# ============================================================

"""
Case A:

Voltage [V]


Case B:

Voltage [mV]


Numerical comparison is invalid until units are
standardized.
"""


# ============================================================
# 81. COMMON MISTAKE - DIFFERENT TIME GRIDS
# ============================================================

"""
If separate datasets have different:

Sampling frequencies

Time vectors

Trigger locations


sample-by-sample subtraction may be invalid.


The datasets may require:

Alignment

Interpolation

Resampling

before direct numerical comparison.
"""


# ============================================================
# 82. COMMON MISTAKE - DIFFERENT FREQUENCY GRIDS
# ============================================================

"""
Similarly:

Case A spectrum:

10 kHz
20 kHz
30 kHz
...


Case B spectrum:

10 kHz
15 kHz
20 kHz
...


should not be directly subtracted by row number.


First align the spectra to a common frequency grid.
"""


# ============================================================
# 83. COMMON MISTAKE - RANKING BY ONE PEAK
# ============================================================

"""
A design with the:

Largest maximum reduction


is not automatically the:

Best overall design.


It may perform poorly elsewhere.

Use multiple engineering metrics when appropriate.
"""


# ============================================================
# 84. COMMON MISTAKE - MEAN OF dB WITHOUT INTERPRETATION
# ============================================================

"""
A numerical mean of dB-domain differences can be useful as
a descriptive metric.

However, averaging logarithmic quantities requires careful
physical interpretation.

Do not automatically treat:

Mean dB

as equivalent to averaging the underlying linear
amplitudes or powers.
"""


# ============================================================
# 85. COMMON MISTAKE - NORMALIZATION HIDES PHYSICAL SCALE
# ============================================================

"""
Normalized plots can make curves easy to compare.

But:

1.0

does not tell the reader whether the original value was:

10 V

100 V

or

1000 V.


Use raw physical plots alongside normalized comparisons
when absolute magnitude matters.
"""


# ============================================================
# 86. COMMON MISTAKE - BAR CHART FOR CONTINUOUS SPECTRUM
# ============================================================

"""
For a continuous frequency spectrum:

Use:

Line plot


For selected frequencies:

Use:

Grouped bar plot


Do not replace an entire continuous spectrum with hundreds
of bars unless there is a specific reason.
"""


# ============================================================
# 87. COMMON MISTAKE - TOO MANY CASES
# ============================================================

"""
If there are:

20 designs


plotting all 20 curves may reduce readability.

Possible solutions:

- Select representative cases
- Rank first
- Use summary tables
- Split figures
- Use subplots
- Use heatmaps
"""


# ============================================================
# 88. COMMON MISTAKE - CLAIMING CAUSATION FROM COMPARISON
# ============================================================

"""
A comparison figure may show:

Design A has lower EMI than Design B.


The figure alone does not necessarily prove WHY.


Engineering explanation may require:

- Physical model
- Circuit analysis
- Parasitic analysis
- Field analysis
- Controlled experiments
- Statistical testing
"""


# ============================================================
# 89. COMMON MISTAKE - CHERRY-PICKING FREQUENCIES
# ============================================================

"""
Selected-frequency bars are useful for summarizing
important points.

However:

Selecting only frequencies where one design performs well
can create a biased presentation.


Selection should be based on:

- Standard frequencies
- Switching harmonics
- Resonances
- Regulatory bands
- Engineering relevance
- Predefined criteria
"""


# ============================================================
# 90. COMPARISON DECISION WORKFLOW
# ============================================================

"""
What Are You Comparing?
        ↓
Define Cases
        ↓
Define Reference
        ↓
Verify Same Units
        ↓
Verify Same Conditions
        ↓
Verify Same Data Grid
        ↓
Choose Engineering Metric
        ↓
Higher Better?
Lower Better?
Difference Only?
        ↓
Calculate Comparison
        ↓
Plot Absolute Values
        ↓
Plot Difference / Reduction
        ↓
Calculate Summary Metrics
        ↓
Check Local Degradation
        ↓
Check Overall Performance
        ↓
Interpret
"""


# ============================================================
# 91. TIME-DOMAIN COMPARISON WORKFLOW
# ============================================================

"""
Time-Domain Cases
        ↓
Check Sampling
        ↓
Check Time Alignment
        ↓
Plot Absolute Waveforms
        ↓
Select Reference
        ↓
Calculate Difference
        ↓
Calculate Relative Change if Appropriate
        ↓
Extract:
Mean
Maximum
Minimum
Final Value
        ↓
Compare Selected Operating Points
        ↓
Interpret
"""


# ============================================================
# 92. FREQUENCY-DOMAIN COMPARISON WORKFLOW
# ============================================================

"""
Frequency-Domain Cases
        ↓
Check Frequency Grid
        ↓
Check Units
        ↓
Select Reference
        ↓
Plot Absolute Spectra
        ↓
Logarithmic Frequency Axis
        ↓
Calculate dB Difference
        ↓
Identify:
Maximum Reduction
Minimum Reduction
Local Increases
Selected Frequencies
        ↓
Create Summary
        ↓
Interpret Broadband / Local Behavior
"""


# ============================================================
# 93. COMPLETE ENGINEERING WORKFLOW
# ============================================================

"""
Raw Simulation / Experimental Data
            ↓
Load Data
            ↓
Inspect Columns
            ↓
Clean Data
            ↓
Validate Units
            ↓
Validate Operating Conditions
            ↓
Define Reference
            ↓
Define Comparison Cases
            ↓
Plot Raw Comparison
            ↓
Calculate Differences
            ↓
Calculate Relevant Metrics
            ↓
Create Summary Table
            ↓
Create Selected-Point Comparison
            ↓
Create Difference Plot
            ↓
Check Improvements
            ↓
Check Degradations
            ↓
Engineering Interpretation
            ↓
Publication Figure
            ↓
Save Processed Data
            ↓
PNG / PDF / SVG
"""


# ============================================================
# 94. RESEARCH COMPARISON CHECKLIST
# ============================================================

"""
Before reporting that one design is better, check:

REFERENCE
------------------------------------------------------------

Is the baseline clearly defined?


OPERATING CONDITIONS
------------------------------------------------------------

Are conditions consistent?


UNITS
------------------------------------------------------------

Are units identical?


SAMPLING
------------------------------------------------------------

Are time/frequency grids compatible?


METRIC
------------------------------------------------------------

Is higher or lower actually better?


DIFFERENCE
------------------------------------------------------------

Is difference calculated correctly?


PERCENTAGE
------------------------------------------------------------

Is percentage change mathematically meaningful?


LOGARITHMIC DATA
------------------------------------------------------------

Are dB quantities handled correctly?


SUMMARY
------------------------------------------------------------

Are both best and worst regions considered?


FIGURE
------------------------------------------------------------

Are axis limits fair?


INTERPRETATION
------------------------------------------------------------

Does the conclusion follow from the data?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
ENGINEERING COMPARISON PLOTS


1. DEFINE CASES

cases = {

    "Baseline":
        "Baseline_V",

    "Design A":
        "Design_A_V",

    "Design B":
        "Design_B_V"

}


------------------------------------------------------------


2. DEFINE REFERENCE

reference = data[
    "Baseline_V"
]


------------------------------------------------------------


3. ABSOLUTE DIFFERENCE

difference = (

    new_case
    - reference

)


------------------------------------------------------------


4. RELATIVE CHANGE FOR LINEAR DATA

relative_change = (

    (
        new_case
        - reference
    )

    / reference

) * 100


Only when:

Reference != 0


and percentage change is physically meaningful.


------------------------------------------------------------


5. LOWER-IS-BETTER REDUCTION

reduction = (

    (
        reference
        - new_case
    )

    / reference

) * 100


Useful for LINEAR metrics such as certain:

Losses

Errors

Temperatures


when the definition is physically appropriate.


------------------------------------------------------------


6. HIGHER-IS-BETTER IMPROVEMENT

improvement = (

    (
        new_case
        - reference
    )

    / reference

) * 100


Example:

Efficiency improvement


when scientifically appropriate.


------------------------------------------------------------


7. dB COMPARISON

For dB-domain attenuation:

reduction_dB = (

    reference_dB

    - case_dB

)


Example:

100 dBµV

to

88 dBµV

=

12 dB reduction


Do NOT automatically call this:

12% reduction.


------------------------------------------------------------


8. SUMMARY STATISTICS

Useful metrics include:

Mean

Minimum

Maximum

Standard deviation

Peak-to-peak

Final value


------------------------------------------------------------


9. RANKING

Higher-is-better:

sort_values(
    ascending=False
)


Lower-is-better:

sort_values(
    ascending=True
)


------------------------------------------------------------


10. SELECTED OPERATING POINTS

Use selected points when they have:

Engineering significance

Standardized meaning

or

Defined comparison value.


------------------------------------------------------------


11. GROUPED BAR PLOT

Useful for:

Several cases

at:

Selected operating points


------------------------------------------------------------


12. CONTINUOUS DATA

Use:

Line plots


for:

Time-domain waveforms

Frequency spectra


------------------------------------------------------------


13. NORMALIZATION

Useful for comparing:

Curve shapes

Relative trends


but normalization removes the direct physical scale.


------------------------------------------------------------


14. FREQUENCY-DOMAIN COMPARISON

Frequency [Hz]
        ↓
Logarithmic X-axis


Magnitude [dBµV]
        ↓
Linear numerical Y-axis


------------------------------------------------------------


15. dB REDUCTION SIGN

Positive:

Reduction / improvement


Negative:

Local increase relative to baseline


------------------------------------------------------------


16. CHECK THE WORST REGION

Do not report only:

Maximum improvement.


Also check:

Minimum improvement

Local degradation

Frequency coverage

Operating-condition dependence


------------------------------------------------------------


17. SELECTED FREQUENCIES

Useful for:

Grouped bars

Summary tables

Key harmonics

Resonances

Standard comparison points


but selected points should not be cherry-picked.


------------------------------------------------------------


18. MULTI-METRIC ANALYSIS

A single engineering metric rarely describes every
tradeoff.

Consider:

Performance

Efficiency

Loss

Thermal behavior

EMI

Cost

Complexity

Reliability


when relevant.


------------------------------------------------------------


19. FAIR AXES

Use consistent axis limits when comparing similar
quantities.

Do not manipulate scales to exaggerate improvements.


------------------------------------------------------------


20. SAVE PROCESSED DATA

Keep:

Raw Data

separate from:

Processed Comparison Data


for reproducibility.


------------------------------------------------------------


21. PUBLICATION OUTPUT

Useful combination:

Absolute Result
        +
Difference / Reduction
        +
Summary Metrics


------------------------------------------------------------


22. MOST IMPORTANT PRINCIPLE

A good engineering comparison does not only answer:

"Which curve looks better?"


It should answer:

What changed?

By how much?

Compared with what?

Under which conditions?

Where did it improve?

Where did it become worse?

Is the difference physically meaningful?


------------------------------------------------------------


23. COMPLETE WORKFLOW

Baseline
    +
Alternative Cases
        ↓
Validate Conditions
        ↓
Absolute Comparison
        ↓
Difference
        ↓
Relative Change / dB Reduction
        ↓
Summary Metrics
        ↓
Selected Operating Points
        ↓
Check Best Region
        ↓
Check Worst Region
        ↓
Engineering Interpretation
        ↓
Publication Figure
        ↓
Export


------------------------------------------------------------


CORE DATA VISUALIZATION SECTION COMPLETE


The main visualization sequence is now complete.

The next stage can add EXTRA / ADVANCED visualization
topics without disturbing the core learning sequence.
"""
