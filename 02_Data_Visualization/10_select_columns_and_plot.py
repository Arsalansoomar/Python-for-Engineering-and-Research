"""
============================================================
Python for Engineering and Research
10 - Select Columns and Plot
============================================================

Purpose:
    Demonstrate different methods for selecting specific
    columns from CSV and Excel datasets before plotting.

Topics:
    1. Why column selection is important
    2. Required libraries
    3. Load CSV data
    4. Inspect available columns
    5. Select one column by name
    6. Select multiple columns by name
    7. Select columns using loc
    8. Select columns using iloc
    9. Select columns by numerical position
    10. Select column ranges
    11. Choose X independently from Y
    12. Plot 2, 3, or many selected columns
    13. Select columns using patterns
    14. Automatically detect columns
    15. Read only required CSV columns
    16. Read only required Excel columns
    17. Select Excel columns by letter
    18. Safe column validation
    19. Reusable plotting function
    20. Common mistakes
    21. Key takeaways

Sample Files:
    sample_data/voltage_current.csv

    sample_data/converter_measurements.xlsx

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHY IS COLUMN SELECTION IMPORTANT?
# ============================================================

"""
Real engineering datasets may contain many columns.

Example:

Time
Input Voltage
Output Voltage
Input Current
Output Current
Power
Temperature
Efficiency
Frequency
Case A
Case B
Case C
...


Usually we do NOT need every column for every figure.

Example research question:

"How does voltage change with time?"


Required columns:

Time
Voltage


Everything else can be ignored for that figure.


Therefore:

Large Dataset
     ↓
Inspect Columns
     ↓
Select Required Variables
     ↓
Plot
"""


# ============================================================
# 2. REQUIRED LIBRARIES
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path


# ============================================================
# 3. LOCATE SAMPLE FILES
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


csv_file = (
    script_folder
    / "sample_data"
    / "voltage_current.csv"
)


excel_file = (
    script_folder
    / "sample_data"
    / "converter_measurements.xlsx"
)


# ============================================================
# 4. CHECK FILES
# ============================================================

if not csv_file.exists():

    raise FileNotFoundError(
        f"CSV file not found:\n"
        f"{csv_file}"
    )


if not excel_file.exists():

    raise FileNotFoundError(
        f"Excel file not found:\n"
        f"{excel_file}"
    )


# ============================================================
# 5. LOAD CSV DATA
# ============================================================

data = pd.read_csv(
    csv_file
)


# ============================================================
# 6. INSPECT AVAILABLE COLUMNS
# ============================================================

"""
Before selecting columns:

ALWAYS inspect the dataset.
"""


print(
    "\n--- Available CSV Columns ---"
)


print(
    data.columns.tolist()
)


print(
    "\n--- First Five Rows ---"
)


print(
    data.head()
)


# ============================================================
# 7. SAMPLE CSV COLUMNS
# ============================================================

"""
The sample CSV contains:

Time_s

Voltage_V

Current_A

Power_W
"""


# ============================================================
# 8. SELECT ONE COLUMN BY NAME
# ============================================================

"""
The most common method:

data["Column_Name"]
"""


voltage = data[
    "Voltage_V"
]


print(
    "\n--- Voltage Column ---"
)


print(
    voltage.head()
)


# ============================================================
# 9. SELECT X AND Y COLUMNS
# ============================================================

time = data[
    "Time_s"
]


voltage = data[
    "Voltage_V"
]


# ============================================================
# 10. BASIC PLOT OF SELECTED COLUMNS
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time,
    voltage,
    linewidth=2
)


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Selected CSV Columns"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 11. SELECT MULTIPLE COLUMNS BY NAME
# ============================================================

"""
To select several columns, use a list.

Important:

One column:

data["Voltage_V"]


Several columns:

data[
    [
        "Voltage_V",
        "Current_A"
    ]
]
"""


selected_columns = [

    "Voltage_V",

    "Current_A"

]


selected_data = data[
    selected_columns
]


print(
    "\n--- Selected Multiple Columns ---"
)


print(
    selected_data.head()
)


# ============================================================
# 12. SELECT THREE COLUMNS
# ============================================================

selected_columns = [

    "Voltage_V",

    "Current_A",

    "Power_W"

]


selected_data = data[
    selected_columns
]


print(
    "\n--- Three Selected Columns ---"
)


print(
    selected_data.head()
)


# ============================================================
# 13. SELECT X PLUS SEVERAL Y COLUMNS
# ============================================================

"""
A useful structure is:

X column:

Time_s


Y columns:

Voltage_V
Current_A
Power_W
"""


x_column = "Time_s"


y_columns = [

    "Voltage_V",

    "Current_A",

    "Power_W"

]


# ============================================================
# 14. SELECT ALL REQUIRED COLUMNS
# ============================================================

required_columns = [

    x_column

] + y_columns


selected_data = data[
    required_columns
]


print(
    "\n--- X + Y Columns ---"
)


print(
    selected_data.head()
)


# ============================================================
# 15. SELECT USING .loc
# ============================================================

"""
.loc selects data primarily using LABELS.

General structure:

data.loc[
    rows,
    columns
]


Example:

All rows

and selected columns.
"""


loc_selected = data.loc[
    :,
    [
        "Time_s",
        "Voltage_V",
        "Current_A"
    ]
]


print(
    "\n--- Selection Using loc ---"
)


print(
    loc_selected.head()
)


# ============================================================
# 16. SELECT COLUMN RANGE USING .loc
# ============================================================

"""
.loc can also select a range of column names.

Important:

The ending column is INCLUDED.
"""


loc_range = data.loc[
    :,
    "Time_s":"Current_A"
]


print(
    "\n--- Column Range Using loc ---"
)


print(
    loc_range.head()
)


# ============================================================
# 17. SELECT USING .iloc
# ============================================================

"""
.iloc selects data using INTEGER POSITIONS.

General structure:

data.iloc[
    rows,
    columns
]


Python indexing starts at:

0


Therefore:

Column 0
    First column

Column 1
    Second column

Column 2
    Third column
"""


print(
    "\n--- Column Positions ---"
)


for index, column in enumerate(
    data.columns
):

    print(
        index,
        column
    )


# ============================================================
# 18. SELECT FIRST COLUMN USING iloc
# ============================================================

first_column = data.iloc[
    :,
    0
]


print(
    "\n--- First Column Using iloc ---"
)


print(
    first_column.head()
)


# ============================================================
# 19. SELECT THIRD COLUMN
# ============================================================

third_column = data.iloc[
    :,
    2
]


print(
    "\n--- Third Column ---"
)


print(
    third_column.head()
)


# ============================================================
# 20. SELECT MULTIPLE COLUMNS BY POSITION
# ============================================================

"""
Suppose we want:

Column 0

Column 1

Column 3


Use:
"""


position_selected = data.iloc[
    :,
    [
        0,
        1,
        3
    ]
]


print(
    "\n--- Selected by Position ---"
)


print(
    position_selected.head()
)


# ============================================================
# 21. SELECT COLUMN RANGE USING iloc
# ============================================================

"""
Python slicing:

start:end


IMPORTANT:

The ending position is NOT included.


Example:

0:3

selects:

0
1
2
"""


first_three_columns = data.iloc[
    :,
    0:3
]


print(
    "\n--- First Three Columns ---"
)


print(
    first_three_columns.head()
)


# ============================================================
# 22. loc VS iloc
# ============================================================

"""
loc

Uses:

COLUMN NAMES / LABELS


Example:

data.loc[
    :,
    [
        "Time_s",
        "Voltage_V"
    ]
]


------------------------------------------------------------


iloc

Uses:

COLUMN POSITIONS


Example:

data.iloc[
    :,
    [
        0,
        1
    ]
]


------------------------------------------------------------


Practical rule:

If you know the column names:

Use names.


If you only know positions:

Use iloc.
"""


# ============================================================
# 23. SELECT X BY NAME AND Y BY NAME
# ============================================================

"""
A clear engineering plotting structure is:

Define X separately.

Define Y separately.
"""


x_column = "Time_s"

y_column = "Power_W"


x = data[
    x_column
]


y = data[
    y_column
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    x,
    y,
    linewidth=2
)


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Power [W]"
)

ax.set_title(
    "Power vs Time"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 24. CHANGE PLOT WITHOUT CHANGING MAIN CODE
# ============================================================

"""
This is useful because only these variables need to change:

x_column

y_column
"""


x_column = "Time_s"

y_column = "Current_A"


x_label = "Time [s]"

y_label = "Current [A]"


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    data[x_column],
    data[y_column],
    linewidth=2
)


ax.set_xlabel(
    x_label
)

ax.set_ylabel(
    y_label
)


ax.set_title(
    f"{y_column} vs {x_column}"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 25. PLOT MULTIPLE SELECTED COLUMNS
# ============================================================

"""
Suppose several selected columns have compatible units.

