"""
============================================================
Python for Engineering and Research
26 - Inset and Zoomed Plots
============================================================

Purpose:
    Demonstrate how inset axes and zoomed regions can be
    used to highlight important details while preserving
    the full engineering waveform, spectrum, or comparison.

Topics:
    1. What is an inset plot?
    2. Why use zoomed regions?
    3. Axes.inset_axes()
    4. Selecting zoom limits
    5. indicate_inset_zoom()
    6. Inset position and size
    7. Switching-transient zoom
    8. Ripple zoom
    9. Multiple engineering cases
    10. Automatic zoom Y-limits
    11. inset_axes() from axes_grid1
    12. Percentage-based inset sizing
    13. zoomed_inset_axes()
    14. mark_inset()
    15. FFT / frequency-domain inset
    16. Logarithmic inset axis
    17. Automatic peak-centered inset
    18. Automatic difference-centered inset
    19. Multiple inset regions
    20. Inset vs subplot
    21. Annotations
    22. Engineering threshold inside inset
    23. Reusable zoom functions
    24. Publication-oriented figure
    25. PNG / PDF / SVG export
    26. Common mistakes
    27. Key takeaways

Sample File:
    sample_data/fft_example.csv

Important:
    A zoomed inset should provide additional detail without
    hiding the overall physical context.

    Magnification should not be used to exaggerate small
    differences.

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

from mpl_toolkits.axes_grid1.inset_locator import (
    inset_axes,
    zoomed_inset_axes,
    mark_inset
)


# ============================================================
# 2. WHAT IS AN INSET PLOT?
# ============================================================

"""
An inset plot is a smaller axis placed inside or close to
the main plot.

Example:

Full Waveform
-------------------------------------------------
|                                               |
|           Main signal                         |
|                                               |
|                  ┌─────────────────┐          |
|                  │   Zoom Region   │          |
|                  │     Detail      │          |
|                  └─────────────────┘          |
|                                               |
-------------------------------------------------


The main plot provides:

CONTEXT


The inset provides:

DETAIL
"""


# ============================================================
# 3. ENGINEERING APPLICATIONS
# ============================================================

"""
Inset plots are commonly useful for:

- Switching transitions
- Turn-on / turn-off behavior
- Voltage overshoot
- Current overshoot
- Ringing
- Steady-state ripple
- Small efficiency differences
- Experimental vs simulation comparison
- FFT resonance regions
- Harmonic peaks
- Narrow frequency bands
- EMI spectrum differences
- Control settling behavior
- Measurement noise
- Small-error regions
"""


# ============================================================
# 4. WHEN AN INSET IS USEFUL
# ============================================================

"""
Suppose the full waveform covers:

0 to 5 ms


but the important switching transition lasts:

2 microseconds.


If only the full waveform is plotted:

The transition may appear as one almost vertical line.


If only the zoomed region is plotted:

The reader loses the overall waveform context.


A useful solution is:

Full waveform
      +
Zoomed inset
"""


# ============================================================
# 5. PROJECT PATHS
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
    / "inset_zoom"
)


output_figure_folder.mkdir(
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
# 6. CREATE SYNTHETIC TIME-DOMAIN DATA
# ============================================================

"""
Create an educational engineering waveform.

The example contains:

- DC level
- Startup transient
- Small ripple
- Local ringing event

This is synthetic teaching data and is not intended to
represent one specific converter.
"""


time_s = np.linspace(
    0,
    0.005,
    5000
)


startup_response = (

    48

    * (
        1
        - np.exp(
            -time_s
            / 0.00045
        )
    )

)


ripple = (

    0.45

    * np.sin(
        2
        * np.pi
        * 100_000
        * time_s
    )

)


ringing_center_s = 0.002


ringing = (

    2.5

    * np.exp(
        -np.abs(
            time_s
            - ringing_center_s
        )
        / 0.000025
    )

    * np.sin(
        2
        * np.pi
        * 350_000
        * (
            time_s
            - ringing_center_s
        )
    )

)


voltage_v = (

    startup_response

    + ripple

    + ringing

)


# ============================================================
# 7. USE MILLISECONDS FOR DISPLAY
# ============================================================

"""
It is often useful to convert the plotted X-axis into a
convenient engineering unit.

Here:

seconds
    ↓
milliseconds


Important:

Use the same physical units in both the main axis and the
inset unless there is a strong reason to do otherwise.
"""


time_ms = (

    time_s

    * 1000

)


# ============================================================
# 8. BASIC FULL WAVEFORM
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    voltage_v,
    linewidth=1.5
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Converter Output Voltage"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 9. BASIC NATIVE INSET
# ============================================================

"""
A native inset can be created using:

ax.inset_axes(
    [x0, y0, width, height]
)


By default these values are relative to the parent axis.

Example:

[0.55, 0.15, 0.40, 0.35]


approximately means:

Start around 55% across the parent axis

Start around 15% from the bottom

Use 40% of the parent width

Use 35% of the parent height
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    voltage_v,
    linewidth=1.5
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True
)


# ------------------------------------------------------------
# Create inset
# ------------------------------------------------------------

axins = ax.inset_axes(
    [
        0.55,
        0.15,
        0.40,
        0.35
    ]
)


axins.plot(
    time_ms,
    voltage_v
)


plt.tight_layout()

plt.show()


# ============================================================
# 10. SELECT THE ZOOM REGION
# ============================================================

"""
An inset becomes useful when its axis limits are restricted.

Example:

Zoom around:

1.95 ms
to
2.05 ms
"""


zoom_x_min = 1.95

zoom_x_max = 2.05


# ============================================================
# 11. ZOOMED INSET USING X LIMITS
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    voltage_v,
    linewidth=1.5
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True
)


axins = ax.inset_axes(
    [
        0.55,
        0.15,
        0.40,
        0.35
    ]
)


axins.plot(
    time_ms,
    voltage_v,
    linewidth=1
)


axins.set_xlim(
    zoom_x_min,
    zoom_x_max
)


axins.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 12. CALCULATE AUTOMATIC Y-LIMITS
# ============================================================

"""
A useful zoom should also restrict the Y-axis.

Rather than guessing the Y limits, calculate them from the
selected X-region.
"""


zoom_mask = (

    (
        time_ms
        >= zoom_x_min
    )

    &

    (
        time_ms
        <= zoom_x_max
    )

)


zoom_voltage = voltage_v[
    zoom_mask
]


zoom_y_min = zoom_voltage.min()

zoom_y_max = zoom_voltage.max()


zoom_y_range = (

    zoom_y_max

    - zoom_y_min

)


zoom_padding = (

    0.10

    * zoom_y_range

)


if zoom_y_range == 0:

    zoom_padding = 1.0


zoom_y_lower = (

    zoom_y_min

    - zoom_padding

)


zoom_y_upper = (

    zoom_y_max

    + zoom_padding

)


print(
    "\n--- Automatic Zoom Limits ---"
)


print(
    "X:",
    zoom_x_min,
    "to",
    zoom_x_max,
    "ms"
)


print(
    "Y:",
    zoom_y_lower,
    "to",
    zoom_y_upper,
    "V"
)


# ============================================================
# 13. COMPLETE ZOOMED INSET
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    voltage_v,
    linewidth=1.5
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Converter Output with Switching-Region Zoom"
)


ax.grid(
    True
)


axins = ax.inset_axes(
    [
        0.53,
        0.14,
        0.42,
        0.38
    ]
)


