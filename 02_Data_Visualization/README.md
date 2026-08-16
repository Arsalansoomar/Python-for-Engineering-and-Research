# Data Visualization with Python

This section provides practical examples of **scientific and engineering data visualization using Python and Matplotlib**.

The examples progress from simple manually defined data to CSV/Excel datasets, multiple-variable comparisons, frequency-domain plots, and publication-quality figures.

The objective is not only to demonstrate plotting commands, but also to explain **how engineering and research data move from a raw dataset to a clear and reproducible figure**.

---

## Learning Workflow

```text
Manual Data
    ↓
Basic Line Plot
    ↓
Multiple Variables
    ↓
Bar / Scatter / Grouped Plots
    ↓
CSV Data
    ↓
Excel Data
    ↓
Multiple Files / Cases
    ↓
Engineering Data Processing
    ↓
Frequency / FFT Visualization
    ↓
Publication-Quality Figures
```

---

## What This Section Covers

### Basic Visualization

* Basic line plots
* Multiple line plots
* Bar plots
* Grouped bar plots
* Scatter plots
* Multiple variables
* Subplots

### External Data

* Plotting from CSV files
* Plotting from Excel files
* Selecting specific columns
* Selecting Excel worksheets
* Comparing multiple CSV files
* Comparing multiple Excel files

### Scientific and Engineering Visualization

* Dual Y-axis plots
* Logarithmic axes
* Axis limits and tick control
* Legends and annotations
* Error bars
* FFT and frequency-domain plots
* Engineering case comparisons

### Figure Export

* PNG
* PDF
* SVG
* High-resolution figures
* Publication-quality formatting

---

## Typical Data Visualization Pipeline

```text
Raw Data
   ↓
CSV / Excel / Python Variables
   ↓
Load Data
   ↓
Inspect Columns
   ↓
Select Required Variables
   ↓
Clean / Process Data
   ↓
Choose Appropriate Plot
   ↓
Add Labels and Units
   ↓
Format Figure
   ↓
Validate Visualization
   ↓
Save Figure
```

---

## Example Applications

The examples are designed around typical engineering and research problems such as:

* Voltage vs Time
* Current vs Time
* Voltage and Current comparison
* Power vs Load
* Efficiency vs Load
* Temperature vs Operating Condition
* Multiple experimental cases
* Multiple simulation cases
* Frequency response
* FFT magnitude vs Frequency
* Comparative engineering results
* Experimental and simulation-data visualization

---

## Standard Plot Structure

Most examples follow the same learning structure:

1. What is the plot?
2. When should it be used?
3. Required imports
4. Example dataset
5. Basic plotting code
6. Engineering example
7. Plot customization
8. Saving the figure
9. Common mistakes
10. Key takeaway

This structure makes each file useful both as a beginner tutorial and as a quick revision reference.

---

## Core Libraries

The main plotting library used in this section is:

```python
import matplotlib.pyplot as plt
```

Additional libraries will be used where required:

```python
import numpy as np
import pandas as pd
```

Their main roles are:

```text
NumPy
    Numerical data and arrays

Pandas
    CSV / Excel and tabular datasets

Matplotlib
    Scientific visualization
```

---

## Basic Example

```python
import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4]

voltage = [0, 24, 48, 47, 46]

plt.plot(time, voltage)

plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("Voltage vs Time")

plt.grid(True)

plt.show()
```

---

## Multiple Variables

The section also demonstrates how to move from:

```text
One X variable
+
One Y variable
```

to:

```text
Time
+
Voltage
+
Current
+
Power
+
Temperature
+
Multiple Experimental Cases
```

without unnecessarily repeating plotting code.

---

## CSV and Excel Workflow

A major focus of this section is practical external-data visualization.

```text
CSV / Excel File
       ↓
Read File
       ↓
Check Column Names
       ↓
Select X Column
       ↓
Select One or More Y Columns
       ↓
Plot
       ↓
Format
       ↓
Save
```

Typical examples include:

```python
data["Time"]
data["Voltage"]
data["Current"]
```

and eventually:

```python
for column in selected_columns:
    plt.plot(
        data["Time"],
        data[column],
        label=column
    )
```

---

## Publication-Quality Figures

Later examples demonstrate how to prepare figures suitable for:

* Research papers
* Journal manuscripts
* Thesis documents
* Conference papers
* Presentations
* Technical reports

The section includes figure sizing, fonts, legends, axis formatting, resolution, and export to formats such as:

```text
PNG
PDF
SVG
```

---

## Important Principle

A good scientific plot should communicate the result clearly without requiring the reader to inspect the source code.

Every figure should therefore contain appropriate:

* Axis labels
* Physical units
* Legends
* Scale selection
* Readable tick labels
* Appropriate limits
* Meaningful annotations where necessary

---

## Intended Audience

This section may be useful for:

* Engineering students
* Graduate researchers
* PhD researchers
* Electrical and electronics engineers
* Power electronics researchers
* Data analysts
* Researchers beginning scientific Python visualization

---

## Related Sections

The visualization examples build on concepts introduced in:

```text
Python Basics
      ↓
NumPy
      ↓
Pandas
      ↓
Data Visualization
```

Later sections will extend these concepts into:

```text
Signal Processing
Machine Learning
Engineering Applications
```
