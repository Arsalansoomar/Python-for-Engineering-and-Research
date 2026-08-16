"""
============================================================
Python for Engineering and Research
05 - Scatter Plot
============================================================

Purpose:
    Introduce scatter plots using Matplotlib and demonstrate
    how relationships between two numerical variables can
    be investigated.

Topics:
    1. What is a scatter plot?
    2. When should it be used?
    3. Required imports
    4. Basic scatter plot
    5. Engineering examples
    6. Marker customization
    7. Correlation
    8. Simple trend line
    9. Measured vs predicted values
    10. Reference line
    11. Point annotations
    12. Outliers
    13. Dense datasets
    14. Saving figures
    15. Common mistakes
    16. Key takeaways

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT IS A SCATTER PLOT?
# ============================================================

"""
A scatter plot displays individual observations as points.

Each point represents:

        X value
           +
        Y value


Example:

Efficiency
   ↑
96 |                  ●
95 |              ●
94 |          ●
93 |      ●
92 |   ●
   +----------------------------→ Temperature


Unlike a line plot, points are not necessarily connected.

Scatter plots are mainly used to investigate relationships
between numerical variables.
"""


# ============================================================
# 2. WHEN SHOULD A SCATTER PLOT BE USED?
# ============================================================

"""
Scatter plots are useful when investigating whether two
numerical variables are related.

Engineering examples:

Temperature vs Efficiency

Load Current vs Power Loss

Voltage vs Current

Switching Frequency vs Loss

Parasitic Capacitance vs EMI Magnitude

Measured vs Simulated Values

Measured vs Predicted Values

Feature vs Target in Machine Learning


Scatter plots can help identify:

- Positive relationships
- Negative relationships
- Weak relationships
- Strong relationships
- Nonlinear relationships
- Clusters
- Outliers
"""


# ============================================================
# 3. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path


# ============================================================
# 4. BASIC DATASET
# ============================================================

"""
Consider converter load current and corresponding
power loss.
"""


load_current = [
    1.0,
    1.5,
    2.0,
    2.5,
    3.0,
    3.5,
    4.0,
    4.5,
    5.0
]


power_loss = [
    4.2,
    5.1,
    6.5,
    8.0,
    10.2,
    12.8,
    16.0,
    19.5,
    23.5
]


# ============================================================
# 5. BASIC SCATTER PLOT
# ============================================================

"""
Basic syntax:

ax.scatter(
    x,
    y
)
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.scatter(
    load_current,
    power_loss
)


ax.set_xlabel(
    "Load Current [A]"
)

ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Load Current vs Power Loss"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 6. INTERPRETING THE RELATIONSHIP
# ============================================================

"""
In this example:

Load Current increases
        ↓
Power Loss generally increases


This suggests a positive relationship.

However:

A scatter plot alone does NOT prove that one variable
causes the other.

It only visualizes the observed relationship.
"""


# ============================================================
# 7. MARKER CUSTOMIZATION
# ============================================================

"""
Useful scatter parameters include:

marker

s
    Marker size

alpha
    Transparency

linewidth


Example:

marker="o"

s=60

alpha=0.7
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.scatter(
    load_current,
    power_loss,
    marker="o",
    s=60,
    alpha=0.8
)


ax.set_xlabel(
    "Load Current [A]"
)

ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Load Current vs Power Loss"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 8. ENGINEERING EXAMPLE - TEMPERATURE VS EFFICIENCY
# ============================================================

"""
Example:

Investigate whether converter efficiency changes with
operating temperature.

The values are synthetic and intended for demonstration.
"""


temperature = [
    35,
    40,
    45,
    50,
    55,
    60,
    65,
    70,
    75,
    80
]


efficiency = [
    95.8,
    95.7,
    95.6,
    95.5,
    95.3,
    95.1,
    94.8,
    94.5,
    94.1,
    93.7
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.scatter(
    temperature,
    efficiency,
    s=60
)


ax.set_xlabel(
    "Temperature [°C]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Temperature vs Converter Efficiency"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 9. POSITIVE AND NEGATIVE RELATIONSHIPS
# ============================================================

"""
POSITIVE RELATIONSHIP

