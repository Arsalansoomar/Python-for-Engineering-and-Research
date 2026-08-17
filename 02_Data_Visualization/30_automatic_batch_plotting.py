"""
============================================================
Python for Engineering and Research
30 - Automatic Batch Plotting
============================================================

Purpose:
    Demonstrate how large numbers of engineering CSV and
    Excel files can be processed, plotted, summarized, and
    exported automatically.

Topics:
    1. What is batch plotting?
    2. Why automate research figures?
    3. pathlib.Path
    4. Folder discovery
    5. glob()
    6. rglob()
    7. CSV batch processing
    8. Excel batch processing
    9. Multiple Excel sheets
    10. Automatic numerical-column detection
    11. Selecting X and Y columns
    12. Required-column validation
    13. Cleaning numerical data
    14. Safe output filenames
    15. Automatic plot titles
    16. Automatic PNG export
    17. Automatic PDF export
    18. Automatic SVG export
    19. Closing figures
    20. Logging
    21. Skipping invalid files
    22. Continue-on-error workflows
    23. Batch summary tables
    24. Multiple cases on one figure
    25. Batch FFT plotting
    26. Logarithmic frequency axes
    27. Automatic engineering statistics
    28. Recursive folder processing
    29. Configurable reusable functions
    30. Complete batch research workflow
    31. Common mistakes
    32. Key takeaways

Sample Files:
    sample_data/voltage_current.csv
    sample_data/multiple_cases.csv
    sample_data/fft_example.csv
    sample_data/converter_measurements.xlsx

Important:
    Batch automation should NEVER silently hide invalid
    files.

    A professional workflow should record:

    - What was processed
    - What was skipped
    - Why processing failed
    - Where outputs were saved

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. REQUIRED LIBRARIES
# ============================================================

import logging
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pathlib import Path


# ============================================================
# 2. WHAT IS BATCH PLOTTING?
# ============================================================

"""
Manual workflow:

File 1
    ↓
Open
    ↓
Plot
    ↓
Save

File 2
    ↓
Open
    ↓
Plot
    ↓
Save

File 3
    ↓
...


This becomes inefficient when the research contains:

10 files

50 files

500 files


------------------------------------------------------------


Batch workflow:

Folder
    ↓
Find Files Automatically
    ↓
Loop Through Files
    ↓
Validate
    ↓
Read
    ↓
Process
    ↓
Plot
    ↓
Save
    ↓
Close Figure
    ↓
Move to Next File
"""


# ============================================================
# 3. ENGINEERING APPLICATIONS
# ============================================================

"""
Batch plotting is useful for:

- Experimental measurements
- Oscilloscope exports
- Converter operating cases
- Parameter sweeps
- Monte Carlo simulations
- FFT spectra
- EMI measurements
- Power-quality datasets
- Temperature tests
- Control-response tests
- Multiple prototypes
- Machine-learning datasets
- Hardware validation
- Simulation-vs-experiment studies
- Daily / weekly test campaigns
"""


# ============================================================
# 4. PROJECT PATHS
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
    / "batch_plotting"
)


output_data_folder = (
    script_folder
    / "output_data"
    / "batch_plotting"
)


log_folder = (
    script_folder
    / "logs"
)


output_figure_folder.mkdir(
    parents=True,
    exist_ok=True
)


output_data_folder.mkdir(
    parents=True,
    exist_ok=True
)


log_folder.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 5. DISPLAY PROJECT PATHS
# ============================================================

print(
    "\n--- Batch Plotting Paths ---"
)


print(
    "Sample Data:"
)


print(
    sample_data_folder
)


print(
    "\nOutput Figures:"
)


print(
    output_figure_folder
)


print(
    "\nOutput Data:"
)


print(
    output_data_folder
)


# ============================================================
# 6. CONFIGURE LOGGING
# ============================================================

"""
Batch jobs should create a record of:

Successful files

Skipped files

Errors

Warnings


This becomes very useful when processing hundreds of
research files.
"""


log_file = (
    log_folder
    / "batch_plotting.log"
)


logging.basicConfig(

    filename=log_file,

    filemode="w",

    level=logging.INFO,

    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    )

)


logger = logging.getLogger(
    __name__
)


logger.info(
    "Batch plotting script started."
)


# ============================================================
# 7. SAFE FILENAME FUNCTION
# ============================================================

def make_safe_filename(
    text
):
    """
    Convert text into a safe filename.

    Examples
    --------
    "Output Voltage [V]"

    becomes approximately:

    "Output_Voltage_V"


    Parameters
    ----------
    text : str
        Original text.

    Returns
    -------
    str
        Filename-safe text.
    """

    text = str(
        text
    ).strip()


    text = re.sub(

        r"[^\w\-.]+",

        "_",

        text

    )


    text = re.sub(

        r"_+",

        "_",

        text

    )


    text = text.strip(
        "_."
    )


    if not text:

        text = "output"


    return text


# ============================================================
# 8. TEST SAFE FILENAMES
# ============================================================

example_names = [

    "Output Voltage [V]",

    "Case A / Test 1",

    "FFT: 10 kHz - 30 MHz",

    "Efficiency (%)"

]


print(
    "\n--- Safe Filename Examples ---"
)


for name in example_names:

    print(
        name,
        "->",
        make_safe_filename(
            name
        )
    )


# ============================================================
# 9. SAVE FIGURE IN MULTIPLE FORMATS
# ============================================================

def save_figure_multiple_formats(
    fig,
    output_folder,
    filename,
    formats=None,
    png_dpi=300
):
    """
    Save a Matplotlib figure in selected formats.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to save.

    output_folder : str or Path
        Destination folder.

    filename : str
        Base filename without extension.

    formats : list, optional
        Example:
        ["png", "pdf", "svg"]

    png_dpi : int
        PNG resolution.

    Returns
    -------
    list[Path]
        Saved file paths.
    """

    if formats is None:

        formats = [
            "png",
            "pdf",
            "svg"
        ]


    supported_formats = {

        "png",

        "pdf",

        "svg"

    }


    output_folder = Path(
        output_folder
    )


    output_folder.mkdir(
        parents=True,
        exist_ok=True
    )


    safe_name = make_safe_filename(
        filename
    )


    saved_files = []


    for file_format in formats:

        file_format = (
            file_format
            .lower()
            .strip()
        )


        if file_format not in supported_formats:

            logger.warning(

                "Unsupported format skipped: %s",

                file_format

            )

            continue


        output_path = (

            output_folder

            / (
                f"{safe_name}."
                f"{file_format}"
            )

        )


        if file_format == "png":

            fig.savefig(

                output_path,

                dpi=png_dpi,

                bbox_inches="tight"

            )

        else:

            fig.savefig(

                output_path,

                bbox_inches="tight"

            )


        saved_files.append(
            output_path
        )


    return saved_files


# ============================================================
# 10. WHY SAVE BEFORE plt.show()?
# ============================================================

"""
Recommended batch workflow:

Create Figure
      ↓
Format
      ↓
Save
      ↓
Close


Batch processing normally does NOT require:

plt.show()


for every figure.

Opening hundreds of windows would defeat the purpose of
automation.
"""


# ============================================================
# 11. AUTOMATIC NUMERICAL-COLUMN DETECTION
# ============================================================

def get_numeric_columns(
    dataframe
):
    """
    Return numerical DataFrame columns.

    Parameters
    ----------
    dataframe : pandas.DataFrame

    Returns
    -------
    list[str]
        Numerical column names.
    """

    numerical_columns = (

        dataframe
        .select_dtypes(
            include="number"
        )
        .columns
        .tolist()

    )


    return numerical_columns


# ============================================================
# 12. COLUMN DETECTION EXAMPLE
# ============================================================

example_dataframe = pd.DataFrame(
    {
        "Time_s":
            [
                0,
                1,
                2
            ],

        "Voltage_V":
            [
                10,
                11,
                12
            ],

        "Case":
            [
                "A",
                "A",
                "A"
            ],

        "Comment":
            [
                "Start",
                "Middle",
                "End"
            ]
    }
)


print(
    "\n--- Numerical Columns ---"
)


print(
    get_numeric_columns(
        example_dataframe
    )
)


# ============================================================
# 13. NUMERIC COERCION FUNCTION
# ============================================================

def convert_columns_to_numeric(
    dataframe,
    columns
):
    """
    Convert selected columns to numerical values.

    Invalid entries become:

    NaN
    """

    dataframe = dataframe.copy()


    for column in columns:

        if column not in dataframe.columns:

            raise KeyError(
                f"Column not found: {column}"
            )


        dataframe[
            column
        ] = pd.to_numeric(

            dataframe[
                column
            ],

            errors="coerce"

        )


    return dataframe


# ============================================================
# 14. REQUIRED COLUMN VALIDATION
# ============================================================

def validate_required_columns(
    dataframe,
    required_columns
):
    """
    Check that required columns exist.

    Returns
    -------
    tuple
        valid : bool

        missing_columns : list
    """

    missing_columns = [

        column

        for column in required_columns

        if column not in dataframe.columns

    ]


    return (

        len(
            missing_columns
        )
        == 0,

        missing_columns

    )


# ============================================================
# 15. BASIC CSV DISCOVERY
# ============================================================

"""
Find CSV files using:

Path.glob()
"""


csv_files = sorted(

    sample_data_folder.glob(
        "*.csv"
    )

)


print(
    "\n--- CSV Files Found ---"
)


for file_path in csv_files:

    print(
        file_path.name
    )


# ============================================================
# 16. RECURSIVE FILE DISCOVERY
# ============================================================

"""
Use:

rglob()

to search subfolders recursively.
"""


recursive_csv_files = sorted(

    sample_data_folder.rglob(
        "*.csv"
    )

)


print(
    "\nRecursive CSV Count:"
)


print(
    len(
        recursive_csv_files
    )
)


# ============================================================
# 17. glob() VS rglob()
# ============================================================

"""
glob("*.csv")

Searches:

Current folder only


------------------------------------------------------------


rglob("*.csv")

Searches:

Current folder
+
All subfolders


Use recursive searches carefully if the folder contains
thousands of files.
"""


# ============================================================
# 18. READ ONE CSV SAFELY
# ============================================================

def read_csv_safely(
    file_path
):
    """
    Read a CSV file.

    Returns
    -------
    dataframe : pandas.DataFrame or None

    error_message : str or None
    """

    file_path = Path(
        file_path
    )


    try:

        dataframe = pd.read_csv(
            file_path
        )


        if dataframe.empty:

            return (
                None,

                "CSV file is empty."
            )


        return (
            dataframe,

            None
        )


    except Exception as error:

        return (
            None,

            str(
                error
            )
        )


# ============================================================
# 19. TEST SAFE CSV READING
# ============================================================

for csv_file in csv_files:

    dataframe, error = (
        read_csv_safely(
            csv_file
        )
    )


    if error is None:

        print(
            f"\nLoaded: "
            f"{csv_file.name}"
        )


        print(
            "Shape:",
            dataframe.shape
        )

    else:

        print(
            f"\nFailed: "
            f"{csv_file.name}"
        )


        print(
            error
        )


# ============================================================
# 20. AUTOMATIC X-COLUMN DETECTION
# ============================================================

"""
Automatic plotting needs to determine:

Which column should be X?


Possible engineering X variables include:

Time

Frequency

Load

Temperature

Voltage

Current

Sample Number


A simple heuristic can search preferred names.
"""


preferred_x_keywords = [

    "time",

    "frequency",

    "load",

    "sample",

    "distance",

    "temperature"

]


def detect_x_column(
    dataframe,
    preferred_keywords=None
):
    """
    Automatically suggest an X column.

    Priority:
        1. Column name contains preferred keyword
        2. First numerical column

    Returns
    -------
    str
        Selected column name.
    """

    if preferred_keywords is None:

        preferred_keywords = (
            preferred_x_keywords
        )


    numeric_columns = get_numeric_columns(
        dataframe
    )


    if not numeric_columns:

        raise ValueError(
            "No numerical columns found."
        )


    for keyword in preferred_keywords:

        for column in numeric_columns:

            if keyword.lower() in column.lower():

                return column


    return numeric_columns[
        0
    ]


# ============================================================
# 21. DETECT Y COLUMNS
# ============================================================

def detect_y_columns(
    dataframe,
    x_column
):
    """
    Select numerical Y columns other than X.
    """

    numeric_columns = get_numeric_columns(
        dataframe
    )


    return [

        column

        for column in numeric_columns

        if column != x_column

    ]


# ============================================================
# 22. COLUMN-DETECTION EXAMPLE
# ============================================================

if csv_files:

    first_dataframe, error = (
        read_csv_safely(
            csv_files[
                0
            ]
        )
    )


    if error is None:

        selected_x = detect_x_column(
            first_dataframe
        )


        selected_y = detect_y_columns(

            first_dataframe,

            selected_x

        )


        print(
            "\n--- Automatic Column Detection ---"
        )


        print(
            "X:",
            selected_x
        )


        print(
            "Y:",
            selected_y
        )


# ============================================================
# 23. BASIC AUTOMATIC DATAFRAME PLOTTER
# ============================================================

def plot_dataframe_columns(
    dataframe,
    x_column,
    y_columns,
    title=None,
    x_label=None,
    y_label="Value",
    line_styles=None
):
    """
    Plot several Y columns against one X column.

    Parameters
    ----------
    dataframe : pandas.DataFrame

    x_column : str

    y_columns : list[str]

    title : str, optional

    x_label : str, optional

    y_label : str

    line_styles : list[str], optional

    Returns
    -------
    fig, ax
    """

    required_columns = [

        x_column

    ] + list(
        y_columns
    )


    valid, missing_columns = (
        validate_required_columns(

            dataframe,

            required_columns

        )
    )


    if not valid:

        raise KeyError(
            f"Missing columns: "
            f"{missing_columns}"
        )


    if not y_columns:

        raise ValueError(
            "At least one Y column is required."
        )


    cleaned = convert_columns_to_numeric(

        dataframe,

        required_columns

    )


    cleaned = cleaned.dropna(
        subset=[
            x_column
        ]
    )


    if cleaned.empty:

        raise ValueError(
            "No valid X values remain."
        )


    if line_styles is None:

        line_styles = [

            "-",

            "--",

            "-.",

            ":"

        ]


    fig, ax = plt.subplots(
        figsize=(8, 4.8)
    )


    plotted_count = 0


    for index, y_column in enumerate(
        y_columns
    ):

        valid_rows = cleaned[
            [
                x_column,
                y_column
            ]
        ].dropna()


        if valid_rows.empty:

            logger.warning(

                "No valid data for column: %s",

                y_column

            )

            continue


        ax.plot(

            valid_rows[
                x_column
            ],

            valid_rows[
                y_column
            ],

            linestyle=line_styles[
                index
                % len(
                    line_styles
                )
            ],

            label=y_column

        )


        plotted_count += 1


    if plotted_count == 0:

        plt.close(
            fig
        )


        raise ValueError(
            "No valid Y data available."
        )


    if x_label is None:

        x_label = x_column


    ax.set_xlabel(
        x_label
    )


    ax.set_ylabel(
        y_label
    )


    if title is not None:

        ax.set_title(
            title
        )


    ax.legend()


    ax.grid(
        True
    )


    fig.tight_layout()


    return (
        fig,
        ax
    )


# ============================================================
# 24. PLOT ONE CSV AUTOMATICALLY
# ============================================================

if csv_files:

    example_file = csv_files[
        0
    ]


    dataframe, error = (
        read_csv_safely(
            example_file
        )
    )


    if error is None:

        try:

            x_column = detect_x_column(
                dataframe
            )


            y_columns = detect_y_columns(

                dataframe,

                x_column

            )


            if y_columns:

                fig, ax = (
                    plot_dataframe_columns(

                        dataframe=dataframe,

                        x_column=x_column,

                        y_columns=y_columns,

                        title=example_file.stem,

                        y_label="Value"

                    )
                )


                plt.show()


        except Exception as error:

            print(
                error
            )


# ============================================================
# 25. BATCH CSV PROCESSING FUNCTION
# ============================================================

def batch_plot_csv_folder(
    input_folder,
    output_folder,
    recursive=False,
    formats=None,
    png_dpi=300,
    maximum_y_columns=None
):
    """
    Automatically plot all CSV files in a folder.

    Parameters
    ----------
    input_folder : str or Path
        Folder containing CSV files.

    output_folder : str or Path
        Destination for figures.

    recursive : bool
        Search subfolders if True.

    formats : list, optional
        Example:
        ["png", "pdf", "svg"]

    png_dpi : int

    maximum_y_columns : int, optional
        Limit number of automatically plotted Y columns.

    Returns
    -------
    summary : pandas.DataFrame
        Batch-processing results.
    """

    input_folder = Path(
        input_folder
    )


    output_folder = Path(
        output_folder
    )


    output_folder.mkdir(
        parents=True,
        exist_ok=True
    )


    if not input_folder.exists():

        raise FileNotFoundError(
            f"Input folder not found:\n"
            f"{input_folder}"
        )


    if recursive:

        file_paths = sorted(
            input_folder.rglob(
                "*.csv"
            )
        )

    else:

        file_paths = sorted(
            input_folder.glob(
                "*.csv"
            )
        )


    summary_rows = []


    logger.info(

        "CSV batch started. Files found: %d",

        len(
            file_paths
        )

    )


    for file_index, file_path in enumerate(
        file_paths,
        start=1
    ):

        print(
            f"\n[{file_index}/"
            f"{len(file_paths)}] "
            f"{file_path.name}"
        )


        logger.info(
            "Processing CSV: %s",
            file_path
        )


        row = {

            "File":
                str(
                    file_path
                ),

            "Status":
                "",

            "Rows":
                np.nan,

            "Columns":
                np.nan,

            "X_Column":
                "",

            "Y_Columns":
                "",

            "Figures_Saved":
                0,

            "Message":
                ""

        }


        try:

            dataframe, read_error = (
                read_csv_safely(
                    file_path
                )
            )


            if read_error is not None:

                raise ValueError(
                    read_error
                )


            row[
                "Rows"
            ] = len(
                dataframe
            )


            row[
                "Columns"
            ] = len(
                dataframe.columns
            )


            # ------------------------------------------------
            # Determine X column
            # ------------------------------------------------

            x_column = detect_x_column(
                dataframe
            )


            # ------------------------------------------------
            # Determine Y columns
            # ------------------------------------------------

            y_columns = detect_y_columns(

                dataframe,

                x_column

            )


            if maximum_y_columns is not None:

                y_columns = y_columns[
                    :maximum_y_columns
                ]


            if not y_columns:

                raise ValueError(
                    "No numerical Y columns found."
                )


            row[
                "X_Column"
            ] = x_column


            row[
                "Y_Columns"
            ] = ", ".join(
                y_columns
            )


            # ------------------------------------------------
            # Create figure
            # ------------------------------------------------

            fig, ax = plot_dataframe_columns(

                dataframe=dataframe,

                x_column=x_column,

                y_columns=y_columns,

                title=file_path.stem,

                x_label=x_column,

                y_label="Value"

            )


            # ------------------------------------------------
            # File-specific output folder
            # ------------------------------------------------

            relative_parent = (
                file_path.parent.relative_to(
                    input_folder
                )

                if recursive

                else Path()
            )


            file_output_folder = (

                output_folder

                / relative_parent

            )


            saved_files = (
                save_figure_multiple_formats(

                    fig=fig,

                    output_folder=(
                        file_output_folder
                    ),

                    filename=file_path.stem,

                    formats=formats,

                    png_dpi=png_dpi

                )
            )


            # ------------------------------------------------
            # CLOSE figure
            # ------------------------------------------------

            plt.close(
                fig
            )


            row[
                "Figures_Saved"
            ] = len(
                saved_files
            )


            row[
                "Status"
            ] = "Processed"


            row[
                "Message"
            ] = "Success"


            logger.info(
                "CSV processed successfully: %s",
                file_path
            )


        except Exception as error:

            row[
                "Status"
            ] = "Skipped"


            row[
                "Message"
            ] = str(
                error
            )


            logger.exception(
                "CSV processing failed: %s",
                file_path
            )


            print(
                "Skipped:",
                error
            )


        summary_rows.append(
            row
        )


    summary = pd.DataFrame(
        summary_rows
    )


    return summary


# ============================================================
# 26. WHY plt.close(fig) MATTERS
# ============================================================

"""
This is extremely important in batch plotting.

