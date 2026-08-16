"""
============================================================
Python for Engineering and Research
04 - Loops
============================================================

Purpose:
    Introduce loops in Python and demonstrate how repetitive
    operations can be automated.

Topics:
    1. for loop
    2. range()
    3. Looping through lists
    4. while loop
    5. break
    6. continue
    7. enumerate()
    8. zip()
    9. Nested loops
    10. Engineering measurement processing
    11. Parameter sweep example
    12. Multiple-case processing

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. BASIC FOR LOOP
# ============================================================

"""
A for loop repeats a block of code for each item
in a sequence.

General syntax:

for item in sequence:
    statement
"""

print("--- Basic FOR Loop ---")

for number in [1, 2, 3, 4, 5]:
    print(number)


# ============================================================
# 2. USING range()
# ============================================================

"""
range() generates a sequence of integer values.

range(stop)

range(start, stop)

range(start, stop, step)

Important:
The stop value is NOT included.
"""

print("\n--- range() Example ---")

for number in range(5):
    print(number)


print("\nRange from 1 to 5:")

for number in range(1, 6):
    print(number)


print("\nRange with step size 2:")

for number in range(0, 11, 2):
    print(number)


# ============================================================
# 3. LOOPING THROUGH A LIST
# ============================================================

"""
Lists are commonly used to store multiple values.

A loop can process every value automatically.
"""

voltages = [48, 50, 52, 54, 56]

print("\n--- Voltage Measurements ---")

for voltage in voltages:
    print("Voltage =", voltage, "V")


# ============================================================
# 4. SIMPLE CALCULATION INSIDE A LOOP
# ============================================================

"""
Calculations can be repeated for every value in a dataset.
"""

currents = [1, 2, 3, 4, 5]

voltage = 48

print("\n--- Power Calculation ---")

for current in currents:

    power = voltage * current

    print(
        "Current =",
        current,
        "A | Power =",
        power,
        "W"
    )


# ============================================================
# 5. SAVING LOOP RESULTS
# ============================================================

"""
Calculated results can be stored in another list.

append() adds a new value to the end of a list.
"""

currents = [1, 2, 3, 4, 5]

power_values = []

for current in currents:

    power = voltage * current

    power_values.append(power)


print("\n--- Stored Results ---")

print("Current Values:", currents)
print("Power Values:", power_values)


# ============================================================
# 6. WHILE LOOP
# ============================================================

"""
A while loop continues running while a condition
remains True.

General syntax:

while condition:
    statement
"""

count = 1

print("\n--- WHILE Loop ---")

while count <= 5:

    print("Count =", count)

    count += 1


# ============================================================
# 7. ENGINEERING WHILE LOOP EXAMPLE
# ============================================================

"""
Example:
Increase a simulated converter output voltage until
the reference voltage is reached.
"""

output_voltage = 70
reference_voltage = 100

print("\n--- Voltage Increase Simulation ---")

while output_voltage < reference_voltage:

    output_voltage += 5

    print(
        "Output Voltage =",
        output_voltage,
        "V"
    )


print("Reference voltage reached")


# ============================================================
# 8. BREAK STATEMENT
# ============================================================

"""
break immediately stops a loop.
"""

temperatures = [45, 55, 65, 75, 95, 80]

temperature_limit = 90

print("\n--- BREAK Example ---")

for temperature in temperatures:

    print(
        "Checking Temperature:",
        temperature,
        "deg C"
    )

    if temperature > temperature_limit:

        print("Critical temperature detected")

        break


# ============================================================
# 9. CONTINUE STATEMENT
# ============================================================

"""
continue skips the current loop iteration and moves
to the next item.
"""

measurements = [48, 49, -1, 50, 51]

print("\n--- CONTINUE Example ---")

for measurement in measurements:

    if measurement < 0:

        print(
            "Invalid measurement ignored:",
            measurement
        )

        continue

    print(
        "Valid Measurement:",
        measurement,
        "V"
    )


# ============================================================
# 10. enumerate()
# ============================================================

"""
enumerate() provides both:

    - item index
    - item value

This is very useful when processing measurement data.
"""

voltages = [48.2, 48.5, 49.0, 49.3]

print("\n--- enumerate() Example ---")

for index, voltage in enumerate(voltages):

    print(
        "Sample",
        index,
        "=",
        voltage,
        "V"
    )


# Start numbering from 1

print("\nSamples starting from 1:")

for index, voltage in enumerate(
    voltages,
    start=1
):

    print(
        "Sample",
        index,
        "=",
        voltage,
        "V"
    )


# ============================================================
# 11. zip()
# ============================================================

"""
zip() allows two or more sequences to be processed
together.

This is extremely useful when working with:

    Time + Voltage
    Voltage + Current
    Frequency + Magnitude
    Input + Output data
"""

voltages = [48, 50, 52, 54]

currents = [2, 2.5, 3, 3.5]

print("\n--- zip() Example ---")

for voltage, current in zip(
    voltages,
    currents
):

    power = voltage * current

    print(
        f"Voltage = {voltage} V | "
        f"Current = {current} A | "
        f"Power = {power:.2f} W"
    )


# ============================================================
# 12. LOOPING THROUGH TIME-SERIES DATA
# ============================================================

"""
Example:
Process time and voltage measurements together.
"""

time = [
    0.0,
    0.001,
    0.002,
    0.003,
    0.004
]

voltage = [
    0,
    20,
    40,
    30,
    10
]

print("\n--- Time-Series Data ---")

for t, v in zip(time, voltage):

    print(
        f"Time = {t:.3f} s | "
        f"Voltage = {v:.2f} V"
    )


# ============================================================
# 13. NESTED LOOPS
# ============================================================

"""
A loop can exist inside another loop.