X increases
     ↓
Y generally increases


Example:

Load Current
     ↓
Power Loss


------------------------------------------------------------


NEGATIVE RELATIONSHIP

X increases
     ↓
Y generally decreases


Example:

Temperature
     ↓
Efficiency


------------------------------------------------------------


NO CLEAR RELATIONSHIP

Changes in X do not show a clear pattern with Y.
"""


# ============================================================
# 10. CORRELATION COEFFICIENT
# ============================================================

"""
A scatter plot provides visual information.

A correlation coefficient provides a numerical indication
of the strength and direction of a LINEAR relationship.

NumPy can calculate Pearson correlation using:

np.corrcoef()


Correlation coefficient:

r ≈ +1
    Strong positive linear relationship

r ≈ 0
    Weak or no linear relationship

r ≈ -1
    Strong negative linear relationship


IMPORTANT:

Correlation does not prove causation.
"""


correlation_matrix = np.corrcoef(
    temperature,
    efficiency
)


correlation = correlation_matrix[
    0,
    1
]


print(
    "--- Correlation Example ---"
)

print(
    f"Correlation coefficient = "
    f"{correlation:.3f}"
)


# ============================================================
# 11. DISPLAY CORRELATION ON FIGURE
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.scatter(
    temperature,
    efficiency,
    s=60
)


ax.set_xlabel(
    "Temperature [°C]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Temperature vs Efficiency"
)


ax.text(
    0.05,
    0.08,
    f"Correlation: r = {correlation:.3f}",
    transform=ax.transAxes
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 12. SIMPLE LINEAR TREND
# ============================================================

"""
Sometimes a simple linear trend line can help visualize
the general relationship.

NumPy provides:

np.polyfit()

For a first-order polynomial:

degree = 1

which represents approximately:

y = m*x + b


This is only a visualization example.

Detailed regression analysis will be covered later in the
Machine Learning section.
"""


temperature_array = np.array(
    temperature
)


efficiency_array = np.array(
    efficiency
)


slope, intercept = np.polyfit(
    temperature_array,
    efficiency_array,
    1
)


trend_values = (
    slope
    * temperature_array
    + intercept
)


print(
    "\n--- Linear Trend ---"
)

print(
    f"Slope = {slope:.4f}"
)

print(
    f"Intercept = {intercept:.4f}"
)


# ============================================================
# 13. SCATTER + TREND LINE
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.scatter(
    temperature_array,
    efficiency_array,
    s=60,
    label="Measurements"
)


ax.plot(
    temperature_array,
    trend_values,
    linestyle="--",
    linewidth=2,
    label="Linear Trend"
)


ax.set_xlabel(
    "Temperature [°C]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Temperature vs Efficiency with Linear Trend"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 14. IMPORTANT NOTE ABOUT TREND LINES
# ============================================================

"""
A trend line should not automatically be interpreted as
a valid physical model.

Before claiming a relationship, researchers should consider:

- Physical mechanism
- Data quantity
- Measurement uncertainty
- Outliers
- Operating range
- Model assumptions
- Statistical significance
- Validation data


A visually good line does not automatically mean that the
underlying relationship is physically meaningful.
"""


# ============================================================
# 15. MEASURED VS PREDICTED VALUES
# ============================================================

"""
Scatter plots are commonly used to compare:

Measured Values

vs

Predicted Values


