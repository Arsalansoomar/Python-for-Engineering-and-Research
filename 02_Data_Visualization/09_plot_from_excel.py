"""
============================================================
Python for Engineering and Research
09 - Plot Data from Excel
============================================================

Purpose:
    Demonstrate how engineering and research data stored
    in Excel workbooks can be loaded, inspected, selected,
    processed, visualized, and compared using Pandas and
    Matplotlib.

Topics:
    1. What is an Excel workbook?
    2. Required libraries
    3. Locate Excel file
    4. Inspect worksheet names
    5. Read one worksheet
    6. Inspect columns
    7. Select X and Y columns
    8. Plot one variable
    9. Plot several variables
    10. Use subplots for different units
    11. Select another worksheet
    12. Load-sweep plotting
    13. Frequency comparison worksheet
    14. Select specific columns using usecols
    15. Select rows using nrows
    16. Skip rows when required
    17. Read several sheets
    18. Automatic sheet selection
    19. Reusable plotting functions
    20. Save figures
    21. Common mistakes
    22. Key takeaways

Sample File:
    sample_data/converter_measurements.xlsx

Worksheets:
    Time_Domain
    Load_Sweep
    Case_Comparison

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT IS AN EXCEL WORKBOOK?
# ============================================================

"""
An Excel workbook normally uses the extension:

.xlsx


Unlike a CSV file, an Excel workbook can contain:

- Multiple worksheets
- Different tables
- Formulas
- Formatting
- Several experiments
- Several simulation cases
- Different operating conditions


Example:

converter_measurements.xlsx

        ↓

┌─────────────────────────────┐
│ Time_Domain                 │
├─────────────────────────────┤
│ Load_Sweep                  │
├─────────────────────────────┤
│ Case_Comparison             │
└─────────────────────────────┘


Therefore the general workflow is:

Excel Workbook
      ↓
Inspect Sheet Names
      ↓
Choose Worksheet
      ↓
Read Data
      ↓
Inspect Columns
      ↓
Choose X
      ↓
Choose Y
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
# 3. REQUIRED PACKAGE
# ============================================================

"""
Pandas normally uses openpyxl to read .xlsx files.

Install the required packages using:

pip install pandas matplotlib openpyxl


This command should normally be run in the terminal.
"""


# ============================================================
# 4. LOCATE THE EXCEL FILE
# ============================================================

"""
Repository structure:

02_Data_Visualization/
│
├── 09_plot_from_excel.py
│
└── sample_data/
    └── converter_measurements.xlsx
"""


script_folder = Path(
    __file__
).resolve().parent


excel_file = (
    script_folder
    / "sample_data"
    / "converter_measurements.xlsx"
)


print(
    "--- Excel File Path ---"
)

print(
    excel_file
)


# ============================================================
# 5. CHECK WHETHER FILE EXISTS
# ============================================================

if not excel_file.exists():

    raise FileNotFoundError(
        f"\nExcel file not found:\n"
        f"{excel_file}\n"
        "\nCheck that the sample_data folder contains "
        "converter_measurements.xlsx."
    )


print(
    "\nExcel file found successfully."
)


# ============================================================
# 6. OPEN EXCEL WORKBOOK
# ============================================================

"""
pd.ExcelFile() opens the workbook and allows us to inspect
available worksheet names before reading the actual data.
"""


workbook = pd.ExcelFile(
    excel_file
)


# ============================================================
# 7. DISPLAY WORKSHEET NAMES
# ============================================================

print(
    "\n--- Available Worksheets ---"
)


print(
    workbook.sheet_names
)


for sheet_name in workbook.sheet_names:

    print(
        sheet_name
    )


# ============================================================
# 8. WHY CHECK SHEET NAMES FIRST?
# ============================================================

"""
A common mistake is assuming that the worksheet is called:

Sheet1


when it may actually be called:

Time_Domain

Experimental Results

Case A

Test_01

FFT_Data


Always inspect:

workbook.sheet_names

when working with an unfamiliar Excel workbook.
"""


# ============================================================
# 9. READ ONE WORKSHEET
# ============================================================

