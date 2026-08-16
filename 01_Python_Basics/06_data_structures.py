"""
============================================================
Python for Engineering and Research
06 - Data Structures
============================================================

Purpose:
    Introduce the main Python data structures and demonstrate
    how they can be used to organize engineering and research
    data.

Topics:
    1. Lists
    2. Accessing list elements
    3. Modifying lists
    4. List methods
    5. Tuples
    6. Dictionaries
    7. Dictionary methods
    8. Sets
    9. Nested data structures
    10. Engineering parameter storage
    11. Multiple simulation cases
    12. Measurement dataset example

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. LISTS
# ============================================================

"""
A list stores multiple values in a single variable.

Lists are:

- Ordered
- Changeable (mutable)
- Able to contain duplicate values

General syntax:

list_name = [value1, value2, value3]
"""

voltages = [48, 50, 52, 54, 56]

print("--- Basic List ---")

print("Voltage Values:", voltages)


# ============================================================
# 2. ACCESSING LIST ELEMENTS
# ============================================================

"""
Python indexing starts from 0.

For the list:

[48, 50, 52, 54, 56]

Index:

 0   1   2   3   4
"""

print("\n--- Access List Elements ---")

print("First Voltage:", voltages[0])
print("Second Voltage:", voltages[1])
print("Last Voltage:", voltages[-1])


# ============================================================
# 3. LIST SLICING
# ============================================================

"""
Slicing extracts part of a list.

Syntax:

list[start:stop]

The stop position is not included.
"""

print("\n--- List Slicing ---")

print(
    "First Three Values:",
    voltages[0:3]
)

print(
    "Values from Index 2:",
    voltages[2:]
)

print(
    "First Three using [:3]:",
    voltages[:3]
)


# ============================================================
# 4. MODIFYING LIST VALUES
# ============================================================

"""
Lists are mutable, meaning their elements can be changed.
"""

voltages[0] = 47.5

print("\n--- Modified List ---")

print(voltages)


# ============================================================
# 5. ADDING ELEMENTS TO A LIST
# ============================================================

"""
append() adds one element to the end of a list.
"""

voltages.append(58)

print("\nAfter append():")
print(voltages)


"""
insert() adds an element at a specified position.
"""

voltages.insert(1, 49)

print("\nAfter insert():")
print(voltages)


# ============================================================
# 6. REMOVING LIST ELEMENTS
# ============================================================

"""
remove() removes a specific value.
"""

voltages.remove(49)

print("\nAfter remove():")
print(voltages)


"""
pop() removes an element using its index.

Without an index, pop() removes the last item.
"""

removed_value = voltages.pop()

print("\nRemoved Value:", removed_value)
print("Updated List:", voltages)


# ============================================================
# 7. LIST LENGTH
# ============================================================

"""
len() returns the number of elements.
"""

number_of_measurements = len(voltages)

print("\n--- List Length ---")

print(
    "Number of Measurements:",
    number_of_measurements
)


# ============================================================
# 8. LOOPING THROUGH A LIST
# ============================================================

currents = [
    1.0,
    1.5,
    2.0,
    2.5
]

print("\n--- Loop Through List ---")

for current in currents:

    print(
        "Current =",
        current,
        "A"
    )


# ============================================================
# 9. LIST OF CALCULATED RESULTS
# ============================================================

"""
Lists are commonly used to store results generated
during calculations.
"""

voltage = 48

current_values = [
    1,
    2,
    3,
    4
]

power_values = []

for current in current_values:

    power = voltage * current

    power_values.append(power)


print("\n--- Calculated Results ---")

print("Current:", current_values)
print("Power:", power_values)


# ============================================================
# 10. IMPORTANT LIST METHODS
# ============================================================

"""
Common list methods:

append()     Add item
insert()     Add item at position
remove()     Remove specific value
pop()        Remove item
sort()       Sort values
reverse()    Reverse order
count()      Count occurrence
index()      Find position
"""

temperatures = [
    75,
    60,
    85,
    70,
    65
]

print("\n--- List Methods ---")

temperatures.sort()

print(
    "Sorted Temperatures:",
    temperatures
)

temperatures.reverse()

print(
    "Reverse Order:",
    temperatures
)


# ============================================================
# 11. TUPLES
# ============================================================

"""
A tuple is similar to a list but cannot normally
be modified after creation.