This becomes especially important in machine learning
and model validation.
"""


measured_power = [
    50,
    100,
    150,
    200,
    250,
    300,
    350,
    400
]


predicted_power = [
    52,
    97,
    153,
    198,
    247,
    305,
    347,
    404
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.scatter(
    measured_power,
    predicted_power,
    s=60
)


ax.set_xlabel(
    "Measured Power [W]"
)

ax.set_ylabel(
    "Predicted Power [W]"
)

ax.set_title(
    "Measured vs Predicted Power"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 16. IDEAL REFERENCE LINE
# ============================================================

"""
For measured-vs-predicted plots, an ideal model would satisfy:

Predicted = Measured

Therefore:

y = x

can be displayed as a reference line.

Points close to the line indicate good agreement.
"""


minimum_value = min(
    measured_power
    + predicted_power
)


maximum_value = max(
    measured_power
    + predicted_power
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.scatter(
    measured_power,
    predicted_power,
    s=60,
    label="Predicted Results"
)


ax.plot(
    [
        minimum_value,
        maximum_value
    ],
    [
        minimum_value,
        maximum_value
    ],
    linestyle="--",
    linewidth=1.5,
    label="Ideal: Predicted = Measured"
)


ax.set_xlabel(
    "Measured Power [W]"
)

ax.set_ylabel(
    "Predicted Power [W]"
)

ax.set_title(
    "Measured vs Predicted Power"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 17. EQUAL AXIS LIMITS
# ============================================================

"""
For measured-vs-predicted plots, equal X and Y limits often
make comparison with the y = x line easier to interpret.
"""


fig, ax = plt.subplots(
    figsize=(6, 6)
)


ax.scatter(
    measured_power,
    predicted_power,
    s=60,
    label="Predicted Results"
)


ax.plot(
    [
        0,
        450
    ],
    [
        0,
        450
    ],
    linestyle="--",
    label="Ideal"
)


ax.set_xlim(
    0,
    450
)

ax.set_ylim(
    0,
    450
)


ax.set_xlabel(
    "Measured Power [W]"
)

ax.set_ylabel(
    "Predicted Power [W]"
)

ax.set_title(
    "Measured vs Predicted Power"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 18. POINT ANNOTATIONS
# ============================================================

"""
Individual observations can be labeled using:

ax.annotate()


This may be useful when every point represents a specific:

- Experiment
- Operating point
- Material
- Converter configuration
- Measurement case
"""


switching_frequency_khz = [
    50,
    75,
    100,
    125,
    150
]


switching_loss = [
    8.5,
    11.2,
    14.8,
    18.6,
    23.5
]


case_labels = [
    "50 kHz",
    "75 kHz",
    "100 kHz",
    "125 kHz",
    "150 kHz"
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.scatter(
    switching_frequency_khz,
    switching_loss,
    s=60
)


for x_value, y_value, label in zip(

    switching_frequency_khz,
    switching_loss,
    case_labels

):

    ax.annotate(
        label,
        (
            x_value,
            y_value
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Switching Loss [W]"
)

ax.set_title(
    "Switching Frequency vs Switching Loss"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 19. OUTLIERS
# ============================================================

"""
Scatter plots are useful for identifying unusual
observations.

Consider the dataset below.
"""


current_data = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
]


loss_data = [
    3,
    5,
    8,
    12,
    17,
    23,
    45,
    38
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.scatter(
    current_data,
    loss_data,
    s=60
)


ax.set_xlabel(
    "Current [A]"
)

ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Scatter Plot with Possible Outlier"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show())


# ============================================================
# 20. IMPORTANT NOTE ABOUT OUTLIERS
# ============================================================

"""
An unusual point should NOT automatically be deleted.

Before removing an outlier, investigate whether it is:

- Measurement error
- Sensor error
- Data-entry error
- Real physical behavior
- Different operating condition
- System fault
- Experimental anomaly


In research, removing data should always have a justified
reason.
"""


# ============================================================
# 21. DENSE SCATTER DATA
# ============================================================

"""
When many points overlap, transparency can improve
visibility.

The alpha parameter controls transparency.

Example:

