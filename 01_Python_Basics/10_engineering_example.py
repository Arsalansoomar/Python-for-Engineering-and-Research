"""
============================================================
Python for Engineering and Research
10 - Engineering Mini Project
============================================================

Project:
    Basic DC-DC Converter Measurement Analysis

Purpose:
    Combine the Python concepts introduced in this section
    into one practical engineering workflow.

Concepts Used:
    - Variables
    - Operators
    - Conditions
    - Loops
    - Functions
    - Lists
    - Dictionaries
    - File handling
    - Exception handling
    - Modules

Workflow:

    Converter Parameters
            ↓
    Measurement Dataset
            ↓
    Validate Measurements
            ↓
    Calculate Power
            ↓
    Calculate Efficiency
            ↓
    Determine Operating Status
            ↓
    Store Results
            ↓
    Export CSV
            ↓
    Display Summary

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. IMPORT REQUIRED MODULES
# ============================================================

import csv
from pathlib import Path


# ============================================================
# 2. CONVERTER PARAMETERS
# ============================================================

"""
A dictionary stores the main converter parameters.
"""

converter = {

    "name": "DC-DC Boost Converter",

    "nominal_input_voltage": 48.0,

    "nominal_output_voltage": 96.0,

    "switching_frequency": 100000,

    "maximum_temperature": 85.0,

    "maximum_output_voltage": 105.0
}


print("=" * 60)

print(
    converter["name"]
)

print("=" * 60)


print(
    f"Nominal Input Voltage  = "
    f"{converter['nominal_input_voltage']} V"
)

print(
    f"Nominal Output Voltage = "
    f"{converter['nominal_output_voltage']} V"
)

print(
    f"Switching Frequency    = "
    f"{converter['switching_frequency']} Hz"
)


# ============================================================
# 3. MEASUREMENT DATA
# ============================================================

"""
Each dictionary represents one measurement point.

