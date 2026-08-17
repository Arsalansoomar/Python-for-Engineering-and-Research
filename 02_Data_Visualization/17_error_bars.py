"""
============================================================
Python for Engineering and Research
17 - Error Bars
============================================================

Purpose:
    Demonstrate how uncertainty, variability, and repeated
    measurements can be represented using error bars in
    Matplotlib.

Topics:
    1. What are error bars?
    2. Why are error bars important?
    3. Standard deviation
    4. Standard error of the mean
    5. Confidence intervals
    6. Measurement uncertainty
    7. Basic y-error bars
    8. Basic x-error bars
    9. X and Y uncertainty together
    10. Repeated measurements
    11. Automatic mean and standard deviation
    12. Multiple experimental cases
    13. Error bars on bar plots
    14. Symmetric uncertainty
    15. Asymmetric uncertainty
    16. capsize and line formatting
    17. Percentage uncertainty
    18. Relative uncertainty
    19. Approximate confidence interval
    20. Reusable functions
    21. Saving figures
    22. Common mistakes
    23. Key takeaways

Important:
    Standard deviation, standard error, confidence interval,
    and measurement uncertainty do NOT mean the same thing.

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT ARE ERROR BARS?
# ============================================================

"""
An error bar displays uncertainty or variability around
a plotted value.

Example:

        |
      --●--
        |
        |
        ↑
     Measured
      Value


The central point may represent:

Mean

Measured value

Predicted value

Estimated parameter


The error bar may represent:

Standard deviation

Standard error

Confidence interval

Measurement uncertainty

Tolerance

Repeatability range


Therefore an error bar does NOT have one universal meaning.
"""


# ============================================================
# 2. WHY ARE ERROR BARS IMPORTANT?
# ============================================================

"""
Suppose two converter designs have measured efficiencies:

Design A:

95.0%


Design B:

95.4%


Without uncertainty, Design B appears better.


But suppose repeated measurements show:

Design A:

95.0 ± 0.1%


Design B:

95.4 ± 0.8%


The interpretation becomes more complicated.


Therefore research figures should communicate both:

Central Result
      +
Variability / Uncertainty
"""


# ============================================================
# 3. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path


# ============================================================
# 4. BASIC ERROR-BAR SYNTAX
# ============================================================

"""
Matplotlib provides:

ax.errorbar()


Basic syntax:

ax.errorbar(
    x,
    y,
    yerr=error
)


where:

x
    X-axis values

y
    Central Y values

yerr
    Y-axis uncertainty
"""


# ============================================================
# 5. SIMPLE ENGINEERING EXAMPLE
# ============================================================

load_percent = np.array(
    [
        20,
        40,
        60,
        80,
        100
    ],
    dtype=float
)


efficiency = np.array(
    [
        92.1,
        94.0,
        95.1,
        95.6,
        95.2
    ]
)


efficiency_error = np.array(
    [
        0.20,
        0.18,
        0.15,
        0.22,
        0.30
    ]
)


# ============================================================
# 6. BASIC Y-ERROR BARS
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    load_percent,
    efficiency,
    yerr=efficiency_error,
    marker="o",
    linewidth=2,
    capsize=5
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Converter Efficiency with Error Bars"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 7. WHAT DOES yerr REPRESENT?
# ============================================================

"""
The previous code only tells Matplotlib:

Draw an error bar.


It does NOT tell the reader whether:

efficiency_error

represents:

Standard deviation

Standard error

Confidence interval

Instrument uncertainty


That meaning must be defined by the researcher.


Example figure caption:

"Error bars represent ±1 standard deviation from five
repeated measurements."


This is scientifically much clearer than simply writing:

"Error bars are shown."
"""


# ============================================================
# 8. CONSTANT ERROR FOR ALL POINTS
# ============================================================

"""
A scalar can be used when every point has the same
uncertainty.

Example:

±0.2%
"""


constant_error = 0.2


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    load_percent,
    efficiency,
    yerr=constant_error,
    marker="o",
    capsize=5
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Constant Y-Uncertainty"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 9. DIFFERENT ERROR FOR EACH POINT
# ============================================================

"""
More commonly, uncertainty may vary between operating
points.

Example:

20% load:
±0.20%

40% load:
±0.18%

60% load:
±0.15%

...
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    load_percent,
    efficiency,
    yerr=efficiency_error,
    fmt="o-",
    capsize=5
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
# 10. WHAT IS fmt?
# ============================================================

"""
fmt controls the basic marker and line style.

Examples:

fmt="o"

    Points only


fmt="o-"

    Circular markers + solid line


fmt="s--"

    Square markers + dashed line


fmt="none"

    Error bars without a connecting data marker/line
"""


# ============================================================
# 11. ERROR-BAR APPEARANCE
# ============================================================