axins.plot(
    time_ms,
    voltage_v,
    linewidth=1
)


axins.set_xlim(
    zoom_x_min,
    zoom_x_max
)


axins.set_ylim(
    zoom_y_lower,
    zoom_y_upper
)


axins.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 14. MARK THE INSET REGION
# ============================================================

"""
The reader should understand which part of the full signal
is represented by the inset.

Matplotlib can draw:

- A rectangle around the zoomed region
- Connector lines to the inset
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    voltage_v,
    linewidth=1.5
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True
)


axins = ax.inset_axes(
    [
        0.52,
        0.12,
        0.43,
        0.40
    ]
)


axins.plot(
    time_ms,
    voltage_v,
    linewidth=1
)


axins.set_xlim(
    zoom_x_min,
    zoom_x_max
)


axins.set_ylim(
    zoom_y_lower,
    zoom_y_upper
)


axins.grid(
    True
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 15. INSET TICK LABEL SIZE
# ============================================================

"""
Inset axes are smaller.

Therefore their tick labels may also need to be reduced
slightly.

Do not make them so small that they become unreadable.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    voltage_v,
    linewidth=1.5
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True
)


axins = ax.inset_axes(
    [
        0.52,
        0.14,
        0.43,
        0.38
    ]
)


axins.plot(
    time_ms,
    voltage_v,
    linewidth=1
)


axins.set_xlim(
    zoom_x_min,
    zoom_x_max
)


axins.set_ylim(
    zoom_y_lower,
    zoom_y_upper
)


axins.tick_params(
    labelsize=7
)


axins.grid(
    True
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 16. ADD INSET AXIS LABELS
# ============================================================

"""
Whether an inset requires its own axis labels depends on
the figure.

If the units are identical to the main axis and obvious,
full labels may be unnecessary.

If there is any ambiguity:

Label the inset.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    voltage_v,
    linewidth=1.5
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True
)


axins = ax.inset_axes(
    [
        0.52,
        0.14,
        0.43,
        0.38
    ]
)


axins.plot(
    time_ms,
    voltage_v,
    linewidth=1
)


axins.set_xlim(
    zoom_x_min,
    zoom_x_max
)


axins.set_ylim(
    zoom_y_lower,
    zoom_y_upper
)


axins.set_xlabel(
    "Time [ms]",
    fontsize=7
)


axins.set_ylabel(
    "Voltage [V]",
    fontsize=7
)


axins.tick_params(
    labelsize=7
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 17. SWITCHING-TRANSIENT EXAMPLE
# ============================================================

"""
Create a simplified switching waveform with:

- Fast transition
- Overshoot
- Damped ringing
"""


switch_time_ns = np.linspace(
    -200,
    1200,
    3000
)


switch_time_s = (

    switch_time_ns

    * 1e-9

)


transition = (

    400

    / (
        1
        + np.exp(
            -switch_time_ns
            / 15
        )
    )

)


overshoot_ringing = np.where(

    switch_time_ns >= 0,

    45

    * np.exp(
        -switch_time_ns
        / 180
    )

    * np.sin(
        2
        * np.pi
        * 18e6
        * switch_time_s
    ),

    0

)


drain_voltage = (

    transition

    + overshoot_ringing

)


# ============================================================
# 18. FULL SWITCHING WAVEFORM + TRANSITION INSET
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    switch_time_ns,
    drain_voltage,
    linewidth=1.5
)


ax.set_xlabel(
    "Time [ns]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Switching Transition"
)


ax.grid(
    True
)


axins = ax.inset_axes(
    [
        0.48,
        0.15,
        0.46,
        0.40
    ]
)


axins.plot(
    switch_time_ns,
    drain_voltage,
    linewidth=1
)


axins.set_xlim(
    -40,
    220
)


transition_mask = (

    (
        switch_time_ns
        >= -40
    )

    &

    (
        switch_time_ns
        <= 220
    )

)


transition_values = drain_voltage[
    transition_mask
]


axins.set_ylim(

    transition_values.min()
    - 20,

    transition_values.max()
    + 20

)


axins.tick_params(
    labelsize=7
)


axins.grid(
    True
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 19. STEADY-STATE RIPPLE EXAMPLE
# ============================================================

"""
An inset is also useful when the full DC value is large but
the ripple is small.

Example:

400 V output

with:

approximately ±1 V ripple
"""


ripple_time_ms = np.linspace(
    0,
    20,
    4000
)


ripple_voltage_v = (

    400

    + 1.0
    * np.sin(
        2
        * np.pi
        * 2
        * ripple_time_ms
    )

    + 0.15
    * np.sin(
        2
        * np.pi
        * 20
        * ripple_time_ms
    )

)


# ============================================================
# 20. RIPPLE ZOOM
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    ripple_time_ms,
    ripple_voltage_v,
    linewidth=1.3
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Output Voltage [V]"
)

ax.set_title(
    "DC Output Voltage with Ripple"
)


ax.grid(
    True
)


axins = ax.inset_axes(
    [
        0.52,
        0.14,
        0.42,
        0.38
    ]
)


axins.plot(
    ripple_time_ms,
    ripple_voltage_v,
    linewidth=1
)


axins.set_xlim(
    12,
    14
)


ripple_zoom_mask = (

    (
        ripple_time_ms
        >= 12
    )

    &

    (
        ripple_time_ms
        <= 14
    )

)


ripple_zoom_values = ripple_voltage_v[
    ripple_zoom_mask
]


axins.set_ylim(

    ripple_zoom_values.min()
    - 0.15,

    ripple_zoom_values.max()
    + 0.15

)


axins.tick_params(
    labelsize=7
)


axins.grid(
    True
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 21. MULTIPLE ENGINEERING CASES
# ============================================================

"""
Insets are especially useful when two curves appear almost
identical in the full plot.

Example:

Simulation

vs

Experiment
"""


simulation_voltage = voltage_v


experimental_voltage = (

    voltage_v

    + 0.20
    * np.sin(
        2
        * np.pi
        * 850
        * time_s
    )

    + 0.08
)


# ============================================================
# 22. MULTIPLE CASES + INSET
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    simulation_voltage,
    linewidth=1.5,
    label="Simulation"
)


ax.plot(
    time_ms,
    experimental_voltage,
    linewidth=1.3,
    linestyle="--",
    label="Experiment"
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


axins = ax.inset_axes(
    [
        0.52,
        0.13,
        0.43,
        0.38
    ]
)


axins.plot(
    time_ms,
    simulation_voltage,
    linewidth=1,
    label="Simulation"
)


axins.plot(
    time_ms,
    experimental_voltage,
    linewidth=1,
    linestyle="--",
    label="Experiment"
)


axins.set_xlim(
    zoom_x_min,
    zoom_x_max
)


combined_zoom_values = np.concatenate(
    [
        simulation_voltage[
            zoom_mask
        ],

        experimental_voltage[
            zoom_mask
        ]
    ]
)


combined_minimum = combined_zoom_values.min()

combined_maximum = combined_zoom_values.max()


combined_range = (

    combined_maximum

    - combined_minimum

)


combined_padding = max(

    0.10
    * combined_range,

    0.1

)


axins.set_ylim(

    combined_minimum
    - combined_padding,

    combined_maximum
    + combined_padding

)


axins.tick_params(
    labelsize=7
)


axins.grid(
    True
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 23. IMPORTANT MULTIPLE-CASE RULE
# ============================================================

"""
If the inset compares:

Simulation

and

Experiment


the SAME two datasets should normally appear in both:

Main plot

and

Inset


unless the figure clearly explains otherwise.

Do not silently show a different dataset inside the inset.
"""


# ============================================================
# 24. AUTOMATIC Y-LIMIT FUNCTION
# ============================================================

def calculate_zoom_ylim(
    x,
    y_arrays,
    x_min,
    x_max,
    padding_fraction=0.10
):
    """
    Calculate Y-axis limits for a selected X region.

    Parameters
    ----------
    x : array-like
        Shared X values.

    y_arrays : array-like or list of array-like
        One or more Y datasets.

    x_min, x_max : float
        Zoomed X range.

    padding_fraction : float
        Fraction of the selected Y range added as padding.

    Returns
    -------
    y_lower, y_upper : float
        Recommended zoomed Y-axis limits.
    """

    x = np.asarray(
        x,
        dtype=float
    )


    if x_min >= x_max:

        raise ValueError(
            "x_min must be smaller than x_max."
        )


    mask = (

        (
            x
            >= x_min
        )

        &

        (
            x
            <= x_max
        )

    )


    if not np.any(
        mask
    ):

        raise ValueError(
            "Selected zoom range contains "
            "no X samples."
        )


    if isinstance(
        y_arrays,
        np.ndarray
    ) and y_arrays.ndim == 1:

        y_arrays = [
            y_arrays
        ]


    selected_values = []


    for values in y_arrays:

        values = np.asarray(
            values,
            dtype=float
        )


        if values.shape != x.shape:

            raise ValueError(
                "All Y arrays must have the "
                "same shape as X."
            )


        selected_values.append(
            values[
                mask
            ]
        )


    combined = np.concatenate(
        selected_values
    )


    combined = combined[
        np.isfinite(
            combined
        )
    ]


    if len(
        combined
    ) == 0:

        raise ValueError(
            "No valid Y values in zoom range."
        )


    minimum = np.min(
        combined
    )


    maximum = np.max(
        combined
    )


    data_range = (

        maximum

        - minimum

    )


    if data_range == 0:

        padding = max(
            abs(
                maximum
            )
            * 0.05,
            1.0
        )

    else:

        padding = (

            padding_fraction

            * data_range

        )


    return (

        minimum
        - padding,

        maximum
        + padding

    )


# ============================================================
# 25. USE AUTOMATIC Y-LIMIT FUNCTION
# ============================================================

auto_y_min, auto_y_max = calculate_zoom_ylim(

    x=time_ms,

    y_arrays=[
        simulation_voltage,
        experimental_voltage
    ],

    x_min=zoom_x_min,

    x_max=zoom_x_max,

    padding_fraction=0.12

)


print(
    "\n--- Reusable Zoom Y Limits ---"
)


print(
    auto_y_min,
    auto_y_max
)


# ============================================================
# 26. axes_grid1 inset_axes()
# ============================================================

"""
Another inset method is available through:

mpl_toolkits.axes_grid1.inset_locator


It allows inset width and height to be specified as:

Percentages

or

physical sizes.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    voltage_v
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True
)


