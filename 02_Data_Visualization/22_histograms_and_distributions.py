"""
============================================================
Python for Engineering and Research
22 - Histograms and Distributions
============================================================

Purpose:
    Demonstrate how histograms and distribution plots can
    be used to investigate repeated measurements, simulated
    populations, engineering variability, and statistical
    behavior using Matplotlib and NumPy.

Topics:
    1. What is a histogram?
    2. Histogram vs line plot
    3. Histogram bins
    4. Number of bins
    5. Automatic bin selection
    6. Custom bin edges
    7. Counts vs probability density
    8. Relative-frequency histograms
    9. Mean and median
    10. Standard deviation
    11. Percentiles
    12. Multiple distributions
    13. Overlapping histograms
    14. Step histograms
    15. Cumulative distributions
    16. Normal-distribution reference curve
    17. Engineering repeated measurements
    18. Comparing several designs
    19. Unequal sample sizes
    20. Outliers
    21. Distribution range
    22. Histogram from CSV
    23. Reusable plotting functions
    24. Saving figures
    25. Common mistakes
    26. Key takeaways

Important:
    A histogram shows the distribution of values.

    It does NOT preserve the original time order or
    sequence of observations.

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

from matplotlib.ticker import PercentFormatter


# ============================================================
# 2. WHAT IS A HISTOGRAM?
# ============================================================

"""
A histogram groups numerical observations into intervals
called:

BINS


Example measurements:

94.8
95.1
95.0
94.9
95.3
95.2
...


The histogram asks:

How many measurements fall between:

94.5 and 95.0?

95.0 and 95.5?

95.5 and 96.0?


This helps reveal the DISTRIBUTION of the data.
"""


# ============================================================
# 3. ENGINEERING APPLICATIONS
# ============================================================

"""
Histograms are useful for:

- Repeated voltage measurements
- Efficiency measurements
- Temperature variation
- Manufacturing tolerances
- Component variation
- Monte Carlo simulation
- Measurement noise
- Power-loss distributions
- Prediction error
- ML residuals
- Reliability studies
- Parameter uncertainty
- Experimental repeatability


Example:

10,000 Monte Carlo converter simulations
        ↓
Efficiency distribution
        ↓
Probability of meeting design target
"""


# ============================================================
# 4. HISTOGRAM VS LINE PLOT
# ============================================================

"""
LINE PLOT

Preserves:

Sequence / X-axis position


Example:

Time
    ↓
Voltage


------------------------------------------------------------


HISTOGRAM

Ignores the original sequence.

Shows:

Frequency of occurrence


Example:

Measured Voltage Values
        ↓
Distribution


The two plots answer different questions.
"""


# ============================================================
# 5. CREATE REPRODUCIBLE ENGINEERING DATA
# ============================================================

"""
Use:

np.random.default_rng()

instead of relying on uncontrolled random values.

A fixed seed makes tutorial results reproducible.
"""


rng = np.random.default_rng(
    42
)


efficiency_measurements = rng.normal(

    loc=95.0,

    scale=0.45,

    size=500

)


print(
    "\n--- Example Measurement Data ---"
)


print(
    efficiency_measurements[:10]
)


print(
    "\nNumber of Measurements:"
)


print(
    len(
        efficiency_measurements
    )
)


# ============================================================
# 6. BASIC HISTOGRAM
# ============================================================

"""
Basic syntax:

ax.hist(
    data
)
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    efficiency_measurements
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)

ax.set_title(
    "Efficiency Measurement Distribution"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 7. WHAT ARE BINS?
# ============================================================

"""
A histogram divides the numerical range into intervals.

Example:

94.0 ───────── 94.5

94.5 ───────── 95.0

95.0 ───────── 95.5

95.5 ───────── 96.0


Each interval is one:

BIN


The height of each bar indicates how many observations
fall inside that interval.
"""


# ============================================================
# 8. SPECIFY NUMBER OF BINS
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    efficiency_measurements,
    bins=15
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)

ax.set_title(
    "Histogram with 15 Bins"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 9. TOO FEW BINS
# ============================================================

"""
Too few bins may hide important structure.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    efficiency_measurements,
    bins=4
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)

ax.set_title(
    "Too Few Bins"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 10. TOO MANY BINS
# ============================================================

"""
Too many bins may make random sample-to-sample variation
look like meaningful structure.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    efficiency_measurements,
    bins=100
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)

ax.set_title(
    "Many Histogram Bins"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 11. BIN SELECTION MATTERS
# ============================================================

"""
Histogram appearance depends on:

- Number of bins
- Bin width
- Bin edges


Therefore:

Do not interpret every small histogram feature as a real
physical phenomenon.

Check whether conclusions remain reasonable when the
binning method changes.
"""


# ============================================================
# 12. AUTOMATIC BIN SELECTION
# ============================================================

"""
NumPy / Matplotlib support automatic bin rules.

Examples:

bins="auto"

bins="fd"

bins="sturges"

bins="sqrt"


"fd"

uses the Freedman-Diaconis approach.


"sturges"

is a classical rule based mainly on sample size.


No single method is best for every dataset.
"""


automatic_bin_methods = [

    "auto",

    "fd",

    "sturges",

    "sqrt"

]


for method in automatic_bin_methods:

    edges = np.histogram_bin_edges(

        efficiency_measurements,

        bins=method

    )


    print(
        f"\n{method}:"
    )


    print(
        "Number of Bins =",
        len(
            edges
        )
        - 1
    )


# ============================================================
# 13. HISTOGRAM USING bins="auto"
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    efficiency_measurements,
    bins="auto"
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)

