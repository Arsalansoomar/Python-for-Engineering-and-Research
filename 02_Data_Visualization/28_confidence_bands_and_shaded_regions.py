"""
============================================================
Python for Engineering and Research
28 - Confidence Bands and Shaded Regions
============================================================

Purpose:
    Demonstrate how continuous uncertainty, experimental
    variability, Monte Carlo envelopes, confidence bands,
    target regions, operating zones, and engineering limits
    can be visualized using Matplotlib.

Topics:
    1. What is a shaded uncertainty band?
    2. fill_between()
    3. Mean ± standard deviation
    4. Mean ± standard error
    5. Approximate 95% confidence interval
    6. Confidence interval interpretation
    7. Min-max envelopes
    8. Percentile bands
    9. Monte Carlo uncertainty
    10. Nested uncertainty regions
    11. Multiple engineering cases
    12. Overlapping uncertainty bands
    13. Experimental vs simulation bands
    14. Target bands
    15. Safe operating regions
    16. Horizontal shaded regions
    17. Vertical shaded regions
    18. Conditional shading
    19. fill_between(where=...)
    20. Positive / negative regions
    21. Above / below requirement
    22. Missing values
    23. Variable sample size
    24. Logarithmic frequency axis
    25. Frequency-band highlighting
    26. Reusable uncertainty functions
    27. Publication-oriented figure
    28. PNG / PDF / SVG export
    29. Common mistakes
    30. Key takeaways

Important:
    Standard deviation, standard error, confidence intervals,
    percentile ranges, tolerance ranges, and measurement
    uncertainty are NOT interchangeable.

    Always state what a shaded band represents.

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. REQUIRED LIBRARIES
# ============================================================

import matplotlib.pyplot as plt
import matplotlib as mpl

import numpy as np
import pandas as pd

from pathlib import Path

from matplotlib.ticker import FuncFormatter


# ============================================================
# 2. WHAT IS A SHADED BAND?
# ============================================================

"""
A shaded band represents a region between:

Lower Bound

and

Upper Bound


Example:

                 Upper Bound
            ───────────────────
           /                    \
          /      SHADING         \
Mean ----/------------------------\----
        /                          \
       ─────────────────────────────
                 Lower Bound


Possible meanings include:

Mean ± Standard Deviation

Mean ± Standard Error

Confidence Interval

Percentile Range

Min-Max Envelope

Measurement Uncertainty

Tolerance Range

Engineering Target Region


The meaning must always be stated clearly.
"""


# ============================================================
# 3. ERROR BARS VS CONTINUOUS BANDS
# ============================================================

"""
ERROR BARS

Useful for:

Discrete operating points

Example:

Load = 20%, 40%, 60%, 80%, 100%


------------------------------------------------------------


SHADED BANDS

Useful for:

Continuous or densely sampled X values

Example:

Time-domain signals

Frequency response

Load sweep

Temperature sweep

Monte Carlo response envelope


Both represent uncertainty or spread,

but the visualization style is different.
"""


# ============================================================
# 4. PROJECT PATHS
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


output_figure_folder = (
    script_folder
    / "output_figures"
    / "confidence_bands"
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


print(
    "\n--- Output Figure Folder ---"
)


print(
    output_figure_folder
)


# ============================================================
# 5. CREATE REPRODUCIBLE EXPERIMENTAL DATA
# ============================================================

"""
Consider repeated converter efficiency measurements.

Each experiment contains efficiency values at several load
points.

Rows:

Repeated experiments


Columns:

Load operating points
"""


rng = np.random.default_rng(
    42
)


load_percent = np.linspace(
    10,
    100,
    19
)


true_efficiency = (

    96.0

    - 0.0007
    * (
        load_percent
        - 75
    ) ** 2

)


number_of_runs = 30


measurement_runs = []


for run in range(
    number_of_runs
):

    measurement_noise = rng.normal(

        loc=0,

        scale=0.30,

        size=len(
            load_percent
        )

    )


    run_offset = rng.normal(
        0,
        0.12
    )


    run_values = (

        true_efficiency

        + measurement_noise

        + run_offset

    )


    measurement_runs.append(
        run_values
    )


measurement_runs = np.asarray(
    measurement_runs
)


print(
    "\n--- Measurement Matrix Shape ---"
)


print(
    measurement_runs.shape
)


# ============================================================
# 6. INTERPRET MATRIX SHAPE
# ============================================================

"""
Example:

30 × 19


means:

30 repeated experiments

at:

19 load points.
"""


# ============================================================
# 7. MEAN CURVE
# ============================================================

mean_efficiency = np.mean(

    measurement_runs,

    axis=0

)


# ============================================================
# 8. SAMPLE STANDARD DEVIATION
# ============================================================

std_efficiency = np.std(

    measurement_runs,

    axis=0,

    ddof=1

)


# ============================================================
# 9. STANDARD ERROR OF THE MEAN
# ============================================================

"""
SEM:

Standard Error of the Mean

For independent repeated observations:

SEM = SD / sqrt(n)


It estimates uncertainty in the estimated mean,

not the spread of individual observations.
"""


sem_efficiency = (

    std_efficiency

    / np.sqrt(
        number_of_runs
    )

)


# ============================================================
# 10. APPROXIMATE 95% CONFIDENCE INTERVAL
# ============================================================

"""
A commonly seen large-sample approximation is:

Mean ± 1.96 × SEM


Important:

This is NOT a universal confidence-interval formula.

For:

Small sample sizes

Non-normal data

Correlated measurements

Repeated-measures structures

Heteroscedastic data

or other statistical designs


a different statistical method may be required.

Later statistical-analysis sections can handle those
methods more formally.
"""


normal_95_multiplier = 1.96


ci95_lower = (

    mean_efficiency

    - normal_95_multiplier
    * sem_efficiency

)


ci95_upper = (

    mean_efficiency

    + normal_95_multiplier
    * sem_efficiency

)


# ============================================================
# 11. BASIC fill_between()
# ============================================================

"""
Basic syntax:

ax.fill_between(
    x,
    lower,
    upper
)


The region between:

lower

and

upper

is filled.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    load_percent,

    mean_efficiency,

    linewidth=2,

    label="Mean"

)


ax.fill_between(

    load_percent,

    mean_efficiency
    - std_efficiency,

    mean_efficiency
    + std_efficiency,

    alpha=0.25,

    label="±1 SD"

)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Mean Efficiency ± Standard Deviation"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 12. MEAN ± SD INTERPRETATION
# ============================================================

"""
Mean ± SD describes:

Spread / variability of the observations


It does NOT directly mean:

Confidence interval of the mean.


A wide SD band indicates:

Large observation-to-observation variability.
"""


# ============================================================
# 13. MEAN ± SEM BAND
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    load_percent,

    mean_efficiency,

    linewidth=2,

    label="Mean"

)


