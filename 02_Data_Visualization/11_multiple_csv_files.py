"""
============================================================
Python for Engineering and Research
11 - Multiple CSV Files
============================================================

Purpose:
    Demonstrate how several CSV files can be discovered,
    loaded, validated, processed, compared, combined, and
    visualized automatically using Pandas and Matplotlib.

Topics:
    1. Why use multiple CSV files?
    2. Expected folder structure
    3. Create demonstration case files
    4. Explicit file list
    5. Read files using a loop
    6. Use filenames as labels
    7. Discover files automatically with glob()
    8. Sort file order
    9. Check required columns
    10. Plot several experimental cases
    11. Handle different file lengths
    12. Combine several files
    13. Add case identifiers
    14. Create subplots
    15. Calculate summary statistics
    16. Select a time window
    17. Reusable comparison function
    18. Save figures
    19. Common mistakes
    20. Key takeaways

Sample Source:
    sample_data/multiple_cases.csv

Generated Demonstration Files:
    sample_data/multiple_csv_cases/
        Case_A.csv
        Case_B.csv
        Case_C.csv
        Case_D.csv

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHY MULTIPLE CSV FILES?
# ============================================================

"""
Engineering experiments often generate one file for each
operating case.

Example:

Experiment_01.csv
Experiment_02.csv
Experiment_03.csv

or:

Baseline.csv
Design_A.csv
Design_B.csv
Design_C.csv


Typical workflow:

Case_A.csv
Case_B.csv
Case_C.csv
Case_D.csv
     ↓
Loop through files
     ↓
Load each dataset
     ↓
Select common variables
     ↓
Plot together
     ↓
Compare results


This is much more efficient than manually writing:

pd.read_csv("Case_A.csv")
pd.read_csv("Case_B.csv")
pd.read_csv("Case_C.csv")
...
"""


# ============================================================
# 2. REQUIRED LIBRARIES
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path


# ============================================================
# 3. DEFINE PROJECT PATHS
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


sample_data_folder = (
    script_folder
    / "sample_data"
)


source_csv = (
    sample_data_folder
    / "multiple_cases.csv"
)


case_folder = (
    sample_data_folder
    / "multiple_csv_cases"
)


output_figure_folder = (
    script_folder
    / "output_figures"
)


output_data_folder = (
    script_folder
    / "output_data"
)


# Create required output folders.

case_folder.mkdir(
    exist_ok=True
)


output_figure_folder.mkdir(
    exist_ok=True
)


output_data_folder.mkdir(
    exist_ok=True
)


# ============================================================
# 4. CHECK SOURCE FILE
# ============================================================

if not source_csv.exists():

    raise FileNotFoundError(
        f"\nSample file not found:\n"
        f"{source_csv}"
    )


# ============================================================
# 5. CREATE DEMONSTRATION CASE FILES
# ============================================================

"""
The existing sample file contains:

Time_s
Case_A_V
Case_B_V
Case_C_V
Case_D_V


For this tutorial, we convert those columns into four
independent CSV files.

This makes the example immediately executable after
cloning the repository.
"""


source_data = pd.read_csv(
    source_csv
)


case_mapping = {

    "Case_A.csv":
        "Case_A_V",

    "Case_B.csv":
        "Case_B_V",

    "Case_C.csv":
        "Case_C_V",

    "Case_D.csv":
        "Case_D_V"

}


for filename, source_column in case_mapping.items():

    case_file = (
        case_folder
        / filename
    )


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


    case_data.to_csv(
        case_file,
        index=False
    )


print(
    "\n--- Demonstration CSV Files Ready ---"
)


for file in case_folder.glob(
    "*.csv"
):

    print(
        file.name
    )


# ============================================================
# 6. EXPECTED FOLDER STRUCTURE
# ============================================================

"""
After the first execution:

sample_data/
│
├── multiple_cases.csv
│
└── multiple_csv_cases/
    ├── Case_A.csv
    ├── Case_B.csv
    ├── Case_C.csv
    └── Case_D.csv