"""
Useful parameters:

capsize

    Length of end caps


elinewidth

    Width of error-bar lines


capthick

    Thickness of error-bar caps


markersize

    Data marker size


linewidth

    Main curve line width
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    load_percent,
    efficiency,
    yerr=efficiency_error,
    fmt="o-",
    capsize=6,
    capthick=1.5,
    elinewidth=1.2,
    markersize=6,
    linewidth=2
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
# 12. X-ERROR BARS
# ============================================================

"""
Uncertainty may also exist in the X variable.

Examples:

Frequency uncertainty

Load uncertainty

Temperature uncertainty

Time uncertainty


Use:

xerr=
"""


temperature = np.array(
    [
        30,
        40,
        50,
        60,
        70
    ],
    dtype=float
)


power_loss = np.array(
    [
        8.2,
        10.5,
        13.8,
        17.6,
        22.1
    ]
)


temperature_uncertainty = np.array(
    [
        0.5,
        0.5,
        0.6,
        0.6,
        0.7
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    temperature,
    power_loss,
    xerr=temperature_uncertainty,
    fmt="o",
    capsize=5
)


ax.set_xlabel(
    "Temperature [°C]"
)

ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Temperature Uncertainty"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 13. X AND Y ERROR BARS TOGETHER
# ============================================================

power_loss_uncertainty = np.array(
    [
        0.3,
        0.4,
        0.5,
        0.6,
        0.8
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    temperature,
    power_loss,
    xerr=temperature_uncertainty,
    yerr=power_loss_uncertainty,
    fmt="o",
    capsize=5
)


ax.set_xlabel(
    "Temperature [°C]"
)

ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "X and Y Measurement Uncertainty"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 14. REPEATED MEASUREMENTS
# ============================================================

"""
A common research workflow is:

Operating Point
      ↓
Repeat Measurement Several Times
      ↓
Calculate Mean
      ↓
Calculate Variability
      ↓
Plot Mean + Error Bar


Example:

Five repeated efficiency measurements are taken at each
load condition.
"""


efficiency_measurements = np.array(
    [
        # Run 1
        [
            92.0,
            93.9,
            95.0,
            95.5,
            95.1
        ],

        # Run 2
        [
            92.2,
            94.1,
            95.2,
            95.7,
            95.4
        ],

        # Run 3
        [
            91.9,
            94.0,
            95.1,
            95.6,
            95.0
        ],

        # Run 4
        [
            92.3,
            94.2,
            95.0,
            95.8,
            95.3
        ],

        # Run 5
        [
            92.1,
            93.8,
            95.3,
            95.5,
            95.2
        ]
    ]
)


# ============================================================
# 15. CHECK ARRAY SHAPE
# ============================================================

"""
Structure:

Rows:
Repeated experiments

Columns:
Operating points
"""


print(
    "\n--- Repeated Measurement Shape ---"
)


print(
    efficiency_measurements.shape
)


print(
    "Number of Runs:",
    efficiency_measurements.shape[0]
)


print(
    "Number of Load Points:",
    efficiency_measurements.shape[1]
)


# ============================================================
# 16. CALCULATE MEAN
# ============================================================

"""
Mean across repeated experiments:

axis=0

means:

Calculate one mean for each load condition.
"""


mean_efficiency = np.mean(
    efficiency_measurements,
    axis=0
)


print(
    "\n--- Mean Efficiency ---"
)


print(
    mean_efficiency
)


# ============================================================
# 17. STANDARD DEVIATION
# ============================================================

"""
Sample standard deviation:

np.std(
    data,
    axis=0,
    ddof=1
)


ddof=1 is commonly used when estimating sample standard
deviation from repeated measurements.
"""


std_efficiency = np.std(
    efficiency_measurements,
    axis=0,
    ddof=1
)


print(
    "\n--- Standard Deviation ---"
)


print(
    std_efficiency
)


# ============================================================
# 18. PLOT MEAN ± STANDARD DEVIATION
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    load_percent,
    mean_efficiency,
    yerr=std_efficiency,
    fmt="o-",
    capsize=5,
    linewidth=2
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Mean Efficiency ± 1 Standard Deviation"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 19. WHAT IS STANDARD DEVIATION?
# ============================================================

"""
Standard deviation describes the spread of observations
around their mean.

Conceptually:

Small standard deviation
        ↓
Repeated measurements are tightly grouped


Large standard deviation
        ↓
Repeated measurements are more dispersed


Standard deviation primarily describes:

DATA VARIABILITY


It does not directly describe the uncertainty in the
estimated mean.
"""


# ============================================================
# 20. STANDARD ERROR OF THE MEAN
# ============================================================

"""
Standard Error of the Mean:

             SD
SEM = ----------------
          sqrt(n)


where:

SD
    Sample standard deviation

n
    Number of repeated observations


