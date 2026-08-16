"""
============================================================
Python for Engineering and Research
05 - Functions
============================================================

Purpose:
    Introduce Python functions and demonstrate how reusable
    blocks of code can simplify engineering calculations.

Topics:
    1. Basic functions
    2. Function parameters
    3. return statement
    4. Multiple parameters
    5. Default arguments
    6. Keyword arguments
    7. Returning multiple values
    8. Docstrings
    9. Local and global variables
    10. Functions with loops
    11. Engineering calculation functions
    12. Reusable analysis functions

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. BASIC FUNCTION
# ============================================================

"""
A function is a reusable block of code that performs
a specific task.

General syntax:

def function_name():
    code
"""

def display_message():
    print("Python for Engineering and Research")


print("--- Basic Function ---")

display_message()


# ============================================================
# 2. FUNCTION WITH A PARAMETER
# ============================================================

"""
Parameters allow values to be passed into a function.

Here, voltage is a parameter.
"""

def display_voltage(voltage):
    print("Voltage =", voltage, "V")


print("\n--- Function Parameter ---")

display_voltage(48)
display_voltage(100)
display_voltage(400)


# ============================================================
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# ============================================================

"""
Functions can receive several input parameters.
"""

def display_measurement(voltage, current):

    print(
        f"Voltage = {voltage:.2f} V | "
        f"Current = {current:.2f} A"
    )


print("\n--- Multiple Parameters ---")

display_measurement(48, 5)
display_measurement(100, 2.5)


# ============================================================
# 4. RETURN STATEMENT
# ============================================================

"""
return sends a calculated result back to the part
of the program that called the function.

This is different from print().

print()  -> displays a value
return   -> gives the value back so it can be reused
"""

def calculate_power(voltage, current):

    power = voltage * current

    return power


power_result = calculate_power(48, 5)

print("\n--- Return Statement ---")

print(
    "Calculated Power =",
    power_result,
    "W"
)


# The returned result can be reused

double_power = power_result * 2

print(
    "Double Power =",
    double_power,
    "W"
)


# ============================================================
# 5. DIRECT RETURN
# ============================================================

"""
A function does not always need an intermediate variable.

This:

power = voltage * current
return power

can also be written as:

return voltage * current
"""

def electrical_power(voltage, current):

    return voltage * current


result = electrical_power(230, 3)

print("\n--- Direct Return ---")
print("Power =", result, "W")


# ============================================================
# 6. DEFAULT ARGUMENTS
# ============================================================

"""
Default arguments provide a predefined value.

If the user does not provide the argument,
the default value is used.
"""

def converter_power(
    voltage,
    current=1.0
):

    return voltage * current


print("\n--- Default Arguments ---")

# Current uses default value of 1 A

print(
    "Power with default current =",
    converter_power(48),
    "W"
)


# Current is manually provided

print(
    "Power with current = 5 A:",
    converter_power(48, 5),
    "W"
)


# ============================================================
# 7. KEYWORD ARGUMENTS
# ============================================================

"""
Arguments can also be passed using parameter names.

This often makes engineering code easier to read.
"""

def system_parameters(
    voltage,
    current,
    frequency
):

    print(
        f"Voltage   = {voltage} V"
    )

    print(
        f"Current   = {current} A"
    )

    print(
        f"Frequency = {frequency} Hz"
    )


print("\n--- Keyword Arguments ---")

system_parameters(
    voltage=48,
    current=5,
    frequency=100000
)


# Keyword arguments can also change the order

print("\nDifferent Argument Order:")

system_parameters(
    frequency=100000,
    voltage=48,
    current=5
)


# ============================================================
# 8. RETURNING MULTIPLE VALUES
# ============================================================

"""
A Python function can return several values.

This is very useful in engineering analysis where one
calculation may produce several results.
"""

def converter_analysis(
    vin,
    iin,
    vout,
    iout
):

    input_power = vin * iin

    output_power = vout * iout

    power_loss = (
        input_power
        - output_power
    )

    efficiency = (
        output_power
        / input_power
    ) * 100

    return (
        input_power,
        output_power,
        power_loss,
        efficiency
    )


pin, pout, loss, efficiency = converter_analysis(
    48,
    5,
    95,
    2.4
)


print("\n--- Multiple Return Values ---")

print(f"Input Power  = {pin:.2f} W")
print(f"Output Power = {pout:.2f} W")
print(f"Power Loss   = {loss:.2f} W")
print(f"Efficiency   = {efficiency:.2f} %")


# ============================================================
# 9. DOCSTRINGS
# ============================================================

"""
A docstring describes what a function does.

Docstrings are particularly important in:

    - Research code
    - Collaborative projects
    - GitHub repositories
    - Reusable engineering scripts
    - Scientific software