ax.fill_between(

    load_percent,

    mean_efficiency
    - sem_efficiency,

    mean_efficiency
    + sem_efficiency,

    alpha=0.25,

    label="±1 SEM"

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


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 14. SD VS SEM
# ============================================================

"""
STANDARD DEVIATION

Describes:

Variability among observations


------------------------------------------------------------


STANDARD ERROR

Describes:

Estimated uncertainty of the sample mean


SEM becomes smaller as:

n increases


assuming the observations provide independent information.


Do not label:

SEM

as:

Standard Deviation
"""


# ============================================================
# 15. APPROXIMATE 95% CI BAND
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    load_percent,

    mean_efficiency,

    linewidth=2,

    label="Mean"

)


ax.fill_between(

    load_percent,

    ci95_lower,

    ci95_upper,

    alpha=0.25,

    label="Approx. 95% CI of Mean"

)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Approximate 95% Confidence Band"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 16. CONFIDENCE INTERVAL INTERPRETATION
# ============================================================

"""
A confidence interval around the estimated mean should not
be interpreted as:

"95% of measurements lie inside this band."


That is a different concept.


A confidence interval concerns uncertainty in an estimated
statistical quantity such as the mean.


The distribution of individual measurements can be much
wider.
"""


# ============================================================
# 17. COMPARE SD AND CI
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    load_percent,

    mean_efficiency,

    linewidth=2,

    label="Mean"

)


ax.fill_between(

    load_percent,

    mean_efficiency
    - std_efficiency,

    mean_efficiency
    + std_efficiency,

    alpha=0.15,

    label="±1 SD"

)


ax.fill_between(

    load_percent,

    ci95_lower,

    ci95_upper,

    alpha=0.30,

    label="Approx. 95% CI of Mean"

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
# 18. MIN-MAX ENVELOPE
# ============================================================

"""
Another simple envelope is:

Minimum observed value

to

Maximum observed value


This shows the complete observed range.

However:

Min and max can be highly sensitive to rare observations.
"""


minimum_efficiency = np.min(

    measurement_runs,

    axis=0

)


maximum_efficiency = np.max(

    measurement_runs,

    axis=0

)


# ============================================================
# 19. MIN-MAX BAND
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    load_percent,

    mean_efficiency,

    linewidth=2,

    label="Mean"

)


ax.fill_between(

    load_percent,

    minimum_efficiency,

    maximum_efficiency,

    alpha=0.20,

    label="Observed Min-Max"

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
# 20. PERCENTILE BANDS
# ============================================================

"""
Percentile bands are very useful for:

Monte Carlo results

Robustness studies

Non-normal distributions


Example:

5th percentile

to

95th percentile


This contains the central:

90%

of the sampled values at each X point.
"""


percentile_5 = np.percentile(

    measurement_runs,

    5,

    axis=0

)


percentile_25 = np.percentile(

    measurement_runs,

    25,

    axis=0

)


percentile_50 = np.percentile(

    measurement_runs,

    50,

    axis=0

)


percentile_75 = np.percentile(

    measurement_runs,

    75,

    axis=0

)


percentile_95 = np.percentile(

    measurement_runs,

    95,

    axis=0

)


# ============================================================
# 21. 5TH-95TH PERCENTILE BAND
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    load_percent,

    percentile_50,

    linewidth=2,

    label="Median"

)


ax.fill_between(

    load_percent,

    percentile_5,

    percentile_95,

    alpha=0.25,

    label="5th-95th Percentile"

)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Percentile Envelope"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 22. NESTED PERCENTILE BANDS
# ============================================================

"""
Nested bands can show:

Central 50%

and

Central 90%


Example:

25th to 75th percentile

inside:

5th to 95th percentile
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.fill_between(

    load_percent,

    percentile_5,

    percentile_95,

    alpha=0.15,

    label="5th-95th Percentile"

)


ax.fill_between(

    load_percent,

    percentile_25,

    percentile_75,

    alpha=0.30,

    label="25th-75th Percentile"

)


ax.plot(

    load_percent,

    percentile_50,

    linewidth=2,

    label="Median"

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

plt.show())


# ============================================================
# 23. MONTE CARLO RESPONSE DATA
# ============================================================

"""
Now create a larger Monte Carlo example.

Suppose converter losses vary because of:

Component tolerance

Temperature

Parasitic variation

Device parameter variation


Each Monte Carlo run produces a loss curve.
"""


number_of_monte_carlo_runs = 1000


frequency_khz = np.linspace(
    50,
    250,
    80
)


base_loss_w = (

    7

    + 0.00018
    * (
        frequency_khz
        - 80
    ) ** 2

)


monte_carlo_losses = []


for run in range(
    number_of_monte_carlo_runs
):

    scale_factor = rng.normal(
        1.0,
        0.06
    )


    offset = rng.normal(
        0,
        0.5
    )


    local_noise = rng.normal(

        0,

        0.18,

        len(
            frequency_khz
        )

    )


    loss_curve = (

        scale_factor
        * base_loss_w

        + offset

        + local_noise

    )


    monte_carlo_losses.append(
        loss_curve
    )


monte_carlo_losses = np.asarray(
    monte_carlo_losses
)


print(
    "\n--- Monte Carlo Matrix ---"
)


print(
    monte_carlo_losses.shape
)


# ============================================================
# 24. MONTE CARLO PERCENTILES
# ============================================================

mc_median = np.percentile(

    monte_carlo_losses,

    50,

    axis=0

)


mc_p05 = np.percentile(

    monte_carlo_losses,

    5,

    axis=0

)


mc_p25 = np.percentile(

    monte_carlo_losses,

    25,

    axis=0

)


mc_p75 = np.percentile(

    monte_carlo_losses,

    75,

    axis=0

)


mc_p95 = np.percentile(

    monte_carlo_losses,

    95,

    axis=0

)


# ============================================================
# 25. MONTE CARLO ENVELOPE
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.fill_between(

    frequency_khz,

    mc_p05,

    mc_p95,

    alpha=0.15,

    label="5th-95th Percentile"

)


ax.fill_between(

    frequency_khz,

    mc_p25,

    mc_p75,

    alpha=0.30,

    label="25th-75th Percentile"

)


ax.plot(

    frequency_khz,

    mc_median,

    linewidth=2,

    label="Median"

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Monte Carlo Loss Envelope"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 26. MONTE CARLO BAND INTERPRETATION
# ============================================================

"""
Percentile bands describe the simulated distribution.

Example:

5th-95th percentile

means:

At each evaluated frequency,

approximately the central 90% of sampled Monte Carlo
results lie between those percentiles.


This is NOT automatically a:

95% confidence interval.
"""


# ============================================================
# 27. SHOW INDIVIDUAL MONTE CARLO RUNS
# ============================================================

"""
A useful teaching comparison is to show:

Some individual runs

behind:

The summary band.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


for run in range(
    30
):

    ax.plot(

        frequency_khz,

        monte_carlo_losses[
            run
        ],

        linewidth=0.5,

        alpha=0.15

    )


ax.fill_between(

    frequency_khz,

    mc_p05,

    mc_p95,

    alpha=0.20,

    label="5th-95th Percentile"

)


