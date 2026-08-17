Data Visualization for Engineering and Research

This folder provides a practical, engineering-focused guide to data visualization with Python. The examples progress from basic line plots to publication-quality scientific figures, automated research workflows, interactive exploration, and engineering parameter-sweep analysis.

The goal is not only to learn Matplotlib syntax, but to understand how to choose, build, validate, interpret, and export figures for real engineering and research work.

Learning Philosophy

Each script follows the same practical progression:

LEVEL 1 — What the plotting concept does
LEVEL 2 — Basic Python / Matplotlib syntax
LEVEL 3 — Engineering or research application

Most files include:

Concept explanation

Basic syntax

Simple example

Engineering example

Reusable functions

Common mistakes

Scientific interpretation

Publication considerations

PNG / PDF / SVG export

Workflow summary

Key takeaways

Recommended Learning Path

Manual Data
    ↓
Basic Line Plot
    ↓
Multiple Variables
    ↓
Bar / Scatter / Grouped Comparisons
    ↓
Subplots / Dual Axes
    ↓
CSV / Excel Data
    ↓
Multiple Files / Sheets
    ↓
Logarithmic Axes / FFT
    ↓
Axis Formatting / Labels / Legends
    ↓
Uncertainty / Error Bars
    ↓
Publication-Quality Figures
    ↓
Engineering Comparison
    ↓
Advanced Scientific Visualization
    ↓
Research Automation
    ↓
3D / Interactive Exploration
    ↓
Engineering Parameter-Sweep Analysis

Folder Structure

02_Data_Visualization/
│
├── README.md
├── CONCEPTS_AND_USE_CASES.md
│
├── 01_basic_line_plot.py
├── 02_multiple_line_plots.py
├── 03_bar_plot.py
├── 04_grouped_bar_plot.py
├── 05_scatter_plot.py
├── 06_multiple_variables.py
├── 07_subplots.py
├── 08_plot_from_csv.py
├── 09_plot_from_excel.py
├── 10_select_columns_and_plot.py
├── 11_multiple_csv_files.py
├── 12_multiple_excel_sheets.py
├── 13_dual_y_axis.py
├── 14_logarithmic_axis.py
├── 15_axis_limits_and_ticks.py
├── 16_legends_labels_annotations.py
├── 17_error_bars.py
├── 18_save_png_pdf_svg.py
├── 19_high_resolution_figures.py
├── 20_publication_quality_plot.py
├── 21_engineering_comparison_plot.py
│
├── 22_histograms_and_distributions.py
├── 23_box_and_violin_plots.py
├── 24_heatmaps_and_correlation_maps.py
├── 25_contour_and_parameter_sweep_plots.py
├── 26_inset_and_zoomed_plots.py
├── 27_multi_panel_publication_figures.py
│
├── 28_confidence_bands_and_shaded_regions.py
├── 29_broken_axis_and_discontinuous_ranges.py
├── 30_automatic_batch_plotting.py
├── 31_3d_engineering_plots.py
├── 32_interactive_plotting.py
└── 33_engineering_parameter_sweep_visualization.py

Section A — Core Data Visualization

Files 01–21 build the fundamental plotting skills required for engineering work.

01 — Basic Line Plot

File: 01_basic_line_plot.py

Learn:

plt.plot()

Figure and axes creation

Labels and units

Grid

Legend

Axis limits

Saving figures

Object-oriented Matplotlib style

Engineering use cases:

Converter startup waveform

Voltage versus time

Current versus time

Temperature versus time

Experimental response curves

02 — Multiple Line Plots

File: 02_multiple_line_plots.py

Learn:

Two variables on one graph

Three or more curves

Loops for multiple cases

Dictionary-based plotting

Simulation versus experiment

Managing too many curves

Engineering use cases:

Multiple converter designs

Baseline versus optimized cases

Efficiency curves

Simulation and experimental validation

03 — Bar Plot

File: 03_bar_plot.py

Learn:

Category comparison

Horizontal and vertical bars

Bar labels

Reference limits

Sorting categories

Engineering use cases:

Power-loss comparison

Temperature comparison

Component comparison

Selected-frequency EMI comparison

04 — Grouped Bar Plot

File: 04_grouped_bar_plot.py

Learn:

Multiple groups at each category

NumPy bar positioning

Automatic grouped plotting

Selected-frequency comparisons

Reference limits

Engineering use cases:

Multiple EMI mitigation cases