If 500 figures are created without closing them:

Memory usage may continuously increase.


Correct batch workflow:

fig, ax = plt.subplots(...)

...

fig.savefig(...)

plt.close(fig)


Do NOT leave hundreds of open figures.
"""


# ============================================================
# 27. RUN CSV BATCH EXAMPLE
# ============================================================

csv_batch_output = (
    output_figure_folder
    / "csv_files"
)


csv_batch_summary = (
    batch_plot_csv_folder(

        input_folder=sample_data_folder,

        output_folder=csv_batch_output,

        recursive=False,

        formats=[
            "png"
        ],

        png_dpi=300,

        maximum_y_columns=5

    )
)


print(
    "\n--- CSV Batch Summary ---"
)


print(
    csv_batch_summary
)


# ============================================================
# 28. SAVE CSV BATCH SUMMARY
# ============================================================

csv_summary_file = (
    output_data_folder
    / "csv_batch_summary.csv"
)


csv_batch_summary.to_csv(

    csv_summary_file,

    index=False

)


print(
    "\nCSV Summary Saved:"
)


print(
    csv_summary_file
)


# ============================================================
# 29. COUNT PROCESSED / SKIPPED FILES
# ============================================================

processed_csv_count = (

    csv_batch_summary[
        "Status"
    ]

    .eq(
        "Processed"
    )

    .sum()

)


skipped_csv_count = (

    csv_batch_summary[
        "Status"
    ]

    .eq(
        "Skipped"
    )

    .sum()

)


print(
    "\nProcessed CSV Files:"
)


print(
    processed_csv_count
)


print(
    "Skipped CSV Files:"
)


print(
    skipped_csv_count
)


# ============================================================
# 30. WHY CONTINUE AFTER ONE FAILURE?
# ============================================================

"""
Suppose:

100 files

are processed.


File 47 is corrupted.


Weak batch program:

Stops completely at File 47.


Better research workflow:

Record File 47 as failed

Continue processing:

48
49
50
...
100


At the end:

Review the failure log.
"""


# ============================================================
# 31. SINGLE-VARIABLE FIGURES
# ============================================================

"""
Sometimes one large multi-variable figure is not desired.

Instead:

Create one figure per variable.
"""


def plot_each_column_separately(
    dataframe,
    x_column,
    y_columns,
    output_folder,
    base_filename,
    formats=None,
    png_dpi=300
):
    """
    Create one figure per Y column.

    Returns
    -------
    list[Path]
        All generated figure paths.
    """

    output_folder = Path(
        output_folder
    )


    generated_files = []


    for y_column in y_columns:

        try:

            cleaned = convert_columns_to_numeric(

                dataframe,

                [
                    x_column,
                    y_column
                ]

            )


            cleaned = cleaned[
                [
                    x_column,
                    y_column
                ]
            ].dropna()


            if cleaned.empty:

                logger.warning(

                    "No valid data for %s",

                    y_column

                )

                continue


            fig, ax = plt.subplots(
                figsize=(7, 4.5)
            )


            ax.plot(

                cleaned[
                    x_column
                ],

                cleaned[
                    y_column
                ]

            )


            ax.set_xlabel(
                x_column
            )


            ax.set_ylabel(
                y_column
            )


            ax.set_title(
                y_column
            )


            ax.grid(
                True
            )


            fig.tight_layout()


            file_name = (

                f"{base_filename}_"
                f"{make_safe_filename(y_column)}"

            )


            saved_files = (
                save_figure_multiple_formats(

                    fig,

                    output_folder,

                    file_name,

                    formats=formats,

                    png_dpi=png_dpi

                )
            )


            generated_files.extend(
                saved_files
            )


            plt.close(
                fig
            )


        except Exception:

            logger.exception(

                "Failed plotting column: %s",

                y_column

            )


    return generated_files


# ============================================================
# 32. MULTIPLE CSV FILES ON ONE FIGURE
# ============================================================

"""
Another common engineering problem:

One file per case.


Example:

Baseline.csv

Design_A.csv

Design_B.csv

Design_C.csv


All files contain:

Time_s

Voltage_V


The goal is:

Compare all cases on one figure.
"""


def compare_csv_files(
    file_paths,
    x_column,
    y_column,
    output_folder,
    output_filename,
    x_label=None,
    y_label=None,
    formats=None
):
    """
    Compare the same X/Y columns across multiple CSV files.
    """

    file_paths = [

        Path(
            file_path
        )

        for file_path in file_paths

    ]


    fig, ax = plt.subplots(
        figsize=(8, 4.8)
    )


    styles = [

        "-",

        "--",

        "-.",

        ":"

    ]


    successful_cases = 0


    for index, file_path in enumerate(
        file_paths
    ):

        try:

            dataframe, error = (
                read_csv_safely(
                    file_path
                )
            )


            if error is not None:

                raise ValueError(
                    error
                )


            valid, missing = (
                validate_required_columns(

                    dataframe,

                    [
                        x_column,
                        y_column
                    ]

                )
            )


            if not valid:

                raise KeyError(
                    f"Missing columns: {missing}"
                )


            cleaned = convert_columns_to_numeric(

                dataframe,

                [
                    x_column,
                    y_column
                ]

            )


            cleaned = cleaned[
                [
                    x_column,
                    y_column
                ]
            ].dropna()


            if cleaned.empty:

                raise ValueError(
                    "No valid numerical data."
                )


            ax.plot(

                cleaned[
                    x_column
                ],

                cleaned[
                    y_column
                ],

                linestyle=styles[
                    index
                    % len(
                        styles
                    )
                ],

                label=file_path.stem

            )


            successful_cases += 1


        except Exception:

            logger.exception(

                "Case comparison failed: %s",

                file_path

            )


    if successful_cases == 0:

        plt.close(
            fig
        )


        raise ValueError(
            "No valid files available for comparison."
        )


    if x_label is None:

        x_label = x_column


    if y_label is None:

        y_label = y_column


    ax.set_xlabel(
        x_label
    )


    ax.set_ylabel(
        y_label
    )


    ax.legend()


    ax.grid(
        True
    )


    fig.tight_layout()


    saved_files = (
        save_figure_multiple_formats(

            fig,

            output_folder,

            output_filename,

            formats=formats

        )
    )


    plt.close(
        fig
    )


    return saved_files


# ============================================================
# 33. DIFFERENT FILE LENGTHS
# ============================================================

"""
Files do NOT need identical lengths merely to be plotted
together.