ax.set_title(
    "Automatic Histogram Binning"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 14. FREEDMAN-DIACONIS BINNING
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    efficiency_measurements,
    bins="fd"
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)

ax.set_title(
    "Freedman-Diaconis Binning"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 15. CUSTOM BIN EDGES
# ============================================================

"""
Bins can be defined explicitly.

Example:

94.0

94.25

94.50

94.75

95.00

...
"""


custom_bin_edges = np.arange(

    93.0,

    97.25,

    0.25

)


print(
    "\n--- Custom Bin Edges ---"
)


print(
    custom_bin_edges
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    efficiency_measurements,
    bins=custom_bin_edges
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 16. WHY CUSTOM BIN EDGES CAN BE USEFUL
# ============================================================

"""
Custom bin edges are useful when:

- Engineering thresholds are known
- Fixed intervals must be compared
- Several datasets must use identical bins
- Reporting standards specify intervals


Example:

Temperature:

20-30 °C

30-40 °C

40-50 °C

50-60 °C
"""


# ============================================================
# 17. HISTOGRAM COUNTS
# ============================================================

"""
Default histogram:

density=False


Y-axis:

COUNT


Example:

One bar height = 74


means:

74 observations fell into that bin.
"""


counts, bin_edges = np.histogram(

    efficiency_measurements,

    bins=15

)


print(
    "\n--- Histogram Counts ---"
)


print(
    counts
)


print(
    "\n--- Bin Edges ---"
)


print(
    bin_edges
)


# ============================================================
# 18. PROBABILITY DENSITY
# ============================================================

"""
Use:

density=True


to normalize the histogram so that the TOTAL AREA under
the histogram equals approximately:

1


Important:

Density is NOT the same as:

Percentage of samples in each bin.


The Y-axis represents:

Probability Density


Its units are approximately:

1 / unit of X
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    efficiency_measurements,
    bins="auto",
    density=True
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Probability Density"
)

ax.set_title(
    "Normalized Probability Density"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 19. RELATIVE-FREQUENCY HISTOGRAM
# ============================================================

"""
Sometimes the desired Y-axis is:

Percentage of observations


rather than:

Count

or

Probability density.


Weights can be used.
"""


weights = (

    np.ones_like(
        efficiency_measurements
    )

    / len(
        efficiency_measurements
    )

)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(

    efficiency_measurements,

    bins=15,

    weights=weights

)


ax.yaxis.set_major_formatter(
    PercentFormatter(
        1.0
    )
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Percentage of Measurements"
)

ax.set_title(
    "Relative-Frequency Histogram"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 20. COUNT VS DENSITY VS PERCENTAGE
# ============================================================

"""
COUNT

Question:

How many observations are in each bin?


------------------------------------------------------------


DENSITY

Question:

What is the estimated probability density?


Total histogram area:

≈ 1


------------------------------------------------------------


PERCENTAGE

Question:

What percentage of observations fall into each bin?


The three Y-axis meanings are different.
"""


# ============================================================
# 21. CALCULATE MEAN
# ============================================================

mean_efficiency = np.mean(
    efficiency_measurements
)


print(
    "\nMean Efficiency:"
)


print(
    f"{mean_efficiency:.4f}%"
)


# ============================================================
# 22. CALCULATE MEDIAN
# ============================================================

median_efficiency = np.median(
    efficiency_measurements
)


print(
    "\nMedian Efficiency:"
)


print(
    f"{median_efficiency:.4f}%"
)


# ============================================================
# 23. SAMPLE STANDARD DEVIATION
# ============================================================

standard_deviation = np.std(

    efficiency_measurements,

    ddof=1

)


print(
    "\nSample Standard Deviation:"
)


print(
    f"{standard_deviation:.4f}"
)


# ============================================================
# 24. MEAN AND MEDIAN ON HISTOGRAM
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    efficiency_measurements,
    bins="auto",
    alpha=0.75
)


ax.axvline(

    mean_efficiency,

    linestyle="--",

    linewidth=2,

    label=(
        f"Mean = "
        f"{mean_efficiency:.2f}%"
    )

)


ax.axvline(

    median_efficiency,

    linestyle="-.",

    linewidth=2,

    label=(
        f"Median = "
        f"{median_efficiency:.2f}%"
    )

)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)


ax.legend()


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 25. WHY MEAN AND MEDIAN BOTH MATTER
# ============================================================

"""
For a reasonably symmetric distribution:

Mean

and

Median

may be similar.


For strongly skewed data or data containing outliers,
they may differ significantly.


Therefore the median can provide useful additional
information.
"""


# ============================================================
# 26. PERCENTILES
# ============================================================

"""
Percentiles describe locations in the distribution.

Example:

5th percentile

50th percentile

95th percentile
"""


percentile_5 = np.percentile(

    efficiency_measurements,

    5

)


percentile_50 = np.percentile(

    efficiency_measurements,

    50

)


percentile_95 = np.percentile(

    efficiency_measurements,

    95

)


print(
    "\n--- Percentiles ---"
)


print(
    f"5th Percentile = "
    f"{percentile_5:.3f}%"
)


print(
    f"50th Percentile = "
    f"{percentile_50:.3f}%"
)


print(
    f"95th Percentile = "
    f"{percentile_95:.3f}%"
)


# ============================================================
# 27. PERCENTILES ON HISTOGRAM
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    efficiency_measurements,
    bins="auto"
)


ax.axvline(
    percentile_5,
    linestyle="--",
    label="5th Percentile"
)


ax.axvline(
    percentile_50,
    linestyle="-.",
    label="Median"
)


ax.axvline(
    percentile_95,
    linestyle="--",
    label="95th Percentile"
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)


ax.legend()


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 28. INTERQUARTILE RANGE
# ============================================================

"""
Quartiles:

Q1 = 25th percentile

Q2 = 50th percentile / median

Q3 = 75th percentile


Interquartile Range:

IQR = Q3 - Q1


IQR describes the spread of the central 50% of the data.
"""


q1 = np.percentile(

    efficiency_measurements,

    25

)


q3 = np.percentile(

    efficiency_measurements,

    75

)


iqr = (

    q3

    - q1

)


print(
    "\n--- Quartile Statistics ---"
)


print(
    f"Q1 = {q1:.3f}%"
)


print(
    f"Q3 = {q3:.3f}%"
)


print(
    f"IQR = {iqr:.3f}"
)


# ============================================================
# 29. NORMAL-DISTRIBUTION REFERENCE CURVE
# ============================================================

"""
If the histogram is displayed using:

density=True


a theoretical normal probability-density curve can be
overlaid for visual comparison.

Important:

This is only a visual comparison.

It is NOT a formal statistical normality test.
"""


x_normal = np.linspace(

    efficiency_measurements.min(),

    efficiency_measurements.max(),

    400

)


normal_pdf = (

    1

    / (
        standard_deviation
        * np.sqrt(
            2
            * np.pi
        )
    )

    * np.exp(
        -0.5
        * (
            (
                x_normal
                - mean_efficiency
            )

            / standard_deviation
        ) ** 2
    )

)


# ============================================================
# 30. HISTOGRAM + NORMAL REFERENCE
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(

    efficiency_measurements,

    bins="auto",

    density=True,

    alpha=0.65,

    label="Measurements"

)


ax.plot(

    x_normal,

    normal_pdf,

    linewidth=2,

    label="Normal Reference"

)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Probability Density"
)

ax.set_title(
    "Measurement Distribution"
)


ax.legend()


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 31. IMPORTANT NORMALITY WARNING
# ============================================================

"""
A histogram that LOOKS approximately bell-shaped does not
prove that the data follow a normal distribution.

Likewise:

A histogram that looks irregular may result from:

- Small sample size
- Poor bin selection
- Outliers
- Mixed operating conditions


Formal distribution testing belongs to statistical
analysis rather than visual inspection alone.
"""


# ============================================================
# 32. MULTIPLE ENGINEERING DESIGNS
# ============================================================

"""
Now create three example engineering cases.
"""


baseline_measurements = rng.normal(

    loc=94.5,

    scale=0.55,

    size=600

)


design_a_measurements = rng.normal(

    loc=95.1,

    scale=0.40,

    size=600

)


design_b_measurements = rng.normal(

    loc=95.5,

    scale=0.30,

    size=600

)


# ============================================================
# 33. COMPARE MULTIPLE HISTOGRAMS
# ============================================================

"""
When comparing distributions, use the SAME bin edges.

Otherwise visual comparison may be misleading.
"""


all_measurements = np.concatenate(
    [
        baseline_measurements,
        design_a_measurements,
        design_b_measurements
    ]
)


shared_bins = np.histogram_bin_edges(

    all_measurements,

    bins=20

)


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.hist(

    baseline_measurements,

    bins=shared_bins,

    alpha=0.45,

    label="Baseline"

)


ax.hist(

    design_a_measurements,

    bins=shared_bins,

    alpha=0.45,

    label="Design A"

)


ax.hist(

    design_b_measurements,

    bins=shared_bins,

    alpha=0.45,

    label="Design B"

)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)

ax.set_title(
    "Distribution Comparison"
)


ax.legend()


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 34. OVERLAPPING HISTOGRAM LIMITATION
# ============================================================

"""
Overlapping filled histograms may become difficult to read
when many cases are shown.

Possible alternatives:

- Step histograms
- Separate subplots
- Box plots
- Violin plots


Box and violin plots will be covered in the next tutorial.
"""


# ============================================================
# 35. STEP HISTOGRAM
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.hist(

    baseline_measurements,

    bins=shared_bins,

    histtype="step",

    linewidth=2,

    label="Baseline"

)


ax.hist(

    design_a_measurements,

    bins=shared_bins,

    histtype="step",

    linewidth=2,

    label="Design A"

)


ax.hist(

    design_b_measurements,

    bins=shared_bins,

    histtype="step",

    linewidth=2,

    label="Design B"

)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)


ax.legend()


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 36. DENSITY COMPARISON
# ============================================================

"""
density=True is especially useful when datasets contain
different numbers of observations.

It allows distribution SHAPE to be compared without raw
sample count dominating the histogram height.
"""


baseline_unequal = rng.normal(

    loc=94.5,

    scale=0.55,

    size=300

)


design_unequal = rng.normal(

    loc=95.2,

    scale=0.40,

    size=1200

)


combined_unequal = np.concatenate(
    [
        baseline_unequal,
        design_unequal
    ]
)


unequal_bins = np.histogram_bin_edges(

    combined_unequal,

    bins="auto"

)


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.hist(

    baseline_unequal,

    bins=unequal_bins,

    density=True,

    histtype="step",

    linewidth=2,

    label=(
        f"Baseline "
        f"(n={len(baseline_unequal)})"
    )

)


ax.hist(

    design_unequal,

    bins=unequal_bins,

    density=True,

    histtype="step",

    linewidth=2,

    label=(
        f"Design "
        f"(n={len(design_unequal)})"
    )

)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Probability Density"
)


ax.legend()


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 37. UNEQUAL SAMPLE-SIZE WARNING
# ============================================================

"""
If:

Dataset A contains:

100 measurements


and:

Dataset B contains:

10,000 measurements


a raw COUNT histogram may naturally be much taller for
Dataset B.

That does NOT automatically mean Dataset B has:

More variability

or

Higher probability.


Use an appropriate normalization when comparing
distribution shapes.
"""


# ============================================================
# 38. CUMULATIVE HISTOGRAM
# ============================================================

"""
A cumulative histogram answers questions such as:

What fraction of measurements are less than or equal to
a selected value?


Use:

cumulative=True
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(

    efficiency_measurements,

    bins=30,

    density=True,

    cumulative=True,

    histtype="step",

    linewidth=2

)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Cumulative Fraction"
)

ax.set_title(
    "Cumulative Efficiency Distribution"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show())


# ============================================================
# 39. CUMULATIVE PERCENTAGE
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(

    efficiency_measurements,

    bins=30,

    weights=(
        np.ones_like(
            efficiency_measurements
        )

        / len(
            efficiency_measurements
        )
    ),

    cumulative=True,

    histtype="step",

    linewidth=2

)


ax.yaxis.set_major_formatter(
    PercentFormatter(
        1.0
    )
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Cumulative Percentage"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show())


# ============================================================
# 40. ENGINEERING TARGET PROBABILITY
# ============================================================

"""
Suppose the design requirement is:

Efficiency >= 94.5%


We can calculate the percentage of samples meeting the
target directly from the data.
"""


efficiency_target = 94.5


samples_meeting_target = (

    efficiency_measurements

    >= efficiency_target

)


target_probability = (

    samples_meeting_target.mean()

    * 100

)


print(
    "\n--- Engineering Target ---"
)


print(
    f"Target Efficiency >= "
    f"{efficiency_target:.2f}%"
)


print(
    f"Samples Meeting Target = "
    f"{target_probability:.2f}%"
)


# ============================================================
# 41. HISTOGRAM WITH ENGINEERING TARGET
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    efficiency_measurements,
    bins="auto",
    alpha=0.75
)


ax.axvline(

    efficiency_target,

    linestyle="--",

    linewidth=2,

    label=(
        f"Target = "
        f"{efficiency_target:.1f}%"
    )

)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)