One deliberately invalid measurement is included to
demonstrate exception handling.
"""

measurements = [

    {
        "time": 0.0,
        "vin": 48.0,
        "iin": 4.5,
        "vout": 94.0,
        "iout": 2.1,
        "temperature": 55
    },

    {
        "time": 0.1,
        "vin": 48.2,
        "iin": 4.8,
        "vout": 95.0,
        "iout": 2.2,
        "temperature": 62
    },

    {
        "time": 0.2,
        "vin": 48.5,
        "iin": 5.0,
        "vout": 96.0,
        "iout": 2.3,
        "temperature": 68
    },

    {
        "time": 0.3,
        "vin": 48.4,
        "iin": 5.2,
        "vout": 98.0,
        "iout": 2.4,
        "temperature": 76
    },

    {
        "time": 0.4,
        "vin": "ERROR",
        "iin": 5.0,
        "vout": 97.0,
        "iout": 2.3,
        "temperature": 72
    },

    {
        "time": 0.5,
        "vin": 48.6,
        "iin": 5.5,
        "vout": 106.0,
        "iout": 2.4,
        "temperature": 90
    }
]


# ============================================================
# 4. CALCULATE ELECTRICAL POWER
# ============================================================


def calculate_power(
    voltage,
    current
):
    """
    Calculate electrical power.

    P = V * I

    Parameters
    ----------
    voltage : float
        Voltage in volts.

    current : float
        Current in amperes.

    Returns
    -------
    float
        Electrical power in watts.
    """

    return voltage * current


# ============================================================
# 5. CALCULATE EFFICIENCY
# ============================================================


def calculate_efficiency(
    input_power,
    output_power
):
    """
    Calculate converter efficiency.

    efficiency = Pout / Pin * 100
    """

    if input_power <= 0:

        return None

    return (
        output_power
        / input_power
    ) * 100


# ============================================================
# 6. TEMPERATURE STATUS
# ============================================================


def temperature_status(
    temperature,
    limit
):
    """
    Classify semiconductor temperature.
    """

    if temperature < 70:

        return "NORMAL"

    elif temperature <= limit:

        return "WARNING"

    else:

        return "CRITICAL"


# ============================================================
# 7. VOLTAGE STATUS
# ============================================================


def voltage_status(
    output_voltage,
    maximum_voltage
):
    """
    Determine whether output voltage exceeds its limit.
    """

    if output_voltage > maximum_voltage:

        return "OVERVOLTAGE"

    else:

        return "NORMAL"


# ============================================================
# 8. COMPLETE SYSTEM STATUS
# ============================================================


def determine_system_status(
    temperature_state,
    voltage_state
):
    """
    Determine overall operating condition.
    """

    if (
        temperature_state == "CRITICAL"
        or voltage_state == "OVERVOLTAGE"
    ):

        return "FAULT"

    elif temperature_state == "WARNING":

        return "WARNING"

    else:

        return "NORMAL"


# ============================================================
# 9. PROCESS MEASUREMENTS
# ============================================================

processed_results = []

invalid_measurements = 0


print(
    "\n--- Processing Measurements ---"
)


for index, measurement in enumerate(
    measurements,
    start=1
):

    try:

        # ----------------------------------------------------
        # Convert values to float
        # ----------------------------------------------------

        time = float(
            measurement["time"]
        )

        vin = float(
            measurement["vin"]
        )

        iin = float(
            measurement["iin"]
        )

        vout = float(
            measurement["vout"]
        )

        iout = float(
            measurement["iout"]
        )

        temperature = float(
            measurement["temperature"]
        )


        # ----------------------------------------------------
        # Calculate power
        # ----------------------------------------------------

        input_power = calculate_power(
            vin,
            iin
        )

        output_power = calculate_power(
            vout,
            iout
        )


        # ----------------------------------------------------
        # Calculate efficiency
        # ----------------------------------------------------

        efficiency = calculate_efficiency(
            input_power,
            output_power
        )


        # ----------------------------------------------------
        # Determine temperature condition
        # ----------------------------------------------------

        temp_state = temperature_status(

            temperature,

            converter[
                "maximum_temperature"
            ]

        )


        # ----------------------------------------------------
        # Determine voltage condition
        # ----------------------------------------------------

        volt_state = voltage_status(

            vout,

            converter[
                "maximum_output_voltage"
            ]

        )


        # ----------------------------------------------------
        # Determine overall system status
        # ----------------------------------------------------

        system_state = determine_system_status(

            temp_state,

            volt_state

        )


        # ----------------------------------------------------
        # Store result
        # ----------------------------------------------------

        result = {

            "sample": index,

            "time": time,

            "vin": vin,

            "iin": iin,

            "vout": vout,

            "iout": iout,

            "input_power": input_power,

            "output_power": output_power,

            "efficiency": efficiency,

            "temperature": temperature,

            "temperature_status": temp_state,

            "voltage_status": volt_state,

            "system_status": system_state
        }


        processed_results.append(
            result
        )


        # ----------------------------------------------------
        # Display processed result
        # ----------------------------------------------------

        print(
            f"Sample {index}: "
            f"Efficiency = {efficiency:.2f} % | "
            f"Temperature = {temperature:.1f} C | "
            f"Status = {system_state}"
        )


    except (
        ValueError,
        TypeError,
        KeyError
    ) as error:

        invalid_measurements += 1

        print(
            f"Sample {index}: "
            f"Invalid measurement skipped "
            f"({error})"
        )

        continue


# ============================================================
# 10. CALCULATE SUMMARY STATISTICS
# ============================================================

"""
For now, basic Python is used.

