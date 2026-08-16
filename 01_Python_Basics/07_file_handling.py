"""
============================================================
Python for Engineering and Research
07 - File Handling
============================================================

Purpose:
    Introduce basic file handling in Python and demonstrate
    how files can be created, read, written, appended, and
    processed in engineering and research workflows.

Topics:
    1. File paths
    2. Opening files
    3. Writing text files
    4. Reading text files
    5. Appending data
    6. File modes
    7. with statement
    8. Reading line-by-line
    9. pathlib
    10. Checking file existence
    11. Creating folders
    12. CSV files
    13. JSON files
    14. Engineering measurement example
    15. Saving calculated results

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. FILE HANDLING CONCEPT
# ============================================================

"""
Files allow data to remain stored after a Python
program has finished running.

Common research files include:

.txt    -> Plain text
.csv    -> Tabular numerical data
.json   -> Structured configuration/data
.xlsx   -> Microsoft Excel
.dat    -> Experimental/simulation data

Python can read existing files and create new ones.
"""


# ============================================================
# 2. FILE MODES
# ============================================================

"""
The open() function is used to open a file.

General syntax:

open("filename", "mode")


Important modes:

"r"     Read
"w"     Write
"a"     Append
"x"     Create new file

"rb"    Read binary
"wb"    Write binary


WARNING:

"w" overwrites existing file contents.

"a" adds new information without deleting
existing contents.
"""


# ============================================================
# 3. WRITE A TEXT FILE
# ============================================================

"""
The "w" mode creates a new file or overwrites
an existing file.
"""

file = open(
    "example.txt",
    "w"
)

file.write(
    "Python for Engineering and Research\n"
)

file.write(
    "This is a basic file-handling example.\n"
)

file.close()


print("--- File Created ---")
print("example.txt has been written.")


# ============================================================
# 4. WHY close() IS IMPORTANT
# ============================================================

"""
close() releases the file after the operation.

Instead of manually using:

file = open(...)
...
file.close()

Python normally recommends using:

with open(...) as file:

because the file is automatically closed.
"""


# ============================================================
# 5. USING WITH open()
# ============================================================

"""
Recommended approach:

with open(...) as file:

The file automatically closes after leaving
the indented block.
"""

with open(
    "engineering_notes.txt",
    "w"
) as file:

    file.write(
        "Engineering Research Notes\n"
    )

    file.write(
        "Input Voltage = 48 V\n"
    )

    file.write(
        "Switching Frequency = 100 kHz\n"
    )


print(
    "\nengineering_notes.txt created."
)


# ============================================================
# 6. READ COMPLETE FILE
# ============================================================

"""
read() returns the complete contents of a file.
"""

with open(
    "engineering_notes.txt",
    "r"
) as file:

    contents = file.read()


print("\n--- Complete File ---")

print(contents)


# ============================================================
# 7. READ ONE LINE
# ============================================================

"""
readline() reads one line at a time.
"""

with open(
    "engineering_notes.txt",
    "r"
) as file:

    first_line = file.readline()


print("--- First Line ---")

print(first_line)


# ============================================================
# 8. READ ALL LINES
# ============================================================

"""
readlines() returns the file contents as a list.

Each line becomes one list element.
"""

with open(
    "engineering_notes.txt",
    "r"
) as file:

    lines = file.readlines()


print("--- readlines() ---")

print(lines)


# ============================================================
# 9. LOOP THROUGH FILE
# ============================================================

"""
A file can be processed line-by-line.

This is useful for large files because the complete
file does not need to be loaded at once.
"""

print("\n--- Line-by-Line Reading ---")

with open(
    "engineering_notes.txt",
    "r"
) as file:

    for line in file:

        print(
            line.strip()
        )


# ============================================================
# 10. strip()
# ============================================================

"""
strip() removes unnecessary whitespace and newline
characters from the beginning/end of text.

Without strip():

"Voltage = 48 V\\n"

With strip():