"""

def calculate_resistive_loss(
    current,
    resistance
):
    """
    Calculate resistive power loss.

    Parameters
    ----------
    current : float
        Current in amperes.

    resistance : float
        Resistance in ohms.

    Returns
    -------
    float
        Power loss in watts.

    Formula
    -------
    P_loss = I^2 * R
    """

    return current ** 2 * resistance


loss = calculate_resistive_loss(
    current=3,
    resistance=2
)


print("\n--- Function with Docstring ---")

print(
    f"Resistive Power Loss = "
    f"{loss:.2f} W"
)


# ============================================================
# 10. FUNCTION FOR EFFICIENCY
# ============================================================

"""
Reusable engineering functions avoid repeating formulas.
"""

def calculate_efficiency(
    input_power,
    output_power
):

    efficiency = (
        output_power
        / input_power
    ) * 100

    return efficiency


efficiency = calculate_efficiency(
    input_power=500,
    output_power=475
)


print("\n--- Efficiency Function ---")

print(
    f"Converter Efficiency = "
    f"{efficiency:.2f} %"
)


# ============================================================
# 11. FUNCTION FOR VOLTAGE GAIN
# ============================================================

def calculate_voltage_gain(
    input_voltage,
    output_voltage
):

    return (
        output_voltage
        / input_voltage
    )


gain = calculate_voltage_gain(
    48,
    96
)


print("\n--- Voltage Gain ---")

print(
    f"Voltage Gain = {gain:.2f}"
)


# ============================================================
# 12. FUNCTION FOR FREQUENCY TO PERIOD
# ============================================================

"""
Relationship:

T = 1 / f

where:

T = period [s]
f = frequency [Hz]
"""

def frequency_to_period(
    frequency
):

    return 1 / frequency


switching_frequency = 100000

period = frequency_to_period(
    switching_frequency
)


print("\n--- Switching Period ---")

print(
    f"Switching Frequency = "
    f"{switching_frequency} Hz"
)

print(
    f"Switching Period = "
    f"{period:.8f} s"
)

print(
    f"Switching Period = "
    f"{period * 1e6:.2f} us"
)


# ============================================================
# 13. dB CONVERSION FUNCTION
# ============================================================

"""
For an amplitude ratio:

dB = 20 log10(A / A_ref)

Note:
Power ratios normally use 10 log10().
"""

import math


def amplitude_to_db(
    amplitude,
    reference=1.0
):

    return (
        20
        * math.log10(
            amplitude / reference
        )
    )


db_value = amplitude_to_db(
    amplitude=10,
    reference=1
)


print("\n--- Amplitude to dB ---")

print(
    f"Amplitude Ratio = 10"
)

print(
    f"Magnitude = {db_value:.2f} dB"
)


# ============================================================
# 14. FUNCTION WITH CONDITIONAL STATEMENTS
# ============================================================

"""
Functions can contain conditions.
"""

def temperature_status(
    temperature
):

    if temperature <= 70:

        return "NORMAL"

    elif temperature <= 90:

        return "WARNING"

    else:

        return "CRITICAL"


print("\n--- Temperature Function ---")

temperatures = [
    60,
    80,
    100
]

for temperature in temperatures:

    status = temperature_status(
        temperature
    )

    print(
        f"Temperature = "
        f"{temperature} deg C | "
        f"Status = {status}"
    )


# ============================================================
# 15. FUNCTION WITH A LOOP
# ============================================================

"""
Functions can also process multiple values.
"""

def calculate_power_list(
    voltage,
    currents
):

    powers = []

    for current in currents:

        power = voltage * current

        powers.append(power)

    return powers


current_values = [
    1,
    2,
    3,
    4,
    5
]

power_values = calculate_power_list(
    voltage=48,
    currents=current_values
)


print("\n--- Function Processing Multiple Values ---")

print(
    "Current Values:",
    current_values
)

print(
    "Power Values:",
    power_values
)


# ============================================================
# 16. MULTIPLE ENGINEERING CASES
# ============================================================

"""
A reusable function can evaluate many operating points.
"""

def calculate_operating_point(
    voltage,
    current
):

    power = voltage * current

    return power


voltages = [
    24,
    48,
    96
]

currents = [
    5,
    4,
    2
]


print("\n--- Multiple Operating Points ---")

for voltage, current in zip(
    voltages,
    currents
):

    power = calculate_operating_point(
        voltage,
        current
    )

    print(
        f"V = {voltage} V | "
        f"I = {current} A | "
        f"P = {power:.2f} W"
    )


# ============================================================
# 17. LOCAL VARIABLES
# ============================================================

"""
Variables created inside a function are usually local.