In this synthetic example, we demonstrate the programming
method.

Always check physical units before combining variables on
the same axis.
"""


selected_y_columns = [

    "Voltage_V",

    "Current_A",

    "Power_W"

]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for column in selected_y_columns:

    ax.plot(
        data["Time_s"],
        data[column],
        label=column
    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Mixed Units"
)

ax.set_title(
    "Selected CSV Variables"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 26. IMPORTANT - DIFFERENT UNITS
# ============================================================

"""
The previous example demonstrates automatic column
selection.

However:

Voltage [V]

Current [A]

Power [W]

have different units.


Therefore a scientific figure should normally use:

Subplots

Separate figures

Dual Y-axis

or normalization.


For different physical units, subplots are often clearer.
"""


# ============================================================
# 27. AUTOMATIC SUBPLOTS FOR SELECTED COLUMNS
# ============================================================

axis_labels = {

    "Voltage_V":
        "Voltage [V]",

    "Current_A":
        "Current [A]",

    "Power_W":
        "Power [W]"

}


selected_y_columns = [

    "Voltage_V",

    "Current_A",

    "Power_W"

]


number_of_plots = len(
    selected_y_columns
)


fig, axes = plt.subplots(
    number_of_plots,
    1,
    figsize=(
        7,
        2.5 * number_of_plots
    ),
    sharex=True
)


if number_of_plots == 1:

    axes = [
        axes
    ]


for ax, column in zip(
    axes,
    selected_y_columns
):

    ax.plot(
        data["Time_s"],
        data[column],
        linewidth=2
    )


    ax.set_ylabel(
        axis_labels.get(
            column,
            column
        )
    )


    ax.grid(
        True
    )


axes[-1].set_xlabel(
    "Time [s]"
)


fig.suptitle(
    "Selected Engineering Variables"
)


plt.tight_layout()

plt.show()


# ============================================================
# 28. SELECT COLUMNS CONTAINING A WORD
# ============================================================

"""
Large datasets may contain columns such as:

Input_Voltage_V

Output_Voltage_V

Gate_Voltage_V

DC_Link_Voltage_V


Instead of manually entering every column, search by
column-name pattern.
"""


voltage_columns = [

    column

    for column in data.columns

    if "Voltage" in column

]


print(
    "\n--- Columns Containing 'Voltage' ---"
)


print(
    voltage_columns
)


# ============================================================
# 29. SELECT COLUMNS CONTAINING "Current"
# ============================================================

current_columns = [

    column

    for column in data.columns

    if "Current" in column

]


print(
    "\n--- Columns Containing 'Current' ---"
)


print(
    current_columns
)


# ============================================================
# 30. CASE-INSENSITIVE COLUMN SEARCH
# ============================================================

"""
Sometimes capitalization is inconsistent.

For example:

Voltage

voltage

VOLTAGE


Use:

.lower()
"""


search_word = "power"


matching_columns = [

    column

    for column in data.columns

    if search_word.lower()
    in column.lower()

]


print(
    "\n--- Case-Insensitive Search ---"
)


print(
    matching_columns
)


# ============================================================
# 31. SELECT COLUMNS STARTING WITH TEXT
# ============================================================

"""
Example:

Case_A
Case_B
Case_C


Use:

startswith()
"""


example_columns = [

    "Time",

    "Case_A",

    "Case_B",

    "Case_C",

    "Temperature"

]


case_columns = [

    column

    for column in example_columns

    if column.startswith(
        "Case_"
    )

]


print(
    "\n--- Columns Starting with Case_ ---"
)


print(
    case_columns
)


# ============================================================
# 32. SELECT COLUMNS ENDING WITH UNIT
# ============================================================

"""
Column names can also encode units.

Example:

Input_Voltage_V

Output_Voltage_V


Columns ending in:

_V

may represent voltage.
"""


columns_ending_v = [

    column

    for column in data.columns

    if column.endswith(
        "_V"
    )

]


print(
    "\n--- Columns Ending with _V ---"
)


print(
    columns_ending_v
)


# ============================================================
# 33. PANDAS filter()
# ============================================================

"""
Pandas also provides:

DataFrame.filter()


