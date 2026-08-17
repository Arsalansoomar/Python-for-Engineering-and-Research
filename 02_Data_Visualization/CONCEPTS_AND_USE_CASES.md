# Data Visualization — Concepts and Engineering Use Cases

This document is a compact reference for the main concepts used throughout the `02_Data_Visualization` folder.

It is designed for quick revision after working through the executable `.py` files.

---

# 1. Complete Visualization Workflow

```text
Engineering Question
        ↓
Data Source
        ↓
Python Variables / CSV / Excel
        ↓
Load Data
        ↓
Inspect Columns
        ↓
Validate
        ↓
Clean / Convert to Numeric
        ↓
Select Variables
        ↓
Process / Calculate Metrics
        ↓
Choose Plot Type
        ↓
Add Units / Labels
        ↓
Format Axes
        ↓
Interpret Scientifically
        ↓
Save
        ↓
Inspect Export
```

---

# 2. Core Libraries

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pathlib import Path
```

Typical roles:

| Library | Main Use |
|---|---|
| Matplotlib | Plotting and figure export |
| NumPy | Numerical arrays and calculations |
| Pandas | CSV / Excel / table processing |
| pathlib | Reliable file and folder paths |

---

# 3. Recommended Path Handling

Prefer:

```python
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

data_file = (
    SCRIPT_DIR
    / "sample_data"
    / "voltage_current.csv"
)
```

Avoid relying on the current working directory when a script should work reliably from different locations.

---

# 4. Basic Line Plot

Use when X is continuous or ordered.

```python
fig, ax = plt.subplots()

