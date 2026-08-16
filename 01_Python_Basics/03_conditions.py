"""
============================================================
Python for Engineering and Research
03 - Conditional Statements
============================================================

Purpose:
    Introduce conditional statements in Python and demonstrate
    how decisions can be made based on different conditions.

Topics:
    1. if statement
    2. if-else statement
    3. if-elif-else statement
    4. Multiple conditions
    5. Nested conditions
    6. Membership conditions
    7. Conditional expression
    8. Engineering protection example
    9. Converter operating-state example

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. IF STATEMENT
# ============================================================

"""
The if statement executes a block of code only when
the specified condition is True.

General syntax:

if condition:
    statement
"""

temperature = 70

if temperature > 60:
    print("Temperature is above 60 deg C")


# ============================================================
# 2. IF-ELSE STATEMENT
# ============================================================

"""
The else statement is executed when the if condition
is False.
"""

voltage = 48

print("\n--- IF-ELSE Example ---")

if voltage >= 48:
    print("Voltage is within the required range")
else:
    print("Voltage is below the required range")


# ============================================================
# 3. IF-ELIF-ELSE STATEMENT
# ============================================================

"""
elif allows several conditions to be evaluated.

Python checks the conditions from top to bottom and executes
the first condition that evaluates to True.
"""

temperature = 75

print("\n--- Temperature Classification ---")

if temperature < 40:
    print("Temperature Status: LOW")

elif temperature < 70:
    print("Temperature Status: NORMAL")

elif temperature < 90:
    print("Temperature Status: HIGH")

else:
    print("Temperature Status: CRITICAL")


# ============================================================
# 4. MULTIPLE CONDITIONS
# ============================================================

"""
Logical operators can combine several conditions.

and -> all conditions must be True
or  -> at least one condition must be True
not -> reverses a condition
"""

voltage = 95
temperature = 72

maximum_voltage = 100
maximum_temperature = 85

print("\n--- Multiple Conditions ---")

if voltage <= maximum_voltage and temperature <= maximum_temperature:
    print("System operating within safe limits")
else:
    print("System operating outside safe limits")


# ============================================================
# 5. USING OR
# ============================================================

"""
The or operator becomes True when at least one
condition is True.
"""

over_voltage = False
over_temperature = True

print("\n--- OR Condition ---")

if over_voltage or over_temperature:
    print("Warning: Protection condition detected")
else:
    print("No protection condition detected")


# ============================================================
# 6. USING NOT
# ============================================================

converter_enabled = False

print("\n--- NOT Condition ---")

if not converter_enabled:
    print("Converter is currently disabled")


# ============================================================
# 7. NESTED CONDITIONS
# ============================================================

"""
An if statement can also be placed inside another
if statement.

This is called a nested condition.
"""

dc_bus_voltage = 400
temperature = 65

print("\n--- Nested Condition ---")

if dc_bus_voltage >= 350:

    print("DC bus voltage available")

    if temperature < 80:
        print("Temperature acceptable")
        print("Converter can operate")

    else:
        print("Temperature too high")

else:
    print("DC bus voltage too low")


# ============================================================
# 8. MEMBERSHIP CONDITIONS
# ============================================================

"""
The 'in' operator checks whether a value exists in a
collection such as a list.
"""

available_modes = [
    "Standby",
    "Normal",
    "Boost",
    "Protection"
]

selected_mode = "Boost"

print("\n--- Membership Condition ---")

if selected_mode in available_modes:
    print("Selected operating mode is valid")
else:
    print("Invalid operating mode")


# ============================================================
# 9. CONDITIONAL EXPRESSION
# ============================================================

"""
A simple if-else condition can also be written in one line.

Syntax:

value_if_true if condition else value_if_false