alpha=0.4
"""


np.random.seed(
    42
)


sample_current = np.random.uniform(
    1,
    10,
    200
)


sample_loss = (
    0.7
    * sample_current ** 2
    + np.random.normal(
        0,
        4,
        200
    )
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.scatter(
    sample_current,
    sample_loss,
    alpha=0.5,
    s=35
)


ax.set_xlabel(
    "Current [A]"
)

ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Dense Scatter Dataset"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 22. MULTIPLE SCATTER GROUPS
# ============================================================

"""
Different experimental groups can also be displayed on
the same scatter plot.

Use this only when the groups share compatible variables
and units.
"""


temperature_case_a = [
    40,
    50,
    60,
    70,
    80
]


efficiency_case_a = [
    95.5,
    95.2,
    94.9,
    94.5,
    94.0
]


temperature_case_b = [
    40,
    50,
    60,
    70,
    80
]


efficiency_case_b = [
    96.0,
    95.8,
    95.5,
    95.2,
    94.9
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.scatter(
    temperature_case_a,
    efficiency_case_a,
    marker="o",
    s=60,
    label="Case A"
)


ax.scatter(
    temperature_case_b,
    efficiency_case_b,
    marker="s",
    s=60,
    label="Case B"
)


ax.set_xlabel(
    "Temperature [°C]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Temperature-Efficiency Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 23. SCATTER VS LINE PLOT
# ============================================================

"""
SCATTER PLOT

Best for:

Relationship between observations


Example:

Temperature vs Efficiency

Measured vs Predicted

Capacitance vs Magnitude


------------------------------------------------------------


LINE PLOT

Best for:

Ordered or continuous progression


Example:

Time vs Voltage

Frequency vs Magnitude

Load vs Efficiency


------------------------------------------------------------


Sometimes both can be used together:

Scatter points
      +
Trend / model line
"""


# ============================================================
# 24. SCATTER VS BAR PLOT
# ============================================================

"""
SCATTER PLOT

X and Y are numerical variables.

Example:

Current [A]
vs
Power Loss [W]


------------------------------------------------------------


BAR PLOT

X represents discrete categories.

Example:

Case A
Case B
Case C

vs

Power Loss [W]
"""


# ============================================================
# 25. SAVE FINAL FIGURE
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


ax.scatter(
    temperature_array,
    efficiency_array,
    s=60,
    label="Measurements"
)


ax.plot(
    temperature_array,
    trend_values,
    linestyle="--",
    linewidth=2,
    label="Linear Trend"
)


ax.set_xlabel(
    "Temperature [°C]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Temperature vs Converter Efficiency"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()


# ============================================================
# 26. SAVE PNG
# ============================================================

png_file = (
    output_folder
    / "scatter_plot.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 27. SAVE PDF
# ============================================================

pdf_file = (
    output_folder
    / "scatter_plot.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 28. SAVE SVG
# ============================================================

svg_file = (
    output_folder
    / "scatter_plot.svg"
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
# 29. COMMON MISTAKE - CONNECTING ALL SCATTER POINTS
# ============================================================

"""
If observations do not have a meaningful sequence,
connecting them with lines may imply a relationship
that does not exist.

For correlation-type data:

ax.scatter(
    x,
    y
)

is generally preferable to:

ax.plot(
    x,
    y
)
"""


# ============================================================
# 30. COMMON MISTAKE - CORRELATION = CAUSATION
# ============================================================

"""
A strong correlation does NOT automatically mean:

X causes Y.


For example:

Two variables may both depend on another variable.

Engineering interpretation should therefore combine:

Data
+
Statistics
+
Physical understanding
+
Experimental evidence
"""


# ============================================================
# 31. COMMON MISTAKE - REMOVING OUTLIERS AUTOMATICALLY
# ============================================================

"""
Do not remove unusual observations only because they make
the plot look less clean.

Investigate the reason first.