A local variable normally exists only inside
that function.
"""

def local_variable_example():

    local_voltage = 48

    print(
        "Inside function:",
        local_voltage
    )


print("\n--- Local Variable ---")

local_variable_example()


# ============================================================
# 18. GLOBAL VARIABLES
# ============================================================

"""
A variable created outside a function is generally
available globally within the module.

However, passing values into functions is usually clearer
than relying heavily on global variables.
"""

dc_bus_voltage = 400


def display_dc_bus():

    print(
        "DC Bus Voltage =",
        dc_bus_voltage,
        "V"
    )


print("\n--- Global Variable ---")

display_dc_bus()


# ============================================================
# 19. ENGINEERING EXAMPLE - DC-DC CONVERTER
# ============================================================

"""
Example:
Build reusable functions for basic converter analysis.
"""


def input_power(
    voltage,
    current
):

    return voltage * current


def output_power(
    voltage,
    current
):

    return voltage * current


def power_loss(
    pin,
    pout
):

    return pin - pout


def efficiency_percent(
    pin,
    pout
):

    return (
        pout / pin
    ) * 100


vin = 48.0
iin = 5.0

vout = 95.0
iout = 2.4


pin = input_power(
    vin,
    iin
)

pout = output_power(
    vout,
    iout
)

loss = power_loss(
    pin,
    pout
)

eff = efficiency_percent(
    pin,
    pout
)


print("\n--- DC-DC Converter Analysis ---")

print(
    f"Input Power  = "
    f"{pin:.2f} W"
)

print(
    f"Output Power = "
    f"{pout:.2f} W"
)

print(
    f"Power Loss   = "
    f"{loss:.2f} W"
)

print(
    f"Efficiency   = "
    f"{eff:.2f} %"
)


# ============================================================
# 20. REUSABLE ANALYSIS FUNCTION
# ============================================================

"""
Instead of writing several independent calculations,
a complete engineering analysis can be placed inside
one reusable function.
"""


def analyze_converter(
    vin,
    iin,
    vout,
    iout
):
    """
    Analyze basic DC-DC converter performance.

    Returns:
        Input power
        Output power
        Power loss
        Efficiency
    """

    pin = vin * iin

    pout = vout * iout

    loss = pin - pout

    efficiency = (
        pout / pin
    ) * 100

    return (
        pin,
        pout,
        loss,
        efficiency
    )


results = analyze_converter(
    vin=48,
    iin=5,
    vout=95,
    iout=2.4
)


print("\n--- Reusable Converter Function ---")

print(
    "Results:",
    results
)


# ============================================================
# 21. WHY FUNCTIONS MATTER FOR DATA ANALYSIS
# ============================================================

"""
Functions become especially useful when the same operation
must be performed on many datasets.

For example, later in this repository we may create:

load_data()
clean_data()
calculate_fft()
calculate_rms()
plot_signal()
save_figure()
train_model()
evaluate_model()

Instead of repeatedly writing the same code, each operation
can be defined once and reused.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
FUNCTIONS


1. BASIC FUNCTION

def function_name():
    code


2. CALL FUNCTION

function_name()


3. FUNCTION WITH PARAMETERS

def calculate_power(voltage, current):
    power = voltage * current


4. RETURN RESULT

def calculate_power(voltage, current):
    return voltage * current


5. USE RETURNED VALUE

power = calculate_power(48, 5)


6. DEFAULT ARGUMENT

def calculate(
    voltage,
    current=1
):
    return voltage * current


7. KEYWORD ARGUMENTS

calculate_power(
    voltage=48,
    current=5
)


8. RETURN MULTIPLE VALUES

def analysis():

    return value1, value2


value1, value2 = analysis()


9. DOCSTRING

def function_name():
    '''
    Description of the function.
    '''
    ...


10. FUNCTIONS CAN CONTAIN

- Calculations
- Conditions
- Loops
- Lists
- Other functions
- Data-processing operations


ENGINEERING APPLICATIONS

Functions are useful for:

- Power calculations
- Efficiency calculations
- Voltage/current analysis
- Frequency conversions
- RMS calculations
- dB conversions
- Signal processing
- FFT calculations
- Parameter sweeps
- Measurement analysis
- Plot generation
- CSV/Excel processing
- Machine-learning preprocessing
- Model evaluation


IMPORTANT PRINCIPLE

If the same calculation or operation is required
several times, consider creating a function.

Instead of:

power1 = voltage1 * current1
power2 = voltage2 * current2
power3 = voltage3 * current3

Use:

def calculate_power(voltage, current):
    return voltage * current

power1 = calculate_power(voltage1, current1)
power2 = calculate_power(voltage2, current2)
power3 = calculate_power(voltage3, current3)
"""
