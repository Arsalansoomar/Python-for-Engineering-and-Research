"""
============================================================
Python for Engineering and Research
33 - Engineering Parameter-Sweep Visualization
============================================================

Purpose:
    Build a complete engineering parameter-sweep workflow
    from synthetic/raw-style parameter cases through
    visualization, constraints, ranking, robustness, and
    publication-ready figures.

Topics:
    1. One-parameter sweeps
    2. Two-parameter sweeps
    3. Long-form DataFrames
    4. Sensitivity curves
    5. Normalized sensitivity
    6. Baseline comparison
    7. Absolute and relative change
    8. dB-domain reduction
    9. Heatmaps
    10. Contour maps
    11. 3D response surfaces
    12. Engineering constraints
    13. Feasible-region maps
    14. Best sampled points
    15. Multi-objective tradeoffs
    16. Pareto-optimal sampled points
    17. Weighted ranking
    18. Robustness / tolerance analysis
    19. Automatic summary tables
    20. Publication multi-panel figures
    21. CSV export
    22. Common mistakes
    23. Key takeaways

Important:
    A parameter sweep evaluates discrete sampled cases.
    The best sampled case is not automatically the global
    optimum of a continuous design space.

    Relative percentage change is appropriate for suitable
    linear quantities. A difference between logarithmic
    quantities such as dBµV should normally be reported in
    dB unless a physically meaningful linear-domain
    conversion is intentionally performed.

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
# 2. PROJECT PATHS
# ============================================================

SCRIPT_DIR = Path(__file__).resolve().parent

OUTPUT_FIG_DIR = (
    SCRIPT_DIR
    / "output_figures"
    / "parameter_sweep"
)

OUTPUT_DATA_DIR = (
    SCRIPT_DIR
    / "output_data"
    / "parameter_sweep"
)

OUTPUT_FIG_DIR.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT_DATA_DIR.mkdir(
    parents=True,
    exist_ok=True
)

print("\n--- Parameter-Sweep Output Folders ---")
print(OUTPUT_FIG_DIR)
print(OUTPUT_DATA_DIR)


# ============================================================
# 3. WHAT IS A PARAMETER SWEEP?
# ============================================================

"""
A parameter sweep systematically evaluates a model,
simulation, or experiment at multiple parameter values.

ONE-PARAMETER SWEEP
------------------------------------------------------------
Gate Resistance
    ↓
2 Ω
4 Ω
6 Ω
8 Ω
10 Ω
    ↓
Observe:
Loss
Overshoot
EMI

TWO-PARAMETER SWEEP
------------------------------------------------------------
Switching Frequency × Load
              ↓
        Engineering Response
              ↓
Efficiency / Loss / Temperature / EMI

The result is not only a collection of plots.
It is a sampled design space.
"""


# ============================================================
# 4. SYNTHETIC ENGINEERING RESPONSE MODEL
# ============================================================

"""
The following function creates reproducible educational
responses for a converter-like design study.

Inputs:
    Switching frequency [kHz]
    Load [%]

Outputs:
    Efficiency [%]
    Power loss [W]
    Temperature [°C]
    Baseline EMI [dBµV]
    Candidate EMI [dBµV]
    EMI reduction [dB]

These equations are teaching examples only.
They are NOT a validated model of a specific converter.
"""


def engineering_response_model(
    frequency_khz,
    load_percent
):
    """
    Calculate synthetic engineering responses.

    Parameters
    ----------
    frequency_khz : array-like
        Switching frequency in kHz.

    load_percent : array-like
        Load in percent.

    Returns
    -------
    dict[str, ndarray]
        Engineering response arrays.
    """

    frequency_khz = np.asarray(
        frequency_khz,
        dtype=float
    )

    load_percent = np.asarray(
        load_percent,
        dtype=float
    )

    # Linear engineering metric: efficiency.
    efficiency_percent = (
        96.40
        - 0.000050
        * (frequency_khz - 135.0) ** 2
        - 0.00032
        * (load_percent - 78.0) ** 2
        - 0.0010
        * np.abs(frequency_khz - 135.0)
    )

    # Loss increases away from a favorable operating region.
    power_loss_w = (
        5.2
        + 0.00016
        * (frequency_khz - 90.0) ** 2
        + 0.00080
        * (load_percent - 25.0) ** 2
        + 0.012
        * load_percent
    )

    # Thermal response derived from the synthetic loss model.
    temperature_c = (
        28.0
        + 2.15
        * power_loss_w
        + 0.025
        * load_percent
    )

    # Synthetic logarithmic EMI metric.
    baseline_emi_dbuV = (
        96.0
        + 4.0
        * np.sin(frequency_khz / 22.0)
        + 0.030
        * load_percent
        + 0.010
        * (frequency_khz - 120.0)
    )

    # Candidate reduction changes across the design space.
    emi_reduction_db = (
        7.0
        + 4.0
        * np.exp(
            -(
                (frequency_khz - 145.0) / 55.0
            ) ** 2
        )
        + 1.5
        * np.exp(
            -(
                (load_percent - 70.0) / 28.0
            ) ** 2
        )
        - 0.010
        * np.abs(load_percent - 70.0)
    )

    candidate_emi_dbuV = (
        baseline_emi_dbuV
        - emi_reduction_db
    )

    return {
        "Efficiency_percent": efficiency_percent,
        "Power_Loss_W": power_loss_w,
        "Temperature_C": temperature_c,
        "Baseline_EMI_dBuV": baseline_emi_dbuV,
        "Candidate_EMI_dBuV": candidate_emi_dbuV,
        "EMI_Reduction_dB": emi_reduction_db
    }


# ============================================================
# 5. ONE-PARAMETER SWEEP
# ============================================================

"""
LEVEL 1 — CONCEPT

Change one parameter while holding the others constant.

LEVEL 2 — EXAMPLE

Frequency:
50 → 250 kHz

Load:
fixed at 70%

LEVEL 3 — ENGINEERING USE

Observe how:
Efficiency
Loss
Temperature
EMI

respond to switching frequency alone.
"""

frequency_sweep_khz = np.linspace(
    50,
    250,
    101
)

fixed_load_percent = 70.0

one_parameter_results = engineering_response_model(
    frequency_sweep_khz,
    fixed_load_percent
)


# ============================================================
# 6. ONE-PARAMETER SWEEP DATAFRAME
# ============================================================

one_parameter_df = pd.DataFrame(
    {
        "Switching_Frequency_kHz": frequency_sweep_khz,
        "Load_percent": fixed_load_percent,
        **one_parameter_results
    }
)

print("\n--- One-Parameter Sweep ---")
print(one_parameter_df.head())


# ============================================================
# 7. BASIC SENSITIVITY CURVES
# ============================================================

fig, axes = plt.subplots(
    3,
    1,
    figsize=(8, 8),
    sharex=True
)

axes[0].plot(
    frequency_sweep_khz,
    one_parameter_df["Efficiency_percent"]
)
axes[0].set_ylabel("Efficiency [%]")

axes[1].plot(
    frequency_sweep_khz,
    one_parameter_df["Power_Loss_W"]
)
axes[1].set_ylabel("Power Loss [W]")

axes[2].plot(
    frequency_sweep_khz,
    one_parameter_df["Temperature_C"]
)
axes[2].set_xlabel("Switching Frequency [kHz]")
axes[2].set_ylabel("Temperature [°C]")

for ax in axes:
    ax.grid(True)

fig.suptitle(
    f"One-Parameter Sweep at {fixed_load_percent:.0f}% Load"
)

fig.tight_layout()
plt.show()


# ============================================================
# 8. NUMERICAL LOCAL SENSITIVITY
# ============================================================

"""
A simple numerical local sensitivity can be estimated with:

dy / dx

using:

np.gradient(y, x)

Units matter.

Example:
Efficiency sensitivity to frequency has units roughly:
percentage points / kHz
"""

frequency_sensitivity_efficiency = np.gradient(
    one_parameter_df["Efficiency_percent"].to_numpy(),
    frequency_sweep_khz
)

frequency_sensitivity_loss = np.gradient(
    one_parameter_df["Power_Loss_W"].to_numpy(),
    frequency_sweep_khz
)


# ============================================================
# 9. PLOT LOCAL SENSITIVITY
# ============================================================

fig, axes = plt.subplots(
    2,
    1,
    figsize=(8, 6),
    sharex=True
)

axes[0].plot(
    frequency_sweep_khz,
    frequency_sensitivity_efficiency
)
axes[0].axhline(0, linestyle="--", linewidth=1)
axes[0].set_ylabel("dη/df [percentage points/kHz]")
axes[0].grid(True)

axes[1].plot(
    frequency_sweep_khz,
    frequency_sensitivity_loss
)
axes[1].axhline(0, linestyle="--", linewidth=1)
axes[1].set_xlabel("Switching Frequency [kHz]")
axes[1].set_ylabel("dLoss/df [W/kHz]")
axes[1].grid(True)

fig.tight_layout()
plt.show()


# ============================================================
# 10. NORMALIZED SENSITIVITY
# ============================================================

"""
A dimensionless normalized local sensitivity is often
written conceptually as:

S = (x / y) * (dy / dx)

Interpretation:
It relates fractional output change to fractional input
change locally.

Important:
This form becomes unstable or inappropriate when x or y is
zero or near zero. It also depends on the physical meaning
of the variables.
"""


def normalized_local_sensitivity(
    x,
    y
):
    """
    Calculate dimensionless local sensitivity:

        S = (x / y) * dy/dx

    NaN is returned where Y is zero or non-finite.
    """

    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.shape != y.shape:
        raise ValueError(
            "X and Y must have identical shapes."
        )

    derivative = np.gradient(y, x)

    sensitivity = np.full_like(
        y,
        np.nan,
        dtype=float
    )

    valid = (
        np.isfinite(x)
        & np.isfinite(y)
        & np.isfinite(derivative)
        & (y != 0)
    )

    sensitivity[valid] = (
        x[valid]
        / y[valid]
        * derivative[valid]
    )

    return sensitivity


normalized_efficiency_sensitivity = (
    normalized_local_sensitivity(
        frequency_sweep_khz,
        one_parameter_df[
            "Efficiency_percent"
        ].to_numpy()
    )
)


# ============================================================
# 11. NORMALIZED SENSITIVITY PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)

ax.plot(
    frequency_sweep_khz,
    normalized_efficiency_sensitivity
)

ax.axhline(0, linestyle="--", linewidth=1)
ax.set_xlabel("Switching Frequency [kHz]")
ax.set_ylabel("Normalized Local Sensitivity [-]")
ax.set_title("Efficiency Sensitivity to Switching Frequency")
ax.grid(True)
fig.tight_layout()
plt.show()


# ============================================================
# 12. BASELINE OPERATING POINT
# ============================================================

"""
A baseline allows every sweep case to be compared with a
common engineering reference.
"""

baseline_frequency_khz = 100.0
baseline_load_percent = 70.0

baseline_response = engineering_response_model(
    baseline_frequency_khz,
    baseline_load_percent
)

baseline_efficiency = float(
    baseline_response["Efficiency_percent"]
)

baseline_loss = float(
    baseline_response["Power_Loss_W"]
)

baseline_temperature = float(
    baseline_response["Temperature_C"]
)

baseline_candidate_emi = float(
    baseline_response["Candidate_EMI_dBuV"]
)

print("\n--- Baseline Operating Point ---")
print(f"Frequency = {baseline_frequency_khz:.1f} kHz")
print(f"Load = {baseline_load_percent:.1f}%")
print(f"Efficiency = {baseline_efficiency:.4f}%")
print(f"Loss = {baseline_loss:.4f} W")
print(f"Temperature = {baseline_temperature:.4f} °C")
print(f"Candidate EMI = {baseline_candidate_emi:.4f} dBµV")


# ============================================================
# 13. ABSOLUTE DIFFERENCE FROM BASELINE
# ============================================================

one_parameter_df[
    "Efficiency_Difference_pp"
] = (
    one_parameter_df["Efficiency_percent"]
    - baseline_efficiency
)

one_parameter_df[
    "Power_Loss_Difference_W"
] = (
    one_parameter_df["Power_Loss_W"]
    - baseline_loss
)


# ============================================================
# 14. RELATIVE CHANGE FOR LINEAR QUANTITY
# ============================================================


def relative_change_percent(
    value,
    reference
):
    """
    Calculate relative percentage change for a suitable
    linear-domain quantity.
    """

    value = np.asarray(value, dtype=float)
    reference = float(reference)

    if reference == 0:
        raise ZeroDivisionError(
            "Reference value must be non-zero."
        )

    return (
        (value - reference)
        / reference
        * 100.0
    )


one_parameter_df[
    "Power_Loss_Relative_Change_percent"
] = relative_change_percent(
    one_parameter_df["Power_Loss_W"],
    baseline_loss
)


# ============================================================
# 15. dB-DOMAIN COMPARISON
# ============================================================

"""
For logarithmic quantities such as dBµV:

Baseline dBµV - Candidate dBµV

is reported directly as a dB difference/reduction.

Do NOT treat:
100 dBµV → 90 dBµV

as an ordinary 10% reduction.
"""

one_parameter_df[
    "Candidate_EMI_Difference_from_Baseline_dB"
] = (
    baseline_candidate_emi
    - one_parameter_df["Candidate_EMI_dBuV"]
)


# ============================================================
# 16. BASELINE COMPARISON FIGURE
# ============================================================

fig, axes = plt.subplots(
    3,
    1,
    figsize=(8, 8),
    sharex=True
)

axes[0].plot(
    frequency_sweep_khz,
    one_parameter_df["Efficiency_Difference_pp"]
)
axes[0].axhline(0, linestyle="--", linewidth=1)
axes[0].set_ylabel("Efficiency Difference [percentage points]")

axes[1].plot(
    frequency_sweep_khz,
    one_parameter_df["Power_Loss_Relative_Change_percent"]
)
axes[1].axhline(0, linestyle="--", linewidth=1)
axes[1].set_ylabel("Loss Relative Change [%]")

axes[2].plot(
    frequency_sweep_khz,
    one_parameter_df[
        "Candidate_EMI_Difference_from_Baseline_dB"
    ]
)
axes[2].axhline(0, linestyle="--", linewidth=1)
axes[2].set_xlabel("Switching Frequency [kHz]")
axes[2].set_ylabel("EMI Difference [dB]")

for ax in axes:
    ax.grid(True)

fig.tight_layout()
plt.show()


# ============================================================
# 17. TWO-PARAMETER SWEEP
# ============================================================

frequency_values_khz = np.linspace(
    50,
    250,
    41
)

load_values_percent = np.linspace(
    20,
    100,
    33
)

frequency_grid, load_grid = np.meshgrid(
    frequency_values_khz,
    load_values_percent
)

grid_results = engineering_response_model(
    frequency_grid,
    load_grid
)


# ============================================================
# 18. LONG-FORM DATAFRAME
# ============================================================

parameter_sweep_df = pd.DataFrame(
    {
        "Switching_Frequency_kHz": frequency_grid.ravel(),
        "Load_percent": load_grid.ravel(),
        "Efficiency_percent": grid_results[
            "Efficiency_percent"
        ].ravel(),
        "Power_Loss_W": grid_results[
            "Power_Loss_W"
        ].ravel(),
        "Temperature_C": grid_results[
            "Temperature_C"
        ].ravel(),
        "Baseline_EMI_dBuV": grid_results[
            "Baseline_EMI_dBuV"
        ].ravel(),
        "Candidate_EMI_dBuV": grid_results[
            "Candidate_EMI_dBuV"
        ].ravel(),
        "EMI_Reduction_dB": grid_results[
            "EMI_Reduction_dB"
        ].ravel()
    }
)

print("\n--- Two-Parameter Sweep Shape ---")
print(parameter_sweep_df.shape)
print(parameter_sweep_df.head())


# ============================================================
# 19. VALIDATE DUPLICATE PARAMETER COMBINATIONS
# ============================================================

parameter_key_columns = [
    "Switching_Frequency_kHz",
    "Load_percent"
]

duplicate_parameter_rows = (
    parameter_sweep_df.duplicated(
        subset=parameter_key_columns,
        keep=False
    )
)

print("\nDuplicate parameter combinations:")
print(int(duplicate_parameter_rows.sum()))


# ============================================================
# 20. PIVOT TABLE HELPER
# ============================================================


def response_pivot_table(
    dataframe,
    value_column,
    aggfunc="mean"
):
    """
    Convert long-form sweep data into a 2D response table.

    pivot_table() is used instead of pivot() so repeated
    parameter combinations can be aggregated deliberately.
    """

    required = {
        "Switching_Frequency_kHz",
        "Load_percent",
        value_column
    }

    missing = required.difference(
        dataframe.columns
    )

    if missing:
        raise KeyError(
            f"Missing columns: {sorted(missing)}"
        )

    pivot = dataframe.pivot_table(
        index="Load_percent",
        columns="Switching_Frequency_kHz",
        values=value_column,
        aggfunc=aggfunc
    )

    return pivot.sort_index().sort_index(axis=1)


# ============================================================
# 21. CREATE RESPONSE MATRICES
# ============================================================

efficiency_pivot = response_pivot_table(
    parameter_sweep_df,
    "Efficiency_percent"
)

loss_pivot = response_pivot_table(
    parameter_sweep_df,
    "Power_Loss_W"
)

temperature_pivot = response_pivot_table(
    parameter_sweep_df,
    "Temperature_C"
)

emi_reduction_pivot = response_pivot_table(
    parameter_sweep_df,
    "EMI_Reduction_dB"
)

pivot_frequency_khz = (
    efficiency_pivot.columns.to_numpy(
        dtype=float
    )
)

pivot_load_percent = (
    efficiency_pivot.index.to_numpy(
        dtype=float
    )
)

pivot_frequency_grid, pivot_load_grid = np.meshgrid(
    pivot_frequency_khz,
    pivot_load_percent
)


# ============================================================
# 22. HEATMAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(8.5, 5.5)
)

heatmap = ax.pcolormesh(
    pivot_frequency_grid,
    pivot_load_grid,
    efficiency_pivot.to_numpy(),
    shading="auto",
    cmap="viridis"
)

colorbar = fig.colorbar(
    heatmap,
    ax=ax
)
colorbar.set_label("Efficiency [%]")

ax.set_xlabel("Switching Frequency [kHz]")
ax.set_ylabel("Load [%]")
ax.set_title("Efficiency Parameter Sweep")
fig.tight_layout()
plt.show()


# ============================================================
# 23. FILLED CONTOUR MAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(8.5, 5.5)
)

contour = ax.contourf(
    pivot_frequency_grid,
    pivot_load_grid,
    efficiency_pivot.to_numpy(),
    levels=20,
    cmap="viridis"
)

contour_lines = ax.contour(
    pivot_frequency_grid,
    pivot_load_grid,
    efficiency_pivot.to_numpy(),
    levels=10,
    linewidths=0.7
)

ax.clabel(
    contour_lines,
    inline=True,
    fontsize=7,
    fmt="%.2f"
)

colorbar = fig.colorbar(
    contour,
    ax=ax
)
colorbar.set_label("Efficiency [%]")

ax.set_xlabel("Switching Frequency [kHz]")
ax.set_ylabel("Load [%]")
ax.set_title("Efficiency Contour Map")
fig.tight_layout()
plt.show()


# ============================================================
# 24. 3D RESPONSE SURFACE
# ============================================================

fig = plt.figure(
    figsize=(8.5, 6)
)

ax = fig.add_subplot(
    111,
    projection="3d"
)

surface = ax.plot_surface(
    pivot_frequency_grid,
    pivot_load_grid,
    efficiency_pivot.to_numpy(),
    cmap="viridis",
    edgecolor="none"
)

colorbar = fig.colorbar(
    surface,
    ax=ax,
    shrink=0.70,
    pad=0.10
)
colorbar.set_label("Efficiency [%]")

ax.set_xlabel("Switching Frequency [kHz]")
ax.set_ylabel("Load [%]")
ax.set_zlabel("Efficiency [%]")
ax.view_init(elev=25, azim=-135)
plt.show()


# ============================================================
# 25. BEST SAMPLED POINTS
# ============================================================

"""
Important terminology:

np.argmax() or idxmax() over the sweep identifies the
BEST SAMPLED POINT among evaluated cases.

It does NOT automatically prove a continuous global
optimum.
"""

best_efficiency_index = parameter_sweep_df[
    "Efficiency_percent"
].idxmax()

best_efficiency_case = parameter_sweep_df.loc[
    best_efficiency_index
].copy()

minimum_loss_index = parameter_sweep_df[
    "Power_Loss_W"
].idxmin()

minimum_loss_case = parameter_sweep_df.loc[
    minimum_loss_index
].copy()

maximum_emi_reduction_index = parameter_sweep_df[
    "EMI_Reduction_dB"
].idxmax()

maximum_emi_reduction_case = parameter_sweep_df.loc[
    maximum_emi_reduction_index
].copy()

print("\n--- Best Sampled Efficiency Case ---")
print(best_efficiency_case)

print("\n--- Minimum Sampled Loss Case ---")
print(minimum_loss_case)

print("\n--- Maximum Sampled EMI Reduction Case ---")
print(maximum_emi_reduction_case)


# ============================================================
# 26. MARK BEST SAMPLED POINT ON CONTOUR
# ============================================================

fig, ax = plt.subplots(
    figsize=(8.5, 5.5)
)

contour = ax.contourf(
    pivot_frequency_grid,
    pivot_load_grid,
    efficiency_pivot.to_numpy(),
    levels=20,
    cmap="viridis"
)

ax.scatter(
    best_efficiency_case[
        "Switching_Frequency_kHz"
    ],
    best_efficiency_case[
        "Load_percent"
    ],
    marker="*",
    s=160,
    label="Best sampled efficiency"
)

colorbar = fig.colorbar(
    contour,
    ax=ax
)
colorbar.set_label("Efficiency [%]")

ax.set_xlabel("Switching Frequency [kHz]")
ax.set_ylabel("Load [%]")
ax.legend()
ax.grid(True, alpha=0.25)
fig.tight_layout()
plt.show()


# ============================================================
# 27. ENGINEERING CONSTRAINTS
# ============================================================

"""
A practical design is usually constrained by more than one
response.

Example constraints:

Efficiency >= 95.5%
Temperature <= 52 °C
Power Loss <= 10 W
EMI Reduction >= 8 dB

These are educational thresholds for this synthetic model.
"""

efficiency_requirement = 95.5
temperature_limit_c = 52.0
power_loss_limit_w = 10.0
emi_reduction_requirement_db = 8.0

parameter_sweep_df[
    "Meets_Efficiency"
] = (
    parameter_sweep_df["Efficiency_percent"]
    >= efficiency_requirement
)

parameter_sweep_df[
    "Meets_Temperature"
] = (
    parameter_sweep_df["Temperature_C"]
    <= temperature_limit_c
)

parameter_sweep_df[
    "Meets_Power_Loss"
] = (
    parameter_sweep_df["Power_Loss_W"]
    <= power_loss_limit_w
)

parameter_sweep_df[
    "Meets_EMI_Reduction"
] = (
    parameter_sweep_df["EMI_Reduction_dB"]
    >= emi_reduction_requirement_db
)

parameter_sweep_df[
    "Feasible"
] = (
    parameter_sweep_df["Meets_Efficiency"]
    & parameter_sweep_df["Meets_Temperature"]
    & parameter_sweep_df["Meets_Power_Loss"]
    & parameter_sweep_df["Meets_EMI_Reduction"]
)

feasible_count = int(
    parameter_sweep_df["Feasible"].sum()
)

print("\n--- Feasible Sampled Cases ---")
print(
    feasible_count,
    "of",
    len(parameter_sweep_df)
)


# ============================================================
# 28. FEASIBLE REGION MAP
# ============================================================

feasible_pivot = response_pivot_table(
    parameter_sweep_df,
    "Feasible",
    aggfunc="max"
).astype(float)

fig, ax = plt.subplots(
    figsize=(8.5, 5.5)
)

feasible_image = ax.pcolormesh(
    pivot_frequency_grid,
    pivot_load_grid,
    feasible_pivot.to_numpy(),
    shading="auto",
    cmap="Greys",
    vmin=0,
    vmax=1
)

ax.set_xlabel("Switching Frequency [kHz]")
ax.set_ylabel("Load [%]")
ax.set_title("Feasible Sampled Design Region")

colorbar = fig.colorbar(
    feasible_image,
    ax=ax,
    ticks=[0, 1]
)
colorbar.set_label("Feasible Flag")

fig.tight_layout()
plt.show()


# ============================================================
# 29. CONSTRAINT BOUNDARIES ON RESPONSE MAP
# ============================================================

fig, ax = plt.subplots(
    figsize=(8.8, 5.8)
)

base_contour = ax.contourf(
    frequency_grid,
    load_grid,
    grid_results["Efficiency_percent"],
    levels=20,
    cmap="viridis"
)

# Each contour is a constraint boundary.
ax.contour(
    frequency_grid,
    load_grid,
    grid_results["Efficiency_percent"],
    levels=[efficiency_requirement],
    linewidths=1.4
)

ax.contour(
    frequency_grid,
    load_grid,
    grid_results["Temperature_C"],
    levels=[temperature_limit_c],
    linewidths=1.4,
    linestyles="--"
)

ax.contour(
    frequency_grid,
    load_grid,
    grid_results["Power_Loss_W"],
    levels=[power_loss_limit_w],
    linewidths=1.4,
    linestyles="-."
)

ax.contour(
    frequency_grid,
    load_grid,
    grid_results["EMI_Reduction_dB"],
    levels=[emi_reduction_requirement_db],
    linewidths=1.4,
    linestyles=":"
)

colorbar = fig.colorbar(
    base_contour,
    ax=ax
)
colorbar.set_label("Efficiency [%]")

ax.set_xlabel("Switching Frequency [kHz]")
ax.set_ylabel("Load [%]")
ax.set_title("Response Map with Engineering Constraint Boundaries")
fig.tight_layout()
plt.show()


# ============================================================
# 30. BEST FEASIBLE SAMPLED CASE
# ============================================================

feasible_cases = parameter_sweep_df[
    parameter_sweep_df["Feasible"]
].copy()

if feasible_cases.empty:
    best_feasible_case = None
    print("\nNo sampled case satisfies all constraints.")
else:
    best_feasible_index = feasible_cases[
        "Efficiency_percent"
    ].idxmax()

    best_feasible_case = parameter_sweep_df.loc[
        best_feasible_index
    ].copy()

    print("\n--- Best Feasible Sampled Case by Efficiency ---")
    print(best_feasible_case)


# ============================================================
# 31. NORMALIZATION FOR MULTI-OBJECTIVE COMPARISON
# ============================================================

"""
Different engineering metrics use different units:

Efficiency [%]
Loss [W]
Temperature [°C]
EMI Reduction [dB]

To create an educational weighted score, each metric can be
scaled to 0–1 first.

Important:
The result depends on:

- normalization method
- selected metric range
- objective direction
- chosen weights

Therefore a weighted score is a design preference model,
not an objective law of nature.
"""


def min_max_normalize(
    values
):
    """
    Normalize finite values to [0, 1].
    """

    values = np.asarray(values, dtype=float)

    minimum = np.nanmin(values)
    maximum = np.nanmax(values)

    if maximum == minimum:
        return np.zeros_like(values)

    return (
        (values - minimum)
        / (maximum - minimum)
    )


parameter_sweep_df[
    "Efficiency_Score"
] = min_max_normalize(
    parameter_sweep_df["Efficiency_percent"]
)

# Lower loss is better, so invert normalized loss.
parameter_sweep_df[
    "Loss_Score"
] = 1.0 - min_max_normalize(
    parameter_sweep_df["Power_Loss_W"]
)

# Lower temperature is better.
parameter_sweep_df[
    "Temperature_Score"
] = 1.0 - min_max_normalize(
    parameter_sweep_df["Temperature_C"]
)

# Higher reduction is better.
parameter_sweep_df[
    "EMI_Score"
] = min_max_normalize(
    parameter_sweep_df["EMI_Reduction_dB"]
)


# ============================================================
# 32. WEIGHTED ENGINEERING SCORE
# ============================================================

weights = {
    "Efficiency_Score": 0.35,
    "Loss_Score": 0.25,
    "Temperature_Score": 0.15,
    "EMI_Score": 0.25
}

if not np.isclose(
    sum(weights.values()),
    1.0
):
    raise ValueError(
        "Multi-objective weights must sum to 1."
    )

parameter_sweep_df[
    "Weighted_Engineering_Score"
] = sum(
    parameter_sweep_df[column]
    * weight
    for column, weight in weights.items()
)


# ============================================================
# 33. RANK SAMPLED CASES
# ============================================================

ranking_df = parameter_sweep_df.sort_values(
    "Weighted_Engineering_Score",
    ascending=False
).copy()

ranking_df[
    "Overall_Rank"
] = np.arange(
    1,
    len(ranking_df) + 1
)

print("\n--- Top 10 Weighted Sampled Cases ---")
print(
    ranking_df[
        [
            "Overall_Rank",
            "Switching_Frequency_kHz",
            "Load_percent",
            "Efficiency_percent",
            "Power_Loss_W",
            "Temperature_C",
            "EMI_Reduction_dB",
            "Weighted_Engineering_Score",
            "Feasible"
        ]
    ].head(10)
)


# ============================================================
# 34. WEIGHTED SCORE MAP
# ============================================================

weighted_score_pivot = response_pivot_table(
    parameter_sweep_df,
    "Weighted_Engineering_Score"
)

fig, ax = plt.subplots(
    figsize=(8.5, 5.5)
)

score_map = ax.pcolormesh(
    pivot_frequency_grid,
    pivot_load_grid,
    weighted_score_pivot.to_numpy(),
    shading="auto",
    cmap="viridis"
)

colorbar = fig.colorbar(
    score_map,
    ax=ax
)
colorbar.set_label("Weighted Engineering Score [-]")

ax.set_xlabel("Switching Frequency [kHz]")
ax.set_ylabel("Load [%]")
ax.set_title("Weighted Multi-Objective Score")
fig.tight_layout()
plt.show()


# ============================================================
# 35. PARETO-OPTIMAL SAMPLED CASES
# ============================================================

"""
A Pareto-optimal sampled case is not dominated by another
sampled case across all selected objectives.

Here we convert every objective into a minimization form:

Minimize:
- negative efficiency
- power loss
- temperature
- negative EMI reduction

This implementation is appropriate for a moderate teaching
sweep. Very large optimization datasets may need more
specialized algorithms.
"""


def pareto_efficient_mask(
    objective_matrix
):
    """
    Return a Boolean mask of nondominated rows.

    All columns are assumed to be minimization objectives.
    """

    costs = np.asarray(
        objective_matrix,
        dtype=float
    )

    if costs.ndim != 2:
        raise ValueError(
            "objective_matrix must be two-dimensional."
        )

    if not np.all(np.isfinite(costs)):
        raise ValueError(
            "Pareto objectives must be finite."
        )

    number_of_points = costs.shape[0]
    efficient = np.ones(
        number_of_points,
        dtype=bool
    )

    for i in range(number_of_points):
        if not efficient[i]:
            continue

        # A point j dominates point i when:
        # j is no worse in every objective
        # and strictly better in at least one.
        candidates = np.where(efficient)[0]
        candidate_costs = costs[candidates]

        dominates_i = (
            np.all(
                candidate_costs <= costs[i],
                axis=1
            )
            & np.any(
                candidate_costs < costs[i],
                axis=1
            )
        )

        if np.any(dominates_i):
            efficient[i] = False

    return efficient


pareto_objectives = np.column_stack(
    [
        -parameter_sweep_df["Efficiency_percent"].to_numpy(),
        parameter_sweep_df["Power_Loss_W"].to_numpy(),
        parameter_sweep_df["Temperature_C"].to_numpy(),
        -parameter_sweep_df["EMI_Reduction_dB"].to_numpy()
    ]
)

parameter_sweep_df[
    "Pareto_Optimal"
] = pareto_efficient_mask(
    pareto_objectives
)

pareto_df = parameter_sweep_df[
    parameter_sweep_df["Pareto_Optimal"]
].copy()

print("\n--- Pareto-Optimal Sampled Cases ---")
print(len(pareto_df))


# ============================================================
# 36. PARETO TRADEOFF PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5.2)
)

ax.scatter(
    parameter_sweep_df["Power_Loss_W"],
    parameter_sweep_df["Efficiency_percent"],
    s=18,
    alpha=0.35,
    label="All sampled cases"
)

ax.scatter(
    pareto_df["Power_Loss_W"],
    pareto_df["Efficiency_percent"],
    s=35,
    marker="o",
    label="Pareto-optimal sampled cases"
)

ax.set_xlabel("Power Loss [W]")
ax.set_ylabel("Efficiency [%]")
ax.set_title("Efficiency–Loss Tradeoff")
ax.legend()
ax.grid(True)
fig.tight_layout()
plt.show()


# ============================================================
# 37. CONSTRAINT-AWARE RANKING
# ============================================================

"""
For practical design selection, it is often useful to rank
only cases that first satisfy mandatory constraints.
"""

feasible_ranking_df = ranking_df[
    ranking_df["Feasible"]
].copy()

if feasible_ranking_df.empty:
    recommended_case = None
    print("\nNo feasible candidate is available for ranking.")
else:
    recommended_case = feasible_ranking_df.iloc[0].copy()

    print("\n--- Recommended Sampled Case Under Current Rules ---")
    print(
        recommended_case[
            [
                "Switching_Frequency_kHz",
                "Load_percent",
                "Efficiency_percent",
                "Power_Loss_W",
                "Temperature_C",
                "EMI_Reduction_dB",
                "Weighted_Engineering_Score"
            ]
        ]
    )


# ============================================================
# 38. ROBUSTNESS / TOLERANCE ANALYSIS
# ============================================================

"""
A candidate that looks good at exactly one sampled point
may become poor when operating conditions vary.