ax.legend()


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 42. DISTRIBUTION SUMMARY FOR MULTIPLE CASES
# ============================================================

engineering_cases = {

    "Baseline":
        baseline_measurements,

    "Design A":
        design_a_measurements,

    "Design B":
        design_b_measurements

}


distribution_summary = []


for case_name, values in engineering_cases.items():

    distribution_summary.append(
        {
            "Case":
                case_name,

            "Samples":
                len(
                    values
                ),

            "Mean":
                np.mean(
                    values
                ),

            "Median":
                np.median(
                    values
                ),

            "Standard_Deviation":
                np.std(
                    values,
                    ddof=1
                ),

            "Minimum":
                np.min(
                    values
                ),

            "Maximum":
                np.max(
                    values
                ),

            "5th_Percentile":
                np.percentile(
                    values,
                    5
                ),

            "95th_Percentile":
                np.percentile(
                    values,
                    95
                )
        }
    )


distribution_summary = pd.DataFrame(
    distribution_summary
)


print(
    "\n--- Distribution Summary ---"
)


print(
    distribution_summary
)


# ============================================================
# 43. DISTRIBUTION SUMMARY BAR PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(

    distribution_summary[
        "Case"
    ],

    distribution_summary[
        "Mean"
    ],

    yerr=distribution_summary[
        "Standard_Deviation"
    ],

    capsize=5

)