Example:

Case A:

1000 samples


Case B:

1500 samples


Both can be plotted using their own:

X

and

Y


arrays.


However:

Sample-by-sample subtraction requires appropriate:

Alignment

Interpolation

Resampling

or

Common X values.
"""


# ============================================================
# 34. DO NOT SUBTRACT BY ROW NUMBER AUTOMATICALLY
# ============================================================

"""
Incorrect assumption:

Case_A.iloc[100]

and:

Case_B.iloc[100]


represent the same physical time.


That is only true if:

Sampling

Timing

Alignment

and

data acquisition

match appropriately.
"""


# ============================================================
# 35. EXCEL FILE DISCOVERY
# ============================================================

excel_files = sorted(

    sample_data_folder.glob(
        "*.xlsx"
    )

)


print(
    "\n--- Excel Files Found ---"
)


for excel_file in excel_files:

    print(
        excel_file.name
    )


# ============================================================
# 36. READ EXCEL WORKBOOK INFORMATION
# ============================================================

for excel_file in excel_files:

    try:

        workbook = pd.ExcelFile(
            excel_file
        )


        print(
            f"\nWorkbook: "
            f"{excel_file.name}"
        )


        print(
            "Sheets:"
        )


        print(
            workbook.sheet_names
        )


    except Exception as error:

        logger.exception(

            "Could not inspect workbook: %s",

            excel_file

        )


        print(
            error
        )


# ============================================================
# 37. EXCEL SHEET PROCESSING FUNCTION
# ============================================================

def process_excel_sheet(
    excel_file,
    sheet_name,
    output_folder,
    formats=None,
    maximum_y_columns=5,
    png_dpi=300
):
    """
    Plot one Excel worksheet automatically.

    Returns
    -------
    dict
        Processing result.
    """

    excel_file = Path(
        excel_file
    )


    result = {

        "Workbook":
            excel_file.name,

        "Sheet":
            sheet_name,

        "Status":
            "",

        "Rows":
            np.nan,

        "Columns":
            np.nan,

        "X_Column":
            "",

        "Y_Columns":
            "",

        "Figures_Saved":
            0,

        "Message":
            ""

    }


    try:

        dataframe = pd.read_excel(

            excel_file,

            sheet_name=sheet_name

        )


        if dataframe.empty:

            raise ValueError(
                "Worksheet is empty."
            )


        result[
            "Rows"
        ] = len(
            dataframe
        )


        result[
            "Columns"
        ] = len(
            dataframe.columns
        )


        # ----------------------------------------------------
        # Convert possible numeric-looking columns
        # ----------------------------------------------------

        for column in dataframe.columns:

            converted = pd.to_numeric(

                dataframe[
                    column
                ],

                errors="coerce"

            )


            # If enough values convert successfully,
            # preserve the converted version.

            valid_ratio = (

                converted.notna().mean()

            )


            if valid_ratio >= 0.80:

                dataframe[
                    column
                ] = converted


        # ----------------------------------------------------
        # Detect plotting columns
        # ----------------------------------------------------

        x_column = detect_x_column(
            dataframe
        )


        y_columns = detect_y_columns(

            dataframe,

            x_column

        )


        y_columns = y_columns[
            :maximum_y_columns
        ]


        if not y_columns:

            raise ValueError(
                "No Y columns available."
            )


        result[
            "X_Column"
        ] = x_column


        result[
            "Y_Columns"
        ] = ", ".join(
            y_columns
        )


        # ----------------------------------------------------
        # Create figure
        # ----------------------------------------------------

        fig, ax = plot_dataframe_columns(

            dataframe=dataframe,

            x_column=x_column,

            y_columns=y_columns,

            title=(
                f"{excel_file.stem} - "
                f"{sheet_name}"
            ),

            x_label=x_column,

            y_label="Value"

        )


        # ----------------------------------------------------
        # Save
        # ----------------------------------------------------

        worksheet_output_folder = (

            Path(
                output_folder
            )

            / make_safe_filename(
                excel_file.stem
            )

        )


        output_name = (

            f"{excel_file.stem}_"
            f"{sheet_name}"

        )


        saved_files = (
            save_figure_multiple_formats(

                fig,

                worksheet_output_folder,

                output_name,

                formats=formats,

                png_dpi=png_dpi

            )
        )


        plt.close(
            fig
        )


        result[
            "Status"
        ] = "Processed"


        result[
            "Figures_Saved"
        ] = len(
            saved_files
        )


        result[
            "Message"
        ] = "Success"


    except Exception as error:

        result[
            "Status"
        ] = "Skipped"


        result[
            "Message"
        ] = str(
            error
        )


        logger.exception(

            "Excel sheet failed: %s | %s",

            excel_file,

            sheet_name

        )


    return result


# ============================================================
# 38. COMPLETE EXCEL BATCH FUNCTION
# ============================================================

def batch_plot_excel_folder(
    input_folder,
    output_folder,
    recursive=False,
    formats=None,
    maximum_y_columns=5,
    png_dpi=300
):
    """
    Process all Excel workbooks and all sheets.

    Returns
    -------
    pandas.DataFrame
        Processing summary.
    """

    input_folder = Path(
        input_folder
    )


    output_folder = Path(
        output_folder
    )


    if recursive:

        excel_paths = sorted(

            list(
                input_folder.rglob(
                    "*.xlsx"
                )
            )

            +

            list(
                input_folder.rglob(
                    "*.xls"
                )
            )

        )

    else:

        excel_paths = sorted(

            list(
                input_folder.glob(
                    "*.xlsx"
                )
            )

            +

            list(
                input_folder.glob(
                    "*.xls"
                )
            )

        )


    summary_rows = []


    for workbook_index, excel_file in enumerate(
        excel_paths,
        start=1
    ):

        print(
            f"\nWorkbook "
            f"{workbook_index}/"
            f"{len(excel_paths)}:"
        )


        print(
            excel_file.name
        )


        try:

            workbook = pd.ExcelFile(
                excel_file
            )


            sheet_names = (
                workbook.sheet_names
            )


        except Exception as error:

            logger.exception(

                "Workbook failed: %s",

                excel_file

            )


            summary_rows.append(
                {
                    "Workbook":
                        excel_file.name,

                    "Sheet":
                        "",

                    "Status":
                        "Skipped",

                    "Rows":
                        np.nan,

                    "Columns":
                        np.nan,

                    "X_Column":
                        "",

                    "Y_Columns":
                        "",

                    "Figures_Saved":
                        0,

                    "Message":
                        str(
                            error
                        )
                }
            )


            continue


        for sheet_name in sheet_names:

            print(
                "  Sheet:",
                sheet_name
            )


            result = process_excel_sheet(

                excel_file=excel_file,

                sheet_name=sheet_name,

                output_folder=output_folder,

                formats=formats,

                maximum_y_columns=(
                    maximum_y_columns
                ),

                png_dpi=png_dpi

            )


            summary_rows.append(
                result
            )


    return pd.DataFrame(
        summary_rows
    )


# ============================================================
# 39. RUN EXCEL BATCH
# ============================================================

excel_batch_output = (
    output_figure_folder
    / "excel_files"
)


excel_batch_summary = (
    batch_plot_excel_folder(

        input_folder=sample_data_folder,

        output_folder=excel_batch_output,

        recursive=False,

        formats=[
            "png"
        ],

        maximum_y_columns=5,

        png_dpi=300

    )
)


print(
    "\n--- Excel Batch Summary ---"
)


print(
    excel_batch_summary
)


# ============================================================
# 40. SAVE EXCEL SUMMARY
# ============================================================

excel_summary_file = (
    output_data_folder
    / "excel_batch_summary.csv"
)


excel_batch_summary.to_csv(

    excel_summary_file,

    index=False

)


# ============================================================
# 41. IMPORTANT EXCEL FORMULA NOTE
# ============================================================

"""
Some Excel workbooks contain formulas.

Depending on:

How the workbook was created

Whether formula results were cached

and

How it is read


formula-derived cells may not always contain immediately
available numerical values.


If a derived quantity such as:

Efficiency


is missing, it may need to be recalculated from numerical
source columns.


Example:

Efficiency [%]

=