NumPy will later make statistical calculations easier.
"""


efficiency_values = []


for result in processed_results:

    if result["efficiency"] is not None:

        efficiency_values.append(
            result["efficiency"]
        )


if len(
    efficiency_values
) > 0:

    average_efficiency = (
        sum(
            efficiency_values
        )
        / len(
            efficiency_values
        )
    )

    maximum_efficiency = max(
        efficiency_values
    )

    minimum_efficiency = min(
        efficiency_values
    )

else:

    average_efficiency = None
    maximum_efficiency = None
    minimum_efficiency = None


# ============================================================
# 11. COUNT SYSTEM STATES
# ============================================================

normal_count = 0
warning_count = 0
fault_count = 0


for result in processed_results:

    state = result[
        "system_status"
    ]

    if state == "NORMAL":

        normal_count += 1

    elif state == "WARNING":

        warning_count += 1

    elif state == "FAULT":

        fault_count += 1


# ============================================================
# 12. CREATE RESULTS DIRECTORY
# ============================================================

results_folder = Path(
    "results"
)


results_folder.mkdir(
    exist_ok=True
)


# ============================================================
# 13. SAVE PROCESSED RESULTS TO CSV
# ============================================================

output_file = (

    results_folder

    / "converter_analysis_results.csv"

)


try:

    with open(
        output_file,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(
            file
        )


        # Header

        writer.writerow(
            [
                "Sample",
                "Time_s",
                "Vin_V",
                "Iin_A",
                "Vout_V",
                "Iout_A",
                "Input_Power_W",
                "Output_Power_W",
                "Efficiency_percent",
                "Temperature_C",
                "Temperature_Status",
                "Voltage_Status",
                "System_Status"
            ]
        )


        # Data

        for result in processed_results:

            writer.writerow(
                [
                    result["sample"],
                    result["time"],
                    result["vin"],
                    result["iin"],
                    result["vout"],
                    result["iout"],
                    result["input_power"],
                    result["output_power"],
                    result["efficiency"],
                    result["temperature"],
                    result["temperature_status"],
                    result["voltage_status"],
                    result["system_status"]
                ]
            )


except OSError as error:

    print(
        "\nUnable to save results:"
    )

    print(
        error
    )


else:

    print(
        "\nResults successfully saved to:"
    )

    print(
        output_file
    )


# ============================================================
# 14. DISPLAY ANALYSIS SUMMARY
# ============================================================

print(
    "\n"
    + "=" * 60
)

print(
    "ANALYSIS SUMMARY"
)

print(
    "=" * 60
)


print(
    f"Total Measurements   = "
    f"{len(measurements)}"
)

print(
    f"Valid Measurements   = "
    f"{len(processed_results)}"
)

print(
    f"Invalid Measurements = "
    f"{invalid_measurements}"
)


if average_efficiency is not None:

    print(
        f"\nAverage Efficiency   = "
        f"{average_efficiency:.2f} %"
    )

    print(
        f"Maximum Efficiency   = "
        f"{maximum_efficiency:.2f} %"
    )

    print(
        f"Minimum Efficiency   = "
        f"{minimum_efficiency:.2f} %"
    )


print(
    f"\nNormal Conditions    = "
    f"{normal_count}"
)

print(
    f"Warning Conditions   = "
    f"{warning_count}"
)

print(
    f"Fault Conditions     = "
    f"{fault_count}"
)


print(
    "\nAnalysis Completed."
)


# ============================================================
# 15. CONCEPTS USED IN THIS PROJECT
# ============================================================

"""
VARIABLES

vin = 48


OPERATORS

power = voltage * current


CONDITIONS

if temperature > limit:
    ...


LOOPS

for measurement in measurements:
    ...


FUNCTIONS

def calculate_power(...):
    ...


LISTS

measurements = [...]


DICTIONARIES

converter = {
    "Vin": 48
}


FILE HANDLING

with open(...) as file:
    ...


EXCEPTION HANDLING

try:
    ...

except ValueError:
    ...


MODULES

import csv

from pathlib import Path
"""


# ============================================================
# 16. ENGINEERING WORKFLOW
# ============================================================

"""
Raw Measurement Data
        ↓
Validate Data
        ↓
Convert to Numerical Values
        ↓
Calculate Input Power
        ↓
Calculate Output Power
        ↓
Calculate Efficiency
        ↓
Check Temperature
        ↓
Check Output Voltage
        ↓
Determine System Status
        ↓
Store Processed Results
        ↓
Export CSV
        ↓
Generate Summary


This same workflow will later be improved using:

NumPy
Pandas
Matplotlib
SciPy
Machine Learning
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
This mini-project demonstrates how individual Python
concepts work together in an engineering application.

The most important lesson is that real Python workflows
normally combine several concepts.

For example:

A function performs the calculation.

A loop processes multiple measurements.

A condition determines operating status.

A dictionary stores parameters.

Exception handling manages invalid data.

File handling saves the results.


NEXT DEVELOPMENT STAGES

Basic Python
       ↓
NumPy
       ↓
Pandas
       ↓
Data Visualization
       ↓
SciPy
       ↓
Signal Processing
       ↓
Machine Learning
       ↓
Engineering Applications
"""
