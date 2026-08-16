# Data Visualization — Concepts and Use Cases

This document provides a practical reference for selecting, creating, and interpreting common Python plots used in engineering, scientific research, and data analysis.

---

# 1. General Visualization Pipeline

```text
Define the Question
       ↓
Identify Available Data
       ↓
Select X and Y Variables
       ↓
Choose Plot Type
       ↓
Process Data if Required
       ↓
Create Plot
       ↓
Add Labels and Units
       ↓
Adjust Scale and Limits
       ↓
Add Legend / Annotation
       ↓
Validate Interpretation
       ↓
Save Figure
```

The plotting command itself is only one part of a complete visualization workflow.

---

# 2. Choosing the Appropriate Plot

| Objective                              | Recommended Plot      |
| -------------------------------------- | --------------------- |
| Show variation with time               | Line plot             |
| Compare several signals                | Multiple line plot    |
| Compare discrete categories            | Bar plot              |
| Compare multiple methods/categories    | Grouped bar plot      |
| Examine relationship between variables | Scatter plot          |
| Compare variables with different units | Dual Y-axis           |
| Show multiple views separately         | Subplots              |
| Display wide frequency ranges          | Logarithmic plot      |
| Show uncertainty                       | Error bars            |
| Display FFT spectrum                   | Frequency-domain plot |

---

# 3. Basic Line Plot

## Use

A line plot is commonly used when one variable changes continuously with another.

Typical examples:

```text
Voltage vs Time
Current vs Time
Temperature vs Time
Efficiency vs Load
Magnitude vs Frequency
```

Basic structure:

```python
plt.plot(x, y)
```

---

# 4. Multiple Line Plot

Use multiple lines when several datasets share the same independent variable.

Example:

```text
Time
 ↓
Voltage Case A
Voltage Case B
Voltage Case C
```

Typical engineering applications:

* Experimental vs Simulation
* Different converter configurations
* Multiple operating conditions
* Multiple control methods
* Several measurement channels

---

# 5. Bar Plot

Bar plots are appropriate for comparing discrete values.

Examples:

```text
Efficiency of Method A, B, C

Peak EMI of Case A, B, C

Power Loss at Different Operating Points
```

A bar plot should generally not be used for continuous time-series data.

---

# 6. Grouped Bar Plot

Grouped bar plots compare multiple quantities for the same categories.

Example:

```text
             100 kHz   1 MHz   10 MHz

Case A          |        |        |
Case B          |        |        |
Case C          |        |        |
```

Useful for:

* Frequency-point comparisons
* Experimental vs simulation results
* Multiple methods at several operating conditions

---

# 7. Scatter Plot

Scatter plots are useful for investigating relationships between two numerical variables.

Examples:

```text
Temperature vs Efficiency

Load Current vs Power Loss

Parasitic Capacitance vs EMI Magnitude
```

They are particularly useful before applying regression or machine learning.

---

# 8. Multiple Variables

A dataset may contain:

```text
Time
Voltage
Current
Power
Temperature
```

Possible approaches include:

### Same scale

Plot variables on the same axis.

### Different scales

Use:

* Subplots
* Normalization
* Dual Y-axis

The selected approach should preserve interpretability.

---

# 9. CSV Visualization Pipeline

```text
CSV File
   ↓
Read Dataset
   ↓
Inspect Header
   ↓
Select X Column
   ↓
Select Y Column(s)
   ↓
Convert / Clean if Required
   ↓
Plot
```

Typical Pandas structure:

```python
import pandas as pd

data = pd.read_csv(
    "measurements.csv"
)
```

Select columns:

```python
time = data["Time"]

voltage = data["Voltage"]
```

Plot:

```python
plt.plot(
    time,
    voltage
)
```

---

# 10. Excel Visualization Pipeline

```text
Excel File
     ↓
Select Worksheet
     ↓
Read Data
     ↓
Inspect Columns
     ↓
Select Required Columns
     ↓
Plot
```

Example:

```python
data = pd.read_excel(
    "measurements.xlsx",
    sheet_name="Test_1"
)
```

This becomes useful when an engineering workbook contains several tests or operating cases.

---

# 11. Plotting Several Columns

Suppose the file contains:

```text
Time
Voltage
Current
Power
Temperature
```

Instead of writing many plotting commands manually:

```python
selected_columns = [
    "Voltage",
    "Current",
    "Power"
]
```

Then:

```python
for column in selected_columns:

    plt.plot(
        data["Time"],
        data[column],
        label=column
    )
```

This approach scales easily from 2 variables to many variables.

---

# 12. Multiple Files

Research data are often stored as:

```text
Case_A.csv
Case_B.csv
Case_C.csv
Case_D.csv
```

The general workflow becomes:

```text
File List
   ↓
Loop Through Files
   ↓
Load Dataset
   ↓
Extract Required Column
   ↓
Plot
   ↓
Add Case Label
```

This avoids repeatedly copying the same plotting command.

---

# 13. Dual Y-Axis

A dual-axis plot is useful when two variables share the same X-axis but have very different units.

Example:

```text
Time
 ↓
Voltage [V]
Current [A]
```

Use carefully because two vertical scales can sometimes make interpretation difficult.

If clarity is reduced, subplots are preferable.

---

# 14. Logarithmic Plots

Logarithmic axes are useful when data span several orders of magnitude.

Engineering applications include:

* Frequency response
* EMI spectra
* FFT results
* Bode plots
* Impedance
* Gain characteristics

Typical frequency axis:

```python
plt.xscale("log")
```

---

# 15. FFT and Frequency-Domain Visualization

A typical FFT plotting workflow is:

```text
Time-Domain Signal
        ↓
Sampling Information
        ↓
FFT
        ↓
Frequency Vector
        ↓
Magnitude
        ↓
Scaling / dB Conversion
        ↓
Frequency Selection
        ↓
Plot
```

Typical final relationship:

```text
Frequency [Hz]
      ↓
Magnitude [dB]
```

This will connect directly with the Signal Processing section.

---

# 16. Axis Labels and Units

Every engineering figure should identify both the variable and its unit.

Good:

```text
Time [s]

Voltage [V]

Current [A]

Frequency [Hz]

Magnitude [dBµV]
```

Weak:

```text
X

Y

Data
```

Correct physical units improve scientific clarity and reproducibility.

---

# 17. Legends

A legend is required when multiple curves or datasets are presented.

Example:

```python
plt.plot(
    time,
    case_a,
    label="Case A"
)

plt.plot(
    time,
    case_b,
    label="Case B"
)

plt.legend()
```

Labels should describe the physical case rather than generic names such as `Data1` or `Series2`.

---

# 18. Axis Limits

Axis limits can focus attention on the region relevant to the analysis.

Example:

```python
plt.xlim(
    0,
    0.01
)
```

For frequency analysis:

```python
plt.xlim(
    1e4,
    30e6
)
```

Limits should not be selected in a way that visually misrepresents the data.

---

# 19. Grid

A grid can improve quantitative interpretation.

Example:

```python
plt.grid(True)
```

Grids should remain visually secondary to the actual data.

---

# 20. Annotations

Annotations can identify:

* Maximum values
* Resonant peaks
* Switching frequency
* Thresholds
* Important operating points
* Experimental events

Example:

```python
plt.annotate(
    "Peak",
    xy=(x_peak, y_peak)
)
```

---

# 21. Error Bars

Error bars represent uncertainty or variability.

They may represent:

* Standard deviation
* Standard error
* Confidence interval
* Measurement uncertainty

Example:

```python
plt.errorbar(
    x,
    y,
    yerr=error
)
```

The meaning of the error bar should always be stated.

---

# 22. Saving Figures

A figure may be saved using:

```python
plt.savefig(
    "figure.png"
)
```

Common formats include:

```text
PNG
PDF
SVG
```

### PNG

Useful for:

* Presentations
* Websites
* General documentation

### PDF

Useful for:

* Academic documents
* Vector graphics
* Journal manuscripts

### SVG

Useful for:

* Vector editing
* Websites
* Scalable graphics

---

# 23. Resolution

Raster figures may require higher resolution.

Example:

```python
plt.savefig(
    "figure.png",
    dpi=300
)
```

Typical values include:

```text
150 DPI → Screen/general use

300 DPI → Common publication quality

600 DPI → High-resolution line/artwork requirements
```

Always follow the requirements of the target journal or publisher.

---

# 24. Publication-Quality Figure Workflow

```text
Processed Data
      ↓
Choose Figure Size
      ↓
Plot Required Data
      ↓
Set Axis Labels + Units
      ↓
Set Limits
      ↓
Set Tick Formatting
      ↓
Add Appropriate Legend
      ↓
Add Necessary Annotation
      ↓
Check Readability
      ↓
Save PDF / SVG / High-DPI PNG
```

---

# 25. Manual Data vs File Data

## Manual Data

Useful for:

* Learning
* Small demonstrations
* Quick calculations

```python
time = [0, 1, 2, 3]

voltage = [0, 20, 40, 50]
```

## CSV / Excel

Preferred for:

* Experiments
* Simulations
* Large datasets
* Research analysis
* Reproducible workflows

---

# 26. Common Mistakes

### Missing axis units

Avoid:

```text
Voltage
```

Prefer:

```text
Voltage [V]
```

### Missing legend

Multiple curves without identification are difficult to interpret.

### Wrong column selection

Always inspect:

```python
print(data.columns)
```

before assuming column names.

### Plotting text as numbers

Check the data type and remove invalid entries where required.

### Excessive curves

Too many curves on a single axis may reduce readability.

Consider:

* Selected representative cases
* Subplots
* Separate figures

### Inappropriate axis scale

Frequency data spanning several decades may require a logarithmic scale.

### Saving after `plt.show()`

Depending on the environment, saving after displaying/closing the figure may produce an empty output.

A safer sequence is:

```python
plt.savefig(
    "figure.png",
    dpi=300
)

plt.show()
```

---

# 27. Quick Plot Selection Guide

```text
Continuous signal?
    ↓
Line Plot

Compare categories?
    ↓
Bar Plot

Compare several category groups?
    ↓
Grouped Bar Plot

Relationship between two variables?
    ↓
Scatter Plot

Variables have different units?
    ↓
Dual Axis or Subplots

Frequency spans several decades?
    ↓
Log Axis

Need uncertainty?
    ↓
Error Bars

Need several independent views?
    ↓
Subplots
```

---

# 28. Research Data Workflow

A complete scientific visualization workflow should ultimately look like:

```text
Experiment / Simulation
         ↓
Raw Data
         ↓
CSV / Excel
         ↓
Pandas
         ↓
Data Cleaning
         ↓
NumPy / SciPy Processing
         ↓
Data Validation
         ↓
Matplotlib
         ↓
Scientific Interpretation
         ↓
Publication Figure
```

---

# 29. Key Takeaway

Scientific plotting is not only about generating a graph.

A useful engineering figure requires:

```text
Correct Data
     +
Correct Plot Type
     +
Correct Units
     +
Clear Labels
     +
Appropriate Scale
     +
Readable Formatting
     +
Reproducible Code
```

The examples in this section progressively demonstrate this complete workflow.
