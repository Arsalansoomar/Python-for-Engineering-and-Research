"""
============================================================
Python for Engineering and Research
29 - Broken Axis and Discontinuous Ranges
============================================================

Purpose:
    Demonstrate how broken axes can be used when one or more
    extreme values compress important engineering details.

Topics:
    1. What is a broken axis?
    2. Why use a broken axis?
    3. When NOT to use one
    4. Normal plot before breaking an axis
    5. Broken Y-axis
    6. Shared X-axis
    7. Hidden spines
    8. Diagonal break marks
    9. Line plots
    10. Scatter plots
    11. Bar plots with extreme values
    12. Broken X-axis
    13. Discontinuous frequency ranges
    14. Multiple engineering cases
    15. Consistent case styles
    16. Different panel-height ratios
    17. Automatic break limits
    18. Reusable broken-Y function
    19. Reusable broken-X function
    20. Publication formatting
    21. PNG / PDF / SVG export
    22. Broken axis vs logarithmic axis
    23. Broken axis vs inset
    24. Broken axis vs subplots
    25. Scientific integrity
    26. Common mistakes
    27. Key takeaways

Important:
    A broken axis intentionally removes part of the visible
    numerical range.

    The omitted range must therefore be obvious to the
    reader.

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


# ============================================================
# 2. WHAT IS A BROKEN AXIS?
# ============================================================

"""
A broken axis displays separated parts of one numerical
range while intentionally omitting another region.

Example:

Y-axis:

100
 95
 90
 85
 //     <- omitted region
 //
 15
 10
  5
  0


The purpose is usually to show:

Large values

and

Small but important variations


without allowing the large values to compress the smaller
region.
"""


# ============================================================
# 3. ENGINEERING APPLICATIONS
# ============================================================

"""
Broken axes may occasionally be useful for:

- One large outlier
- Startup peak + small steady-state variation
- Extreme fault current + normal current
- Large transient + low ripple
- One much larger bar value
- Thermal events
- Experimental outliers
- Widely separated operating ranges
- Selected frequency ranges


However:

A broken axis should not be the default solution.
"""


# ============================================================
# 4. FIRST CONSIDER ALTERNATIVES
# ============================================================

"""
Before using a broken axis, consider:

1. Logarithmic axis

2. Inset / zoomed plot

3. Separate subplots

4. Normalization

5. Difference plot

6. Separate figure


A broken axis is most useful when:

Two separated numerical regions genuinely need to be
viewed together.
"""


# ============================================================
# 5. PROJECT PATHS
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


output_figure_folder = (
    script_folder
    / "output_figures"
    / "broken_axis"
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
# 6. CREATE REPRODUCIBLE EXAMPLE DATA
# ============================================================

rng = np.random.default_rng(
    42
)


sample_number = np.arange(
    1,
    31
)


measurement = rng.normal(

    loc=10,

    scale=1.0,

    size=len(
        sample_number
    )

)


# Add two large values

measurement[
    7
] = 82


measurement[
    22
] = 91


# ============================================================
# 7. NORMAL PLOT FIRST
# ============================================================

"""
Always inspect the normal unbroken plot first.

This allows us to see why a broken axis might be useful.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    sample_number,

    measurement,

    marker="o"

)


ax.set_xlabel(
    "Sample Number"
)

ax.set_ylabel(
    "Measured Value [-]"
)

