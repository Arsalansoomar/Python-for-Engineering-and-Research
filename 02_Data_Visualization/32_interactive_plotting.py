"""
============================================================
Python for Engineering and Research
32 - Interactive Plotting
============================================================

Purpose:
    Demonstrate how Matplotlib interaction and widgets can
    be used to explore engineering datasets, parameter
    sweeps, time-domain signals, FFT spectra, operating
    points, and design cases interactively.

Topics:
    1. What is interactive plotting?
    2. Static vs interactive figures
    3. Interactive backends
    4. Matplotlib toolbar
    5. plt.ion() / plt.ioff()
    6. Event-driven plotting
    7. Callback functions
    8. Slider widget
    9. Multiple sliders
    10. Slider reset
    11. Discrete sliders
    12. Engineering operating-point slider
    13. Parameter-sweep cross sections
    14. RangeSlider
    15. Interactive frequency window
    16. Button widget
    17. Reset button
    18. Save-current-view button
    19. RadioButtons
    20. Interactive case selection
    21. CheckButtons
    22. Toggle multiple engineering curves
    23. TextBox
    24. Numerical parameter input
    25. Cursor
    26. SpanSelector
    27. Interactive time-window selection
    28. RMS calculation from selected region
    29. Mouse-click events
    30. Point inspection
    31. Keyboard events
    32. Interactive FFT comparison
    33. Interactive frequency-band analysis
    34. Interactive parameter-map cross section
    35. Dynamic annotations
    36. Reusable interactive functions
    37. Saving static snapshots
    38. Interactive vs publication figures
    39. Backend limitations
    40. Common mistakes
    41. Key takeaways

Sample File:
    sample_data/fft_example.csv

Important:
    Interactive visualization is mainly an ANALYSIS and
    EXPLORATION tool.

    Journal papers normally require reproducible static
    figures.

    Therefore a strong research workflow is:

    Interactive Exploration
            ↓
    Identify Important Result
            ↓
    Record Numerical Parameters
            ↓
    Generate Static Publication Figure
            ↓
    Export PNG / PDF / SVG

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

from matplotlib.widgets import (
    Slider,
    RangeSlider,
    Button,
    RadioButtons,
    CheckButtons,
    TextBox,
    Cursor,
    SpanSelector
)


# ============================================================
# 2. WHAT IS INTERACTIVE PLOTTING?
# ============================================================

"""
A normal static workflow is:

Data
    ↓
Plot
    ↓
Save Figure


An interactive workflow is:

Data
    ↓
Plot
    ↓
User Changes Something
    ↓
Callback Function
    ↓
Plot Updates
    ↓
User Explores Another Condition
    ↓
Plot Updates Again


Examples:

Move a slider
        ↓
Change switching frequency


Move another slider
        ↓
Change load


Click checkbox
        ↓
Hide / show design case


Drag frequency range
        ↓
Analyse only selected band
"""


# ============================================================
# 3. ENGINEERING APPLICATIONS
# ============================================================

"""
Interactive plotting is useful for:

- Parameter sweeps
- Converter operating-point exploration
- Switching-frequency selection
- Load variation
- FFT / EMI exploration
- Frequency-band selection
- Comparing multiple designs
- Experimental waveform inspection
- Simulation-vs-experiment comparison
- Selecting analysis windows
- Calculating local RMS
- Peak inspection
- Control-parameter tuning
- Sensitivity studies
- DOE exploration
- ML prediction visualization
"""


# ============================================================
# 4. STATIC VS INTERACTIVE
# ============================================================

"""
STATIC FIGURE

Best for:

Paper

Thesis

Report

Presentation

GitHub README

Archiving


------------------------------------------------------------


INTERACTIVE FIGURE

Best for:

Exploration

Debugging

Parameter selection

Data inspection

Sensitivity analysis

Finding interesting regions


------------------------------------------------------------


A useful research workflow uses BOTH.
"""


# ============================================================
# 5. IMPORTANT BACKEND NOTE
# ============================================================

"""
Interactive widgets require an interactive Matplotlib
backend.

Depending on the environment, figures may appear in:

A desktop GUI window

A notebook interactive canvas

An IDE plot window


If the environment uses a completely static backend,
widgets may be displayed but may not respond interactively.


This file is therefore best tested in an environment such
as:

Python script + GUI backend

Spyder

PyCharm

VS Code

Jupyter with an appropriate interactive Matplotlib backend
"""


# ============================================================
# 6. PROJECT PATHS
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
    / "interactive"
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
    "\n--- Interactive Plot Output Folder ---"
)


print(
    output_figure_folder
)


# ============================================================
# 7. CHECK INTERACTIVE MODE
# ============================================================

print(
    "\n--- Matplotlib Interactive Mode ---"
)


print(
    plt.isinteractive()
)


# ============================================================
# 8. plt.ion()
# ============================================================

"""
Interactive mode can be enabled using:

plt.ion()


and disabled using:

plt.ioff()


Whether this is necessary depends on:

Environment

Backend

How the script is executed


For most standalone examples below:

plt.show()

is sufficient to launch the interactive figure.
"""


# ============================================================
# 9. OPTIONAL INTERACTIVE MODE
# ============================================================

"""
Example:

plt.ion()

print(
    plt.isinteractive()
)

plt.ioff()


We will not globally force interactive mode here because:

Interactive behavior differs between environments.
"""


# ============================================================
# 10. MATPLOTLIB TOOLBAR
# ============================================================

"""
Many GUI Matplotlib windows already provide toolbar tools
such as:

Pan

Zoom

Home / Reset View

Back

Forward

Save Figure


These are interactive even before custom widgets are added.


Custom widgets become useful when interaction needs to
change the ENGINEERING MODEL or DATA itself.
"""


# ============================================================
# 11. FIRST SLIDER EXAMPLE
# ============================================================

"""
LEVEL 1 — CONCEPT

A slider allows a numerical value to be changed
interactively.


LEVEL 2 — SYNTAX

slider = Slider(
    slider_axis,
    "Amplitude",
    minimum,
    maximum,
    valinit=initial_value
)


slider.on_changed(
    callback_function
)


LEVEL 3 — ENGINEERING APPLICATION

Change:

Ripple amplitude

Switching frequency

Load

Resistance

Capacitance

Temperature

etc.
"""


# ============================================================
# 12. CREATE BASIC SIGNAL
# ============================================================

time_s = np.linspace(
    0,
    0.002,
    3000
)


initial_frequency_hz = 5_000

initial_amplitude_v = 5.0


signal_v = (

    initial_amplitude_v

    * np.sin(
        2
        * np.pi
        * initial_frequency_hz
        * time_s
    )

)


# ============================================================
# 13. BASIC SLIDER FIGURE
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)


# Leave space under the plot for slider

fig.subplots_adjust(
    bottom=0.23
)


line, = ax.plot(

    time_s
    * 1000,

    signal_v

)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Interactive Signal Amplitude"
)


ax.grid(
    True
)


# Slider axis

amplitude_slider_axis = fig.add_axes(
    [
        0.18,
        0.08,
        0.65,
        0.04
    ]
)


amplitude_slider = Slider(

    ax=amplitude_slider_axis,

    label="Amplitude [V]",

    valmin=1.0,

    valmax=10.0,

    valinit=initial_amplitude_v

)


# ============================================================
# 14. SLIDER CALLBACK
# ============================================================

def update_amplitude(
    value
):
    """
    Update waveform when amplitude slider changes.
    """

    new_amplitude = (
        amplitude_slider.val
    )


    new_signal = (

        new_amplitude

        * np.sin(
            2
            * np.pi
            * initial_frequency_hz
            * time_s
        )

    )


    line.set_ydata(
        new_signal
    )


    ax.set_ylim(

        -1.15
        * new_amplitude,

        1.15
        * new_amplitude

    )


    fig.canvas.draw_idle()


# Connect slider to callback

amplitude_slider.on_changed(
    update_amplitude
)


plt.show()


# ============================================================
# 15. WHAT IS draw_idle()?
# ============================================================

"""
Inside interactive callbacks use:

fig.canvas.draw_idle()


This requests that the canvas be redrawn after the plotted
data have changed.


Typical callback:

Change Parameter
        ↓
Calculate New Data
        ↓
line.set_ydata(...)
        ↓
fig.canvas.draw_idle()
"""


# ============================================================
# 16. TWO SLIDERS
# ============================================================

"""
Now control:

Amplitude

and

Frequency


simultaneously.
"""


initial_amplitude = 5.0

initial_frequency = 3_000


fig, ax = plt.subplots(
    figsize=(8, 5.5)
)


fig.subplots_adjust(
    bottom=0.30
)


initial_signal = (

    initial_amplitude

    * np.sin(
        2
        * np.pi
        * initial_frequency
        * time_s
    )

)


signal_line, = ax.plot(

    time_s
    * 1000,

    initial_signal

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
# Amplitude slider
# ------------------------------------------------------------

amplitude_axis = fig.add_axes(
    [
        0.18,
        0.14,
        0.65,
        0.035
    ]
)


amplitude_control = Slider(

    amplitude_axis,

    "Amplitude [V]",

    1.0,

    10.0,

    valinit=initial_amplitude

)


# ------------------------------------------------------------
# Frequency slider
# ------------------------------------------------------------

frequency_axis = fig.add_axes(
    [
        0.18,
        0.07,
        0.65,
        0.035
    ]
)


frequency_control = Slider(

    frequency_axis,

    "Frequency [Hz]",

    500,

    10_000,

    valinit=initial_frequency

)


# ============================================================
# 17. MULTI-SLIDER CALLBACK
# ============================================================

def update_signal(
    value
):
    """
    Read both slider values and update the waveform.
    """

    amplitude = (
        amplitude_control.val
    )


    frequency = (
        frequency_control.val
    )


    updated_signal = (

        amplitude

        * np.sin(
            2
            * np.pi
            * frequency
            * time_s
        )

    )


    signal_line.set_ydata(
        updated_signal
    )


    ax.set_ylim(

        -1.15
        * amplitude,

        1.15
        * amplitude

    )


    fig.canvas.draw_idle()


amplitude_control.on_changed(
    update_signal
)


frequency_control.on_changed(
    update_signal
)


plt.show()


# ============================================================
# 18. IMPORTANT WIDGET REFERENCE RULE
# ============================================================

"""
Keep references to widget objects:

amplitude_control

frequency_control


Do not create a widget and immediately lose the object
reference.

Interactive widgets need to remain alive while the figure
is active.
"""


# ============================================================
# 19. DISCRETE SLIDER
# ============================================================

"""
Sometimes engineering parameters are discrete.

Example:

Gate resistance:

2 Ω

4 Ω

6 Ω

8 Ω

10 Ω


Use:

valstep=
"""


gate_resistance_values = np.array(
    [
        2,
        4,
        6,
        8,
        10
    ],
    dtype=float
)


fig, ax = plt.subplots(
    figsize=(8, 5)
)


fig.subplots_adjust(
    bottom=0.23
)


switching_time_ns = np.linspace(
    0,
    500,
    1000
)


initial_gate_resistance = 4.0


def calculate_switching_voltage(
    resistance_ohm
):
    """
    Synthetic teaching model.

    Larger gate resistance produces slower transition.

    This is not intended as a device-accurate model.
    """

    time_constant = (

        20

        + 4
        * resistance_ohm

    )


    voltage = (

        400

        * (
            1
            - np.exp(
                -switching_time_ns
                / time_constant
            )
        )

    )


    return voltage


switching_line, = ax.plot(

    switching_time_ns,

    calculate_switching_voltage(
        initial_gate_resistance
    )

)


ax.set_xlabel(
    "Time [ns]"
)

ax.set_ylabel(
    "Drain Voltage [V]"
)

ax.set_title(
    "Interactive Gate-Resistance Example"
)


ax.grid(
    True
)


gate_slider_axis = fig.add_axes(
    [
        0.18,
        0.08,
        0.65,
        0.04
    ]
)


gate_slider = Slider(

    gate_slider_axis,

    "Gate Resistance [Ω]",

    valmin=gate_resistance_values.min(),

    valmax=gate_resistance_values.max(),

    valinit=initial_gate_resistance,

    valstep=gate_resistance_values

)


def update_gate_resistance(
    value
):

    resistance = (
        gate_slider.val
    )


    switching_line.set_ydata(

        calculate_switching_voltage(
            resistance
        )

    )


    ax.set_title(

        "Gate Resistance = "
        f"{resistance:.0f} Ω"

    )


    fig.canvas.draw_idle()


gate_slider.on_changed(
    update_gate_resistance
)


plt.show()


# ============================================================
# 20. ENGINEERING PARAMETER-SWEEP DATA
# ============================================================

"""
Now create:

Switching Frequency [kHz]

Load [%]

Efficiency [%]


The model is synthetic and intended only for teaching.
"""


switching_frequency_khz = np.linspace(

    50,

    250,

    101

)


load_percent = np.linspace(

    20,

    100,

    81

)


frequency_grid, load_grid = np.meshgrid(

    switching_frequency_khz,

    load_percent

)


efficiency_map = (

    96.2

    - 0.000050
    * (
        frequency_grid
        - 135
    ) ** 2

    - 0.00035
    * (
        load_grid
        - 75
    ) ** 2

)


# ============================================================
# 21. INTERACTIVE LOAD CROSS-SECTION
# ============================================================

"""
The 2D parameter map contains:

Frequency × Load → Efficiency


A slider can select:

Load


and dynamically show:

Efficiency vs Frequency

for that load.
"""


initial_load = 60.0


initial_load_index = np.argmin(

    np.abs(
        load_percent
        - initial_load
    )

)


fig, axes = plt.subplots(

    1,

    2,

    figsize=(11, 5)

)


fig.subplots_adjust(
    bottom=0.22
)


# ------------------------------------------------------------
# Parameter map
# ------------------------------------------------------------

parameter_image = axes[
    0
].pcolormesh(

    frequency_grid,

    load_grid,

    efficiency_map,

    shading="auto",

    cmap="viridis"

)


colorbar = fig.colorbar(

    parameter_image,

    ax=axes[
        0
    ]

)


colorbar.set_label(
    "Efficiency [%]"
)


axes[
    0
].set_xlabel(
    "Switching Frequency [kHz]"
)


axes[
    0
].set_ylabel(
    "Load [%]"
)


selected_load_line = axes[
    0
].axhline(

    load_percent[
        initial_load_index
    ],

    linestyle="--"

)


# ------------------------------------------------------------
# Cross section
# ------------------------------------------------------------

cross_section_line, = axes[
    1
].plot(

    switching_frequency_khz,

    efficiency_map[
        initial_load_index,
        :
    ]

)


axes[
    1
].set_xlabel(
    "Switching Frequency [kHz]"
)


axes[
    1
].set_ylabel(
    "Efficiency [%]"
)


axes[
    1
].set_title(
    f"Load = "
    f"{load_percent[initial_load_index]:.0f}%"
)


axes[
    1
].grid(
    True
)


# ------------------------------------------------------------
# Load slider
# ------------------------------------------------------------

load_slider_axis = fig.add_axes(
    [
        0.20,
        0.07,
        0.60,
        0.04
    ]
)


load_slider = Slider(

    load_slider_axis,

    "Load [%]",

    valmin=load_percent.min(),

    valmax=load_percent.max(),

    valinit=initial_load,

    valstep=load_percent

)


# ============================================================
# 22. PARAMETER-MAP CALLBACK
# ============================================================

def update_load_cross_section(
    value
):

    selected_load = (
        load_slider.val
    )


    index = np.argmin(

        np.abs(
            load_percent
            - selected_load
        )

    )


    cross_section_line.set_ydata(

        efficiency_map[
            index,
            :
        ]

    )


    selected_load_line.set_ydata(
        [
            load_percent[
                index
            ],
            load_percent[
                index
            ]
        ]
    )


    axes[
        1
    ].set_title(

        f"Load = "
        f"{load_percent[index]:.0f}%"

    )


    axes[
        1
    ].relim()


    axes[
        1
    ].autoscale_view(
        scalex=False,
        scaley=True
    )


    fig.canvas.draw_idle()


load_slider.on_changed(
    update_load_cross_section
)


plt.show()


# ============================================================
# 23. WHY CROSS-SECTIONS ARE USEFUL
# ============================================================

"""
An interactive parameter map helps answer:

How does efficiency change with frequency

at:

20% load?

40% load?

60% load?

80% load?

100% load?


Instead of manually generating:

Five separate figures.
"""


# ============================================================
# 24. RangeSlider
# ============================================================

"""
A RangeSlider selects:

Minimum value

and

Maximum value


simultaneously.

Example:

Frequency window:

1 MHz
to
5 MHz
"""


# ============================================================
# 25. LOAD FFT SAMPLE DATA
# ============================================================

fft_file = (
    sample_data_folder
    / "fft_example.csv"
)


if fft_file.exists():

    fft_data = pd.read_csv(
        fft_file
    )

else:

    print(
        "\nFFT sample file not found."
    )


    print(
        "Creating synthetic FFT data."
    )


    synthetic_frequency = np.logspace(

        4,

        np.log10(
            30e6
        ),

        700

    )


    log_f = np.log10(
        synthetic_frequency
    )


    synthetic_unshielded = (

        110

        - 9
        * (
            log_f
            - 4
        )

        + 5
        * np.sin(
            6
            * log_f
        )

    )


    fft_data = pd.DataFrame(
        {
            "Frequency_Hz":
                synthetic_frequency,

            "Unshielded_dBuV":
                synthetic_unshielded,

            "Case_A_dBuV":
                synthetic_unshielded
                - 4,

            "Case_B_dBuV":
                synthetic_unshielded
                - 8,

            "Case_C_dBuV":
                synthetic_unshielded
                - 5
        }
    )


# ============================================================
# 26. VALIDATE FFT COLUMNS
# ============================================================

fft_columns = [

    "Frequency_Hz",

    "Unshielded_dBuV",

    "Case_A_dBuV",

    "Case_B_dBuV",

    "Case_C_dBuV"

]


missing_fft_columns = [

    column

    for column in fft_columns

    if column not in fft_data.columns

]


if missing_fft_columns:

    raise KeyError(
        f"Missing FFT columns: "
        f"{missing_fft_columns}"
    )


# ============================================================
# 27. CLEAN FFT DATA
# ============================================================

for column in fft_columns:

    fft_data[
        column
    ] = pd.to_numeric(

        fft_data[
            column
        ],

        errors="coerce"

    )


fft_data = fft_data.dropna(
    subset=fft_columns
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


case_a_dbuV = fft_data[
    "Case_A_dBuV"
].to_numpy()


case_b_dbuV = fft_data[
    "Case_B_dBuV"
].to_numpy()


case_c_dbuV = fft_data[
    "Case_C_dBuV"
].to_numpy()


# ============================================================
# 28. INTERACTIVE FREQUENCY RangeSlider
# ============================================================

"""
RangeSlider will select a frequency interval.

Because frequency spans several decades, we will move the
slider in:

log10(frequency)

rather than raw frequency.

This gives more useful interactive control across decades.
"""


log_frequency = np.log10(
    frequency_hz
)


initial_frequency_limits = (

    max(
        frequency_hz.min(),
        100e3
    ),

    min(
        frequency_hz.max(),
        10e6
    )

)


initial_log_limits = (

    np.log10(
        initial_frequency_limits[
            0
        ]
    ),

    np.log10(
        initial_frequency_limits[
            1
        ]
    )

)


fig, ax = plt.subplots(
    figsize=(8.5, 5.5)
)


fig.subplots_adjust(
    bottom=0.24
)


spectrum_line, = ax.plot(

    frequency_hz,

    unshielded_dbuV,

    label="Unshielded"

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


range_slider_axis = fig.add_axes(
    [
        0.18,
        0.08,
        0.65,
        0.04
    ]
)


frequency_range_slider = RangeSlider(

    range_slider_axis,

    "log10(f) Range",

    valmin=log_frequency.min(),

    valmax=log_frequency.max(),

    valinit=initial_log_limits

)


# ============================================================
# 29. RANGE CALLBACK
# ============================================================

def update_frequency_range(
    values
):

    log_minimum, log_maximum = (
        frequency_range_slider.val
    )


    frequency_minimum = (

        10 ** log_minimum

    )


    frequency_maximum = (

        10 ** log_maximum

    )


    ax.set_xlim(

        frequency_minimum,

        frequency_maximum

    )


    selected_mask = (

        (
            frequency_hz
            >= frequency_minimum
        )

        &

        (
            frequency_hz
            <= frequency_maximum
        )

    )


    if np.any(
        selected_mask
    ):

        selected_values = (
            unshielded_dbuV[
                selected_mask
            ]
        )


        minimum = selected_values.min()

        maximum = selected_values.max()


        padding = max(

            0.08
            * (
                maximum
                - minimum
            ),

            1.0

        )


        ax.set_ylim(

            minimum
            - padding,

            maximum
            + padding

        )


    fig.canvas.draw_idle()


frequency_range_slider.on_changed(
    update_frequency_range
)


plt.show()


# ============================================================
# 30. WHY USE LOG-FREQUENCY CONTROL?
# ============================================================

"""
Suppose frequency spans:

10 kHz

to

30 MHz


A linear slider places most of the visual travel in the
high-frequency region.


Using:

log10(frequency)


gives approximately equal slider space to each frequency
decade.
"""


# ============================================================
# 31. BUTTON WIDGET
# ============================================================

"""
Buttons trigger actions.

Examples:

Reset

Save

Next Case

Previous Case

Apply Filter

Calculate Metric
"""


# ============================================================
# 32. SLIDER + RESET BUTTON
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5.5)
)


fig.subplots_adjust(
    bottom=0.30
)


initial_amplitude = 5

initial_frequency = 3000


reset_line, = ax.plot(

    time_s
    * 1000,

    initial_amplitude
    * np.sin(
        2
        * np.pi
        * initial_frequency
        * time_s
    )

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


amplitude_axis = fig.add_axes(
    [
        0.18,
        0.15,
        0.62,
        0.035
    ]
)


frequency_axis = fig.add_axes(
    [
        0.18,
        0.09,
        0.62,
        0.035
    ]
)


reset_button_axis = fig.add_axes(
    [
        0.82,
        0.09,
        0.10,
        0.095
    ]
)


reset_amplitude_slider = Slider(

    amplitude_axis,

    "Amplitude [V]",

    1,

    10,

    valinit=initial_amplitude

)


reset_frequency_slider = Slider(

    frequency_axis,

    "Frequency [Hz]",

    500,

    10_000,

    valinit=initial_frequency

)


reset_button = Button(

    reset_button_axis,

    "Reset"

)


def update_reset_example(
    value
):

    amplitude = (
        reset_amplitude_slider.val
    )


    frequency = (
        reset_frequency_slider.val
    )


    updated_signal = (

        amplitude

        * np.sin(
            2
            * np.pi
            * frequency
            * time_s
        )

    )


    reset_line.set_ydata(
        updated_signal
    )


    ax.set_ylim(

        -1.15
        * amplitude,

        1.15
        * amplitude

    )


    fig.canvas.draw_idle()


def reset_controls(
    event
):

    reset_amplitude_slider.reset()

    reset_frequency_slider.reset()


reset_amplitude_slider.on_changed(
    update_reset_example
)


reset_frequency_slider.on_changed(
    update_reset_example
)


reset_button.on_clicked(
    reset_controls
)


plt.show()


# ============================================================
# 33. SAVE CURRENT VIEW BUTTON
# ============================================================

"""
Interactive exploration can lead to an important view.

A button can save the CURRENT figure state.

However:

For publication reproducibility,

also record the numerical parameters that created that
state.
"""


fig, ax = plt.subplots(
    figsize=(8, 5.3)
)


fig.subplots_adjust(
    bottom=0.27
)


save_line, = ax.plot(

    time_s
    * 1000,

    initial_amplitude
    * np.sin(
        2
        * np.pi
        * initial_frequency
        * time_s
    )

)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


save_slider_axis = fig.add_axes(
    [
        0.18,
        0.10,
        0.58,
        0.04
    ]
)


save_button_axis = fig.add_axes(
    [
        0.80,
        0.08,
        0.13,
        0.08
    ]
)


save_frequency_slider = Slider(

    save_slider_axis,

    "Frequency [Hz]",

    500,

    10_000,

    valinit=initial_frequency

)


save_button = Button(

    save_button_axis,

    "Save View"

)


def update_save_example(
    value
):

    frequency = (
        save_frequency_slider.val
    )


    save_line.set_ydata(

        initial_amplitude

        * np.sin(
            2
            * np.pi
            * frequency
            * time_s
        )

    )


    ax.set_title(

        f"Frequency = "
        f"{frequency:.0f} Hz"

    )


    fig.canvas.draw_idle()


def save_current_view(
    event
):

    frequency = (
        save_frequency_slider.val
    )


    output_file = (

        output_figure_folder

        / (
            "interactive_snapshot_"
            f"{frequency:.0f}_Hz.png"
        )

    )


    fig.savefig(

        output_file,

        dpi=300,

        bbox_inches="tight"

    )


    print(
        "\nSaved current interactive view:"
    )


    print(
        output_file
    )


save_frequency_slider.on_changed(
    update_save_example
)


save_button.on_clicked(
    save_current_view
)


plt.show()


# ============================================================
# 34. RADIO BUTTONS
# ============================================================

"""
Radio buttons allow ONE option to be selected from several
choices.

Example:

Unshielded

Case A

Case B

Case C
"""


fft_cases = {

    "Unshielded":
        unshielded_dbuV,

    "Case A":
        case_a_dbuV,

    "Case B":
        case_b_dbuV,

    "Case C":
        case_c_dbuV

}


fig, ax = plt.subplots(
    figsize=(9, 5.5)
)


fig.subplots_adjust(
    left=0.28
)


radio_line, = ax.plot(

    frequency_hz,

    unshielded_dbuV

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


ax.grid(
    True,
    which="both"
)


radio_axis = fig.add_axes(
    [
        0.03,
        0.35,
        0.18,
        0.28
    ]
)


case_selector = RadioButtons(

    radio_axis,

    list(
        fft_cases.keys()
    ),

    active=0

)


def update_selected_case(
    label
):

    selected_values = (
        fft_cases[
            label
        ]
    )


    radio_line.set_ydata(
        selected_values
    )


    ax.set_title(
        label
    )


    ax.relim()


    ax.autoscale_view(
        scalex=False,
        scaley=True
    )


    fig.canvas.draw_idle()


case_selector.on_clicked(
    update_selected_case
)


plt.show()


# ============================================================
# 35. RADIO BUTTON USE CASE
# ============================================================

"""
RadioButtons are useful when:

Exactly ONE case should be active.


Examples:

Prototype A / B / C

Simulation / Experiment

Voltage / Current / Power

Operating Mode 1 / 2 / 3
"""


# ============================================================
# 36. CHECK BUTTONS
# ============================================================

"""
CheckButtons allow:

Multiple cases

to be enabled or disabled independently.


This is ideal for:

Comparing several spectra

or

Many engineering cases.
"""


fig, ax = plt.subplots(
    figsize=(9.2, 5.5)
)


fig.subplots_adjust(
    left=0.28
)


case_lines = {}


line_styles = {

    "Unshielded":
        "-",

    "Case A":
        "--",

    "Case B":
        "-.",

    "Case C":
        ":"

}


for case_name, values in (
    fft_cases.items()
):

    line, = ax.plot(

        frequency_hz,

        values,

        linestyle=line_styles[
            case_name
        ],

        label=case_name

    )


    case_lines[
        case_name
    ] = line


ax.set_xscale(
    "log"
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.grid(
    True,
    which="both"
)


ax.legend()


check_axis = fig.add_axes(
    [
        0.03,
        0.32,
        0.18,
        0.32
    ]
)


case_checkboxes = CheckButtons(

    check_axis,

    labels=list(
        fft_cases.keys()
    ),

    actives=[
        True,
        True,
        True,
        True
    ]

)


def toggle_case_visibility(
    label
):

    selected_line = (
        case_lines[
            label
        ]
    )


    selected_line.set_visible(

        not selected_line.get_visible()

    )


    fig.canvas.draw_idle()


case_checkboxes.on_clicked(
    toggle_case_visibility
)


plt.show()


# ============================================================
# 37. CHECKBOX APPLICATIONS
# ============================================================

"""
Useful for:

Show / hide:

Baseline

Optimized design

Simulation

Experiment

Measurement limit

Prediction

Confidence interval

Individual harmonics


CheckButtons are especially valuable when:

Many overlapping lines make the figure difficult to read.
"""


# ============================================================
# 38. TextBox
# ============================================================

"""
TextBox allows direct text input.

Example:

Enter:

1500000


to inspect:

1.5 MHz
"""


fig, ax = plt.subplots(
    figsize=(8.5, 5.5)
)


fig.subplots_adjust(
    bottom=0.22
)


textbox_line, = ax.plot(

    frequency_hz,

    unshielded_dbuV

)


selected_frequency_marker, = ax.plot(

    [],

    [],

    marker="o",

    linestyle="None"

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


ax.grid(
    True,
    which="both"
)


textbox_axis = fig.add_axes(
    [
        0.25,
        0.07,
        0.45,
        0.06
    ]
)


frequency_textbox = TextBox(

    textbox_axis,

    "Frequency [Hz]",

    initial="1000000"

)


# ============================================================
# 39. TEXTBOX CALLBACK
# ============================================================

def inspect_frequency_from_text(
    text
):

    try:

        requested_frequency = float(
            text
        )


        if requested_frequency <= 0:

            raise ValueError


        nearest_index = np.argmin(

            np.abs(
                frequency_hz
                - requested_frequency
            )

        )


        nearest_frequency = (
            frequency_hz[
                nearest_index
            ]
        )


        nearest_magnitude = (
            unshielded_dbuV[
                nearest_index
            ]
        )


        selected_frequency_marker.set_data(

            [
                nearest_frequency
            ],

            [
                nearest_magnitude
            ]

        )


        ax.set_title(

            f"Nearest Sample: "
            f"{nearest_frequency:.3e} Hz, "
            f"{nearest_magnitude:.2f} dBµV"

        )


        fig.canvas.draw_idle()


    except ValueError:

        ax.set_title(
            "Enter a positive numerical frequency."
        )


        fig.canvas.draw_idle()


frequency_textbox.on_submit(
    inspect_frequency_from_text
)


plt.show()


# ============================================================
# 40. TEXT INPUT WARNING
# ============================================================

"""
Always validate user input.