Simulation versus experiment

Design comparison at selected frequencies

05 — Scatter Plot

File: 05_scatter_plot.py

Learn:

Scatter plots

Correlation visualization

Trend lines

Measured versus predicted

Ideal y = x comparison

Outlier annotation

Engineering use cases:

Power loss versus current

Temperature versus efficiency

Experimental versus predicted values

ML model validation

06 — Multiple Variables

File: 06_multiple_variables.py

Learn how to decide between:

Same axis

Subplots

Dual Y axes

Normalized values

Selected variables

Engineering use cases:

Voltage, current, power, efficiency

Multi-variable converter data

Relative improvement comparison

07 — Subplots

File: 07_subplots.py

Learn:

plt.subplots()

Shared X axes

Multiple rows and columns

Automatic subplot generation

Global labels

Removing unused axes

Engineering use cases:

Voltage / current / power / temperature

Simulation and hardware comparisons

Multi-signal experiment figures

08 — Plot from CSV

File: 08_plot_from_csv.py

Learn:

pandas.read_csv()

File validation

Column inspection

Numeric conversion

Missing-data handling

Derived quantities

Processed-data export

Engineering use cases:

Oscilloscope exports

Simulation results

Measurement logs

Processed experimental datasets

09 — Plot from Excel

File: 09_plot_from_excel.py

Learn:

pandas.ExcelFile

Sheet selection

usecols

skiprows

nrows

Multiple worksheets

Processed Excel export

Engineering use cases:

Test reports

Multi-sheet measurement workbooks

Load sweeps

Frequency-response sheets

10 — Select Columns and Plot

File: 10_select_columns_and_plot.py

Learn:

Column selection by name

.loc

.iloc

Pattern-based selection

Numeric-only selection

Programmatic selection

Engineering use cases:

Large measurement tables

Automated research scripts

Flexible CSV / Excel workflows

11 — Multiple CSV Files

File: 11_multiple_csv_files.py

Learn:

Path.glob()

Loading several files

File-by-file comparison

Long-form tables

Different-length datasets

Alignment warnings

Engineering use cases:

One file per design case

Multiple experiments

Parameter sweeps

Batch simulation outputs

12 — Multiple Excel Sheets

File: 12_multiple_excel_sheets.py

Learn:

Reading all worksheets

Sheet-name filtering

Multi-sheet comparison

Validation

Summary generation

Engineering use cases:

One sheet per operating case

Experimental campaign workbooks

Multiple parameter conditions

13 — Dual Y Axis

File: 13_dual_y_axis.py

Learn:

twinx()

Independent Y scales

Combined legends

Dual-axis limitations

Difference between twinx() and secondary_yaxis()

Engineering use cases:

Efficiency and temperature

Power and temperature

Voltage and current when carefully justified

14 — Logarithmic Axis

File: 14_logarithmic_axis.py

Learn:

semilogx

semilogy

loglog

Positive-value requirements

Log-frequency plotting

Logarithmic tick formatting

Engineering use cases:

FFT

EMI spectra

Frequency response

Bode-style data

Wide dynamic range

Important: A frequency axis may be logarithmic while a numeric dBµV Y-axis remains linear.

15 — Axis Limits and Ticks

File: 15_axis_limits_and_ticks.py

Learn:

X and Y limits

Major and minor ticks

Locators

Scientific notation

Frequency formatting

Zoom versus data filtering

Engineering use cases:

Publication formatting

Selected operating regions

Frequency-axis formatting

16 — Legends, Labels and Annotations

File: 16_legends_labels_annotations.py

Learn:

Engineering units

Titles

Legends

Text

Arrows

Reference lines

Highlighted regions

Maximum / minimum annotations

Engineering use cases:

Marking sampled peaks

Operating limits

Target regions

Important transitions

17 — Error Bars

File: 17_error_bars.py

Learn:

Standard deviation

Standard error

Approximate confidence intervals

Measurement uncertainty

Symmetric and asymmetric error bars

fill_between() introduction

Engineering use cases:

Repeated experiments

Measurement uncertainty

Experimental validation

Important: SD, SEM, confidence intervals, and measurement uncertainty are different concepts.

18 — Save PNG, PDF and SVG

File: 18_save_png_pdf_svg.py

Learn:

Raster versus vector formats

DPI

Figure size

Transparent backgrounds

Batch saving

Metadata

Output naming

Engineering use cases:

Thesis figures

Journal figures