ax.set_title(
    "Normal Axis"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 8. PROBLEM WITH THE NORMAL AXIS
# ============================================================

"""
Most values are near:

8 to 12


but two values are near:

80 to 90


Therefore the normal axis uses approximately:

0 to 100


The smaller variations become visually compressed.
"""


# ============================================================
# 9. BASIC BROKEN Y-AXIS
# ============================================================

"""
A common broken-Y approach uses:

Two vertically stacked axes

with:

sharex=True


Both axes contain the SAME data.

The upper axis displays the high-value region.

The lower axis displays the low-value region.
"""


fig, (
    ax_top,
    ax_bottom
) = plt.subplots(

    2,

    1,

    sharex=True,

    figsize=(8, 5.5)

)


# Plot identical data on both axes

ax_top.plot(

    sample_number,

    measurement,

    marker="o"

)


ax_bottom.plot(

    sample_number,

    measurement,

    marker="o"

)


# Different visible Y ranges

ax_top.set_ylim(
    75,
    100
)


ax_bottom.set_ylim(
    6,
    14
)


ax_bottom.set_xlabel(
    "Sample Number"
)


ax_top.set_ylabel(
    "Measured Value [-]"
)


ax_bottom.set_ylabel(
    "Measured Value [-]"
)


plt.show()


# ============================================================
# 10. REDUCE SPACE BETWEEN AXES
# ============================================================

"""
The two axes should visually behave like two parts of one
figure.

Reduce the vertical gap.
"""


fig, (
    ax_top,
    ax_bottom
) = plt.subplots(

    2,

    1,

    sharex=True,

    figsize=(8, 5.5)

)


fig.subplots_adjust(
    hspace=0.05
)


for ax in [
    ax_top,
    ax_bottom
]:

    ax.plot(

        sample_number,

        measurement,

        marker="o"

    )


ax_top.set_ylim(
    75,
    100
)


ax_bottom.set_ylim(
    6,
    14
)


plt.show()


# ============================================================
# 11. HIDE TOUCHING SPINES
# ============================================================

"""
To visually communicate a discontinuity:

Hide:

Bottom spine of upper axis

and:

Top spine of lower axis.
"""


fig, (
    ax_top,
    ax_bottom
) = plt.subplots(

    2,

    1,

    sharex=True,

    figsize=(8, 5.5)

)


fig.subplots_adjust(
    hspace=0.05
)


for ax in [
    ax_top,
    ax_bottom
]:

    ax.plot(

        sample_number,

        measurement,

        marker="o"

    )


ax_top.set_ylim(
    75,
    100
)


ax_bottom.set_ylim(
    6,
    14
)


# Hide touching spines

ax_top.spines[
    "bottom"
].set_visible(
    False
)


ax_bottom.spines[
    "top"
].set_visible(
    False
)


# Hide top-axis X tick labels

ax_top.tick_params(

    axis="x",

    which="both",

    bottom=False,

    labelbottom=False

)


ax_bottom.set_xlabel(
    "Sample Number"
)


plt.show()


# ============================================================
# 12. ADD DIAGONAL BREAK MARKS
# ============================================================

"""
Diagonal marks make the omitted range explicit.

The marks are drawn in axis coordinates so that they stay
attached to the axes when the figure is resized.
"""


fig, (
    ax_top,
    ax_bottom
) = plt.subplots(

    2,

    1,

    sharex=True,

    figsize=(8, 5.5)

)


fig.subplots_adjust(
    hspace=0.05
)


for ax in [
    ax_top,
    ax_bottom
]:

    ax.plot(

        sample_number,

        measurement,

        marker="o"

    )


ax_top.set_ylim(
    75,
    100
)


ax_bottom.set_ylim(
    6,
    14
)


ax_top.spines[
    "bottom"
].set_visible(
    False
)


ax_bottom.spines[
    "top"
].set_visible(
    False
)


ax_top.tick_params(

    axis="x",

    which="both",

    bottom=False,

    labelbottom=False

)


# ------------------------------------------------------------
# Diagonal break marks
# ------------------------------------------------------------

diagonal_size = 0.012


break_style = dict(

    color="k",

    clip_on=False,

    linewidth=1

)


# Upper axis: bottom marks

ax_top.plot(

    (
        -diagonal_size,
        +diagonal_size
    ),

    (
        -diagonal_size,
        +diagonal_size
    ),

    transform=ax_top.transAxes,

    **break_style

)


ax_top.plot(

    (
        1 - diagonal_size,
        1 + diagonal_size
    ),

    (
        -diagonal_size,
        +diagonal_size
    ),

    transform=ax_top.transAxes,

    **break_style

)


# Lower axis: top marks

ax_bottom.plot(

    (
        -diagonal_size,
        +diagonal_size
    ),

    (
        1 - diagonal_size,
        1 + diagonal_size
    ),

    transform=ax_bottom.transAxes,

    **break_style

)


ax_bottom.plot(

    (
        1 - diagonal_size,
        1 + diagonal_size
    ),

    (
        1 - diagonal_size,
        1 + diagonal_size
    ),

    transform=ax_bottom.transAxes,

    **break_style

)


ax_bottom.set_xlabel(
    "Sample Number"
)


fig.supylabel(
    "Measured Value [-]"
)


plt.show()


# ============================================================
# 13. COMPLETE BROKEN Y-AXIS EXAMPLE
# ============================================================

fig, (
    ax_top,
    ax_bottom
) = plt.subplots(

    2,

    1,

    sharex=True,

    figsize=(8, 5.5),

    height_ratios=[
        1,
        2
    ]

)


fig.subplots_adjust(
    hspace=0.05
)


for ax in [
    ax_top,
    ax_bottom
]:

    ax.plot(

        sample_number,

        measurement,

        marker="o",

        linewidth=1.3

    )


    ax.grid(
        True,
        alpha=0.35
    )


ax_top.set_ylim(
    75,
    100
)


ax_bottom.set_ylim(
    6,
    14
)


ax_top.spines[
    "bottom"
].set_visible(
    False
)


ax_bottom.spines[
    "top"
].set_visible(
    False
)


ax_top.tick_params(

    axis="x",

    bottom=False,

    labelbottom=False

)


# Break marks

diagonal_size = 0.012


break_style = dict(

    color="k",

    clip_on=False,

    linewidth=1

)


for x_position in [
    0,
    1
]:

    ax_top.plot(

        (
            x_position
            - diagonal_size,

            x_position
            + diagonal_size
        ),

        (
            -diagonal_size,
            +diagonal_size
        ),

        transform=ax_top.transAxes,

        **break_style

    )


    ax_bottom.plot(

        (
            x_position
            - diagonal_size,

            x_position
            + diagonal_size
        ),

        (
            1 - diagonal_size,
            1 + diagonal_size
        ),

        transform=ax_bottom.transAxes,

        **break_style

    )


ax_bottom.set_xlabel(
    "Sample Number"
)


fig.supylabel(
    "Measured Value [-]"
)


plt.show()


# ============================================================
# 14. HEIGHT RATIOS
# ============================================================

"""
The displayed range:

6 to 14

contains most of the engineering information.

The upper range:

75 to 100

contains only two extreme points.

Therefore:

height_ratios=[1, 2]

gives more visual space to the lower region.


This is a design choice.

The omitted range must still remain obvious.
"""


# ============================================================
# 15. BROKEN AXIS WITH SCATTER DATA
# ============================================================

fig, (
    ax_top,
    ax_bottom
) = plt.subplots(

    2,

    1,

    sharex=True,

    figsize=(8, 5.5)

)


fig.subplots_adjust(
    hspace=0.05
)


for ax in [
    ax_top,
    ax_bottom
]:

    ax.scatter(

        sample_number,

        measurement,

        s=30

    )


ax_top.set_ylim(
    75,
    100
)


ax_bottom.set_ylim(
    6,
    14
)


ax_top.spines[
    "bottom"
].set_visible(
    False
)


ax_bottom.spines[
    "top"
].set_visible(
    False
)


ax_top.tick_params(

    bottom=False,

    labelbottom=False

)


plt.show()


# ============================================================
# 16. ENGINEERING BAR-PLOT EXAMPLE
# ============================================================

"""
Broken axes are often seen in bar plots when one category
is much larger than the others.

Use especially carefully because bar-chart height strongly
communicates magnitude.
"""


design_names = [

    "Design A",

    "Design B",

    "Design C",

    "Design D",

    "Fault Case"

]


power_loss_w = np.array(
    [
        12.2,
        10.8,
        9.9,
        11.5,
        72.0
    ]
)


# ============================================================
# 17. NORMAL BAR PLOT FIRST
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.bar(

    design_names,

    power_loss_w

)


ax.set_ylabel(
    "Power Loss [W]"
)

ax.set_title(
    "Power-Loss Comparison"
)


ax.grid(
    True,
    axis="y"
)


plt.tight_layout()

plt.show()


# ============================================================
# 18. BROKEN-Y BAR PLOT
# ============================================================

fig, (
    ax_top,
    ax_bottom
) = plt.subplots(

    2,

    1,

    sharex=True,

    figsize=(8, 5.8),

    height_ratios=[
        1,
        2
    ]

)


fig.subplots_adjust(
    hspace=0.05
)


# Plot same bars on both axes

ax_top.bar(

    design_names,

    power_loss_w

)


ax_bottom.bar(

    design_names,

    power_loss_w

)


# Visible ranges

ax_top.set_ylim(
    65,
    76
)


ax_bottom.set_ylim(
    0,
    16
)


# Hide touching spines

ax_top.spines[
    "bottom"
].set_visible(
    False
)


ax_bottom.spines[
    "top"
].set_visible(
    False
)


ax_top.tick_params(

    axis="x",

    bottom=False,

    labelbottom=False

)


ax_bottom.tick_params(

    axis="x",

    rotation=15

)


# Break marks

diagonal_size = 0.012


for x_position in [
    0,
    1
]:

    ax_top.plot(

        (
            x_position
            - diagonal_size,

            x_position
            + diagonal_size
        ),

        (
            -diagonal_size,
            + diagonal_size
        ),

        transform=ax_top.transAxes,

        color="k",

        clip_on=False

    )


    ax_bottom.plot(

        (
            x_position
            - diagonal_size,

            x_position
            + diagonal_size
        ),

        (
            1 - diagonal_size,
            1 + diagonal_size
        ),

        transform=ax_bottom.transAxes,

        color="k",

        clip_on=False

    )


fig.supylabel(
    "Power Loss [W]"
)


plt.show()


# ============================================================
# 19. BAR-PLOT WARNING
# ============================================================

"""
Broken bar-chart axes require particular caution.

A bar normally communicates magnitude relative to a
baseline.

Breaking the numerical range interrupts that geometric
relationship.

Therefore:

Always show the break clearly.

Consider whether another plot type would communicate the
result more honestly.
"""


# ============================================================
# 20. ENGINEERING TRANSIENT EXAMPLE
# ============================================================

"""
Example:

Current is normally near:

5 A

but contains a short fault transient near:

80 A.
"""


time_ms = np.linspace(
    0,
    10,
    2000
)


normal_current = (

    5

    + 0.25
    * np.sin(
        2
        * np.pi
        * 0.8
        * time_ms
    )

)


fault_center_ms = 5


fault_pulse = (

    75

    * np.exp(
        -(
            (
                time_ms
                - fault_center_ms
            )

            / 0.08
        ) ** 2
    )

)


current_a = (

    normal_current

    + fault_pulse

)


# ============================================================
# 21. NORMAL TRANSIENT PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    current_a
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Current [A]"
)