axins = inset_axes(

    ax,

    width="40%",

    height="35%",

    loc="lower right"

)


axins.plot(
    time_ms,
    voltage_v
)


axins.set_xlim(
    zoom_x_min,
    zoom_x_max
)


axins.set_ylim(
    zoom_y_lower,
    zoom_y_upper
)


axins.tick_params(
    labelsize=7
)


plt.tight_layout()

plt.show()


# ============================================================
# 27. PERCENTAGE-BASED INSET SIZE
# ============================================================

"""
Example:

width="40%"

height="35%"


means the inset size is relative to the parent axis.

This can be convenient when figure dimensions may change.
"""


# ============================================================
# 28. zoomed_inset_axes()
# ============================================================

"""
zoomed_inset_axes() creates an anchored inset associated
with a zoom factor.

The actual data region is still selected using:

set_xlim()

set_ylim()
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    voltage_v,
    linewidth=1.5
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True
)


zoom_ax = zoomed_inset_axes(

    ax,

    zoom=3,

    loc="lower right"

)


zoom_ax.plot(
    time_ms,
    voltage_v,
    linewidth=1
)


zoom_ax.set_xlim(
    zoom_x_min,
    zoom_x_max
)


zoom_ax.set_ylim(
    zoom_y_lower,
    zoom_y_upper
)


zoom_ax.tick_params(
    labelsize=7
)


plt.tight_layout()

plt.show()


# ============================================================
# 29. mark_inset()
# ============================================================

"""
mark_inset() can draw:

Rectangle around the zoom region
        +
Connecting lines


when using inset axes from axes_grid1.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    voltage_v,
    linewidth=1.5
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True
)


zoom_ax = zoomed_inset_axes(

    ax,

    zoom=3,

    loc="lower right"

)


zoom_ax.plot(
    time_ms,
    voltage_v,
    linewidth=1
)


zoom_ax.set_xlim(
    zoom_x_min,
    zoom_x_max
)


zoom_ax.set_ylim(
    zoom_y_lower,
    zoom_y_upper
)


zoom_ax.tick_params(
    labelsize=7
)


mark_inset(

    ax,

    zoom_ax,

    loc1=2,

    loc2=4,

    fc="none",

    ec="0.5"

)


plt.tight_layout()

plt.show()


# ============================================================
# 30. NATIVE vs axes_grid1 APPROACH
# ============================================================

"""
Two useful workflows are:

NATIVE MATPLOTLIB

ax.inset_axes(...)

ax.indicate_inset_zoom(...)


------------------------------------------------------------


AXES_GRID1 TOOLKIT

inset_axes(...)

zoomed_inset_axes(...)

mark_inset(...)


Both can be useful.

Choose the approach that keeps the research code clear and
maintainable.
"""


# ============================================================
# 31. INSET LOCATION
# ============================================================

"""
Common inset locations include:

Upper right

Upper left

Lower right

Lower left


The best location depends on the data.


Do NOT place the inset over:

- Important peaks
- Experimental differences
- Annotations
- Legend
- Critical transitions
"""


# ============================================================
# 32. MOVE INSET TO UPPER LEFT
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    voltage_v
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True
)


axins = ax.inset_axes(
    [
        0.08,
        0.55,
        0.40,
        0.36
    ]
)


axins.plot(
    time_ms,
    voltage_v
)


axins.set_xlim(
    zoom_x_min,
    zoom_x_max
)


axins.set_ylim(
    zoom_y_lower,
    zoom_y_upper
)


axins.tick_params(
    labelsize=7
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 33. AUTOMATIC PEAK ZOOM
# ============================================================

"""
Sometimes the region of interest is centered on the
maximum measured value.

Example:

Voltage overshoot.
"""


peak_index = np.argmax(
    drain_voltage
)


peak_time_ns = switch_time_ns[
    peak_index
]


peak_voltage_v = drain_voltage[
    peak_index
]


print(
    "\n--- Switching Peak ---"
)


print(
    f"Peak Time = "
    f"{peak_time_ns:.2f} ns"
)


print(
    f"Peak Voltage = "
    f"{peak_voltage_v:.2f} V"
)


# ============================================================
# 34. CREATE PEAK-CENTERED WINDOW
# ============================================================

peak_window_ns = 180


peak_zoom_min = (

    peak_time_ns

    - peak_window_ns

)


peak_zoom_max = (

    peak_time_ns

    + peak_window_ns

)


peak_y_min, peak_y_max = calculate_zoom_ylim(

    x=switch_time_ns,

    y_arrays=drain_voltage,

    x_min=peak_zoom_min,

    x_max=peak_zoom_max,

    padding_fraction=0.10

)


# ============================================================
# 35. AUTOMATIC PEAK-CENTERED INSET
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    switch_time_ns,
    drain_voltage,
    linewidth=1.5
)