ax.plot(
    x,
    y
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

plt.show()
```

Engineering use cases:

- Voltage versus time
- Current versus time
- Efficiency versus load
- Temperature versus time
- Frequency response

---

# 5. Multiple Line Plots

```python
fig, ax = plt.subplots()

ax.plot(
    x,
    case_a,
    label="Case A"
)

ax.plot(
    x,
    case_b,
    label="Case B"
)

ax.legend()

plt.show()
```

Use when:

```text
Same X quantity
+
Compatible Y quantity
+
Several cases
```

Examples:

- Baseline vs optimized design
- Simulation vs experiment
- Multiple control strategies

---

# 6. Bar Plot

Use for category comparison.

```python
ax.bar(
    categories,
    values
)
```

Good for:

- Power losses by design
- Temperature by prototype
- Selected-frequency values
- Component comparison

Not ideal for:

- Dense continuous frequency spectra
- Long time-series data

---

# 7. Grouped Bar Plot

Typical concept:

```python
x = np.arange(
    len(
        categories
    )
)

width = 0.25

ax.bar(
    x - width,
    case_a,
    width,
    label="Case A"
)

ax.bar(
    x,
    case_b,
    width,
    label="Case B"
)
```

Use when several cases must be compared at the same discrete operating points.

---

# 8. Scatter Plot

```python
ax.scatter(
    x,
    y
)
```

Use for:

- Relationship between two variables
- Experimental spread
- Measured vs predicted
- Outlier inspection

Useful additions:

```python
np.corrcoef(...)
np.polyfit(...)
```

Remember:

```text
Correlation
≠
Causation
```

---

# 9. Subplots

```python
fig, axes = plt.subplots(
    3,
    1,
    sharex=True
)
```

Use when variables have different units:

```text
Voltage [V]
Current [A]
Power [W]
Temperature [°C]
```

Prefer subplots instead of forcing incompatible variables onto one Y-axis.

---

# 10. Dual Y Axis

```python
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
```

Use cautiously when:

```text
One common X
+
Two different Y quantities
```

Example:

```text
Load [%]
→ Efficiency [%]
→ Temperature [°C]
```

Important:

Visual curve crossing does **not** mean the numerical values are equal.

---

# 11. CSV Workflow

```python
df = pd.read_csv(
    file_path
)
```

Recommended sequence:

```text
Read
↓
Inspect columns
↓
Validate required columns
↓
Convert numeric
↓
Handle NaN
↓
Select variables
↓
Plot
```

Numeric conversion:

```python
df[
    "Voltage_V"
] = pd.to_numeric(
    df[
        "Voltage_V"
    ],
    errors="coerce"
)
```

---

# 12. Excel Workflow

```python
workbook = pd.ExcelFile(
    excel_file
)

print(
    workbook.sheet_names
)

df = pd.read_excel(
    excel_file,
    sheet_name="Load_Sweep"
)
```

Useful options:

```python
usecols=
skiprows=
nrows=
header=
```

---

# 13. Selecting Columns

By name:

```python
df[
    [
        "Time_s",
        "Voltage_V"
    ]
]
```

With `.loc`:

```python
df.loc[
    :,
    [
        "Time_s",
        "Voltage_V"
    ]
]
```

With `.iloc`:

```python
df.iloc[
    :,
    [
        0,
        2
    ]
]
```

Pattern selection:

```python
selected = [
    column
    for column in df.columns
    if "Voltage" in column
]
```

---

# 14. Multiple Files

```python
files = sorted(
    folder.glob(
        "*.csv"
    )
)

for file_path in files:
    df = pd.read_csv(
        file_path
    )
```

Important:

Different-length files can be plotted independently.

But:

```text
sample-by-sample subtraction
```

requires aligned X coordinates.

---

# 15. Multiple Excel Sheets

```python
workbook = pd.ExcelFile(
    file_path
)

for sheet_name in workbook.sheet_names:

    df = pd.read_excel(
        file_path,
        sheet_name=sheet_name
    )
```

Use when one workbook contains:

- Multiple experiments
- Multiple cases
- Different result categories

---

# 16. Logarithmic Axes

```python
ax.set_xscale(
    "log"
)
```

or:

```python
ax.semilogx(
    x,
    y
)
```

Requirements:

```text
Logarithmic coordinates must be positive.
```

Typical engineering use:

```text
Frequency [Hz]
```

---

# 17. FFT / EMI Plotting

Typical:

```python
ax.plot(
    frequency_hz,
    magnitude_dbuV
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
```

Important distinction:

```text
Logarithmic X axis
≠
log-transforming numeric dBµV Y values
```

---

# 18. dB Difference

For two values already expressed in dBµV:

```python
reduction_db = (
    baseline_dbuV
    - improved_dbuV
)
```

Example:

```text
100 dBµV - 90 dBµV = 10 dB
```

Do not calculate:

```python
(100 - 90) / 100 * 100
```

and call it EMI percentage reduction.

---

# 19. Axis Limits

```python
ax.set_xlim(
    x_min,
    x_max
)

ax.set_ylim(
    y_min,
    y_max
)
```

Important:

```text
set_xlim()
and
set_ylim()
```

change the displayed view.

They do not filter the underlying dataset.

---

# 20. Ticks

Manual ticks:

```python
ax.set_xticks(
    [
        0,
        20,
        40,
        60,
        80,
        100
    ]
)
```

Locator:

```python
from matplotlib.ticker import MultipleLocator

ax.xaxis.set_major_locator(
    MultipleLocator(
        20
    )
)
```

---

# 21. Labels and Units

Recommended style:

```text
Time [s]
Voltage [V]
Current [A]
Power [W]
Frequency [Hz]
Temperature [°C]
Efficiency [%]
Magnitude [dBµV]
```

A technical plot without units is incomplete unless the quantity is explicitly dimensionless.

---

# 22. Legend

```python
ax.legend()
```

For many panels with the same cases:

```python
fig.legend(
    handles,
    labels
)
```

Avoid repeating identical legends unnecessarily.

---

# 23. Annotations

```python
ax.annotate(
    "Peak",
    xy=(
        x_peak,
        y_peak
    ),
    xytext=(
        10,
        20
    ),
    textcoords="offset points",
    arrowprops={
        "arrowstyle":
            "->"
    }
)
```

Use for:

- Maximum sampled value
- Switching transition
- Resonance
- Target crossing
- Experimental anomaly

---

# 24. Reference Lines

Horizontal:

```python
ax.axhline(
    limit
)
```

Vertical:

```python
ax.axvline(
    operating_point
)
```

Use for:

- Limits
- Targets
- Selected operating points
- Switching times

---

# 25. Error Bars

```python
ax.errorbar(
    x,
    mean,
    yerr=error
)
```

Possible error definitions:

```text
Standard deviation
Standard error
Confidence interval
Measurement uncertainty
```

The plot must identify which one is used.

---

# 26. Standard Deviation

Sample SD:

```python
std = np.std(
    data,
    ddof=1
)
```

Interpretation:

```text
Spread among observations
```

---

# 27. Standard Error

```python
sem = (
    std
    / np.sqrt(
        n
    )
)
```

Interpretation:

```text
Uncertainty of estimated mean
```

under appropriate assumptions.

---

# 28. Approximate 95% CI

A common large-sample normal approximation:

```python
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
```

This is not a universal CI formula.

---

# 29. Saving Figures

PNG:

```python
fig.savefig(
    "figure.png",
    dpi=300,
    bbox_inches="tight"
)
```

PDF:

```python
fig.savefig(
    "figure.pdf",
    bbox_inches="tight"
)
```

SVG:

```python
fig.savefig(
    "figure.svg",
    bbox_inches="tight"
)
```

Recommended:

```text
Create
↓
Format
↓
Save
↓
Show
```

---

# 30. Raster vs Vector

## PNG

Best for:

- General use
- Web
- Raster-heavy plots
- Presentations

## PDF / SVG

Best for:

- Vector line plots
- Publication workflows
- Scalable text and lines

Check journal requirements before submission.

---

# 31. DPI

DPI controls raster resolution.

Example:

```python
fig.savefig(
    "figure.png",
    dpi=300
)
```

Remember:

```text
High DPI
≠
good scientific figure
```

The figure also needs:

- Correct dimensions
- Readable labels
- Good axis choices
- Clear interpretation

---

# 32. Histograms

```python
ax.hist(
    values,
    bins="auto"
)
```

Useful bin strategies include:

```text
auto
fd
sturges
sqrt
```

Use for:

- Measurement spread
- Noise
- Monte Carlo outcomes
- Residuals

---

# 33. Distribution Summary

Useful metrics:

```python
mean = np.mean(
    values
)

median = np.median(
    values
)

std = np.std(
    values,
    ddof=1
)

q1 = np.percentile(
    values,
    25
)

q3 = np.percentile(
    values,
    75
)

iqr = q3 - q1
```

---

# 34. Box Plot

```python
ax.boxplot(
    datasets,
    tick_labels=labels
)
```

Shows:

```text
Median
Q1
Q3
Whiskers
Fliers
```

Important:

A flier is not automatically invalid data.

---

# 35. Violin Plot

```python
ax.violinplot(
    datasets,
    showmedians=True
)
```

Useful for visualizing:

```text
Distribution shape
+
density
+
central tendency
```

Violin shape depends on:

- Sample size
- Bandwidth
- Distribution

---

# 36. Heatmap

Structured matrix example:

```python
image = ax.imshow(
    matrix,
    aspect="auto",
    origin="lower"
)
```

or:

```python
mesh = ax.pcolormesh(
    x_grid,
    y_grid,
    response,
    shading="auto"
)
```

Use for:

- Parameter maps
- Correlation matrices
- Load × frequency response

---

# 37. Colorbar

```python
colorbar = fig.colorbar(
    image,
    ax=ax
)

colorbar.set_label(
    "Efficiency [%]"
)
```

A quantitative colormap without a colorbar may be difficult to interpret.

---

# 38. Sequential vs Diverging Color Scale

## Sequential

Use for one-direction magnitude:

```text
Temperature
Loss
Efficiency
Amplitude
```

## Diverging

Use when zero or another center has meaning:

```text
Difference
Signed error
Correlation
Improvement / degradation
```

Example:

```python
cmap="coolwarm"
vmin=-maximum
vmax=maximum
```

---

# 39. Correlation Matrix

```python
numeric_df = df.select_dtypes(
    include="number"
)

corr = numeric_df.corr(
    method="pearson"
)
```

Pearson correlation:

```text
-1 → strong negative linear association
 0 → weak/no linear association
+1 → strong positive linear association
```

Important:

```text
Correlation
≠
Causation
```

Also remember that Pearson correlation targets linear association.

---

# 40. Contour Plot

```python
contour = ax.contour(
    X,
    Y,
    Z
)
```

Filled:

```python
contour = ax.contourf(
    X,
    Y,
    Z,
    levels=20
)
```

Use for:

- Equal-response lines
- Design-space maps
- Optimization regions
- Constraints

---

# 41. Meshgrid

```python
X, Y = np.meshgrid(
    x_values,
    y_values
)
```

Typical relationship:

```text
Parameter X
×
Parameter Y
→
Response Z
```

---

# 42. Best Sampled Point

Maximum:

```python
index = np.unravel_index(
    np.argmax(
        Z
    ),
    Z.shape
)
```

Minimum:

```python
index = np.unravel_index(
    np.argmin(
        Z
    ),
    Z.shape
)
```

Terminology:

```text
Best sampled point
```

not automatically:

```text
Global continuous optimum
```

---

# 43. Inset Plot

```python
axins = ax.inset_axes(
    [
        0.55,
        0.15,
        0.40,
        0.35
    ]
)
```

Then:

```python
axins.plot(
    x,
    y
)

axins.set_xlim(
    zoom_min,
    zoom_max
)
```

Use for:

- Overshoot
- Ringing
- Ripple
- Narrow spectral region

---

# 44. Zoom Indicator

```python
ax.indicate_inset_zoom(
    axins
)
```

This visually connects the inset with the selected region.

---

# 45. Multi-Panel Figures

Basic:

```python
fig, axes = plt.subplots(
    2,
    2
)
```

Panel identifiers:

```text
(a)
(b)
(c)
(d)
```

Use for journal figures containing related results.

---

# 46. GridSpec

```python
from matplotlib.gridspec import GridSpec

grid = GridSpec(
    2,
    2,
    figure=fig
)
```

Use when panels require:

- Different widths
- Different heights
- Row spanning
- Column spanning

---

# 47. subplot_mosaic

```python
fig, axes = plt.subplot_mosaic(
    [
        [
            "fft",
            "fft",
            "summary"
        ],
        [
            "time",
            "map",
            "summary"
        ]
    ]
)
```

Useful for complex semantic layouts.

---

# 48. Shared Colorbar

For directly comparable heatmaps:

```text
same response quantity
same colormap
same vmin
same vmax
```

Then:

```python
fig.colorbar(
    image,
    ax=axes
)
```

Do not use one colorbar for physically different quantities.

---

# 49. Confidence / Uncertainty Band

```python
ax.fill_between(
    x,
    lower,
    upper,
    alpha=0.25
)
```

Possible meanings:

```text
Mean ± SD
Mean ± SEM
Confidence interval
Percentile envelope
Min-max envelope
Measurement uncertainty
```

Always define the meaning.

---

# 50. Percentile Band

```python
lower = np.percentile(
    repeated_data,
    5,
    axis=0
)

upper = np.percentile(
    repeated_data,
    95,
    axis=0
)
```

Typical Monte Carlo interpretation:

```text
central 90% sampled range
```

not automatically:

```text
90% confidence interval
```

---

# 51. Horizontal Target Region

```python
ax.axhspan(
    lower,
    upper,
    alpha=0.2
)
```

Use for:

- Voltage tolerance
- Temperature limit
- Efficiency target

---

# 52. Vertical Operating Region

```python
ax.axvspan(
    x_start,
    x_end,
    alpha=0.2
)
```

Use for:

- Startup
- Steady state
- Frequency band
- Measurement interval

---

# 53. Conditional Shading

```python
condition = (
    difference
    >= 0
)

ax.fill_between(
    x,
    0,
    difference,
    where=condition,
    interpolate=True
)
```

Use for:

- Improvement / degradation
- Requirement violation
- Above / below limit

---

# 54. Broken Y Axis

Typical structure:

```python
fig, (
    ax_top,
    ax_bottom
) = plt.subplots(
    2,
    1,
    sharex=True
)
```

Plot the same data on both:

```python
ax_top.plot(
    x,
    y
)

ax_bottom.plot(
    x,
    y
)
```

Then different Y limits.

Important:

The omitted range must be clearly marked.

---

# 55. Broken Axis Alternatives

Before using a broken axis, consider:

```text
Log axis
Inset
Separate subplot
Normalization
Difference plot
```

Broken axes are powerful but can exaggerate visual differences.

---

# 56. Batch Plotting

Basic discovery:

```python
files = sorted(
    folder.glob(
        "*.csv"
    )
)
```

Recursive:

```python
files = sorted(
    folder.rglob(
        "*.csv"
    )
)
```

---

# 57. Batch Processing Pattern

```python
for file_path in files:

    try:
        df = pd.read_csv(
            file_path
        )

        # validate
        # process
        # plot
        # save

    except Exception as error:

        # log failure
        continue
```

Do not let one corrupted file terminate an entire research campaign unless stopping is intentionally required.

---

# 58. Close Figures in Batch Loops

```python
fig.savefig(
    output_file
)

plt.close(
    fig
)
```

This is important for memory management.

---

# 59. Batch Logging

Use:

```python
import logging
```

Track:

```text
Processed files
Skipped files
Failure reasons
Output locations
```

---

# 60. Natural Sorting

String sorting may produce:

```text
Case_1
Case_10
Case_2
```

Natural sorting should produce:

```text
Case_1
Case_2
Case_10
```

Useful for simulation and experimental case numbering.

---

# 61. 3D Axis

```python
fig = plt.figure()

ax = fig.add_subplot(
    111,
    projection="3d"
)
```

---

# 62. 3D Surface

```python
surface = ax.plot_surface(
    X,
    Y,
    Z,
    cmap="viridis"
)
```

Use for geometric understanding of:

```text
Parameter X
×
Parameter Y
→
Response Z
```

---

# 63. 3D Scatter

```python
ax.scatter(
    x,
    y,
    z
)
```

Use for:

- DOE
- Random sampling
- Irregular simulations
- Experimental points

---

# 64. Triangulated Surface

```python
ax.plot_trisurf(
    x,
    y,
    z
)
```

Use for irregular X-Y coordinates.

Important:

The triangulated surface visually connects sampled points; it does not mean every location was directly measured or simulated.

---

# 65. 3D Camera

```python
ax.view_init(
    elev=25,
    azim=-135
)
```

Camera angle changes appearance, not underlying data.

For direct comparison between surfaces, use consistent views.

---

# 66. Interactive Slider

```python
from matplotlib.widgets import Slider

slider = Slider(
    slider_axis,
    "Load [%]",
    20,
    100,
    valinit=60
)
```

Callback:

```python
def update(
    value
):
    load = slider.val

    line.set_ydata(
        new_values
    )

    fig.canvas.draw_idle()

slider.on_changed(
    update
)
```

---

# 67. RangeSlider

```python
from matplotlib.widgets import RangeSlider
```

Use for:

```text
Frequency minimum
+
Frequency maximum
```

---

# 68. RadioButtons

Use when only one case should be active:

```text
Unshielded
Case A
Case B
Case C
```

---

# 69. CheckButtons

Use when several cases may be shown or hidden independently.

---

# 70. SpanSelector

Use for mouse-selected X ranges:

```text
Time window
Frequency band
Steady-state region
```

Possible calculations after selection:

```text
Mean
RMS
Maximum
Minimum
Peak-to-peak
```

---

# 71. Interactive vs Publication

Recommended:

```text
Interactive Exploration
        ↓
Record Important Parameters
        ↓
Formal Numerical Analysis
        ↓
Static Reproducible Figure
```

Do not rely on screenshots of interactively adjusted plots.

---

# 72. Parameter Sweep

One-parameter example:

```text
Switching Frequency
        ↓
Efficiency
Loss
Temperature
EMI
```

Two-parameter example:

```text
Switching Frequency
        ×
Load
        ↓
Response
```

---

# 73. Local Sensitivity

Numerical derivative:

```python
sensitivity = np.gradient(
    response,
    parameter
)
```

Interpret units carefully.

Example:

```text
Efficiency sensitivity
[% per kHz]
```

or:

```text
Loss sensitivity
[W per kHz]
```

---

# 74. Normalized Local Sensitivity

A common dimensionless form:

```python
normalized_sensitivity = (
    parameter
    / response
) * (
    d_response
    / d_parameter
)
```

Interpret cautiously near zero response values.

---

# 75. Baseline Difference

Linear quantity:

```python
difference = (
    improved
    - baseline
)
```

Relative change:

```python
relative_change_percent = (
    difference
    / baseline
) * 100
```

Only when the quantity and denominator make physical sense.

---

# 76. Percentage Points

For quantities already expressed in percent:

```python
difference_pp = (
    design_b_percent
    - design_a_percent
)
```

Example:

```text
95% - 94% = 1 percentage point
```

---

# 77. Long-Form Parameter Data

Recommended table:

```text
Frequency_kHz
Load_percent
Efficiency_percent
Power_Loss_W
Temperature_C
EMI_Reduction_dB
```

This is useful for:

- Pandas
- ML
- DOE
- CSV export
- Ranking
- Filtering

---

# 78. Pivot Table

Convert long form into response matrix:

```python
pivot = df.pivot_table(
    index="Load_percent",
    columns="Frequency_kHz",
    values="Efficiency_percent",
    aggfunc="mean"
)
```

Prefer `pivot_table()` when duplicate parameter combinations may exist.

---

# 79. Engineering Constraints

Example:

```python
feasible = (
    (efficiency >= 95.0)
    &
    (temperature <= 80.0)
    &
    (loss <= 20.0)
)
```

Constraint logic must reflect actual engineering requirements.

---

# 80. Feasible Region

Boolean feasible map:

```python
feasible.astype(
    int
)
```

Plot using:

- Heatmap
- Contour
- Scatter

---

# 81. Weighted Engineering Score

Example idea:

```text
Efficiency ↑
EMI Reduction ↑
Loss ↓
Temperature ↓
```

Normalize first, then weight.

Important:

```text
Weighted-score winner
≠
universally best design
```

The result depends on chosen weights and normalization.

---

# 82. Pareto Analysis

A candidate is Pareto-optimal when no other candidate is better in all objectives simultaneously and strictly better in at least one.

Typical objectives:

```text
Maximize:
Efficiency
EMI reduction

Minimize:
Loss
Temperature
```

Pareto analysis identifies tradeoffs, not one automatic winner.

---

# 83. Robustness Analysis

After finding a promising design:

```text
Candidate
    ↓
Perturb parameters
    ↓
Monte Carlo / tolerance samples
    ↓
Recalculate response
    ↓
Check constraints
    ↓
Estimate robustness under assumed model
```

Important:

A Monte Carlo feasibility fraction is conditional on the assumed parameter distributions and model.

It is not automatically universal reliability.

---

# 84. Publication Multi-Panel Capstone

A useful final engineering figure may combine:

```text
(a) Sensitivity curve
(b) Contour map
(c) Feasible region
(d) Pareto tradeoff
```

This tells a complete engineering design-space story.

---

# 85. Plot Selection Decision Tree

```text
Time evolution?
    ↓
Line plot

Category comparison?
    ↓
Bar plot

Relationship between variables?
    ↓
Scatter plot

Distribution?
    ↓
Histogram

Compare distributions?
    ↓
Box / violin

Matrix?
    ↓
Heatmap

Equal-response regions?
    ↓
Contour

Small detail?
    ↓
Inset

Several related results?
    ↓
Multi-panel

Continuous uncertainty?
    ↓
Shaded band

Extreme numerical gap?
    ↓
Consider log / inset first
    ↓
Broken axis if justified

Many files?
    ↓
Batch plotting

Two parameters → one response?
    ↓
Contour + optional 3D

Interactive exploration?
    ↓
Widgets

Complete design study?
    ↓
Parameter-sweep visualization
```

---

# 86. Engineering Interpretation Checklist

Before accepting a plot, ask:

```text
1. What physical question does it answer?

2. Are units shown?

3. Are axis scales appropriate?

4. Are cases directly comparable?

5. Are any values normalized?

6. Are dB values treated correctly?

7. Are percentages and percentage points distinguished?

8. Does the figure show sampled data or interpolation?

9. Are uncertainty definitions stated?

10. Are peaks formally detected or only sampled maxima?

11. Are different files properly aligned before subtraction?

12. Could axis limits exaggerate the result?

13. Is the figure reproducible?

14. Can it be exported without taking a screenshot?
```

---

# 87. Publication Checklist

```text
Correct data
    ↓
Correct units
    ↓
Appropriate plot type
    ↓
Readable final physical size
    ↓
Consistent typography
    ↓
Clear line / marker identity
    ↓
Fair axis limits
    ↓
Correct uncertainty terminology
    ↓
Correct dB interpretation
    ↓
Numerical result verified
    ↓
PNG / PDF / SVG
    ↓
Caption
```

---

# 88. Common Mistakes Summary

Avoid:

- Plotting incompatible units on one Y-axis
- Treating dB values as linear percentages
- Calling `idxmax()` formal peak detection
- Subtracting unequal datasets by row number
- Using different heatmap scales for direct comparison
- Hiding uncertainty definitions
- Using broken axes without break marks
- Leaving hundreds of batch figures open
- Trusting automatic column selection blindly
- Presenting interpolated / triangulated data as measured data
- Calling the best grid point a global optimum
- Calling a weighted-score result universally optimal
- Using interactive screenshots instead of reproducible static figures
- Choosing 3D when a 2D contour is clearer

---

# 89. Recommended Research Data Structure

```text
project/
│
├── raw_data/
│
├── processed_data/
│
├── scripts/
│
├── output_data/
│
├── output_figures/
│
└── logs/
```

Never overwrite raw experimental data during normal processing.

---

# 90. Final Learning Outcome

After completing all 33 scripts, the intended capability is:

```text
Raw Engineering Data
        ↓
Python
        ↓
Clean / Validate
        ↓
Scientific Analysis
        ↓
Appropriate Visualization
        ↓
Quantitative Comparison
        ↓
Automated Processing
        ↓
Design-Space Analysis
        ↓
Publication Figure
        ↓
Engineering Decision
```

The purpose of visualization is not only to make data look attractive.

The purpose is to make engineering information:

```text
Clear
Quantitative
Reproducible
Scientifically defensible
Useful for decisions
```