SEM estimates the statistical uncertainty associated with
the sample mean.
"""


number_of_measurements = (
    efficiency_measurements.shape[0]
)


sem_efficiency = (

    std_efficiency

    / np.sqrt(
        number_of_measurements
    )

)


print(
    "\n--- Standard Error ---"
)


print(
    sem_efficiency
)


# ============================================================
# 21. PLOT MEAN ± STANDARD ERROR
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    load_percent,
    mean_efficiency,
    yerr=sem_efficiency,
    fmt="o-",
    capsize=5
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Mean Efficiency ± Standard Error"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 22. STANDARD DEVIATION VS STANDARD ERROR
# ============================================================

"""
STANDARD DEVIATION

Describes:

Spread / variability of individual observations


Formula concept:

How widely measurements vary around the mean


------------------------------------------------------------


STANDARD ERROR

Describes:

Statistical uncertainty in the estimated mean


Formula:

SEM = SD / sqrt(n)


------------------------------------------------------------


They answer DIFFERENT questions.

Do not choose SEM simply because it produces smaller
error bars.
"""


# ============================================================
# 23. APPROXIMATE 95% CONFIDENCE INTERVAL
# ============================================================

"""
For sufficiently large samples under suitable statistical
assumptions, a commonly used approximate 95% confidence
interval for the mean is:

Mean ± 1.96 × SEM


IMPORTANT:

This is a normal-approximation example.

For small samples, the Student's t-distribution is generally
more appropriate.

That calculation can later be performed using SciPy.
"""


approximate_ci_95 = (

    1.96

    * sem_efficiency

)


print(
    "\n--- Approximate 95% CI Half-Width ---"
)


print(
    approximate_ci_95
)


# ============================================================
# 24. PLOT APPROXIMATE 95% CI
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    load_percent,
    mean_efficiency,
    yerr=approximate_ci_95,
    fmt="o-",
    capsize=5
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Mean Efficiency with Approximate 95% CI"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 25. IMPORTANT CONFIDENCE-INTERVAL NOTE
# ============================================================

"""
Do not automatically use:

1.96 × SEM

for every experiment.

Confidence intervals depend on:

- Sample size
- Statistical distribution
- Independence assumptions
- Estimation method
- Required confidence level


For small repeated-measurement datasets, a Student's
t-based confidence interval is commonly more appropriate.


Later:

SciPy

can calculate appropriate critical values.
"""


# ============================================================
# 26. MEASUREMENT UNCERTAINTY
# ============================================================

"""
Measurement uncertainty is conceptually different from
standard deviation and standard error.

Example:

Voltage measurement:

100.0 V ± 0.5 V


The ±0.5 V may come from:

Instrument accuracy

Calibration

Probe accuracy

Resolution

Repeatability

Environmental effects

Uncertainty propagation


Measurement uncertainty should be based on the actual
measurement methodology.

It should NOT automatically be replaced by:

Standard deviation

or:

Standard error.
"""


# ============================================================
# 27. SIMPLE INSTRUMENT-UNCERTAINTY EXAMPLE
# ============================================================

measured_voltage = np.array(
    [
        48.0,
        72.0,
        96.0,
        120.0
    ]
)


voltage_uncertainty = np.array(
    [
        0.3,
        0.4,
        0.5,
        0.6
    ]
)


operating_point = np.array(
    [
        1,
        2,
        3,
        4
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    operating_point,
    measured_voltage,
    yerr=voltage_uncertainty,
    fmt="o",
    capsize=5
)


ax.set_xlabel(
    "Operating Point"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Measured Voltage with Instrument Uncertainty"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 28. SYMMETRIC ERROR BARS
# ============================================================

"""
Most examples so far use symmetric error bars.

Example:

95.0 ± 0.5


Lower:

94.5


Upper:

95.5


Matplotlib accepts:

yerr=0.5

or an array:

yerr=[
    0.2,
    0.3,
    0.4
]
"""


# ============================================================
# 29. ASYMMETRIC ERROR BARS
# ============================================================

"""
Sometimes uncertainty is not symmetric.

Example:

Measured value:

95.0


Lower uncertainty:

-0.3


Upper uncertainty:

+0.7


Matplotlib supports asymmetric errors.

For N points:

yerr must contain:

[
    lower_errors,
    upper_errors
]


Shape:

2 × N
"""


asymmetric_mean = np.array(
    [
        92.0,
        94.0,
        95.2,
        95.6,
        95.3
    ]
)


lower_error = np.array(
    [
        0.2,
        0.3,
        0.2,
        0.4,
        0.3
    ]
)


upper_error = np.array(
    [
        0.4,
        0.5,
        0.3,
        0.6,
        0.5
    ]
)


asymmetric_error = np.vstack(
    [
        lower_error,
        upper_error
    ]
)


print(
    "\n--- Asymmetric Error Shape ---"
)


print(
    asymmetric_error.shape
)


# ============================================================
# 30. PLOT ASYMMETRIC ERROR BARS
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    load_percent,
    asymmetric_mean,
    yerr=asymmetric_error,
    fmt="o-",
    capsize=5
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Asymmetric Error Bars"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 31. ERROR BARS ON BAR PLOTS
# ============================================================

"""
Bar plots can also display uncertainty.