Tuples are:

- Ordered
- Immutable
- Able to contain duplicate values

Syntax:

tuple_name = (value1, value2, value3)
"""

frequency_range = (
    10000,
    30000000
)

print("\n--- Tuple ---")

print(
    "Frequency Range:",
    frequency_range
)

print(
    "Minimum Frequency:",
    frequency_range[0],
    "Hz"
)

print(
    "Maximum Frequency:",
    frequency_range[1],
    "Hz"
)


# ============================================================
# 12. WHY USE A TUPLE?
# ============================================================

"""
Tuples are useful when values should remain fixed.

Examples:

- Coordinate pairs
- Frequency limits
- Fixed configuration values
- RGB values
- Constant settings
"""

frequency_limits = (
    10000,
    30000000
)

print("\nFixed Frequency Limits:")
print(frequency_limits)


# ============================================================
# 13. DICTIONARIES
# ============================================================

"""
A dictionary stores information as:

key : value

Syntax:

dictionary = {
    "key1": value1,
    "key2": value2
}

Dictionaries are extremely useful for engineering
parameters and research datasets.
"""

converter = {

    "type": "Boost Converter",

    "input_voltage": 48,

    "output_voltage": 96,

    "switching_frequency": 100000,

    "semiconductor": "GaN HEMT"
}


print("\n--- Dictionary ---")

print(converter)


# ============================================================
# 14. ACCESSING DICTIONARY VALUES
# ============================================================

print("\n--- Dictionary Values ---")

print(
    "Converter Type:",
    converter["type"]
)

print(
    "Input Voltage:",
    converter["input_voltage"],
    "V"
)

print(
    "Switching Frequency:",
    converter["switching_frequency"],
    "Hz"
)


# ============================================================
# 15. USING get()
# ============================================================

"""
get() is another way to access dictionary values.

It is often safer because it can return a default value
instead of producing an error when a key is missing.
"""

efficiency = converter.get(
    "efficiency",
    "Not Available"
)

print("\nEfficiency:", efficiency)


# ============================================================
# 16. MODIFY DICTIONARY VALUE
# ============================================================

converter["output_voltage"] = 100

print("\nUpdated Output Voltage:")

print(
    converter["output_voltage"],
    "V"
)


# ============================================================
# 17. ADD NEW DICTIONARY ITEM
# ============================================================

converter["efficiency"] = 95.5

print("\nUpdated Dictionary:")

print(converter)


# ============================================================
# 18. LOOP THROUGH A DICTIONARY
# ============================================================

print("\n--- Dictionary Loop ---")

for key, value in converter.items():

    print(
        key,
        "=",
        value
    )


# ============================================================
# 19. DICTIONARY KEYS AND VALUES
# ============================================================

print("\nDictionary Keys:")

print(
    converter.keys()
)


print("\nDictionary Values:")

print(
    converter.values()
)


# ============================================================
# 20. ENGINEERING PARAMETER DICTIONARY
# ============================================================

"""
A dictionary is an effective way to store all parameters
associated with one engineering system.
"""

system_parameters = {

    "Vin": 48.0,

    "Vout": 96.0,

    "Iin": 5.0,

    "Iout": 2.4,

    "Fsw": 100000,

    "Temperature": 65
}


print("\n--- System Parameters ---")

for parameter, value in system_parameters.items():

    print(
        parameter,
        "=",
        value
    )


# ============================================================
# 21. CALCULATIONS USING DICTIONARY VALUES
# ============================================================

input_power = (
    system_parameters["Vin"]
    * system_parameters["Iin"]
)

output_power = (
    system_parameters["Vout"]
    * system_parameters["Iout"]
)

efficiency = (
    output_power
    / input_power
) * 100


print("\n--- Dictionary-Based Calculation ---")

print(
    f"Input Power = "
    f"{input_power:.2f} W"
)

print(
    f"Output Power = "
    f"{output_power:.2f} W"
)

print(
    f"Efficiency = "
    f"{efficiency:.2f} %"
)


# ============================================================
# 22. SETS
# ============================================================

"""
A set stores unique values.

