"""
============================================================
Python for Engineering and Research
02 - Python Operators
============================================================

Purpose:
    Introduce the most commonly used Python operators and
    demonstrate their use in basic engineering calculations.

Topics:
    1. Arithmetic operators
    2. Comparison operators
    3. Assignment operators
    4. Logical operators
    5. Modulus operator
    6. Exponentiation
    7. Floor division
    8. Operator precedence
    9. Engineering application

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

"""
Arithmetic operators are used to perform mathematical
calculations.

+    Addition
-    Subtraction
*    Multiplication
/    Division
%    Modulus (remainder)
**   Exponentiation
//   Floor division
"""

a = 10
b = 3

print("--- Arithmetic Operators ---")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)


# ============================================================
# 2. ENGINEERING ARITHMETIC EXAMPLE
# ============================================================

voltage = 48.0       # Voltage [V]
current = 5.0        # Current [A]

power = voltage * current

print("\n--- Electrical Power ---")
print("Voltage:", voltage, "V")
print("Current:", current, "A")
print("Power:", power, "W")


# ============================================================
# 3. COMPARISON OPERATORS
# ============================================================

"""
Comparison operators compare two values.

==    Equal to
!=    Not equal to
>     Greater than
<     Less than
>=    Greater than or equal to
<=    Less than or equal to

The result is always True or False.
"""

temperature = 75

print("\n--- Comparison Operators ---")

print("Temperature == 75:", temperature == 75)
print("Temperature != 75:", temperature != 75)
print("Temperature > 60:", temperature > 60)
print("Temperature < 100:", temperature < 100)
print("Temperature >= 75:", temperature >= 75)
print("Temperature <= 80:", temperature <= 80)


# ============================================================
# 4. ASSIGNMENT OPERATORS
# ============================================================

"""
Assignment operators modify the value of a variable.

=     Assign value
+=    Add and assign
-=    Subtract and assign
*=    Multiply and assign
/=    Divide and assign
"""

value = 10

print("\n--- Assignment Operators ---")

print("Initial value:", value)

value += 5
print("After += 5:", value)

value -= 3
print("After -= 3:", value)

value *= 2
print("After *= 2:", value)

value /= 4
print("After /= 4:", value)


# ============================================================
# 5. LOGICAL OPERATORS
# ============================================================

"""
Logical operators combine multiple conditions.

and    True when both conditions are True
or     True when at least one condition is True
not    Reverses a Boolean condition
"""

voltage = 48
temperature = 65

safe_voltage = voltage <= 60
safe_temperature = temperature <= 80

print("\n--- Logical Operators ---")

print(
    "Voltage AND Temperature Safe:",
    safe_voltage and safe_temperature
)

print(
    "At Least One Condition Safe:",
    safe_voltage or safe_temperature
)

print(
    "NOT Safe Voltage:",
    not safe_voltage
)


# ============================================================
# 6. MODULUS OPERATOR
# ============================================================

"""
The modulus operator (%) returns the remainder after division.

It is commonly useful for:
    - Checking even/odd numbers
    - Periodic operations
    - Counters
    - Sampling operations
"""

sample_number = 20

remainder = sample_number % 5

print("\n--- Modulus Operator ---")
print("20 % 5 =", remainder)


# Example: Check whether a number is even

number = 10

is_even = number % 2 == 0

print("Is 10 even?", is_even)


# ============================================================
# 7. EXPONENTIATION
# ============================================================

"""
The ** operator raises a value to a power.
"""

resistance = 10
current = 2

# Resistive power loss:
# P = I^2 R

power_loss = current ** 2 * resistance

print("\n--- Exponentiation Example ---")
print("Resistance:", resistance, "Ohm")
print("Current:", current, "A")
print("Power Loss:", power_loss, "W")


# ============================================================
# 8. FLOOR DIVISION
# ============================================================

"""
Floor division (//) performs division and returns the
integer quotient without the remainder.
"""

total_samples = 1050
samples_per_block = 100

complete_blocks = total_samples // samples_per_block
remaining_samples = total_samples % samples_per_block

print("\n--- Floor Division Example ---")

print("Complete Blocks:", complete_blocks)
print("Remaining Samples:", remaining_samples)


# ============================================================
# 9. OPERATOR PRECEDENCE
# ============================================================

"""
Python follows mathematical operator precedence.

Parentheses        ()
Exponentiation     **
Multiplication     *
Division           /
Addition           +
Subtraction        -

Using parentheses is recommended when an expression
may otherwise be difficult to understand.
"""

result_1 = 10 + 5 * 2
result_2 = (10 + 5) * 2

print("\n--- Operator Precedence ---")

print("10 + 5 * 2 =", result_1)
print("(10 + 5) * 2 =", result_2)


# ============================================================
# 10. ENGINEERING EXAMPLE
# ============================================================

"""
Example:
Calculate the input power, output power, converter efficiency,
and power loss of a DC-DC converter.
"""

input_voltage = 48.0       # [V]
input_current = 5.0        # [A]

output_voltage = 95.0      # [V]
output_current = 2.4       # [A]


# Input electrical power

input_power = input_voltage * input_current


# Output electrical power

output_power = output_voltage * output_current


# Converter power loss

power_loss = input_power - output_power


# Converter efficiency

efficiency = (output_power / input_power) * 100


print("\n--- Converter Engineering Example ---")

print(f"Input Voltage   = {input_voltage:.2f} V")
print(f"Input Current   = {input_current:.2f} A")

print(f"Output Voltage  = {output_voltage:.2f} V")
print(f"Output Current  = {output_current:.2f} A")

print(f"Input Power     = {input_power:.2f} W")
print(f"Output Power    = {output_power:.2f} W")

print(f"Power Loss      = {power_loss:.2f} W")
print(f"Efficiency      = {efficiency:.2f} %")


# ============================================================
# 11. OPERATING CONDITION EXAMPLE
# ============================================================

"""
Comparison and logical operators can also be used to evaluate
whether an engineering system is operating within specified
limits.
"""

maximum_temperature = 85       # [deg C]
maximum_voltage = 100          # [V]

measured_temperature = 72
measured_voltage = 95

system_safe = (
    measured_temperature <= maximum_temperature
    and measured_voltage <= maximum_voltage
)

print("\n--- Operating Condition Check ---")

print("Measured Temperature:", measured_temperature, "deg C")
print("Measured Voltage:", measured_voltage, "V")

print("System Operating Within Limits:", system_safe)


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
IMPORTANT OPERATORS

Arithmetic:

+     Addition
-     Subtraction
*     Multiplication
/     Division
%     Remainder
**    Power
//    Floor division


Comparison:

==    Equal
!=    Not equal
>     Greater than
<     Less than
>=    Greater than or equal
<=    Less than or equal


Logical:

and   Both conditions must be True
or    At least one condition must be True
not   Reverse the condition


Assignment:

=     Assign
+=    Add and assign
-=    Subtract and assign
*=    Multiply and assign
/=    Divide and assign


Engineering examples:

Power:
    P = V * I

Resistive loss:
    P_loss = I**2 * R

Efficiency:
    efficiency = (P_out / P_in) * 100
"""