This is called a nested loop.

Nested loops are useful for:

    - Parameter combinations
    - Simulation cases
    - Matrix processing
    - Design-of-experiments
"""

input_voltages = [24, 48]

currents = [1, 2, 3]

print("\n--- Nested Loop ---")

for voltage in input_voltages:

    for current in currents:

        power = voltage * current

        print(
            f"Voltage = {voltage} V | "
            f"Current = {current} A | "
            f"Power = {power} W"
        )


# ============================================================
# 14. ENGINEERING EXAMPLE - MULTIPLE LOAD CONDITIONS
# ============================================================

"""
Example:
Calculate output power and efficiency for several
load-current conditions.
"""

input_voltage = 48
input_current = 5

input_power = input_voltage * input_current

output_voltage = 95

load_currents = [
    1.0,
    1.5,
    2.0,
    2.4
]

print("\n--- Converter Load Analysis ---")

for load_current in load_currents:

    output_power = (
        output_voltage
        * load_current
    )

    efficiency = (
        output_power
        / input_power
    ) * 100

    print(
        f"Load Current = {load_current:.2f} A | "
        f"Output Power = {output_power:.2f} W | "
        f"Efficiency = {efficiency:.2f} %"
    )


# ============================================================
# 15. PARAMETER SWEEP EXAMPLE
# ============================================================

"""
Parameter sweeps are common in engineering simulations.

Example:
Evaluate several gate-resistance values.

In a real simulation, each resistance value could be sent
to a circuit model or simulation software.
"""

gate_resistance_values = [
    2,
    5,
    10,
    15,
    20
]

print("\n--- Gate Resistance Sweep ---")

for resistance in gate_resistance_values:

    print(
        f"Running case for "
        f"Rg = {resistance} Ohm"
    )


# ============================================================
# 16. STORE PARAMETER-SWEEP RESULTS
# ============================================================

"""
Results generated during a parameter sweep can
also be saved.

For demonstration, a simple calculation is used.
"""

resistance_values = [
    2,
    5,
    10,
    15,
    20
]

current = 2

loss_results = []

for resistance in resistance_values:

    power_loss = (
        current ** 2
        * resistance
    )

    loss_results.append(power_loss)


print("\n--- Parameter Sweep Results ---")

print(
    "Resistance:",
    resistance_values
)

print(
    "Power Loss:",
    loss_results
)


# ============================================================
# 17. MULTIPLE SIMULATION CASES
# ============================================================

"""
A loop can automatically process multiple named
engineering cases.
"""

simulation_cases = [
    "Case_A",
    "Case_B",
    "Case_C",
    "Case_D"
]

print("\n--- Simulation Cases ---")

for case in simulation_cases:

    print(
        f"Processing {case}"
    )


# ============================================================
# 18. MULTIPLE VARIABLES USING zip()
# ============================================================

"""
Several related variables can be processed together.

This pattern will later be useful for plotting multiple
measurement or simulation datasets.
"""

case_names = [
    "Case_A",
    "Case_B",
    "Case_C"
]

peak_values = [
    82.5,
    76.3,
    70.8
]

print("\n--- Multiple Case Results ---")

for case, peak in zip(
    case_names,
    peak_values
):

    print(
        f"{case}: "
        f"Peak Value = {peak:.2f}"
    )


# ============================================================
# 19. FIND MAXIMUM VALUE USING A LOOP
# ============================================================

"""
Although Python provides built-in functions such as max(),
understanding the loop logic is useful for learning.
"""

measurements = [
    42,
    57,
    49,
    68,
    61
]

maximum_value = measurements[0]

for value in measurements:

    if value > maximum_value:

        maximum_value = value


print("\n--- Maximum Measurement ---")

print(
    "Maximum Value =",
    maximum_value
)


# ============================================================
# 20. COUNT VALUES ABOVE A LIMIT
# ============================================================

"""
Example:
Count how many measurements exceed an engineering limit.
"""

temperatures = [
    55,
    62,
    81,
    75,
    90,
    68
]

temperature_limit = 80

count_above_limit = 0

for temperature in temperatures:

    if temperature > temperature_limit:

        count_above_limit += 1


print("\n--- Limit Check ---")

print(
    "Measurements above limit =",
    count_above_limit
)


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
LOOPS


1. FOR LOOP

for item in sequence:
    code


2. RANGE

for i in range(5):
    print(i)


3. LOOP THROUGH LIST

for voltage in voltages:
    print(voltage)


4. WHILE LOOP

while condition:
    code


5. BREAK

Stops the loop completely.

if condition:
    break


6. CONTINUE

Skips the current iteration.

if condition:
    continue


7. ENUMERATE

Returns index and value.

for index, value in enumerate(data):
    print(index, value)


8. ZIP

Processes multiple sequences together.

for voltage, current in zip(
    voltages,
    currents
):
    power = voltage * current


9. NESTED LOOP

for voltage in voltages:

    for current in currents:

        power = voltage * current


10. STORE RESULTS

results = []

for value in data:

    result = value * 2

    results.append(result)


COMMON ENGINEERING USES

Loops are useful for:

- Processing measurements
- Repeating calculations
- Parameter sweeps
- Simulation automation
- Processing multiple cases
- Frequency sweeps
- Temperature monitoring
- Voltage/current datasets
- CSV or Excel rows
- Repeating plots
- Data cleaning
- Machine-learning experiments


IMPORTANT:

Avoid unnecessary loops when libraries such as NumPy
can perform the same operation efficiently on complete arrays.

Example:

Python loop:

for value in data:
    result = value * 2

NumPy approach:

result = data * 2

Both approaches are useful, but vectorized NumPy operations
are generally preferred for large numerical datasets.
"""