Sets are useful when duplicate values should be removed.

Syntax:

set_name = {value1, value2, value3}
"""

measurements = {
    48,
    50,
    50,
    52,
    52,
    54
}


print("\n--- Set ---")

print(measurements)


# Notice:

# Duplicate values are automatically removed.


# ============================================================
# 23. REMOVE DUPLICATES USING SET
# ============================================================

frequency_values = [

    100000,

    500000,

    100000,

    1000000,

    500000,

    5000000
]


unique_frequencies = set(
    frequency_values
)


print("\n--- Unique Frequency Values ---")

print(unique_frequencies)


# ============================================================
# 24. SET OPERATIONS
# ============================================================

"""
Sets support useful mathematical operations.

Union:
    Values in either set

Intersection:
    Values common to both sets

Difference:
    Values present in one but not the other
"""

case_a = {
    100000,
    500000,
    1000000
}

case_b = {
    500000,
    1000000,
    5000000
}


print("\n--- Set Operations ---")

print(
    "Union:",
    case_a | case_b
)

print(
    "Intersection:",
    case_a & case_b
)

print(
    "Difference:",
    case_a - case_b
)


# ============================================================
# 25. NESTED LISTS
# ============================================================

"""
A list can contain other lists.

This can represent tabular or matrix-like data.
"""

measurements = [

    [0.0, 48.0, 2.0],

    [0.1, 49.0, 2.1],

    [0.2, 50.0, 2.2]

]


print("\n--- Nested List ---")

print(measurements)


# Access second row

print(
    "Second Row:",
    measurements[1]
)


# Access voltage from first row

print(
    "First Voltage:",
    measurements[0][1]
)


# ============================================================
# 26. LIST OF DICTIONARIES
# ============================================================

"""
A list of dictionaries is very useful for storing
multiple experimental or simulation cases.
"""

simulation_cases = [

    {
        "case": "Case_A",
        "voltage": 48,
        "current": 5
    },

    {
        "case": "Case_B",
        "voltage": 50,
        "current": 4.8
    },

    {
        "case": "Case_C",
        "voltage": 52,
        "current": 4.5
    }

]


print("\n--- Multiple Simulation Cases ---")

for case in simulation_cases:

    print(
        case["case"],
        "| Voltage =",
        case["voltage"],
        "V | Current =",
        case["current"],
        "A"
    )


# ============================================================
# 27. CALCULATE RESULTS FOR MULTIPLE CASES
# ============================================================

"""
The structure above can be combined with loops to perform
calculations automatically.
"""

print("\n--- Simulation Case Calculations ---")

for case in simulation_cases:

    power = (
        case["voltage"]
        * case["current"]
    )

    print(
        f'{case["case"]}: '
        f'Power = {power:.2f} W'
    )


# ============================================================
# 28. NESTED DICTIONARY
# ============================================================

"""
A dictionary can contain other dictionaries.

This is useful for organizing complex research data.
"""

research_results = {

    "Unshielded": {

        "peak": 92.5,

        "average": 75.3

    },

    "Case_A": {

        "peak": 84.2,

        "average": 69.1

    },

    "Case_B": {

        "peak": 78.5,

        "average": 64.4

    }

}


print("\n--- Nested Dictionary ---")

print(
    "Unshielded Peak:",
    research_results[
        "Unshielded"
    ][
        "peak"
    ]
)


print(
    "Case B Average:",
    research_results[
        "Case_B"
    ][
        "average"
    ]
)


# ============================================================
# 29. LOOP THROUGH NESTED DICTIONARY
# ============================================================

print("\n--- Research Results ---")

for case, results in research_results.items():

    print(
        f"{case}: "
        f"Peak = {results['peak']:.2f}, "
        f"Average = {results['average']:.2f}"
    )


# ============================================================
# 30. MEASUREMENT DATASET EXAMPLE
# ============================================================

"""
A simple research dataset can be represented as a dictionary
containing several related lists.