Output Power
/
Input Power
×
100
"""


# ============================================================
# 42. GENERIC ENGINEERING SUMMARY STATISTICS
# ============================================================

def summarize_numeric_columns(
    dataframe
):
    """
    Calculate basic statistics for numerical columns.

    Returns
    -------
    pandas.DataFrame
    """

    numeric_data = dataframe.select_dtypes(
        include="number"
    )


    if numeric_data.empty:

        return pd.DataFrame()


    summary = numeric_data.agg(
        [
            "count",
            "mean",
            "std",
            "min",
            "max"
        ]
    ).T


    summary[
        "peak_to_peak"
    ] = (

        summary[
            "max"
        ]

        - summary[
            "min"
        ]

    )


    return summary


# ============================================================
# 43. SUMMARY STATISTICS EXAMPLE
# ============================================================

if csv_files:

    dataframe, error = (
        read_csv_safely(
            csv_files[
                0
            ]
        )
    )


    if error is None:

        numeric_summary = (
            summarize_numeric_columns(
                dataframe
            )
        )


        print(
            "\n--- Numeric Summary ---"
        )


        print(
            numeric_summary
        )


# ============================================================
# 44. SAVE SUMMARY FOR EVERY CSV FILE
# ============================================================

def batch_summarize_csv_files(
    input_folder,
    recursive=False
):
    """
    Calculate summary statistics for every CSV file.

    Returns
    -------
    pandas.DataFrame
        Long-form summary table.
    """

    input_folder = Path(
        input_folder
    )


    if recursive:

        files = sorted(
            input_folder.rglob(
                "*.csv"
            )
        )

    else:

        files = sorted(
            input_folder.glob(
                "*.csv"
            )
        )


    summary_rows = []


    for file_path in files:

        dataframe, error = (
            read_csv_safely(
                file_path
            )
        )


        if error is not None:

            continue


        statistics = (
            summarize_numeric_columns(
                dataframe
            )
        )


        if statistics.empty:

            continue


        statistics = (
            statistics
            .reset_index()
            .rename(
                columns={
                    "index":
                        "Variable"
                }
            )
        )


        statistics.insert(

            0,

            "File",

            file_path.name

        )


        summary_rows.append(
            statistics
        )


    if not summary_rows:

        return pd.DataFrame()


    return pd.concat(

        summary_rows,

        ignore_index=True

    )


# ============================================================
# 45. GENERATE FULL NUMERIC SUMMARY
# ============================================================

full_numeric_summary = (
    batch_summarize_csv_files(

        sample_data_folder

    )
)


if not full_numeric_summary.empty:

    full_summary_file = (
        output_data_folder
        / "all_csv_numeric_summary.csv"
    )


    full_numeric_summary.to_csv(

        full_summary_file,

        index=False

    )


    print(
        "\nFull Numerical Summary Saved:"
    )


    print(
        full_summary_file
    )


# ============================================================
# 46. SPECIALIZED FFT BATCH PLOTTING
# ============================================================

"""
Generic automatic plotting is useful,

but engineering research often benefits from specialized
plotters.

FFT files normally require:

- Frequency validation
- Positive X values
- Logarithmic X-axis
- dBµV Y-axis
- Defined frequency limits
"""


def plot_fft_file(
    file_path,
    output_folder,
    frequency_column="Frequency_Hz",
    case_columns=None,
    frequency_min=None,
    frequency_max=None,
    formats=None,
    png_dpi=300
):
    """
    Create an FFT / spectrum plot from one CSV file.

    Parameters
    ----------
    file_path : str or Path

    output_folder : str or Path

    frequency_column : str

    case_columns : list[str], optional

    frequency_min : float, optional

    frequency_max : float, optional

    formats : list, optional

    png_dpi : int

    Returns
    -------
    dict
        Processing result.
    """

    file_path = Path(
        file_path
    )


    result = {

        "File":
            file_path.name,

        "Status":
            "",

        "Frequency_Column":
            frequency_column,

        "Cases":
            "",

        "Points":
            np.nan,

        "Message":
            ""

    }


    try:

        dataframe = pd.read_csv(
            file_path
        )


        if frequency_column not in dataframe.columns:

            raise KeyError(
                f"Frequency column not found: "
                f"{frequency_column}"
            )


        if case_columns is None:

            case_columns = [

                column

                for column in dataframe.columns

                if (
                    column
                    != frequency_column
                    and pd.api.types.is_numeric_dtype(
                        dataframe[
                            column
                        ]
                    )
                )

            ]


        required = [

            frequency_column

        ] + list(
            case_columns
        )


        valid, missing = (
            validate_required_columns(

                dataframe,

                required

            )
        )


        if not valid:

            raise KeyError(
                f"Missing columns: {missing}"
            )


        dataframe = (
            convert_columns_to_numeric(

                dataframe,

                required

            )
        )


        dataframe = dataframe.dropna(
            subset=[
                frequency_column
            ]
        )


        dataframe = dataframe[
            dataframe[
                frequency_column
            ] > 0
        ]


        if frequency_min is not None:

            dataframe = dataframe[
                dataframe[
                    frequency_column
                ]
                >= frequency_min
            ]


        if frequency_max is not None:

            dataframe = dataframe[
                dataframe[
                    frequency_column
                ]
                <= frequency_max
            ]


        dataframe = dataframe.sort_values(
            frequency_column
        )


        if dataframe.empty:

            raise ValueError(
                "No valid positive frequency "
                "data remain."
            )


        fig, ax = plt.subplots(
            figsize=(8.5, 5)
        )


        line_styles = [

            "-",

            "--",

            "-.",

            ":"

        ]


        plotted_cases = []


        for index, column in enumerate(
            case_columns
        ):

            valid_case = dataframe[
                [
                    frequency_column,
                    column
                ]
            ].dropna()


            if valid_case.empty:

                continue


            ax.plot(

                valid_case[
                    frequency_column
                ],

                valid_case[
                    column
                ],

                linestyle=line_styles[
                    index
                    % len(
                        line_styles
                    )
                ],

                label=column

            )


            plotted_cases.append(
                column
            )


        if not plotted_cases:

            plt.close(
                fig
            )


            raise ValueError(
                "No valid spectrum cases found."
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
            file_path.stem
        )


        ax.legend()


        ax.grid(
            True,
            which="both"
        )


        fig.tight_layout()


        save_figure_multiple_formats(

            fig=fig,

            output_folder=output_folder,

            filename=(
                f"{file_path.stem}_FFT"
            ),

            formats=formats,

            png_dpi=png_dpi

        )


        plt.close(
            fig
        )


        result[
            "Status"
        ] = "Processed"


        result[
            "Cases"
        ] = ", ".join(
            plotted_cases
        )


        result[
            "Points"
        ] = len(
            dataframe
        )


        result[
            "Message"
        ] = "Success"


    except Exception as error:

        result[
            "Status"
        ] = "Skipped"


        result[
            "Message"
        ] = str(
            error
        )


        logger.exception(

            "FFT processing failed: %s",

            file_path

        )


    return result


# ============================================================
# 47. RUN FFT SAMPLE
# ============================================================

fft_sample_file = (
    sample_data_folder
    / "fft_example.csv"
)


if fft_sample_file.exists():

    fft_output_folder = (
        output_figure_folder
        / "fft"
    )


    fft_result = plot_fft_file(

        file_path=fft_sample_file,

        output_folder=fft_output_folder,

        frequency_column=(
            "Frequency_Hz"
        ),

        case_columns=[
            "Unshielded_dBuV",
            "Case_A_dBuV",
            "Case_B_dBuV",
            "Case_C_dBuV"
        ],

        frequency_min=10e3,

        frequency_max=30e6,

        formats=[
            "png",
            "pdf",
            "svg"
        ]

    )


    print(
        "\n--- FFT Batch Result ---"
    )


    print(
        fft_result
    )


# ============================================================
# 48. BATCH FFT FOLDER FUNCTION
# ============================================================

def batch_plot_fft_folder(
    input_folder,
    output_folder,
    frequency_column="Frequency_Hz",
    recursive=False,
    formats=None
):
    """
    Process every compatible FFT CSV file in a folder.
    """

    input_folder = Path(
        input_folder
    )


    if recursive:

        file_paths = sorted(
            input_folder.rglob(
                "*.csv"
            )
        )

    else:

        file_paths = sorted(
            input_folder.glob(
                "*.csv"
            )
        )


    summary_rows = []


    for file_path in file_paths:

        dataframe, error = (
            read_csv_safely(
                file_path
            )
        )


        if error is not None:

            continue


        if frequency_column not in dataframe.columns:

            continue


        candidate_cases = [

            column

            for column in dataframe.columns

            if column != frequency_column

        ]


        result = plot_fft_file(

            file_path=file_path,

            output_folder=output_folder,

            frequency_column=(
                frequency_column
            ),

            case_columns=(
                candidate_cases
            ),

            formats=formats

        )


        summary_rows.append(
            result
        )


    return pd.DataFrame(
        summary_rows
    )


# ============================================================
# 49. FFT SUMMARY
# ============================================================

fft_batch_summary = (
    batch_plot_fft_folder(

        input_folder=sample_data_folder,

        output_folder=(
            output_figure_folder
            / "fft_batch"
        ),

        frequency_column=(
            "Frequency_Hz"
        ),

        formats=[
            "png"
        ]

    )
)


if not fft_batch_summary.empty:

    fft_summary_file = (
        output_data_folder
        / "fft_batch_summary.csv"
    )


    fft_batch_summary.to_csv(

        fft_summary_file,

        index=False

    )


# ============================================================
# 50. BATCH PEAK EXTRACTION
# ============================================================

"""
Batch processing can do more than create figures.

