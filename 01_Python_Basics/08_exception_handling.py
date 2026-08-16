"""
============================================================
Python for Engineering and Research
08 - Exception Handling
============================================================

Purpose:
    Introduce exception handling in Python and demonstrate
    how errors can be detected and managed without causing
    an entire program to terminate unexpectedly.

Topics:
    1. What is an exception?
    2. try and except
    3. Handling specific exceptions
    4. Multiple exceptions
    5. else
    6. finally
    7. File errors
    8. Invalid numerical data
    9. Dictionary and list errors
    10. raise
    11. Input validation
    12. Engineering calculation protection
    13. CSV data validation
    14. Processing multiple measurement files safely

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT IS AN EXCEPTION?
# ============================================================

"""
An exception is an error that occurs while a Python
program is running.

Examples:

ZeroDivisionError
    Dividing by zero

ValueError
    Invalid numerical conversion

FileNotFoundError
    Requested file does not exist

TypeError
    Incorrect data type

KeyError
    Dictionary key does not exist

IndexError
    List index does not exist


Without exception handling, an error may terminate
the complete Python program.
"""


# ============================================================
# 2. BASIC try / except
# ============================================================

"""
General syntax:

try:
    code_that_may_fail

except:
    code_to_run_if_error_occurs
"""

print("--- Basic Exception Handling ---")

try:

    result = 10 / 0

except:

    print(
        "An error occurred."
    )


# ============================================================
# 3. HANDLE A SPECIFIC EXCEPTION
# ============================================================

"""
It is better to catch specific exceptions rather
than using a general except statement.
"""

print("\n--- ZeroDivisionError ---")

try:

    result = 10 / 0

except ZeroDivisionError:

    print(
        "Error: Division by zero is not allowed."
    )


# ============================================================
# 4. SUCCESSFUL EXECUTION
# ============================================================

try:

    result = 10 / 2

    print(
        "\nResult =",
        result
    )

except ZeroDivisionError:

    print(
        "Division by zero detected."
    )


# ============================================================
# 5. VALUE ERROR
# ============================================================

"""
ValueError occurs when the data type is valid for an
operation but the supplied value is inappropriate.

Example:

float("abc")

cannot convert the text "abc" into a number.
"""

print("\n--- ValueError Example ---")

measurement = "48.5"

try:

    voltage = float(
        measurement
    )

    print(
        "Voltage =",
        voltage,
        "V"
    )

except ValueError:

    print(
        "Invalid voltage measurement."
    )


# Invalid example

measurement = "invalid"

try:

    voltage = float(
        measurement
    )

except ValueError:

    print(
        "Cannot convert measurement to float:",
        measurement
    )


# ============================================================
# 6. MULTIPLE EXCEPTIONS
# ============================================================

"""
Different errors can be handled separately.
"""

print("\n--- Multiple Exceptions ---")


value = "48"
divisor = 0


try:

    number = float(
        value
    )

    result = (
        number
        / divisor
    )


except ValueError:

    print(
        "The supplied value is not numerical."
    )


except ZeroDivisionError:

    print(
        "The divisor cannot be zero."
    )


# ============================================================
# 7. CATCH MULTIPLE EXCEPTIONS TOGETHER
# ============================================================

"""
Several exception types can also use the same handler.
"""

value = "abc"

try:

    result = (
        float(value)
        / 2
    )

except (
    ValueError,
    TypeError
):

    print(
        "\nInvalid numerical input."
    )


# ============================================================
# 8. DISPLAY THE ERROR MESSAGE
# ============================================================

"""
The exception object can be stored using:

except ExceptionType as error:

This allows Python's original error message to be displayed.
"""

print("\n--- Exception Message ---")

try:

    number = float(
        "not_a_number"
    )

except ValueError as error:

    print(
        "Error:",
        error
    )


# ============================================================
# 9. ELSE
# ============================================================

"""
else runs only when NO exception occurs.

Structure:

try:
    ...

except:
    ...

else:
    ...
"""

print("\n--- try / except / else ---")

voltage_text = "48.2"


try:

    voltage = float(
        voltage_text
    )


except ValueError:

    print(
        "Invalid voltage."
    )


else:

    print(
        "Measurement successfully converted."
    )

    print(
        "Voltage =",
        voltage,
        "V"
    )


# ============================================================
# 10. FINALLY
# ============================================================

"""
finally runs whether an exception occurs or not.

This is useful for cleanup operations.

Structure:

try:
    ...

except:
    ...

finally:
    ...
"""

print("\n--- finally Example ---")


try:

    result = 100 / 5


except ZeroDivisionError:

    print(
        "Division error."
    )


finally:

    print(
        "Calculation attempt completed."
    )


# ============================================================
# 11. COMPLETE STRUCTURE
# ============================================================

"""
A complete exception-handling structure can contain:

try
except
else
finally
"""

print("\n--- Complete Structure ---")


try:

    input_voltage = float(
        "48.0"
    )


except ValueError:

    print(
        "Invalid input voltage."
    )


else:

    print(
        "Voltage successfully loaded:",
        input_voltage,
        "V"
    )


finally:

    print(
        "Voltage processing completed."
    )


# ============================================================
# 12. FILE NOT FOUND
# ============================================================

"""
FileNotFoundError is particularly important in research
and data-analysis scripts.

A script should provide a meaningful message when the
requested measurement file does not exist.
"""

print("\n--- FileNotFoundError ---")


try:

    with open(
        "missing_measurement_file.csv",
        "r"
    ) as file:

        data = file.read()


except FileNotFoundError:

    print(
        "Measurement file was not found."
    )


# ============================================================
# 13. pathlib FILE CHECK
# ============================================================

"""
Files can also be checked before opening them.
"""

from pathlib import Path


file_path = Path(
    "measurement_data.csv"
)


print("\n--- File Existence Check ---")


if file_path.exists():

    print(
        "Measurement file exists."
    )

else:

    print(
        "Measurement file does not exist."
    )


# ============================================================
# 14. TYPE ERROR
# ============================================================

"""
TypeError occurs when an operation receives an
incompatible data type.
"""

print("\n--- TypeError Example ---")


voltage = "48"
current = 5


try:

    power = (
        voltage
        * current
    )

    print(
        power
    )


except TypeError as error:

    print(
        "Type error:",
        error
    )


"""
Note:

In this particular example, multiplying a string by an
integer is actually allowed in Python:

"48" * 5

produces repeated text.

Therefore engineering data should often be explicitly
converted and validated before calculations.
"""


# ============================================================
# 15. SAFE NUMERICAL CONVERSION
# ============================================================

"""
A function can safely convert measurement values.
"""


def convert_to_float(
    value
):

    try:

        return float(
            value
        )

    except (
        ValueError,
        TypeError
    ):

        return None


print("\n--- Safe Conversion ---")


measurements = [
    "48.2",
    "49.0",
    "invalid",
    None,
    "50.1"
]


for measurement in measurements:

    value = convert_to_float(
        measurement
    )

    print(
        measurement,
        "->",
        value
    )


# ============================================================
# 16. SKIP INVALID MEASUREMENTS
# ============================================================

"""
Invalid values can be ignored while valid values continue
to be processed.

This is useful when a dataset contains corrupted entries.
"""

measurements = [
    "48.2",
    "49.1",
    "ERROR",
    "50.3",
    "",
    "51.0"
]


valid_measurements = []


print("\n--- Measurement Validation ---")


for measurement in measurements:

    try:

        value = float(
            measurement
        )

        valid_measurements.append(
            value
        )


    except ValueError:

        print(
            "Invalid measurement ignored:",
            repr(measurement)
        )


print(
    "Valid Measurements:",
    valid_measurements
)


# ============================================================
# 17. DIVISION BY ZERO IN ENGINEERING CALCULATIONS
# ============================================================

"""
Efficiency:

eta = Pout / Pin * 100

If Pin = 0, division by zero occurs.
"""


def calculate_efficiency(
    input_power,
    output_power
):

    try:

        efficiency = (
            output_power
            / input_power
        ) * 100

        return efficiency


    except ZeroDivisionError:

        print(
            "Input power cannot be zero."
        )

        return None


print("\n--- Safe Efficiency Calculation ---")


efficiency = calculate_efficiency(
    input_power=500,
    output_power=475
)


print(
    "Efficiency:",
    efficiency
)


efficiency = calculate_efficiency(
    input_power=0,
    output_power=100
)


print(
    "Efficiency:",
    efficiency
)


# ============================================================
# 18. BETTER VALIDATION BEFORE CALCULATION
# ============================================================

"""
Exception handling is useful, but predictable engineering
conditions should often be checked explicitly.

For example, instead of relying only on ZeroDivisionError,
we can validate the input first.
"""


def safe_efficiency(
    input_power,
    output_power
):

    if input_power <= 0:

        return None

    return (
        output_power
        / input_power
    ) * 100


print("\n--- Input Validation ---")


result = safe_efficiency(
    500,
    475
)


print(
    "Efficiency =",
    result
)


# ============================================================
# 19. KEY ERROR
# ============================================================

"""
KeyError occurs when a dictionary key does not exist.
"""

converter = {

    "Vin": 48,

    "Vout": 96,

    "Fsw": 100000
}


print("\n--- KeyError ---")


try:

    efficiency = converter[
        "Efficiency"
    ]


except KeyError:

    print(
        "Efficiency parameter is not available."
    )


# ============================================================
# 20. SAFER DICTIONARY ACCESS
# ============================================================

"""
For expected missing values, dictionary.get() is often
simpler than exception handling.
"""


efficiency = converter.get(
    "Efficiency",
    "Not Available"
)


print(
    "Efficiency:",
    efficiency
)


# ============================================================
# 21. INDEX ERROR
# ============================================================

"""
IndexError occurs when a requested list position
does not exist.
"""

voltage_values = [
    48,
    50,
    52
]


print("\n--- IndexError ---")


try:

    print(
        voltage_values[10]
    )


except IndexError:

    print(
        "Requested measurement index does not exist."
    )


# ============================================================
# 22. RAISING AN EXCEPTION
# ============================================================

"""
Python allows us to intentionally generate an exception
using:

raise

This is useful when inputs violate engineering or
mathematical requirements.
"""


def calculate_resistance(
    voltage,
    current
):

    if current == 0:

        raise ValueError(
            "Current must be non-zero."
        )

    return (
        voltage
        / current
    )


print("\n--- raise Example ---")


try:

    resistance = calculate_resistance(
        voltage=48,
        current=0
    )


except ValueError as error:

    print(
        "Calculation Error:",
        error
    )


# ============================================================
# 23. ENGINEERING LIMIT VALIDATION
# ============================================================

"""
Engineering functions can validate whether supplied
parameters are physically meaningful.
"""


def validate_voltage(
    voltage
):

    if voltage < 0:

        raise ValueError(
            "Voltage cannot be negative in this example."
        )

    if voltage > 1000:

        raise ValueError(
            "Voltage exceeds the allowed range."
        )

    return voltage


print("\n--- Voltage Validation ---")


try:

    measured_voltage = validate_voltage(
        450
    )

    print(
        "Accepted Voltage:",
        measured_voltage,
        "V"
    )


except ValueError as error:

    print(
        error
    )


# ============================================================
# 24. ENGINEERING PARAMETER VALIDATION
# ============================================================

"""
Several parameters can be checked before performing
an analysis.
"""


def calculate_power(
    voltage,
    current
):

    if voltage < 0:

        raise ValueError(
            "Voltage must be non-negative."
        )

    if current < 0:

        raise ValueError(
            "Current must be non-negative."
        )

    return (
        voltage
        * current
    )


print("\n--- Parameter Validation ---")


try:

    power = calculate_power(
        voltage=48,
        current=5
    )

    print(
        "Power =",
        power,
        "W"
    )


except ValueError as error:

    print(
        "Invalid parameter:",
        error
    )


# ============================================================
# 25. CSV DATA WITH INVALID VALUES
# ============================================================

"""
Research datasets may contain missing or corrupted values.

Example CSV:

Time,Voltage,Current
0.0,48.0,1.0
0.1,48.5,1.5
0.2,ERROR,2.0
0.3,49.0,2.5

The invalid row should not necessarily terminate the
complete analysis.
"""


import csv


csv_file = Path(
    "example_measurements.csv"
)


# Create demonstration file

with open(
    csv_file,
    "w",
    newline=""
) as file:

    writer = csv.writer(
        file
    )

    writer.writerow(
        [
            "Time",
            "Voltage",
            "Current"
        ]
    )

    writer.writerow(
        [
            0.0,
            48.0,
            1.0
        ]
    )

    writer.writerow(
        [
            0.1,
            48.5,
            1.5
        ]
    )

    writer.writerow(
        [
            0.2,
            "ERROR",
            2.0
        ]
    )

    writer.writerow(
        [
            0.3,
            49.0,
            2.5
        ]
    )


# ============================================================
# 26. PROCESS CSV SAFELY
# ============================================================

valid_rows = []


print("\n--- Safe CSV Processing ---")


try:

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

        for row_number, row in enumerate(
            reader,
            start=2
        ):

            try:

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


                valid_rows.append(
                    [
                        time,
                        voltage,
                        current,
                        power
                    ]
                )


            except (
                ValueError,
                IndexError
            ):

                print(
                    f"Invalid data at CSV row "
                    f"{row_number}: {row}"
                )


except FileNotFoundError:

    print(
        "CSV measurement file not found."
    )


print(
    "\nValid Processed Rows:"
)


for row in valid_rows:

    print(
        row
    )


# ============================================================
# 27. PROCESS MULTIPLE FILES SAFELY
# ============================================================

"""
A research project may contain several measurement or
simulation files.