For example:

like="Voltage"
"""


voltage_filtered = data.filter(
    like="Voltage"
)


print(
    "\n--- Pandas filter(like='Voltage') ---"
)


print(
    voltage_filtered.head()
)


# ============================================================
# 34. REGEX-BASED COLUMN SELECTION
# ============================================================

"""
More advanced selection can use regular expressions.

Example:

Select columns containing:

Voltage

or

Current
"""


electrical_columns = data.filter(
    regex="Voltage|Current"
)


print(
    "\n--- Voltage or Current Columns ---"
)


print(
    electrical_columns.head()
)


# ============================================================
# 35. READ ONLY REQUIRED CSV COLUMNS
# ============================================================

"""
Instead of loading the complete CSV and selecting later,
Pandas can load only required columns.

This can save memory for large datasets.
"""


csv_subset = pd.read_csv(

    csv_file,

    usecols=[
        "Time_s",
        "Voltage_V"
    ]

)


print(
    "\n--- CSV Loaded with usecols ---"
)


print(
    csv_subset.head()
)


# ============================================================
# 36. CSV usecols BY POSITION
# ============================================================

"""
pd.read_csv() can also select columns by integer position.

Example:

Columns 0 and 2.
"""


csv_position_subset = pd.read_csv(

    csv_file,

    usecols=[
        0,
        2
    ]

)


print(
    "\n--- CSV Columns 0 and 2 ---"
)


print(
    csv_position_subset.head()
)


# ============================================================
# 37. LOAD EXCEL DATA
# ============================================================

excel_data = pd.read_excel(

    excel_file,

    sheet_name="Time_Domain"

)


print(
    "\n--- Excel Columns ---"
)


print(
    excel_data.columns.tolist()
)


# ============================================================
# 38. SELECT EXCEL COLUMNS BY NAME
# ============================================================

excel_selected = excel_data[
    [
        "Time_s",
        "Output_Voltage_V",
        "Output_Current_A"
    ]
]


print(
    "\n--- Selected Excel Columns ---"
)


print(
    excel_selected.head()
)


# ============================================================
# 39. READ ONLY SELECTED EXCEL COLUMNS
# ============================================================

"""
usecols works with pd.read_excel() as well.
"""


excel_subset = pd.read_excel(

    excel_file,

    sheet_name="Time_Domain",

    usecols=[
        "Time_s",
        "Output_Voltage_V",
        "Temperature_C"
    ]

)


print(
    "\n--- Excel usecols by Name ---"
)


print(
    excel_subset.head()
)


# ============================================================
# 40. SELECT EXCEL COLUMNS BY LETTER
# ============================================================

"""
Excel-style column letters can be used.

Example:

A:C

means:

A
B
C
"""


excel_a_to_c = pd.read_excel(

    excel_file,

    sheet_name="Time_Domain",

    usecols="A:C"

)


print(
    "\n--- Excel Columns A:C ---"
)


print(
    excel_a_to_c.head()
)


# ============================================================
# 41. SELECT NON-CONSECUTIVE EXCEL COLUMN LETTERS
# ============================================================

"""
Excel also supports non-contiguous ranges.

Example:

A,C,E
"""


excel_non_contiguous = pd.read_excel(

    excel_file,

    sheet_name="Time_Domain",

    usecols="A,C,E"

)


print(
    "\n--- Excel Columns A, C and E ---"
)


print(
    excel_non_contiguous.head()
)


# ============================================================
# 42. EXCEL POSITION SELECTION AFTER LOADING
# ============================================================

"""
After loading the workbook, iloc can be used exactly like
it was used for CSV data.
"""


excel_by_position = excel_data.iloc[
    :,
    [
        0,
        2,
        4
    ]
]


print(
    "\n--- Excel Columns by Position ---"
)


print(
    excel_by_position.head()
)


# ============================================================
# 43. PLOT SELECTED EXCEL COLUMNS
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    excel_data["Time_s"],
    excel_data["Input_Voltage_V"],
    label="Input Voltage"
)


ax.plot(
    excel_data["Time_s"],
    excel_data["Output_Voltage_V"],
    label="Output Voltage"
)


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Selected Excel Voltage Columns"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 44. SELECT ALL VOLTAGE COLUMNS AUTOMATICALLY
# ============================================================

excel_voltage_columns = [

    column

    for column in excel_data.columns

    if "Voltage" in column

]


print(
    "\n--- Excel Voltage Columns ---"
)


print(
    excel_voltage_columns
)


# ============================================================
# 45. AUTOMATIC VOLTAGE PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for column in excel_voltage_columns:

    ax.plot(
        excel_data["Time_s"],
        excel_data[column],
        linewidth=2,
        label=column
    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Automatically Selected Voltage Columns"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 46. REMOVE X COLUMN FROM AUTOMATIC SEARCH
# ============================================================

"""
Sometimes a pattern search may accidentally include the
X-axis column.