It can also extract engineering metrics.

Example:

Maximum sampled spectral value

and its frequency.
"""


def calculate_spectrum_peak(
    dataframe,
    frequency_column,
    magnitude_column
):
    """
    Find maximum sampled spectral magnitude.

    Important:
        This identifies the maximum sampled point.

        It is not formal peak detection.
    """

    required = [

        frequency_column,

        magnitude_column

    ]


    dataframe = convert_columns_to_numeric(

        dataframe,

        required

    )


    valid = dataframe[
        required
    ].dropna()


    valid = valid[
        valid[
            frequency_column
        ] > 0
    ]


    if valid.empty:

        raise ValueError(
            "No valid spectrum data."
        )


    peak_index = valid[
        magnitude_column
    ].idxmax()


    return {

        "Peak_Frequency_Hz":
            valid.loc[
                peak_index,
                frequency_column
            ],

        "Peak_Magnitude":
            valid.loc[
                peak_index,
                magnitude_column
            ]

    }


# ============================================================
# 51. FFT PEAK SUMMARY EXAMPLE
# ============================================================

if fft_sample_file.exists():

    fft_dataframe = pd.read_csv(
        fft_sample_file
    )


    fft_peak_rows = []


    for magnitude_column in [
        "Unshielded_dBuV",
        "Case_A_dBuV",
        "Case_B_dBuV",
        "Case_C_dBuV"
    ]:

        if magnitude_column not in (
            fft_dataframe.columns
        ):

            continue


        try:

            peak = calculate_spectrum_peak(

                dataframe=fft_dataframe,

                frequency_column=(
                    "Frequency_Hz"
                ),

                magnitude_column=(
                    magnitude_column
                )

            )


            fft_peak_rows.append(
                {
                    "Case":
                        magnitude_column,

                    **peak
                }
            )


        except Exception:

            logger.exception(

                "Peak calculation failed: %s",

                magnitude_column

            )


    fft_peak_summary = pd.DataFrame(
        fft_peak_rows
    )


    print(
        "\n--- FFT Peak Summary ---"
    )


    print(
        fft_peak_summary
    )


    fft_peak_summary.to_csv(

        output_data_folder
        / "fft_peak_summary.csv",

        index=False

    )


# ============================================================
# 52. AUTOMATIC SUBPLOTS FOR MANY VARIABLES
# ============================================================

def plot_columns_as_subplots(
    dataframe,
    x_column,
    y_columns,
    title=None,
    maximum_columns=8
):
    """
    Create one vertically stacked subplot per variable.
    """

    if len(
        y_columns
    ) > maximum_columns:

        y_columns = y_columns[
            :maximum_columns
        ]


    if not y_columns:

        raise ValueError(
            "No Y columns provided."
        )


    required = [

        x_column

    ] + y_columns


    dataframe = convert_columns_to_numeric(

        dataframe,

        required

    )


    number_of_plots = len(
        y_columns
    )


    fig, axes = plt.subplots(

        number_of_plots,

        1,

        figsize=(
            8,
            max(
                3.0,
                number_of_plots
                * 2.2
            )
        ),

        sharex=True

    )


    if number_of_plots == 1:

        axes = np.array(
            [
                axes
            ]
        )


    for ax, y_column in zip(
        axes,
        y_columns
    ):

        valid = dataframe[
            [
                x_column,
                y_column
            ]
        ].dropna()


        ax.plot(

            valid[
                x_column
            ],

            valid[
                y_column
            ]

        )


        ax.set_ylabel(
            y_column
        )


        ax.grid(
            True
        )


    axes[
        -1
    ].set_xlabel(
        x_column
    )


    if title is not None:

        fig.suptitle(
            title
        )


    fig.tight_layout()


    return (
        fig,
        axes
    )


# ============================================================
# 53. WHY SUBPLOTS FOR DIFFERENT UNITS?
# ============================================================

"""
Suppose a CSV contains:

Voltage [V]

Current [A]

Power [W]

Temperature [°C]


Putting all four on one Y-axis may be misleading.


A better automatic approach may be:

Four aligned subplots

with:

Shared X axis.
"""


# ============================================================
# 54. BATCH SUBPLOT EXAMPLE
# ============================================================

voltage_current_file = (
    sample_data_folder
    / "voltage_current.csv"
)


if voltage_current_file.exists():

    dataframe = pd.read_csv(
        voltage_current_file
    )


    x_column = detect_x_column(
        dataframe
    )


    y_columns = detect_y_columns(

        dataframe,

        x_column

    )


    fig, axes = (
        plot_columns_as_subplots(

            dataframe=dataframe,

            x_column=x_column,

            y_columns=y_columns,

            title=(
                "Automatic Engineering Subplots"
            )

        )
    )


    save_figure_multiple_formats(

        fig,

        output_figure_folder
        / "automatic_subplots",

        "voltage_current_subplots",

        formats=[
            "png",
            "pdf"
        ]

    )


    plt.close(
        fig
    )


# ============================================================
# 55. RESEARCH CONFIGURATION DICTIONARY
# ============================================================

"""
A practical batch script should separate:

Configuration

from:

Processing logic.


This makes the script easier to reuse.
"""


batch_configuration = {

    "csv_input_folder":
        sample_data_folder,

    "excel_input_folder":
        sample_data_folder,

    "output_folder":
        output_figure_folder,

    "recursive":
        False,

    "png_dpi":
        300,

    "formats":
        [
            "png"
        ],

    "maximum_y_columns":
        5

}


print(
    "\n--- Batch Configuration ---"
)


for key, value in (
    batch_configuration.items()
):

    print(
        key,
        "=",
        value
    )


# ============================================================
# 56. COMPLETE RESEARCH BATCH FUNCTION
# ============================================================

def run_complete_batch_workflow(
    configuration
):
    """
    Run CSV and Excel processing from one configuration.

    Parameters
    ----------
    configuration : dict

    Returns
    -------
    dict
        Batch results.
    """

    required_configuration_keys = [

        "csv_input_folder",

        "excel_input_folder",

        "output_folder",

        "recursive",

        "png_dpi",

        "formats",

        "maximum_y_columns"

    ]


    missing_keys = [

        key

        for key in required_configuration_keys

        if key not in configuration

    ]


    if missing_keys:

        raise KeyError(
            f"Missing configuration keys: "
            f"{missing_keys}"
        )


    main_output = Path(
        configuration[
            "output_folder"
        ]
    )


    # --------------------------------------------------------
    # CSV processing
    # --------------------------------------------------------

    csv_results = batch_plot_csv_folder(

        input_folder=configuration[
            "csv_input_folder"
        ],

        output_folder=(
            main_output
            / "complete_batch_csv"
        ),

        recursive=configuration[
            "recursive"
        ],

        formats=configuration[
            "formats"
        ],

        png_dpi=configuration[
            "png_dpi"
        ],

        maximum_y_columns=configuration[
            "maximum_y_columns"
        ]

    )


    # --------------------------------------------------------
    # Excel processing
    # --------------------------------------------------------

    excel_results = batch_plot_excel_folder(

        input_folder=configuration[
            "excel_input_folder"
        ],

        output_folder=(
            main_output
            / "complete_batch_excel"
        ),

        recursive=configuration[
            "recursive"
        ],

        formats=configuration[
            "formats"
        ],

        png_dpi=configuration[
            "png_dpi"
        ],

        maximum_y_columns=configuration[
            "maximum_y_columns"
        ]

    )


    return {

        "csv":
            csv_results,

        "excel":
            excel_results

    }


# ============================================================
# 57. COMPLETE BATCH EXECUTION
# ============================================================

complete_results = (
    run_complete_batch_workflow(

        batch_configuration

    )
)


# ============================================================
# 58. COMBINE PROCESSING SUMMARIES
# ============================================================

csv_results = complete_results[
    "csv"
].copy()


excel_results = complete_results[
    "excel"
].copy()


if not csv_results.empty:

    csv_results[
        "Source_Type"
    ] = "CSV"


if not excel_results.empty:

    excel_results[
        "Source_Type"
    ] = "Excel"


# Different tables contain different columns.

combined_processing_summary = pd.concat(

    [
        csv_results,
        excel_results
    ],

    ignore_index=True,

    sort=False

)


combined_summary_file = (
    output_data_folder
    / "complete_batch_processing_summary.csv"
)


combined_processing_summary.to_csv(

    combined_summary_file,

    index=False

)


print(
    "\n--- Complete Processing Summary ---"
)


print(
    combined_processing_summary
)


# ============================================================
# 59. BATCH STATUS SUMMARY
# ============================================================

if not combined_processing_summary.empty:

    status_counts = (

        combined_processing_summary[
            "Status"
        ]

        .value_counts(
            dropna=False
        )

    )


    print(
        "\n--- Processing Status Counts ---"
    )


    print(
        status_counts
    )


# ============================================================
# 60. CREATE STATUS BAR CHART
# ============================================================

if not combined_processing_summary.empty:

    status_counts = (

        combined_processing_summary[
            "Status"
        ]

        .value_counts()

    )


    fig, ax = plt.subplots(
        figsize=(6, 4)
    )


    bars = ax.bar(

        status_counts.index,

        status_counts.values

    )


    ax.bar_label(
        bars
    )


    ax.set_xlabel(
        "Processing Status"
    )


    ax.set_ylabel(
        "Number of Items"
    )


    ax.set_title(
        "Batch Processing Summary"
    )


    ax.grid(
        True,
        axis="y"
    )


    fig.tight_layout()


    save_figure_multiple_formats(

        fig,

        output_figure_folder,

        "batch_processing_status",

        formats=[
            "png",
            "pdf"
        ]

    )


    plt.close(
        fig
    )


# ============================================================
# 61. PROGRESS DISPLAY
# ============================================================

"""
For long batch jobs, progress information is useful.