Use:

yerr=
"""


design_names = [

    "Baseline",

    "Design A",

    "Design B"

]


mean_loss = np.array(
    [
        18.2,
        15.4,
        13.8
    ]
)


std_loss = np.array(
    [
        1.1,
        0.8,
        0.6
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(
    design_names,
    mean_loss,
    yerr=std_loss,
    capsize=5
)


ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Power Loss with Standard Deviation"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 32. BAR LABELS WITH ERROR BARS
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(
    design_names,
    mean_loss,
    yerr=std_loss,
    capsize=5
)


ax.bar_label(
    bars,
    fmt="%.1f",
    padding=5
)


ax.set_ylabel(
    "Power Loss [W]"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 33. MULTIPLE CASES WITH ERROR BARS
# ============================================================

"""
Suppose two converter designs were repeatedly tested at
the same loads.
"""


design_a_mean = np.array(
    [
        91.5,
        93.6,
        94.8,
        95.2,
        94.9
    ]
)


design_a_std = np.array(
    [
        0.3,
        0.2,
        0.2,
        0.3,
        0.4
    ]
)


design_b_mean = np.array(
    [
        92.2,
        94.2,
        95.3,
        95.8,
        95.4
    ]
)


design_b_std = np.array(
    [
        0.2,
        0.2,
        0.15,
        0.2,
        0.25
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    load_percent,
    design_a_mean,
    yerr=design_a_std,
    fmt="o-",
    capsize=5,
    label="Design A"
)


ax.errorbar(
    load_percent,
    design_b_mean,
    yerr=design_b_std,
    fmt="s--",
    capsize=5,
    label="Design B"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Design Comparison with Variability"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 34. GROUPED BAR PLOT WITH ERROR BARS
# ============================================================

"""
Grouped bars can also include uncertainty.
"""


load_categories = [

    "25%",

    "50%",

    "75%",

    "100%"

]


baseline_mean = np.array(
    [
        91.0,
        93.2,
        94.1,
        93.8
    ]
)


baseline_std = np.array(
    [
        0.4,
        0.3,
        0.35,
        0.5
    ]
)


optimized_mean = np.array(
    [
        92.0,
        94.4,
        95.3,
        95.0
    ]
)


optimized_std = np.array(
    [
        0.3,
        0.2,
        0.25,
        0.3
    ]
)


x_positions = np.arange(
    len(
        load_categories
    )
)


bar_width = 0.35


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.bar(
    x_positions
    - bar_width / 2,
    baseline_mean,
    width=bar_width,
    yerr=baseline_std,
    capsize=4,
    label="Baseline"
)


ax.bar(
    x_positions
    + bar_width / 2,
    optimized_mean,
    width=bar_width,
    yerr=optimized_std,
    capsize=4,
    label="Optimized"
)


ax.set_xticks(
    x_positions
)


ax.set_xticklabels(
    load_categories
)


ax.set_xlabel(
    "Load"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Grouped Comparison with Standard Deviation"
)


ax.legend()


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 35. PERCENTAGE UNCERTAINTY
# ============================================================

"""
Absolute uncertainty:

Measured:

100 V ± 2 V


Absolute uncertainty:

2 V


Relative uncertainty:

2 / 100 = 0.02


Percentage uncertainty:

2%
"""


measured_value = 100.0

absolute_uncertainty = 2.0


relative_uncertainty = (

    absolute_uncertainty

    / measured_value

)


percentage_uncertainty = (

    relative_uncertainty

    * 100

)


print(
    "\n--- Uncertainty Example ---"
)


print(
    f"Measured Value = "
    f"{measured_value:.1f} V"
)


print(
    f"Absolute Uncertainty = "
    f"{absolute_uncertainty:.1f} V"
)


print(
    f"Relative Uncertainty = "
    f"{relative_uncertainty:.4f}"
)


print(
    f"Percentage Uncertainty = "
    f"{percentage_uncertainty:.2f}%"
)


# ============================================================
# 36. CALCULATE PERCENTAGE UNCERTAINTY FOR ARRAY
# ============================================================

voltage_values = np.array(
    [
        48,
        72,
        96,
        120
    ],
    dtype=float
)


voltage_errors = np.array(
    [
        0.3,
        0.4,
        0.5,
        0.6
    ]
)


percentage_errors = (

    voltage_errors

    / voltage_values

) * 100


print(
    "\n--- Voltage Percentage Uncertainty ---"
)


print(
    percentage_errors
)


# ============================================================
# 37. IMPORTANT: dB UNCERTAINTY
# ============================================================

"""
Be careful when working with logarithmic quantities such as:

dB

dBµV

dBm


A simple percentage calculation directly on dB values is
generally not physically meaningful.

Example:

100 dBµV ± 2 dB


should not automatically be described as:

2% uncertainty.