The following Monte Carlo example perturbs:

Switching frequency ±5% approximately
Load ±5% approximately

using normally distributed perturbations with sigma chosen
so that 3 sigma is about 5% of the nominal value.

This is only an assumed perturbation model for teaching.
It is not a universal tolerance or reliability model.
"""

rng = np.random.default_rng(42)

robustness_samples = 10_000

if recommended_case is not None:
    nominal_frequency = float(
        recommended_case[
            "Switching_Frequency_kHz"
        ]
    )

    nominal_load = float(
        recommended_case[
            "Load_percent"
        ]
    )

    frequency_sigma = (
        0.05
        * nominal_frequency
        / 3.0
    )

    load_sigma = (
        0.05
        * nominal_load
        / 3.0
    )

    robustness_frequency = rng.normal(
        nominal_frequency,
        frequency_sigma,
        robustness_samples
    )

    robustness_load = rng.normal(
        nominal_load,
        load_sigma,
        robustness_samples
    )

    # Keep the synthetic operating variables inside the
    # original investigated range.
    robustness_frequency = np.clip(
        robustness_frequency,
        frequency_values_khz.min(),
        frequency_values_khz.max()
    )

    robustness_load = np.clip(
        robustness_load,
        load_values_percent.min(),
        load_values_percent.max()
    )

    robustness_results = engineering_response_model(
        robustness_frequency,
        robustness_load
    )

    robustness_feasible = (
        (
            robustness_results[
                "Efficiency_percent"
            ]
            >= efficiency_requirement
        )
        & (
            robustness_results[
                "Temperature_C"
            ]
            <= temperature_limit_c
        )
        & (
            robustness_results[
                "Power_Loss_W"
            ]
            <= power_loss_limit_w
        )
        & (
            robustness_results[
                "EMI_Reduction_dB"
            ]
            >= emi_reduction_requirement_db
        )
    )

    assumed_feasibility_probability = (
        100.0
        * np.mean(
            robustness_feasible
        )
    )

    print("\n--- Robustness Result ---")
    print(
        "Constraint-feasible Monte Carlo samples = "
        f"{assumed_feasibility_probability:.2f}%"
    )


# ============================================================
# 39. ROBUSTNESS DISTRIBUTIONS
# ============================================================

if recommended_case is not None:
    fig, axes = plt.subplots(
        2,
        2,
        figsize=(10, 7)
    )

    robustness_plot_data = [
        (
            robustness_results["Efficiency_percent"],
            "Efficiency [%]",
            efficiency_requirement
        ),
        (
            robustness_results["Power_Loss_W"],
            "Power Loss [W]",
            power_loss_limit_w
        ),
        (
            robustness_results["Temperature_C"],
            "Temperature [°C]",
            temperature_limit_c
        ),
        (
            robustness_results["EMI_Reduction_dB"],
            "EMI Reduction [dB]",
            emi_reduction_requirement_db
        )
    ]

    for ax, (
        values,
        label,
        limit
    ) in zip(
        axes.flatten(),
        robustness_plot_data
    ):
        ax.hist(
            values,
            bins=35,
            alpha=0.75
        )

        ax.axvline(
            limit,
            linestyle="--",
            linewidth=1.2,
            label="Constraint"
        )

        ax.set_xlabel(label)
        ax.set_ylabel("Count")
        ax.legend()
        ax.grid(True, alpha=0.25)

    fig.suptitle(
        "Robustness Around Recommended Sampled Case"
    )
    fig.tight_layout()
    plt.show()


# ============================================================
# 40. ROBUSTNESS SUMMARY TABLE
# ============================================================

if recommended_case is not None:
    robustness_summary = pd.DataFrame(
        {
            "Metric": [
                "Efficiency_percent",
                "Power_Loss_W",
                "Temperature_C",
                "EMI_Reduction_dB"
            ],
            "Mean": [
                np.mean(
                    robustness_results[
                        "Efficiency_percent"
                    ]
                ),
                np.mean(
                    robustness_results[
                        "Power_Loss_W"
                    ]
                ),
                np.mean(
                    robustness_results[
                        "Temperature_C"
                    ]
                ),
                np.mean(
                    robustness_results[
                        "EMI_Reduction_dB"
                    ]
                )
            ],
            "Std": [
                np.std(
                    robustness_results[
                        "Efficiency_percent"
                    ],
                    ddof=1
                ),
                np.std(
                    robustness_results[
                        "Power_Loss_W"
                    ],
                    ddof=1
                ),
                np.std(
                    robustness_results[
                        "Temperature_C"
                    ],
                    ddof=1
                ),
                np.std(
                    robustness_results[
                        "EMI_Reduction_dB"
                    ],
                    ddof=1
                )
            ],
            "P05": [
                np.percentile(
                    robustness_results[
                        "Efficiency_percent"
                    ],
                    5
                ),
                np.percentile(
                    robustness_results[
                        "Power_Loss_W"
                    ],
                    5
                ),
                np.percentile(
                    robustness_results[
                        "Temperature_C"
                    ],
                    5
                ),
                np.percentile(
                    robustness_results[
                        "EMI_Reduction_dB"
                    ],
                    5
                )
            ],
            "Median": [
                np.median(
                    robustness_results[
                        "Efficiency_percent"
                    ]
                ),
                np.median(
                    robustness_results[
                        "Power_Loss_W"
                    ]
                ),
                np.median(
                    robustness_results[
                        "Temperature_C"
                    ]
                ),
                np.median(
                    robustness_results[
                        "EMI_Reduction_dB"
                    ]
                )
            ],
            "P95": [
                np.percentile(
                    robustness_results[
                        "Efficiency_percent"
                    ],
                    95
                ),
                np.percentile(
                    robustness_results[
                        "Power_Loss_W"
                    ],
                    95
                ),
                np.percentile(
                    robustness_results[
                        "Temperature_C"
                    ],
                    95
                ),
                np.percentile(
                    robustness_results[
                        "EMI_Reduction_dB"
                    ],
                    95
                )
            ]
        }
    )

    print("\n--- Robustness Summary ---")
    print(robustness_summary)


# ============================================================
# 41. AUTOMATIC TOP-N TABLE
# ============================================================

TOP_N = 10

ranking_columns = [
    "Overall_Rank",
    "Switching_Frequency_kHz",
    "Load_percent",
    "Efficiency_percent",
    "Power_Loss_W",
    "Temperature_C",
    "EMI_Reduction_dB",
    "Weighted_Engineering_Score",
    "Feasible",
    "Pareto_Optimal"
]

top_n_df = ranking_df[
    ranking_columns
].head(TOP_N).copy()


# ============================================================
# 42. SAVE PROCESSED TABLES
# ============================================================

one_parameter_file = (
    OUTPUT_DATA_DIR
    / "one_parameter_frequency_sweep.csv"
)

full_sweep_file = (
    OUTPUT_DATA_DIR
    / "two_parameter_sweep.csv"
)

ranking_file = (
    OUTPUT_DATA_DIR
    / "parameter_sweep_ranking.csv"
)

pareto_file = (
    OUTPUT_DATA_DIR
    / "pareto_optimal_sampled_cases.csv"
)

top_n_file = (
    OUTPUT_DATA_DIR
    / "top_10_parameter_sweep_cases.csv"
)

one_parameter_df.to_csv(
    one_parameter_file,
    index=False
)

parameter_sweep_df.to_csv(
    full_sweep_file,
    index=False
)

ranking_df.to_csv(
    ranking_file,
    index=False
)

pareto_df.to_csv(
    pareto_file,
    index=False
)

top_n_df.to_csv(
    top_n_file,
    index=False
)

if recommended_case is not None:
    robustness_summary_file = (
        OUTPUT_DATA_DIR
        / "recommended_case_robustness_summary.csv"
    )

    robustness_summary.to_csv(
        robustness_summary_file,
        index=False
    )

print("\n--- Processed Data Saved ---")
print(one_parameter_file)
print(full_sweep_file)
print(ranking_file)
print(pareto_file)
print(top_n_file)


# ============================================================
# 43. REUSABLE RESPONSE MAP FUNCTION
# ============================================================


def plot_response_map(
    dataframe,
    value_column,
    colorbar_label,
    title=None,
    cmap="viridis",
    contour_levels=20,
    show_contour_lines=True
):
    """
    Create a filled contour map from long-form sweep data.
    """

    pivot = response_pivot_table(
        dataframe,
        value_column
    )

    x = pivot.columns.to_numpy(dtype=float)
    y = pivot.index.to_numpy(dtype=float)
    x_grid, y_grid = np.meshgrid(x, y)
    z = pivot.to_numpy(dtype=float)

    fig, ax = plt.subplots(
        figsize=(8.5, 5.5)
    )

    filled = ax.contourf(
        x_grid,
        y_grid,
        z,
        levels=contour_levels,
        cmap=cmap
    )

    if show_contour_lines:
        lines = ax.contour(
            x_grid,
            y_grid,
            z,
            levels=10,
            linewidths=0.6
        )

        ax.clabel(
            lines,
            inline=True,
            fontsize=7
        )

    colorbar = fig.colorbar(
        filled,
        ax=ax
    )
    colorbar.set_label(colorbar_label)

    ax.set_xlabel(
        "Switching Frequency [kHz]"
    )
    ax.set_ylabel("Load [%]")

    if title is not None:
        ax.set_title(title)

    fig.tight_layout()

    return fig, ax


# ============================================================
# 44. USE REUSABLE MAP FUNCTION
# ============================================================

fig, ax = plot_response_map(
    parameter_sweep_df,
    value_column="EMI_Reduction_dB",
    colorbar_label="EMI Reduction [dB]",
    title="EMI Reduction Parameter Map",
    cmap="viridis"
)
plt.show()


# ============================================================
# 45. REUSABLE BEST-SAMPLED FUNCTION
# ============================================================


def find_best_sampled_case(
    dataframe,
    metric_column,
    objective="max",
    feasible_only=False
):
    """
    Return the best sampled row for one metric.

    Parameters
    ----------
    dataframe : pandas.DataFrame

    metric_column : str

    objective : {'max', 'min'}

    feasible_only : bool
        Restrict search to rows with Feasible == True.
    """

    data = dataframe.copy()

    if feasible_only:
        if "Feasible" not in data.columns:
            raise KeyError(
                "Feasible column is required."
            )

        data = data[
            data["Feasible"]
        ]

    if data.empty:
        return None

    if metric_column not in data.columns:
        raise KeyError(
            f"Metric column not found: {metric_column}"
        )

    if objective == "max":
        index = data[metric_column].idxmax()
    elif objective == "min":
        index = data[metric_column].idxmin()
    else:
        raise ValueError(
            "objective must be 'max' or 'min'."
        )

    return dataframe.loc[index].copy()


# ============================================================
# 46. BEST-CASE FUNCTION EXAMPLES
# ============================================================

best_temperature_case = find_best_sampled_case(
    parameter_sweep_df,
    "Temperature_C",
    objective="min"
)

best_feasible_emi_case = find_best_sampled_case(
    parameter_sweep_df,
    "EMI_Reduction_dB",
    objective="max",
    feasible_only=True
)


# ============================================================
# 47. PUBLICATION SIZE
# ============================================================


def mm_to_inches(
    millimeters
):
    return millimeters / 25.4


publication_width_mm = 178
publication_width_in = mm_to_inches(
    publication_width_mm
)
publication_height_in = (
    publication_width_in
    * 0.78
)

publication_style = {
    "font.size": 8,
    "axes.labelsize": 9,
    "axes.titlesize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "axes.linewidth": 0.8,
    "lines.linewidth": 1.3,
    "lines.markersize": 4,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.top": True,
    "ytick.right": True
}


# ============================================================
# 48. FINAL PUBLICATION MULTI-PANEL FIGURE
# ============================================================

"""
Capstone figure:

(a) One-parameter efficiency sweep
(b) Two-parameter efficiency contour
(c) Feasible-region map
(d) Efficiency-loss tradeoff with Pareto samples
"""

with mpl.rc_context(publication_style):
    fig, axes = plt.subplots(
        2,
        2,
        figsize=(
            publication_width_in,
            publication_height_in
        ),
        layout="constrained"
    )

    # --------------------------------------------------------
    # (a) 1D sensitivity sweep
    # --------------------------------------------------------
    ax_a = axes[0, 0]

    ax_a.plot(
        frequency_sweep_khz,
        one_parameter_df["Efficiency_percent"]
    )

    ax_a.axvline(
        baseline_frequency_khz,
        linestyle="--",
        linewidth=1,
        label="Baseline"
    )

    ax_a.set_xlabel("Switching Frequency [kHz]")
    ax_a.set_ylabel("Efficiency [%]")
    ax_a.legend()
    ax_a.grid(True, alpha=0.30)
    ax_a.text(
        0.02,
        0.96,
        "(a)",
        transform=ax_a.transAxes,
        va="top",
        fontweight="bold"
    )

    # --------------------------------------------------------
    # (b) Efficiency contour
    # --------------------------------------------------------
    ax_b = axes[0, 1]

    efficiency_contour = ax_b.contourf(
        frequency_grid,
        load_grid,
        grid_results["Efficiency_percent"],
        levels=18,
        cmap="viridis"
    )

    ax_b.scatter(
        best_efficiency_case[
            "Switching_Frequency_kHz"
        ],
        best_efficiency_case[
            "Load_percent"
        ],
        marker="*",
        s=70
    )

    ax_b.set_xlabel("Switching Frequency [kHz]")
    ax_b.set_ylabel("Load [%]")
    ax_b.text(
        0.02,
        0.96,
        "(b)",
        transform=ax_b.transAxes,
        va="top",
        fontweight="bold"
    )

    efficiency_colorbar = fig.colorbar(
        efficiency_contour,
        ax=ax_b
    )
    efficiency_colorbar.set_label("Efficiency [%]")

    # --------------------------------------------------------
    # (c) Feasible map
    # --------------------------------------------------------
    ax_c = axes[1, 0]

    feasible_image = ax_c.pcolormesh(
        pivot_frequency_grid,
        pivot_load_grid,
        feasible_pivot.to_numpy(),
        shading="auto",
        cmap="Greys",
        vmin=0,
        vmax=1
    )

    if recommended_case is not None:
        ax_c.scatter(
            recommended_case[
                "Switching_Frequency_kHz"
            ],
            recommended_case[
                "Load_percent"
            ],
            marker="*",
            s=70,
            label="Recommended sampled case"
        )
        ax_c.legend()

    ax_c.set_xlabel("Switching Frequency [kHz]")
    ax_c.set_ylabel("Load [%]")
    ax_c.text(
        0.02,
        0.96,
        "(c)",
        transform=ax_c.transAxes,
        va="top",
        fontweight="bold"
    )

    feasible_colorbar = fig.colorbar(
        feasible_image,
        ax=ax_c,
        ticks=[0, 1]
    )
    feasible_colorbar.set_label("Feasible Flag")

    # --------------------------------------------------------
    # (d) Tradeoff / Pareto plot
    # --------------------------------------------------------
    ax_d = axes[1, 1]

    ax_d.scatter(
        parameter_sweep_df["Power_Loss_W"],
        parameter_sweep_df["Efficiency_percent"],
        s=10,
        alpha=0.25,
        label="All sampled cases"
    )

    ax_d.scatter(
        pareto_df["Power_Loss_W"],
        pareto_df["Efficiency_percent"],
        s=22,
        label="Pareto-optimal samples"
    )

    ax_d.set_xlabel("Power Loss [W]")
    ax_d.set_ylabel("Efficiency [%]")
    ax_d.legend()
    ax_d.grid(True, alpha=0.30)
    ax_d.text(
        0.02,
        0.96,
        "(d)",
        transform=ax_d.transAxes,
        va="top",
        fontweight="bold"
    )

    # --------------------------------------------------------
    # Save before show()
    # --------------------------------------------------------
    final_png = (
        OUTPUT_FIG_DIR
        / "engineering_parameter_sweep_capstone.png"
    )

    final_pdf = (
        OUTPUT_FIG_DIR
        / "engineering_parameter_sweep_capstone.pdf"
    )

    final_svg = (
        OUTPUT_FIG_DIR
        / "engineering_parameter_sweep_capstone.svg"
    )

    fig.savefig(
        final_png,
        dpi=300,
        bbox_inches="tight"
    )

    fig.savefig(
        final_pdf,
        bbox_inches="tight"
    )

    fig.savefig(
        final_svg,
        bbox_inches="tight"
    )

    print("\n--- Final Capstone Figures Saved ---")
    print(final_png)
    print(final_pdf)
    print(final_svg)

    plt.show()


# ============================================================
# 49. AUTOMATIC SUMMARY RECORD
# ============================================================

summary_rows = [
    {
        "Selection": "Best sampled efficiency",
        "Switching_Frequency_kHz": best_efficiency_case[
            "Switching_Frequency_kHz"
        ],
        "Load_percent": best_efficiency_case[
            "Load_percent"
        ],
        "Efficiency_percent": best_efficiency_case[
            "Efficiency_percent"
        ],
        "Power_Loss_W": best_efficiency_case[
            "Power_Loss_W"
        ],
        "Temperature_C": best_efficiency_case[
            "Temperature_C"
        ],
        "EMI_Reduction_dB": best_efficiency_case[
            "EMI_Reduction_dB"
        ]
    },
    {
        "Selection": "Minimum sampled loss",
        "Switching_Frequency_kHz": minimum_loss_case[
            "Switching_Frequency_kHz"
        ],
        "Load_percent": minimum_loss_case[
            "Load_percent"
        ],
        "Efficiency_percent": minimum_loss_case[
            "Efficiency_percent"
        ],
        "Power_Loss_W": minimum_loss_case[
            "Power_Loss_W"
        ],
        "Temperature_C": minimum_loss_case[
            "Temperature_C"
        ],
        "EMI_Reduction_dB": minimum_loss_case[
            "EMI_Reduction_dB"
        ]
    },
    {
        "Selection": "Maximum sampled EMI reduction",
        "Switching_Frequency_kHz": maximum_emi_reduction_case[
            "Switching_Frequency_kHz"
        ],
        "Load_percent": maximum_emi_reduction_case[
            "Load_percent"
        ],
        "Efficiency_percent": maximum_emi_reduction_case[
            "Efficiency_percent"
        ],
        "Power_Loss_W": maximum_emi_reduction_case[
            "Power_Loss_W"
        ],
        "Temperature_C": maximum_emi_reduction_case[
            "Temperature_C"
        ],
        "EMI_Reduction_dB": maximum_emi_reduction_case[
            "EMI_Reduction_dB"
        ]
    }
]

if recommended_case is not None:
    summary_rows.append(
        {
            "Selection": "Recommended feasible weighted case",
            "Switching_Frequency_kHz": recommended_case[
                "Switching_Frequency_kHz"
            ],
            "Load_percent": recommended_case[
                "Load_percent"
            ],
            "Efficiency_percent": recommended_case[
                "Efficiency_percent"
            ],
            "Power_Loss_W": recommended_case[
                "Power_Loss_W"
            ],
            "Temperature_C": recommended_case[
                "Temperature_C"
            ],
            "EMI_Reduction_dB": recommended_case[
                "EMI_Reduction_dB"
            ]
        }
    )

selection_summary_df = pd.DataFrame(
    summary_rows
)

selection_summary_file = (
    OUTPUT_DATA_DIR
    / "parameter_sweep_selection_summary.csv"
)

selection_summary_df.to_csv(
    selection_summary_file,
    index=False
)


# ============================================================
# 50. COMMON MISTAKE - BEST SAMPLED == GLOBAL OPTIMUM
# ============================================================

"""
Incorrect:

"The global optimum occurs at 135 kHz."

when only a finite grid was evaluated.

Better:

"The best sampled case within the evaluated grid occurred
at ..."

Formal continuous optimization or a refined sweep is needed
before making a stronger claim.
"""


# ============================================================
# 51. COMMON MISTAKE - TOO COARSE A GRID
# ============================================================

"""
A sweep with:

50 kHz
100 kHz
150 kHz
200 kHz
250 kHz

may miss important behavior between samples.

Possible response:

Coarse Sweep
    ↓
Identify Candidate Region
    ↓
Refined Sweep
    ↓
Validate
"""


# ============================================================
# 52. COMMON MISTAKE - TOO DENSE WITHOUT PURPOSE
# ============================================================

"""
A very dense sweep can waste:

Simulation time
Measurement time
Storage
Post-processing time

Use engineering knowledge, DOE, adaptive sampling, or
surrogate models when brute-force resolution becomes
expensive.
"""


# ============================================================
# 53. COMMON MISTAKE - CHANGING MULTIPLE PARAMETERS IN A 1D SWEEP
# ============================================================

"""
If a plot is described as:

Efficiency vs Switching Frequency

while:

Load
Temperature
Input voltage

also change between points,

then the result is not a clean one-parameter sensitivity
study.
"""


# ============================================================
# 54. COMMON MISTAKE - WRONG SENSITIVITY UNITS
# ============================================================

"""
dη/df

has units.

If:
η is percent
and
f is kHz

then the derivative has units approximately:
percentage points per kHz.

Do not label it simply:
Sensitivity [%]
without defining the calculation.
"""


# ============================================================
# 55. COMMON MISTAKE - NORMALIZED SENSITIVITY NEAR ZERO
# ============================================================

"""
S = (x/y) dy/dx

can become unstable when:

y ≈ 0

or may be inappropriate when the physical variable does not
have a meaningful ratio scale.
"""


# ============================================================
# 56. COMMON MISTAKE - PERCENTAGE POINTS VS PERCENT
# ============================================================

"""
Efficiency:
94%
→
95%

Absolute change:
1 percentage point

Relative change:
(95 - 94) / 94 × 100
≈ 1.06%

These are different.
"""


# ============================================================
# 57. COMMON MISTAKE - PERCENT CHANGE FROM dBµV
# ============================================================

"""
100 dBµV
→
90 dBµV

Difference:
10 dB

Do not report:
10% reduction

unless the values are intentionally converted into an
appropriate linear physical domain first.
"""


# ============================================================
# 58. COMMON MISTAKE - HEATMAP WITHOUT UNITS
# ============================================================

"""
Every parameter map should clearly define:

X parameter + unit
Y parameter + unit
Color response + unit
"""


# ============================================================
# 59. COMMON MISTAKE - DIFFERENT COLOR LIMITS
# ============================================================

"""
If Design A and Design B are compared using two heatmaps,
different automatic color limits can make small differences
look large.

For direct comparison, use common:

vmin
vmax
colormap
"""


# ============================================================
# 60. COMMON MISTAKE - INTERPOLATION PRESENTED AS MEASUREMENT
# ============================================================

"""
A smooth contour or triangulated surface may visually fill
space between sampled cases.

Do not imply those intermediate locations were directly:

Measured
or
Simulated

unless they actually were.
"""


# ============================================================
# 61. COMMON MISTAKE - IGNORING FAILED CASES
# ============================================================

"""
A missing simulation can mean:

Solver failure
Instability
Invalid operating point
Unsafe region
Missing data

Do not automatically replace missing cases with zero.
"""


# ============================================================
# 62. COMMON MISTAKE - RANKING BEFORE CONSTRAINTS
# ============================================================

"""
A high weighted score does not make an infeasible design
acceptable.

A useful workflow is often:

Mandatory Constraints
        ↓
Feasible Cases
        ↓
Ranking / Optimization
"""


# ============================================================
# 63. COMMON MISTAKE - ARBITRARY WEIGHTS HIDDEN
# ============================================================

"""
If a weighted score uses:

35% Efficiency
25% Loss
15% Temperature
25% EMI

state those weights.

Changing the weights can change the recommended case.
"""


# ============================================================
# 64. COMMON MISTAKE - PARETO FRONT CALLED ONE BEST DESIGN
# ============================================================

"""
Pareto analysis normally identifies a SET of nondominated
tradeoff solutions.

It does not automatically choose one final design.

Final selection may require:

Constraints
Preferences
Cost
Reliability
Manufacturability
Experimental validation
"""


# ============================================================
# 65. COMMON MISTAKE - MONTE CARLO RESULT CALLED RELIABILITY
# ============================================================

"""
The fraction of Monte Carlo samples satisfying constraints
under an assumed perturbation distribution is conditional
on that assumed model.

Do not automatically call it:

"System reliability"

without a validated probabilistic reliability model.
"""


# ============================================================
# 66. COMMON MISTAKE - ROBUSTNESS ONLY AT NOMINAL POINT
# ============================================================

"""
Nominal Performance
        ≠
Robust Performance

A design may be excellent at exactly one point and fragile
to:

Tolerance
Temperature
Load variation
Parasitic variation
Measurement variation
"""


# ============================================================
# 67. COMMON MISTAKE - RAW DATA OVERWRITTEN
# ============================================================

"""
Recommended structure:

raw_data/
    Original simulations / experiments

output_data/
    Processed sweep tables

output_figures/
    Generated figures

Never overwrite the only copy of raw research data.
"""


# ============================================================
# 68. ONE-PARAMETER WORKFLOW
# ============================================================

"""
Choose Parameter
      ↓