Simple approach:

[1/100]

[2/100]

[3/100]


This avoids the appearance that the script has stopped.
"""


# ============================================================
# 62. DO NOT PRINT ENTIRE DATAFRAME FOR EVERY FILE
# ============================================================

"""
During a 500-file batch:

Printing every row of every dataset can create enormous
terminal output.

Prefer:

Filename

Shape

Status

Important warning

Summary result
"""


# ============================================================
# 63. LOG FILE LOCATION
# ============================================================

print(
    "\n--- Log File ---"
)


print(
    log_file
)


logger.info(
    "Batch plotting script completed."
)


# ============================================================
# 64. COMMON MISTAKE - HARDCODED FILE NAMES
# ============================================================

"""
Weak batch workflow:

file1 = "test1.csv"

file2 = "test2.csv"

file3 = "test3.csv"

...


Better:

files = folder.glob(
    "*.csv"
)


The program automatically discovers available files.
"""


# ============================================================
# 65. COMMON MISTAKE - NO SORTING
# ============================================================

"""
File-system discovery order should not always be assumed.

Use:

sorted(...)


when deterministic processing order matters.
"""


# ============================================================
# 66. COMMON MISTAKE - LEXICOGRAPHIC SORTING
# ============================================================

"""
Consider filenames:

Case_1.csv

Case_2.csv

Case_10.csv


Normal string sorting may produce:

Case_1

Case_10

Case_2


If numerical ordering matters,

a natural-sort function may be needed.
"""


# ============================================================
# 67. NATURAL SORT KEY
# ============================================================

def natural_sort_key(
    text
):
    """
    Sort strings containing numbers naturally.

    Example:

    Case_1
    Case_2
    Case_10
    """

    return [

        int(
            part
        )

        if part.isdigit()

        else part.lower()

        for part in re.split(
            r"(\d+)",
            str(
                text
            )
        )

    ]


# ============================================================
# 68. NATURAL SORT EXAMPLE
# ============================================================

case_names = [

    "Case_1.csv",

    "Case_10.csv",

    "Case_2.csv",

    "Case_20.csv",

    "Case_3.csv"

]


print(
    "\n--- Normal Sort ---"
)


print(
    sorted(
        case_names
    )
)


print(
    "\n--- Natural Sort ---"
)


print(
    sorted(

        case_names,

        key=natural_sort_key

    )
)


# ============================================================
# 69. COMMON MISTAKE - ONE BAD FILE STOPS EVERYTHING
# ============================================================

"""
Use:

try:
    process()

except Exception:
    log()
    continue


for batch workflows where continuing is scientifically and
operationally appropriate.


Do not silently suppress errors.

Record them.
"""


# ============================================================
# 70. COMMON MISTAKE - NO FILE VALIDATION
# ============================================================

"""
A CSV extension does not guarantee:

Correct columns

Correct units

Correct data types

Correct experiment


Validate before plotting.
"""


# ============================================================
# 71. COMMON MISTAKE - AUTOMATIC COLUMN DETECTION TRUSTED BLINDLY
# ============================================================

"""
Automatic X/Y detection is convenient.

But:

Time_s

Temperature_C

Frequency_Hz


are all numerical.


A heuristic may select the wrong column.


For important research:

Specify expected columns explicitly whenever possible.
"""


# ============================================================
# 72. COMMON MISTAKE - DIFFERENT UNITS ON ONE AXIS
# ============================================================

"""
Automatic plotting may find:

Voltage_V

Current_A

Power_W

Temperature_C


Do not assume that every numerical column should share one
Y-axis.

Consider:

Subplots

Selected variables

Separate figures
"""


# ============================================================
# 73. COMMON MISTAKE - TOO MANY CURVES
# ============================================================

"""
A file containing:

50 numerical Y columns


can generate an unreadable plot.


Possible strategies:

Limit columns

Group related quantities

Use subplots

Generate one figure per variable

Use heatmaps

Create summary statistics
"""


# ============================================================
# 74. COMMON MISTAKE - NEVER CLOSING FIGURES
# ============================================================

"""
Bad:

for file in files:

    fig, ax = plt.subplots()

    ...

    fig.savefig(...)


No:

plt.close(fig)


Result:

Memory usage may grow continuously.


Correct:

fig.savefig(...)

plt.close(fig)
"""


# ============================================================
# 75. COMMON MISTAKE - plt.show() IN BATCH LOOP
# ============================================================

"""
Opening one interactive window for each of:

500 files


defeats automatic processing.


For batch mode:

Save

then:

Close.
"""


# ============================================================
# 76. COMMON MISTAKE - OVERWRITING OUTPUTS
# ============================================================

"""
Suppose every figure is saved as:

plot.png


Then each new figure overwrites the previous one.


Use descriptive filenames such as:

Case_A_voltage.png

Case_B_voltage.png

FFT_Test_01.png
"""


# ============================================================
# 77. COMMON MISTAKE - RAW AND PROCESSED DATA MIXED
# ============================================================

"""
Recommended structure:

sample_data/
or
raw_data/

    Original files


output_data/

    Processed tables


output_figures/

    Generated figures


logs/

    Processing records


Do not overwrite the raw experimental dataset.
"""


# ============================================================
# 78. COMMON MISTAKE - NO PROCESSING LOG
# ============================================================

"""
After processing 300 files:

You should be able to answer:

Which files succeeded?

Which failed?

Why?

How many figures were generated?

Where are they?
"""


# ============================================================
# 79. COMMON MISTAKE - IGNORING EMPTY FILES
# ============================================================

"""
Empty files should be:

Detected

Logged

Skipped


not converted into meaningless blank figures.
"""


# ============================================================
# 80. COMMON MISTAKE - IGNORING NaN
# ============================================================

"""
Invalid numerical values may become:

NaN


Plots and statistics should intentionally handle them.


Do not silently convert:

NaN

to:

0


unless zero is physically justified.
"""


# ============================================================
# 81. COMMON MISTAKE - SAMPLE-BY-SAMPLE CASE COMPARISON
# ============================================================

"""
Different files may have:

Different sampling frequency

Different starting time

Different number of samples

Different X grids


Before calculating:

Case B - Case A


align the data appropriately.
"""


# ============================================================
# 82. COMMON MISTAKE - FFT WITH NONPOSITIVE FREQUENCY
# ============================================================

"""
A logarithmic X-axis requires:

Frequency > 0


Validate before:

ax.set_xscale(
    "log"
)
"""


# ============================================================
# 83. COMMON MISTAKE - DB PERCENTAGE
# ============================================================

"""
Do not calculate:

Percentage reduction

directly from:

dBµV values.


Example:

100 dBµV
to
90 dBµV


is:

10 dB reduction


not automatically:

10% reduction.
"""


# ============================================================
# 84. COMMON MISTAKE - PEAK CALLED FORMAL PEAK DETECTION
# ============================================================

"""
Using:

idxmax()


finds:

Maximum sampled point.


It is NOT equivalent to:

Signal-processing peak detection

with:

Prominence

Width

Distance

Threshold


Those topics belong more naturally in the signal-processing
section.
"""


# ============================================================
# 85. COMMON MISTAKE - RECURSIVE SEARCH TOO BROAD
# ============================================================

"""
rglob("*.csv")


may accidentally include:

Processed files

Previous outputs

Temporary files

Backup folders


Use a clear project directory structure.
"""


# ============================================================
# 86. COMMON MISTAKE - OUTPUT FOLDER INSIDE INPUT SEARCH
# ============================================================

"""
Suppose:

Input folder

also contains:

output/

and recursive search is enabled.


The next script run may process its own previous outputs.


Keep:

Raw Input

and

Generated Output


separate whenever possible.
"""


# ============================================================
# 87. COMMON MISTAKE - AUTOMATION WITHOUT VISUAL CHECK
# ============================================================

"""
Automation saves time.

It does NOT remove the need to inspect results.


Recommended:

Generate all figures automatically

        ↓

Review representative cases

        ↓

Review failed / unusual cases

        ↓

Use selected figures for publication.
"""


# ============================================================
# 88. CSV BATCH WORKFLOW
# ============================================================

"""
CSV Folder
    ↓
