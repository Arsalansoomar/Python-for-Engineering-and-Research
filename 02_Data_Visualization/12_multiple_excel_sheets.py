"""
============================================================
Python for Engineering and Research
12 - Multiple Excel Sheets
============================================================

Purpose:
    Demonstrate how several worksheets inside one Excel
    workbook can be discovered, loaded, validated, compared,
    combined, processed, and visualized automatically.

Topics:
    1. Why use multiple Excel worksheets?
    2. Create demonstration multi-sheet workbook
    3. Inspect worksheet names
    4. Read one worksheet
    5. Read selected worksheets
    6. Read all worksheets
    7. Loop through worksheets
    8. Compare the same variable across sheets
    9. Validate worksheet columns
    10. Skip unwanted worksheets
    11. Combine worksheets
    12. Add worksheet/case identifier
    13. Calculate summary statistics
    14. Plot one subplot per worksheet
    15. Filter the same range from every worksheet
    16. Handle different worksheet lengths
    17. Reusable comparison function
    18. Save processed results
    19. Common mistakes
    20. Key takeaways

Sample Source:
    sample_data/multiple_cases.csv

Generated Workbook:
    output_data/multiple_sheet_cases.xlsx

Generated Worksheets:
    Case_A
    Case_B
    Case_C
    Case_D

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHY MULTIPLE EXCEL SHEETS?
# ============================================================

"""
Engineering experiments are often stored inside one Excel
workbook with one worksheet for each case.

Example:

converter_tests.xlsx

        ↓

┌──────────────────────────────┐
│ Case_A                       │
├──────────────────────────────┤
│ Case_B                       │
├──────────────────────────────┤
│ Case_C                       │
├──────────────────────────────┤
│ Case_D                       │
└──────────────────────────────┘


Each worksheet may contain:

Time_s
Voltage_V
Current_A
Temperature_C
...


Instead of manually writing:

case_a = pd.read_excel(
    file,
    sheet_name="Case_A"
)

case_b = pd.read_excel(
    file,
    sheet_name="Case_B"
)

case_c = pd.read_excel(
    file,
    sheet_name="Case_C"
)


we can automate the process.
"""


# ============================================================
# 2. REQUIRED LIBRARIES
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path


# ============================================================
# 3. DEFINE PATHS
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


sample_data_folder = (
    script_folder
    / "sample_data"
)


output_data_folder = (
    script_folder
    / "output_data"
)


output_figure_folder = (
    script_folder
    / "output_figures"
)


output_data_folder.mkdir(
    exist_ok=True
)


output_figure_folder.mkdir(
    exist_ok=True
)


source_csv = (
    sample_data_folder
    / "multiple_cases.csv"
)


multi_sheet_file = (
    output_data_folder
    / "multiple_sheet_cases.xlsx"
)


# ============================================================
# 4. CHECK SOURCE DATA
# ============================================================

if not source_csv.exists():

    raise FileNotFoundError(
        f"\nSource CSV file not found:\n"
        f"{source_csv}"
    )


# ============================================================
# 5. CREATE DEMONSTRATION MULTI-SHEET WORKBOOK
# ============================================================

"""
Our existing sample CSV contains:

Time_s

Case_A_V

Case_B_V

Case_C_V

Case_D_V


We convert each case into an independent Excel worksheet.

Each worksheet will contain:

Time_s

Voltage_V
"""


source_data = pd.read_csv(
    source_csv
)


case_mapping = {

    "Case_A":
        "Case_A_V",

    "Case_B":
        "Case_B_V",

    "Case_C":
        "Case_C_V",

    "Case_D":
        "Case_D_V"

}


with pd.ExcelWriter(
    multi_sheet_file,
    engine="openpyxl"
) as writer:

    for sheet_name, source_column in case_mapping.items():

        case_data = pd.DataFrame(
            {
                "Time_s":
                    source_data[
                        "Time_s"
                    ],

                "Voltage_V":
                    source_data[
                        source_column
                    ]
            }
        )


        case_data.to_excel(
            writer,
            sheet_name=sheet_name,
            index=False
        )


print(
    "\n--- Multi-Sheet Workbook Created ---"
)


print(
    multi_sheet_file
)


# ============================================================
# 6. EXPECTED WORKBOOK STRUCTURE
# ============================================================

"""
multiple_sheet_cases.xlsx

    ├── Case_A
    │     ├── Time_s
    │     └── Voltage_V
    │
    ├── Case_B
    │     ├── Time_s
    │     └── Voltage_V
    │
    ├── Case_C
    │     ├── Time_s
    │     └── Voltage_V
    │
    └── Case_D
          ├── Time_s
          └── Voltage_V