Do not assume:

Textbox contents

are:

Numerical

Positive

Inside expected range

Physically meaningful
"""


# ============================================================
# 41. CURSOR
# ============================================================

"""
A cursor can provide crosshair guidance while moving the
mouse across a plot.

This is useful for visual inspection.

It does NOT automatically calculate an exact nearest data
sample.
"""


fig, ax = plt.subplots(
    figsize=(8.5, 5)
)


ax.plot(

    frequency_hz,

    unshielded_dbuV

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


ax.grid(
    True,
    which="both"
)


interactive_cursor = Cursor(

    ax,

    useblit=True,

    linewidth=1

)


plt.show()


# ============================================================
# 42. CURSOR REFERENCE
# ============================================================

"""
Keep:

interactive_cursor


as an object reference while the figure is open.

Otherwise the widget may stop responding.
"""


# ============================================================
# 43. SpanSelector
# ============================================================

"""
SpanSelector lets the user drag across an X-axis region.

Engineering applications:

Select time interval

Select frequency band

Select steady-state region

Select resonance band

Select FFT integration region
"""


# ============================================================
# 44. CREATE TIME-DOMAIN MEASUREMENT
# ============================================================

measurement_time_ms = np.linspace(
    0,
    20,
    5000
)


measurement_time_s = (

    measurement_time_ms

    / 1000

)


measurement_voltage = (

    48

    + 0.7
    * np.sin(
        2
        * np.pi
        * 1000
        * measurement_time_s
    )

    + 0.15
    * np.sin(
        2
        * np.pi
        * 5000
        * measurement_time_s
    )

)


# ============================================================
# 45. SPAN SELECTOR + ZOOM PANEL
# ============================================================

fig, axes = plt.subplots(

    2,

    1,

    figsize=(8.5, 6.5)

)


axes[
    0
].plot(

    measurement_time_ms,

    measurement_voltage

)


axes[
    0
].set_xlabel(
    "Time [ms]"
)


axes[
    0
].set_ylabel(
    "Voltage [V]"
)


axes[
    0
].set_title(
    "Drag Across a Time Region"
)


axes[
    0
].grid(
    True
)


zoom_line, = axes[
    1
].plot(

    measurement_time_ms,

    measurement_voltage

)


axes[
    1
].set_xlabel(
    "Time [ms]"
)


axes[
    1
].set_ylabel(
    "Voltage [V]"
)


axes[
    1
].grid(
    True
)


# ============================================================
# 46. SPAN CALLBACK
# ============================================================

def select_time_region(
    x_min,
    x_max
):

    selected_mask = (

        (
            measurement_time_ms
            >= x_min
        )

        &

        (
            measurement_time_ms
            <= x_max
        )

    )


    if not np.any(
        selected_mask
    ):

        return


    selected_time = (
        measurement_time_ms[
            selected_mask
        ]
    )


    selected_voltage = (
        measurement_voltage[
            selected_mask
        ]
    )


    zoom_line.set_data(

        selected_time,

        selected_voltage

    )


    axes[
        1
    ].set_xlim(

        selected_time.min(),

        selected_time.max()

    )


    minimum = (
        selected_voltage.min()
    )


    maximum = (
        selected_voltage.max()
    )


    padding = max(

        0.10
        * (
            maximum
            - minimum
        ),

        0.1

    )


    axes[
        1
    ].set_ylim(

        minimum
        - padding,

        maximum
        + padding

    )


    # --------------------------------------------------------
    # Calculate RMS
    # --------------------------------------------------------

    rms_voltage = np.sqrt(

        np.mean(
            selected_voltage ** 2
        )

    )


    axes[
        1
    ].set_title(

        f"Selected Region: "
        f"{x_min:.2f} to "
        f"{x_max:.2f} ms | "
        f"RMS = {rms_voltage:.3f} V"

    )


    fig.canvas.draw_idle()


# ============================================================
# 47. CREATE SpanSelector
# ============================================================

time_span_selector = SpanSelector(

    axes[
        0
    ],

    select_time_region,

    "horizontal",

    useblit=True,

    interactive=True

)


plt.tight_layout()

plt.show()


# ============================================================
# 48. RMS WARNING
# ============================================================

"""
The example calculates:

sqrt(
    mean(
        voltage ** 2
    )
)


This is the RMS of the COMPLETE voltage waveform in the
selected region.

If the engineering question is:

AC ripple RMS


around a DC operating value,

the mean/DC component may first need to be removed:

ripple = signal - mean(signal)

then calculate:

RMS(ripple)


The definition must match the research question.
"""


# ============================================================
# 49. INTERACTIVE FREQUENCY-BAND ANALYSIS
# ============================================================

fig, axes = plt.subplots(

    2,

    1,

    figsize=(8.5, 6.5)

)


axes[
    0
].plot(

    frequency_hz,

    unshielded_dbuV

)


axes[
    0
].set_xscale(
    "log"
)


axes[
    0
].set_xlabel(
    "Frequency [Hz]"
)


axes[
    0
].set_ylabel(
    "Magnitude [dBµV]"
)


axes[
    0
].set_title(
    "Drag Across a Frequency Band"
)


axes[
    0
].grid(
    True,
    which="both"
)


selected_band_line, = axes[
    1
].plot(

    frequency_hz,

    unshielded_dbuV

)


axes[
    1
].set_xscale(
    "log"
)


axes[
    1
].set_xlabel(
    "Frequency [Hz]"
)


axes[
    1
].set_ylabel(
    "Magnitude [dBµV]"
)


axes[
    1
].grid(
    True,
    which="both"
)


# ============================================================
# 50. FREQUENCY SPAN CALLBACK
# ============================================================

def select_frequency_band(
    frequency_minimum,
    frequency_maximum
):

    if frequency_minimum <= 0:

        return


    band_mask = (

        (
            frequency_hz
            >= frequency_minimum
        )

        &

        (
            frequency_hz
            <= frequency_maximum
        )

    )


    if not np.any(
        band_mask
    ):

        return


    selected_frequency = (
        frequency_hz[
            band_mask
        ]
    )


    selected_magnitude = (
        unshielded_dbuV[
            band_mask
        ]
    )


    selected_band_line.set_data(

        selected_frequency,

        selected_magnitude

    )


    axes[
        1
    ].set_xlim(

        selected_frequency.min(),

        selected_frequency.max()

    )


    minimum = (
        selected_magnitude.min()
    )


    maximum = (
        selected_magnitude.max()
    )


    padding = max(

        0.10
        * (
            maximum
            - minimum
        ),

        1.0

    )


    axes[
        1
    ].set_ylim(

        minimum
        - padding,

        maximum
        + padding

    )


    peak_index = np.argmax(
        selected_magnitude
    )


    peak_frequency = (
        selected_frequency[
            peak_index
        ]
    )


    peak_magnitude = (
        selected_magnitude[
            peak_index
        ]
    )


    axes[
        1
    ].set_title(

        "Selected Band | "
        f"Max Sample = "
        f"{peak_magnitude:.2f} dBµV "
        f"at {peak_frequency:.3e} Hz"

    )


    fig.canvas.draw_idle()


frequency_span_selector = SpanSelector(

    axes[
        0
    ],

    select_frequency_band,

    "horizontal",

    useblit=True,

    interactive=True

)


plt.tight_layout()

plt.show()


# ============================================================
# 51. PEAK TERMINOLOGY
# ============================================================

"""
Using:

np.argmax()


identifies:

Maximum sampled value


inside the selected region.


It is not formal signal-processing peak detection using:

Prominence

Width

Distance

Threshold


Formal peak detection will be covered in the
Signal Processing section.
"""


# ============================================================
# 52. MOUSE CLICK EVENTS
# ============================================================

"""
Matplotlib figures also expose lower-level events.

Example:

fig.canvas.mpl_connect(
    "button_press_event",
    callback
)


This allows custom interaction when the mouse is clicked.
"""


fig, ax = plt.subplots(
    figsize=(8.5, 5)
)


ax.plot(

    frequency_hz,

    unshielded_dbuV

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


ax.set_title(
    "Click Near a Spectrum Point"
)


ax.grid(
    True,
    which="both"
)


click_marker, = ax.plot(

    [],

    [],

    marker="o",

    linestyle="None"

)


click_annotation = ax.annotate(

    "",

    xy=(
        frequency_hz[
            0
        ],

        unshielded_dbuV[
            0
        ]
    ),

    xytext=(
        15,
        15
    ),

    textcoords="offset points",

    arrowprops={
        "arrowstyle":
            "->"
    }

)


click_annotation.set_visible(
    False
)


# ============================================================
# 53. CLICK CALLBACK
# ============================================================

def inspect_clicked_point(
    event
):

    if event.inaxes != ax:

        return


    if event.xdata is None:

        return


    if event.xdata <= 0:

        return


    # On a log axis, compare positions in log frequency.

    nearest_index = np.argmin(

        np.abs(

            np.log10(
                frequency_hz
            )

            - np.log10(
                event.xdata
            )

        )

    )


    nearest_frequency = (
        frequency_hz[
            nearest_index
        ]
    )


    nearest_magnitude = (
        unshielded_dbuV[
            nearest_index
        ]
    )


    click_marker.set_data(

        [
            nearest_frequency
        ],

        [
            nearest_magnitude
        ]

    )


    click_annotation.xy = (

        nearest_frequency,

        nearest_magnitude

    )


    click_annotation.set_text(

        f"{nearest_frequency:.3e} Hz\n"
        f"{nearest_magnitude:.2f} dBµV"

    )


    click_annotation.set_visible(
        True
    )


    fig.canvas.draw_idle()


click_connection_id = (
    fig.canvas.mpl_connect(

        "button_press_event",

        inspect_clicked_point

    )
)


plt.show()


# ============================================================
# 54. EVENT CONNECTION ID
# ============================================================

"""
mpl_connect()