glob()
    ↓
Sort Files
    ↓
For Each File
    ↓
Read
    ↓
Validate
    ↓
Detect / Select Columns
    ↓
Clean Numeric Data
    ↓
Plot
    ↓
Save
    ↓
Close
    ↓
Record Status
    ↓
Next File
"""


# ============================================================
# 89. EXCEL BATCH WORKFLOW
# ============================================================

"""
Excel Folder
      ↓
Find Workbooks
      ↓
For Each Workbook
      ↓
Read Sheet Names
      ↓
For Each Sheet
      ↓
Load Data
      ↓
Validate
      ↓
Detect Columns
      ↓
Plot
      ↓
Save
      ↓
Close
      ↓
Record Status
"""


# ============================================================
# 90. FFT BATCH WORKFLOW
# ============================================================

"""
FFT Files
    ↓
Verify Frequency Column
    ↓
Convert to Numeric
    ↓
Remove Invalid Frequencies
    ↓
Frequency > 0
    ↓
Select Cases
    ↓
Logarithmic X-axis
    ↓
Plot Spectra
    ↓
Calculate Sampled Peaks
    ↓
Save Figure
    ↓
Save Summary
"""


# ============================================================
# 91. EXPERIMENTAL CAMPAIGN WORKFLOW
# ============================================================

"""
Experiment 001
Experiment 002
Experiment 003
...
Experiment 500
        ↓
Raw CSV Folder
        ↓
Automatic Batch Script
        ↓
Figures
        +
Summary Metrics
        +
Logs
        ↓
Quality Check
        ↓
Selected Cases
        ↓
Paper / Thesis
"""


# ============================================================
# 92. SIMULATION PARAMETER-SWEEP WORKFLOW
# ============================================================

"""
Simulation Cases
        ↓
Case_001.csv
Case_002.csv
...
Case_N.csv
        ↓
Batch Processing
        ↓
Extract:
Peak
Mean
RMS
Final Value
        ↓
Generate:
Individual Figures
Comparison Figures
Summary Tables
        ↓
Parameter Analysis
"""


# ============================================================
# 93. RESEARCH FOLDER STRUCTURE
# ============================================================

"""
Recommended example:

project/
│
├── raw_data/
│   ├── experiment_001.csv
│   ├── experiment_002.csv
│   └── ...
│
├── scripts/
│   └── batch_plot.py
│
├── output_data/
│   ├── summary.csv
│   └── peaks.csv
│
├── output_figures/
│   ├── experiment_001.png
│   ├── experiment_002.png
│   └── ...
│
└── logs/
    └── batch_plotting.log
"""


# ============================================================
# 94. BATCH-PROCESSING CHECKLIST
# ============================================================

"""
Before running a large batch job:


INPUT
------------------------------------------------------------

Is the input folder correct?

Are raw files separated from output files?


DISCOVERY
------------------------------------------------------------

glob()?

or

rglob()?


ORDER
------------------------------------------------------------

Does processing order matter?

Normal sort?

Natural sort?


VALIDATION
------------------------------------------------------------

Are required columns defined?

Are units consistent?

Are numerical values valid?


PLOTTING
------------------------------------------------------------

Which column is X?

Which columns are Y?

Do different units require subplots?


FREQUENCY DATA
------------------------------------------------------------

Are all frequencies positive?

Should X be logarithmic?


OUTPUT
------------------------------------------------------------

Are filenames unique?

Are output folders created automatically?


MEMORY
------------------------------------------------------------

Is every figure closed after saving?


ERROR HANDLING
------------------------------------------------------------

Will one invalid file stop the entire batch?


LOGGING
------------------------------------------------------------

Are failures recorded?


SUMMARY
------------------------------------------------------------

Is a processing summary produced?


QUALITY CONTROL
------------------------------------------------------------

Will representative figures be manually inspected?
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
AUTOMATIC BATCH PLOTTING


1. FIND CSV FILES

files = sorted(

    folder.glob(
        "*.csv"
    )

)


------------------------------------------------------------


2. RECURSIVE SEARCH

files = sorted(

    folder.rglob(
        "*.csv"
    )

)


------------------------------------------------------------


3. FIND EXCEL FILES

files = sorted(

    folder.glob(
        "*.xlsx"
    )

)


------------------------------------------------------------


4. PROCESS FILES IN A LOOP

for file_path in files:

    dataframe = pd.read_csv(
        file_path
    )


------------------------------------------------------------


5. NUMERICAL COLUMNS

numeric_columns = (

    dataframe

    .select_dtypes(
        include="number"
    )

    .columns

    .tolist()

)


------------------------------------------------------------


6. COLUMN VALIDATION

required = [

    "Time_s",

    "Voltage_V"

]


missing = [

    column

    for column in required

    if column not in dataframe.columns

]


------------------------------------------------------------


7. NUMERIC COERCION

dataframe[
    column
] = pd.to_numeric(

    dataframe[
        column
    ],

    errors="coerce"

)


------------------------------------------------------------


8. SAFE FILENAMES

Convert:

"Output Voltage [V]"

into something like:

"Output_Voltage_V"


------------------------------------------------------------


9. MULTIPLE FORMATS

Save:

PNG

PDF

SVG


automatically.


------------------------------------------------------------


10. BATCH MODE

Usually:

DO NOT call plt.show()

for every figure.


Instead:

Save
    ↓
Close


------------------------------------------------------------


11. CLOSE FIGURES

plt.close(
    fig
)


Extremely important for large batch jobs.


------------------------------------------------------------


12. ERROR HANDLING

try:

    process_file()

except Exception as error:

    log_error()

    continue


------------------------------------------------------------


13. LOGGING

Use:

logging


to record:

Processed

Skipped

Failed

Warnings


------------------------------------------------------------


14. SUMMARY TABLE

Useful columns:

File

Status

Rows

Columns

X Column

Y Columns

Figures Saved

Message


------------------------------------------------------------


15. EXCEL WORKFLOW

Workbook
    ↓
sheet_names
    ↓
Loop Through Sheets
    ↓
Plot
    ↓
Save


------------------------------------------------------------


16. MULTIPLE FILE COMPARISON

One CSV per case:

Case A

Case B

Case C


can be plotted together when they contain compatible
physical variables.


------------------------------------------------------------


17. DIFFERENT FILE LENGTHS

Okay for independent plotting.


Not automatically okay for:

Sample-by-sample subtraction.


------------------------------------------------------------


18. FFT AUTOMATION

Validate:

Frequency_Hz > 0


then:

ax.set_xscale(
    "log"
)


------------------------------------------------------------


19. FFT PEAK

idxmax()

finds:

Maximum sampled point.


It is not formal signal-processing peak detection.


------------------------------------------------------------


20. dB DATA

Difference:

100 dBµV
-
90 dBµV

=

10 dB


Do not calculate ordinary percentage directly from dB
values.


------------------------------------------------------------


21. SUBPLOTS

Useful when automatically detected variables have
different units:

Voltage

Current

Power

Temperature


------------------------------------------------------------


22. NATURAL SORTING

Useful for:

Case_1

Case_2

Case_10


instead of:

Case_1

Case_10

Case_2


------------------------------------------------------------


23. KEEP RAW DATA SEPARATE

raw_data/

output_data/

output_figures/

logs/


------------------------------------------------------------


24. AUTOMATION != BLIND TRUST

Always inspect:

Representative outputs

Failures

Outliers

Unexpected plots


------------------------------------------------------------


25. ENGINEERING APPLICATIONS

Batch plotting is especially useful for:

Experimental campaigns

Parameter sweeps

FFT / EMI studies

Monte Carlo results

Hardware validation

Simulation cases

Temperature testing

Control experiments

ML datasets


------------------------------------------------------------


26. MOST IMPORTANT PRINCIPLE

A good batch-processing script should answer:

What files were found?

What files were processed?

What files failed?

Why did they fail?

What variables were plotted?

Where were figures saved?

What numerical summary was generated?


------------------------------------------------------------


27. COMPLETE WORKFLOW

Research Data Folder
        ↓
Discover Files
        ↓
Sort
        ↓
Validate
        ↓
Read
        ↓
Clean
        ↓
Select Variables
        ↓
Plot
        ↓
Save
        ↓
Close Figure
        ↓
Calculate Metrics
        ↓
Record Status
        ↓
Continue
        ↓
Summary Table
        ↓
Log File
        ↓
Quality Check
        ↓
Research Results


------------------------------------------------------------


NEXT:

31_3d_engineering_plots.py


The next file will cover:

3D axes

3D scatter plots

3D line plots

Surface plots

plot_surface()

Wireframe plots

Mesh grids

Parameter-response surfaces

Efficiency vs load and frequency

Power-loss surfaces

Temperature surfaces

3D color mapping

Colorbars

Viewing angles

Elevation / azimuth

Scatter + surface comparison

Marking optimum points

Multiple operating cases

3D vs contour plots

When 2D contour plots are clearer

Publication limitations of 3D figures

and engineering/research best practices.
"""
