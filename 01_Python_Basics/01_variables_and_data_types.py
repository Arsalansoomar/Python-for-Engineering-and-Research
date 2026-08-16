"""
============================================================
Python for Engineering and Research
01 - Variables and Data Types
============================================================

Purpose:
    Introduce Python variables and the most important basic
    data types.

Topics:
    1. Variables
    2. Integer (int)
    3. Floating-point number (float)
    4. String (str)
    5. Boolean (bool)
    6. Checking data types
    7. Type conversion
    8. Basic engineering application

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. VARIABLES
# ============================================================

# A variable stores a value that can be used later in a program.

voltage = 48
current = 5
name = "GaN Converter"

print("Voltage:", voltage)
print("Current:", current)
print("System:", name)


# ============================================================
# 2. INTEGER DATA TYPE
# ============================================================

# Integers are whole numbers without decimal points.

switching_frequency = 100000
number_of_samples = 1000

print("\nSwitching Frequency:", switching_frequency, "Hz")
print("Number of Samples:", number_of_samples)


# ============================================================
# 3. FLOAT DATA TYPE
# ============================================================

# Floats represent numbers containing decimal values.

input_voltage = 48.5
output_voltage = 96.8
efficiency = 0.95

print("\nInput Voltage:", input_voltage, "V")
print("Output Voltage:", output_voltage, "V")
print("Efficiency:", efficiency)


# ============================================================
# 4. STRING DATA TYPE
# ============================================================

# Strings store text and are written inside quotation marks.

converter_type = "Boost Converter"
semiconductor = "GaN HEMT"

print("\nConverter Type:", converter_type)
print("Semiconductor:", semiconductor)


# ============================================================
# 5. BOOLEAN DATA TYPE
# ============================================================

# Boolean variables can contain only True or False.

converter_enabled = True
fault_detected = False

print("\nConverter Enabled:", converter_enabled)
print("Fault Detected:", fault_detected)


# ============================================================
# 6. CHECKING DATA TYPES
# ============================================================

# The type() function identifies the data type of a variable.

print("\nData Types:")

print(type(switching_frequency))
print(type(input_voltage))
print(type(converter_type))
print(type(converter_enabled))


# ============================================================
# 7. TYPE CONVERSION
# ============================================================

# Python allows conversion between compatible data types.

frequency_text = "100000"

# Convert string to integer
frequency_integer = int(frequency_text)

print("\nOriginal value:", frequency_text)
print("Original type:", type(frequency_text))

print("Converted value:", frequency_integer)
print("Converted type:", type(frequency_integer))


# Integer to float

voltage_integer = 48
voltage_float = float(voltage_integer)

print("\nInteger Voltage:", voltage_integer)
print("Float Voltage:", voltage_float)


# Number to string

temperature = 25.5

temperature_text = str(temperature)

print("\nTemperature as number:", temperature)
print("Temperature as string:", temperature_text)


# ============================================================
# 8. ENGINEERING EXAMPLE
# ============================================================

"""
Example:
Calculate the voltage gain and electrical power of a
DC-DC converter.
"""

vin = 48.0          # Input voltage [V]
vout = 96.0         # Output voltage [V]
iout = 4.5          # Output current [A]

# Voltage gain

voltage_gain = vout / vin

# Output power

output_power = vout * iout

print("\n--- Engineering Example ---")

print("Input Voltage:", vin, "V")
print("Output Voltage:", vout, "V")
print("Output Current:", iout, "A")

print("Voltage Gain:", voltage_gain)
print("Output Power:", output_power, "W")


# ============================================================
# 9. FORMATTED OUTPUT
# ============================================================

# f-strings provide a convenient way to display variables
# together with text.

print("\n--- Formatted Output ---")

print(f"Input Voltage  = {vin} V")
print(f"Output Voltage = {vout} V")
print(f"Output Current = {iout} A")
print(f"Voltage Gain   = {voltage_gain:.2f}")
print(f"Output Power   = {output_power:.2f} W")


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
Important Python Data Types:

int     -> Whole numbers
           Example: 100000

float   -> Decimal numbers
           Example: 48.5

str     -> Text
           Example: "GaN Converter"

bool    -> Logical values
           True or False

Useful Functions:

type()  -> Check the data type
int()   -> Convert to integer
float() -> Convert to float
str()   -> Convert to string
"""