It can be excluded explicitly.
"""


x_column = "Time_s"


selected_columns = [

    column

    for column in excel_data.columns

    if "Voltage" in column

    and column != x_column

]


# ============================================================
# 47. COLUMN VALIDATION FUNCTION
# ============================================================

def validate_columns(
    dataframe,
    columns
):
    """
    Check whether requested columns exist.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Dataset containing columns.

    columns : list
        Required column names.

    Raises
    ------
    KeyError
        If one or more columns are missing.
    """

    missing_columns = [

        column

        for column in columns

        if column not in dataframe.columns

    ]


    if missing_columns:

        raise KeyError(
            f"\nMissing columns:"
            f"\n{missing_columns}"
            f"\n\nAvailable columns:"
            f"\n{dataframe.columns.tolist()}"
        )


# ============================================================
# 48. TEST COLUMN VALIDATION
# ============================================================

validate_columns(

    data,

    [
        "Time_s",
        "Voltage_V"
    ]

)


# ============================================================
# 49. REUSABLE MULTI-COLUMN PLOT FUNCTION
# ============================================================

def plot_selected_columns(
    dataframe,
    x_column,
    y_columns,
    x_label,
    y_label,
    title
):
    """
    Plot several selected Y columns against one X column.

    This function is intended for variables with compatible
    physical units.
    """

    required_columns = [

        x_column

    ] + y_columns


    validate_columns(
        dataframe,
        required_columns
    )


    fig, ax = plt.subplots(
        figsize=(7, 4.5)
    )


    for column in y_columns:

        ax.plot(
            dataframe[
                x_column
            ],
            dataframe[
                column
            ],
            linewidth=2,
            label=column
        )


    ax.set_xlabel(
        x_label
    )

    ax.set_ylabel(
        y_label
    )

    ax.set_title(
        title
    )


    ax.grid(
        True
    )

    ax.legend()


    plt.tight_layout()

    plt.show()


# ============================================================
# 50. USE FUNCTION WITH EXCEL DATA
# ============================================================

plot_selected_columns(

    dataframe=excel_data,

    x_column="Time_s",

    y_columns=[
        "Input_Voltage_V",
        "Output_Voltage_V"
    ],

    x_label="Time [s]",

    y_label="Voltage [V]",

    title="Input and Output Voltage"

)


# ============================================================
# 51. REUSABLE SUBPLOT FUNCTION
# ============================================================

"""
For variables with different units, use separate subplots.
"""


def plot_selected_subplots(
    dataframe,
    x_column,
    y_columns,
    axis_labels,
    x_label,
    title
):
    """
    Plot multiple selected columns on independent Y-axes
    arranged vertically.
    """

    required_columns = [

        x_column

    ] + y_columns


    validate_columns(
        dataframe,
        required_columns
    )


    number_of_plots = len(
        y_columns
    )


    if number_of_plots == 0:

        raise ValueError(
            "At least one Y column must be selected."
        )


    if len(
        axis_labels
    ) != number_of_plots:

        raise ValueError(
            "The number of axis labels must match "
            "the number of Y columns."
        )


    fig, axes = plt.subplots(

        number_of_plots,

        1,

        figsize=(
            7,
            2.5 * number_of_plots
        ),

        sharex=True

    )


    if number_of_plots == 1:

        axes = [
            axes
        ]


    for ax, column, label in zip(

        axes,

        y_columns,

        axis_labels

    ):

        ax.plot(
            dataframe[
                x_column
            ],
            dataframe[
                column
            ],
            linewidth=2
        )


        ax.set_ylabel(
            label
        )

        ax.grid(
            True
        )


    axes[-1].set_xlabel(
        x_label
    )


    fig.suptitle(
        title
    )


    plt.tight_layout()

    plt.show()


# ============================================================
# 52. USE SUBPLOT FUNCTION
# ============================================================

plot_selected_subplots(

    dataframe=excel_data,

    x_column="Time_s",

    y_columns=[

        "Output_Voltage_V",

        "Output_Current_A",

        "Temperature_C"

    ],

    axis_labels=[

        "Voltage [V]",

        "Current [A]",

        "Temperature [°C]"

    ],

    x_label="Time [s]",

    title="Selected Converter Variables"

)


# ============================================================
# 53. USER-DEFINED COLUMN LIST
# ============================================================

"""
One of the simplest reusable approaches is to keep all
column choices near the top of a script.