Logarithmic quantities require interpretation according to
the underlying physical quantity and measurement method.
"""


# ============================================================
# 38. ERROR BAR VS SHADED UNCERTAINTY REGION
# ============================================================

"""
For dense line data, hundreds or thousands of error bars
may make a figure difficult to read.

An alternative is:

Mean Curve
    +
Shaded Uncertainty Region


using:

ax.fill_between()


This can be clearer for:

Time-series data

Frequency responses

Repeated simulations

Confidence bands
"""


x_dense = np.linspace(
    0,
    10,
    100
)


mean_signal = np.sin(
    x_dense
)


signal_std = (
    0.1
    +
    0.03
    * np.abs(
        np.sin(
            x_dense
        )
    )
)


lower_bound = (
    mean_signal
    - signal_std
)


upper_bound = (
    mean_signal
    + signal_std
)


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    x_dense,
    mean_signal,
    linewidth=2,
    label="Mean"
)


ax.fill_between(
    x_dense,
    lower_bound,
    upper_bound,
    alpha=0.25,
    label="±1 Standard Deviation"
)


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Amplitude [-]"
)

ax.set_title(
    "Mean with Shaded Variability Region"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 39. ERROR BARS VS SHADED REGION
# ============================================================

"""
ERROR BARS

Useful for:

Small number of discrete points

Load sweeps

Experimental operating points

Bar plots


------------------------------------------------------------


SHADED REGION

Useful for:

Many closely spaced points

Time-series signals

Frequency responses

Confidence bands

Repeated simulations


Choose the visualization that communicates uncertainty
clearly.
"""


# ============================================================
# 40. REUSABLE STATISTICS FUNCTION
# ============================================================

def calculate_statistics(
    repeated_measurements
):
    """
    Calculate mean, sample standard deviation, and
    standard error across repeated measurements.

    Parameters
    ----------
    repeated_measurements : array-like
        Rows represent repeated measurements and columns
        represent operating conditions.

    Returns
    -------
    mean_values : numpy.ndarray
        Mean for each operating condition.

    standard_deviation : numpy.ndarray
        Sample standard deviation.

    standard_error : numpy.ndarray
        Standard error of the mean.
    """

    data = np.asarray(
        repeated_measurements,
        dtype=float
    )


    if data.ndim != 2:

        raise ValueError(
            "Repeated measurement data must be a "
            "two-dimensional array."
        )


    number_of_runs = (
        data.shape[0]
    )


    if number_of_runs < 2:

        raise ValueError(
            "At least two repeated measurements are "
            "required to calculate sample standard "
            "deviation."
        )


    mean_values = np.mean(
        data,
        axis=0
    )


    standard_deviation = np.std(
        data,
        axis=0,
        ddof=1
    )


    standard_error = (

        standard_deviation

        / np.sqrt(
            number_of_runs
        )

    )


    return (
        mean_values,
        standard_deviation,
        standard_error
    )


# ============================================================
# 41. USE STATISTICS FUNCTION
# ============================================================

(
    calculated_mean,
    calculated_std,
    calculated_sem
) = calculate_statistics(
    efficiency_measurements
)


print(
    "\n--- Statistics Function Results ---"
)


print(
    "Mean:"
)


print(
    calculated_mean
)


print(
    "\nStandard Deviation:"
)


print(
    calculated_std
)


print(
    "\nStandard Error:"
)


print(
    calculated_sem
)


# ============================================================
# 42. REUSABLE ERROR-BAR PLOT FUNCTION
# ============================================================

def plot_with_error_bars(
    x,
    y,
    y_error,
    x_label,
    y_label,
    title,
    legend_label=None
):
    """
    Create a line plot with symmetric Y-error bars.

    Parameters
    ----------
    x : array-like
        X-axis values.

    y : array-like
        Central Y values.

    y_error : array-like or float
        Y-axis error magnitude.

    x_label : str
        X-axis label.

    y_label : str
        Y-axis label.

    title : str
        Figure title.

    legend_label : str, optional
        Legend label.

    Returns
    -------
    fig, ax
        Matplotlib figure and axis.
    """

    x = np.asarray(
        x
    )


    y = np.asarray(
        y
    )


    if len(x) != len(y):

        raise ValueError(
            "X and Y must have the same number "
            "of observations."
        )


    fig, ax = plt.subplots(
        figsize=(7, 4.5)
    )


    ax.errorbar(
        x,
        y,
        yerr=y_error,
        fmt="o-",
        capsize=5,
        linewidth=2,
        label=legend_label
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


    if legend_label is not None:

        ax.legend()


    plt.tight_layout()


    return (
        fig,
        ax
    )


# ============================================================
# 43. USE REUSABLE ERROR-BAR FUNCTION
# ============================================================

fig, ax = plot_with_error_bars(

    x=load_percent,

    y=mean_efficiency,

    y_error=std_efficiency,

    x_label="Load [%]",

    y_label="Efficiency [%]",

    title="Repeated Converter Measurements",

    legend_label="Mean ± 1 SD"

)


plt.show()


# ============================================================
# 44. REUSABLE MEAN + SD WORKFLOW
# ============================================================

def plot_repeated_measurements(
    x,
    repeated_measurements,
    x_label,
    y_label,
    title
):
    """
    Calculate mean and sample standard deviation from
    repeated experiments and plot mean ± 1 SD.
    """

    (
        mean_values,
        standard_deviation,
        standard_error
    ) = calculate_statistics(
        repeated_measurements
    )


    fig, ax = plt.subplots(
        figsize=(7, 4.5)
    )


    ax.errorbar(
        x,
        mean_values,
        yerr=standard_deviation,
        fmt="o-",
        capsize=5,
        linewidth=2,
        label="Mean ± 1 SD"
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


    ax.legend()


    ax.grid(
        True
    )


    plt.tight_layout()


    return (
        fig,
        ax,
        mean_values,
        standard_deviation,
        standard_error
    )


# ============================================================
# 45. USE COMPLETE WORKFLOW
# ============================================================

(
    fig,
    ax,
    result_mean,
    result_std,
    result_sem
) = plot_repeated_measurements(

    x=load_percent,

    repeated_measurements=efficiency_measurements,

    x_label="Load [%]",

    y_label="Efficiency [%]",

    title="Repeated Efficiency Measurements"

)


plt.show()


# ============================================================
# 46. ERROR-BAR CAPTION EXAMPLES
# ============================================================

"""
GOOD:

"Values represent mean ± 1 standard deviation from five
independent measurements."


GOOD:

"Error bars indicate the 95% confidence interval of the
estimated mean."


GOOD:

"Error bars represent expanded measurement uncertainty."


LESS INFORMATIVE:

"Error bars are included."


The reader should know exactly what the bars represent.
"""


# ============================================================
# 47. ERROR BARS AND OVERLAP
# ============================================================

"""
Suppose:

Design A:

95.0 ± 0.5


Design B:

95.3 ± 0.5


The error bars overlap.


This does NOT automatically prove:

"There is no statistically significant difference."


Likewise, non-overlapping error bars do not universally
provide a formal statistical significance test.


Statistical significance depends on:

- What the error bars represent
- Sample sizes
- Statistical assumptions
- Experimental design
- Appropriate hypothesis test


Formal statistical testing should be performed separately.
"""


# ============================================================
# 48. MISSING VALUES IN REPEATED MEASUREMENTS
# ============================================================

"""
Real experiments may contain:

NaN


If missing measurements are scientifically justified and
properly documented, NumPy provides functions such as:

np.nanmean()

np.nanstd()


Example:

mean = np.nanmean(
    data,
    axis=0
)


However:

Do not silently ignore missing research measurements.

Investigate and document why the value is missing.
"""


# ============================================================
# 49. SAVE FINAL FIGURE
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


output_figure_folder = (
    script_folder
    / "output_figures"
)


output_figure_folder.mkdir(
    exist_ok=True
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.errorbar(
    load_percent,
    mean_efficiency,
    yerr=std_efficiency,
    fmt="o-",
    capsize=5,
    capthick=1.3,
    elinewidth=1.2,
    linewidth=2,
    label="Mean ± 1 SD"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Converter Efficiency with Experimental Variability"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()


# ============================================================
# 50. SAVE PNG
# ============================================================

png_file = (
    output_figure_folder
    / "error_bars.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 51. SAVE PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "error_bars.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 52. SAVE SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "error_bars.svg"
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
# 53. COMMON MISTAKE - NOT DEFINING THE ERROR BAR
# ============================================================

"""
A figure showing:

Value ± Error


is incomplete if the reader does not know whether Error
means:

Standard deviation

Standard error

Confidence interval

Measurement uncertainty


Always define the meaning.
"""


# ============================================================
# 54. COMMON MISTAKE - SD AND SEM USED INTERCHANGEABLY
# ============================================================

"""
Standard deviation and standard error are different.

SD:

Describes spread of measurements.


SEM:

Describes statistical uncertainty of the mean.


SEM is usually smaller than SD because:

SEM = SD / sqrt(n)


Do not choose SEM merely because it produces visually
smaller error bars.
"""


# ============================================================
# 55. COMMON MISTAKE - ±1 SD CALLED 95% CI
# ============================================================

"""
Mean ± 1 standard deviation

is NOT automatically the same as:

95% confidence interval.


These quantities answer different statistical questions.
"""


# ============================================================
# 56. COMMON MISTAKE - ±SEM CALLED MEASUREMENT UNCERTAINTY
# ============================================================

"""
Standard error does not automatically represent the full
measurement uncertainty.

Measurement uncertainty can include:

Calibration uncertainty

Instrument accuracy

Resolution

Repeatability

Environmental effects

Probe uncertainty

Data-processing uncertainty