returns a connection ID.

It can later be disconnected using:

fig.canvas.mpl_disconnect(
    connection_id
)


This is useful in larger interactive applications.
"""


# ============================================================
# 55. KEYBOARD EVENTS
# ============================================================

"""
Keyboard interaction can also be connected.

Example:

Press:

r

to reset axis limits.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(

    measurement_time_ms,

    measurement_voltage

)


ax.set_xlabel(
    "Time [ms]"
)

ax.set_ylabel(
    "Voltage [V]"
)


ax.set_title(
    "Zoom Manually, Then Press 'r' to Reset"
)


ax.grid(
    True
)


original_xlim = ax.get_xlim()

original_ylim = ax.get_ylim()


def keyboard_callback(
    event
):

    if event.key == "r":

        ax.set_xlim(
            original_xlim
        )


        ax.set_ylim(
            original_ylim
        )


        fig.canvas.draw_idle()


keyboard_connection = (
    fig.canvas.mpl_connect(

        "key_press_event",

        keyboard_callback

    )
)


plt.show()


# ============================================================
# 56. INTERACTIVE FFT CASE + FREQUENCY WINDOW
# ============================================================

"""
Now combine:

RadioButtons
        +
RangeSlider


so the user can:

Select one design case

and

Choose a frequency window.
"""


fig, ax = plt.subplots(
    figsize=(9.5, 5.8)
)


fig.subplots_adjust(
    left=0.27,
    bottom=0.23
)