Presentations

GitHub documentation

19 — High-Resolution Figures

File: 19_high_resolution_figures.py

Learn:

Physical dimensions

DPI versus pixel size

mm / inch conversion

300 / 600 DPI

Final-size readability

Important: High DPI alone does not make a figure publication quality.

20 — Publication-Quality Plot

File: 20_publication_quality_plot.py

Learn:

Consistent typography

Line widths

Markers

Axis styling

Final physical size

Vector export

Panel-label preparation

Engineering use cases:

Journal figures

Thesis results

Conference papers

Note: Publisher instructions override example dimensions and font choices.

21 — Engineering Comparison Plot

File: 21_engineering_comparison_plot.py

This is the capstone of the core section.

Learn:

Baseline comparison

Absolute differences

Relative improvement

Metric direction

Ranking

Selected operating points

dB reduction

Multi-metric comparison

Processed-data export

Engineering use cases:

Baseline versus optimized converter designs

Simulation versus experiment

EMI mitigation comparisons

Efficiency / loss / thermal comparisons

Section B — Advanced Scientific Visualization

Files 22–27 focus on the visualization styles frequently seen in scientific and engineering publications.

22 — Histograms and Distributions

File: 22_histograms_and_distributions.py

Use for:

Measurement distributions

Noise distributions

Monte Carlo results

Repeated experiments

Data-quality inspection

Topics include:

Histogram bins

Counts / density / percentage

Mean / median / SD

Percentiles / IQR

Cumulative distributions

Outlier investigation

23 — Box and Violin Plots

File: 23_box_and_violin_plots.py

Use for:

Comparing repeated measurements

Comparing several designs

Skewed distributions

Unequal sample sizes

Topics include:

Median

Quartiles

IQR

Whiskers

Fliers

Violin KDE

Raw-point overlays

Distribution summaries

24 — Heatmaps and Correlation Maps

File: 24_heatmaps_and_correlation_maps.py

Use for:

Parameter matrices

Correlation matrices

Load × frequency response

Temperature maps

Efficiency maps

Topics include:

imshow

pcolormesh

Colorbars

Annotations

Sequential and diverging scales

Correlation interpretation

Important: Correlation does not establish causation.

25 — Contour and Parameter-Sweep Plots

File: 25_contour_and_parameter_sweep_plots.py

Use for:

Design spaces

Equal-response regions

Optimization

Engineering constraints

Parameter sweeps

Topics include:

contour

contourf

Filled contours

Constraint boundaries

Best sampled operating points

26 — Inset and Zoomed Plots

File: 26_inset_and_zoomed_plots.py

Use for:

Switching transitions

Overshoot

Ringing

Ripple

FFT peaks

Simulation versus experiment detail

Topics include:

Axes.inset_axes()

indicate_inset_zoom()

zoomed_inset_axes()

mark_inset()

Automatic zoom limits

27 — Multi-Panel Publication Figures

File: 27_multi_panel_publication_figures.py

Use for:

(a)–(d) journal figures

Time + frequency domain

Mixed line / bar / heatmap layouts

Simulation + experiment + summary

Topics include:

plt.subplots()

GridSpec

subplot_mosaic()

Shared axes

Common legends

Shared colorbars

Panel labels

Publication dimensions

Section C — Research Automation and Specialized Visualization

Files 28–33 focus on uncertainty visualization, automation, complex engineering plots, interactive exploration, and complete parameter-study workflows.

28 — Confidence Bands and Shaded Regions

File: 28_confidence_bands_and_shaded_regions.py

Use for:

Mean ± SD

Mean ± SEM

Approximate confidence intervals

Percentile envelopes

Monte Carlo bands

Engineering limits

Operating regions

Topics include:

fill_between()

axhspan()

axvspan()

Conditional shading

Nested bands

Frequency-band highlighting

Important: SD, SEM, CI, percentile range, min-max range, and engineering target bands are not interchangeable.

29 — Broken Axis and Discontinuous Ranges

File: 29_broken_axis_and_discontinuous_ranges.py

Use when:

One extreme value compresses important detail

Normal and fault ranges must be shown together

Two separated ranges are important

Before using a broken axis, consider:

Log axis

Inset

Separate subplots

Difference plot

Important: Always make the omitted axis range obvious.

30 — Automatic Batch Plotting

File: 30_automatic_batch_plotting.py

Use for:

Tens or hundreds of CSV files

Multiple Excel workbooks