Research data must remain traceable and scientifically
justifiable.
"""


# ============================================================
# 32. COMMON MISTAKE - DIFFERENT DATA LENGTHS
# ============================================================

"""
Each observation needs one X and one Y value.

Incorrect:

X:

10 observations

Y:

9 observations


Correct:

X and Y must contain corresponding observations.
"""


# ============================================================
# 33. COMMON MISTAKE - USING CATEGORY DATA
# ============================================================

"""
Scatter plots require numerical X values.

For:

Case A
Case B
Case C

use a bar plot.

For:

Temperature = 40, 50, 60 °C

use a scatter plot when investigating the relationship
between temperature and another numerical quantity.
"""


# ============================================================
# 34. SCATTER PLOT WORKFLOW
# ============================================================

"""
Define Research Question
        ↓
Select Numerical X Variable
        ↓
Select Numerical Y Variable
        ↓
Check Corresponding Observations
        ↓
Create Scatter Plot
        ↓
Inspect Relationship
        ↓
Check Possible Outliers
        ↓
Calculate Correlation if Appropriate
        ↓
Add Trend Model if Justified
        ↓
Interpret Physically
        ↓
Save Figure
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
SCATTER PLOTS


1. BASIC SCATTER PLOT

fig, ax = plt.subplots()


ax.scatter(
    x,
    y
)


------------------------------------------------------------


2. X AND Y SHOULD NORMALLY BE NUMERICAL

Example:

Current [A]

vs

Power Loss [W]


------------------------------------------------------------


3. SCATTER PLOTS HELP IDENTIFY

Positive relationships

Negative relationships

Weak relationships

Strong relationships

Clusters

Outliers

Nonlinear behavior


------------------------------------------------------------


4. CORRELATION

correlation = np.corrcoef(
    x,
    y
)[0, 1]


Approximate interpretation:

+1
Strong positive linear relationship

0
Weak/no linear relationship

-1
Strong negative linear relationship


------------------------------------------------------------


5. IMPORTANT

Correlation does NOT prove causation.


------------------------------------------------------------


6. SIMPLE TREND LINE

slope, intercept = np.polyfit(
    x,
    y,
    1
)


trend = (
    slope * x
    + intercept
)


------------------------------------------------------------


7. MEASURED VS PREDICTED

Scatter plots are particularly useful for:

Measured values
        ↓
Predicted values


Ideal agreement:

Predicted = Measured


------------------------------------------------------------


8. OUTLIERS

Investigate unusual points before removing them.


------------------------------------------------------------


9. LARGE DATASETS

Use transparency:

ax.scatter(
    x,
    y,
    alpha=0.5
)


------------------------------------------------------------


10. ENGINEERING APPLICATIONS

- Temperature vs Efficiency
- Current vs Power Loss
- Frequency vs Loss
- Parasitic Parameter vs EMI
- Measured vs Simulated
- Measured vs Predicted
- Experimental correlation analysis
- Machine-learning feature analysis


------------------------------------------------------------


11. VISUALIZATION SELECTION

Time → Voltage
    LINE PLOT

Case → Efficiency
    BAR PLOT

Several Cases at Same Categories
    GROUPED BAR PLOT

Temperature → Efficiency
    SCATTER PLOT


------------------------------------------------------------


12. IMPORTANT RESEARCH PRINCIPLE

Scatter Plot
      ↓
Observe Relationship
      ↓
Quantify Relationship
      ↓
Check Physical Meaning
      ↓
Validate
      ↓
Interpret


A visually strong relationship should not be treated as a
scientific conclusion without appropriate validation.


------------------------------------------------------------


NEXT:

06_multiple_variables.py

will address one of the most common practical questions:

"I have Time, Voltage, Current, Power and Temperature.
How should I visualize several variables?"

We will cover:

Same-axis variables
Different units
Normalization
Automatic plotting with dictionaries
When NOT to put everything on one figure
"""