ax.set_title(
    "Fault Current"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 22. BROKEN-Y TRANSIENT PLOT
# ============================================================

fig, (
    ax_top,
    ax_bottom
) = plt.subplots(

    2,

    1,

    sharex=True,

    figsize=(8, 5.8),

    height_ratios=[
        1,
        2
    ]

)


fig.subplots_adjust(
    hspace=0.05
)


for ax in [
    ax_top,
    ax_bottom
]:

    ax.plot(

        time_ms,

        current_a,

        linewidth=1.3

    )


    ax.grid(
        True,
        alpha=0.35
    )


ax_top.set_ylim(
    65,
    85
)


ax_bottom.set_ylim(
    4,
    6
)


ax_top.spines[
    "bottom"
].set_visible(
    False
)


ax_bottom.spines[
    "top"
].set_visible(
    False
)


ax_top.tick_params(

    axis="x",

    bottom=False,

    labelbottom=False

)


ax_bottom.set_xlabel(
    "Time [ms]"
)


fig.supylabel(
    "Current [A]"
)


# Break marks

diagonal_size = 0.012


for x_position in [
    0,
    1
]:

    ax_top.plot(

        (
            x_position
            - diagonal_size,

            x_position
            + diagonal_size
        ),

        (
            -diagonal_size,
            +diagonal_size
        ),

        transform=ax_top.transAxes,

        color="k",

        clip_on=False

    )


    ax_bottom.plot(

        (
            x_position
            - diagonal_size,

            x_position
            + diagonal_size
        ),

        (
            1 - diagonal_size,
            1 + diagonal_size
        ),

        transform=ax_bottom.transAxes,

        color="k",

        clip_on=False

    )


plt.show()


# ============================================================
# 23. BROKEN Y vs INSET
# ============================================================

"""
For the fault-current example:

BROKEN Y-AXIS

shows:

Normal region
+
Fault region


but removes the middle Y range.


------------------------------------------------------------


INSET

keeps the complete main scale

and magnifies one region.


For many engineering papers:

Inset may be easier to interpret.


The correct choice depends on the scientific question.
"""


# ============================================================
# 24. BROKEN X-AXIS
# ============================================================

"""
An X-axis can also be discontinuous.

Example:

The researcher wants to show:

0 to 2 ms

and:

8 to 10 ms


while omitting:

2 to 8 ms.


Use this only when the omitted interval is made obvious.
"""


time_long_ms = np.linspace(
    0,
    10,
    2000
)


signal_v = (

    20

    + 2
    * np.sin(
        2
        * np.pi
        * 0.8
        * time_long_ms
    )

)


# ============================================================
# 25. BASIC BROKEN X-AXIS
# ============================================================

fig, (
    ax_left,
    ax_right
) = plt.subplots(

    1,

    2,

    sharey=True,

    figsize=(9, 4.5),

    width_ratios=[
        1,
        1
    ]

)


fig.subplots_adjust(
    wspace=0.05
)


# Plot same data

ax_left.plot(
    time_long_ms,
    signal_v
)


ax_right.plot(
    time_long_ms,
    signal_v
)


# Different X ranges

ax_left.set_xlim(
    0,
    2
)


ax_right.set_xlim(
    8,
    10
)


# Hide touching spines

ax_left.spines[
    "right"
].set_visible(
    False
)


ax_right.spines[
    "left"
].set_visible(
    False
)


ax_right.tick_params(

    axis="y",

    left=False,

    labelleft=False

)


ax_left.set_ylabel(
    "Voltage [V]"
)


fig.supxlabel(
    "Time [ms]"
)


plt.show()


# ============================================================
# 26. ADD BROKEN-X MARKS
# ============================================================

fig, (
    ax_left,
    ax_right
) = plt.subplots(

    1,

    2,

    sharey=True,

    figsize=(9, 4.5)

)


fig.subplots_adjust(
    wspace=0.05
)


ax_left.plot(
    time_long_ms,
    signal_v
)


ax_right.plot(
    time_long_ms,
    signal_v
)


ax_left.set_xlim(
    0,
    2
)


ax_right.set_xlim(
    8,
    10
)


ax_left.spines[
    "right"
].set_visible(
    False
)


ax_right.spines[
    "left"
].set_visible(
    False
)


ax_right.tick_params(

    axis="y",

    left=False,

    labelleft=False

)


diagonal_size = 0.015


# Right edge of left axis

ax_left.plot(

    (
        1 - diagonal_size,
        1 + diagonal_size
    ),

    (
        -diagonal_size,
        +diagonal_size
    ),

    transform=ax_left.transAxes,

    color="k",

    clip_on=False

)


ax_left.plot(

    (
        1 - diagonal_size,
        1 + diagonal_size
    ),

    (
        1 - diagonal_size,
        1 + diagonal_size
    ),

    transform=ax_left.transAxes,

    color="k",

    clip_on=False

)


# Left edge of right axis

ax_right.plot(

    (
        -diagonal_size,
        +diagonal_size
    ),

    (
        -diagonal_size,
        +diagonal_size
    ),

    transform=ax_right.transAxes,

    color="k",

    clip_on=False

)


ax_right.plot(

    (
        -diagonal_size,
        +diagonal_size
    ),

    (
        1 - diagonal_size,
        1 + diagonal_size
    ),

    transform=ax_right.transAxes,

    color="k",

    clip_on=False

)


ax_left.set_ylabel(
    "Voltage [V]"
)


fig.supxlabel(
    "Time [ms]"
)


plt.show()


# ============================================================
# 27. DISCONTINUOUS FREQUENCY RANGES
# ============================================================

"""
Broken X axes can be useful for selected separated
frequency regions.

Example:

100 kHz to 500 kHz

and:

10 MHz to 30 MHz


Important:

The missing middle frequency range must remain obvious.
"""


frequency_hz = np.logspace(

    4,

    np.log10(
        30e6
    ),

    800

)


spectrum_dbuV = (

    105

    - 7
    * (
        np.log10(
            frequency_hz
        )
        - 4
    )

    + 4
    * np.sin(
        5
        * np.log10(
            frequency_hz
        )
    )

)


# ============================================================
# 28. TWO SELECTED FREQUENCY WINDOWS
# ============================================================

fig, (
    ax_low,
    ax_high
) = plt.subplots(

    1,

    2,

    sharey=True,

    figsize=(9, 4.5),

    width_ratios=[
        1,
        1
    ]

)


fig.subplots_adjust(
    wspace=0.05
)


for ax in [
    ax_low,
    ax_high
]:

    ax.plot(

        frequency_hz,

        spectrum_dbuV

    )


    ax.set_xscale(
        "log"
    )


    ax.grid(
        True,
        which="both"
    )


ax_low.set_xlim(
    100e3,
    500e3
)


ax_high.set_xlim(
    10e6,
    30e6
)


ax_low.spines[
    "right"
].set_visible(
    False
)


ax_high.spines[
    "left"
].set_visible(
    False
)


ax_high.tick_params(

    axis="y",

    left=False,

    labelleft=False

)


ax_low.set_ylabel(
    "Magnitude [dBµV]"
)


fig.supxlabel(
    "Frequency [Hz]"
)


plt.show()


# ============================================================
# 29. FREQUENCY WARNING
# ============================================================

"""
A broken frequency axis can make the omitted spectral range
easy to overlook.

For full-spectrum engineering results:

A complete logarithmic spectrum is often preferable.

Use a broken frequency axis mainly when the separated bands
are specifically the subject of the comparison.
"""


# ============================================================
# 30. MULTIPLE CASES WITH BROKEN Y-AXIS
# ============================================================

case_a = measurement


case_b = (

    measurement

    - 0.7

)


case_c = (

    measurement

    + 0.4

)


engineering_cases = {

    "Case A":
        case_a,

    "Case B":
        case_b,

    "Case C":
        case_c

}


line_styles = {

    "Case A":
        "-",

    "Case B":
        "--",

    "Case C":
        "-."

}


fig, (
    ax_top,
    ax_bottom
) = plt.subplots(

    2,

    1,

    sharex=True,

    figsize=(8, 5.8)

)


fig.subplots_adjust(
    hspace=0.05
)


for case_name, values in engineering_cases.items():

    style = line_styles[
        case_name
    ]


    ax_top.plot(

        sample_number,

        values,

        linestyle=style,

        marker="o",

        label=case_name

    )


    ax_bottom.plot(

        sample_number,

        values,

        linestyle=style,

        marker="o",

        label=case_name

    )


ax_top.set_ylim(
    74,
    95
)


ax_bottom.set_ylim(
    6,
    14
)


ax_top.spines[
    "bottom"
].set_visible(
    False
)


ax_bottom.spines[
    "top"
].set_visible(
    False
)


ax_top.tick_params(

    axis="x",

    bottom=False,

    labelbottom=False

)


ax_top.legend(
    ncols=3
)


ax_bottom.set_xlabel(
    "Sample Number"
)


fig.supylabel(
    "Measured Value [-]"
)


plt.show()


# ============================================================
# 31. CONSISTENT CASE STYLE
# ============================================================

"""
If:

Case A = solid

Case B = dashed

Case C = dash-dot


then those styles should remain identical on both visible
axis regions.

Otherwise the figure can become difficult to interpret.
"""


# ============================================================
# 32. AUTOMATIC BREAK DETECTION CONCEPT
# ============================================================

"""
A broken axis should normally be chosen deliberately.

However, code can help identify a large gap in sorted data.

Example:

Values:

9.1
9.5
10.0
10.2
11.0
82.0
91.0


Large numerical gap:

11
to
82


could suggest a candidate axis break.
"""


sorted_measurements = np.sort(
    measurement
)


measurement_gaps = np.diff(
    sorted_measurements
)


largest_gap_index = np.argmax(
    measurement_gaps
)


largest_gap = measurement_gaps[
    largest_gap_index
]


lower_gap_value = sorted_measurements[
    largest_gap_index
]


upper_gap_value = sorted_measurements[
    largest_gap_index
    + 1
]


print(
    "\n--- Largest Numerical Gap ---"
)


print(
    f"Lower Edge = "
    f"{lower_gap_value:.3f}"
)


print(
    f"Upper Edge = "
    f"{upper_gap_value:.3f}"
)


print(
    f"Gap = "
    f"{largest_gap:.3f}"
)


# ============================================================
# 33. AUTOMATIC BREAK WARNING
# ============================================================

"""
A large numerical gap does NOT automatically mean:

Use a broken axis.


The decision should depend on:

- Engineering meaning
- Distribution
- Communication goal
- Presence of outliers
- Whether a log scale is valid
- Whether an inset would be clearer


Automation can suggest:

Possible break limits


but should not replace scientific judgment.
"""


# ============================================================
# 34. REUSABLE BREAK-MARK FUNCTION
# ============================================================

def add_y_break_marks(
    ax_top,
    ax_bottom,
    size=0.012,
    linewidth=1.0
):
    """
    Add diagonal marks between two vertically stacked axes.

    Parameters
    ----------
    ax_top : matplotlib.axes.Axes
        Upper axis.

    ax_bottom : matplotlib.axes.Axes
        Lower axis.

    size : float
        Diagonal mark size in axis coordinates.

    linewidth : float
        Break-mark line width.
    """

    style = dict(

        color="k",

        clip_on=False,

        linewidth=linewidth

    )


    for x_position in [
        0,
        1
    ]:

        ax_top.plot(

            (
                x_position
                - size,

                x_position
                + size
            ),

            (
                -size,
                +size
            ),

            transform=ax_top.transAxes,

            **style

        )


        ax_bottom.plot(

            (
                x_position
                - size,

                x_position
                + size
            ),

            (
                1 - size,
                1 + size
            ),

            transform=ax_bottom.transAxes,

            **style

        )


# ============================================================
# 35. REUSABLE BROKEN Y-AXIS FUNCTION
# ============================================================

def plot_broken_y_axis(
    x,
    datasets,
    lower_ylim,
    upper_ylim,
    x_label,
    y_label,
    title=None,
    line_styles=None,
    height_ratios=(
        1,
        2
    ),
    markers=True
):
    """
    Create a broken Y-axis line comparison.

    Parameters
    ----------
    x : array-like
        Shared X values.

    datasets : dict
        Mapping:
        display label -> Y array

    lower_ylim : tuple
        Lower visible Y range.

    upper_ylim : tuple
        Upper visible Y range.

    x_label : str
        X-axis label.

    y_label : str
        Shared Y-axis label.

    title : str, optional
        Figure title.

    line_styles : dict, optional
        Mapping:
        display label -> line style

    height_ratios : tuple
        Relative heights:
        upper axis, lower axis

    markers : bool
        Display markers.

    Returns
    -------
    fig, ax_top, ax_bottom
    """

    x = np.asarray(
        x,
        dtype=float
    )


    if not datasets:

        raise ValueError(
            "At least one dataset is required."
        )


    if (
        lower_ylim[
            0
        ]
        >= lower_ylim[
            1
        ]
    ):

        raise ValueError(
            "lower_ylim must be increasing."
        )


    if (
        upper_ylim[
            0
        ]
        >= upper_ylim[
            1
        ]
    ):

        raise ValueError(
            "upper_ylim must be increasing."
        )


    if lower_ylim[
        1
    ] >= upper_ylim[
        0
    ]:

        raise ValueError(
            "The lower and upper Y ranges "
            "should be separated."
        )


    if line_styles is None:

        styles = [
            "-",
            "--",
            "-.",
            ":"
        ]


        line_styles = {

            name:
                styles[
                    index
                    % len(
                        styles
                    )
                ]

            for index, name in enumerate(
                datasets
            )

        }


    fig, (
        ax_top,
        ax_bottom
    ) = plt.subplots(

        2,

        1,

        sharex=True,

        figsize=(8, 5.8),

        height_ratios=list(
            height_ratios
        )

    )


    fig.subplots_adjust(
        hspace=0.05
    )


    for name, values in datasets.items():

        values = np.asarray(
            values,
            dtype=float
        )


        if values.shape != x.shape:

            raise ValueError(
                f"Dataset '{name}' must have "
                "the same shape as X."
            )


        marker = (

            "o"

            if markers

            else None

        )


        style = line_styles.get(
            name,
            "-"
        )


        for ax in [
            ax_top,
            ax_bottom
        ]:

            ax.plot(

                x,

                values,

                linestyle=style,

                marker=marker,

                linewidth=1.3,

                label=name

            )


    ax_top.set_ylim(
        *upper_ylim
    )


    ax_bottom.set_ylim(
        *lower_ylim
    )


    # Hide touching spines

    ax_top.spines[
        "bottom"
    ].set_visible(
        False
    )


    ax_bottom.spines[
        "top"
    ].set_visible(
        False
    )


    ax_top.tick_params(

        axis="x",

        bottom=False,

        labelbottom=False

    )


    # Grid

    for ax in [
        ax_top,
        ax_bottom
    ]:

        ax.grid(

            True,

            alpha=0.35

        )


    # Break marks

    add_y_break_marks(

        ax_top,

        ax_bottom

    )


    ax_bottom.set_xlabel(
        x_label
    )


    fig.supylabel(
        y_label
    )


    if title is not None:

        fig.suptitle(
            title
        )


    if len(
        datasets
    ) > 1:

        ax_top.legend()


    return (
        fig,
        ax_top,
        ax_bottom
    )


# ============================================================
# 36. USE REUSABLE BROKEN Y FUNCTION
# ============================================================

fig, ax_top, ax_bottom = (
    plot_broken_y_axis(

        x=sample_number,

        datasets=engineering_cases,

        lower_ylim=(
            6,
            14
        ),

        upper_ylim=(
            74,
            95
        ),

        x_label="Sample Number",

        y_label="Measured Value [-]",

        title=(
            "Reusable Broken Y-Axis Example"
        ),

        line_styles=line_styles

    )
)


plt.show()


# ============================================================
# 37. REUSABLE BROKEN-X MARK FUNCTION
# ============================================================

def add_x_break_marks(
    ax_left,
    ax_right,
    size=0.015,
    linewidth=1.0
):
    """
    Add diagonal marks between two side-by-side axes.
    """

    style = dict(

        color="k",

        clip_on=False,

        linewidth=linewidth

    )


    for y_position in [
        0,
        1
    ]:

        ax_left.plot(

            (
                1 - size,
                1 + size
            ),

            (
                y_position
                - size,

                y_position
                + size
            ),

            transform=ax_left.transAxes,

            **style

        )


        ax_right.plot(

            (
                -size,
                +size
            ),

            (
                y_position
                - size,

                y_position
                + size
            ),

            transform=ax_right.transAxes,

            **style

        )


# ============================================================
# 38. REUSABLE BROKEN X-AXIS FUNCTION
# ============================================================

def plot_broken_x_axis(
    x,
    datasets,
    left_xlim,
    right_xlim,
    x_label,
    y_label,
    title=None,
    line_styles=None
):
    """
    Create a broken X-axis comparison.

    Parameters
    ----------
    x : array-like
        Shared X values.

    datasets : dict
        Mapping:
        label -> Y values

    left_xlim : tuple
        First visible X interval.

    right_xlim : tuple
        Second visible X interval.

    x_label : str
        Shared X-axis label.

    y_label : str
        Y-axis label.

    title : str, optional

    line_styles : dict, optional

    Returns
    -------
    fig, ax_left, ax_right
    """

    x = np.asarray(
        x,
        dtype=float
    )


    if left_xlim[
        1
    ] >= right_xlim[
        0
    ]:

        raise ValueError(
            "Left and right ranges should "
            "be separated."
        )


    if line_styles is None:

        styles = [
            "-",
            "--",
            "-.",
            ":"
        ]


        line_styles = {

            name:
                styles[
                    index
                    % len(
                        styles
                    )
                ]

            for index, name in enumerate(
                datasets
            )

        }


    fig, (
        ax_left,
        ax_right
    ) = plt.subplots(

        1,

        2,

        sharey=True,

        figsize=(9, 4.8)

    )


    fig.subplots_adjust(
        wspace=0.05
    )


    for name, values in datasets.items():

        values = np.asarray(
            values,
            dtype=float
        )


        if values.shape != x.shape:

            raise ValueError(
                f"Dataset '{name}' does not "
                "match X shape."
            )


        style = line_styles.get(
            name,
            "-"
        )


        for ax in [
            ax_left,
            ax_right
        ]:

            ax.plot(

                x,

                values,

                linestyle=style,

                linewidth=1.4,

                label=name

            )


    ax_left.set_xlim(
        *left_xlim
    )


    ax_right.set_xlim(
        *right_xlim
    )


    ax_left.spines[
        "right"
    ].set_visible(
        False
    )


    ax_right.spines[
        "left"
    ].set_visible(
        False
    )


    ax_right.tick_params(

        axis="y",

        left=False,

        labelleft=False

    )


    add_x_break_marks(

        ax_left,

        ax_right

    )


    for ax in [
        ax_left,
        ax_right
    ]:

        ax.grid(

            True,

            alpha=0.35

        )


    ax_left.set_ylabel(
        y_label
    )


    fig.supxlabel(
        x_label
    )


    if title is not None:

        fig.suptitle(
            title
        )


    if len(
        datasets
    ) > 1:

        ax_left.legend()


    return (
        fig,
        ax_left,
        ax_right
    )


# ============================================================
# 39. USE REUSABLE BROKEN X FUNCTION
# ============================================================

broken_x_cases = {

    "Voltage":
        signal_v

}


fig, ax_left, ax_right = (
    plot_broken_x_axis(

        x=time_long_ms,

        datasets=broken_x_cases,

        left_xlim=(
            0,
            2
        ),

        right_xlim=(
            8,
            10
        ),

        x_label="Time [ms]",

        y_label="Voltage [V]",

        title="Reusable Broken X-Axis"

    )
)


plt.show()


# ============================================================
# 40. LOGARITHMIC AXIS ALTERNATIVE
# ============================================================

"""
A log axis may be preferable when:

Values span several orders of magnitude

and:

All relevant values are positive.


Example:

1

10

100

1000


A logarithmic axis preserves the complete numerical range
instead of deleting an interval.
"""


positive_values = np.array(
    [
        1,
        3,
        10,
        30,
        100,
        300,
        1000
    ]
)


fig, axes = plt.subplots(

    1,

    2,

    figsize=(10, 4)

)


axes[0].plot(

    np.arange(
        len(
            positive_values
        )
    ),

    positive_values,

    marker="o"

)


axes[0].set_title(
    "Linear Y-axis"
)


axes[1].plot(

    np.arange(
        len(
            positive_values
        )
    ),

    positive_values,

    marker="o"

)


axes[1].set_yscale(
    "log"
)


axes[1].set_title(
    "Logarithmic Y-axis"
)


for ax in axes:

    ax.set_xlabel(
        "Sample"
    )


    ax.set_ylabel(
        "Value"
    )


    ax.grid(
        True,
        which="both"
    )


plt.tight_layout()

plt.show()


# ============================================================
# 41. BROKEN AXIS vs LOG AXIS
# ============================================================

"""
BROKEN AXIS

Removes an interval from the visual range.


Useful when:

Two separated ranges matter.


------------------------------------------------------------


LOG AXIS

Keeps the complete range but changes numerical spacing.


Useful when:

Values span several orders of magnitude.


------------------------------------------------------------


These solve different visualization problems.
"""


# ============================================================
# 42. BROKEN AXIS vs INSET
# ============================================================

"""
BROKEN AXIS

Two separated ranges are both emphasized.


------------------------------------------------------------


INSET

Main plot keeps the complete range.

A selected region is magnified.


For many cases:

Inset is less disruptive to the numerical axis.
"""


# ============================================================
# 43. BROKEN AXIS vs NORMALIZED DATA
# ============================================================

"""
Normalization may help compare relative shapes.

Example:

Value / Maximum


However:

Normalization removes direct physical magnitude.


Broken axes preserve physical units but omit a numerical
interval.


Choose based on the research question.
"""


# ============================================================
# 44. BROKEN AXIS vs SEPARATE SUBPLOTS
# ============================================================

"""
Separate subplots may be clearer when:

The two numerical regions correspond to physically
different operating conditions.


Example:

Normal operation

vs

Fault condition


A broken axis is most natural when the reader should still
understand the data as one numerical quantity with a
discontinuous displayed range.
"""


# ============================================================
# 45. PUBLICATION SIZE
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


publication_width_in = mm_to_inches(
    publication_width_mm
)


publication_height_in = (

    publication_width_in

    * 0.72

)


# ============================================================
# 46. PUBLICATION STYLE
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
        1.3,

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
# 47. FINAL PUBLICATION BROKEN-Y FIGURE
# ============================================================

with mpl.rc_context(
    publication_style
):

    fig, (
        ax_top,
        ax_bottom
    ) = plt.subplots(

        2,

        1,

        sharex=True,

        figsize=(
            publication_width_in,
            publication_height_in
        ),

        height_ratios=[
            1,
            2
        ]

    )


    fig.subplots_adjust(
        hspace=0.05
    )


    # --------------------------------------------------------
    # Plot data
    # --------------------------------------------------------

    for (
        case_name,
        values
    ) in engineering_cases.items():

        style = line_styles[
            case_name
        ]


        for ax in [
            ax_top,
            ax_bottom
        ]:

            ax.plot(

                sample_number,

                values,

                linestyle=style,

                marker="o",

                markersize=3,

                label=case_name

            )


    # --------------------------------------------------------
    # Ranges
    # --------------------------------------------------------

    ax_top.set_ylim(
        74,
        95
    )


    ax_bottom.set_ylim(
        6,
        14
    )


    # --------------------------------------------------------
    # Broken-axis formatting
    # --------------------------------------------------------

    ax_top.spines[
        "bottom"
    ].set_visible(
        False
    )


    ax_bottom.spines[
        "top"
    ].set_visible(
        False
    )


    ax_top.tick_params(

        axis="x",

        bottom=False,

        labelbottom=False

    )


    add_y_break_marks(

        ax_top,

        ax_bottom,

        size=0.012,

        linewidth=0.9

    )


    # --------------------------------------------------------
    # Grid
    # --------------------------------------------------------

    for ax in [
        ax_top,
        ax_bottom
    ]:

        ax.grid(

            True,

            alpha=0.30,

            linewidth=0.5

        )


    # --------------------------------------------------------
    # Labels
    # --------------------------------------------------------

    ax_bottom.set_xlabel(
        "Sample Number"
    )


    fig.supylabel(
        "Measured Value [-]"
    )


    ax_top.legend(
        ncols=3
    )


    # --------------------------------------------------------
    # Save
    # --------------------------------------------------------

    publication_png = (
        output_figure_folder
        / "publication_broken_axis.png"
    )


    publication_pdf = (
        output_figure_folder
        / "publication_broken_axis.pdf"
    )


    publication_svg = (
        output_figure_folder
        / "publication_broken_axis.svg"
    )


    fig.savefig(

        publication_png,

        dpi=300,

        bbox_inches="tight"

    )


    fig.savefig(

        publication_pdf,

        bbox_inches="tight"

    )


    fig.savefig(

        publication_svg,

        bbox_inches="tight"

    )


    print(
        "\n--- Publication Files Saved ---"
    )


    print(
        publication_png
    )


    print(
        publication_pdf
    )


    print(
        publication_svg
    )


    plt.show()


# ============================================================
# 48. SAVE EXAMPLE DATA
# ============================================================

broken_axis_data = pd.DataFrame(
    {
        "Sample_Number":
            sample_number,

        "Case_A":
            case_a,

        "Case_B":
            case_b,

        "Case_C":
            case_c
    }
)


broken_axis_csv = (
    output_data_folder
    / "broken_axis_example_data.csv"
)


broken_axis_data.to_csv(

    broken_axis_csv,

    index=False

)


print(
    "\nExample Data Saved:"
)


print(
    broken_axis_csv
)


# ============================================================
# 49. SCIENTIFIC INTEGRITY
# ============================================================

"""
A broken axis changes the geometry of the visual
representation.

Therefore:

The break must be obvious.

Axis values must remain visible.

The omitted range must not be hidden silently.

The caption should mention the broken axis when useful.


Readers should immediately understand that the numerical
axis is discontinuous.
"""


# ============================================================
# 50. COMMON MISTAKE - NO BREAK SYMBOL
# ============================================================

"""
If a numerical range is omitted but no break mark is shown:

The reader may assume the axis is continuous.


Always make the discontinuity visually clear.
"""


# ============================================================
# 51. COMMON MISTAKE - HIDDEN TICK VALUES
# ============================================================

"""
A broken axis should still provide numerical ticks.

Do not remove so many ticks that the reader cannot
understand the two visible ranges.
"""


# ============================================================
# 52. COMMON MISTAKE - EXAGGERATING SMALL DIFFERENCES
# ============================================================

"""
Suppose:

Design A = 95.0%

Design B = 95.1%


A broken axis beginning at:

94.9%


can make the difference look very large.


The numerical values remain:

0.1 percentage point apart.


Visual emphasis must not replace numerical interpretation.
"""


# ============================================================
# 53. COMMON MISTAKE - BREAKING BAR AXIS CARELESSLY
# ============================================================

"""
Bar-chart height normally communicates distance from a
baseline.

Breaking the axis can alter that visual interpretation.

Use extra caution with:

Bar charts

Column charts

Area charts
"""


# ============================================================
# 54. COMMON MISTAKE - TOO MANY BREAKS
# ============================================================

"""
An axis with:

Three

Four

or

Five


discontinuous regions becomes difficult to interpret.

Use:

Separate panels

or

Another visualization method.
"""


# ============================================================
# 55. COMMON MISTAKE - BOTH X AND Y BROKEN
# ============================================================

"""
Breaking:

X

and

Y


simultaneously can make a figure extremely difficult to
read.

Avoid this unless the scientific need is unusually strong.
"""


# ============================================================
# 56. COMMON MISTAKE - BREAK NOT EXPLAINED
# ============================================================

"""
A figure caption may state:

"The Y-axis is broken between 15 and 70 A to improve
visibility of the nominal and fault-current regions."


This removes ambiguity.
"""


# ============================================================
# 57. COMMON MISTAKE - INCONSISTENT BREAK MARKS
# ============================================================

"""
Both sides of the axis should generally communicate the
break consistently.

Do not place a break symbol on only one side when that
makes the visual structure ambiguous.
"""


# ============================================================
# 58. COMMON MISTAKE - DIFFERENT DATA ON TWO AXES
# ============================================================

"""
For a standard broken Y-axis:

Upper axis

and

Lower axis


normally show the SAME dataset.

Only the visible limits differ.


If different datasets are plotted:

It is no longer simply one broken-axis representation.
"""


# ============================================================
# 59. COMMON MISTAKE - OVERLAPPING RANGES
# ============================================================

"""
Example:

Lower axis:

0 to 20


Upper axis:

15 to 50


These ranges overlap.

A standard broken axis should normally use distinct,
non-overlapping ranges.
"""


# ============================================================
# 60. COMMON MISTAKE - WRONG ORDER
# ============================================================

"""
Upper Y region should contain:

Higher numerical values.


Lower Y region should contain:

Lower numerical values.


Reversing this without clear reason can confuse readers.
"""


# ============================================================
# 61. COMMON MISTAKE - BREAKING AN ALREADY LOG AXIS
# ============================================================

"""
Before combining:

Logarithmic scaling

and

Axis breaks


ask whether the resulting representation remains easy to
understand.

Often a single logarithmic axis already solves the dynamic
range problem.
"""


# ============================================================
# 62. COMMON MISTAKE - BROKEN FREQUENCY AXIS HIDES RESONANCE
# ============================================================

"""
If the omitted frequency range contains important:

Resonances

Harmonics

EMI peaks

or

Transitions


a broken axis may hide scientifically relevant behavior.

Use the full spectrum when broadband behavior matters.
"""


# ============================================================
# 63. COMMON MISTAKE - CALLING OMITTED REGION ZERO
# ============================================================

"""
A broken range does NOT mean:

The missing region contains zero values.


It means:

That part of the axis is not displayed.
"""


# ============================================================
# 64. COMMON MISTAKE - NO ORIGINAL FULL PLOT CHECK
# ============================================================

"""
Always inspect the complete unbroken data first.

This helps prevent:

Accidental hiding of important observations.
"""


# ============================================================
# 65. DECISION WORKFLOW
# ============================================================

"""
Extreme Values Present?
        ↓
Plot Full Data First
        ↓
Is Detail Still Readable?
        ↓
YES
        ↓
Keep Normal Axis


NO
        ↓
Can Log Scale Solve It?
        ↓
YES
        ↓
Consider Log Scale


NO
        ↓
Would Inset Preserve Context Better?
        ↓
YES
        ↓
Use Inset


NO
        ↓
Would Separate Panels Be Clearer?
        ↓
YES
        ↓
Use Subplots


NO
        ↓
Consider Broken Axis
        ↓
Clearly Mark Discontinuity
        ↓
Show Numerical Ticks
        ↓
Explain in Caption
"""


# ============================================================
# 66. BROKEN-Y WORKFLOW
# ============================================================

"""
Full Dataset
      ↓
Identify Lower Range
      ↓
Identify Upper Range
      ↓
Create Two Axes
      ↓
sharex=True
      ↓
Plot SAME Data
      ↓
Set Different Y Limits
      ↓
Hide Touching Spines
      ↓
Add Diagonal Break Marks
      ↓
Check Numerical Integrity
"""


# ============================================================
# 67. BROKEN-X WORKFLOW
# ============================================================

"""
Full X Range
      ↓
Identify Region 1
      ↓
Identify Region 2
      ↓
Create Side-by-Side Axes
      ↓
sharey=True
      ↓
Plot SAME Data
      ↓
Set Different X Limits
      ↓
Hide Touching Spines
      ↓
Add Break Marks
      ↓
Clearly Show Omitted Interval
"""


# ============================================================
# 68. BAR-PLOT DECISION WORKFLOW
# ============================================================

"""
One Extreme Bar?
      ↓
Can Full Axis Still Communicate Others?
      ↓
NO
      ↓
Consider:
Log Plot
Dot Plot
Separate Panel
Inset
      ↓
Only If Necessary:
Broken Bar Axis
      ↓
Explicit Break Marks
      ↓
Numerical Labels
"""


# ============================================================
# 69. PUBLICATION CHECKLIST
# ============================================================

"""
Before publishing a broken-axis figure, check:


NECESSITY
------------------------------------------------------------

Is the broken axis genuinely needed?

Would an inset be clearer?

Would a log scale be better?


FULL DATA
------------------------------------------------------------

Was the complete dataset inspected?


BREAK
------------------------------------------------------------

Is the discontinuity immediately visible?

Are diagonal break marks present?


AXIS VALUES
------------------------------------------------------------

Are numerical ranges clearly shown?


OMITTED RANGE
------------------------------------------------------------

Can the reader determine which interval is missing?


DATA
------------------------------------------------------------

Are the same datasets plotted on both axis sections?


STYLES
------------------------------------------------------------

Are cases represented consistently?


BAR PLOTS
------------------------------------------------------------

Could the break exaggerate visual differences?


FREQUENCY DATA
------------------------------------------------------------

Does the omitted region contain important spectral
information?


CAPTION
------------------------------------------------------------

Should the broken interval be stated explicitly?


OUTPUT
------------------------------------------------------------

Does the break remain visible in:

PNG?

PDF?

SVG?


FINAL TEST
------------------------------------------------------------

Could a reader mistakenly believe the axis is continuous?

If yes:

Improve the figure.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
BROKEN AXIS AND DISCONTINUOUS RANGES


1. BASIC BROKEN Y-AXIS

fig, (
    ax_top,
    ax_bottom
) = plt.subplots(

    2,

    1,

    sharex=True

)


------------------------------------------------------------


2. PLOT SAME DATA

ax_top.plot(
    x,
    y
)


ax_bottom.plot(
    x,
    y
)


------------------------------------------------------------


3. SET DIFFERENT Y LIMITS

ax_top.set_ylim(
    high_min,
    high_max
)


ax_bottom.set_ylim(
    low_min,
    low_max
)


------------------------------------------------------------


4. HIDE TOUCHING SPINES

ax_top.spines[
    "bottom"
].set_visible(
    False
)


ax_bottom.spines[
    "top"
].set_visible(
    False
)


------------------------------------------------------------


5. HIDE DUPLICATE X TICKS

ax_top.tick_params(

    axis="x",

    bottom=False,

    labelbottom=False

)


------------------------------------------------------------


6. ADD BREAK MARKS

Use short diagonal lines at the discontinuity.


------------------------------------------------------------


7. BROKEN X-AXIS

fig, (
    ax_left,
    ax_right
) = plt.subplots(

    1,

    2,

    sharey=True

)


------------------------------------------------------------


8. BROKEN X LIMITS

ax_left.set_xlim(
    x1_min,
    x1_max
)


ax_right.set_xlim(
    x2_min,
    x2_max
)


------------------------------------------------------------


9. BROKEN X SPINES

ax_left.spines[
    "right"
].set_visible(
    False
)


ax_right.spines[
    "left"
].set_visible(
    False
)


------------------------------------------------------------


10. HEIGHT RATIOS

Useful when:

Lower region contains most detail

and:

Upper region contains only extremes.


------------------------------------------------------------


11. WIDTH RATIOS

Useful when two X ranges require different visual space.


------------------------------------------------------------


12. BROKEN AXIS DOES NOT REMOVE DATA

Normally:

The same dataset is plotted on both axes.


Only:

Visible limits

change.


------------------------------------------------------------


13. BROKEN AXIS != FILTERING

Filtering changes the dataset.

Broken axes change the displayed ranges.


------------------------------------------------------------


14. LOGARITHMIC ALTERNATIVE

Consider:

ax.set_yscale(
    "log"
)


when values span several orders of magnitude.


------------------------------------------------------------


15. INSET ALTERNATIVE

Use an inset when:

Full context should remain visible

and:

One region needs magnification.


------------------------------------------------------------


16. SUBPLOT ALTERNATIVE

Use separate subplots when:

The regions represent distinct analyses or operating
conditions.


------------------------------------------------------------


17. BAR PLOTS

Use broken bar axes cautiously.

Bar height strongly communicates magnitude.


------------------------------------------------------------


18. FREQUENCY DATA

A broken frequency axis may hide broadband behavior.

Use only when separated bands are specifically relevant.


------------------------------------------------------------


19. AUTOMATIC GAP DETECTION

sorted_values = np.sort(
    values
)


gaps = np.diff(
    sorted_values
)


largest_gap = np.argmax(
    gaps
)


This may suggest a candidate break,

but does NOT decide whether a break is scientifically
appropriate.


------------------------------------------------------------


20. PUBLICATION REQUIREMENT

The omitted region must be visually obvious.


------------------------------------------------------------


21. ENGINEERING APPLICATIONS

Possible uses include:

Fault current + normal current

Large transient + small ripple

Extreme temperature events

Outlier measurements

Separated operating ranges

Selected frequency bands

Large category differences


------------------------------------------------------------


22. MOST IMPORTANT PRINCIPLE

A broken axis deliberately changes how numerical distance
is displayed.


Therefore the reader must immediately understand:

Where the break occurs

What range is omitted

and

What the actual numerical values are.


------------------------------------------------------------


23. COMPLETE WORKFLOW

Full Engineering Data
        ↓
Plot Normally
        ↓
Identify Dynamic-Range Problem
        ↓
Consider Log Scale
        ↓
Consider Inset
        ↓
Consider Separate Panels
        ↓
If Broken Axis Is Best:
        ↓
Create Shared Axes
        ↓
Plot Same Data
        ↓
Set Discontinuous Limits
        ↓
Hide Touching Spines
        ↓
Add Break Marks
        ↓
Keep Units / Ticks Visible
        ↓
Check for Misleading Emphasis
        ↓
Export
        ↓
Explain if Necessary


------------------------------------------------------------


NEXT:

30_automatic_batch_plotting.py


The next file will move from specialized visualization
into RESEARCH AUTOMATION:

Multiple CSV files

Multiple Excel files

Multiple sheets

Automatic column detection

Automatic plotting loops

File-name generation

Output folders

Batch PNG / PDF / SVG export

Skipping invalid files

Logging processed / failed files

Automatically closing figures

Summary tables

Automatic case comparison

Batch FFT plotting

Batch engineering reports

and scalable workflows for dozens or hundreds of research
datasets.
"""