Multiple worksheets

FFT campaigns

Experimental campaigns

Simulation sweeps

Topics include:

File discovery

glob() / rglob()

Column detection

Validation

Logging

Continue-on-error workflows

Summary tables

Automatic export

Natural sorting

plt.close(fig)

Typical workflow:

Raw Data Folder
    ↓
Discover Files
    ↓
Validate
    ↓
Process
    ↓
Plot
    ↓
Save
    ↓
Close
    ↓
Log
    ↓
Summary

31 — 3D Engineering Plots

File: 31_3d_engineering_plots.py

Use for:

Response surfaces

DOE points

Efficiency / loss / temperature surfaces

Operating trajectories

Irregular parameter samples

Topics include:

3D lines

3D scatter

plot_surface()

plot_wireframe()

plot_trisurf()

Camera angle

Surface colorbars

Contour projection

Best sampled points

Important: 3D is useful for geometric intuition, but 2D contour plots are often clearer for quantitative publication analysis.

32 — Interactive Plotting

File: 32_interactive_plotting.py

Use for:

Parameter exploration

FFT inspection

Time-window selection

Case selection

Dynamic cross sections

Operating-point exploration

Topics include:

Slider

RangeSlider

Button

RadioButtons

CheckButtons

TextBox

Cursor

SpanSelector

Mouse / keyboard events

Static snapshot generation

Recommended workflow:

Interactive Exploration
        ↓
Identify Important Result
        ↓
Record Numerical Settings
        ↓
Generate Reproducible Static Figure

33 — Engineering Parameter-Sweep Visualization

File: 33_engineering_parameter_sweep_visualization.py

This is the capstone of the complete Data Visualization section.

It combines:

One-parameter sweeps

Sensitivity analysis

Normalized sensitivity

Baseline comparison

Two-parameter sweeps

Long-form DataFrames

Pivot tables

Heatmaps

Contours

3D surfaces

Engineering constraints

Feasible regions

Best sampled points

Weighted multi-objective ranking

Pareto analysis

Robustness analysis

Monte Carlo studies

Publication multi-panel figures

Processed-data export

Complete workflow:

Engineering Parameters
        ↓
Parameter Sweep
        ↓
Sensitivity
        ↓
Visualization
        ↓
Constraint Analysis
        ↓
Feasible Region
        ↓
Candidate Ranking
        ↓
Pareto Tradeoffs
        ↓
Robustness Analysis
        ↓
Engineering Decision
        ↓
Validation
        ↓
Publication Figure

Sample Data

The visualization examples use synthetic educational datasets.

Recommended sample-data folder:

sample_data/
├── voltage_current.csv
├── multiple_cases.csv
├── fft_example.csv
└── converter_measurements.xlsx

Typical columns include:

voltage_current.csv

Time_s
Voltage_V
Current_A
Power_W

multiple_cases.csv

Time_s
Case_A_V
Case_B_V
Case_C_V
Case_D_V

fft_example.csv

Frequency_Hz
Unshielded_dBuV
Case_A_dBuV
Case_B_dBuV
Case_C_dBuV

converter_measurements.xlsx

Example sheets:

Time_Domain
Load_Sweep
Case_Comparison

Recommended Output Structure

The scripts commonly create folders such as:

02_Data_Visualization/
│
├── sample_data/
│
├── output_data/
│   ├── processed_results.csv
│   ├── comparison_summary.csv
│   └── ...
│
├── output_figures/
│   ├── distributions/
│   ├── heatmaps/
│   ├── inset_zoom/
│   ├── multi_panel/
│   ├── confidence_bands/
│   ├── broken_axis/
│   ├── batch_plotting/
│   ├── 3d_engineering/
│   └── interactive/
│
└── logs/
    └── batch_plotting.log

Keep:

RAW DATA
    ≠
PROCESSED DATA
    ≠
GENERATED FIGURES

Core Python Libraries

Most examples use:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

Additional Matplotlib tools are introduced only where needed, including:

from matplotlib.gridspec import GridSpec
from matplotlib.widgets import Slider, RangeSlider
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

Engineering Plot Selection Guide

Engineering Question

Recommended Plot

How does a variable change with time?

Line plot

How do several cases compare?

Multiple line plot

How do categories compare?

Bar plot

How do multiple cases compare at selected categories?

Grouped bar

Is there a relationship between two variables?

Scatter

How do several physical quantities evolve together?

Subplots