"""


# ============================================================
# 7. OPEN WORKBOOK
# ============================================================

"""
pd.ExcelFile() is useful when we first want to inspect
the workbook structure.
"""


workbook = pd.ExcelFile(
    multi_sheet_file
)


# ============================================================
# 8. INSPECT WORKSHEET NAMES
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
# 9. NUMBER OF WORKSHEETS
# ============================================================

print(
    "\nNumber of Worksheets:"
)


print(
    len(
        workbook.sheet_names
    )
)


# ============================================================
# 10. READ ONE WORKSHEET
# ============================================================

case_a = pd.read_excel(

    multi_sheet_file,

    sheet_name="Case_A"

)


print(
    "\n--- Case_A Data ---"
)


print(
    case_a.head()
)


# ============================================================
# 11. INSPECT COLUMNS
# ============================================================

print(
    "\n--- Case_A Columns ---"
)


print(
    case_a.columns.tolist()
)


print(
    "\n--- Data Types ---"
)


print(
    case_a.dtypes
)


# ============================================================
# 12. BASIC PLOT FROM ONE WORKSHEET
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    case_a["Time_s"],
    case_a["Voltage_V"],
    linewidth=2
)


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Case A"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 13. READ SELECTED WORKSHEETS
# ============================================================

"""
Sometimes only selected worksheets are required.

Example:

Case_A

and

Case_C
"""


selected_sheets = [

    "Case_A",

    "Case_C"

]


selected_data = pd.read_excel(

    multi_sheet_file,

    sheet_name=selected_sheets

)


# ============================================================
# 14. WHAT DOES THIS RETURN?
# ============================================================

"""
When several worksheets are requested:

pd.read_excel(
    file,
    sheet_name=[
        "Case_A",
        "Case_C"
    ]
)


returns a DICTIONARY.

Structure:

{
    "Case_A": DataFrame,
    "Case_C": DataFrame
}
"""


print(
    "\n--- Selected Sheet Dictionary ---"
)


print(
    selected_data.keys()
)


# ============================================================
# 15. ACCESS SELECTED WORKSHEET
# ============================================================

case_c = selected_data[
    "Case_C"
]


print(
    "\n--- Case C ---"
)


print(
    case_c.head()
)


# ============================================================
# 16. PLOT SELECTED WORKSHEETS
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for sheet_name, dataframe in selected_data.items():

    ax.plot(
        dataframe["Time_s"],
        dataframe["Voltage_V"],
        linewidth=2,
        label=sheet_name
    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Selected Excel Worksheets"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 17. READ ALL WORKSHEETS
# ============================================================

"""
Use:

sheet_name=None

to load ALL worksheets.

The result is again a dictionary.
"""


all_sheets = pd.read_excel(

    multi_sheet_file,

    sheet_name=None

)


print(
    "\n--- All Loaded Worksheets ---"
)


print(
    all_sheets.keys()
)


# ============================================================
# 18. LOOP THROUGH ALL WORKSHEETS
# ============================================================

for sheet_name, dataframe in all_sheets.items():

    print(
        f"\nWorksheet: "
        f"{sheet_name}"
    )

    print(
        "Shape:",
        dataframe.shape
    )

    print(
        "Columns:",
        dataframe.columns.tolist()
    )


# ============================================================
# 19. COMPARE SAME VARIABLE FROM EVERY SHEET
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for sheet_name, dataframe in all_sheets.items():

    ax.plot(
        dataframe["Time_s"],
        dataframe["Voltage_V"],
        linewidth=2,
        label=sheet_name
    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Multiple Excel Worksheet Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 20. CLEAN SHEET NAMES FOR LEGEND
# ============================================================

"""
Worksheet:

Case_A

can be displayed as:

Case A
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for sheet_name, dataframe in all_sheets.items():

    clean_label = (
        sheet_name
        .replace(
            "_",
            " "
        )
    )


    ax.plot(
        dataframe["Time_s"],
        dataframe["Voltage_V"],
        linewidth=2,
        label=clean_label
    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Engineering Case Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 21. VALIDATE REQUIRED COLUMNS
# ============================================================

required_columns = [

    "Time_s",

    "Voltage_V"

]


def validate_columns(
    dataframe,
    required_columns,
    sheet_name=None
):
    """
    Check whether required columns exist in a worksheet.
    """

    missing_columns = [

        column

        for column in required_columns

        if column not in dataframe.columns

    ]


    if missing_columns:

        raise KeyError(
            f"\nMissing columns: "
            f"{missing_columns}"
            f"\nWorksheet: "
            f"{sheet_name}"
            f"\nAvailable columns:"
            f"\n{dataframe.columns.tolist()}"
        )


# ============================================================
# 22. VALIDATE ALL WORKSHEETS
# ============================================================

for sheet_name, dataframe in all_sheets.items():

    validate_columns(

        dataframe,

        required_columns,

        sheet_name

    )


print(
    "\nAll worksheets contain the required columns."
)


# ============================================================
# 23. CLEAN COLUMN NAMES
# ============================================================

"""
Real Excel exports may contain:

" Time_s "

instead of:

"Time_s"


Clean column headers using:

.str.strip()
"""


for sheet_name, dataframe in all_sheets.items():

    dataframe.columns = (

        dataframe.columns

        .str.strip()

    )


# ============================================================
# 24. LOAD SHEETS INTO CUSTOM DICTIONARY
# ============================================================

"""
Sometimes we want to manually control which worksheets
are included.
"""


sheets_to_compare = [

    "Case_A",

    "Case_B",

    "Case_D"

]


datasets = {}


for sheet_name in sheets_to_compare:

    datasets[
        sheet_name
    ] = pd.read_excel(

        multi_sheet_file,

        sheet_name=sheet_name

    )


print(
    "\n--- Custom Dataset Dictionary ---"
)


print(
    datasets.keys()
)


# ============================================================
# 25. PLOT CUSTOM WORKSHEET SELECTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, dataframe in datasets.items():

    ax.plot(
        dataframe["Time_s"],
        dataframe["Voltage_V"],
        linewidth=2,
        label=case_name
    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Selected Case Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 26. COMBINE ALL WORKSHEETS
# ============================================================

"""
A useful analysis format is:

Time_s
Voltage_V
Case


Instead of keeping data separated across worksheets, the
data can be combined into one long-format DataFrame.
"""


combined_dataframes = []


for sheet_name, dataframe in all_sheets.items():

    temporary_data = dataframe.copy()


    temporary_data[
        "Case"
    ] = sheet_name


    combined_dataframes.append(
        temporary_data
    )


combined_data = pd.concat(

    combined_dataframes,

    ignore_index=True

)


print(
    "\n--- Combined Excel Data ---"
)


print(
    combined_data.head()
)


print(
    "\nCombined Shape:"
)


print(
    combined_data.shape
)


# ============================================================
# 27. AVAILABLE CASES AFTER COMBINATION
# ============================================================

print(
    "\n--- Available Cases ---"
)


print(
    combined_data[
        "Case"
    ].unique()
)


# ============================================================
# 28. SELECT ONE CASE FROM COMBINED DATA
# ============================================================

selected_case = combined_data[

    combined_data[
        "Case"
    ] == "Case_B"

]


print(
    "\n--- Case B from Combined Data ---"
)


print(
    selected_case.head()
)


# ============================================================
# 29. SAVE COMBINED DATA TO CSV
# ============================================================

combined_csv = (
    output_data_folder
    / "combined_excel_sheets.csv"
)


combined_data.to_csv(
    combined_csv,
    index=False
)


print(
    "\nCombined CSV saved to:"
)


print(
    combined_csv
)


# ============================================================
# 30. SAVE COMBINED DATA TO EXCEL
# ============================================================

combined_excel = (
    output_data_folder
    / "combined_excel_sheets.xlsx"
)


combined_data.to_excel(
    combined_excel,
    index=False
)


print(
    "\nCombined Excel file saved to:"
)


print(
    combined_excel
)


# ============================================================
# 31. SUMMARY STATISTICS FOR EACH SHEET
# ============================================================

"""
Calculate:

Number of samples

Mean

Minimum

Maximum

Standard deviation
"""


summary_results = []


for sheet_name, dataframe in all_sheets.items():

    voltage = dataframe[
        "Voltage_V"
    ]


    summary_results.append(
        {
            "Case":
                sheet_name,

            "Samples":
                len(dataframe),

            "Mean_V":
                voltage.mean(),

            "Minimum_V":
                voltage.min(),

            "Maximum_V":
                voltage.max(),

            "Std_V":
                voltage.std()
        }
    )


summary_data = pd.DataFrame(
    summary_results
)


print(
    "\n--- Worksheet Summary ---"
)


print(
    summary_data
)


# ============================================================
# 32. SAVE SUMMARY TABLE
# ============================================================

summary_file = (
    output_data_folder
    / "excel_sheet_summary.csv"
)


summary_data.to_csv(
    summary_file,
    index=False
)


print(
    "\nSummary saved to:"
)


print(
    summary_file
)


# ============================================================
# 33. SUMMARY BAR PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(

    summary_data[
        "Case"
    ],

    summary_data[
        "Maximum_V"
    ]

)


ax.set_xlabel(
    "Case"
)

ax.set_ylabel(
    "Maximum Voltage [V]"
)

ax.set_title(
    "Maximum Voltage by Worksheet"
)


ax.grid(
    True,
    axis="y"
)


ax.bar_label(
    bars,
    fmt="%.2f",
    padding=3
)


plt.tight_layout()

plt.show()


# ============================================================
# 34. ONE SUBPLOT PER WORKSHEET
# ============================================================

number_of_sheets = len(
    all_sheets
)


fig, axes = plt.subplots(

    number_of_sheets,

    1,

    figsize=(
        7,
        2.3 * number_of_sheets
    ),

    sharex=True

)


if number_of_sheets == 1:

    axes = [
        axes
    ]


for ax, (
    sheet_name,
    dataframe
) in zip(

    axes,

    all_sheets.items()

):

    ax.plot(
        dataframe["Time_s"],
        dataframe["Voltage_V"],
        linewidth=2
    )


    ax.set_ylabel(
        "Voltage [V]"
    )


    ax.set_title(
        sheet_name
    )


    ax.grid(
        True
    )


axes[-1].set_xlabel(
    "Time [s]"
)


fig.suptitle(
    "Individual Excel Worksheets"
)


plt.tight_layout()

plt.show()


# ============================================================
# 35. FILTER SAME TIME RANGE FROM EVERY SHEET
# ============================================================

"""
Suppose only:

5 ms to 15 ms

should be compared.
"""


start_time = 0.005

end_time = 0.015


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for sheet_name, dataframe in all_sheets.items():

    selected_window = dataframe[
        (
            dataframe[
                "Time_s"
            ] >= start_time
        )
        &
        (
            dataframe[
                "Time_s"
            ] <= end_time
        )
    ]


    ax.plot(

        selected_window[
            "Time_s"
        ],

        selected_window[
            "Voltage_V"
        ],

        marker="o",

        label=sheet_name

    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Selected Time Window"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 36. DIFFERENT WORKSHEET LENGTHS
# ============================================================

"""
Excel worksheets do NOT need identical row counts for
ordinary plotting.

For example:

Case A:
1000 rows

Case B:
950 rows

Case C:
1200 rows


Each worksheet can use its own X/Y pair.

However, direct calculations such as:

Case A - Case B

require proper alignment.
"""


print(
    "\n--- Samples per Worksheet ---"
)


for sheet_name, dataframe in all_sheets.items():

    print(
        sheet_name,
        ":",
        len(dataframe),
        "samples"
    )


# ============================================================
# 37. IMPORTANT: CHECK X-AXIS ALIGNMENT
# ============================================================

"""
Before comparing worksheets numerically, check:

- Same sampling interval?
- Same number of samples?
- Same start time?
- Same end time?
- Same trigger point?
- Same measurement conditions?


Visualization:

Different X vectors may be acceptable.


Direct numerical subtraction:

Requires proper alignment.
"""


# ============================================================
# 38. CHECK TIME RANGE OF EVERY SHEET
# ============================================================

print(
    "\n--- Time Range per Worksheet ---"
)


for sheet_name, dataframe in all_sheets.items():

    minimum_time = dataframe[
        "Time_s"
    ].min()


    maximum_time = dataframe[
        "Time_s"
    ].max()


    print(
        sheet_name,
        ":",
        minimum_time,
        "to",
        maximum_time,
        "s"
    )


# ============================================================
# 39. SKIP UNWANTED WORKSHEETS
# ============================================================

"""
Real workbooks may contain sheets such as:

Summary

Notes

Parameters

Raw_Data

Case_A

Case_B


Not every sheet should automatically be treated as
measurement data.
"""


example_sheet_names = [

    "Summary",

    "Case_A",

    "Case_B",

    "Notes",

    "Case_C"

]


ignored_sheets = [

    "Summary",

    "Notes"

]


sheets_for_analysis = [

    sheet

    for sheet in example_sheet_names

    if sheet not in ignored_sheets

]


print(
    "\n--- Example Sheets for Analysis ---"
)


print(
    sheets_for_analysis
)


# ============================================================
# 40. SELECT SHEETS USING NAME PATTERN
# ============================================================

"""
If measurement worksheets follow a naming convention:

Case_A

Case_B

Case_C


we can select only sheets starting with:

Case_
"""


case_sheet_names = [

    sheet_name

    for sheet_name in workbook.sheet_names

    if sheet_name.startswith(
        "Case_"
    )

]


print(
    "\n--- Sheets Starting with Case_ ---"
)


print(
    case_sheet_names
)


# ============================================================
# 41. CASE-INSENSITIVE SHEET SEARCH
# ============================================================

search_word = "case"


matching_sheets = [

    sheet_name

    for sheet_name in workbook.sheet_names

    if search_word.lower()
    in sheet_name.lower()

]


print(
    "\n--- Matching Worksheets ---"
)


print(
    matching_sheets
)


# ============================================================
# 42. HANDLE MISSING WORKSHEET
# ============================================================

def validate_sheet(
    workbook,
    sheet_name
):
    """
    Check whether a worksheet exists.
    """

    if sheet_name not in workbook.sheet_names:

        raise ValueError(
            f"\nWorksheet '{sheet_name}' "
            f"does not exist."
            f"\nAvailable worksheets:"
            f"\n{workbook.sheet_names}"
        )


# ============================================================
# 43. TEST WORKSHEET VALIDATION
# ============================================================

validate_sheet(
    workbook,
    "Case_A"
)


# ============================================================
# 44. REUSABLE MULTIPLE-SHEET PLOT FUNCTION
# ============================================================

def plot_multiple_excel_sheets(
    filename,
    sheet_names,
    x_column,
    y_column,
    x_label,
    y_label,
    title
):
    """
    Plot the same variable from several Excel worksheets.

    Parameters
    ----------
    filename : str or Path
        Excel workbook path.

    sheet_names : list or None
        Worksheets to compare.

        If None:
            All worksheets are used.

    x_column : str
        X-axis column.

    y_column : str
        Y-axis column.

    x_label : str
        X-axis label.

    y_label : str
        Y-axis label.

    title : str
        Figure title.
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


    if sheet_names is None:

        sheet_names = (
            excel_workbook
            .sheet_names
        )


    for sheet_name in sheet_names:

        validate_sheet(
            excel_workbook,
            sheet_name
        )


    fig, ax = plt.subplots(
        figsize=(7, 4.5)
    )


    for sheet_name in sheet_names:

        dataframe = pd.read_excel(

            filename,

            sheet_name=sheet_name

        )


        dataframe.columns = (

            dataframe.columns

            .str.strip()

        )


        validate_columns(

            dataframe,

            [
                x_column,
                y_column
            ],

            sheet_name

        )


        label = (
            sheet_name
            .replace(
                "_",
                " "
            )
        )


        ax.plot(

            dataframe[
                x_column
            ],

            dataframe[
                y_column
            ],

            linewidth=2,

            label=label

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
# 45. USE REUSABLE FUNCTION
# ============================================================

plot_multiple_excel_sheets(

    filename=multi_sheet_file,

    sheet_names=[
        "Case_A",
        "Case_B",
        "Case_C",
        "Case_D"
    ],

    x_column="Time_s",

    y_column="Voltage_V",

    x_label="Time [s]",

    y_label="Voltage [V]",

    title="Automatic Excel Worksheet Comparison"

)


# ============================================================
# 46. USE ALL WORKSHEETS AUTOMATICALLY
# ============================================================

plot_multiple_excel_sheets(

    filename=multi_sheet_file,

    sheet_names=None,

    x_column="Time_s",

    y_column="Voltage_V",

    x_label="Time [s]",

    y_label="Voltage [V]",

    title="All Excel Worksheets"

)


# ============================================================
# 47. SAVE FINAL COMPARISON FIGURE
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for sheet_name, dataframe in all_sheets.items():

    label = (
        sheet_name
        .replace(
            "_",
            " "
        )
    )


    ax.plot(

        dataframe[
            "Time_s"
        ],

        dataframe[
            "Voltage_V"
        ],

        linewidth=2,

        label=label

    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Multiple Excel Sheet Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()


# ============================================================
# 48. SAVE PNG
# ============================================================

png_file = (
    output_figure_folder
    / "multiple_excel_sheets.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 49. SAVE PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "multiple_excel_sheets.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 50. SAVE SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "multiple_excel_sheets.svg"
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
# 51. COMMON MISTAKE - ASSUMING SHEET NAMES
# ============================================================

"""
Avoid assuming:

Sheet1

Sheet2

Sheet3


Always inspect:

workbook = pd.ExcelFile(
    file
)


print(
    workbook.sheet_names
)
"""


# ============================================================
# 52. COMMON MISTAKE - PROCESSING EVERY SHEET
# ============================================================

"""
Workbook:

Summary

Notes

Parameters

Case_A

Case_B


Using:

sheet_name=None

loads all worksheets.

However, not every worksheet necessarily contains
measurement data.

Filter the sheet names before analysis.
"""


# ============================================================
# 53. COMMON MISTAKE - DIFFERENT COLUMN NAMES
# ============================================================

"""
Case_A:

Time_s
Voltage_V


Case_B:

Time
Voltage


Although the physical data may be equivalent, Python sees
different column names.

Solutions include:

Rename columns

or

Standardize exported data.
"""


# ============================================================
# 54. COMMON MISTAKE - SAME COLUMN POSITION
# ============================================================

"""
Worksheet A:

Column A = Time
Column B = Voltage


Worksheet B:

Column A = Sample
Column B = Time
Column C = Voltage


Selecting:

iloc[:, 1]

would select different variables.

Meaningful column names are generally safer.
"""


# ============================================================
# 55. COMMON MISTAKE - DIRECTLY SUBTRACTING WORKSHEETS
# ============================================================

"""
Do not automatically calculate:

Case_A["Voltage_V"]
-
Case_B["Voltage_V"]


without checking:

Time alignment

Sampling frequency

Number of samples

Trigger point

Missing values


Numerical comparison requires aligned observations.
"""


# ============================================================
# 56. COMMON MISTAKE - DIFFERENT UNITS
# ============================================================

"""
Worksheet A:

Voltage [V]


Worksheet B:

Voltage [mV]


Even if both appear to represent voltage, the numerical
comparison is invalid until units are standardized.
"""


# ============================================================
# 57. COMMON MISTAKE - SILENTLY SKIPPING SHEETS
# ============================================================

"""
If a worksheet cannot be processed, record:

Worksheet name

Reason

Missing columns

Invalid data

Processing decision


Research workflows should remain traceable.
"""


# ============================================================
# 58. MULTIPLE CSV VS MULTIPLE EXCEL SHEETS
# ============================================================

"""
MULTIPLE CSV FILES

Case_A.csv
Case_B.csv
Case_C.csv

        ↓

folder.glob(
    "*.csv"
)


------------------------------------------------------------


MULTIPLE EXCEL SHEETS

cases.xlsx

    Case_A
    Case_B
    Case_C

        ↓

workbook.sheet_names
"""


# ============================================================
# 59. MULTIPLE EXCEL WORKFLOW
# ============================================================

"""
Excel Workbook
       ↓
pd.ExcelFile()
       ↓
Inspect sheet_names
       ↓
Select Required Sheets
       ↓
Loop Through Sheets
       ↓
pd.read_excel()
       ↓
Clean Column Names
       ↓
Validate Columns
       ↓
Select X / Y
       ↓
Plot
       ↓
Combine Worksheets
       ↓
Calculate Statistics
       ↓
Save Results
"""


# ============================================================
# 60. ENGINEERING RESEARCH WORKFLOW
# ============================================================

"""
Experiment Workbook
        ↓
Case A Sheet
Case B Sheet
Case C Sheet
Case D Sheet
        ↓
Python
        ↓
Automatic Worksheet Detection
        ↓
Validation
        ↓
Same Variable Extracted
        ↓
Case Comparison
        ↓
Summary Metrics
        ↓
Engineering Interpretation
        ↓
Publication Figure
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
MULTIPLE EXCEL SHEETS


1. INSPECT WORKSHEETS

workbook = pd.ExcelFile(
    "data.xlsx"
)


print(
    workbook.sheet_names
)


------------------------------------------------------------


2. READ ONE SHEET

data = pd.read_excel(

    "data.xlsx",

    sheet_name="Case_A"

)


------------------------------------------------------------


3. READ SELECTED SHEETS

data = pd.read_excel(

    "data.xlsx",

    sheet_name=[
        "Case_A",
        "Case_B"
    ]

)


Returns:

Dictionary of DataFrames


------------------------------------------------------------


4. READ ALL SHEETS

all_sheets = pd.read_excel(

    "data.xlsx",

    sheet_name=None

)


------------------------------------------------------------


5. LOOP THROUGH SHEETS

for sheet_name, data in all_sheets.items():

    print(
        sheet_name
    )


------------------------------------------------------------


6. PLOT SAME VARIABLE

for sheet_name, data in all_sheets.items():

    ax.plot(

        data["Time_s"],

        data["Voltage_V"],

        label=sheet_name

    )


------------------------------------------------------------


7. FILTER SHEETS BY NAME

case_sheets = [

    sheet

    for sheet in workbook.sheet_names

    if sheet.startswith(
        "Case_"
    )

]


------------------------------------------------------------


8. EXCLUDE UNWANTED SHEETS

ignored = [

    "Summary",

    "Notes"

]


selected = [

    sheet

    for sheet in workbook.sheet_names

    if sheet not in ignored

]


------------------------------------------------------------


9. COMBINE WORKSHEETS

Add:

data["Case"] = sheet_name


Then:

combined = pd.concat(
    dataframes,
    ignore_index=True
)


------------------------------------------------------------


10. SUMMARY STATISTICS

For every worksheet calculate:

Number of samples

Mean

Minimum

Maximum

Standard deviation

Peak


------------------------------------------------------------


11. DIFFERENT WORKSHEET LENGTHS

Acceptable for:

Plotting


Requires alignment for:

Subtraction

Average waveforms

Point-by-point error

Direct numerical comparison


------------------------------------------------------------


12. VALIDATE BEFORE ANALYSIS

Check:

Worksheet exists

Required columns exist

Units match

Time vectors are appropriate

Data types are numerical

Missing data are understood


------------------------------------------------------------


13. MULTIPLE CSV VS EXCEL

CSV:

Many files
    ↓
glob()


Excel:

One file
    ↓
Many sheets
    ↓
sheet_names


------------------------------------------------------------


14. MOST IMPORTANT RULE

Do not assume that every worksheet in an engineering
workbook contains compatible measurement data.

Inspect:

Sheet Name
   ↓
Columns
   ↓
Units
   ↓
Data Types
   ↓
Sampling
   ↓
Then Compare


------------------------------------------------------------


15. COMPLETE WORKFLOW

Excel Workbook
      ↓
Inspect Sheets
      ↓
Select Cases
      ↓
Read
      ↓
Validate
      ↓
Process
      ↓
Compare
      ↓
Combine
      ↓
Summarize
      ↓
Plot
      ↓
Export


------------------------------------------------------------


NEXT:

13_dual_y_axis.py


This will address another common engineering problem:

"I have two variables with different units,
but I want to compare them against the same X-axis."


Example:

          Voltage [V]
              ↑
              │
Time ─────────┼─────────
              │
              ↓
         Current [A]


We should cover:

Voltage + Current

Efficiency + Temperature

Power + Temperature

ax.twinx()

Independent Y-axis limits

Separate Y labels

Legend handling

When dual Y-axis is appropriate

When it becomes misleading

Dual Y-axis vs subplots

Publication-quality use
"""