Example:
"""


X_COLUMN = "Time_s"


Y_COLUMNS = [

    "Input_Voltage_V",

    "Output_Voltage_V"

]


X_LABEL = "Time [s]"

Y_LABEL = "Voltage [V]"


# ============================================================
# 54. PLOT USER-DEFINED SELECTION
# ============================================================

plot_selected_columns(

    dataframe=excel_data,

    x_column=X_COLUMN,

    y_columns=Y_COLUMNS,

    x_label=X_LABEL,

    y_label=Y_LABEL,

    title="User-Selected Variables"

)


# ============================================================
# 55. SELECT COLUMN BY NUMBER ENTERED IN CODE
# ============================================================

"""
Sometimes the researcher knows:

"Plot column 3 against column 1"

rather than knowing the exact header name.
"""


x_position = 0

y_position = 2


x_column_name = data.columns[
    x_position
]


y_column_name = data.columns[
    y_position
]


print(
    "\n--- Position-Based Selection ---"
)


print(
    "X Column:",
    x_column_name
)


print(
    "Y Column:",
    y_column_name
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(

    data.iloc[
        :,
        x_position
    ],

    data.iloc[
        :,
        y_position
    ]

)


ax.set_xlabel(
    x_column_name
)

ax.set_ylabel(
    y_column_name
)

ax.set_title(
    "Position-Based Column Selection"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 56. CONVERT COLUMN POSITION TO COLUMN NAME
# ============================================================

"""
Useful operation:

column_name = data.columns[position]
"""


position = 1


column_name = data.columns[
    position
]


print(
    "\nColumn at position",
    position,
    "=",
    column_name
)


# ============================================================
# 57. SELECT EVERY SECOND COLUMN
# ============================================================

"""
Python slicing can select columns at regular intervals.

Example:

0, 2, 4, 6, ...
"""


every_second_column = data.iloc[
    :,
    ::2
]


print(
    "\n--- Every Second Column ---"
)


print(
    every_second_column.head()
)


# ============================================================
# 58. SELECT ALL COLUMNS EXCEPT ONE
# ============================================================

"""
Sometimes we want every column except the X-axis.
"""


all_except_time = data.drop(
    columns=[
        "Time_s"
    ]
)


print(
    "\n--- All Columns Except Time ---"
)


print(
    all_except_time.head()
)


# ============================================================
# 59. SELECT NUMERICAL COLUMNS ONLY
# ============================================================

"""
Large datasets may contain:

Numerical columns

Text labels

Dates

Comments


Pandas can select only numerical columns.
"""


numeric_data = data.select_dtypes(
    include="number"
)


print(
    "\n--- Numerical Columns ---"
)


print(
    numeric_data.columns.tolist()
)


# ============================================================
# 60. CLEAN COLUMN NAMES
# ============================================================

"""
Instrument exports sometimes contain spaces:

" Voltage_V "

instead of:

"Voltage_V"


Clean them using:
"""


clean_data = data.copy()


clean_data.columns = (

    clean_data.columns

    .str.strip()

)


# ============================================================
# 61. SAVE FINAL SELECTED DATASET
# ============================================================

"""
Selected columns can be saved as a new CSV.