Other systematic and random contributions
"""


# ============================================================
# 57. COMMON MISTAKE - 1.96 × SEM FOR SMALL SAMPLE
# ============================================================

"""
For small sample sizes:

Mean ± 1.96 × SEM


may not be the appropriate confidence interval.

A Student's t critical value is commonly used instead.

SciPy will later be useful for this calculation.
"""


# ============================================================
# 58. COMMON MISTAKE - TOO MANY ERROR BARS
# ============================================================

"""
Imagine:

10,000 frequency samples

each with one vertical error bar.


The plot may become unreadable.


Consider:

Mean curve
+
Shaded uncertainty region


using:

ax.fill_between()
"""


# ============================================================
# 59. COMMON MISTAKE - ERROR BARS HIDDEN BY AXIS LIMIT
# ============================================================

"""
Suppose:

Mean = 95

Error = ±5


but:

ax.set_ylim(
    92,
    98
)


part of the uncertainty range is hidden.

Axis limits should include relevant error ranges unless
intentional clipping is clearly justified.
"""


# ============================================================
# 60. COMMON MISTAKE - NEGATIVE PHYSICAL VALUES
# ============================================================

"""
Suppose:

Current = 0.2 A

Uncertainty = ±0.5 A


The lower error bar reaches:

-0.3 A


Matplotlib can display this numerically, but the researcher
should consider whether:

- Negative current is physically possible
- The uncertainty model is appropriate
- The measurement is near the detection limit
"""


# ============================================================
# 61. COMMON MISTAKE - ERROR BARS FROM ONE MEASUREMENT
# ============================================================

"""
Standard deviation cannot be estimated from one
measurement alone.

Repeated observations are required to estimate
repeatability statistically.

However, instrument uncertainty may still be available
from:

Calibration

Manufacturer specification

Measurement model


Do not invent standard deviation when repeated data do
not exist.
"""


# ============================================================
# 62. COMMON MISTAKE - USING POPULATION SD FOR SAMPLE DATA
# ============================================================

"""
NumPy default:

np.std(
    data
)


uses:

ddof=0


For sample standard deviation from repeated experimental
measurements, researchers commonly use:

np.std(
    data,
    ddof=1
)


The correct choice depends on the statistical context.
"""


# ============================================================
# 63. COMMON MISTAKE - INTERPRETING OVERLAP AS A TEST
# ============================================================

"""
Error-bar overlap is a visualization.

It is NOT automatically a statistical hypothesis test.

Use appropriate statistical methods when claiming:

Significant difference

No significant difference

Confidence in superiority

Model equivalence
"""


# ============================================================
# 64. COMMON MISTAKE - ERROR BAR WITHOUT SAMPLE SIZE
# ============================================================

"""
When reporting variability from repeated measurements,
sample size is often useful.

Example:

Mean ± SD, n = 5


The same standard deviation estimated from:

n = 3

and:

n = 100

does not imply the same confidence in the estimated mean.
"""


# ============================================================
# 65. ERROR-BAR DECISION WORKFLOW
# ============================================================

"""
What Does the Central Point Represent?
          ↓
Mean / Measurement / Estimate
          ↓
Why Is There an Error Bar?
          ↓
Variability?
Measurement uncertainty?
Mean uncertainty?
Confidence interval?
          ↓
Choose Correct Quantity
          ↓
Calculate Correctly
          ↓
Plot with:
yerr / xerr
          ↓
State Meaning Explicitly
          ↓
Check Axis Range
          ↓
Check Readability
          ↓
Interpret Carefully
"""


# ============================================================
# 66. REPEATED EXPERIMENT WORKFLOW
# ============================================================

"""
Experiment
    ↓
Operating Point 1
    ↓
Repeat Measurement n Times
    ↓
Operating Point 2
    ↓
Repeat Measurement n Times
    ↓
...
    ↓
Create Measurement Matrix
    ↓
Calculate Mean
    ↓
Calculate SD
    ↓
Calculate SEM if Required
    ↓
Calculate CI if Required
    ↓
Choose Appropriate Error Representation
    ↓
Plot
    ↓
State:
"Error bars represent ..."
"""


# ============================================================
# 67. ENGINEERING EXAMPLES
# ============================================================

"""
EXAMPLE 1

Efficiency vs Load

Central value:

Mean efficiency

Error:

±1 standard deviation


------------------------------------------------------------


EXAMPLE 2

Voltage Measurement

Central value:

Measured voltage

Error:

Measurement uncertainty


------------------------------------------------------------


EXAMPLE 3

Estimated Mean Temperature

Central value:

Mean temperature

Error:

95% confidence interval


------------------------------------------------------------


EXAMPLE 4

Frequency and Magnitude

X error:

Frequency uncertainty

Y error:

Magnitude uncertainty


------------------------------------------------------------


EXAMPLE 5

Repeated Time-Series Measurements

Central result:

Mean waveform

Variability:

Shaded ±1 standard deviation region
"""


# ============================================================
# 68. STATISTICAL QUANTITY SUMMARY
# ============================================================

"""
STANDARD DEVIATION

Question:

"How variable are the individual measurements?"


------------------------------------------------------------


STANDARD ERROR

Question:

"How precisely has the mean been estimated?"


------------------------------------------------------------


CONFIDENCE INTERVAL

Question:

"What interval is associated with the estimated parameter
under the stated confidence procedure?"


------------------------------------------------------------


MEASUREMENT UNCERTAINTY

Question:

"What range of uncertainty is associated with the measured
quantity according to the measurement model?"


These should not be treated as interchangeable quantities.
"""


# ============================================================
# 69. PUBLICATION CHECKLIST
# ============================================================

"""
Before publishing a figure with error bars, check:

What does each central point represent?

What does each error bar represent?

How many measurements were used?

Were repeated measurements independent?

Was SD or SEM calculated correctly?

Is the confidence interval method appropriate?

Are measurement uncertainties properly defined?

Are X errors relevant?

Are error bars visible?

Are the units clear?

Does the caption explicitly define the error bars?

Are statistical claims supported by formal analysis?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
ERROR BARS


1. BASIC Y-ERROR BAR

ax.errorbar(

    x,

    y,

    yerr=error

)


------------------------------------------------------------


2. X-ERROR BAR

ax.errorbar(

    x,

    y,

    xerr=error

)


------------------------------------------------------------


3. X AND Y ERROR

ax.errorbar(

    x,

    y,

    xerr=x_error,

    yerr=y_error

)


------------------------------------------------------------


4. ADD CAPS

ax.errorbar(

    x,

    y,

    yerr=error,

    capsize=5

)


------------------------------------------------------------


5. STANDARD DEVIATION

std = np.std(

    measurements,

    axis=0,

    ddof=1

)


------------------------------------------------------------


6. STANDARD ERROR

sem = (

    std

    / np.sqrt(
        n
    )

)


------------------------------------------------------------


7. APPROXIMATE 95% CI

ci = (

    1.96

    * sem

)


Only appropriate under suitable assumptions.

For small samples, Student's t is commonly required.


------------------------------------------------------------


8. ASYMMETRIC ERROR

yerr = np.vstack(
    [
        lower_error,
        upper_error
    ]
)


------------------------------------------------------------


9. BAR PLOT ERROR

ax.bar(

    categories,

    mean,

    yerr=error,

    capsize=5

)


------------------------------------------------------------


10. REPEATED MEASUREMENTS

Repeated Runs
      ↓
Mean
      ↓
SD
      ↓
SEM / CI if needed
      ↓
Plot


------------------------------------------------------------


11. STANDARD DEVIATION

Describes:

Spread of individual observations.


------------------------------------------------------------


12. STANDARD ERROR

Describes:

Precision of the estimated mean.


------------------------------------------------------------


13. CONFIDENCE INTERVAL

Requires:

A defined statistical confidence procedure.


------------------------------------------------------------


14. MEASUREMENT UNCERTAINTY

Can include:

Instrument accuracy

Calibration

Resolution

Repeatability

Environmental effects

Other uncertainty sources


------------------------------------------------------------


15. ERROR BAR CAPTION

Prefer:

"Values represent mean ± 1 SD from five repeated
measurements."


rather than:

"Error bars are shown."


------------------------------------------------------------


16. SHADED UNCERTAINTY

For dense data:

ax.fill_between(

    x,

    mean - error,

    mean + error,

    alpha=0.25

)


------------------------------------------------------------


17. dB VALUES

Do not calculate naive percentage uncertainty directly
from dB or dBµV values.


------------------------------------------------------------


18. ERROR-BAR OVERLAP

Does NOT automatically prove or disprove statistical
significance.


------------------------------------------------------------


19. IMPORTANT RESEARCH PRINCIPLE

Never choose the error-bar definition because it produces
the smallest or most visually favorable uncertainty.

Choose it according to:

The research question

The experiment

The statistical meaning

The measurement method


------------------------------------------------------------


20. COMPLETE WORKFLOW

Repeated / Uncertain Data
          ↓
Identify Meaning of Error
          ↓
Calculate Correct Quantity
          ↓
Mean / Measurement
          ↓
SD / SEM / CI / Uncertainty
          ↓
Plot
          ↓
Label
          ↓
State Error Definition
          ↓
Interpret
          ↓
Report


------------------------------------------------------------


NEXT:

18_plot_styles_and_formatting.py


The next file will focus on general figure appearance:

Figure size

Font sizes

Line width

Marker size

Line styles

Grid formatting

Tick formatting

Spines

Legend formatting

Global rcParams

Temporary style settings

Reusable publication formatting

Consistent formatting across many figures

Screen/report/presentation figure differences

and importantly:

How to make figures professional without over-formatting
or altering the scientific meaning of the data.
"""