If one file is missing, we may want the program to continue
processing the remaining files.
"""


measurement_files = [

    "case_A.csv",

    "case_B.csv",

    "missing_case.csv",

    "case_C.csv"

]


print(
    "\n--- Multiple File Processing ---"
)


for filename in measurement_files:

    try:

        with open(
            filename,
            "r"
        ) as file:

            print(
                f"Processing {filename}"
            )


    except FileNotFoundError:

        print(
            f"WARNING: {filename} not found. "
            f"Skipping file."
        )

        continue


# ============================================================
# 28. FUNCTION FOR SAFE FILE READING
# ============================================================

"""
Reusable functions can make file handling more robust.
"""


def read_text_file(
    filename
):

    try:

        with open(
            filename,
            "r"
        ) as file:

            return file.read()


    except FileNotFoundError:

        print(
            f"File not found: {filename}"
        )

        return None


print(
    "\n--- Safe File Function ---"
)


data = read_text_file(
    "engineering_notes.txt"
)


if data is not None:

    print(
        data
    )


# ============================================================
# 29. BAD PRACTICE: BARE except
# ============================================================

"""
This works:

try:
    ...

except:
    ...

but it catches almost every exception and can hide
programming errors.

For research code, prefer specific exceptions:

except ValueError:
except FileNotFoundError:
except ZeroDivisionError:

This makes debugging easier.
"""


# ============================================================
# 30. WHEN SHOULD EXCEPTIONS BE USED?
# ============================================================

"""
Use exception handling for situations such as:

- Missing files
- Invalid external data
- Failed type conversions
- File-access problems
- Unexpected user input
- Failed calculations
- Missing dictionary entries
- Data-format problems


Do NOT use exceptions as a replacement for normal
engineering logic.

For example:

if temperature > temperature_limit:
    ...

is normally better than intentionally raising and
catching an exception for every high temperature.
"""


# ============================================================
# 31. RESEARCH WORKFLOW EXAMPLE
# ============================================================

"""
A robust research script may follow this structure:

Load Measurement File
        ↓
Check File Exists
        ↓
Read Dataset
        ↓
Validate Numerical Values
        ↓
Ignore / Report Invalid Rows
        ↓
Perform Calculation
        ↓
Save Valid Results
        ↓
Continue With Next Dataset

This prevents a single corrupted value from unnecessarily
terminating a large batch-analysis workflow.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
EXCEPTION HANDLING


1. BASIC STRUCTURE

try:

    code

except:

    error_handling


------------------------------------------------------------


2. SPECIFIC EXCEPTION

try:

    result = 10 / 0

except ZeroDivisionError:

    print(
        "Cannot divide by zero"
    )


------------------------------------------------------------


3. MULTIPLE EXCEPTIONS

try:

    ...

except ValueError:

    ...

except ZeroDivisionError:

    ...


------------------------------------------------------------


4. MULTIPLE EXCEPTIONS TOGETHER

try:

    ...

except (
    ValueError,
    TypeError
):

    ...


------------------------------------------------------------


5. EXCEPTION MESSAGE

try:

    ...

except ValueError as error:

    print(error)


------------------------------------------------------------


6. ELSE

Runs only if no exception occurs.

try:

    ...

except:

    ...

else:

    ...


------------------------------------------------------------


7. FINALLY

Always runs.

try:

    ...

except:

    ...

finally:

    ...


------------------------------------------------------------


8. RAISE

Generate an exception intentionally.

if current == 0:

    raise ValueError(
        "Current cannot be zero."
    )


------------------------------------------------------------


COMMON EXCEPTIONS


ZeroDivisionError

    10 / 0


ValueError

    float("abc")


FileNotFoundError

    open("missing.csv")


TypeError

    incompatible data types


KeyError

    dictionary["missing_key"]


IndexError

    data[100]


------------------------------------------------------------


ENGINEERING / RESEARCH USES

Exception handling is useful for:

- Missing CSV files
- Missing Excel files
- Corrupted measurement values
- Invalid numerical conversion
- Invalid parameters
- Division by zero
- Batch processing
- Parameter sweeps
- Experimental datasets
- Simulation outputs
- Automated plotting
- Machine-learning pipelines


------------------------------------------------------------


IMPORTANT PRINCIPLE

Expected engineering condition:

if voltage > voltage_limit:
    print("Overvoltage")


Unexpected program/data problem:

try:
    voltage = float(raw_data)

except ValueError:
    print("Invalid measurement")


Use normal conditions for predictable system logic.

Use exception handling for operations that may fail
unexpectedly.


------------------------------------------------------------


RECOMMENDED RESEARCH PATTERN

try:

    load_data()

except FileNotFoundError:

    report_missing_file()

except ValueError:

    report_invalid_data()

else:

    analyze_data()

finally:

    cleanup_if_required()


------------------------------------------------------------


WHY THIS MATTERS

A research script processing:

100 measurement files

should not necessarily terminate because:

File 37 is missing

or

Row 125 contains an invalid value.

Proper exception handling allows the program to:

detect the problem
        ↓
report it
        ↓
skip invalid data if appropriate
        ↓
continue processing
        ↓
preserve valid results
"""