ax.plot(

    frequency_khz,

    mc_median,

    linewidth=2,

    label="Median"

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Power Loss [W]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show())


# ============================================================
# 28. DO NOT PLOT THOUSANDS OF LINES UNNECESSARILY
# ============================================================

"""
Plotting:

1000 Monte Carlo curves


can create a visually dense figure.

A useful approach is:

A few representative runs

+
Percentile envelope

+
Median


or simply:

Percentile envelope

+
Median.
"""


# ============================================================
# 29. TARGET BAND
# ============================================================

"""
Shading is not only for uncertainty.

It can also represent an engineering target.

Example:

Desired output voltage:

47.5 V
to
48.5 V
"""


time_ms = np.linspace(
    0,
    5,
    1000
)


output_voltage = (

    48

    * (
        1
        - np.exp(
            -time_ms
            / 0.7
        )
    )

    + 0.25
    * np.sin(
        2
        * np.pi
        * 3
        * time_ms
    )

)


target_voltage_min = 47.5

target_voltage_max = 48.5


# ============================================================
# 30. HORIZONTAL TARGET REGION
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    time_ms,

    output_voltage,

    label="Output Voltage"

)


ax.axhspan(

    target_voltage_min,

    target_voltage_max,

    alpha=0.20,

    label="Target Range"

)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Voltage Target Region"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show())


# ============================================================
# 31. HORIZONTAL SHADED REGION
# ============================================================

"""
Use:

ax.axhspan(
    y_min,
    y_max
)


for horizontal engineering bands such as:

Safe temperature

Target voltage

Allowed efficiency

Acceptable THD

Measurement tolerance
"""


# ============================================================
# 32. VERTICAL OPERATING REGION
# ============================================================

"""
A vertical span represents a selected X-axis region.

Example:

Steady-state window:

3 ms to 5 ms
"""


steady_state_start = 3.0

steady_state_end = 5.0


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    output_voltage
)


ax.axvspan(

    steady_state_start,

    steady_state_end,

    alpha=0.20,

    label="Steady-State Window"

)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show())


# ============================================================
# 33. VERTICAL SHADED REGION APPLICATIONS
# ============================================================

"""
axvspan() is useful for:

Startup region

Steady-state region

Measurement window

Regulatory frequency band

Resonance region

Operating interval

Fault interval

Training / test region
"""


# ============================================================
# 34. MULTIPLE OPERATING REGIONS
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    output_voltage
)


ax.axvspan(

    0,

    1.0,

    alpha=0.15,

    label="Startup"

)


ax.axvspan(

    1.0,

    3.0,

    alpha=0.12,

    label="Settling"

)


ax.axvspan(

    3.0,

    5.0,

    alpha=0.15,

    label="Steady State"

)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show())


# ============================================================
# 35. CONDITIONAL fill_between()
# ============================================================

"""
fill_between() supports:

where=


This allows only selected parts of the data to be shaded.


Example:

Shade where:

Voltage >= Lower Target

AND

Voltage <= Upper Target
"""


inside_target = (

    (
        output_voltage
        >= target_voltage_min
    )

    &

    (
        output_voltage
        <= target_voltage_max
    )

)


# ============================================================
# 36. SHADE WHEN SIGNAL IS INSIDE TARGET
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    time_ms,

    output_voltage,

    linewidth=1.5,

    label="Output Voltage"

)


ax.fill_between(

    time_ms,

    target_voltage_min,

    target_voltage_max,

    where=inside_target,

    alpha=0.30,

    interpolate=True,

    label="Inside Target"

)


ax.axhline(

    target_voltage_min,

    linestyle="--",

    linewidth=1

)


ax.axhline(

    target_voltage_max,

    linestyle="--",

    linewidth=1

)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show())


# ============================================================
# 37. OUTSIDE-TARGET MASK
# ============================================================

outside_target = (

    ~inside_target

)


# ============================================================
# 38. SHADE TARGET VIOLATIONS
# ============================================================

"""
For violations, shade between the signal and the nearest
engineering boundary.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    time_ms,

    output_voltage,

    linewidth=1.5

)


# ------------------------------------------------------------
# Below lower target
# ------------------------------------------------------------

below_target = (

    output_voltage

    < target_voltage_min

)


ax.fill_between(

    time_ms,

    output_voltage,

    target_voltage_min,

    where=below_target,

    alpha=0.25,

    interpolate=True,

    label="Below Target"

)


# ------------------------------------------------------------
# Above upper target
# ------------------------------------------------------------

above_target = (

    output_voltage

    > target_voltage_max

)


ax.fill_between(

    time_ms,

    target_voltage_max,

    output_voltage,

    where=above_target,

    alpha=0.25,

    interpolate=True,

    label="Above Target"

)


ax.axhspan(

    target_voltage_min,

    target_voltage_max,

    alpha=0.08,

    label="Target Range"

)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show())


# ============================================================
# 39. POSITIVE AND NEGATIVE REGIONS
# ============================================================

"""
Conditional shading can also show:

Positive values

vs

Negative values.


Example:

Difference between:

Design B

and:

Baseline
"""


load_dense = np.linspace(
    10,
    100,
    200
)


baseline_performance = (

    94

    + 0.018
    * load_dense

    - 0.00012
    * load_dense ** 2

)


design_performance = (

    baseline_performance

    + 0.5

    * np.sin(
        load_dense
        / 12
    )

)


performance_difference = (

    design_performance

    - baseline_performance

)


# ============================================================
# 40. SHADE POSITIVE / NEGATIVE DIFFERENCE
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    load_dense,

    performance_difference,

    linewidth=1.8

)


ax.axhline(

    0,

    linewidth=1

)


ax.fill_between(

    load_dense,

    0,

    performance_difference,

    where=(
        performance_difference
        >= 0
    ),

    interpolate=True,

    alpha=0.25,

    label="Improvement"

)


ax.fill_between(

    load_dense,

    0,

    performance_difference,

    where=(
        performance_difference
        < 0
    ),

    interpolate=True,

    alpha=0.25,

    label="Reduction in Performance"

)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Difference [percentage points]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show())


# ============================================================
# 41. CONDITIONAL SHADING INTERPRETATION
# ============================================================

"""
Shading helps identify regions where a condition is true.

However:

Always include numerical axis values.

Do not interpret:

Shaded region

without knowing:

What inequality created it?
"""


# ============================================================
# 42. TWO ENGINEERING CASES WITH UNCERTAINTY
# ============================================================

"""
Now compare two designs.

Each has:

Mean

and