"""
The Time_Domain worksheet contains:

Time
Input Voltage
Output Voltage
Input Current
Output Current
Power
Efficiency
Temperature
"""


time_data = pd.read_excel(
    excel_file,
    sheet_name="Time_Domain"
)


# ============================================================
# 10. DISPLAY FIRST ROWS
# ============================================================

print(
    "\n--- Time_Domain: First Five Rows ---"
)


print(
    time_data.head()
)


# ============================================================
# 11. CHECK DATASET SHAPE
# ============================================================

print(
    "\n--- Dataset Shape ---"
)


print(
    time_data.shape
)


print(
    "Rows:",
    time_data.shape[0]
)


print(
    "Columns:",
    time_data.shape[1]
)


# ============================================================
# 12. CHECK COLUMN NAMES
# ============================================================

"""
This is extremely important.

Always inspect the actual Excel column names before
attempting to select them.
"""


print(
    "\n--- Time_Domain Columns ---"
)


print(
    time_data.columns.tolist()
)


# ============================================================
# 13. CHECK DATA TYPES
# ============================================================

print(
    "\n--- Data Types ---"
)


print(
    time_data.dtypes
)


# ============================================================
# 14. DATASET INFORMATION
# ============================================================

print(
    "\n--- Dataset Information ---"
)


time_data.info()


# ============================================================
# 15. BASIC STATISTICS
# ============================================================

print(
    "\n--- Statistical Summary ---"
)


print(
    time_data.describe()
)


# ============================================================
# 16. EXPECTED Time_Domain COLUMNS
# ============================================================

"""
The sample workbook contains approximately:

Time_s

Input_Voltage_V

Output_Voltage_V

Input_Current_A

Output_Current_A

Input_Power_W

Output_Power_W

Efficiency_percent

Temperature_C
"""


# ============================================================
# 17. SELECT X AND Y COLUMNS
# ============================================================

time = time_data[
    "Time_s"
]


output_voltage = time_data[
    "Output_Voltage_V"
]


# ============================================================
# 18. BASIC EXCEL LINE PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time,
    output_voltage,
    linewidth=2
)


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Output Voltage [V]"
)