"Voltage = 48 V"
"""


# ============================================================
# 11. APPEND TO FILE
# ============================================================

"""
The "a" mode adds new content without deleting
existing information.
"""

with open(
    "engineering_notes.txt",
    "a"
) as file:

    file.write(
        "Output Voltage = 96 V\n"
    )

    file.write(
        "Efficiency = 95 %\n"
    )


print(
    "\nNew information appended."
)


# Read again

with open(
    "engineering_notes.txt",
    "r"
) as file:

    print(
        file.read()
    )


# ============================================================
# 12. WRITE MULTIPLE LINES
# ============================================================

"""
writelines() writes multiple strings.

Newline characters must normally be supplied manually.
"""

measurements = [

    "48.2 V\n",

    "48.5 V\n",

    "49.0 V\n",

    "49.3 V\n"

]


with open(
    "voltage_measurements.txt",
    "w"
) as file:

    file.writelines(
        measurements
    )


print(
    "Voltage measurements saved."
)


# ============================================================
# 13. READ NUMERICAL VALUES FROM TEXT FILE
# ============================================================

"""
Assume the file contains one numerical value
on each line.

Example:

48.2
48.5
49.0
49.3
"""

numerical_measurements = [

    48.2,

    48.5,

    49.0,

    49.3

]


with open(
    "numerical_data.txt",
    "w"
) as file:

    for value in numerical_measurements:

        file.write(
            f"{value}\n"
        )


# Read numbers back

loaded_measurements = []


with open(
    "numerical_data.txt",
    "r"
) as file:

    for line in file:

        value = float(
            line.strip()
        )

        loaded_measurements.append(
            value
        )


print(
    "\n--- Loaded Numerical Data ---"
)

print(
    loaded_measurements
)


# ============================================================
# 14. FILE PATHS
# ============================================================

"""
Files may exist in:

- Current directory
- Subfolders
- Parent folders
- Absolute locations


Relative path example:

data/measurements.txt

Absolute path example on Windows:

C:/Users/User/Documents/data.txt

Absolute path example on Linux/macOS:

/home/user/data/data.txt
"""


# ============================================================
# 15. pathlib
# ============================================================

"""
pathlib is the recommended modern Python module
for working with file and folder paths.
"""

from pathlib import Path


file_path = Path(
    "engineering_notes.txt"
)


print("\n--- pathlib Example ---")

print(
    "File Path:",
    file_path
)


# ============================================================
# 16. CHECK WHETHER FILE EXISTS
# ============================================================

if file_path.exists():

    print(
        "File exists."
    )

else:

    print(
        "File does not exist."
    )


# ============================================================
# 17. FILE NAME AND EXTENSION
# ============================================================

print(
    "File Name:",
    file_path.name
)

print(
    "File Extension:",
    file_path.suffix
)

print(
    "File Stem:",
    file_path.stem
)


"""
For:

engineering_notes.txt

name:
engineering_notes.txt

stem:
engineering_notes

suffix:
.txt
"""


# ============================================================
# 18. CURRENT WORKING DIRECTORY
# ============================================================

current_folder = Path.cwd()


print(
    "\nCurrent Working Directory:"
)

print(
    current_folder
)


# ============================================================
# 19. CREATE A DIRECTORY
# ============================================================

"""
mkdir() creates a folder.

exist_ok=True prevents an error when the folder
already exists.
"""

data_folder = Path(
    "data"
)

data_folder.mkdir(
    exist_ok=True
)


print(
    "\nData folder created or already exists."
)


# ============================================================
# 20. CREATE FILE INSIDE FOLDER
# ============================================================

measurement_file = (
    data_folder
    / "measurements.txt"
)


with open(
    measurement_file,
    "w"
) as file:

    file.write(
        "48.2\n"
    )

    file.write(
        "49.1\n"
    )

    file.write(
        "50.0\n"
    )


print(
    "Measurement file created at:"
)

print(
    measurement_file
)


# ============================================================
# 21. CSV FILES
# ============================================================

"""
CSV means:

Comma-Separated Values

CSV files are extremely common for:

- Measurement data
- Oscilloscope exports
- Simulation results
- Experimental datasets
- Machine-learning datasets

Example:

Time,Voltage,Current
0.0,0,0
0.001,24,1.2
0.002,48,2.1
"""


# ============================================================
# 22. WRITE CSV FILE
# ============================================================

import csv


csv_file = (
    data_folder
    / "converter_measurements.csv"
)


with open(
    csv_file,
    "w",
    newline=""
) as file:

    writer = csv.writer(
        file
    )

    # Header

    writer.writerow(
        [
            "Time",
            "Voltage",
            "Current"
        ]
    )

    # Data

    writer.writerow(
        [
            0.000,
            0,
            0
        ]
    )

    writer.writerow(
        [
            0.001,
            24,
            1.2
        ]
    )

    writer.writerow(
        [
            0.002,
            48,
            2.1
        ]
    )

    writer.writerow(
        [
            0.003,
            49,
            2.0
        ]
    )


print(
    "\nCSV file created:"
)

print(
    csv_file
)


# ============================================================
# 23. WRITE MULTIPLE CSV ROWS
# ============================================================

data = [

    [0.000, 0, 0],

    [0.001, 24, 1.2],

    [0.002, 48, 2.1],

    [0.003, 49, 2.0]

]


another_csv = (
    data_folder
    / "measurement_table.csv"
)


with open(
    another_csv,
    "w",
    newline=""
) as file:

    writer = csv.writer(
        file
    )

    writer.writerow(
        [
            "Time_s",
            "Voltage_V",
            "Current_A"
        ]
    )

    writer.writerows(
        data
    )


# ============================================================
# 24. READ CSV FILE
# ============================================================

print(
    "\n--- Read CSV File ---"
)


with open(
    csv_file,
    "r"
) as file:

    reader = csv.reader(
        file
    )

    for row in reader:

        print(
            row
        )


# ============================================================
# 25. SKIP CSV HEADER
# ============================================================

"""
Sometimes we only want numerical rows.

next(reader) reads and skips the first row.
"""

print(
    "\n--- CSV Data Without Header ---"
)


with open(
    csv_file,
    "r"
) as file:

    reader = csv.reader(
        file
    )

    header = next(
        reader
    )

    print(
        "Header:",
        header
    )

    for row in reader:

        print(
            row
        )


# ============================================================
# 26. CONVERT CSV VALUES TO NUMBERS
# ============================================================

"""
CSV values are normally read as strings.

Therefore numerical conversion may be required.
"""

time_values = []
voltage_values = []
current_values = []


with open(
    csv_file,
    "r"
) as file:

    reader = csv.reader(
        file
    )

    next(
        reader
    )

    for row in reader:

        time = float(
            row[0]
        )

        voltage = float(
            row[1]
        )

        current = float(
            row[2]
        )

        time_values.append(
            time
        )

        voltage_values.append(
            voltage
        )

        current_values.append(
            current
        )


print(
    "\n--- Extracted CSV Columns ---"
)

print(
    "Time:",
    time_values
)

print(
    "Voltage:",
    voltage_values
)

print(
    "Current:",
    current_values
)


# ============================================================
# 27. CALCULATE POWER FROM CSV DATA
# ============================================================

power_values = []


for voltage, current in zip(
    voltage_values,
    current_values
):

    power = (
        voltage
        * current
    )

    power_values.append(
        power
    )


print(
    "\nCalculated Power:"
)

print(
    power_values
)


# ============================================================
# 28. SAVE CALCULATED RESULTS TO CSV
# ============================================================

results_file = (
    data_folder
    / "calculated_results.csv"
)


with open(
    results_file,
    "w",
    newline=""
) as file:

    writer = csv.writer(
        file
    )

    writer.writerow(
        [
            "Time_s",
            "Voltage_V",
            "Current_A",
            "Power_W"
        ]
    )

    for time, voltage, current, power in zip(

        time_values,

        voltage_values,

        current_values,

        power_values

    ):

        writer.writerow(
            [
                time,
                voltage,
                current,
                power
            ]
        )


print(
    "\nCalculated results saved:"
)

print(
    results_file
)


# ============================================================
# 29. JSON FILES
# ============================================================

"""
JSON means:

JavaScript Object Notation

JSON is useful for structured information such as:

- Simulation settings
- Model parameters
- Experiment configurations
- Software settings
- Metadata

Python dictionaries can easily be stored as JSON.
"""


import json


converter_parameters = {

    "converter": "Boost",

    "input_voltage_V": 48,

    "output_voltage_V": 96,

    "switching_frequency_Hz": 100000,

    "semiconductor": "GaN HEMT",

    "efficiency_percent": 95.0

}


json_file = (
    data_folder
    / "converter_parameters.json"
)


# ============================================================
# 30. WRITE JSON
# ============================================================

with open(
    json_file,
    "w"
) as file:

    json.dump(
        converter_parameters,
        file,
        indent=4
    )


print(
    "\nJSON file created:"
)

print(
    json_file
)


# ============================================================
# 31. READ JSON
# ============================================================

with open(
    json_file,
    "r"
) as file:

    loaded_parameters = json.load(
        file
    )


print(
    "\n--- Loaded JSON Data ---"
)

print(
    loaded_parameters
)


print(
    "Input Voltage:",
    loaded_parameters[
        "input_voltage_V"
    ],
    "V"
)


# ============================================================
# 32. ENGINEERING EXAMPLE
# ============================================================

"""
Example:

Store converter operating measurements in a CSV file,
read them again, calculate electrical power, and save
the processed results.

This represents a simplified research workflow:

Measurement
    ↓
File
    ↓
Python
    ↓
Calculation
    ↓
New Results File
"""


engineering_data = [

    [0.0, 48.0, 1.0],

    [0.1, 48.2, 1.5],

    [0.2, 48.5, 2.0],

    [0.3, 48.7, 2.5],

    [0.4, 49.0, 3.0]

]


input_file = (
    data_folder
    / "engineering_data.csv"
)


# Write measurement data

with open(
    input_file,
    "w",
    newline=""
) as file:

    writer = csv.writer(
        file
    )

    writer.writerow(
        [
            "Time_s",
            "Voltage_V",
            "Current_A"
        ]
    )

    writer.writerows(
        engineering_data
    )


# Read and process measurement data

processed_data = []


with open(
    input_file,
    "r"
) as file:

    reader = csv.reader(
        file
    )

    next(
        reader
    )

    for row in reader:

        time = float(
            row[0]
        )

        voltage = float(
            row[1]
        )

        current = float(
            row[2]
        )

        power = (
            voltage
            * current
        )

        processed_data.append(
            [
                time,
                voltage,
                current,
                power
            ]
        )


# Save processed results

output_file = (
    data_folder
    / "engineering_results.csv"
)


with open(
    output_file,
    "w",
    newline=""
) as file:

    writer = csv.writer(
        file
    )

    writer.writerow(
        [
            "Time_s",
            "Voltage_V",
            "Current_A",
            "Power_W"
        ]
    )

    writer.writerows(
        processed_data
    )


print(
    "\n--- Engineering File Workflow ---"
)

print(
    "Input File:",
    input_file
)

print(
    "Output File:",
    output_file
)


# ============================================================
# 33. DISPLAY PROCESSED RESULTS
# ============================================================

for row in processed_data:

    time = row[0]
    voltage = row[1]
    current = row[2]
    power = row[3]

    print(
        f"Time = {time:.2f} s | "
        f"Voltage = {voltage:.2f} V | "
        f"Current = {current:.2f} A | "
        f"Power = {power:.2f} W"
    )


# ============================================================
# 34. IMPORTANT NOTE ABOUT EXCEL FILES
# ============================================================

"""
Python can also read Microsoft Excel (.xlsx) files.