Standard deviation.
"""


design_a_mean = (

    94.0

    + 1.5
    * (
        1
        - np.exp(
            -load_dense
            / 35
        )
    )

)


design_b_mean = (

    design_a_mean

    + 0.55

)


design_a_std = (

    0.35

    + 0.10
    * np.sin(
        load_dense
        / 20
    ) ** 2

)


design_b_std = (

    0.25

    + 0.08
    * np.cos(
        load_dense
        / 25
    ) ** 2

)


# ============================================================
# 43. TWO UNCERTAINTY BANDS
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    load_dense,

    design_a_mean,

    linewidth=2,

    label="Design A Mean"

)


ax.fill_between(

    load_dense,

    design_a_mean
    - design_a_std,

    design_a_mean
    + design_a_std,

    alpha=0.20

)


ax.plot(

    load_dense,

    design_b_mean,

    linewidth=2,

    linestyle="--",

    label="Design B Mean"

)


ax.fill_between(

    load_dense,

    design_b_mean
    - design_b_std,

    design_b_mean
    + design_b_std,

    alpha=0.20

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

plt.show())


# ============================================================
# 44. OVERLAPPING-BAND WARNING
# ============================================================

"""
Visual overlap between uncertainty bands does NOT by
itself provide a universal statistical significance test.


Likewise:

Non-overlapping shaded bands

do not automatically establish a specific hypothesis-test
result.


Statistical inference requires a method appropriate to the
study design.
"""


# ============================================================
# 45. SIMULATION VS EXPERIMENT BAND
# ============================================================

"""
Example:

Simulation produces one deterministic prediction.

Experiment produces:

Mean
+
Measured variability.
"""


simulation_efficiency = (

    true_efficiency

    + 0.08

)


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    load_percent,

    simulation_efficiency,

    linewidth=2,

    linestyle="--",

    label="Simulation"

)


ax.plot(

    load_percent,

    mean_efficiency,

    linewidth=2,

    label="Experimental Mean"

)


ax.fill_between(

    load_percent,

    mean_efficiency
    - std_efficiency,

    mean_efficiency
    + std_efficiency,

    alpha=0.20,

    label="Experimental ±1 SD"

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

plt.show())


# ============================================================
# 46. MODEL UNCERTAINTY VS MEASUREMENT VARIABILITY
# ============================================================

"""
Do not automatically shade simulation and experimental
results using the same statistical meaning.

For example:

Experimental band:

Repeated-measurement SD


Simulation band:

Parameter-uncertainty percentile range


These represent different sources of variation.

The figure caption should state the definition of each.
"""


# ============================================================
# 47. VARIABLE SAMPLE SIZE
# ============================================================

"""
Real experiments may have different numbers of valid
measurements at different X points.

Example:

Some runs contain missing measurements.
"""


measurement_runs_missing = (
    measurement_runs.copy()
)


measurement_runs_missing[
    0:5,
    3
] = np.nan


measurement_runs_missing[
    0:10,
    10
] = np.nan


measurement_runs_missing[
    0:15,
    16
] = np.nan


# ============================================================
# 48. VALID SAMPLE COUNT AT EACH X
# ============================================================

valid_sample_count = np.sum(

    np.isfinite(
        measurement_runs_missing
    ),

    axis=0

)


print(
    "\n--- Valid Sample Count at Each Load ---"
)


print(
    valid_sample_count
)


# ============================================================
# 49. NaN-AWARE MEAN
# ============================================================

missing_mean = np.nanmean(

    measurement_runs_missing,

    axis=0

)


# ============================================================
# 50. NaN-AWARE STANDARD DEVIATION
# ============================================================

missing_std = np.nanstd(

    measurement_runs_missing,

    axis=0,

    ddof=1

)


# ============================================================
# 51. VARIABLE-N SEM
# ============================================================

missing_sem = (

    missing_std

    / np.sqrt(
        valid_sample_count
    )

)


# ============================================================
# 52. VARIABLE-N CONFIDENCE BAND
# ============================================================

missing_ci_lower = (

    missing_mean

    - 1.96
    * missing_sem

)


missing_ci_upper = (

    missing_mean

    + 1.96
    * missing_sem

)


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    load_percent,

    missing_mean,

    label="Mean"

)


ax.fill_between(

    load_percent,

    missing_ci_lower,

    missing_ci_upper,

    alpha=0.25,

    label="Approx. 95% CI"

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

plt.show())


# ============================================================
# 53. MISSING-DATA WARNING
# ============================================================

"""
If the number of observations varies across X:

The uncertainty band may change partly because:

n changed.


Therefore researchers should inspect or report:

Valid sample counts


when this matters.
"""


# ============================================================
# 54. FREQUENCY-DOMAIN UNCERTAINTY
# ============================================================

"""
Uncertainty bands also work on logarithmic X axes.

Example:

Frequency-domain magnitude uncertainty.
"""


frequency_hz = np.logspace(

    4,

    np.log10(
        30e6
    ),

    400

)


log_frequency = np.log10(
    frequency_hz
)


frequency_mean_dbuV = (

    105

    - 8
    * (
        log_frequency
        - 4
    )

    + 4
    * np.sin(
        4
        * log_frequency
    )

)


frequency_std_db = (

    1.5

    + 0.8
    * np.sin(
        2
        * log_frequency
    ) ** 2

)


# ============================================================
# 55. LOG-FREQUENCY UNCERTAINTY BAND
# ============================================================

fig, ax = plt.subplots(
    figsize=(8.5, 5)
)


ax.plot(

    frequency_hz,

    frequency_mean_dbuV,

    linewidth=1.6,

    label="Mean Spectrum"

)


ax.fill_between(

    frequency_hz,

    frequency_mean_dbuV
    - frequency_std_db,

    frequency_mean_dbuV
    + frequency_std_db,

    alpha=0.22,

    label="±1 SD"

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


ax.legend()


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show())


# ============================================================
# 56. dB BAND WARNING
# ============================================================

"""
A band expressed as:

Mean dBµV ± SD in dB


is a statistical summary in the logarithmic dB domain.

It should not automatically be interpreted as the same
thing as calculating uncertainty in linear voltage and
then converting the limits to dB.

The correct treatment depends on:

What quantity varied?

How uncertainty was defined?

In which domain the statistics were calculated?
"""


# ============================================================
# 57. FREQUENCY-BAND HIGHLIGHTING
# ============================================================

"""
Vertical shaded regions are useful for identifying:

Frequency bands

Harmonic regions

Measurement ranges

Regulatory ranges