Two different Y units with one common X?

Dual Y axis, cautiously

Frequency-domain response?

Log-X line plot

Distribution of repeated measurements?

Histogram

Compare distributions across designs?

Box / violin

Matrix-like response?

Heatmap

Equal-response regions?

Contour

Important small detail inside a full result?

Inset

Several related paper results?

Multi-panel figure

Continuous uncertainty?

Shaded band

Extreme values compress the important range?

First consider log/inset; broken axis only if justified

Hundreds of files?

Batch plotting

Two parameters affecting one response?

Contour + optional 3D surface

Interactive exploration?

Matplotlib widgets

Full engineering design-space analysis?

Parameter-sweep workflow

Important Scientific Visualization Rules

1. Always Include Units

Prefer:

Voltage [V]
Current [A]
Power [W]
Frequency [Hz]
Temperature [°C]
Efficiency [%]
Magnitude [dBµV]

Avoid unlabeled numerical axes.

2. Frequency and dB Data

For EMI / FFT data:

Frequency → commonly logarithmic X-axis
dBµV → numeric Y-axis remains linear

A change from:

100 dBµV → 90 dBµV

is:

10 dB reduction

not automatically:

10% reduction

3. Percentage Point vs Relative Percentage

Example:

94% → 95%

Absolute efficiency change:

1 percentage point

Relative change:

(95 - 94) / 94 × 100 ≈ 1.06%

These are different quantities.

4. Sampled Maximum vs Peak Detection

Using:

idxmax()
np.argmax()

finds the:

maximum sampled point

It is not automatically formal signal-processing peak detection.

5. Different File Lengths

Different-length datasets can be plotted together.

However, sample-by-sample operations such as:

Case B - Case A

require appropriate alignment, interpolation, or resampling.

6. Uncertainty Terminology

Do not mix:

Standard Deviation
Standard Error
Confidence Interval
Prediction Interval
Measurement Uncertainty
Percentile Envelope
Min-Max Range
Engineering Target Range

The figure must state exactly what the band or error bar represents.

7. Publication Dimensions

Example widths in scripts are educational examples only.

Always check:

Journal instructions

Conference requirements

Thesis template

Publisher figure specifications

Research Figure Workflow

A strong engineering figure normally follows:

Engineering Question
        ↓
Load / Generate Data
        ↓
Validate
        ↓
Clean
        ↓
Select Variables
        ↓
Choose Appropriate Plot
        ↓
Add Units
        ↓
Set Fair Axis Limits
        ↓
Add Legend / Annotation
        ↓
Calculate Numerical Metrics
        ↓
Check Scientific Interpretation
        ↓
Save Figure
        ↓
Inspect Exported Result
        ↓
Use in Thesis / Paper / Report

Publication Workflow

Raw Data
    ↓
Processed Data
    ↓
Exploratory Plots
    ↓
Engineering Interpretation
    ↓
Select Important Results
    ↓
Publication-Quality Figure
    ↓
PNG / PDF / SVG
    ↓
Figure Caption
    ↓
Paper / Thesis

Suggested Learning Levels

Beginner

Start with:

01–07

Focus on:

Line plots

Multiple variables

Bars

Scatter

Subplots

Intermediate

Continue with:

08–17

Focus on:

CSV

Excel

Multiple files

Log axes

Formatting

Error bars

Research / Publication

Continue with:

18–27

Focus on:

High-resolution export

Publication style

Engineering comparison

Distributions

Heatmaps

Contours

Insets

Multi-panel figures

Advanced Research Automation

Continue with:

28–33

Focus on:

Continuous uncertainty

Broken axes

Batch processing

3D visualization

Interactive exploration

Complete parameter-sweep analysis

Final Skill Progression

After completing this folder, the learner should be able to move from:

"I know how to make a Python plot."

to:

"I can build a reproducible engineering visualization workflow
from raw CSV/Excel data to processed results, quantitative
comparison, publication figures, automated case processing,
and design-space analysis."

Next Recommended Repository Sections

After Data Visualization, the natural progression is:

NumPy
    ↓
Pandas
    ↓
SciPy
    ↓
Signal Processing
    ↓
Machine Learning
    ↓
Engineering Applications

The visualization skills developed here will be reused throughout all later engineering examples.

Author

Arsalan Muhammad Soomar

Engineering and research portfolio:

https://www.arsalanm.com/

This repository is intended as a practical learning and reference resource for students, researchers, and engineers.