However, Excel handling normally requires external
libraries such as:

pandas
openpyxl

Example using Pandas:

import pandas as pd

data = pd.read_excel(
    "measurements.xlsx"
)

print(data)


We will cover Excel files thoroughly later in the
Pandas and Data Visualization sections.
"""


# ============================================================
# 35. IMPORTANT NOTE ABOUT PANDAS
# ============================================================

"""
The built-in csv module is useful for understanding
how CSV files work.

However, for research and engineering datasets,
Pandas usually provides a simpler and more powerful
approach.

Built-in CSV:

import csv

with open("data.csv") as file:
    reader = csv.reader(file)


Pandas:

import pandas as pd

data = pd.read_csv(
    "data.csv"
)


Later sections will cover:

- Selecting columns
- Removing rows
- Missing values
- Multiple CSV files
- Excel sheets
- Column names
- Data filtering
- Plotting CSV data
- Plotting Excel data
- Exporting processed datasets
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
FILE HANDLING


1. OPEN FILE

file = open(
    "data.txt",
    "r"
)


------------------------------------------------------------


2. RECOMMENDED APPROACH

with open(
    "data.txt",
    "r"
) as file:

    data = file.read()


The file automatically closes.


------------------------------------------------------------


3. FILE MODES

"r"     Read

"w"     Write / overwrite

"a"     Append

"x"     Create new file


------------------------------------------------------------


4. READ COMPLETE FILE

data = file.read()


------------------------------------------------------------


5. READ ONE LINE

line = file.readline()


------------------------------------------------------------


6. READ ALL LINES

lines = file.readlines()


------------------------------------------------------------


7. WRITE FILE

with open(
    "results.txt",
    "w"
) as file:

    file.write(
        "Result = 48 V"
    )


------------------------------------------------------------


8. APPEND FILE

with open(
    "results.txt",
    "a"
) as file:

    file.write(
        "New Result"
    )


------------------------------------------------------------


9. PATHLIB

from pathlib import Path

path = Path(
    "data/results.csv"
)


Useful:

path.exists()

path.name

path.stem

path.suffix

Path.cwd()


------------------------------------------------------------


10. CREATE FOLDER

folder = Path(
    "data"
)

folder.mkdir(
    exist_ok=True
)


------------------------------------------------------------


11. CSV

CSV files store tabular data.

Example:

Time,Voltage,Current

0.0,48,1

0.1,49,2


Python built-in module:

import csv


------------------------------------------------------------


12. JSON

Useful for structured configuration.

Example:

{
    "Vin": 48,
    "Vout": 96,
    "Fsw": 100000
}


Python:

import json


------------------------------------------------------------


COMMON ENGINEERING WORKFLOW


Measurement Equipment
        ↓
CSV / TXT / Excel
        ↓
Python
        ↓
Read Data
        ↓
Clean Data
        ↓
Perform Calculations
        ↓
Plot Results
        ↓
Save Processed Data
        ↓
Use in Report / Paper


------------------------------------------------------------


COMMON RESEARCH APPLICATIONS

File handling is used for:

- Oscilloscope data
- Simulation outputs
- Experimental measurements
- Voltage/current datasets
- FFT results
- EMI measurements
- Parameter sweeps
- Machine-learning datasets
- Configuration files
- Result logging
- Processed-data export


------------------------------------------------------------


IMPORTANT WARNING

Opening a file using:

"w"

will overwrite the previous content.

Use:

"a"

when existing contents should be retained.


------------------------------------------------------------


IMPORTANT FOR FUTURE SECTIONS

Basic Python:

open()
csv
json
pathlib

        ↓

Pandas:

pd.read_csv()
pd.read_excel()

        ↓

Data Cleaning

        ↓

Column Selection

        ↓

Matplotlib

        ↓

Multiple Variable Plotting

        ↓

Publication-Quality Figures
"""