ax.bar_label(
    bars,
    fmt="%.2f",
    padding=4
)


ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Mean ± 1 Standard Deviation"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 44. DISTRIBUTION VS MEAN ± SD
# ============================================================

"""
Mean ± standard deviation summarizes the dataset.

Histogram shows much more about:

- Shape
- Multiple modes
- Asymmetry
- Outliers
- Tails


Therefore:

Summary statistics

and

distribution plots

are complementary.
"""


# ============================================================
# 45. OUTLIER EXAMPLE
# ============================================================

measurements_with_outliers = np.concatenate(
    [
        efficiency_measurements,

        np.array(
            [
                91.5,
                91.8,
                98.2
            ]
        )
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    measurements_with_outliers,
    bins="auto"
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)

ax.set_title(
    "Distribution Containing Outliers"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 46. IQR OUTLIER RULE
# ============================================================

"""
A common descriptive rule identifies potential outliers
outside:

Q1 - 1.5 × IQR

and

Q3 + 1.5 × IQR


This is a statistical screening rule.

It does NOT automatically mean such observations should
be deleted.
"""


q1_outlier = np.percentile(

    measurements_with_outliers,

    25

)


q3_outlier = np.percentile(

    measurements_with_outliers,

    75

)


iqr_outlier = (

    q3_outlier

    - q1_outlier

)


lower_outlier_limit = (

    q1_outlier

    - 1.5
    * iqr_outlier

)


upper_outlier_limit = (

    q3_outlier

    + 1.5
    * iqr_outlier

)


potential_outliers = measurements_with_outliers[
    (
        measurements_with_outliers
        < lower_outlier_limit
    )
    |
    (
        measurements_with_outliers
        > upper_outlier_limit
    )
]


print(
    "\n--- Potential Outliers ---"
)


print(
    potential_outliers
)


# ============================================================
# 47. NEVER DELETE OUTLIERS AUTOMATICALLY
# ============================================================

"""
Potential outliers may result from:

- Measurement error
- Sensor failure
- Data-entry error
- Real rare behavior
- Physical transient
- Process instability


Do not automatically delete them simply because they are
statistically unusual.

Investigate the engineering reason first.
"""


# ============================================================
# 48. HISTOGRAM RANGE
# ============================================================

"""
Matplotlib supports:

range=(minimum, maximum)


Example:

Only display data between:

94% and 96%
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(

    efficiency_measurements,

    bins=15,

    range=(
        94,
        96
    )

)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 49. RANGE WARNING
# ============================================================

"""
Using:

range=(94, 96)


excludes observations outside that range from the
histogram calculation.

This is different from:

ax.set_xlim(
    94,
    96
)


which only changes what is visible.


This is the same general distinction discussed earlier:

DATA SELECTION

vs

VISUAL ZOOMING
"""


# ============================================================
# 50. VISUAL ZOOM ONLY
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    efficiency_measurements,
    bins="auto"
)


ax.set_xlim(
    94,
    96
)


ax.set_xlabel(
    "Efficiency [%]"
)

ax.set_ylabel(
    "Count"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 51. LOGARITHMIC Y-AXIS
# ============================================================

"""
For distributions containing very rare events, a
logarithmic count axis can sometimes reveal low-frequency
bins.

Use carefully:

ax.set_yscale(
    "log"
)


This changes the visual representation of counts.
"""


rare_event_data = np.concatenate(
    [
        rng.normal(
            0,
            1,
            5000
        ),

        rng.normal(
            6,
            0.5,
            20
        )
    ]
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    rare_event_data,
    bins=60
)


ax.set_yscale(
    "log"
)


ax.set_xlabel(
    "Measured Value [-]"
)

ax.set_ylabel(
    "Count"
)

ax.set_title(
    "Histogram with Logarithmic Count Axis"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 52. LOG HISTOGRAM WARNING
# ============================================================

"""
Use a logarithmic count axis only when it supports the
analysis.

Equal vertical distances no longer represent equal count
differences.

Do not use log scaling merely to make rare bins appear
larger.
"""


# ============================================================
# 53. HISTOGRAM FROM CSV
# ============================================================

"""
Now connect histograms to the existing sample-data folder.

Sample file:

voltage_current.csv


Expected columns:

Time_s

Voltage_V

Current_A

Power_W
"""


csv_file = (
    script_folder
    / "sample_data"
    / "voltage_current.csv"
)


if not csv_file.exists():

    raise FileNotFoundError(
        f"\nSample file not found:\n"
        f"{csv_file}"
    )


csv_data = pd.read_csv(
    csv_file
)


print(
    "\n--- CSV Columns ---"
)


print(
    csv_data.columns.tolist()
)


# ============================================================
# 54. CHECK REQUIRED CSV COLUMN
# ============================================================

required_column = "Power_W"


if required_column not in csv_data.columns:

    raise KeyError(
        f"Required column not found: "
        f"{required_column}"
    )


power_values = pd.to_numeric(

    csv_data[
        required_column
    ],

    errors="coerce"

).dropna()


# ============================================================
# 55. HISTOGRAM FROM CSV COLUMN
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.hist(
    power_values,
    bins="auto"
)


ax.set_xlabel(
    "Power [W]"
)

ax.set_ylabel(
    "Count"
)

ax.set_title(
    "Distribution of Power Samples from CSV"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show())


# ============================================================
# 56. TIME-SERIES DISTRIBUTION WARNING
# ============================================================

"""
The CSV example contains samples from a time-domain
dataset.

A histogram of these samples describes:

How frequently different power values occur.


It does NOT automatically describe:

Repeated-measurement uncertainty.


For uncertainty analysis, the observations should come
from an appropriate repeated-measurement or statistical
sampling process.
"""


# ============================================================
# 57. HISTOGRAM FUNCTION
# ============================================================

def plot_histogram(
    data,
    x_label,
    title=None,
    bins="auto",
    density=False,
    mean_line=True,
    median_line=False
):
    """
    Create a reusable histogram.

    Parameters
    ----------
    data : array-like
        Numerical observations.

    x_label : str
        X-axis label including unit.

    title : str, optional
        Figure title.

    bins : int, str, or array-like
        Histogram bin definition.

    density : bool
        If True, show probability density.

    mean_line : bool
        Display mean reference line.

    median_line : bool
        Display median reference line.

    Returns
    -------
    fig, ax
        Matplotlib figure and axis.
    """

    values = np.asarray(
        data,
        dtype=float
    )


    values = values[
        np.isfinite(
            values
        )
    ]


    if len(
        values
    ) == 0:

        raise ValueError(
            "No valid numerical data "
            "available for histogram."
        )


    fig, ax = plt.subplots(
        figsize=(7, 4.5)
    )


    ax.hist(

        values,

        bins=bins,

        density=density,

        alpha=0.75

    )


    if mean_line:

        mean_value = np.mean(
            values
        )


        ax.axvline(

            mean_value,

            linestyle="--",

            linewidth=2,

            label=(
                f"Mean = "
                f"{mean_value:.3g}"
            )

        )


    if median_line:

        median_value = np.median(
            values
        )


        ax.axvline(

            median_value,

            linestyle="-.",

            linewidth=2,

            label=(
                f"Median = "
                f"{median_value:.3g}"
            )

        )


    ax.set_xlabel(
        x_label
    )


    if density:

        ax.set_ylabel(
            "Probability Density"
        )

    else:

        ax.set_ylabel(
            "Count"
        )


    if title is not None:

        ax.set_title(
            title
        )


    if (
        mean_line
        or median_line
    ):

        ax.legend()


    ax.grid(
        True,
        axis="y"
    )


    plt.tight_layout()


    return (
        fig,
        ax
    )


# ============================================================
# 58. USE HISTOGRAM FUNCTION
# ============================================================

fig, ax = plot_histogram(

    data=efficiency_measurements,

    x_label="Efficiency [%]",

    title="Repeated Efficiency Measurements",

    bins="fd",

    density=False,

    mean_line=True,

    median_line=True

)


plt.show())


# ============================================================
# 59. MULTIPLE-DISTRIBUTION FUNCTION
# ============================================================

def plot_distribution_comparison(
    datasets,
    x_label,
    bins="auto",
    density=True,
    title=None
):
    """
    Compare multiple distributions using common bin edges.

    Parameters
    ----------
    datasets : dict
        Mapping:
        display label -> numerical observations

    x_label : str
        X-axis label.

    bins : int or str
        Bin specification.

    density : bool
        Normalize distribution if True.

    title : str, optional
        Plot title.

    Returns
    -------
    fig, ax
        Matplotlib figure and axis.
    """

    if not datasets:

        raise ValueError(
            "At least one dataset is required."
        )


    cleaned_datasets = {}


    for case_name, values in datasets.items():

        values = np.asarray(
            values,
            dtype=float
        )


        values = values[
            np.isfinite(
                values
            )
        ]


        if len(
            values
        ) == 0:

            raise ValueError(
                f"No valid data for "
                f"{case_name}."
            )


        cleaned_datasets[
            case_name
        ] = values


    combined_values = np.concatenate(
        list(
            cleaned_datasets.values()
        )
    )


    common_bins = np.histogram_bin_edges(

        combined_values,

        bins=bins

    )


    fig, ax = plt.subplots(
        figsize=(8, 4.8)
    )


    line_styles = [

        "-",

        "--",

        "-.",

        ":"

    ]


    for index, (
        case_name,
        values
    ) in enumerate(
        cleaned_datasets.items()
    ):

        ax.hist(

            values,

            bins=common_bins,

            density=density,

            histtype="step",

            linewidth=2,

            linestyle=line_styles[
                index
                % len(
                    line_styles
                )
            ],

            label=(
                f"{case_name} "
                f"(n={len(values)})"
            )

        )


    ax.set_xlabel(
        x_label
    )


    if density:

        ax.set_ylabel(
            "Probability Density"
        )

    else:

        ax.set_ylabel(
            "Count"
        )


    if title is not None:

        ax.set_title(
            title
        )


    ax.legend()


    ax.grid(
        True,
        axis="y"
    )


    plt.tight_layout()


    return (
        fig,
        ax
    )


# ============================================================
# 60. USE DISTRIBUTION COMPARISON FUNCTION
# ============================================================

fig, ax = plot_distribution_comparison(

    datasets=engineering_cases,

    x_label="Efficiency [%]",

    bins="fd",

    density=True,

    title="Engineering Design Distributions"

)


plt.show())


# ============================================================
# 61. REUSABLE DISTRIBUTION SUMMARY FUNCTION
# ============================================================

def summarize_distribution(
    values
):
    """
    Calculate common descriptive statistics.

    Returns
    -------
    dict
        Distribution summary.
    """

    values = np.asarray(
        values,
        dtype=float
    )


    values = values[
        np.isfinite(
            values
        )
    ]


    if len(
        values
    ) == 0:

        raise ValueError(
            "No valid numerical values."
        )


    sample_std = (

        np.std(
            values,
            ddof=1
        )

        if len(
            values
        ) > 1

        else np.nan

    )


    return {
        "Samples":
            len(
                values
            ),

        "Mean":
            np.mean(
                values
            ),

        "Median":
            np.median(
                values
            ),

        "Standard_Deviation":
            sample_std,

        "Minimum":
            np.min(
                values
            ),

        "Maximum":
            np.max(
                values
            ),

        "Q1":
            np.percentile(
                values,
                25
            ),

        "Q3":
            np.percentile(
                values,
                75
            ),

        "5th_Percentile":
            np.percentile(
                values,
                5
            ),

        "95th_Percentile":
            np.percentile(
                values,
                95
            )
    }


# ============================================================
# 62. USE SUMMARY FUNCTION
# ============================================================

summary = summarize_distribution(
    efficiency_measurements
)


print(
    "\n--- Reusable Distribution Summary ---"
)


for key, value in summary.items():

    print(
        key,
        "=",
        value
    )


# ============================================================
# 63. SAVE OUTPUT FOLDER
# ============================================================

output_figure_folder = (
    script_folder
    / "output_figures"
    / "distributions"
)


output_figure_folder.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 64. FINAL ENGINEERING DISTRIBUTION FIGURE
# ============================================================

fig, ax = plot_distribution_comparison(

    datasets=engineering_cases,

    x_label="Efficiency [%]",

    bins="fd",

    density=True,

    title="Efficiency Distribution Comparison"

)


# ============================================================
# 65. SAVE PNG
# ============================================================

png_file = (
    output_figure_folder
    / "engineering_distribution_comparison.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 66. SAVE PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "engineering_distribution_comparison.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 67. SAVE SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "engineering_distribution_comparison.svg"
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


plt.show())


# ============================================================
# 68. SAVE DISTRIBUTION SUMMARY
# ============================================================

summary_output_file = (
    script_folder
    / "output_data"
    / "distribution_summary.csv"
)


summary_output_file.parent.mkdir(
    parents=True,
    exist_ok=True
)


distribution_summary.to_csv(
    summary_output_file,
    index=False
)


print(
    "\nDistribution summary saved:"
)


print(
    summary_output_file
)


# ============================================================
# 69. COMMON MISTAKE - TOO FEW BINS
# ============================================================

"""
Too few bins may hide:

- Multiple populations
- Tails
- Asymmetry
- Outliers
"""


# ============================================================
# 70. COMMON MISTAKE - TOO MANY BINS
# ============================================================

"""
Too many bins may make random sampling noise look like
real distribution structure.
"""


# ============================================================
# 71. COMMON MISTAKE - DIFFERENT BINS FOR CASES
# ============================================================

"""
When comparing:

Baseline

Design A

Design B


using different bin edges for every case may create an
unfair visual comparison.

Prefer common bins.
"""


# ============================================================
# 72. COMMON MISTAKE - COUNT COMPARISON WITH UNEQUAL n
# ============================================================

"""
Dataset A:

n = 100


Dataset B:

n = 10,000


Dataset B will naturally produce larger counts.

Use:

density=True

or

relative-frequency normalization

when comparing distribution shapes.
"""


# ============================================================
# 73. COMMON MISTAKE - DENSITY CALLED PERCENTAGE
# ============================================================

"""
density=True

does NOT automatically mean:

Percentage


The Y-axis represents:

Probability Density


Use explicit weights if percentage per bin is required.
"""


# ============================================================
# 74. COMMON MISTAKE - NORMAL CURVE ON COUNT HISTOGRAM
# ============================================================

"""
A theoretical probability-density curve should normally
be compared with:

density=True


If the histogram Y-axis contains raw counts, the scales
do not directly match.
"""


# ============================================================
# 75. COMMON MISTAKE - HISTOGRAM AS TIME RESPONSE
# ============================================================

"""
Histogram:

Does not preserve time order.


If the research question is:

When did the transient occur?


use:

Time-domain plot


not only:

Histogram.
"""


# ============================================================
# 76. COMMON MISTAKE - IGNORING SAMPLE SIZE
# ============================================================

"""
A histogram generated from:

n = 10


is much less informative about distribution shape than:

n = 10,000


Always consider the sample size.
"""


# ============================================================
# 77. COMMON MISTAKE - ASSUMING NORMALITY
# ============================================================

"""
Do not conclude:

"The data are normally distributed"


only because the histogram looks roughly bell-shaped.

Formal statistical tests and physical understanding may
be required.
"""


# ============================================================
# 78. COMMON MISTAKE - AUTOMATIC OUTLIER DELETION
# ============================================================

"""
An unusual value is not automatically an invalid value.

Investigate:

Measurement setup

Sensor behavior

Physical mechanism

Data processing

before removing observations.
"""


# ============================================================
# 79. COMMON MISTAKE - HISTOGRAM RANGE HIDES DATA
# ============================================================

"""
Using:

range=(94, 96)


removes observations outside that interval from the
histogram calculation.

This can hide important tails or outliers.


Use carefully and report the selected range when relevant.
"""


# ============================================================
# 80. COMMON MISTAKE - CHERRY-PICKING BIN WIDTH
# ============================================================

"""
Changing the bins until a desired pattern appears can
produce misleading conclusions.

Choose bins using:

- A documented rule
- Common bin edges
- Engineering thresholds
- A justified fixed interval
"""


# ============================================================
# 81. COMMON MISTAKE - MEAN ONLY
# ============================================================

"""
Two datasets can have nearly identical means but very
different distributions.

Example:

Case A:

Mean = 95%
SD = 0.2%


Case B:

Mean = 95%
SD = 2.0%


The mean alone hides important variability.
"""


# ============================================================
# 82. COMMON MISTAKE - DISTRIBUTION ONLY
# ============================================================

"""
Likewise, a histogram without summary values may make
precise engineering comparison difficult.

Useful combination:

Histogram
+
Mean
+
Median
+
Standard deviation
+
Percentiles
"""


# ============================================================
# 83. ENGINEERING DISTRIBUTION WORKFLOW
# ============================================================

"""
Repeated Measurements / Simulations
              ↓
Check Data Quality
              ↓
Check Units
              ↓
Check Sample Size
              ↓
Select Common Bins
              ↓
Plot Histogram
              ↓
Calculate Mean
              ↓
Calculate Median
              ↓
Calculate Standard Deviation
              ↓
Calculate Percentiles
              ↓
Check Outliers
              ↓
Compare Cases
              ↓
Check Engineering Target
              ↓
Interpret Distribution
"""


# ============================================================
# 84. MONTE CARLO WORKFLOW
# ============================================================

"""
Parameter Variation
        ↓
Monte Carlo Simulation
        ↓
Thousands of Results
        ↓
Histogram
        ↓
Mean / Spread
        ↓
Percentiles
        ↓
Target Probability
        ↓
Risk / Robustness Assessment
"""


# ============================================================
# 85. EXPERIMENTAL WORKFLOW
# ============================================================

"""
Repeated Experiment
        ↓
Measurement 1
Measurement 2
Measurement 3
...
Measurement n
        ↓
Histogram
        ↓
Distribution Shape
        ↓
Mean
Median
SD
Percentiles
        ↓
Repeatability Interpretation
"""


# ============================================================
# 86. HISTOGRAM DECISION GUIDE
# ============================================================

"""
Need to show signal versus time?
        ↓
LINE PLOT


Need to show relationship between X and Y?
        ↓
SCATTER PLOT


Need to show category magnitudes?
        ↓
BAR PLOT


Need to show distribution of numerical observations?
        ↓
HISTOGRAM


Need compact comparison of quartiles/outliers?
        ↓
BOX PLOT


Need distribution shape + density comparison?
        ↓
VIOLIN PLOT
"""


# ============================================================
# 87. PUBLICATION CHECKLIST
# ============================================================

"""
Before publishing a histogram, check:

What does each observation represent?

What is the sample size?

Are units shown?

How were bins selected?

Are all cases using common bins?

Does Y represent:

Count?

Density?

Percentage?

Are mean / median lines identified?

Are outliers visible?

Was the plotted range restricted?

Are distributions being compared fairly?

Does the caption explain the dataset?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
HISTOGRAMS AND DISTRIBUTIONS


1. BASIC HISTOGRAM

ax.hist(
    data
)


------------------------------------------------------------


2. NUMBER OF BINS

ax.hist(

    data,

    bins=20

)


------------------------------------------------------------


3. AUTOMATIC BINNING

ax.hist(

    data,

    bins="auto"

)


Other options include:

"fd"

"sturges"

"sqrt"


------------------------------------------------------------


4. CUSTOM BIN EDGES

bins = np.arange(

    minimum,

    maximum,

    step

)


ax.hist(

    data,

    bins=bins

)


------------------------------------------------------------


5. HISTOGRAM COUNTS

Default:

density=False


Y-axis:

Count


------------------------------------------------------------


6. PROBABILITY DENSITY

ax.hist(

    data,

    density=True

)


Total histogram area:

approximately 1


------------------------------------------------------------


7. RELATIVE FREQUENCY

weights = (

    np.ones_like(
        data
    )

    / len(
        data
    )

)


ax.hist(

    data,

    weights=weights

)


------------------------------------------------------------


8. MEAN

mean = np.mean(
    data
)


------------------------------------------------------------


9. MEDIAN

median = np.median(
    data
)


------------------------------------------------------------


10. SAMPLE STANDARD DEVIATION

std = np.std(

    data,

    ddof=1

)


------------------------------------------------------------


11. PERCENTILES

p5 = np.percentile(
    data,
    5
)


p95 = np.percentile(
    data,
    95
)


------------------------------------------------------------


12. INTERQUARTILE RANGE

q1 = np.percentile(
    data,
    25
)


q3 = np.percentile(
    data,
    75
)


iqr = q3 - q1


------------------------------------------------------------


13. MEAN REFERENCE LINE

ax.axvline(

    mean,

    linestyle="--"

)


------------------------------------------------------------


14. MULTIPLE DISTRIBUTIONS

Use:

Common bin edges


for fair comparison.


------------------------------------------------------------


15. STEP HISTOGRAM

ax.hist(

    data,

    histtype="step"

)


Useful when several distributions overlap.


------------------------------------------------------------


16. UNEQUAL SAMPLE SIZES

For distribution-shape comparison:

density=True


can be more appropriate than raw counts.


------------------------------------------------------------


17. CUMULATIVE HISTOGRAM

ax.hist(

    data,

    cumulative=True

)


------------------------------------------------------------


18. ENGINEERING TARGET

probability = (

    data
    >= target

).mean() * 100


------------------------------------------------------------


19. OUTLIERS

IQR screening:

Lower Limit

=

Q1 - 1.5 × IQR


Upper Limit

=

Q3 + 1.5 × IQR


Do NOT automatically delete identified points.


------------------------------------------------------------


20. NORMAL DISTRIBUTION OVERLAY

Use:

density=True


when comparing against a theoretical probability-density
curve.


------------------------------------------------------------


21. HISTOGRAM DOES NOT SHOW TIME ORDER

Histogram:

Distribution


Line plot:

Sequence / time response


------------------------------------------------------------


22. COUNT != DENSITY != PERCENTAGE

Always label the Y-axis correctly.


------------------------------------------------------------


23. BIN SELECTION AFFECTS APPEARANCE

Check that conclusions do not depend only on one arbitrary
bin choice.


------------------------------------------------------------


24. DISTRIBUTION COMPARISON

Useful combination:

Histogram

+
Mean

+
Median

+
Standard Deviation

+
Percentiles


------------------------------------------------------------


25. ENGINEERING APPLICATIONS

Histograms are especially useful for:

Repeated measurements

Monte Carlo simulations

Tolerance analysis

Experimental variability

ML residuals

Prediction errors

Reliability analysis

Parameter uncertainty


------------------------------------------------------------


26. MOST IMPORTANT PRINCIPLE

A histogram should answer:

How are the observed values distributed?


It should not be used to claim more than the available
sample size and statistical evidence support.


------------------------------------------------------------


27. COMPLETE WORKFLOW

Numerical Observations
        ↓
Clean Data
        ↓
Check Sample Size
        ↓
Choose Bins
        ↓
Histogram
        ↓
Mean / Median
        ↓
Spread
        ↓
Percentiles
        ↓
Outliers
        ↓
Compare Cases
        ↓
Engineering Interpretation
        ↓
Report


------------------------------------------------------------


NEXT:

23_box_and_violin_plots.py


The next file will focus on compact distribution
comparison using:

Box plots

Median

Quartiles

Interquartile range

Whiskers

Potential outliers

Multiple engineering cases

Horizontal box plots

Notched box plots

Violin plots

Distribution shape

Box plot vs histogram

Box plot vs error bars

and how these plots are commonly used for experimental,
Monte Carlo, and machine-learning results.
"""