Later, Pandas will provide a more powerful structure called
a DataFrame for this type of data.
"""

measurement_data = {

    "time": [
        0.0,
        0.001,
        0.002,
        0.003
    ],

    "voltage": [
        0,
        25,
        48,
        47
    ],

    "current": [
        0,
        1.2,
        2.1,
        2.0
    ]

}


print("\n--- Measurement Dataset ---")

print(
    "Time:",
    measurement_data["time"]
)

print(
    "Voltage:",
    measurement_data["voltage"]
)

print(
    "Current:",
    measurement_data["current"]
)


# ============================================================
# 31. PROCESS DATASET
# ============================================================

"""
Multiple variables stored inside the dictionary can be
processed together using zip().
"""

print("\n--- Process Measurement Dataset ---")

for time, voltage, current in zip(

    measurement_data["time"],

    measurement_data["voltage"],

    measurement_data["current"]

):

    power = (
        voltage
        * current
    )

    print(
        f"Time = {time:.3f} s | "
        f"Voltage = {voltage:.2f} V | "
        f"Current = {current:.2f} A | "
        f"Power = {power:.2f} W"
    )


# ============================================================
# 32. MUTABLE VS IMMUTABLE
# ============================================================

"""
An important concept:

Mutable:
    Can be changed after creation.

Immutable:
    Cannot normally be changed after creation.


Common examples:

list        -> Mutable

dictionary  -> Mutable

set         -> Mutable

tuple       -> Immutable
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
PYTHON DATA STRUCTURES


1. LIST

Ordered and changeable.

Example:

voltages = [48, 50, 52]

Access:

voltages[0]

Add:

voltages.append(54)

Remove:

voltages.remove(50)


------------------------------------------------------------


2. TUPLE

Ordered but normally cannot be changed.

Example:

frequency_range = (
    10000,
    30000000
)

Useful for fixed values.


------------------------------------------------------------


3. DICTIONARY

Stores key-value pairs.

Example:

converter = {

    "Vin": 48,

    "Vout": 96,

    "Fsw": 100000

}


Access:

converter["Vin"]


Add:

converter["Efficiency"] = 95


Loop:

for key, value in converter.items():

    print(key, value)


------------------------------------------------------------


4. SET

Stores unique values.

Example:

frequencies = {

    100000,

    500000,

    100000

}

The duplicate is removed.


------------------------------------------------------------


QUICK COMPARISON


LIST

Syntax:

[]

Example:

[48, 50, 52]

Best for:

- Measurements
- Samples
- Ordered results
- Plot data


TUPLE

Syntax:

()

Example:

(10000, 30000000)

Best for:

- Fixed values
- Limits
- Coordinates
- Constant settings


DICTIONARY

Syntax:

{}

Example:

{
    "Vin": 48,
    "Vout": 96
}

Best for:

- System parameters
- Simulation settings
- Experiment results
- Named variables


SET

Syntax:

{}

Example:

{1, 2, 3}

Best for:

- Unique values
- Duplicate removal
- Set comparisons


------------------------------------------------------------


ENGINEERING EXAMPLES


LIST:

voltage = [
    48,
    49,
    50,
    51
]


DICTIONARY:

converter = {

    "Voltage": 48,

    "Current": 5,

    "Frequency": 100000

}


LIST OF DICTIONARIES:

cases = [

    {
        "Case": "A",
        "Voltage": 48
    },

    {
        "Case": "B",
        "Voltage": 52
    }

]


DICTIONARY OF LISTS:

data = {

    "Time": [...],

    "Voltage": [...],

    "Current": [...]

}


------------------------------------------------------------


IMPORTANT FOR FUTURE SECTIONS

These data structures directly connect to:

NumPy:
    Python lists -> NumPy arrays

Pandas:
    Dictionaries/lists -> DataFrames

Matplotlib:
    Lists/arrays -> plotted variables

CSV/Excel:
    Tables -> DataFrames

Machine Learning:
    Structured data -> Features and targets


In engineering and research work, lists and dictionaries
are particularly useful for organizing measurements,
parameters, simulation cases, and analysis results.
"""