ax.scatter(
    peak_time_ns,
    peak_voltage_v,
    s=25,
    label="Peak"
)


ax.set_xlabel(
    "Time [ns]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.legend()


ax.grid(
    True
)


axins = ax.inset_axes(
    [
        0.48,
        0.13,
        0.46,
        0.42
    ]
)


axins.plot(
    switch_time_ns,
    drain_voltage,
    linewidth=1
)


axins.scatter(
    peak_time_ns,
    peak_voltage_v,
    s=16
)


axins.set_xlim(
    peak_zoom_min,
    peak_zoom_max
)


axins.set_ylim(
    peak_y_min,
    peak_y_max
)


axins.tick_params(
    labelsize=7
)


axins.grid(
    True
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 36. AUTOMATIC DIFFERENCE REGION
# ============================================================

"""
For two engineering cases, the most interesting zoom may
be where their absolute difference is largest.
"""


difference = np.abs(

    experimental_voltage

    - simulation_voltage

)


difference_index = np.argmax(
    difference
)


maximum_difference_time = time_ms[
    difference_index
]


maximum_difference_value = difference[
    difference_index
]


print(
    "\n--- Maximum Simulation / Experiment Difference ---"
)


print(
    f"Time = "
    f"{maximum_difference_time:.4f} ms"
)


print(
    f"Difference = "
    f"{maximum_difference_value:.4f} V"
)


# ============================================================
# 37. DIFFERENCE-CENTERED ZOOM RANGE
# ============================================================

difference_half_window_ms = 0.12


difference_zoom_min = max(

    time_ms.min(),

    maximum_difference_time
    - difference_half_window_ms

)


difference_zoom_max = min(

    time_ms.max(),

    maximum_difference_time
    + difference_half_window_ms

)


difference_y_min, difference_y_max = (
    calculate_zoom_ylim(

        x=time_ms,

        y_arrays=[
            simulation_voltage,
            experimental_voltage
        ],

        x_min=difference_zoom_min,

        x_max=difference_zoom_max,

        padding_fraction=0.12

    )
)


# ============================================================
# 38. DIFFERENCE-CENTERED INSET
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    simulation_voltage,
    label="Simulation"
)


ax.plot(
    time_ms,
    experimental_voltage,
    linestyle="--",
    label="Experiment"
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


axins = ax.inset_axes(
    [
        0.52,
        0.14,
        0.43,
        0.38
    ]
)


axins.plot(
    time_ms,
    simulation_voltage
)


axins.plot(
    time_ms,
    experimental_voltage,
    linestyle="--"
)


axins.set_xlim(
    difference_zoom_min,
    difference_zoom_max
)


axins.set_ylim(
    difference_y_min,
    difference_y_max
)


axins.tick_params(
    labelsize=7
)


axins.grid(
    True
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 39. IMPORTANT AUTOMATIC-ZOOM WARNING
# ============================================================

"""
Automatically zooming to:

Largest difference

or

Largest peak


can be useful for analysis.


However:

The selected region should still be scientifically
meaningful.


Do not automatically present the most visually dramatic
region while ignoring equally important behavior elsewhere.
"""


# ============================================================
# 40. LOAD FFT SAMPLE DATA
# ============================================================

fft_file = (
    sample_data_folder
    / "fft_example.csv"
)


if not fft_file.exists():

    raise FileNotFoundError(
        f"\nFFT sample file not found:\n"
        f"{fft_file}"
    )


fft_data = pd.read_csv(
    fft_file
)


required_fft_columns = [

    "Frequency_Hz",

    "Unshielded_dBuV",

    "Case_A_dBuV",

    "Case_B_dBuV",

    "Case_C_dBuV"

]


missing_fft_columns = [

    column

    for column in required_fft_columns

    if column not in fft_data.columns

]


if missing_fft_columns:

    raise KeyError(
        f"Missing FFT columns: "
        f"{missing_fft_columns}"
    )


# ============================================================
# 41. CLEAN FFT DATA
# ============================================================

for column in required_fft_columns:

    fft_data[
        column
    ] = pd.to_numeric(

        fft_data[
            column
        ],

        errors="coerce"

    )


fft_data = fft_data.dropna(
    subset=required_fft_columns
)


fft_data = fft_data[
    fft_data[
        "Frequency_Hz"
    ] > 0
]


fft_data = fft_data.sort_values(
    "Frequency_Hz"
)


frequency_hz = fft_data[
    "Frequency_Hz"
].to_numpy()


unshielded_dbuV = fft_data[
    "Unshielded_dBuV"
].to_numpy()


case_b_dbuV = fft_data[
    "Case_B_dBuV"
].to_numpy()


# ============================================================
# 42. FULL FFT COMPARISON
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    frequency_hz,
    unshielded_dbuV,
    label="Unshielded"
)


ax.plot(
    frequency_hz,
    case_b_dbuV,
    linestyle="--",
    label="Case B"
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

plt.show()


# ============================================================
# 43. FIND FFT PEAK
# ============================================================

fft_peak_index = np.argmax(
    unshielded_dbuV
)


fft_peak_frequency = frequency_hz[
    fft_peak_index
]


fft_peak_magnitude = unshielded_dbuV[
    fft_peak_index
]


print(
    "\n--- FFT Peak ---"
)


print(
    f"Frequency = "
    f"{fft_peak_frequency:.3e} Hz"
)


print(
    f"Magnitude = "
    f"{fft_peak_magnitude:.2f} dBµV"
)


# ============================================================
# 44. MULTIPLICATIVE WINDOW FOR LOG FREQUENCY
# ============================================================

"""
On a logarithmic frequency axis, a multiplicative window is
often more natural than:

Peak ± fixed Hz.


Example:

Peak / 2
to
Peak × 2
"""


fft_zoom_min = max(

    frequency_hz.min(),

    fft_peak_frequency
    / 2

)


fft_zoom_max = min(

    frequency_hz.max(),

    fft_peak_frequency
    * 2

)


# ============================================================
# 45. FFT ZOOM Y-LIMITS
# ============================================================

fft_y_min, fft_y_max = calculate_zoom_ylim(

    x=frequency_hz,

    y_arrays=[
        unshielded_dbuV,
        case_b_dbuV
    ],

    x_min=fft_zoom_min,

    x_max=fft_zoom_max,

    padding_fraction=0.12

)


# ============================================================
# 46. FFT WITH LOGARITHMIC INSET
# ============================================================

fig, ax = plt.subplots(
    figsize=(8.5, 5)
)


ax.plot(
    frequency_hz,
    unshielded_dbuV,
    linewidth=1.5,
    label="Unshielded"
)


ax.plot(
    frequency_hz,
    case_b_dbuV,
    linewidth=1.5,
    linestyle="--",
    label="Case B"
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


axins = ax.inset_axes(
    [
        0.50,
        0.14,
        0.44,
        0.40
    ]
)


axins.plot(
    frequency_hz,
    unshielded_dbuV,
    linewidth=1
)


axins.plot(
    frequency_hz,
    case_b_dbuV,
    linewidth=1,
    linestyle="--"
)


axins.set_xscale(
    "log"
)


axins.set_xlim(
    fft_zoom_min,
    fft_zoom_max
)


axins.set_ylim(
    fft_y_min,
    fft_y_max
)


axins.tick_params(
    labelsize=7
)


axins.grid(
    True,
    which="both"
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 47. LOG MAIN AXIS + LOG INSET
# ============================================================

"""
When the main figure uses:

Logarithmic frequency


the inset should normally preserve that scale unless the
research question specifically requires a different
representation.


Do not silently switch between:

Log frequency

and

Linear frequency


because visual spacing changes.
"""


# ============================================================
# 48. FFT REDUCTION
# ============================================================

"""
Calculate direct dB-domain reduction:

Reduction [dB]
=
Unshielded [dBµV]
-
Case B [dBµV]
"""


reduction_db = (

    unshielded_dbuV

    - case_b_dbuV

)


maximum_reduction_index = np.argmax(
    reduction_db
)


maximum_reduction_frequency = frequency_hz[
    maximum_reduction_index
]


maximum_reduction_db = reduction_db[
    maximum_reduction_index
]


print(
    "\n--- Maximum Sampled Reduction ---"
)


print(
    f"Frequency = "
    f"{maximum_reduction_frequency:.3e} Hz"
)


print(
    f"Reduction = "
    f"{maximum_reduction_db:.2f} dB"
)


# ============================================================
# 49. ZOOM AROUND MAXIMUM REDUCTION
# ============================================================

reduction_zoom_min = max(

    frequency_hz.min(),

    maximum_reduction_frequency
    / 2

)


reduction_zoom_max = min(

    frequency_hz.max(),

    maximum_reduction_frequency
    * 2

)


reduction_y_min, reduction_y_max = (
    calculate_zoom_ylim(

        x=frequency_hz,

        y_arrays=reduction_db,

        x_min=reduction_zoom_min,

        x_max=reduction_zoom_max,

        padding_fraction=0.15

    )
)


# ============================================================
# 50. REDUCTION PLOT WITH INSET
# ============================================================

fig, ax = plt.subplots(
    figsize=(8.5, 5)
)


ax.plot(
    frequency_hz,
    reduction_db,
    linewidth=1.5
)


ax.axhline(
    0,
    linestyle="--",
    linewidth=1
)


ax.set_xscale(
    "log"
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Reduction [dB]"
)

ax.set_title(
    "Frequency-Domain Reduction"
)


ax.grid(
    True,
    which="both"
)


axins = ax.inset_axes(
    [
        0.50,
        0.14,
        0.44,
        0.40
    ]
)


axins.plot(
    frequency_hz,
    reduction_db,
    linewidth=1
)


axins.axhline(
    0,
    linestyle="--",
    linewidth=0.8
)


axins.scatter(
    maximum_reduction_frequency,
    maximum_reduction_db,
    s=18
)


axins.set_xscale(
    "log"
)


axins.set_xlim(
    reduction_zoom_min,
    reduction_zoom_max
)


axins.set_ylim(
    reduction_y_min,
    reduction_y_max
)


axins.tick_params(
    labelsize=7
)


axins.grid(
    True,
    which="both"
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 51. ENGINEERING THRESHOLD INSIDE INSET
# ============================================================

"""
An inset can include an engineering threshold.

Example:

5 dB reduction target.
"""


reduction_target_db = 5


fig, ax = plt.subplots(
    figsize=(8.5, 5)
)


ax.plot(
    frequency_hz,
    reduction_db
)


ax.axhline(
    reduction_target_db,
    linestyle="--",
    label="5 dB target"
)


ax.set_xscale(
    "log"
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Reduction [dB]"
)


ax.legend()


ax.grid(
    True,
    which="both"
)


axins = ax.inset_axes(
    [
        0.50,
        0.14,
        0.44,
        0.40
    ]
)


axins.plot(
    frequency_hz,
    reduction_db
)


axins.axhline(
    reduction_target_db,
    linestyle="--"
)


axins.set_xscale(
    "log"
)


axins.set_xlim(
    reduction_zoom_min,
    reduction_zoom_max
)


local_y_min = min(
    reduction_y_min,
    reduction_target_db
    - 1
)


local_y_max = max(
    reduction_y_max,
    reduction_target_db
    + 1
)


axins.set_ylim(
    local_y_min,
    local_y_max
)


axins.tick_params(
    labelsize=7
)


axins.grid(
    True,
    which="both"
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 52. MULTIPLE INSETS
# ============================================================

"""
Sometimes two different regions are scientifically useful.

Example:

Inset 1:

Startup


Inset 2:

Steady-state ripple


Use multiple insets sparingly.

Too many inset panels can make a figure difficult to read.
"""


fig, ax = plt.subplots(
    figsize=(9, 5)
)


ax.plot(
    time_ms,
    voltage_v,
    linewidth=1.5
)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True
)


# ------------------------------------------------------------
# Inset 1: startup
# ------------------------------------------------------------

startup_inset = ax.inset_axes(
    [
        0.08,
        0.52,
        0.35,
        0.38
    ]
)


startup_inset.plot(
    time_ms,
    voltage_v
)


startup_inset.set_xlim(
    0,
    0.6
)


startup_y_min, startup_y_max = (
    calculate_zoom_ylim(

        x=time_ms,

        y_arrays=voltage_v,

        x_min=0,

        x_max=0.6,

        padding_fraction=0.08

    )
)


startup_inset.set_ylim(
    startup_y_min,
    startup_y_max
)


startup_inset.tick_params(
    labelsize=7
)


startup_inset.set_title(
    "Startup",
    fontsize=8
)


# ------------------------------------------------------------
# Inset 2: ringing
# ------------------------------------------------------------

ringing_inset = ax.inset_axes(
    [
        0.58,
        0.12,
        0.35,
        0.38
    ]
)


ringing_inset.plot(
    time_ms,
    voltage_v
)


ringing_inset.set_xlim(
    zoom_x_min,
    zoom_x_max
)


ringing_inset.set_ylim(
    zoom_y_lower,
    zoom_y_upper
)


ringing_inset.tick_params(
    labelsize=7
)


ringing_inset.set_title(
    "Ringing",
    fontsize=8
)


ax.indicate_inset_zoom(
    ringing_inset
)


plt.tight_layout()

plt.show()


# ============================================================
# 53. INSET VS SUBPLOT
# ============================================================

"""
INSET

Best when:

The zoomed information is a detail of the SAME main result.


Example:

Full waveform
+
Switching transient


------------------------------------------------------------


SUBPLOT

Best when:

Both views deserve similar visual importance

or

Several different quantities are being compared.


Example:

(a) Voltage

(b) Current

(c) Power


Do not force every secondary plot into an inset.
"""


# ============================================================
# 54. SUBPLOT ALTERNATIVE
# ============================================================

fig, axes = plt.subplots(

    2,

    1,

    figsize=(8, 6),

    sharex=False

)


# Full waveform

axes[0].plot(
    time_ms,
    voltage_v
)


axes[0].set_xlabel(
    "Time [ms]"
)

axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].set_title(
    "Full Waveform"
)


axes[0].grid(
    True
)


# Zoomed waveform

axes[1].plot(
    time_ms,
    voltage_v
)


axes[1].set_xlim(
    zoom_x_min,
    zoom_x_max
)


axes[1].set_ylim(
    zoom_y_lower,
    zoom_y_upper
)


axes[1].set_xlabel(
    "Time [ms]"
)

axes[1].set_ylabel(
    "Voltage [V]"
)

axes[1].set_title(
    "Zoomed Switching Region"
)


axes[1].grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 55. ANNOTATION INSIDE INSET
# ============================================================

"""
The inset can contain a key annotation.

Example:

Maximum overshoot.
"""


overshoot_index = np.argmax(
    drain_voltage
)


overshoot_time = switch_time_ns[
    overshoot_index
]


overshoot_voltage = drain_voltage[
    overshoot_index
]


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    switch_time_ns,
    drain_voltage
)


ax.set_xlabel(
    "Time [ns]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.grid(
    True
)


axins = ax.inset_axes(
    [
        0.48,
        0.14,
        0.46,
        0.42
    ]
)


axins.plot(
    switch_time_ns,
    drain_voltage
)


axins.set_xlim(
    peak_zoom_min,
    peak_zoom_max
)


axins.set_ylim(
    peak_y_min,
    peak_y_max
)


axins.scatter(
    overshoot_time,
    overshoot_voltage,
    s=18
)


axins.annotate(

    (
        f"{overshoot_voltage:.1f} V"
    ),

    xy=(
        overshoot_time,
        overshoot_voltage
    ),

    xytext=(
        12,
        -20
    ),

    textcoords="offset points",

    fontsize=7,

    arrowprops={
        "arrowstyle":
            "->"
    }

)


axins.tick_params(
    labelsize=7
)


ax.indicate_inset_zoom(
    axins
)


plt.tight_layout()

plt.show()


# ============================================================
# 56. REUSABLE NATIVE ZOOM FUNCTION
# ============================================================

def add_zoom_inset(
    ax,
    x,
    y_arrays,
    x_min,
    x_max,
    bounds=(
        0.52,
        0.14,
        0.43,
        0.38
    ),
    labels=None,
    line_styles=None,
    x_scale="linear",
    padding_fraction=0.10,
    show_indicator=True
):
    """
    Add a reusable zoomed inset to an existing axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Parent axis.

    x : array-like
        Shared X data.

    y_arrays : array-like or list
        One or more Y arrays.

    x_min, x_max : float
        Zoomed X-axis limits.

    bounds : tuple
        Inset location:
        (x0, y0, width, height)
        in parent-axis coordinates.

    labels : list, optional
        Labels corresponding to Y arrays.

    line_styles : list, optional
        Line styles corresponding to Y arrays.

    x_scale : str
        "linear" or "log".

    padding_fraction : float
        Automatic Y-axis padding.

    show_indicator : bool
        Draw zoom rectangle/connectors.

    Returns
    -------
    inset_ax : matplotlib.axes.Axes
        Created inset axis.
    """

    x = np.asarray(
        x,
        dtype=float
    )


    if isinstance(
        y_arrays,
        np.ndarray
    ) and y_arrays.ndim == 1:

        y_arrays = [
            y_arrays
        ]


    y_arrays = [

        np.asarray(
            values,
            dtype=float
        )

        for values in y_arrays

    ]


    if labels is None:

        labels = [

            None

            for _ in y_arrays

        ]


    if line_styles is None:

        default_styles = [
            "-",
            "--",
            "-.",
            ":"
        ]


        line_styles = [

            default_styles[
                index
                % len(
                    default_styles
                )
            ]

            for index in range(
                len(
                    y_arrays
                )
            )

        ]


    if len(
        labels
    ) != len(
        y_arrays
    ):

        raise ValueError(
            "labels must match number of Y arrays."
        )


    if len(
        line_styles
    ) != len(
        y_arrays
    ):

        raise ValueError(
            "line_styles must match number of Y arrays."
        )


    y_min, y_max = calculate_zoom_ylim(

        x=x,

        y_arrays=y_arrays,

        x_min=x_min,

        x_max=x_max,

        padding_fraction=padding_fraction

    )


    inset_ax = ax.inset_axes(
        bounds
    )


    for values, label, style in zip(

        y_arrays,

        labels,

        line_styles

    ):

        inset_ax.plot(

            x,

            values,

            linestyle=style,

            linewidth=1,

            label=label

        )


    inset_ax.set_xlim(
        x_min,
        x_max
    )


    inset_ax.set_ylim(
        y_min,
        y_max
    )


    inset_ax.set_xscale(
        x_scale
    )


    inset_ax.tick_params(
        labelsize=7
    )


    inset_ax.grid(
        True,
        which="both"
    )


    if show_indicator:

        ax.indicate_inset_zoom(
            inset_ax
        )


    return inset_ax


# ============================================================
# 57. USE REUSABLE ZOOM FUNCTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    time_ms,
    simulation_voltage,
    label="Simulation"
)


ax.plot(
    time_ms,
    experimental_voltage,
    linestyle="--",
    label="Experiment"
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


zoom_axis = add_zoom_inset(

    ax=ax,

    x=time_ms,

    y_arrays=[
        simulation_voltage,
        experimental_voltage
    ],

    x_min=zoom_x_min,

    x_max=zoom_x_max,

    labels=[
        "Simulation",
        "Experiment"
    ],

    line_styles=[
        "-",
        "--"
    ],

    x_scale="linear"

)


plt.tight_layout()

plt.show()


# ============================================================
# 58. USE FUNCTION FOR FFT DATA
# ============================================================

fig, ax = plt.subplots(
    figsize=(8.5, 5)
)


ax.plot(
    frequency_hz,
    unshielded_dbuV,
    label="Unshielded"
)


ax.plot(
    frequency_hz,
    case_b_dbuV,
    linestyle="--",
    label="Case B"
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


zoom_axis = add_zoom_inset(

    ax=ax,

    x=frequency_hz,

    y_arrays=[
        unshielded_dbuV,
        case_b_dbuV
    ],

    x_min=fft_zoom_min,

    x_max=fft_zoom_max,

    labels=[
        "Unshielded",
        "Case B"
    ],

    line_styles=[
        "-",
        "--"
    ],

    x_scale="log",

    padding_fraction=0.12

)


plt.tight_layout()

plt.show()


# ============================================================
# 59. PUBLICATION-SIZED FIGURE
# ============================================================

"""
For a publication figure:

Design the main figure close to its intended final size.

Then make sure:

- Inset remains readable
- Tick labels are not too small
- Connector lines remain visible
- Legend does not overlap inset
- Important data are not hidden
"""


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

    * 0.58

)


# ============================================================
# 60. FINAL PUBLICATION ENGINEERING FIGURE
# ============================================================

fig, ax = plt.subplots(

    figsize=(
        publication_width_in,
        publication_height_in
    )

)


ax.plot(
    frequency_hz,
    unshielded_dbuV,
    linewidth=1.4,
    label="Unshielded"
)


ax.plot(
    frequency_hz,
    case_b_dbuV,
    linewidth=1.4,
    linestyle="--",
    label="Case B"
)


ax.set_xscale(
    "log"
)


ax.set_xlabel(
    "Frequency [Hz]",
    fontsize=9
)


ax.set_ylabel(
    "Magnitude [dBµV]",
    fontsize=9
)


ax.tick_params(
    labelsize=8,
    direction="in",
    top=True,
    right=True
)


ax.legend(
    fontsize=8,
    loc="best"
)


ax.grid(
    True,
    which="major",
    linewidth=0.5,
    alpha=0.4
)


# ------------------------------------------------------------
# Publication inset
# ------------------------------------------------------------

publication_inset = ax.inset_axes(
    [
        0.52,
        0.14,
        0.43,
        0.40
    ]
)


publication_inset.plot(
    frequency_hz,
    unshielded_dbuV,
    linewidth=1
)


publication_inset.plot(
    frequency_hz,
    case_b_dbuV,
    linewidth=1,
    linestyle="--"
)


publication_inset.set_xscale(
    "log"
)


publication_inset.set_xlim(
    fft_zoom_min,
    fft_zoom_max
)


publication_inset.set_ylim(
    fft_y_min,
    fft_y_max
)


publication_inset.tick_params(
    labelsize=7,
    direction="in"
)


publication_inset.grid(
    True,
    which="major",
    linewidth=0.4,
    alpha=0.4
)


ax.indicate_inset_zoom(
    publication_inset
)


plt.tight_layout()


# ============================================================
# 61. SAVE PNG
# ============================================================

png_file = (
    output_figure_folder
    / "engineering_fft_inset.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 62. SAVE PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "engineering_fft_inset.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 63. SAVE SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "engineering_fft_inset.svg"
)


fig.savefig(
    svg_file,
    bbox_inches="tight"
)


print(
    "\n--- Publication Figures Saved ---"
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
# 64. SAVE BEFORE show()
# ============================================================

"""
For final research figures:

Create
    ↓
Format
    ↓
Save
    ↓
show()


This avoids possible backend-dependent issues after the
figure window has been closed.
"""


# ============================================================
# 65. INSET DOES NOT CHANGE THE ORIGINAL DATA
# ============================================================

"""
An inset should normally show the SAME underlying data with
different axis limits.

Main plot:

Full range


Inset:

Selected range


The inset is a visual magnification, not new experimental
data.
"""


# ============================================================
# 66. ZOOMING VS FILTERING
# ============================================================

"""
VISUAL ZOOM

set_xlim()

set_ylim()


The complete dataset remains plotted.


------------------------------------------------------------


DATA FILTERING

data = data[
    condition
]


Observations outside the selected region are removed from
the processed subset.


These are different operations.
"""


# ============================================================
# 67. COMMON MISTAKE - DIFFERENT UNITS
# ============================================================

"""
Main axis:

Time [ms]


Inset:

Time [µs]


This may be scientifically valid,

but it must be clearly labeled.


Do not silently change units between the main plot and
inset.
"""


# ============================================================
# 68. COMMON MISTAKE - DIFFERENT AXIS SCALE
# ============================================================

"""
Main FFT plot:

Logarithmic X-axis


Inset:

Linear X-axis


can significantly change visual spacing.


Use a different scale only when it supports a specific
analysis and is clearly communicated.
"""


# ============================================================
# 69. COMMON MISTAKE - EXCESSIVE MAGNIFICATION
# ============================================================

"""
Suppose two signals differ by only:

0.001%


An extremely narrow Y-axis can make the curves appear
dramatically different.


The numerical magnitude should always remain visible and
the interpretation should reflect the actual engineering
significance.
"""


# ============================================================
# 70. COMMON MISTAKE - INSET HIDES IMPORTANT DATA
# ============================================================

"""
An inset placed over:

Maximum peak

Resonance

Legend

Transition

or

Important comparison region


can make the main plot harder to interpret.

Choose inset position carefully.
"""


# ============================================================
# 71. COMMON MISTAKE - NO ZOOM INDICATOR
# ============================================================

"""
Without a rectangle or connector, the reader may not know:

Which region was magnified?


Use:

indicate_inset_zoom()

or:

mark_inset()


when it improves clarity.
"""


# ============================================================
# 72. COMMON MISTAKE - TINY INSET
# ============================================================

"""
A very small inset may technically contain the information
but still be unreadable after publication scaling.

Check:

Tick labels

Lines

Markers

Annotations


at final document size.
"""


# ============================================================
# 73. COMMON MISTAKE - HUGE INSET
# ============================================================

"""
If the inset occupies most of the figure:

The main plot loses its role as context.


Consider instead:

Two subplots.
"""


# ============================================================
# 74. COMMON MISTAKE - TOO MANY INSETS
# ============================================================

"""
Three, four, or five inset windows can make one figure
difficult to follow.

If several regions require detailed discussion:

Use:

Multi-panel figures

or

Separate figures.
"""


# ============================================================
# 75. COMMON MISTAKE - DIFFERENT DATA IN THE INSET
# ============================================================

"""
If the main figure shows:

Simulation


but the inset unexpectedly shows:

Experiment


the comparison becomes ambiguous.


Inset content should be traceable to the main figure.
"""


# ============================================================
# 76. COMMON MISTAKE - CHERRY-PICKING
# ============================================================

"""
Do not zoom only into the region where a preferred design
looks better while ignoring regions where it performs
worse.


The full plot should provide enough context for a fair
comparison.
"""


# ============================================================
# 77. COMMON MISTAKE - NO NUMERICAL CONTEXT
# ============================================================

"""
A magnified difference may look large.

Report:

Actual magnitude

Unit

Operating condition


Example:

Difference = 0.15 V


rather than only:

"Design B is significantly different."
"""


# ============================================================
# 78. COMMON MISTAKE - INSET USED INSTEAD OF ANALYSIS
# ============================================================

"""
An inset can reveal:

Overshoot

Ringing

Peak difference


but quantitative analysis should still calculate values
such as:

Peak voltage

Rise time

Settling time

Ripple

Frequency

Reduction

Error
"""


# ============================================================
# 79. COMMON MISTAKE - INSET LABELS TOO LARGE
# ============================================================

"""
Inset labels that use the same oversized typography as the
main figure can consume too much space.

Use a slightly smaller but still readable font.
"""


# ============================================================
# 80. COMMON MISTAKE - INSET LABELS TOO SMALL
# ============================================================

"""
Do not reduce inset text simply because the axis is small.

At final publication dimensions:

The text still needs to be readable.
"""


# ============================================================
# 81. COMMON MISTAKE - SCREENSHOT OF ZOOM
# ============================================================

"""
Do not manually zoom the interactive Matplotlib window and
take a screenshot.

Create the zoomed region directly in Python so that:

Axis limits

Data

Labels

Resolution

Export

remain reproducible.
"""


# ============================================================
# 82. COMMON MISTAKE - NO REPRODUCIBLE ZOOM LIMITS
# ============================================================

"""
Instead of manually adjusting until the plot looks good,
store the selected limits in code.

Example:

zoom_x_min = 1.95

zoom_x_max = 2.05


This makes the research figure reproducible.
"""


# ============================================================
# 83. SWITCHING-TRANSIENT WORKFLOW
# ============================================================

"""
Full Switching Waveform
        ↓
Identify Transition
        ↓
Select Time Window
        ↓
Calculate Local Y Range
        ↓
Create Inset
        ↓
Show Overshoot / Ringing
        ↓
Calculate Peak Values
        ↓
Engineering Interpretation
"""


# ============================================================
# 84. RIPPLE WORKFLOW
# ============================================================

"""
DC Output Signal
        ↓
Full Operating Window
        ↓
Select Steady-State Region
        ↓
Zoom
        ↓
Measure:
Peak
Minimum
Peak-to-Peak Ripple
        ↓
Interpret
"""


# ============================================================
# 85. FFT INSET WORKFLOW
# ============================================================

"""
Full Spectrum
        ↓
Logarithmic Frequency Axis
        ↓
Identify Peak / Resonance / Band
        ↓
Choose Frequency Window
        ↓
Create Logarithmic Inset
        ↓
Compare Cases
        ↓
Quantify dB Difference
        ↓
Engineering Interpretation
"""


# ============================================================
# 86. SIMULATION VS EXPERIMENT WORKFLOW
# ============================================================

"""
Simulation
      +
Experiment
        ↓
Full Comparison
        ↓
Calculate Absolute Difference
        ↓
Find Important Region
        ↓
Inset
        ↓
Detailed Agreement / Deviation
        ↓
Quantify Error
"""


# ============================================================
# 87. INSET DECISION GUIDE
# ============================================================

"""
Need the whole waveform only?
        ↓
NORMAL LINE PLOT


Need one detail while preserving context?
        ↓
INSET


Need two equally important views?
        ↓
SUBPLOTS


Need several detailed regions?
        ↓
MULTI-PANEL FIGURE


Need a different physical variable?
        ↓
SUBPLOT
or
DUAL AXIS
depending on the problem
"""


# ============================================================
# 88. PUBLICATION CHECKLIST
# ============================================================

"""
Before publishing an inset figure, check:

MAIN PLOT
------------------------------------------------------------

Does it show the complete relevant context?

Are units correct?

Are axis limits fair?


INSET
------------------------------------------------------------

Does it show the same underlying data?

Is the zoom range scientifically justified?

Are units clearly understood?

Is the scale linear or logarithmic as intended?


INDICATOR
------------------------------------------------------------

Can the reader identify the magnified region?


POSITION
------------------------------------------------------------

Does the inset hide important data?

Does it overlap the legend?


READABILITY
------------------------------------------------------------

Are inset ticks readable?

Are lines distinguishable?

Are annotations readable?


INTERPRETATION
------------------------------------------------------------

Is the numerical magnitude of the difference stated?

Is magnification being mistaken for physical significance?


REPRODUCIBILITY
------------------------------------------------------------

Are zoom limits stored in code?

Can the figure be regenerated directly?


OUTPUT
------------------------------------------------------------

PNG saved?

PDF saved?

SVG saved?

Checked at final paper size?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
INSET AND ZOOMED PLOTS


1. BASIC NATIVE INSET

axins = ax.inset_axes(

    [
        x0,
        y0,
        width,
        height
    ]

)


------------------------------------------------------------


2. PLOT SAME DATA

axins.plot(
    x,
    y
)


------------------------------------------------------------


3. SELECT ZOOM REGION

axins.set_xlim(

    x_min,

    x_max

)


axins.set_ylim(

    y_min,

    y_max

)


------------------------------------------------------------


4. MARK ZOOM REGION

ax.indicate_inset_zoom(
    axins
)


This helps connect:

Main plot

to

Inset detail.


------------------------------------------------------------


5. AUTOMATIC Y LIMITS

Select data inside:

x_min
to
x_max


Then calculate:

Minimum

Maximum

Padding


------------------------------------------------------------


6. axes_grid1 INSET

axins = inset_axes(

    ax,

    width="40%",

    height="35%",

    loc="lower right"

)


------------------------------------------------------------


7. ZOOMED INSET AXES

axins = zoomed_inset_axes(

    ax,

    zoom=3,

    loc="lower right"

)


------------------------------------------------------------


8. mark_inset()

mark_inset(

    ax,

    axins,

    loc1=2,

    loc2=4

)


Useful for drawing:

Zoom rectangle

+
Connectors


------------------------------------------------------------


9. TIME-DOMAIN APPLICATIONS

Useful for:

Switching transition

Overshoot

Ringing

Ripple

Settling

Measurement noise


------------------------------------------------------------


10. FREQUENCY-DOMAIN APPLICATIONS

Useful for:

Resonance

Harmonics

Peak comparison

Narrow EMI band

Spectral reduction


------------------------------------------------------------


11. LOGARITHMIC FREQUENCY

If the main spectrum uses:

Log X-axis


the inset will often also use:

Log X-axis


unless another representation is intentionally required.


------------------------------------------------------------


12. AUTOMATIC PEAK ZOOM

peak_index = np.argmax(
    y
)


peak_x = x[
    peak_index
]


Then define a window around the peak.


------------------------------------------------------------


13. MULTIPLE CASES

Plot the same cases in:

Main axis

and

Inset


for traceable comparison.


------------------------------------------------------------


14. DIFFERENCE-CENTERED ZOOM

difference = np.abs(

    case_a

    - case_b

)


The largest difference can help identify a candidate zoom
region.


------------------------------------------------------------


15. INSET vs SUBPLOT

INSET:

Detail of main result


SUBPLOT:

Separate or equally important result


------------------------------------------------------------


16. MULTIPLE INSETS

Possible,

but use sparingly.


Too many inset windows can reduce readability.


------------------------------------------------------------


17. UNIT CONSISTENCY

Main:

Time [ms]


Inset:

Time [ms]


is easiest to interpret.


If units change:

Label them explicitly.


------------------------------------------------------------


18. MAGNIFICATION

A larger visual difference in an inset does not mean the
physical difference itself is large.


Always report numerical values.


------------------------------------------------------------


19. ZOOMING != FILTERING

set_xlim()

changes the visible region.


Boolean filtering changes the selected dataset.


------------------------------------------------------------


20. REPRODUCIBILITY

Store:

Zoom minimum

Zoom maximum

Inset bounds

Scale

Annotations


inside the Python script.


------------------------------------------------------------


21. ENGINEERING APPLICATIONS

Inset figures are especially useful for:

GaN switching transients

Voltage overshoot

Current ringing

Converter ripple

Simulation vs experiment

FFT peaks

EMI spectra

Control settling

Small efficiency differences

Error analysis


------------------------------------------------------------


22. PUBLICATION EXPORT

Useful outputs:

PNG

PDF

SVG


------------------------------------------------------------


23. MOST IMPORTANT PRINCIPLE

An inset should answer:

"What important detail cannot be seen clearly in the full
figure?"


It should not be added only for decoration.


------------------------------------------------------------


24. COMPLETE WORKFLOW

Engineering Result
        ↓
Plot Full Data
        ↓
Identify Important Region
        ↓
Select Zoom Limits
        ↓
Calculate Local Y Range
        ↓
Create Inset
        ↓
Plot Same Data
        ↓
Mark Zoom Region
        ↓
Add Necessary Annotation
        ↓
Quantify Result
        ↓
Check Final Size
        ↓
Export


------------------------------------------------------------


NEXT:

27_multi_panel_publication_figures.py


The next file will focus on one of the most important
research-paper plotting workflows:

(a), (b), (c), (d) figures

2 × 1 layouts

1 × 2 layouts

2 × 2 layouts

GridSpec

Different panel sizes

Shared X axes

Shared Y axes

Common legends

Panel labels

Common X/Y labels

Removing unused axes

Mixing line plots, bars, heatmaps, and contours

One colorbar for several panels

Consistent axis limits

Publication dimensions

Tight/constrained layouts

High-resolution export

and complete multi-panel engineering figures.
"""