ax.set_title(
    "Output Voltage from Excel"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 19. INPUT AND OUTPUT VOLTAGE
# ============================================================

"""
Input and Output Voltage share the same physical unit.

Therefore they can reasonably be compared on the same
Y-axis.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_data["Time_s"],
    time_data["Input_Voltage_V"],
    linewidth=2,
    label="Input Voltage"
)


ax.plot(
    time_data["Time_s"],
    time_data["Output_Voltage_V"],
    linewidth=2,
    label="Output Voltage"
)


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Input and Output Voltage from Excel"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 20. INPUT AND OUTPUT CURRENT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    time_data["Time_s"],
    time_data["Input_Current_A"],
    linewidth=2,
    label="Input Current"
)


ax.plot(
    time_data["Time_s"],
    time_data["Output_Current_A"],
    linewidth=2,
    label="Output Current"
)


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Current [A]"
)

ax.set_title(
    "Input and Output Current from Excel"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 21. DIFFERENT PHYSICAL VARIABLES
# ============================================================

"""
Suppose we want:

Output Voltage [V]

Output Current [A]

Temperature [°C]


These variables should normally not share one ordinary
Y-axis because they have different physical units.

Subplots provide a clearer solution.
"""


fig, axes = plt.subplots(
    nrows=3,
    ncols=1,
    figsize=(7, 8),
    sharex=True
)


# Voltage

axes[0].plot(
    time_data["Time_s"],
    time_data["Output_Voltage_V"],
    linewidth=2
)

axes[0].set_ylabel(
    "Voltage [V]"
)

axes[0].grid(
    True
)


# Current

axes[1].plot(
    time_data["Time_s"],
    time_data["Output_Current_A"],
    linewidth=2
)

axes[1].set_ylabel(
    "Current [A]"
)

axes[1].grid(
    True
)


# Temperature

axes[2].plot(
    time_data["Time_s"],
    time_data["Temperature_C"],
    linewidth=2
)

axes[2].set_xlabel(
    "Time [s]"
)

axes[2].set_ylabel(
    "Temperature [°C]"
)

axes[2].grid(
    True
)


fig.suptitle(
    "Converter Time-Domain Measurements"
)


plt.tight_layout()

plt.show()


# ============================================================
# 22. READ ANOTHER WORKSHEET
# ============================================================

"""
Now read:

Load_Sweep
"""


load_data = pd.read_excel(
    excel_file,
    sheet_name="Load_Sweep"
)


print(
    "\n--- Load_Sweep Data ---"
)


print(
    load_data.head()
)


print(
    "\n--- Load_Sweep Columns ---"
)


print(
    load_data.columns.tolist()
)


# ============================================================
# 23. LOAD SWEEP COLUMNS
# ============================================================

"""
The worksheet contains approximately:

Load_percent

Output_Current_A

Output_Voltage_V

Input_Power_W

Output_Power_W

Efficiency_percent

Temperature_C
"""


# ============================================================
# 24. PLOT EFFICIENCY VS LOAD
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_data["Load_percent"],
    load_data["Efficiency_percent"],
    marker="o",
    linewidth=2
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Converter Efficiency vs Load"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 25. TEMPERATURE VS LOAD
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_data["Load_percent"],
    load_data["Temperature_C"],
    marker="o",
    linewidth=2
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Temperature [°C]"
)

ax.set_title(
    "Converter Temperature vs Load"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 26. MULTIPLE LOAD-SWEEP VARIABLES
# ============================================================

"""
Because Efficiency and Temperature use different units,
use separate subplots.
"""


fig, axes = plt.subplots(
    2,
    1,
    figsize=(7, 6),
    sharex=True
)


axes[0].plot(
    load_data["Load_percent"],
    load_data["Efficiency_percent"],
    marker="o"
)

axes[0].set_ylabel(
    "Efficiency [%]"
)

axes[0].grid(
    True
)


axes[1].plot(
    load_data["Load_percent"],
    load_data["Temperature_C"],
    marker="o"
)

axes[1].set_xlabel(
    "Load [%]"
)

axes[1].set_ylabel(
    "Temperature [°C]"
)

axes[1].grid(
    True
)


fig.suptitle(
    "Converter Performance vs Load"
)


plt.tight_layout()

plt.show()


# ============================================================
# 27. READ FREQUENCY COMPARISON WORKSHEET
# ============================================================

frequency_data = pd.read_excel(
    excel_file,
    sheet_name="Case_Comparison"
)


print(
    "\n--- Case_Comparison Data ---"
)


print(
    frequency_data.head()
)


print(
    "\n--- Case_Comparison Columns ---"
)


print(
    frequency_data.columns.tolist()
)


# ============================================================
# 28. EXPECTED FREQUENCY COLUMNS
# ============================================================

"""
The worksheet contains:

Frequency_Hz

Unshielded_dBuV

Case_A_dBuV

Case_B_dBuV

Case_C_dBuV
"""


# ============================================================
# 29. FREQUENCY COMPARISON
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


ax.plot(
    frequency_data["Frequency_Hz"],
    frequency_data["Unshielded_dBuV"],
    linewidth=2,
    label="Unshielded"
)


ax.plot(
    frequency_data["Frequency_Hz"],
    frequency_data["Case_A_dBuV"],
    linewidth=2,
    label="Case A"
)


ax.plot(
    frequency_data["Frequency_Hz"],
    frequency_data["Case_B_dBuV"],
    linewidth=2,
    label="Case B"
)


ax.plot(
    frequency_data["Frequency_Hz"],
    frequency_data["Case_C_dBuV"],
    linewidth=2,
    label="Case C"
)


ax.set_xlabel(
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)

ax.set_title(
    "Frequency-Domain Case Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 30. LOGARITHMIC FREQUENCY AXIS
# ============================================================

"""
Engineering frequency data often cover several decades.

For example:

10 kHz

to

30 MHz


A logarithmic X-axis is often more appropriate.
"""


fig, ax = plt.subplots(
    figsize=(8, 4.8)
)


frequency_columns = {

    "Unshielded": "Unshielded_dBuV",

    "Case A": "Case_A_dBuV",

    "Case B": "Case_B_dBuV",

    "Case C": "Case_C_dBuV"

}


for case_name, column_name in frequency_columns.items():

    ax.plot(
        frequency_data["Frequency_Hz"],
        frequency_data[column_name],
        linewidth=2,
        label=case_name
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
    "Frequency-Domain Comparison"
)


ax.grid(
    True,
    which="both"
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 31. SELECT ONLY SPECIFIC EXCEL COLUMNS
# ============================================================

"""
Large workbooks may contain many columns.

Pandas can read only selected columns using:

usecols=
"""


selected_data = pd.read_excel(

    excel_file,

    sheet_name="Time_Domain",

    usecols=[
        "Time_s",
        "Output_Voltage_V",
        "Output_Current_A"
    ]

)


print(
    "\n--- Selected Excel Columns ---"
)


print(
    selected_data.head()
)


# ============================================================
# 32. usecols WITH EXCEL COLUMN LETTERS
# ============================================================

"""
Excel-style column ranges may also be used.

Example:

usecols="A:E"


This reads columns:

A
B
C
D
E


This can be useful when the workbook layout is already
known.
"""


first_five_columns = pd.read_excel(

    excel_file,

    sheet_name="Time_Domain",

    usecols="A:E"

)


print(
    "\n--- First Five Excel Columns ---"
)


print(
    first_five_columns.head()
)


# ============================================================
# 33. READ LIMITED NUMBER OF ROWS
# ============================================================

"""
Use:

nrows=

when only part of a large Excel worksheet is required.
"""


first_five_rows = pd.read_excel(

    excel_file,

    sheet_name="Time_Domain",

    nrows=5

)


print(
    "\n--- First Five Data Rows ---"
)


print(
    first_five_rows
)


# ============================================================
# 34. SKIP ROWS
# ============================================================

"""
Real engineering Excel files often contain:

Company name

Test information

Instrument details

Date

Notes

before the actual table begins.


Example workbook layout:

Row 1    Experiment Name
Row 2    Date
Row 3    Instrument
Row 4    Notes
Row 5    Time, Voltage, Current
Row 6    Data
Row 7    Data


In such cases:

skiprows=

can be useful.


Example:

data = pd.read_excel(
    "measurement.xlsx",
    skiprows=4
)


Do NOT use skiprows for the supplied sample workbook
because its header already starts correctly on row 1.
"""


# ============================================================
# 35. CUSTOM HEADER ROW
# ============================================================

"""
Another option is:

header=


For example:

header=4

means Excel row 5 is treated as the column-name row
because Python uses zero-based indexing.


Example:

data = pd.read_excel(
    "measurement.xlsx",
    header=4
)


This is common when measurement equipment exports metadata
before the real table.
"""


# ============================================================
# 36. READ ALL WORKSHEETS
# ============================================================

"""
Pandas can read every sheet at once using:

sheet_name=None


The result is a dictionary.

Key:

Worksheet name

Value:

Pandas DataFrame
"""


all_sheets = pd.read_excel(
    excel_file,
    sheet_name=None
)


print(
    "\n--- Sheets Loaded into Dictionary ---"
)


print(
    all_sheets.keys()
)


# ============================================================
# 37. ACCESS SHEET FROM DICTIONARY
# ============================================================

time_sheet = all_sheets[
    "Time_Domain"
]


load_sheet = all_sheets[
    "Load_Sweep"
]


comparison_sheet = all_sheets[
    "Case_Comparison"
]


print(
    "\nTime_Domain rows:",
    len(time_sheet)
)


print(
    "Load_Sweep rows:",
    len(load_sheet)
)


print(
    "Case_Comparison rows:",
    len(comparison_sheet)
)


# ============================================================
# 38. LOOP THROUGH ALL SHEETS
# ============================================================

"""
This is useful when inspecting an unfamiliar workbook.
"""


print(
    "\n--- Workbook Summary ---"
)


for sheet_name, dataframe in all_sheets.items():

    print(
        f"\nSheet: {sheet_name}"
    )

    print(
        f"Shape: {dataframe.shape}"
    )

    print(
        "Columns:"
    )

    print(
        dataframe.columns.tolist()
    )


# ============================================================
# 39. CHECK WHETHER SHEET EXISTS
# ============================================================

selected_sheet = "Time_Domain"


if selected_sheet not in workbook.sheet_names:

    raise ValueError(
        f"Worksheet '{selected_sheet}' not found."
        f"\nAvailable worksheets:"
        f"\n{workbook.sheet_names}"
    )


# ============================================================
# 40. SAFE EXCEL-READING FUNCTION
# ============================================================

def read_excel_sheet(
    filename,
    sheet_name
):
    """
    Safely load one worksheet from an Excel workbook.

    Parameters
    ----------
    filename : str or Path
        Excel workbook.

    sheet_name : str
        Worksheet to load.

    Returns
    -------
    pandas.DataFrame
        Loaded worksheet.
    """

    filename = Path(
        filename
    )


    if not filename.exists():

        raise FileNotFoundError(
            f"Excel file not found: "
            f"{filename}"
        )


    excel_workbook = pd.ExcelFile(
        filename
    )


    if sheet_name not in excel_workbook.sheet_names:

        raise ValueError(
            f"Worksheet '{sheet_name}' not found."
            f"\nAvailable worksheets:"
            f"\n{excel_workbook.sheet_names}"
        )


    dataframe = pd.read_excel(
        filename,
        sheet_name=sheet_name
    )


    return dataframe


# ============================================================
# 41. USE SAFE FUNCTION
# ============================================================

example_data = read_excel_sheet(

    excel_file,

    "Load_Sweep"

)


print(
    "\n--- Data Loaded with Function ---"
)


print(
    example_data.head()
)


# ============================================================
# 42. SAFE COLUMN CHECK
# ============================================================

def check_columns(
    dataframe,
    required_columns
):
    """
    Check whether all required columns exist.
    """

    missing_columns = [

        column

        for column in required_columns

        if column not in dataframe.columns

    ]


    if missing_columns:

        raise KeyError(
            f"Missing columns: "
            f"{missing_columns}"
            f"\nAvailable columns:"
            f"\n{dataframe.columns.tolist()}"
        )


# ============================================================
# 43. TEST COLUMN CHECK
# ============================================================

check_columns(

    load_data,

    [
        "Load_percent",
        "Efficiency_percent"
    ]

)


# ============================================================
# 44. REUSABLE EXCEL PLOTTING FUNCTION
# ============================================================

def plot_excel_column(
    filename,
    sheet_name,
    x_column,
    y_column,
    x_label,
    y_label,
    title
):
    """
    Read an Excel worksheet and plot one selected
    Y column against one X column.
    """

    dataframe = read_excel_sheet(
        filename,
        sheet_name
    )


    check_columns(

        dataframe,

        [
            x_column,
            y_column
        ]

    )


    fig, ax = plt.subplots(
        figsize=(7, 4.5)
    )


    ax.plot(
        dataframe[x_column],
        dataframe[y_column],
        linewidth=2
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


    plt.tight_layout()

    plt.show()


# ============================================================
# 45. USE REUSABLE FUNCTION
# ============================================================

plot_excel_column(

    filename=excel_file,

    sheet_name="Load_Sweep",

    x_column="Load_percent",

    y_column="Efficiency_percent",

    x_label="Load [%]",

    y_label="Efficiency [%]",

    title="Efficiency vs Load"

)


# ============================================================
# 46. REUSABLE MULTIPLE-COLUMN FUNCTION
# ============================================================

"""
Now create a function that plots several selected columns.

This is particularly useful when an Excel worksheet
contains many engineering variables.
"""


def plot_excel_subplots(
    filename,
    sheet_name,
    x_column,
    y_columns,
    y_labels,
    x_label,
    title
):
    """
    Plot selected Excel columns as vertically stacked
    subplots.
    """

    dataframe = read_excel_sheet(
        filename,
        sheet_name
    )


    required_columns = [
        x_column
    ] + y_columns


    check_columns(
        dataframe,
        required_columns
    )


    if len(
        y_columns
    ) != len(
        y_labels
    ):

        raise ValueError(
            "Number of Y columns must match "
            "number of Y labels."
        )


    number_of_plots = len(
        y_columns
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

        y_labels

    ):

        ax.plot(
            dataframe[x_column],
            dataframe[column],
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
# 47. USE MULTIPLE-COLUMN FUNCTION
# ============================================================

plot_excel_subplots(

    filename=excel_file,

    sheet_name="Time_Domain",

    x_column="Time_s",

    y_columns=[
        "Output_Voltage_V",
        "Output_Current_A",
        "Temperature_C"
    ],

    y_labels=[
        "Voltage [V]",
        "Current [A]",
        "Temperature [°C]"
    ],

    x_label="Time [s]",

    title="Converter Measurements from Excel"

)


# ============================================================
# 48. SELECT DATA USING VARIABLES
# ============================================================

"""
Instead of editing the plotting code repeatedly, define
the worksheet and columns near the beginning.
"""


sheet_to_plot = "Load_Sweep"

x_column = "Load_percent"

y_column = "Efficiency_percent"


selected_data = pd.read_excel(
    excel_file,
    sheet_name=sheet_to_plot
)


x = selected_data[
    x_column
]


y = selected_data[
    y_column
]


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    x,
    y,
    marker="o"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Selected Excel Data"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 49. FILTER EXCEL DATA
# ============================================================

"""
Pandas filtering works in the same way after data have
been loaded from Excel.

Example:

Only use load >= 50%.
"""


high_load_data = load_data[
    load_data["Load_percent"] >= 50
]


print(
    "\n--- High Load Data ---"
)


print(
    high_load_data
)


# ============================================================
# 50. PLOT FILTERED EXCEL DATA
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    high_load_data["Load_percent"],
    high_load_data["Efficiency_percent"],
    marker="o"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Efficiency for Load ≥ 50%"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 51. CHECK MISSING VALUES
# ============================================================

print(
    "\n--- Missing Values ---"
)


print(
    time_data.isna().sum()
)


# ============================================================
# 52. NUMERICAL CONVERSION
# ============================================================

"""
Real Excel files may contain entries such as:

ERROR

-

N/A

No Data


Use:

pd.to_numeric(
    ...,
    errors="coerce"
)

to convert invalid numerical entries into NaN.
"""


clean_voltage = pd.to_numeric(

    time_data[
        "Output_Voltage_V"
    ],

    errors="coerce"

)


# ============================================================
# 53. CLEAN COLUMN NAMES
# ============================================================

"""
Real Excel column names may contain extra spaces.

Example:

" Output Voltage "

instead of:

"Output Voltage"


Remove surrounding spaces using:
"""


clean_column_example = time_data.copy()


clean_column_example.columns = (

    clean_column_example.columns

    .str.strip()

)


# ============================================================
# 54. RENAME COLUMNS
# ============================================================

"""
Sometimes exported instrument headers are difficult
to work with.

Pandas can rename them.
"""


renamed_example = time_data.rename(

    columns={

        "Time_s":
            "Time",

        "Output_Voltage_V":
            "Voltage"

    }

)


print(
    "\n--- Example Renamed Columns ---"
)


print(
    renamed_example.columns.tolist()
)


# ============================================================
# 55. SAVE PROCESSED DATA TO EXCEL
# ============================================================

"""
Processed data can also be written back to Excel.

This requires openpyxl for .xlsx output.
"""


output_data_folder = (
    script_folder
    / "output_data"
)


output_data_folder.mkdir(
    exist_ok=True
)


processed_excel = (
    output_data_folder
    / "processed_load_data.xlsx"
)


load_data.to_excel(
    processed_excel,
    index=False
)


print(
    "\nProcessed Excel file saved to:"
)


print(
    processed_excel
)


# ============================================================
# 56. SAVE FINAL FIGURE
# ============================================================

output_figure_folder = (
    script_folder
    / "output_figures"
)


output_figure_folder.mkdir(
    exist_ok=True
)


fig, axes = plt.subplots(
    2,
    1,
    figsize=(7, 6),
    sharex=True
)


axes[0].plot(
    load_data["Load_percent"],
    load_data["Efficiency_percent"],
    marker="o",
    linewidth=2
)

axes[0].set_ylabel(
    "Efficiency [%]"
)

axes[0].grid(
    True
)


axes[1].plot(
    load_data["Load_percent"],
    load_data["Temperature_C"],
    marker="o",
    linewidth=2
)

axes[1].set_xlabel(
    "Load [%]"
)

axes[1].set_ylabel(
    "Temperature [°C]"
)

axes[1].grid(
    True
)


fig.suptitle(
    "Converter Performance from Excel"
)


plt.tight_layout()


# ============================================================
# 57. SAVE PNG
# ============================================================

png_file = (
    output_figure_folder
    / "excel_measurements.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 58. SAVE PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "excel_measurements.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 59. SAVE SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "excel_measurements.svg"
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
# 60. COMMON MISTAKE - WRONG WORKSHEET NAME
# ============================================================

"""
Incorrect:

pd.read_excel(
    file,
    sheet_name="Sheet1"
)


when the actual worksheet is:

Time_Domain


Always check:

workbook.sheet_names
"""


# ============================================================
# 61. COMMON MISTAKE - WRONG COLUMN NAME
# ============================================================

"""
Suppose Excel contains:

Output_Voltage_V


but the script uses:

data["Output Voltage"]


This results in:

KeyError


Always inspect:

data.columns.tolist()
"""


# ============================================================
# 62. COMMON MISTAKE - WRONG HEADER ROW
# ============================================================

"""
Some engineering Excel files contain metadata before
the actual column header.

Example:

Test Name
Date
Device
Comment
Time, Voltage, Current


If the wrong row is interpreted as the header, Pandas may
create incorrect column names.

Possible solutions:

skiprows=

or

header=
"""


# ============================================================
# 63. COMMON MISTAKE - READING WRONG SHEET
# ============================================================

"""
An Excel workbook may contain:

Raw_Data

Processed_Data

Summary

FFT

Results


Make sure that the selected worksheet contains the data
you actually intend to analyze.
"""


# ============================================================
# 64. COMMON MISTAKE - MIXING PHYSICAL UNITS
# ============================================================

"""
If the worksheet contains:

Voltage [V]

Current [A]

Temperature [°C]


do not automatically place all of them on one Y-axis.

Use:

Subplots

Dual Y-axis

Normalization

or separate figures.
"""


# ============================================================
# 65. COMMON MISTAKE - TRUSTING FORMULAS WITHOUT CHECKING
# ============================================================

"""
Excel workbooks may contain calculated columns generated
using formulas.

When performing research analysis, verify:

- Formula correctness
- Units
- Missing values
- References
- Data types
- Whether values were recalculated


Python can also calculate important derived quantities
independently for validation.
"""


# ============================================================
# 66. CSV VS EXCEL
# ============================================================

"""
CSV

Usually contains:

One table

No worksheets

Simple structure


Read with:

pd.read_csv()


------------------------------------------------------------


EXCEL

Can contain:

Several worksheets

Several tables

Formulas

Different experimental cases


Read with:

pd.read_excel()
"""


# ============================================================
# 67. EXCEL WORKFLOW
# ============================================================

"""
Excel File
    ↓
Check File Exists
    ↓
pd.ExcelFile()
    ↓
Inspect sheet_names
    ↓
Select Worksheet
    ↓
pd.read_excel()
    ↓
data.head()
    ↓
data.columns
    ↓
data.dtypes
    ↓
Check Missing Values
    ↓
Select X Column
    ↓
Select Y Column(s)
    ↓
Filter / Clean
    ↓
Plot
    ↓
Format
    ↓
Save Figure
"""


# ============================================================
# 68. ENGINEERING WORKFLOW
# ============================================================

"""
Measurement Equipment
        ↓
Excel Workbook
        ↓
Raw_Data Sheet
        ↓
Python
        ↓
Inspect Workbook
        ↓
Select Required Sheet
        ↓
Select Required Columns
        ↓
Clean / Validate
        ↓
Calculate
        ↓
Visualize
        ↓
Save Processed Data
        ↓
Publication Figure
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
PLOT FROM EXCEL


1. READ EXCEL FILE

data = pd.read_excel(
    "measurement.xlsx"
)


------------------------------------------------------------


2. SELECT WORKSHEET

data = pd.read_excel(
    "measurement.xlsx",
    sheet_name="Time_Domain"
)


------------------------------------------------------------


3. CHECK WORKSHEET NAMES

workbook = pd.ExcelFile(
    "measurement.xlsx"
)


print(
    workbook.sheet_names
)


------------------------------------------------------------


4. INSPECT DATA

print(
    data.head()
)


print(
    data.columns
)


print(
    data.dtypes
)


------------------------------------------------------------


5. SELECT COLUMNS

x = data[
    "Time_s"
]


y = data[
    "Output_Voltage_V"
]


------------------------------------------------------------


6. PLOT

ax.plot(
    x,
    y
)


------------------------------------------------------------


7. SELECT ONLY REQUIRED COLUMNS

data = pd.read_excel(
    file,
    usecols=[
        "Time_s",
        "Output_Voltage_V"
    ]
)


------------------------------------------------------------


8. EXCEL COLUMN RANGE

data = pd.read_excel(
    file,
    usecols="A:E"
)


------------------------------------------------------------


9. SELECT NUMBER OF ROWS

data = pd.read_excel(
    file,
    nrows=100
)


------------------------------------------------------------


10. SKIP METADATA ROWS

data = pd.read_excel(
    file,
    skiprows=4
)


Use only when the workbook contains rows before the
actual table.


------------------------------------------------------------


11. READ ALL WORKSHEETS

all_sheets = pd.read_excel(
    file,
    sheet_name=None
)


This returns a dictionary:

{
    "Sheet1": DataFrame,
    "Sheet2": DataFrame,
    ...
}


------------------------------------------------------------


12. DIFFERENT PHYSICAL UNITS

Voltage [V]

Current [A]

Temperature [°C]


Prefer subplots rather than one mixed-unit Y-axis.


------------------------------------------------------------


13. FREQUENCY DATA

Frequency_Hz
     ↓
Magnitude_dBuV


For wide frequency ranges:

ax.set_xscale(
    "log"
)


------------------------------------------------------------


14. SAVE PROCESSED EXCEL

data.to_excel(
    "processed.xlsx",
    index=False
)


------------------------------------------------------------


15. COMMON ERRORS

FileNotFoundError
    Wrong workbook path

ValueError
    Wrong worksheet name

KeyError
    Wrong column name

object dtype
    Numerical column contains text

NaN
    Missing or invalid values

Incorrect header
    Metadata rows interpreted as column names


------------------------------------------------------------


16. MOST IMPORTANT EXCEL HABIT

Do not immediately assume:

Sheet1

Column A

Column B


Instead:

Open Workbook
     ↓
Check Sheet Names
     ↓
Select Sheet
     ↓
Check Column Names
     ↓
Check Data Types
     ↓
Then Plot


------------------------------------------------------------


17. COMPLETE WORKFLOW

Excel
  ↓
Workbook
  ↓
Worksheet
  ↓
Columns
  ↓
Rows
  ↓
Clean
  ↓
Process
  ↓
Plot
  ↓
Export


------------------------------------------------------------


NEXT:

10_select_columns_and_plot.py


This next file will focus specifically on a very common
student/research problem:

"I have a CSV or Excel file with 20 columns.
How do I choose only columns 1, 4, 7 and 10?"


We can cover:

Column names
Column numbers
iloc
loc
usecols
Single column
Multiple columns
Column ranges
Automatic selection
Pattern-based selection
Selecting X independently from Y
Plotting 2, 3, 5 or many selected columns
"""