combined_fft_line, = ax.plot(

    frequency_hz,

    unshielded_dbuV

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


ax.grid(
    True,
    which="both"
)


# ------------------------------------------------------------
# Radio buttons
# ------------------------------------------------------------

combined_radio_axis = fig.add_axes(
    [
        0.03,
        0.38,
        0.17,
        0.25
    ]
)


combined_case_selector = RadioButtons(

    combined_radio_axis,

    list(
        fft_cases.keys()
    ),

    active=0

)


# ------------------------------------------------------------
# Frequency slider
# ------------------------------------------------------------

combined_range_axis = fig.add_axes(
    [
        0.28,
        0.07,
        0.60,
        0.04
    ]
)


combined_frequency_slider = RangeSlider(

    combined_range_axis,

    "log10(f)",

    valmin=log_frequency.min(),

    valmax=log_frequency.max(),

    valinit=(
        log_frequency.min(),
        log_frequency.max()
    )

)


# Track currently selected case

interactive_state = {

    "case":
        "Unshielded"

}


# ============================================================
# 57. COMBINED UPDATE FUNCTION
# ============================================================

def update_fft_dashboard(
    value=None
):

    selected_case = (
        interactive_state[
            "case"
        ]
    )


    selected_values = (
        fft_cases[
            selected_case
        ]
    )


    combined_fft_line.set_ydata(
        selected_values
    )


    log_minimum, log_maximum = (
        combined_frequency_slider.val
    )


    frequency_minimum = (
        10 ** log_minimum
    )


    frequency_maximum = (
        10 ** log_maximum
    )


    combined_mask = (

        (
            frequency_hz
            >= frequency_minimum
        )

        &

        (
            frequency_hz
            <= frequency_maximum
        )

    )


    ax.set_xlim(

        frequency_minimum,

        frequency_maximum

    )


    if np.any(
        combined_mask
    ):

        visible_values = (
            selected_values[
                combined_mask
            ]
        )


        minimum = visible_values.min()

        maximum = visible_values.max()


        padding = max(

            0.08
            * (
                maximum
                - minimum
            ),

            1.0

        )


        ax.set_ylim(

            minimum
            - padding,

            maximum
            + padding

        )


        maximum_index = np.argmax(
            visible_values
        )


        visible_frequency = (
            frequency_hz[
                combined_mask
            ]
        )


        maximum_frequency = (
            visible_frequency[
                maximum_index
            ]
        )


        maximum_value = (
            visible_values[
                maximum_index
            ]
        )


        ax.set_title(

            f"{selected_case} | "
            f"Max Sample = "
            f"{maximum_value:.2f} dBµV "
            f"at {maximum_frequency:.3e} Hz"

        )


    fig.canvas.draw_idle()


def change_fft_case(
    label
):

    interactive_state[
        "case"
    ] = label


    update_fft_dashboard()


combined_case_selector.on_clicked(
    change_fft_case
)


combined_frequency_slider.on_changed(
    update_fft_dashboard
)


plt.show()


# ============================================================
# 58. INTERACTIVE DESIGN-COMPARISON DASHBOARD
# ============================================================

"""
We can also combine:

CheckButtons
        +
RangeSlider


to compare multiple spectra only inside a selected band.
"""


fig, ax = plt.subplots(
    figsize=(9.5, 5.8)
)


fig.subplots_adjust(
    left=0.27,
    bottom=0.23
)


dashboard_lines = {}


for case_name, values in (
    fft_cases.items()
):

    dashboard_line, = ax.plot(

        frequency_hz,

        values,

        linestyle=line_styles[
            case_name
        ],

        label=case_name

    )


    dashboard_lines[
        case_name
    ] = dashboard_line


ax.set_xscale(
    "log"
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.grid(
    True,
    which="both"
)


ax.legend()


dashboard_checkbox_axis = fig.add_axes(
    [
        0.03,
        0.35,
        0.17,
        0.28
    ]
)


dashboard_checkboxes = CheckButtons(

    dashboard_checkbox_axis,

    list(
        fft_cases.keys()
    ),

    actives=[
        True,
        True,
        True,
        True
    ]

)


dashboard_range_axis = fig.add_axes(
    [
        0.28,
        0.07,
        0.60,
        0.04
    ]
)


dashboard_range_slider = RangeSlider(

    dashboard_range_axis,

    "log10(f)",

    valmin=log_frequency.min(),

    valmax=log_frequency.max(),

    valinit=(
        log_frequency.min(),
        log_frequency.max()
    )

)


# ============================================================
# 59. DASHBOARD UPDATE FUNCTIONS
# ============================================================

def toggle_dashboard_case(
    label
):

    line = dashboard_lines[
        label
    ]


    line.set_visible(

        not line.get_visible()

    )


    fig.canvas.draw_idle()


def update_dashboard_range(
    values
):

    log_minimum, log_maximum = (
        dashboard_range_slider.val
    )


    frequency_minimum = (
        10 ** log_minimum
    )


    frequency_maximum = (
        10 ** log_maximum
    )


    ax.set_xlim(

        frequency_minimum,

        frequency_maximum

    )


    visible_values = []


    mask = (

        (
            frequency_hz
            >= frequency_minimum
        )

        &

        (
            frequency_hz
            <= frequency_maximum
        )

    )


    for case_name, line in (
        dashboard_lines.items()
    ):

        if line.get_visible():

            values = fft_cases[
                case_name
            ]


            visible_values.extend(
                values[
                    mask
                ]
            )


    if visible_values:

        visible_values = np.asarray(
            visible_values
        )


        minimum = (
            visible_values.min()
        )


        maximum = (
            visible_values.max()
        )


        padding = max(

            0.08
            * (
                maximum
                - minimum
            ),

            1.0

        )


        ax.set_ylim(

            minimum
            - padding,

            maximum
            + padding

        )


    fig.canvas.draw_idle()


dashboard_checkboxes.on_clicked(
    toggle_dashboard_case
)


dashboard_range_slider.on_changed(
    update_dashboard_range
)


plt.show()


# ============================================================
# 60. INTERACTIVE REDUCTION ANALYSIS
# ============================================================

"""
For EMI comparison:

Reduction [dB]
=
Unshielded [dBµV]
-
Selected Case [dBµV]


Positive:

Selected case has lower dBµV at that sampled frequency.


Negative:

Selected case is higher.
"""


reduction_cases = {

    "Case A":
        (
            unshielded_dbuV
            - case_a_dbuV
        ),

    "Case B":
        (
            unshielded_dbuV
            - case_b_dbuV
        ),

    "Case C":
        (
            unshielded_dbuV
            - case_c_dbuV
        )

}


fig, ax = plt.subplots(
    figsize=(9, 5.3)
)


fig.subplots_adjust(
    left=0.28
)


initial_reduction_case = "Case A"


reduction_line, = ax.plot(

    frequency_hz,

    reduction_cases[
        initial_reduction_case
    ]

)


ax.axhline(
    0,
    linestyle="--"
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


ax.grid(
    True,
    which="both"
)


reduction_radio_axis = fig.add_axes(
    [
        0.04,
        0.38,
        0.16,
        0.22
    ]
)


reduction_selector = RadioButtons(

    reduction_radio_axis,

    list(
        reduction_cases.keys()
    )

)


def update_reduction_case(
    label
):

    values = (
        reduction_cases[
            label
        ]
    )


    reduction_line.set_ydata(
        values
    )


    ax.relim()


    ax.autoscale_view(
        scalex=False,
        scaley=True
    )


    maximum_index = np.argmax(
        values
    )


    ax.set_title(

        f"{label}: "
        f"Max Sampled Reduction = "
        f"{values[maximum_index]:.2f} dB"

    )


    fig.canvas.draw_idle()


reduction_selector.on_clicked(
    update_reduction_case
)


plt.show()


# ============================================================
# 61. IMPORTANT dB NOTE
# ============================================================

"""
For two dBµV values:

100 dBµV

and

90 dBµV


difference:

=

10 dB


Do NOT calculate ordinary percentage reduction directly
from the dB values.

If a linear-amplitude percentage is needed:

Convert to the appropriate linear domain first.
"""


# ============================================================
# 62. TEXTBOX FOR LOAD SELECTION
# ============================================================

"""
Slider:

Excellent for exploration.


TextBox:

Useful when an exact parameter value should be entered.
"""


fig, ax = plt.subplots(
    figsize=(8.5, 5.3)
)


fig.subplots_adjust(
    bottom=0.23
)


initial_index = np.argmin(

    np.abs(
        load_percent
        - 60
    )

)


load_text_line, = ax.plot(

    switching_frequency_khz,

    efficiency_map[
        initial_index,
        :
    ]

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


load_text_axis = fig.add_axes(
    [
        0.30,
        0.07,
        0.40,
        0.06
    ]
)


load_textbox = TextBox(

    load_text_axis,

    "Load [%]",

    initial="60"

)


def update_load_from_text(
    text
):

    try:

        requested_load = float(
            text
        )


        if (
            requested_load
            < load_percent.min()
            or
            requested_load
            > load_percent.max()
        ):

            raise ValueError


        index = np.argmin(

            np.abs(
                load_percent
                - requested_load
            )

        )


        actual_load = (
            load_percent[
                index
            ]
        )


        load_text_line.set_ydata(

            efficiency_map[
                index,
                :
            ]

        )


        ax.set_title(

            f"Nearest Available Load = "
            f"{actual_load:.1f}%"

        )


        ax.relim()


        ax.autoscale_view(
            scalex=False,
            scaley=True
        )


        fig.canvas.draw_idle()


    except ValueError:

        ax.set_title(

            "Enter a load inside "
            f"{load_percent.min():.0f}-"
            f"{load_percent.max():.0f}%"

        )


        fig.canvas.draw_idle()


load_textbox.on_submit(
    update_load_from_text
)


plt.show()


# ============================================================
# 63. INTERACTIVE OPERATING POINT
# ============================================================

"""
Now use TWO sliders:

Switching Frequency

Load


and display:

Current operating-point efficiency.
"""


fig, ax = plt.subplots(
    figsize=(8, 5.5)
)


fig.subplots_adjust(
    bottom=0.30
)


map_plot = ax.pcolormesh(

    frequency_grid,

    load_grid,

    efficiency_map,

    shading="auto",

    cmap="viridis"

)


colorbar = fig.colorbar(

    map_plot,

    ax=ax

)


colorbar.set_label(
    "Efficiency [%]"
)


initial_frequency = 135

initial_load = 75


operating_marker, = ax.plot(

    [
        initial_frequency
    ],

    [
        initial_load
    ],

    marker="o",

    linestyle="None"

)


ax.set_xlabel(
    "Switching Frequency [kHz]"
)

ax.set_ylabel(
    "Load [%]"
)


frequency_operating_axis = fig.add_axes(
    [
        0.20,
        0.14,
        0.60,
        0.035
    ]
)


load_operating_axis = fig.add_axes(
    [
        0.20,
        0.07,
        0.60,
        0.035
    ]
)


operating_frequency_slider = Slider(

    frequency_operating_axis,

    "Frequency [kHz]",

    valmin=switching_frequency_khz.min(),

    valmax=switching_frequency_khz.max(),

    valinit=initial_frequency

)


operating_load_slider = Slider(

    load_operating_axis,

    "Load [%]",

    valmin=load_percent.min(),

    valmax=load_percent.max(),

    valinit=initial_load

)


# ============================================================
# 64. CALCULATE RESPONSE AT ARBITRARY POINT
# ============================================================

def calculate_efficiency(
    frequency_khz,
    load_value
):
    """
    Same synthetic model used to generate the parameter map.
    """

    return (

        96.2

        - 0.000050
        * (
            frequency_khz
            - 135
        ) ** 2

        - 0.00035
        * (
            load_value
            - 75
        ) ** 2

    )


# ============================================================
# 65. OPERATING-POINT CALLBACK
# ============================================================

def update_operating_point(
    value
):

    frequency = (
        operating_frequency_slider.val
    )


    load_value = (
        operating_load_slider.val
    )


    efficiency = calculate_efficiency(

        frequency,

        load_value

    )


    operating_marker.set_data(

        [
            frequency
        ],

        [
            load_value
        ]

    )


    ax.set_title(

        f"Frequency = {frequency:.1f} kHz | "
        f"Load = {load_value:.1f}% | "
        f"Efficiency = {efficiency:.3f}%"

    )


    fig.canvas.draw_idle()


operating_frequency_slider.on_changed(
    update_operating_point
)


operating_load_slider.on_changed(
    update_operating_point
)


update_operating_point(
    None
)


plt.show()


# ============================================================
# 66. INTERACTIVE MODEL VS SAMPLED DATA
# ============================================================

"""
Important distinction:

If the slider can select:

137.3 kHz


but simulations were performed only at:

135 kHz

140 kHz


then an exact response at:

137.3 kHz


must come from:

Analytical model

Interpolation

Surrogate model

or another predictive method.


Do not imply that every interactive point was directly
measured or simulated.
"""


# ============================================================
# 67. REUSABLE SLIDER-CONTROLLED CURVE FUNCTION
# ============================================================

def create_parameter_slider_plot(
    x,
    model_function,
    parameter_name,
    parameter_unit,
    parameter_minimum,
    parameter_maximum,
    parameter_initial,
    x_label,
    y_label,
    parameter_step=None
):
    """
    Create a reusable slider-controlled 2D curve.

    Parameters
    ----------
    x : array-like
        X values.

    model_function : callable
        Function:
        y = model_function(x, parameter)

    parameter_name : str

    parameter_unit : str

    parameter_minimum : float

    parameter_maximum : float

    parameter_initial : float

    x_label : str

    y_label : str

    parameter_step : float or array-like, optional

    Returns
    -------
    fig, ax, slider
    """

    x = np.asarray(
        x,
        dtype=float
    )


    initial_y = model_function(

        x,

        parameter_initial

    )


    initial_y = np.asarray(
        initial_y,
        dtype=float
    )


    if initial_y.shape != x.shape:

        raise ValueError(
            "model_function output must "
            "match X shape."
        )


    fig, ax = plt.subplots(
        figsize=(8, 5)
    )


    fig.subplots_adjust(
        bottom=0.23
    )


    line, = ax.plot(

        x,

        initial_y

    )


    ax.set_xlabel(
        x_label
    )


    ax.set_ylabel(
        y_label
    )


    ax.grid(
        True
    )


    slider_axis = fig.add_axes(
        [
            0.18,
            0.08,
            0.65,
            0.04
        ]
    )


    slider_label = (

        f"{parameter_name} "
        f"[{parameter_unit}]"

        if parameter_unit

        else parameter_name

    )


    slider = Slider(

        slider_axis,

        slider_label,

        valmin=parameter_minimum,

        valmax=parameter_maximum,

        valinit=parameter_initial,

        valstep=parameter_step

    )


    def update(
        value
    ):

        parameter = (
            slider.val
        )


        updated_y = np.asarray(

            model_function(
                x,
                parameter
            ),

            dtype=float

        )


        line.set_ydata(
            updated_y
        )


        ax.relim()


        ax.autoscale_view(
            scalex=False,
            scaley=True
        )


        ax.set_title(

            f"{parameter_name} = "
            f"{parameter:.3g} "
            f"{parameter_unit}"

        )


        fig.canvas.draw_idle()


    slider.on_changed(
        update
    )


    return (
        fig,
        ax,
        slider
    )


# ============================================================
# 68. USE REUSABLE SLIDER FUNCTION
# ============================================================

def ripple_model(
    time_values,
    amplitude
):

    return (

        48

        + amplitude
        * np.sin(
            2
            * np.pi
            * 1000
            * time_values
        )

    )


ripple_time_s = np.linspace(
    0,
    0.005,
    1500
)


fig, ax, reusable_slider = (
    create_parameter_slider_plot(

        x=ripple_time_s,

        model_function=ripple_model,

        parameter_name="Ripple Amplitude",

        parameter_unit="V",

        parameter_minimum=0.1,

        parameter_maximum=2.0,

        parameter_initial=0.5,

        x_label="Time [s]",

        y_label="Voltage [V]"

    )
)


plt.show()


# ============================================================
# 69. REUSABLE CASE SELECTOR
# ============================================================

def create_radio_case_plot(
    x,
    cases,
    x_label,
    y_label,
    x_scale="linear",
    title=None
):
    """
    Create an interactive single-case selector.

    Parameters
    ----------
    x : array-like

    cases : dict
        display label -> Y array

    x_label : str

    y_label : str

    x_scale : str
        "linear" or "log"

    title : str, optional

    Returns
    -------
    fig, ax, radio_buttons
    """

    x = np.asarray(
        x,
        dtype=float
    )


    if not cases:

        raise ValueError(
            "At least one case is required."
        )


    case_names = list(
        cases.keys()
    )


    first_case = case_names[
        0
    ]


    first_values = np.asarray(

        cases[
            first_case
        ],

        dtype=float

    )


    if first_values.shape != x.shape:

        raise ValueError(
            "Case data must match X shape."
        )


    fig, ax = plt.subplots(
        figsize=(9, 5)
    )


    fig.subplots_adjust(
        left=0.28
    )


    line, = ax.plot(

        x,

        first_values

    )


    ax.set_xscale(
        x_scale
    )


    ax.set_xlabel(
        x_label
    )


    ax.set_ylabel(
        y_label
    )


    ax.grid(
        True,
        which="both"
    )


    if title is not None:

        ax.set_title(
            title
        )


    radio_axis = fig.add_axes(
        [
            0.03,
            0.35,
            0.18,
            0.30
        ]
    )


    radio_buttons = RadioButtons(

        radio_axis,

        case_names,

        active=0

    )


    def update_case(
        label
    ):

        values = np.asarray(

            cases[
                label
            ],

            dtype=float

        )


        if values.shape != x.shape:

            return


        line.set_ydata(
            values
        )


        ax.relim()


        ax.autoscale_view(
            scalex=False,
            scaley=True
        )


        ax.set_title(
            label
        )


        fig.canvas.draw_idle()


    radio_buttons.on_clicked(
        update_case
    )


    return (
        fig,
        ax,
        radio_buttons
    )


# ============================================================
# 70. USE REUSABLE CASE SELECTOR
# ============================================================

fig, ax, reusable_radio = (
    create_radio_case_plot(

        x=frequency_hz,

        cases=fft_cases,

        x_label="Frequency [Hz]",

        y_label="Magnitude [dBµV]",

        x_scale="log",

        title="Interactive FFT Case Selection"

    )
)


plt.show()


# ============================================================
# 71. INTERACTIVE SNAPSHOT + PARAMETER LOG
# ============================================================

"""
For reproducible research:

Do not save only:

figure.png


Also save:

Parameter settings.
"""


snapshot_parameter_file = (

    output_data_folder
    / "interactive_snapshot_parameters.csv"

)


# ============================================================
# 72. SAVE PARAMETERS FUNCTION
# ============================================================

def save_interactive_parameters(
    parameters,
    output_file
):
    """
    Save current interactive parameters to CSV.

    Parameters
    ----------
    parameters : dict

    output_file : str or Path
    """

    output_file = Path(
        output_file
    )


    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    dataframe = pd.DataFrame(
        [
            parameters
        ]
    )


    dataframe.to_csv(

        output_file,

        index=False

    )


# ============================================================
# 73. EXAMPLE PARAMETER SAVE
# ============================================================

example_parameters = {

    "Switching_Frequency_kHz":
        135,

    "Load_percent":
        75,

    "Selected_Case":
        "Case B",

    "Frequency_Min_Hz":
        100e3,

    "Frequency_Max_Hz":
        10e6

}


save_interactive_parameters(

    example_parameters,

    snapshot_parameter_file

)


print(
    "\n--- Example Interactive Parameters Saved ---"
)


print(
    snapshot_parameter_file
)


# ============================================================
# 74. STATIC SNAPSHOT WORKFLOW
# ============================================================

"""
Interactive Figure
        ↓
Adjust Sliders
        ↓
Choose Case
        ↓
Choose Frequency Window
        ↓
Record Parameter Values
        ↓
Save Parameters
        ↓
Generate Static Figure
        ↓
Save PNG / PDF / SVG


This is much more reproducible than:

Interactively adjust figure
        ↓
Take screenshot
"""


# ============================================================
# 75. SAVE STATIC FFT FIGURE FROM PARAMETERS
# ============================================================

selected_case_name = "Case B"

selected_frequency_min = 100e3

selected_frequency_max = 10e6


selected_case_values = (
    fft_cases[
        selected_case_name
    ]
)


selected_mask = (

    (
        frequency_hz
        >= selected_frequency_min
    )

    &

    (
        frequency_hz
        <= selected_frequency_max
    )

)


fig, ax = plt.subplots(
    figsize=(8.5, 5)
)


ax.plot(

    frequency_hz[
        selected_mask
    ],

    selected_case_values[
        selected_mask
    ],

    label=selected_case_name

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


fig.tight_layout()


static_png = (
    output_figure_folder
    / "selected_interactive_result.png"
)


static_pdf = (
    output_figure_folder
    / "selected_interactive_result.pdf"
)


static_svg = (
    output_figure_folder
    / "selected_interactive_result.svg"
)


fig.savefig(

    static_png,

    dpi=300,

    bbox_inches="tight"

)


fig.savefig(

    static_pdf,

    bbox_inches="tight"

)


fig.savefig(

    static_svg,

    bbox_inches="tight"

)


print(
    "\n--- Static Selected Result Saved ---"
)


print(
    static_png
)


print(
    static_pdf
)


print(
    static_svg
)


plt.show()


# ============================================================
# 76. INTERACTIVE PLOT != PUBLICATION FIGURE
# ============================================================

"""
Interactive controls such as:

Sliders

Buttons

CheckBoxes


are primarily for:

Analysis

Exploration

Demonstration


A journal paper usually contains:

Static figures.


Therefore the final figure should still be generated using
explicit numerical settings stored in code.
"""


# ============================================================
# 77. STATIC EXPORT DOES NOT SAVE WIDGET BEHAVIOR
# ============================================================

"""
If an interactive figure is saved as:

PNG

PDF

SVG


the exported file represents a static visual state.

The slider does not remain draggable inside a normal PNG.

The checkbox does not remain clickable inside a normal PDF
figure.

The saved image is not the interactive application.
"""


# ============================================================
# 78. COMMON MISTAKE - WIDGET OBJECT LOST
# ============================================================

"""
Bad:

Slider(
    axis,
    ...
)


without assigning it to a variable.


Better:

frequency_slider = Slider(
    axis,
    ...
)


Keep the widget object alive while the figure is open.
"""


# ============================================================
# 79. COMMON MISTAKE - NO CALLBACK
# ============================================================

"""
Creating:

Slider(...)


does not automatically update the plot.


Connect:

slider.on_changed(
    update_function
)
"""


# ============================================================
# 80. COMMON MISTAKE - FORGETTING draw_idle()
# ============================================================

"""
After changing:

Line data

Axis limits

Text

Markers


request a redraw:

fig.canvas.draw_idle()
"""


# ============================================================
# 81. COMMON MISTAKE - RECALCULATING EVERYTHING
# ============================================================

"""
Weak interactive implementation:

Delete entire figure

Recreate all axes

Replot everything


for every slider movement.


Better:

Update existing artists.


Examples:

line.set_ydata(...)

line.set_data(...)

marker.set_data(...)

text.set_text(...)

ax.set_xlim(...)
"""


# ============================================================
# 82. COMMON MISTAKE - SLOW CALLBACK
# ============================================================

"""
Slider callbacks can execute many times while the user
moves the slider.

Avoid unnecessarily expensive operations inside every
callback.

Examples of potentially expensive work:

Large file reads

Large ML retraining

Heavy simulations

Repeated FFT calculation on huge datasets


Possible strategy:

Precompute results

Cache results

Reduce interactive resolution

Calculate expensive model only after explicit button click
"""


# ============================================================
# 83. COMMON MISTAKE - FILE READING INSIDE SLIDER
# ============================================================

"""
Bad:

Every slider movement:

pd.read_csv(
    huge_file.csv
)


Better:

Load dataset once

before creating the interactive figure.


Then the callback operates on:

Arrays already in memory.
"""


# ============================================================
# 84. COMMON MISTAKE - SLIDER OUTSIDE VALID PHYSICS
# ============================================================

"""
A slider may technically allow:

Switching frequency = 1 MHz


but the converter model may only be validated between:

50 kHz

and

250 kHz.


Interactive controls should respect:

Valid engineering ranges.
"""


# ============================================================
# 85. COMMON MISTAKE - INTERPOLATION NOT DISCLOSED
# ============================================================

"""
Suppose measured loads are:

20%

40%

60%

80%

100%


but the slider selects:

53%.


If the displayed value was interpolated:

State that.


Do not imply:

53%

was directly measured.
"""


# ============================================================
# 86. COMMON MISTAKE - TOO MANY CONTROLS
# ============================================================

"""
A figure with:

10 sliders

8 checkboxes

6 buttons

3 text boxes


may become harder to use than the original dataset.


Interactive interfaces should remain focused on the
engineering question.
"""


# ============================================================
# 87. COMMON MISTAKE - CONTROLS COVER DATA
# ============================================================

"""
Reserve space using:

fig.subplots_adjust(...)


or a suitable layout.


Do not place controls directly over:

Important curves

Labels

Legends

Colorbars
"""


# ============================================================
# 88. COMMON MISTAKE - NO INPUT VALIDATION
# ============================================================

"""
Text input can contain:

Letters

Negative values

Values outside range

Empty strings


Validate before using the value in engineering
calculations.
"""


# ============================================================
# 89. COMMON MISTAKE - WRONG LOG SLIDER
# ============================================================

"""
A raw-frequency slider from:

10 kHz

to

30 MHz


may provide poor resolution at low frequencies.


For broad frequency ranges:

Consider controlling:

log10(frequency)


and converting back:

frequency = 10 ** slider_value
"""


# ============================================================
# 90. COMMON MISTAKE - LOG AXIS WITH NONPOSITIVE DATA
# ============================================================

"""
For:

ax.set_xscale(
    "log"
)


require:

X > 0


Validate frequencies first.
"""


# ============================================================
# 91. COMMON MISTAKE - POINT CLICK CALLED EXACT MEASUREMENT
# ============================================================

"""
A mouse click may occur BETWEEN sampled data points.

If the program selects the nearest sample:

Report:

Nearest sample


not:

Exact measurement at clicked X.
"""


# ============================================================
# 92. COMMON MISTAKE - VISUAL SELECTION REPLACES NUMERICAL METHOD
# ============================================================

"""
Dragging a frequency region can help explore data.

But final research analysis may require an explicitly
defined numerical band such as:

150 kHz to 30 MHz


Store those limits in the final analysis code.
"""


# ============================================================
# 93. COMMON MISTAKE - SELECTED WINDOW CHERRY-PICKED
# ============================================================

"""
Interactive tools make it easy to find a region where one
design looks especially good.

Do not use that convenience to hide regions where:

Performance becomes worse.


Final comparisons should use:

Justified

Consistent

Documented

analysis ranges.
"""


# ============================================================
# 94. COMMON MISTAKE - SCREENSHOT
# ============================================================

"""
Do not finish an interactive analysis by:

Taking a screenshot.


Better:

Record parameter values

Generate the final static plot from code

Save with:

fig.savefig(...)
"""


# ============================================================
# 95. COMMON MISTAKE - ONLY INTERACTIVE RESULT SAVED
# ============================================================

"""
A future researcher should be able to reproduce the same
figure without manually moving sliders.

Therefore save:

Input data

Parameter values

Processing script

Static figure
"""


# ============================================================
# 96. SLIDER WORKFLOW
# ============================================================

"""
Engineering Model
      ↓
Choose Parameter
      ↓
Define Valid Range
      ↓
Create Slider
      ↓
Create Callback
      ↓
Read slider.val
      ↓
Update Model
      ↓
Update Line
      ↓
draw_idle()
"""


# ============================================================
# 97. FFT INTERACTIVE WORKFLOW
# ============================================================

"""
FFT Dataset
      ↓
Validate Frequency > 0
      ↓
Plot Full Spectrum
      ↓
Select Case
      ↓
Select Frequency Band
      ↓
Calculate Local Maximum
      ↓
Compare Cases
      ↓
Record Selected Range
      ↓
Generate Final Static Figure
"""


# ============================================================
# 98. PARAMETER-SWEEP WORKFLOW
# ============================================================

"""
Parameter Map
      ↓
Slider Selects Load
      ↓
Extract Frequency Cross-Section
      ↓
Observe Response
      ↓
Select Candidate Region
      ↓
Refine Simulation / Experiment
      ↓
Validate Candidate
"""


# ============================================================
# 99. TIME-WINDOW WORKFLOW
# ============================================================

"""
Time-Domain Signal
      ↓
SpanSelector
      ↓
Select Region
      ↓
Calculate:
Mean
RMS
Peak
Peak-to-Peak
      ↓
Inspect Detail
      ↓
Define Final Numerical Window
      ↓
Repeat Analysis Reproducibly
"""


# ============================================================
# 100. CASE-SELECTION WORKFLOW
# ============================================================

"""
Many Cases
      ↓
RadioButtons
or
CheckButtons
      ↓
Show Selected Cases
      ↓
Inspect Differences
      ↓
Identify Important Comparisons
      ↓
Generate Static Comparison Figure
"""


# ============================================================
# 101. WIDGET DECISION GUIDE
# ============================================================

"""
Need one continuous numerical parameter?
        ↓
Slider


Need numerical lower + upper limits?
        ↓
RangeSlider


Need one option from several?
        ↓
RadioButtons


Need several independent ON/OFF choices?
        ↓
CheckButtons


Need an action?
        ↓
Button


Need exact typed input?
        ↓
TextBox


Need mouse crosshair?
        ↓
Cursor


Need drag-selected X range?
        ↓
SpanSelector


Need custom mouse behavior?
        ↓
mpl_connect()


Need final journal figure?
        ↓
Static Matplotlib Figure
"""


# ============================================================
# 102. INTERACTIVE RESEARCH WORKFLOW
# ============================================================

"""
Raw Engineering Data
        ↓
Load Once
        ↓
Validate
        ↓
Interactive Exploration
        ↓
Slider / Selector / Buttons
        ↓
Investigate:
Regions
Cases
Parameters
Peaks
Ranges
        ↓
Record Important Numerical Settings
        ↓
Run Formal Analysis
        ↓
Generate Reproducible Static Figure
        ↓
Save:
PNG
PDF
SVG
        ↓
Paper / Thesis / Report
"""


# ============================================================
# 103. PUBLICATION CHECKLIST
# ============================================================

"""
After using an interactive figure for research, check:


DATA
------------------------------------------------------------

Was the raw dataset preserved?


PARAMETER RANGE
------------------------------------------------------------

Did controls stay inside valid engineering limits?


INTERPOLATION
------------------------------------------------------------

Were unsampled points interpolated or predicted?

Was that distinction clear?


ANALYSIS RANGE
------------------------------------------------------------

Was the final selected time / frequency range documented?


CASES
------------------------------------------------------------

Were all relevant cases considered?


METRICS
------------------------------------------------------------

Were important values calculated numerically rather than
only judged visually?


REPRODUCIBILITY
------------------------------------------------------------

Can the selected result be regenerated without moving
widgets manually?


STATIC FIGURE
------------------------------------------------------------

Was a publication-ready figure created from explicit
parameters?


OUTPUT
------------------------------------------------------------

PNG?

PDF?

SVG?


SCRIPT
------------------------------------------------------------

Does the code preserve:

Selected limits

Case names

Operating point

Processing method?


FINAL QUESTION
------------------------------------------------------------

If another researcher runs the script one year later:

Can they reproduce the same final result?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
INTERACTIVE PLOTTING


1. INTERACTIVE MODE

plt.ion()


Check:

plt.isinteractive()


------------------------------------------------------------


2. BASIC SLIDER

slider = Slider(

    slider_axis,

    "Parameter",

    minimum,

    maximum,

    valinit=initial_value

)


------------------------------------------------------------


3. SLIDER CALLBACK

def update(
    value
):

    parameter = slider.val

    ...

    line.set_ydata(
        new_y
    )

    fig.canvas.draw_idle()


slider.on_changed(
    update
)


------------------------------------------------------------


4. DISCRETE SLIDER

Slider(

    ...,

    valstep=[
        2,
        4,
        6,
        8,
        10
    ]

)


Useful for:

Discrete engineering values.


------------------------------------------------------------


5. RANGE SLIDER

range_slider = RangeSlider(

    axis,

    "Range",

    minimum,

    maximum,

    valinit=(
        lower,
        upper
    )

)


------------------------------------------------------------


6. RANGE VALUE

lower, upper = (
    range_slider.val
)


------------------------------------------------------------


7. BUTTON

button = Button(

    button_axis,

    "Reset"

)


button.on_clicked(
    callback
)


------------------------------------------------------------


8. RESET SLIDER

slider.reset()


------------------------------------------------------------


9. RADIO BUTTONS

radio = RadioButtons(

    axis,

    [
        "Case A",
        "Case B",
        "Case C"
    ]

)


Useful when:

One choice should be active.


------------------------------------------------------------


10. CHECK BUTTONS

checks = CheckButtons(

    axis,

    labels=[
        "Case A",
        "Case B",
        "Case C"
    ],

    actives=[
        True,
        True,
        False
    ]

)


Useful when:

Several cases may be visible simultaneously.


------------------------------------------------------------


11. TEXT INPUT

textbox = TextBox(

    axis,

    "Frequency",

    initial="1000000"

)


textbox.on_submit(
    callback
)


------------------------------------------------------------


12. CURSOR

cursor = Cursor(

    ax,

    useblit=True

)


Useful for:

Visual point inspection.


------------------------------------------------------------


13. SPAN SELECTOR

selector = SpanSelector(

    ax,

    callback,

    "horizontal",

    interactive=True

)


Useful for:

Time windows

Frequency bands


------------------------------------------------------------


14. CUSTOM MOUSE EVENT

connection_id = (

    fig.canvas.mpl_connect(

        "button_press_event",

        callback

    )

)


------------------------------------------------------------


15. KEYBOARD EVENT

fig.canvas.mpl_connect(

    "key_press_event",

    callback

)


------------------------------------------------------------


16. UPDATE EXISTING LINE

line.set_ydata(
    new_values
)


Better than recreating the whole figure unnecessarily.


------------------------------------------------------------


17. UPDATE X AND Y

line.set_data(

    new_x,

    new_y

)


------------------------------------------------------------


18. REQUEST REDRAW

fig.canvas.draw_idle()


------------------------------------------------------------


19. LOGARITHMIC FREQUENCY CONTROL

For broad ranges:

slider_value
=
log10(
    frequency
)


Then:

frequency
=
10 ** slider_value


------------------------------------------------------------


20. INTERACTIVE FFT

Case Selector
        +
Frequency Range
        ↓
Inspect Spectrum
        ↓
Calculate Local Metrics


------------------------------------------------------------


21. PARAMETER MAP

Heatmap
        +
Load Slider
        ↓
Cross-Section Curve


------------------------------------------------------------


22. OPERATING POINT

Frequency Slider
        +
Load Slider
        ↓
Model Response


------------------------------------------------------------


23. IMPORTANT MODEL DISTINCTION

Interactive point may represent:

Measured value

Simulated value

Interpolated value

Analytical value

ML prediction


State which one.


------------------------------------------------------------


24. POINT INSPECTION

Mouse click

may select:

Nearest sampled point


not necessarily:

Exact clicked coordinate.


------------------------------------------------------------


25. SPAN SELECTION

Useful for:

RMS

Mean

Peak

Peak-to-peak

Selected frequency range


------------------------------------------------------------


26. RMS DEFINITION

RMS of complete waveform

is different from:

RMS of AC ripple after removing DC.


------------------------------------------------------------


27. FFT MAXIMUM

np.argmax()

identifies:

Maximum sampled point.


It is not formal peak detection.


------------------------------------------------------------


28. dB DIFFERENCE

100 dBµV
-
90 dBµV

=

10 dB


not automatically:

10%.


------------------------------------------------------------


29. PERFORMANCE

Load large datasets ONCE.

Do not repeatedly read files during every slider movement.


------------------------------------------------------------


30. WIDGET REFERENCES

Keep:

slider

button

radio

checkbox

cursor

selector


objects alive while the figure is active.


------------------------------------------------------------


31. INTERACTIVE != PUBLICATION

Interactive tools:

Explore


Static figures:

Communicate final results


------------------------------------------------------------


32. SNAPSHOT

Saving the current interactive view is useful,

but also save:

Parameter values.


------------------------------------------------------------


33. REPRODUCIBILITY

Do not rely on remembering:

Where the slider was.


Store:

Frequency

Load

Case

Time range

Frequency range

Analysis settings


------------------------------------------------------------


34. ENGINEERING APPLICATIONS

Especially useful for:

Power electronics

FFT / EMI

Control systems

Experimental measurements

Parameter sweeps

Thermal studies

DOE

Optimization

ML prediction

Signal processing

Renewable-energy research


------------------------------------------------------------


35. MOST IMPORTANT PRINCIPLE

Interactive plotting should help answer:

"What should I investigate?"


It should then lead to:

A numerical

documented

reproducible

engineering analysis.


------------------------------------------------------------


36. COMPLETE WORKFLOW

Engineering Dataset
        ↓
Validate
        ↓
Create Base Figure
        ↓
Add Widget
        ↓
Define Callback
        ↓
Interact
        ↓
Update Existing Artists
        ↓
draw_idle()
        ↓
Inspect Important Region
        ↓
Calculate Numerical Metric
        ↓
Record Settings
        ↓
Generate Static Figure
        ↓
Export
        ↓
Paper / Thesis / Report


------------------------------------------------------------


NEXT:

33_engineering_parameter_sweep_visualization.py


The next file will be the FINAL specialized visualization
file and will bring together many earlier concepts into one
complete engineering workflow:

Parameter sweeps

DOE-style datasets

One-parameter sweeps

Two-parameter sweeps

Sensitivity curves

Normalized sensitivity

Heatmaps

Contour maps

3D surfaces

Baseline comparison

Absolute difference

Relative change for linear quantities

dB reduction for logarithmic quantities

Feasible regions

Engineering constraints

Optimum sampled points

Multi-objective tradeoffs

Robustness / tolerance results

Automatic ranking

Long-form DataFrames

Pivot tables

Publication multi-panel figures

Saving processed results

and a complete:

Simulation / Experiment
        ↓
Parameter Sweep
        ↓
Visualization
        ↓
Optimization
        ↓
Engineering Decision

workflow.
"""