This is useful when creating a smaller processed dataset.
"""


output_data_folder = (
    script_folder
    / "output_data"
)


output_data_folder.mkdir(
    exist_ok=True
)


columns_to_save = [

    "Time_s",

    "Voltage_V",

    "Current_A"

]


selected_output = data[
    columns_to_save
]


output_csv = (
    output_data_folder
    / "selected_columns.csv"
)


selected_output.to_csv(
    output_csv,
    index=False
)


print(
    "\nSelected dataset saved to:"
)


print(
    output_csv
)


# ============================================================
# 62. SAVE FINAL FIGURE
# ============================================================

output_figure_folder = (
    script_folder
    / "output_figures"
)


output_figure_folder.mkdir(
    exist_ok=True
)


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for column in [

    "Input_Voltage_V",

    "Output_Voltage_V"

]:

    ax.plot(
        excel_data["Time_s"],
        excel_data[column],
        linewidth=2,
        label=column
    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Selected Excel Variables"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()


png_file = (
    output_figure_folder
    / "selected_columns_plot.png"
)


pdf_file = (
    output_figure_folder
    / "selected_columns_plot.pdf"
)


svg_file = (
    output_figure_folder
    / "selected_columns_plot.svg"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
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
# 63. COMMON MISTAKE - ONE BRACKET VS TWO
# ============================================================

"""
ONE COLUMN:

data[
    "Voltage_V"
]


returns a Pandas Series.


MULTIPLE COLUMNS:

data[
    [
        "Voltage_V",
        "Current_A"
    ]
]


returns a DataFrame.


The inner list is required when selecting multiple
columns.
"""


# ============================================================
# 64. COMMON MISTAKE - loc VS iloc
# ============================================================

"""
Incorrect idea:

data.iloc[
    :,
    "Voltage_V"
]


iloc expects an integer position.


Correct:

data.iloc[
    :,
    1
]


or:

data.loc[
    :,
    "Voltage_V"
]
"""


# ============================================================
# 65. COMMON MISTAKE - PYTHON INDEXING STARTS AT ZERO
# ============================================================

"""
Python:

0 = First column

1 = Second column

2 = Third column

3 = Fourth column


Therefore:

data.iloc[
    :,
    2
]


selects the THIRD column.
"""


# ============================================================
# 66. COMMON MISTAKE - iloc RANGE END IS EXCLUDED
# ============================================================

"""
Example:

data.iloc[
    :,
    0:3
]


selects:

0
1
2


It does NOT select column 3.
"""


# ============================================================
# 67. COMMON MISTAKE - loc RANGE END IS INCLUDED
# ============================================================

"""
Unlike iloc slicing:

data.loc[
    :,
    "Time_s":"Current_A"
]


includes both:

Time_s

and

Current_A

assuming the columns are ordered accordingly.
"""


# ============================================================
# 68. COMMON MISTAKE - WRONG COLUMN ORDER
# ============================================================

"""
Column positions may change when a new CSV or Excel file
is exported.

Example:

Old file:

0 Time
1 Voltage
2 Current


New file:

0 Sample
1 Time
2 Voltage
3 Current


A script using:

iloc[:, 1]

may now select Time instead of Voltage.


For reproducible research, selecting by meaningful column
name is often safer than selecting only by position.
"""


# ============================================================
# 69. COMMON MISTAKE - PLOTTING ALL COLUMNS
# ============================================================

"""
Avoid:

for column in data.columns:

    ax.plot(
        data["Time_s"],
        data[column]
    )


because:

Time itself may be plotted as Y.

Different physical units may be mixed.

Unnecessary variables may clutter the figure.


Select variables intentionally.
"""


# ============================================================
# 70. COMMON MISTAKE - MIXING UNITS
# ============================================================

"""
Selected columns:

Voltage_V

Current_A

Power_W


do NOT become scientifically compatible simply because
Python can plot them together.

Check:

Physical quantity

Unit

Scale

Research question


before choosing the visualization method.
"""


# ============================================================
# 71. COLUMN-SELECTION DECISION
# ============================================================

"""
Do I know the column name?
        |
       Yes
        ↓
Use:
data["Column"]


Do I need several named columns?
        |
       Yes
        ↓
Use:
data[
    ["A", "B", "C"]
]


Do I know only the column position?
        |
       Yes
        ↓
Use:
data.iloc[:, position]


Do I need a label-based range?
        |
       Yes
        ↓
Use:
data.loc[:, "A":"D"]


Do I need a position-based range?
        |
       Yes
        ↓
Use:
data.iloc[:, 0:4]


Do many columns share a keyword?
        |
       Yes
        ↓
Use:
filter()
or
list comprehension
"""


# ============================================================
# 72. PRACTICAL ENGINEERING EXAMPLE
# ============================================================

"""
Suppose an Excel file contains:

Time_s
Input_Voltage_V
Output_Voltage_V
Input_Current_A
Output_Current_A
Input_Power_W
Output_Power_W
Efficiency_percent
Temperature_C


Question 1:

Compare input and output voltage.