Hold Other Conditions Constant
      ↓
Run Sweep
      ↓
Plot Response
      ↓
Calculate Local Sensitivity
      ↓
Compare with Baseline
      ↓
Identify Important Region
      ↓
Refine if Needed
"""


# ============================================================
# 69. TWO-PARAMETER WORKFLOW
# ============================================================

"""
Parameter X
      ×
Parameter Y
      ↓
Evaluate Response
      ↓
Long-Form DataFrame
      ↓
Pivot Table
      ↓
Heatmap
      ↓
Contour
      ↓
3D Surface
      ↓
Engineering Interpretation
"""


# ============================================================
# 70. CONSTRAINT WORKFLOW
# ============================================================

"""
Engineering Requirements
        ↓
Efficiency Minimum
Temperature Maximum
Loss Maximum
EMI Reduction Minimum
        ↓
Boolean Masks
        ↓
Feasible Region
        ↓
Feasible Candidate Set
"""


# ============================================================
# 71. MULTI-OBJECTIVE WORKFLOW
# ============================================================

"""
Feasible Cases
      ↓
Define Objective Direction
      ↓
Efficiency ↑
Loss ↓
Temperature ↓
EMI Reduction ↑
      ↓
Pareto Analysis
      +
Optional Weighted Score
      ↓
Candidate Ranking
      ↓
Engineering Selection
"""


# ============================================================
# 72. ROBUSTNESS WORKFLOW
# ============================================================

"""
Nominal Candidate
      ↓
Define Variation Model
      ↓
Monte Carlo Samples
      ↓
Recalculate Responses
      ↓
Evaluate Constraints
      ↓
Distribution Statistics
      ↓
Robustness Assessment
      ↓
Validate with Realistic Tolerances
"""


# ============================================================
# 73. COMPLETE RESEARCH WORKFLOW
# ============================================================

"""
Simulation / Experiment
        ↓
Raw Parameter Cases
        ↓
Validate Data
        ↓
One-Parameter Sensitivity
        ↓
Two-Parameter Sweep
        ↓
Heatmap / Contour / 3D
        ↓
Baseline Comparison
        ↓
Engineering Constraints
        ↓
Feasible Region
        ↓
Best Sampled Cases
        ↓
Pareto / Weighted Tradeoff
        ↓
Robustness Analysis
        ↓
Candidate Selection
        ↓
Additional Simulation / Experiment
        ↓
Validation
        ↓
Publication Figure
"""


# ============================================================
# 74. FINAL CHECKLIST
# ============================================================

"""
Before publishing a parameter-sweep result, check:

PARAMETERS
------------------------------------------------------------
What was swept?
What was held constant?
What range was used?
What step/resolution was used?

DATA
------------------------------------------------------------
Measured?
Simulated?
Analytical?
ML predicted?
Interpolated?

UNITS
------------------------------------------------------------
Are all parameter and response units shown?

SENSITIVITY
------------------------------------------------------------
Is the sensitivity definition stated?
Are derivative units correct?

BASELINE
------------------------------------------------------------
Is the reference case defined?

LINEAR CHANGE
------------------------------------------------------------
Absolute difference?
Relative percentage?
Percentage points?

LOG QUANTITIES
------------------------------------------------------------
Are dB differences treated correctly?

MAPS
------------------------------------------------------------
Are colormap limits appropriate?
Are comparable maps using comparable scales?

OPTIMUM
------------------------------------------------------------
Is it described as best sampled point when appropriate?

CONSTRAINTS
------------------------------------------------------------
Are thresholds documented?

MULTI-OBJECTIVE
------------------------------------------------------------
Are objective directions clear?
Are score weights visible?

PARETO
------------------------------------------------------------
Is Pareto analysis described as a tradeoff set rather than
one automatic winner?

ROBUSTNESS
------------------------------------------------------------
What variation distribution was assumed?
How many samples were used?
Is the result being interpreted within those assumptions?

OUTPUT
------------------------------------------------------------
Were processed tables saved?
Were publication figures saved?
Can the result be reproduced?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
ENGINEERING PARAMETER-SWEEP VISUALIZATION

1. ONE-PARAMETER SWEEP
------------------------------------------------------------
Change one parameter while holding other conditions fixed.

2. TWO-PARAMETER SWEEP
------------------------------------------------------------
Parameter X × Parameter Y → Response Z.

3. LONG-FORM DATA
------------------------------------------------------------
Store each evaluated parameter combination as one row.

4. PIVOT TABLE
------------------------------------------------------------
Use pivot_table() to convert long-form data into a 2D
response matrix, especially when repeated combinations may
need aggregation.

5. HEATMAP
------------------------------------------------------------
pcolormesh() is useful for compact response maps.

6. CONTOUR
------------------------------------------------------------
contourf() visualizes equal-response regions and is often
excellent for engineering design-space interpretation.

7. 3D SURFACE
------------------------------------------------------------
plot_surface() provides geometric intuition but does not
replace precise 2D analysis.

8. LOCAL SENSITIVITY
------------------------------------------------------------
np.gradient(y, x) estimates dy/dx numerically.

9. NORMALIZED SENSITIVITY
------------------------------------------------------------
S = (x/y) dy/dx can provide a dimensionless local measure
when mathematically and physically appropriate.

10. BASELINE COMPARISON
------------------------------------------------------------
Use one clearly defined reference case.

11. PERCENTAGE POINTS
------------------------------------------------------------
94% → 95% = +1 percentage point.

12. RELATIVE PERCENT
------------------------------------------------------------
(95 - 94) / 94 × 100 ≈ 1.06%.

13. dB DIFFERENCE
------------------------------------------------------------
100 dBµV → 90 dBµV = 10 dB reduction, not automatically
10%.

14. BEST SAMPLED POINT
------------------------------------------------------------
idxmax(), idxmin(), argmax(), and argmin() search the
available sampled cases.

15. GLOBAL OPTIMUM
------------------------------------------------------------
A finite sweep does not by itself establish the global
continuous optimum.

16. CONSTRAINTS
------------------------------------------------------------
Build Boolean masks for engineering requirements.

17. FEASIBLE REGION
------------------------------------------------------------
Combine mandatory constraints before ranking candidates.

18. NORMALIZATION
------------------------------------------------------------
Different units can be mapped to dimensionless scores, but
the method changes interpretation.

19. WEIGHTED SCORE
------------------------------------------------------------
Weighted rankings are preference-dependent. State weights.

20. PARETO ANALYSIS
------------------------------------------------------------
Pareto-optimal sampled points represent nondominated
tradeoffs among objectives.

21. ROBUSTNESS
------------------------------------------------------------
Perturb candidate parameters and evaluate how often the
assumed samples satisfy the defined constraints.

22. MONTE CARLO CAUTION
------------------------------------------------------------
The result depends on the assumed variation model. It is
not automatically a general reliability probability.

23. PUBLICATION
------------------------------------------------------------
A strong final figure may combine:
(a) sensitivity curve,
(b) contour map,
(c) feasible region,
(d) Pareto tradeoff.

24. SAVE DATA
------------------------------------------------------------
Export:
- full sweep
- ranking
- Pareto set
- robustness summary
- selected candidates

25. MOST IMPORTANT PRINCIPLE
------------------------------------------------------------
Parameter-sweep visualization should support an engineering
decision, not only produce attractive figures.

26. COMPLETE PIPELINE
------------------------------------------------------------
Parameters
    ↓
Sweep
    ↓
Validate
    ↓
Sensitivity
    ↓
Visualize
    ↓
Compare Baseline
    ↓
Apply Constraints
    ↓
Identify Tradeoffs
    ↓
Rank Candidates
    ↓
Test Robustness
    ↓
Validate Physically
    ↓
Publish

------------------------------------------------------------

ADVANCED DATA VISUALIZATION SECTION COMPLETE

Files 22–33 now cover:

22  Histograms and distributions
23  Box and violin plots
24  Heatmaps and correlation maps
25  Contour and parameter-sweep plots
26  Inset and zoomed plots
27  Multi-panel publication figures
28  Confidence bands and shaded regions
29  Broken axes and discontinuous ranges
30  Automatic batch plotting
31  3D engineering plots
32  Interactive plotting
33  Engineering parameter-sweep visualization

NEXT REPOSITORY STEP:

Review and update:

02_Data_Visualization/README.md

and

02_Data_Visualization/CONCEPTS_AND_USE_CASES.md

so that the complete 01–33 visualization section has a
clear learning order, concept map, and engineering-use-case
index.
"""