Resonance bands
"""


selected_band_min_hz = 1e6

selected_band_max_hz = 5e6


fig, ax = plt.subplots(
    figsize=(8.5, 5)
)


ax.plot(

    frequency_hz,

    frequency_mean_dbuV

)


ax.set_xscale(
    "log"
)


ax.axvspan(

    selected_band_min_hz,

    selected_band_max_hz,

    alpha=0.20,

    label="Selected Analysis Band"

)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.legend()


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show())


# ============================================================
# 58. MULTIPLE FREQUENCY REGIONS
# ============================================================

fig, ax = plt.subplots(
    figsize=(8.5, 5)
)


ax.plot(

    frequency_hz,

    frequency_mean_dbuV

)


ax.set_xscale(
    "log"
)


ax.axvspan(

    100e3,

    1e6,

    alpha=0.12,

    label="Band 1"

)


ax.axvspan(

    1e6,

    10e6,

    alpha=0.12,

    label="Band 2"

)


ax.axvspan(

    10e6,

    30e6,

    alpha=0.12,

    label="Band 3"

)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.legend()


ax.grid(
    True,
    which="both"
)


plt.tight_layout()

plt.show())


# ============================================================
# 59. REUSABLE STATISTICS FUNCTION
# ============================================================

def calculate_band_statistics(
    repeated_data,
    axis=0
):
    """
    Calculate common repeated-measurement statistics.

    Parameters
    ----------
    repeated_data : array-like
        Repeated observations.

    axis : int
        Axis containing repeated observations.

    Returns
    -------
    statistics : dict
        Mean, SD, SEM, approximate 95% CI,
        min/max, and selected percentiles.
    """

    values = np.asarray(
        repeated_data,
        dtype=float
    )


    valid_count = np.sum(

        np.isfinite(
            values
        ),

        axis=axis

    )


    mean = np.nanmean(

        values,

        axis=axis

    )


    std = np.nanstd(

        values,

        axis=axis,

        ddof=1

    )


    with np.errstate(
        divide="ignore",
        invalid="ignore"
    ):

        sem = (

            std

            / np.sqrt(
                valid_count
            )

        )


    ci95_lower = (

        mean

        - 1.96
        * sem

    )


    ci95_upper = (

        mean

        + 1.96
        * sem

    )


    return {

        "count":
            valid_count,

        "mean":
            mean,

        "std":
            std,

        "sem":
            sem,

        "ci95_lower":
            ci95_lower,

        "ci95_upper":
            ci95_upper,

        "minimum":
            np.nanmin(
                values,
                axis=axis
            ),

        "maximum":
            np.nanmax(
                values,
                axis=axis
            ),

        "p05":
            np.nanpercentile(
                values,
                5,
                axis=axis
            ),

        "p25":
            np.nanpercentile(
                values,
                25,
                axis=axis
            ),

        "median":
            np.nanpercentile(
                values,
                50,
                axis=axis
            ),

        "p75":
            np.nanpercentile(
                values,
                75,
                axis=axis
            ),

        "p95":
            np.nanpercentile(
                values,
                95,
                axis=axis
            )

    }


# ============================================================
# 60. USE STATISTICS FUNCTION
# ============================================================

statistics = calculate_band_statistics(

    measurement_runs

)


print(
    "\n--- Statistics Keys ---"
)


print(
    statistics.keys()
)


# ============================================================
# 61. REUSABLE BAND-PLOTTING FUNCTION
# ============================================================

def plot_uncertainty_band(
    ax,
    x,
    center,
    lower,
    upper,
    label,
    line_label=None,
    alpha=0.25,
    linestyle="-",
    linewidth=1.8
):
    """
    Plot a central curve with a shaded band.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axis.

    x : array-like
        X coordinates.

    center : array-like
        Central curve.

    lower : array-like
        Lower band.

    upper : array-like
        Upper band.

    label : str
        Band label.

    line_label : str, optional
        Central-line legend label.

    alpha : float
        Band transparency.

    linestyle : str
        Center-line style.

    linewidth : float
        Center-line width.
    """

    x = np.asarray(
        x,
        dtype=float
    )


    center = np.asarray(
        center,
        dtype=float
    )


    lower = np.asarray(
        lower,
        dtype=float
    )


    upper = np.asarray(
        upper,
        dtype=float
    )


    if not (
        x.shape
        ==
        center.shape
        ==
        lower.shape
        ==
        upper.shape
    ):

        raise ValueError(
            "X, center, lower, and upper "
            "must have identical shapes."
        )


    ax.fill_between(

        x,

        lower,

        upper,

        alpha=alpha,

        label=label

    )


    ax.plot(

        x,

        center,

        linestyle=linestyle,

        linewidth=linewidth,

        label=line_label

    )


# ============================================================
# 62. USE REUSABLE BAND FUNCTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


plot_uncertainty_band(

    ax=ax,

    x=load_percent,

    center=statistics[
        "mean"
    ],

    lower=statistics[
        "ci95_lower"
    ],

    upper=statistics[
        "ci95_upper"
    ],

    label="Approx. 95% CI",

    line_label="Mean"

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

plt.show())


# ============================================================
# 63. REUSABLE PERCENTILE-BAND FUNCTION
# ============================================================

def plot_percentile_band(
    ax,
    x,
    repeated_data,
    lower_percentile=5,
    upper_percentile=95,
    center_percentile=50,
    label=None,
    alpha=0.25
):
    """
    Plot a percentile envelope from repeated data.

    Parameters
    ----------
    ax : matplotlib.axes.Axes

    x : array-like
        Shared X values.

    repeated_data : 2D array-like
        Shape:
        runs × X points

    lower_percentile : float

    upper_percentile : float

    center_percentile : float

    label : str, optional

    alpha : float

    Returns
    -------
    lower, center, upper : ndarray
    """

    x = np.asarray(
        x,
        dtype=float
    )


    data = np.asarray(
        repeated_data,
        dtype=float
    )


    if data.ndim != 2:

        raise ValueError(
            "repeated_data must be two-dimensional."
        )


    if data.shape[1] != len(
        x
    ):

        raise ValueError(
            "Number of X values must match "
            "the second dimension of repeated_data."
        )


    if not (
        0
        <= lower_percentile
        <= center_percentile
        <= upper_percentile
        <= 100
    ):

        raise ValueError(
            "Percentiles must satisfy:\n"
            "0 <= lower <= center <= upper <= 100"
        )


    lower = np.nanpercentile(

        data,

        lower_percentile,

        axis=0

    )


    center = np.nanpercentile(

        data,

        center_percentile,

        axis=0

    )


    upper = np.nanpercentile(

        data,

        upper_percentile,

        axis=0

    )


    if label is None:

        label = (

            f"{lower_percentile:g}th-"
            f"{upper_percentile:g}th Percentile"

        )


    ax.fill_between(

        x,

        lower,

        upper,

        alpha=alpha,

        label=label

    )


    ax.plot(

        x,

        center,

        linewidth=1.8,

        label=(
            f"{center_percentile:g}th Percentile"
        )

    )


    return (
        lower,
        center,
        upper
    )


# ============================================================
# 64. USE PERCENTILE FUNCTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


plot_percentile_band(

    ax=ax,

    x=frequency_khz,

    repeated_data=monte_carlo_losses,

    lower_percentile=5,

    upper_percentile=95,

    center_percentile=50

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Power Loss [W]"
)


ax.legend()


ax.grid(
    True
)


plt.tight_layout()

plt.show())


# ============================================================
# 65. SAVE SUMMARY DATA
# ============================================================

summary_dataframe = pd.DataFrame(
    {
        "Load_percent":
            load_percent,

        "Mean_Efficiency_percent":
            statistics[
                "mean"
            ],

        "SD_percent":
            statistics[
                "std"
            ],

        "SEM_percent":
            statistics[
                "sem"
            ],

        "CI95_Lower_percent":
            statistics[
                "ci95_lower"
            ],

        "CI95_Upper_percent":
            statistics[
                "ci95_upper"
            ],

        "P05_percent":
            statistics[
                "p05"
            ],

        "Median_percent":
            statistics[
                "median"
            ],

        "P95_percent":
            statistics[
                "p95"
            ],

        "Valid_Samples":
            statistics[
                "count"
            ]
    }
)


summary_file = (
    output_data_folder
    / "confidence_band_summary.csv"
)


summary_dataframe.to_csv(

    summary_file,

    index=False

)


print(
    "\n--- Confidence Summary Saved ---"
)


print(
    summary_file
)


# ============================================================
# 66. PUBLICATION FIGURE SIZE
# ============================================================

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


publication_width_mm = 178


publication_width_in = (
    mm_to_inches(
        publication_width_mm
    )
)


publication_height_in = (

    publication_width_in

    * 0.72

)


# ============================================================
# 67. PUBLICATION STYLE
# ============================================================

publication_style = {

    "font.size":
        8,

    "axes.labelsize":
        9,

    "axes.titlesize":
        9,

    "xtick.labelsize":
        8,

    "ytick.labelsize":
        8,

    "legend.fontsize":
        8,

    "axes.linewidth":
        0.8,

    "lines.linewidth":
        1.4,

    "xtick.direction":
        "in",

    "ytick.direction":
        "in",

    "xtick.top":
        True,

    "ytick.right":
        True

}


# ============================================================
# 68. FINAL MULTI-PANEL UNCERTAINTY FIGURE
# ============================================================

"""
Final example:

(a)

Repeated-measurement SD


(b)

Approximate confidence interval


(c)

Monte Carlo percentile envelope


(d)

Engineering target / operating region
"""


with mpl.rc_context(
    publication_style
):

    fig, axes = plt.subplots(

        2,

        2,

        figsize=(
            publication_width_in,
            publication_height_in
        ),

        layout="constrained"

    )


    # ========================================================
    # PANEL (a) - MEAN ± SD
    # ========================================================

    ax_a = axes[
        0,
        0
    ]


    ax_a.plot(

        load_percent,

        mean_efficiency,

        label="Mean"

    )


    ax_a.fill_between(

        load_percent,

        mean_efficiency
        - std_efficiency,

        mean_efficiency
        + std_efficiency,

        alpha=0.25,

        label="±1 SD"

    )


    ax_a.set_xlabel(
        "Load [%]"
    )


    ax_a.set_ylabel(
        "Efficiency [%]"
    )


    ax_a.legend()


    ax_a.text(

        0.02,

        0.96,

        "(a)",

        transform=ax_a.transAxes,

        va="top",

        fontweight="bold"

    )


    ax_a.grid(
        True,
        alpha=0.35
    )


    # ========================================================
    # PANEL (b) - 95% CI
    # ========================================================

    ax_b = axes[
        0,
        1
    ]


    ax_b.plot(

        load_percent,

        mean_efficiency,

        label="Mean"

    )


    ax_b.fill_between(

        load_percent,

        ci95_lower,

        ci95_upper,

        alpha=0.25,

        label="Approx. 95% CI"

    )


    ax_b.set_xlabel(
        "Load [%]"
    )


    ax_b.set_ylabel(
        "Efficiency [%]"
    )


    ax_b.legend()


    ax_b.text(

        0.02,

        0.96,

        "(b)",

        transform=ax_b.transAxes,

        va="top",

        fontweight="bold"

    )


    ax_b.grid(
        True,
        alpha=0.35
    )


    # ========================================================
    # PANEL (c) - MONTE CARLO PERCENTILE BAND
    # ========================================================

    ax_c = axes[
        1,
        0
    ]


    ax_c.fill_between(

        frequency_khz,

        mc_p05,

        mc_p95,

        alpha=0.15,

        label="5th-95th"

    )


    ax_c.fill_between(

        frequency_khz,

        mc_p25,

        mc_p75,

        alpha=0.30,

        label="25th-75th"

    )


    ax_c.plot(

        frequency_khz,

        mc_median,

        label="Median"

    )


    ax_c.set_xlabel(
        "Switching Frequency [kHz]"
    )


    ax_c.set_ylabel(
        "Power Loss [W]"
    )


    ax_c.legend()


    ax_c.text(

        0.02,

        0.96,

        "(c)",

        transform=ax_c.transAxes,

        va="top",

        fontweight="bold"

    )


    ax_c.grid(
        True,
        alpha=0.35
    )


    # ========================================================
    # PANEL (d) - TARGET REGION
    # ========================================================

    ax_d = axes[
        1,
        1
    ]


    ax_d.plot(

        time_ms,

        output_voltage,

        label="Output Voltage"

    )


    ax_d.axhspan(

        target_voltage_min,

        target_voltage_max,

        alpha=0.20,

        label="Target Range"

    )


    ax_d.axvspan(

        steady_state_start,

        steady_state_end,

        alpha=0.10,

        label="Steady State"

    )


    ax_d.set_xlabel(
        "Time [ms]"
    )


    ax_d.set_ylabel(
        "Voltage [V]"
    )


    ax_d.legend()


    ax_d.text(

        0.02,

        0.96,

        "(d)",

        transform=ax_d.transAxes,

        va="top",

        fontweight="bold"

    )


    ax_d.grid(
        True,
        alpha=0.35
    )


    # ========================================================
    # SAVE FINAL FIGURE
    # ========================================================

    final_png = (
        output_figure_folder
        / "engineering_uncertainty_bands.png"
    )


    final_pdf = (
        output_figure_folder
        / "engineering_uncertainty_bands.pdf"
    )


    final_svg = (
        output_figure_folder
        / "engineering_uncertainty_bands.svg"
    )


    fig.savefig(

        final_png,

        dpi=300

    )


    fig.savefig(
        final_pdf
    )


    fig.savefig(
        final_svg
    )


    print(
        "\n--- Final Uncertainty Figures Saved ---"
    )


    print(
        final_png
    )


    print(
        final_pdf
    )


    print(
        final_svg
    )


    plt.show()


# ============================================================
# 69. STANDARD DEVIATION IS NOT A CONFIDENCE INTERVAL
# ============================================================

"""
Incorrect:

"Shaded area represents 95% confidence interval"

when the code actually plots:

mean ± standard deviation


Always match:

Mathematical calculation

and

Figure description.
"""


# ============================================================
# 70. SEM IS NOT SD
# ============================================================

"""
SD:

Spread of observations


SEM:

Uncertainty in estimated mean


A small SEM does not necessarily mean the physical process
has low variability.
"""


# ============================================================
# 71. CI IS NOT A PREDICTION INTERVAL
# ============================================================

"""
A confidence interval for the mean addresses:

Where the estimated mean may lie.


A prediction interval addresses:

Where a future observation may lie.


Prediction intervals are normally wider.


Do not use the terminology interchangeably.
"""


# ============================================================
# 72. PERCENTILE BAND IS NOT CONFIDENCE BAND
# ============================================================

"""
Example:

5th-95th percentile Monte Carlo envelope


describes:

Distribution of simulated outcomes


It is not automatically:

A 90% confidence interval of a model parameter.
"""


# ============================================================
# 73. MIN-MAX BAND IS SENSITIVE TO EXTREMES
# ============================================================

"""
As the number of runs increases:

The observed minimum and maximum may move outward.


Therefore min-max envelopes should not automatically be
interpreted as stable uncertainty intervals.
"""


# ============================================================
# 74. COMMON MISTAKE - NO BAND DEFINITION
# ============================================================

"""
Weak legend:

Uncertainty


Better:

Mean ± 1 SD

Approx. 95% CI of Mean

5th-95th Percentile

Observed Min-Max

Instrument Uncertainty ±0.5 V


The reader should know exactly what the band means.
"""


# ============================================================
# 75. COMMON MISTAKE - TOO DARK SHADING
# ============================================================

"""
A fully opaque uncertainty region can hide:

Data curves

Grid

Other cases


Use:

alpha=


to make the band partially transparent.
"""


# ============================================================
# 76. COMMON MISTAKE - TOO LIGHT SHADING
# ============================================================

"""
If:

alpha

is extremely small,

the band may disappear in:

PDF viewing

Printing

Presentation projection


Always inspect the exported figure.
"""


# ============================================================
# 77. COMMON MISTAKE - MANY OVERLAPPING BANDS
# ============================================================

"""
Five or ten overlapping uncertainty bands may become
difficult to interpret.

Consider:

Separate panels

Summary statistics

Difference curves

or

Selected representative cases.
"""


# ============================================================
# 78. COMMON MISTAKE - BAND WITHOUT CENTER CURVE
# ============================================================

"""
A shaded region alone may make it unclear what central
estimate is being reported.

Often use:

Band
+
Mean / Median line
"""


# ============================================================
# 79. COMMON MISTAKE - MEAN WITH PERCENTILE BAND
# ============================================================

"""
It is possible to plot:

Mean

with:

5th-95th percentiles.


But be clear about the combination.

For skewed data:

Median

may align more naturally with percentile bands.
"""


# ============================================================
# 80. COMMON MISTAKE - INTERPOLATING MISSING DATA SILENTLY
# ============================================================

"""
If observations are missing:

Do not automatically interpolate them merely to make the
band visually continuous.

Missing values may indicate:

Failed experiment

Invalid simulation

Unsafe operating condition

Sensor failure


Investigate first.
"""


# ============================================================
# 81. COMMON MISTAKE - DIFFERENT SAMPLE COUNTS
# ============================================================

"""
If:

n = 30

at one X value

and:

n = 5

at another,


the statistical uncertainty of the mean may differ partly
because of the sample count.


Inspect:

n(x)
"""


# ============================================================
# 82. COMMON MISTAKE - 1.96 FOR EVERY STUDY
# ============================================================

"""
The multiplier:

1.96


is often used with a large-sample normal approximation.

It should NOT be blindly applied to every experiment.


Small samples and more complex experimental designs may
require different statistical methods.
"""


# ============================================================
# 83. COMMON MISTAKE - CORRELATED REPEATED DATA
# ============================================================

"""
If repeated observations are strongly correlated:

The simple:

SEM = SD / sqrt(n)


interpretation may not be appropriate.


Examples:

Time-series autocorrelation

Repeated measurements on the same device

Nested experiments


Experimental structure matters.
"""


# ============================================================
# 84. COMMON MISTAKE - SHADED REGION = PROBABILITY
# ============================================================

"""
A shaded area on a figure does not inherently represent:

Probability.


It only represents whatever numerical boundaries were
provided to:

fill_between()

axhspan()

or

axvspan()


The statistical meaning comes from the calculation.
"""


# ============================================================
# 85. COMMON MISTAKE - TARGET BAND = MEASUREMENT UNCERTAINTY
# ============================================================

"""
A target region such as:

47.5 V to 48.5 V


represents:

Engineering requirement


not automatically:

Measurement uncertainty.
"""


# ============================================================
# 86. COMMON MISTAKE - FREQUENCY BAND = UNCERTAINTY
# ============================================================

"""
A shaded:

1 MHz to 5 MHz


region represents an X-axis operating or analysis range.

It is not an uncertainty band unless explicitly defined
that way.
"""


# ============================================================
# 87. COMMON MISTAKE - LOG AXIS BAND CONFUSION
# ============================================================

"""
On a logarithmic X-axis:

1 kHz to 10 kHz

occupies the same visual decade width as:

1 MHz to 10 MHz.


This is expected.

Do not interpret horizontal visual width using linear
frequency spacing.
"""


# ============================================================
# 88. COMMON MISTAKE - STATISTICAL BAND FROM ONE RUN
# ============================================================

"""
One waveform does not provide repeated-measurement SD
simply because it contains many time samples.

Time samples

are not automatically:

Independent repeated experiments.


Define the source of statistical variability correctly.
"""


# ============================================================
# 89. EXPERIMENTAL WORKFLOW
# ============================================================

"""
Repeated Experiments
        ↓
Align Operating Points
        ↓
Check Data Quality
        ↓
Calculate Mean
        ↓
Calculate SD
        ↓
Calculate SEM if Appropriate
        ↓
Calculate CI if Statistically Appropriate
        ↓
Create Shaded Band
        ↓
State Definition in Legend / Caption
        ↓
Engineering Interpretation
"""


# ============================================================
# 90. MONTE CARLO WORKFLOW
# ============================================================

"""
Parameter Distributions
        ↓
Monte Carlo Runs
        ↓
Response Curves
        ↓
Percentiles
        ↓
Median
        ↓
5th-95th Envelope
        ↓
Robustness Assessment
        ↓
Probability / Risk Analysis
"""


# ============================================================
# 91. OPERATING-REGION WORKFLOW
# ============================================================

"""
Engineering Requirement
        ↓
Define Lower / Upper Limit
        ↓
axhspan()
        ↓
Plot Measured Response
        ↓
Identify Violations
        ↓
fill_between(where=...)
        ↓
Calculate Violation Duration / Range
        ↓
Engineering Interpretation
"""


# ============================================================
# 92. FREQUENCY-BAND WORKFLOW
# ============================================================

"""
Spectrum
        ↓
Select Frequency Region
        ↓
axvspan()
        ↓
Highlight Band
        ↓
Calculate:
Peak
Mean
Energy
Reduction
        ↓
Interpret Selected Frequency Region
"""


# ============================================================
# 93. UNCERTAINTY DECISION GUIDE
# ============================================================

"""
Need variability of observations?
        ↓
STANDARD DEVIATION BAND


Need uncertainty of estimated mean?
        ↓
SEM / CONFIDENCE INTERVAL
with appropriate statistical method


Need distribution range?
        ↓
PERCENTILE BAND


Need complete observed range?
        ↓
MIN-MAX BAND


Need engineering target?
        ↓
axhspan()


Need X-axis operating region?
        ↓
axvspan()


Need conditional positive / negative area?
        ↓
fill_between(
    where=...
)
"""


# ============================================================
# 94. PUBLICATION CHECKLIST
# ============================================================

"""
Before publishing a shaded-band figure, check:


BAND MEANING
------------------------------------------------------------

Does the shading represent:

SD?

SEM?

CI?

Percentiles?

Min-Max?

Measurement uncertainty?

Engineering limits?


STATISTICS
------------------------------------------------------------

Is the statistical calculation appropriate?

What is n?

Are observations independent?

Are missing values present?


CENTER CURVE
------------------------------------------------------------

Mean?

Median?

Prediction?

Simulation?


UNITS
------------------------------------------------------------

Are X and Y units clear?


LEGEND
------------------------------------------------------------

Does it state exactly what the band represents?


MULTIPLE CASES
------------------------------------------------------------

Are overlapping bands readable?

Would separate panels be clearer?


TARGET REGIONS
------------------------------------------------------------

Are engineering limits clearly distinguished from
statistical uncertainty?


FREQUENCY
------------------------------------------------------------

Is the logarithmic axis interpreted correctly?


OUTPUT
------------------------------------------------------------

Is transparency visible in:

PNG?

PDF?

SVG?


FINAL CHECK
------------------------------------------------------------

Can the reader understand the shaded region without
guessing its meaning?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
CONFIDENCE BANDS AND SHADED REGIONS


1. BASIC SHADED BAND

ax.fill_between(

    x,

    lower,

    upper

)


------------------------------------------------------------


2. MEAN ± STANDARD DEVIATION

lower = (

    mean

    - std

)


upper = (

    mean

    + std

)


Represents:

Observation variability


------------------------------------------------------------


3. STANDARD ERROR

sem = (

    std

    / np.sqrt(
        n
    )

)


Represents:

Estimated uncertainty of the mean

under appropriate assumptions.


------------------------------------------------------------


4. APPROXIMATE 95% CI

lower = (

    mean

    - 1.96
    * sem

)


upper = (

    mean

    + 1.96
    * sem

)


This is a common normal approximation,

not a universal formula.


------------------------------------------------------------


5. MIN-MAX ENVELOPE

minimum = np.min(
    repeated_data,
    axis=0
)


maximum = np.max(
    repeated_data,
    axis=0
)


------------------------------------------------------------


6. PERCENTILE BAND

lower = np.percentile(

    data,

    5,

    axis=0

)


upper = np.percentile(

    data,

    95,

    axis=0

)


------------------------------------------------------------


7. MEDIAN

median = np.percentile(

    data,

    50,

    axis=0

)


Especially useful with percentile envelopes.


------------------------------------------------------------


8. NESTED BANDS

Example:

5th-95th Percentile

+
25th-75th Percentile

+
Median


------------------------------------------------------------


9. MONTE CARLO

Monte Carlo Runs
        ↓
Percentiles
        ↓
Shaded Envelope


Useful for:

Robustness

Tolerance analysis

Reliability

Parameter uncertainty


------------------------------------------------------------


10. TARGET REGION

ax.axhspan(

    lower_target,

    upper_target

)


Useful for:

Voltage tolerance

Temperature limits

Efficiency requirements

THD limits


------------------------------------------------------------


11. OPERATING REGION

ax.axvspan(

    x_start,

    x_end

)


Useful for:

Startup

Steady state

Frequency bands

Measurement windows


------------------------------------------------------------


12. CONDITIONAL SHADING

ax.fill_between(

    x,

    lower,

    upper,

    where=condition

)


------------------------------------------------------------


13. ABOVE / BELOW ZERO

condition = (

    difference
    >= 0

)


Useful for showing:

Improvement

vs

Degradation


------------------------------------------------------------


14. INTERPOLATION

fill_between(

    ...,

    where=condition,

    interpolate=True

)


can improve visual boundaries around crossings.


------------------------------------------------------------


15. MISSING VALUES

Use:

np.nanmean()

np.nanstd()

np.nanpercentile()


when missing values are intentionally retained as NaN.


------------------------------------------------------------


16. VARIABLE SAMPLE SIZE

Calculate:

valid_count = np.sum(

    np.isfinite(
        data
    ),

    axis=0

)


when sample counts vary.


------------------------------------------------------------


17. LOGARITHMIC FREQUENCY

fill_between()

can be used normally,

then:

ax.set_xscale(
    "log"
)


------------------------------------------------------------


18. dB DOMAIN

Be clear whether statistics were calculated in:

Linear amplitude

Power

or

dB values.


These are not automatically equivalent.


------------------------------------------------------------


19. SD != SEM

SD:

Observation spread


SEM:

Uncertainty of estimated mean


------------------------------------------------------------


20. CI != PERCENTILE RANGE

Confidence interval:

Uncertainty in an estimated quantity


Percentile envelope:

Distribution of sampled outcomes


------------------------------------------------------------


21. CI != PREDICTION INTERVAL

Confidence interval:

Mean estimate


Prediction interval:

Future individual observation


------------------------------------------------------------


22. TARGET BAND != UNCERTAINTY BAND

Engineering requirement

and

statistical uncertainty

are different concepts.


------------------------------------------------------------


23. SHADED REGION MUST BE DEFINED

Do not label only:

"Band"


Use:

"Mean ± 1 SD"

"Approx. 95% CI"

"5th-95th Percentile"

"Target Range"

"Steady-State Window"


------------------------------------------------------------


24. TRANSPARENCY

Use:

alpha=


to keep underlying data visible.


------------------------------------------------------------


25. MULTIPLE BANDS

Use carefully.

Too many overlapping bands can become unreadable.


------------------------------------------------------------


26. ENGINEERING APPLICATIONS

Useful for:

Repeated experiments

Monte Carlo simulations

Robustness analysis

Prediction uncertainty

Simulation variability

Measurement variability

Voltage tolerance

Temperature limits

EMI frequency bands

Control operating zones

Safe operating areas


------------------------------------------------------------


27. MOST IMPORTANT PRINCIPLE

A shaded region has no statistical meaning by itself.


The meaning comes from:

How the lower bound was calculated

and

How the upper bound was calculated.


Always state exactly what the band represents.


------------------------------------------------------------


28. COMPLETE WORKFLOW

Repeated / Simulated Data
        ↓
Define Statistical Question
        ↓
Calculate Center
        ↓
Calculate Lower Bound
        ↓
Calculate Upper Bound
        ↓
fill_between()
        ↓
Label Band Clearly
        ↓
Add Engineering Limits if Needed
        ↓
Check Sample Size
        ↓
Check Assumptions
        ↓
Engineering Interpretation
        ↓
Publication Figure


------------------------------------------------------------


NEXT:

29_broken_axis_and_discontinuous_ranges.py


The next file will focus on:

Broken axes

Discontinuous Y ranges

Discontinuous X ranges

Outlier-dominated plots

Large dynamic differences

Broken-axis indicators

Two stacked axes

Shared X-axis broken Y ranges

Side-by-side broken X ranges

Engineering examples

When broken axes are justified

When they become misleading

Bar plots with extreme values

Voltage / current examples

Publication formatting

and alternatives such as:

Logarithmic axes

Normalization

Insets

Separate subplots

before choosing a broken axis.
"""