This is sometimes called a conditional or ternary expression.
"""

temperature = 65

status = "Safe" if temperature < 80 else "Unsafe"

print("\n--- Conditional Expression ---")
print("Temperature Status:", status)


# ============================================================
# 10. ENGINEERING EXAMPLE - TEMPERATURE PROTECTION
# ============================================================

"""
Example:
Determine the operating condition of a power converter based
on semiconductor temperature.
"""

device_temperature = 92       # [deg C]

normal_limit = 70
warning_limit = 90

print("\n--- Semiconductor Temperature Protection ---")

if device_temperature <= normal_limit:

    device_status = "NORMAL"

elif device_temperature <= warning_limit:

    device_status = "WARNING"

else:

    device_status = "CRITICAL"


print(f"Device Temperature = {device_temperature} deg C")
print(f"Device Status      = {device_status}")


# ============================================================
# 11. ENGINEERING EXAMPLE - OVERVOLTAGE / OVERCURRENT
# ============================================================

"""
Protection systems frequently evaluate several measurements
simultaneously.
"""

measured_voltage = 405        # [V]
measured_current = 8.5        # [A]

maximum_voltage = 420
maximum_current = 10

print("\n--- Electrical Protection Check ---")

if measured_voltage > maximum_voltage:

    print("FAULT: Overvoltage detected")

elif measured_current > maximum_current:

    print("FAULT: Overcurrent detected")

else:

    print("System operating normally")


# ============================================================
# 12. COMBINED PROTECTION CHECK
# ============================================================

"""
Several protection conditions can be evaluated together.
"""

voltage = 410
current = 9
temperature = 78

voltage_limit = 420
current_limit = 10
temperature_limit = 85

print("\n--- Combined Protection System ---")

if (
    voltage <= voltage_limit
    and current <= current_limit
    and temperature <= temperature_limit
):

    print("SYSTEM STATUS: SAFE")

else:

    print("SYSTEM STATUS: FAULT")


# ============================================================
# 13. IDENTIFY WHICH FAULT OCCURRED
# ============================================================

"""
Instead of only reporting that a fault exists, individual
conditions can be checked separately.
"""

voltage = 430
current = 9
temperature = 90

print("\n--- Fault Identification ---")

if voltage > voltage_limit:
    print("Overvoltage detected")

if current > current_limit:
    print("Overcurrent detected")

if temperature > temperature_limit:
    print("Overtemperature detected")


# ============================================================
# 14. CONVERTER OPERATING-STATE EXAMPLE
# ============================================================

"""
Example:
Classify the operating state of a DC-DC converter based
on measured output voltage.

Reference output voltage = 100 V
"""

reference_voltage = 100       # [V]
output_voltage = 96           # [V]

lower_limit = 0.95 * reference_voltage
upper_limit = 1.05 * reference_voltage

print("\n--- Converter Operating State ---")

if output_voltage < lower_limit:

    operating_state = "UNDERVOLTAGE"

elif output_voltage > upper_limit:

    operating_state = "OVERVOLTAGE"

else:

    operating_state = "NORMAL"


print(f"Reference Voltage = {reference_voltage:.2f} V")
print(f"Measured Voltage  = {output_voltage:.2f} V")
print(f"Lower Limit       = {lower_limit:.2f} V")
print(f"Upper Limit       = {upper_limit:.2f} V")
print(f"Operating State   = {operating_state}")


# ============================================================
# 15. EFFICIENCY CLASSIFICATION EXAMPLE
# ============================================================

"""
Conditional statements can also classify calculated
engineering performance.
"""

input_power = 500             # [W]
output_power = 475            # [W]

efficiency = (output_power / input_power) * 100

print("\n--- Efficiency Classification ---")

if efficiency >= 95:

    performance = "Excellent"

elif efficiency >= 90:

    performance = "Good"

elif efficiency >= 80:

    performance = "Acceptable"

else:

    performance = "Poor"


print(f"Input Power  = {input_power:.2f} W")
print(f"Output Power = {output_power:.2f} W")
print(f"Efficiency   = {efficiency:.2f} %")
print(f"Performance  = {performance}")


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
CONDITIONAL STATEMENTS


1. IF

if condition:
    code


2. IF-ELSE

if condition:
    code_if_true
else:
    code_if_false


3. IF-ELIF-ELSE

if condition_1:
    code

elif condition_2:
    code

else:
    code


4. MULTIPLE CONDITIONS

if condition_1 and condition_2:
    code


5. OR CONDITION

if condition_1 or condition_2:
    code


6. NOT CONDITION

if not condition:
    code


7. NESTED CONDITION

if condition_1:

    if condition_2:
        code


8. CONDITIONAL EXPRESSION

status = "Safe" if temperature < 80 else "Unsafe"


IMPORTANT:

Python uses indentation to define blocks of code.

Correct:

if voltage > 50:
    print("High Voltage")

Incorrect:

if voltage > 50:
print("High Voltage")


ENGINEERING APPLICATIONS:

Conditional statements are useful for:

- Overvoltage detection
- Overcurrent protection
- Temperature monitoring
- Fault detection
- Operating-state classification
- Efficiency classification
- Control-system decisions
- Data filtering
- Measurement validation
"""