Each individual CSV contains:

Time_s
Voltage_V
"""


# ============================================================
# 7. EXPLICIT FILE LIST
# ============================================================

"""
The simplest approach is to manually define the files.

This is useful when only specific cases should be compared.
"""


csv_files = [

    case_folder
    / "Case_A.csv",

    case_folder
    / "Case_B.csv",

    case_folder
    / "Case_C.csv",

    case_folder
    / "Case_D.csv"

]


# ============================================================
# 8. CHECK ALL FILES
# ============================================================

for file in csv_files:

    if not file.exists():

        raise FileNotFoundError(
            f"CSV file not found: "
            f"{file}"
        )


# ============================================================
# 9. READ ONE FILE
# ============================================================

example_data = pd.read_csv(
    csv_files[0]
)


print(
    "\n--- First File ---"
)


print(
    csv_files[0].name
)


print(
    example_data.head()
)


print(
    "\nColumns:"
)


print(
    example_data.columns.tolist()
)


# ============================================================
# 10. BASIC MULTIPLE-FILE LOOP
# ============================================================

"""
Each file is loaded inside a loop.

The same X and Y columns are selected from every file.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for file in csv_files:

    data = pd.read_csv(
        file
    )


    ax.plot(
        data["Time_s"],
        data["Voltage_V"],
        linewidth=2,
        label=file.stem
    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Multiple CSV Case Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 11. WHAT IS file.stem?
# ============================================================

"""
For:

Case_A.csv


file.name returns:

Case_A.csv


file.stem returns:

Case_A


Therefore:

label=file.stem

automatically creates useful legend labels.
"""


for file in csv_files:

    print(
        "\nFull Path:",
        file
    )

    print(
        "Filename:",
        file.name
    )

    print(
        "Stem:",
        file.stem
    )

    print(
        "Extension:",
        file.suffix
    )


# ============================================================
# 12. AUTOMATIC FILE DISCOVERY
# ============================================================

"""
Instead of manually listing every file, Python can
automatically discover CSV files.

Use:

Path.glob()
"""


discovered_files = list(
    case_folder.glob(
        "*.csv"
    )
)


print(
    "\n--- Automatically Discovered Files ---"
)


for file in discovered_files:

    print(
        file.name
    )


# ============================================================
# 13. SORT FILES
# ============================================================

"""
Operating-system file order should not always be assumed.

Sorting provides predictable plotting order.
"""


discovered_files = sorted(
    case_folder.glob(
        "*.csv"
    )
)


print(
    "\n--- Sorted Files ---"
)


for file in discovered_files:

    print(
        file.name
    )


# ============================================================
# 14. AUTOMATIC MULTIPLE-FILE PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for file in discovered_files:

    data = pd.read_csv(
        file
    )


    ax.plot(
        data["Time_s"],
        data["Voltage_V"],
        linewidth=2,
        label=file.stem
    )


ax.set_xlabel(
    "Time [s]"
)

ax.set_ylabel(
    "Voltage [V]"
)

ax.set_title(
    "Automatically Discovered CSV Files"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 15. REQUIRED COLUMN VALIDATION
# ============================================================

"""
Never assume every CSV file contains the expected columns.

Required:

Time_s
Voltage_V
"""


required_columns = [

    "Time_s",

    "Voltage_V"

]


# ============================================================
# 16. VALIDATION FUNCTION
# ============================================================

def validate_columns(
    dataframe,
    required_columns,
    filename=None
):
    """
    Check whether required columns exist.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Dataset to validate.

    required_columns : list
        Required column names.

    filename : optional
        Filename used in the error message.
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
            f"\nFile: {filename}"
            f"\nAvailable columns:"
            f"\n{dataframe.columns.tolist()}"
        )


# ============================================================
# 17. VALIDATE EVERY FILE
# ============================================================

for file in discovered_files:

    data = pd.read_csv(
        file
    )


    validate_columns(
        data,
        required_columns,
        file.name
    )


print(
    "\nAll CSV files contain required columns."
)


# ============================================================
# 18. CLEAN COLUMN NAMES
# ============================================================

"""
Real measurement files may contain spaces such as:

" Time_s "

instead of:

"Time_s"


Clean column names before validation.
"""


for file in discovered_files:

    data = pd.read_csv(
        file
    )


    data.columns = (
        data.columns
        .str.strip()
    )


# ============================================================
# 19. DIFFERENT FILE LENGTHS
# ============================================================

"""
Different CSV files do NOT need the same number of rows
for ordinary plotting.

Example:

Case A:
1000 samples

Case B:
950 samples

Case C:
1200 samples


Each case can be plotted using its OWN X-axis:

ax.plot(
    data["Time_s"],
    data["Voltage_V"]
)


This works because each X/Y pair comes from the same file.
"""


print(
    "\n--- Number of Samples per File ---"
)


for file in discovered_files:

    data = pd.read_csv(
        file
    )


    print(
        file.stem,
        ":",
        len(data),
        "samples"
    )


# ============================================================
# 20. IMPORTANT - DIRECT SAMPLE-BY-SAMPLE COMPARISON
# ============================================================

"""
Different file lengths become important when performing
calculations such as:

Case A - Case B


Direct subtraction requires the data to be properly aligned.

Before performing sample-by-sample calculations, check:

- Same time vector?
- Same sampling frequency?
- Same number of samples?
- Same trigger/reference point?
- Same measurement window?


If not, the data may require:

Interpolation

Resampling

Time alignment

or merging based on a common coordinate.


Simple plotting does not require identical file lengths.
"""


# ============================================================
# 21. LOAD FILES INTO A DICTIONARY
# ============================================================

"""
A dictionary provides a convenient structure:

Case Name
    ↓
DataFrame
"""


datasets = {}


for file in discovered_files:

    datasets[
        file.stem
    ] = pd.read_csv(
        file
    )


print(
    "\n--- Dataset Dictionary ---"
)


print(
    datasets.keys()
)


# ============================================================
# 22. ACCESS ONE DATASET
# ============================================================

case_a_data = datasets[
    "Case_A"
]


print(
    "\n--- Case A ---"
)


print(
    case_a_data.head()
)


# ============================================================
# 23. PLOT FROM DICTIONARY
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name, data in datasets.items():

    ax.plot(
        data["Time_s"],
        data["Voltage_V"],
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
    "Dictionary-Based CSV Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 24. COMBINE FILES INTO ONE LONG-FORM DATAFRAME
# ============================================================

"""
A useful data-analysis structure is:

Time_s
Voltage_V
Case


Example:

0.000    48.0    Case_A
0.001    48.9    Case_A
...
0.000    48.2    Case_B
0.001    48.7    Case_B


This is called LONG FORMAT.
"""


combined_datasets = []


for file in discovered_files:

    data = pd.read_csv(
        file
    )


    data[
        "Case"
    ] = file.stem


    combined_datasets.append(
        data
    )


combined_data = pd.concat(
    combined_datasets,
    ignore_index=True
)


print(
    "\n--- Combined Dataset ---"
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
# 25. DISPLAY AVAILABLE CASES
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
# 26. SELECT ONE CASE FROM COMBINED DATA
# ============================================================

selected_case = combined_data[
    combined_data[
        "Case"
    ] == "Case_B"
]


print(
    "\n--- Selected Case B ---"
)


print(
    selected_case.head()
)


# ============================================================
# 27. PLOT COMBINED DATA BY CASE
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for case_name in combined_data[
    "Case"
].unique():

    case_data = combined_data[
        combined_data[
            "Case"
        ] == case_name
    ]


    ax.plot(
        case_data["Time_s"],
        case_data["Voltage_V"],
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
    "Combined CSV Dataset"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()

plt.show()


# ============================================================
# 28. SAVE COMBINED DATASET
# ============================================================

combined_csv = (
    output_data_folder
    / "combined_multiple_cases.csv"
)


combined_data.to_csv(
    combined_csv,
    index=False
)


print(
    "\nCombined dataset saved to:"
)


print(
    combined_csv
)


# ============================================================
# 29. SUMMARY STATISTICS FOR EACH FILE
# ============================================================

"""
Multiple files are often compared using summary metrics.

Examples:

Mean
Maximum
Minimum
Standard deviation
Peak value
"""


summary_results = []


for file in discovered_files:

    data = pd.read_csv(
        file
    )


    voltage = data[
        "Voltage_V"
    ]


    summary_results.append(
        {
            "Case":
                file.stem,

            "Samples":
                len(data),

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
    "\n--- Summary Statistics ---"
)


print(
    summary_data
)


# ============================================================
# 30. SAVE SUMMARY TABLE
# ============================================================

summary_csv = (
    output_data_folder
    / "multiple_csv_summary.csv"
)


summary_data.to_csv(
    summary_csv,
    index=False
)


print(
    "\nSummary table saved to:"
)


print(
    summary_csv
)


# ============================================================
# 31. BAR PLOT OF MAXIMUM VALUES
# ============================================================

"""
After processing multiple files, summary results can
themselves be visualized.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


bars = ax.bar(
    summary_data["Case"],
    summary_data["Maximum_V"]
)


ax.set_xlabel(
    "Case"
)

ax.set_ylabel(
    "Maximum Voltage [V]"
)

ax.set_title(
    "Maximum Voltage from Multiple CSV Files"
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
# 32. FILTER SAME TIME WINDOW FROM EACH FILE
# ============================================================

"""
Suppose only:

5 ms to 15 ms

is required.
"""


start_time = 0.005

end_time = 0.015


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for file in discovered_files:

    data = pd.read_csv(
        file
    )


    selected_window = data[
        (
            data["Time_s"]
            >= start_time
        )
        &
        (
            data["Time_s"]
            <= end_time
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
        label=file.stem
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
# 33. ONE SUBPLOT PER CSV FILE
# ============================================================

"""
Instead of putting every case on one axis, each file can
receive its own subplot.
"""


number_of_files = len(
    discovered_files
)


fig, axes = plt.subplots(
    number_of_files,
    1,
    figsize=(
        7,
        2.3 * number_of_files
    ),
    sharex=True
)


if number_of_files == 1:

    axes = [
        axes
    ]


for ax, file in zip(
    axes,
    discovered_files
):

    data = pd.read_csv(
        file
    )


    ax.plot(
        data["Time_s"],
        data["Voltage_V"],
        linewidth=2
    )


    ax.set_ylabel(
        "Voltage [V]"
    )


    ax.set_title(
        file.stem
    )


    ax.grid(
        True
    )


axes[-1].set_xlabel(
    "Time [s]"
)


fig.suptitle(
    "Individual CSV Cases"
)


plt.tight_layout()

plt.show()


# ============================================================
# 34. AUTOMATIC FILE LABEL CLEANING
# ============================================================

"""
Filename:

Case_A.csv


Default stem:

Case_A


For presentation, underscores can be replaced:

Case A
"""


for file in discovered_files:

    clean_label = (
        file.stem
        .replace(
            "_",
            " "
        )
    )


    print(
        clean_label
    )


# ============================================================
# 35. PLOT WITH CLEAN LABELS
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for file in discovered_files:

    data = pd.read_csv(
        file
    )


    clean_label = (
        file.stem
        .replace(
            "_",
            " "
        )
    )


    ax.plot(
        data["Time_s"],
        data["Voltage_V"],
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
# 36. SEARCH FILES USING A PATTERN
# ============================================================

"""
glob() can search for only selected filename patterns.

Examples:

Case_*.csv

Experiment_*.csv

Test_*.csv
"""


case_files = sorted(
    case_folder.glob(
        "Case_*.csv"
    )
)


print(
    "\n--- Files Matching Case_*.csv ---"
)


for file in case_files:

    print(
        file.name
    )


# ============================================================
# 37. RECURSIVE FILE SEARCH
# ============================================================

"""
rglob() searches through subfolders as well.

Example:

folder.rglob("*.csv")


Useful structure:

Experiment_Data/
    Day_1/
        Case_A.csv

    Day_2/
        Case_B.csv

    Day_3/
        Case_C.csv
"""


recursive_files = list(
    case_folder.rglob(
        "*.csv"
    )
)


print(
    "\nRecursive CSV Count:"
)


print(
    len(
        recursive_files
    )
)


# ============================================================
# 38. HANDLE EMPTY FOLDER
# ============================================================

"""
Always check whether any files were actually discovered.
"""


if len(
    discovered_files
) == 0:

    raise FileNotFoundError(
        f"No CSV files were found in:\n"
        f"{case_folder}"
    )


# ============================================================
# 39. HANDLE INVALID FILE
# ============================================================

"""
A robust processing loop may skip a damaged or invalid file
rather than terminating the entire analysis.

The decision to skip a research dataset should always be
reported and scientifically justified.
"""


valid_datasets = {}


for file in discovered_files:

    try:

        data = pd.read_csv(
            file
        )


        validate_columns(
            data,
            required_columns,
            file.name
        )


        valid_datasets[
            file.stem
        ] = data


    except Exception as error:

        print(
            f"\nCould not process "
            f"{file.name}:"
        )

        print(
            error
        )


print(
    "\nSuccessfully Loaded Cases:"
)


print(
    valid_datasets.keys()
)


# ============================================================
# 40. IMPORTANT RESEARCH NOTE
# ============================================================

"""
Do not silently ignore failed measurement files.

If a file cannot be processed:

Record:

- Filename
- Reason
- Missing column
- Corrupted row
- Instrument problem
- Processing decision


Research workflows should remain traceable.
"""


# ============================================================
# 41. REUSABLE MULTIPLE CSV FUNCTION
# ============================================================

def plot_multiple_csv_files(
    folder,
    file_pattern,
    x_column,
    y_column,
    x_label,
    y_label,
    title
):
    """
    Automatically discover and compare several CSV files.

    Parameters
    ----------
    folder : str or Path
        Folder containing CSV files.

    file_pattern : str
        File pattern such as "*.csv" or "Case_*.csv".

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

    folder = Path(
        folder
    )


    files = sorted(
        folder.glob(
            file_pattern
        )
    )


    if not files:

        raise FileNotFoundError(
            f"No files matching "
            f"'{file_pattern}' found in "
            f"{folder}"
        )


    fig, ax = plt.subplots(
        figsize=(7, 4.5)
    )


    for file in files:

        dataframe = pd.read_csv(
            file
        )


        required = [
            x_column,
            y_column
        ]


        validate_columns(
            dataframe,
            required,
            file.name
        )


        label = (
            file.stem
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
# 42. USE REUSABLE FUNCTION
# ============================================================

plot_multiple_csv_files(

    folder=case_folder,

    file_pattern="Case_*.csv",

    x_column="Time_s",

    y_column="Voltage_V",

    x_label="Time [s]",

    y_label="Voltage [V]",

    title="Automatic Multiple CSV Comparison"

)


# ============================================================
# 43. SAVE FINAL COMPARISON FIGURE
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


for file in discovered_files:

    data = pd.read_csv(
        file
    )


    label = (
        file.stem
        .replace(
            "_",
            " "
        )
    )


    ax.plot(
        data["Time_s"],
        data["Voltage_V"],
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
    "Multiple CSV Engineering Comparison"
)


ax.grid(
    True
)

ax.legend()


plt.tight_layout()


# ============================================================
# 44. SAVE PNG
# ============================================================

png_file = (
    output_figure_folder
    / "multiple_csv_files.png"
)


fig.savefig(
    png_file,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 45. SAVE PDF
# ============================================================

pdf_file = (
    output_figure_folder
    / "multiple_csv_files.pdf"
)


fig.savefig(
    pdf_file,
    bbox_inches="tight"
)


# ============================================================
# 46. SAVE SVG
# ============================================================

svg_file = (
    output_figure_folder
    / "multiple_csv_files.svg"
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
# 47. COMMON MISTAKE - MANUALLY READING EVERY FILE
# ============================================================

"""
Inefficient:

case_a = pd.read_csv(
    "Case_A.csv"
)

case_b = pd.read_csv(
    "Case_B.csv"
)

case_c = pd.read_csv(
    "Case_C.csv"
)

case_d = pd.read_csv(
    "Case_D.csv"
)


This becomes difficult when there are many files.


Better:

for file in files:

    data = pd.read_csv(
        file
    )
"""


# ============================================================
# 48. COMMON MISTAKE - ASSUMING FILE ORDER
# ============================================================

"""
Do not assume:

glob()

always returns files in the desired order.


Prefer:

files = sorted(
    folder.glob(
        "*.csv"
    )
)
"""


# ============================================================
# 49. COMMON MISTAKE - SAME COLUMN POSITION
# ============================================================

"""
Suppose:

Case_A.csv:

Time
Voltage
Current


Case_B.csv:

Sample
Time
Voltage
Current


Using:

data.iloc[:, 1]

selects different physical variables between files.


Meaningful column names such as:

data["Voltage_V"]

are generally safer.
"""


# ============================================================
# 50. COMMON MISTAKE - SAME NUMBER OF ROWS ASSUMPTION
# ============================================================

"""
Do not assume every file contains exactly:

1000 samples.


For plotting:

Different row counts are usually acceptable.


For sample-by-sample calculations:

The data must first be properly aligned.
"""


# ============================================================
# 51. COMMON MISTAKE - DIFFERENT TIME VECTORS
# ============================================================

"""
Two files may contain:

Case A:

0.000
0.001
0.002
...


Case B:

0.000
0.0005
0.0010
...


They have different sampling intervals.

Plotting is possible.

Direct subtraction is NOT automatically valid.

Consider:

Interpolation

Resampling

or alignment to a common time vector.
"""


# ============================================================
# 52. COMMON MISTAKE - DIFFERENT UNITS BETWEEN FILES
# ============================================================

"""
One file may contain:

Voltage [V]


Another may contain:

Voltage [mV]


Even if both columns are named:

Voltage


the numerical comparison would be incorrect.

Always verify:

- Units
- Scaling
- Sensor gain
- Probe attenuation
- Sampling conditions
"""


# ============================================================
# 53. COMMON MISTAKE - DUPLICATE LEGEND NAMES
# ============================================================

"""
Files such as:

Run1/data.csv

Run2/data.csv

Run3/data.csv


all have:

file.stem = "data"


Therefore the legend would contain duplicate labels.

In that situation, construct the label using the parent
folder:

label = file.parent.name
"""


# ============================================================
# 54. COMMON MISTAKE - TOO MANY FILES ON ONE FIGURE
# ============================================================

"""
Python can plot:

5 files

50 files

500 files


but displaying all of them on one figure may not be useful.

For many files, consider:

- Representative cases
- Summary statistics
- Mean + uncertainty
- Subplots
- Heatmaps
- Statistical distributions
- Automated result extraction
"""


# ============================================================
# 55. MULTIPLE CSV WORKFLOW
# ============================================================

"""
CSV Folder
    ↓
Discover Files
    ↓
Sort Files
    ↓
Loop Through Files
    ↓
Read CSV
    ↓
Clean Headers
    ↓
Validate Columns
    ↓
Select X / Y
    ↓
Plot Each Case
    ↓
Use Filename as Label
    ↓
Calculate Statistics
    ↓
Combine Results
    ↓
Save Figure
    ↓
Save Processed Data
"""


# ============================================================
# 56. ENGINEERING RESEARCH WORKFLOW
# ============================================================

"""
Experiment

    ↓

Case_A.csv

Case_B.csv

Case_C.csv

Case_D.csv

    ↓

Python File Discovery

    ↓

Automated Processing

    ↓

Same Variable Extracted from Every Case

    ↓

Comparison Plot

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
MULTIPLE CSV FILES


1. FIND ALL CSV FILES

files = sorted(
    folder.glob(
        "*.csv"
    )
)


------------------------------------------------------------


2. FIND SPECIFIC FILE PATTERN

files = sorted(
    folder.glob(
        "Case_*.csv"
    )
)


------------------------------------------------------------


3. LOOP THROUGH FILES

for file in files:

    data = pd.read_csv(
        file
    )


------------------------------------------------------------


4. AUTOMATIC LEGEND LABEL

label = file.stem


Case_A.csv

becomes:

Case_A


------------------------------------------------------------


5. CLEAN LABEL

label = (
    file.stem
    .replace(
        "_",
        " "
    )
)


Case_A

becomes:

Case A


------------------------------------------------------------


6. PLOT SAME VARIABLE FROM EVERY FILE

for file in files:

    data = pd.read_csv(
        file
    )

    ax.plot(
        data["Time_s"],
        data["Voltage_V"],
        label=file.stem
    )


------------------------------------------------------------


7. VALIDATE REQUIRED COLUMNS

required = [
    "Time_s",
    "Voltage_V"
]


Check every file before processing.


------------------------------------------------------------


8. STORE DATASETS IN DICTIONARY

datasets = {}


for file in files:

    datasets[
        file.stem
    ] = pd.read_csv(
        file
    )


------------------------------------------------------------


9. COMBINE FILES

Add:

data["Case"] = file.stem


Then:

combined = pd.concat(
    datasets,
    ignore_index=True
)


------------------------------------------------------------


10. SUMMARY STATISTICS

For each case calculate:

Mean

Minimum

Maximum

Standard deviation

Peak

Number of samples


------------------------------------------------------------


11. DIFFERENT FILE LENGTHS

Different file lengths are acceptable for:

Plotting


They require careful alignment for:

Direct subtraction

Error calculations

Average waveforms

Point-by-point comparison


------------------------------------------------------------


12. DIFFERENT TIME VECTORS

Check:

Sampling interval

Sampling frequency

Trigger point

Measurement duration


before numerical comparison.


------------------------------------------------------------


13. USE glob()

Manual:

Case_A.csv
Case_B.csv
Case_C.csv


Automatic:

folder.glob(
    "Case_*.csv"
)


This makes the workflow scalable.


------------------------------------------------------------


14. RESEARCH PRINCIPLE

Do not silently skip a failed file.

Record:

Which file failed

Why it failed

How it was handled


------------------------------------------------------------


15. COMPLETE WORKFLOW

Many CSV Files
      ↓
Discover
      ↓
Validate
      ↓
Read
      ↓
Select
      ↓
Clean
      ↓
Process
      ↓
Compare
      ↓
Summarize
      ↓
Plot
      ↓
Export


------------------------------------------------------------


NEXT:

12_multiple_excel_sheets.py


This will address:

One Excel Workbook
       ↓
Many Worksheets
       ↓
Case A
Case B
Case C
Case D
       ↓
Loop Through Sheets
       ↓
Select Same Columns
       ↓
Compare Automatically


We can cover:

workbook.sheet_names

Reading selected sheets

Reading every sheet

Skipping summary sheets

Automatic sheet labels

Different columns between sheets

Combining worksheets

Comparing one variable from every sheet

Subplots

Summary statistics

Saving combined results
"""
