# Python Basics — Concepts, Workflow, and Use Cases

This document provides a quick-reference overview of the fundamental Python concepts introduced in the `01_Python_Basics` section.

It is designed for both beginners and users who need a concise revision reference before working with scientific computing, data analysis, signal processing, plotting, or machine learning.

---

## 1. Python Learning Pipeline

```text
Variables and Data Types
          ↓
       Operators
          ↓
      Conditions
          ↓
        Loops
          ↓
      Functions
          ↓
   Data Structures
          ↓
    File Handling
          ↓
 Exception Handling
          ↓
Modules and Packages
          ↓
Engineering Application
```

Each stage introduces concepts required by the following stages.

---

# 2. Variables and Data Types

## Definition

A variable stores information that can be accessed and reused by a Python program.

```python
voltage = 48.0
current = 5.0
converter = "Boost Converter"
enabled = True
```

## Important Data Types

| Type    | Meaning        | Example  |
| ------- | -------------- | -------- |
| `int`   | Whole number   | `100000` |
| `float` | Decimal number | `48.5`   |
| `str`   | Text           | `"GaN"`  |
| `bool`  | Logical value  | `True`   |

## Engineering Use

Variables can represent:

* Voltage
* Current
* Temperature
* Frequency
* Efficiency
* Measurement values
* Simulation parameters

---

# 3. Operators

## Definition

Operators perform mathematical, logical, comparison, and assignment operations.

Important arithmetic operators:

```text
+     Addition
-     Subtraction
*     Multiplication
/     Division
**    Exponentiation
%     Remainder
//    Floor division
```

Example:

```python
power = voltage * current
```

Engineering applications include:

* Power calculations
* Efficiency calculations
* Converter gain
* Loss calculations
* Mathematical models

---

# 4. Conditional Statements

## Definition

Conditional statements allow Python to make decisions.

```python
if temperature > 85:
    print("Overtemperature")
else:
    print("Temperature Normal")
```

Typical structure:

```text
Measurement
     ↓
Check Condition
     ↓
True / False
     ↓
Take Appropriate Action
```

Engineering applications include:

* Overvoltage detection
* Overcurrent detection
* Temperature protection
* Fault classification
* Operating-state detection

---

# 5. Loops

## Definition

Loops repeat an operation automatically.

```python
for voltage in voltages:
    print(voltage)
```

Useful commands include:

```text
for
while
range()
enumerate()
zip()
break
continue
```

Engineering applications include:

* Processing measurements
* Frequency sweeps
* Parameter sweeps
* Multiple simulation cases
* Batch file processing
* Repetitive calculations

---

# 6. Functions

## Definition

Functions store reusable blocks of code.

```python
def calculate_power(voltage, current):
    return voltage * current
```

Use:

```python
power = calculate_power(48, 5)
```

Typical workflow:

```text
Input Parameters
       ↓
    Function
       ↓
 Calculation
       ↓
 Returned Result
```

Functions are useful for:

* Repeated calculations
* Signal processing
* Data cleaning
* Plotting
* FFT analysis
* Machine-learning preprocessing
* Engineering models

---

# 7. Data Structures

Python provides several structures for storing data.

## List

```python
voltages = [48, 49, 50]
```

Best for ordered measurements and samples.

## Tuple

```python
frequency_range = (10000, 30000000)
```

Best for fixed values.

## Dictionary

```python
converter = {
    "Vin": 48,
    "Vout": 96,
    "Fsw": 100000
}
```

Best for named parameters and configuration data.

## Set

```python
frequencies = {100000, 500000, 1000000}
```

Best for unique values.

---

# 8. File Handling

## Definition

File handling allows Python to load and save external data.

Typical workflow:

```text
Measurement / Simulation
          ↓
     CSV / TXT / JSON
          ↓
       Python
          ↓
     Processing
          ↓
       Results
```

Common file types:

| File    | Typical Use                       |
| ------- | --------------------------------- |
| `.txt`  | Notes and simple numerical data   |
| `.csv`  | Measurement and simulation tables |
| `.json` | Configuration and parameters      |
| `.xlsx` | Excel datasets                    |

Excel processing will be covered later using Pandas and OpenPyXL.

---

# 9. Exception Handling

## Definition

Exception handling prevents unexpected errors from terminating an entire program.

```python
try:
    voltage = float(value)

except ValueError:
    print("Invalid measurement")
```

Typical research application:

```text
Load Dataset
     ↓
Check Data
     ↓
Invalid Value?
   ↙       ↘
 Yes       No
 ↓          ↓
Report    Process
 ↓          ↓
Skip     Continue
```

Useful exceptions include:

```text
ValueError
FileNotFoundError
ZeroDivisionError
TypeError
KeyError
IndexError
```

---

# 10. Modules and Packages

## Module

Usually one Python file.

```text
engineering_tools.py
```

## Package

Collection of related modules.

```text
engineering_tools/
├── power.py
├── signals.py
└── plotting.py
```

## Library

Broader collection of reusable functionality.

Examples:

```text
NumPy
Pandas
Matplotlib
SciPy
Scikit-learn
```

Common scientific imports:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

---

# 11. Basic Engineering Python Pipeline

A typical engineering analysis eventually follows:

```text
Define Parameters
       ↓
Load Measurement Data
       ↓
Validate Data
       ↓
Perform Calculations
       ↓
Process Multiple Samples
       ↓
Classify Operating Conditions
       ↓
Store Results
       ↓
Visualize Results
       ↓
Export Processed Data
```

As the repository progresses, this will evolve into:

```text
CSV / Excel
     ↓
Pandas
     ↓
NumPy
     ↓
SciPy
     ↓
Signal Processing
     ↓
Matplotlib
     ↓
Machine Learning
     ↓
Engineering Interpretation
```

---

# 12. Quick Selection Guide

| Requirement            | Python Concept     |
| ---------------------- | ------------------ |
| Store one value        | Variable           |
| Perform calculation    | Operator           |
| Make decision          | `if / elif / else` |
| Repeat operation       | Loop               |
| Reuse calculation      | Function           |
| Store several values   | List               |
| Store named parameters | Dictionary         |
| Store fixed values     | Tuple              |
| Keep unique values     | Set                |
| Read measurement file  | File handling      |
| Handle corrupted data  | Exceptions         |
| Reuse external tools   | Modules/packages   |

---

# 13. Engineering and Research Applications

The concepts introduced in this section form the foundation for later applications including:

* Measurement processing
* CSV and Excel analysis
* Signal processing
* FFT analysis
* Frequency-domain analysis
* Power calculations
* Parameter sweeps
* Scientific visualization
* Automated plotting
* Machine learning
* Model validation
* Research-data processing
* Experimental result analysis

The following repository sections build progressively on these fundamentals.