Select:

Time_s
Input_Voltage_V
Output_Voltage_V


------------------------------------------------------------


Question 2:

Analyze device temperature.

Select:

Time_s
Temperature_C


------------------------------------------------------------


Question 3:

Compare input and output power.

Select:

Time_s
Input_Power_W
Output_Power_W


------------------------------------------------------------


Question 4:

Plot several variables with different units.

Select:

Output_Voltage_V
Output_Current_A
Temperature_C


Then use:

SUBPLOTS

instead of placing everything on one Y-axis.
"""


# ============================================================
# 73. COMPLETE DATA-SELECTION PIPELINE
# ============================================================

"""
CSV / Excel
     ↓
Read File
     ↓
Inspect Column Names
     ↓
Understand Physical Units
     ↓
Define Research Question
     ↓
Choose X Variable
     ↓
Choose Y Variable(s)
     ↓
Select Columns
     ↓
Check Missing Columns
     ↓
Check Data Types
     ↓
Plot
     ↓
Validate Interpretation
     ↓
Save Figure
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
SELECT COLUMNS AND PLOT


1. ONE COLUMN BY NAME

data[
    "Voltage_V"
]


------------------------------------------------------------


2. MULTIPLE COLUMNS BY NAME

data[
    [
        "Voltage_V",
        "Current_A"
    ]
]


------------------------------------------------------------


3. LABEL-BASED SELECTION

data.loc[
    :,
    [
        "Voltage_V",
        "Current_A"
    ]
]


------------------------------------------------------------


4. POSITION-BASED SELECTION

data.iloc[
    :,
    [
        1,
        2
    ]
]


------------------------------------------------------------


5. POSITION RANGE

data.iloc[
    :,
    0:3
]


selects:

0
1
2


------------------------------------------------------------


6. LABEL RANGE

data.loc[
    :,
    "Time_s":"Current_A"
]


The ending label is included.


------------------------------------------------------------


7. DEFINE X INDEPENDENTLY

x_column = "Time_s"


------------------------------------------------------------


8. DEFINE MULTIPLE Y VARIABLES

y_columns = [

    "Voltage_V",

    "Current_A",

    "Power_W"

]


------------------------------------------------------------


9. SELECT USING KEYWORD

voltage_columns = [

    column

    for column in data.columns

    if "Voltage" in column

]


------------------------------------------------------------


10. PANDAS FILTER

data.filter(
    like="Voltage"
)


------------------------------------------------------------


11. REGEX FILTER

data.filter(
    regex="Voltage|Current"
)


------------------------------------------------------------


12. CSV usecols

pd.read_csv(

    "data.csv",

    usecols=[
        "Time",
        "Voltage"
    ]

)


------------------------------------------------------------


13. EXCEL usecols BY NAME

pd.read_excel(

    "data.xlsx",

    usecols=[
        "Time",
        "Voltage"
    ]

)


------------------------------------------------------------


14. EXCEL usecols BY LETTER

pd.read_excel(

    "data.xlsx",

    usecols="A:C"

)


or:

pd.read_excel(

    "data.xlsx",

    usecols="A,C,E"

)


------------------------------------------------------------


15. SELECT NUMERICAL COLUMNS

data.select_dtypes(
    include="number"
)


------------------------------------------------------------


16. REMOVE ONE COLUMN

data.drop(
    columns=[
        "Time_s"
    ]
)


------------------------------------------------------------


17. MOST IMPORTANT PRACTICAL RULE

Column selection should be based on:

Research Question
       +
Physical Meaning
       +
Units
       +
Required Comparison


not simply:

"Plot every column in the file."


------------------------------------------------------------


18. RECOMMENDED WORKFLOW

Inspect
   ↓
Select
   ↓
Validate
   ↓
Plot
   ↓
Interpret


------------------------------------------------------------


NEXT:

11_multiple_csv_files.py


This will address another very common research problem:

"I have:

Case_A.csv
Case_B.csv
Case_C.csv
Case_D.csv

and I want to compare all of them automatically."


We will cover:

Multiple filenames
        ↓
Loop through CSV files
        ↓
Read each file
        ↓
Select same column
        ↓
Plot all cases
        ↓
Automatic labels
        ↓
glob() file discovery
        ↓
Different file lengths
        ↓
Different column names
        ↓
Subplots
        ↓
Automatic case comparison
        ↓
Publication-ready output
"""
