"""
============================================================
Python for Engineering and Research
09 - Modules and Packages
============================================================

Purpose:
    Introduce Python modules, packages, libraries, imports,
    package installation, and reusable code organization.

Topics:
    1. What is a module?
    2. What is a package?
    3. What is a library?
    4. Python Standard Library
    5. import
    6. from ... import ...
    7. Import aliases
    8. Third-party packages
    9. pip installation
    10. requirements.txt
    11. Creating custom modules
    12. __name__ == "__main__"
    13. Engineering examples
    14. Scientific Python ecosystem

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHAT IS A MODULE?
# ============================================================

"""
A module is usually a single Python file containing
reusable Python code.

Example:

engineering_tools.py

The file may contain:

- Functions
- Variables
- Classes
- Constants

Another Python program can import and reuse them.
"""


# ============================================================
# 2. WHAT IS A PACKAGE?
# ============================================================

"""
A package organizes multiple related Python modules.

Example structure:

engineering_tools/
│
├── __init__.py
├── power.py
├── signals.py
└── plotting.py


Here:

engineering_tools
    -> Package

power.py
    -> Module

signals.py
    -> Module

plotting.py
    -> Module
"""


# ============================================================
# 3. WHAT IS A LIBRARY?
# ============================================================

"""
The term library is commonly used for a broader collection
of reusable software functionality.

For example:

NumPy
Pandas
Matplotlib
SciPy
Scikit-learn

In normal discussion, the words package and library are
sometimes used interchangeably.

A simple practical interpretation is:

Module
    One Python file

Package
    Collection of related modules

Library
    Collection of tools designed for a broader purpose
"""


# ============================================================
# 4. PYTHON STANDARD LIBRARY
# ============================================================

"""
Python includes many modules automatically.

These are part of the Python Standard Library.

Examples:

math
statistics
random
csv
json
pathlib
os
sys
datetime

These normally do NOT require pip installation.
"""


# ============================================================
# 5. BASIC IMPORT
# ============================================================

"""
General syntax:

import module_name
"""


import math


print("--- Basic Import ---")

print(
    "Square Root of 25 =",
    math.sqrt(25)
)


# ============================================================
# 6. USING MODULE FUNCTIONS
# ============================================================

"""
After importing math:

math.sqrt()
math.sin()
math.cos()
math.log10()
math.pi

can be accessed using:

module.function()
"""


radius = 5

area = (
    math.pi
    * radius ** 2
)


print("\n--- Math Module ---")

print(
    f"Circle Area = {area:.2f}"
)


# ============================================================
# 7. ENGINEERING MATH EXAMPLE
# ============================================================

"""
Convert an amplitude ratio to decibels.

For amplitude quantities:

dB = 20 log10(A / A_ref)
"""


amplitude = 10
reference = 1


magnitude_db = (
    20
    * math.log10(
        amplitude / reference
    )
)


print("\n--- dB Calculation ---")

print(
    f"Magnitude = "
    f"{magnitude_db:.2f} dB"
)


# ============================================================
# 8. IMPORT SPECIFIC FUNCTION
# ============================================================

"""
Instead of importing the entire module:

import math

we can import a specific function:

from math import sqrt
"""


from math import sqrt


result = sqrt(
    81
)


print(
    "\nSquare Root of 81 =",
    result
)


# ============================================================
# 9. IMPORT MULTIPLE FUNCTIONS
# ============================================================

"""
Several functions can be imported together.
"""


from math import (
    sin,
    cos,
    pi
)


angle_deg = 30

angle_rad = (
    angle_deg
    * pi
    / 180
)


print("\n--- Trigonometric Functions ---")

print(
    f"sin(30 deg) = "
    f"{sin(angle_rad):.3f}"
)

print(
    f"cos(30 deg) = "
    f"{cos(angle_rad):.3f}"
)


# ============================================================
# 10. IMPORT ALIAS
# ============================================================

"""
Modules can be given shorter names using:

import module as alias

This is extremely common in scientific Python.
"""


import statistics as stats


measurements = [
    48.2,
    49.1,
    48.7,
    49.5,
    48.9
]


mean_voltage = stats.mean(
    measurements
)


print("\n--- Import Alias ---")

print(
    f"Mean Voltage = "
    f"{mean_voltage:.2f} V"
)


# ============================================================
# 11. COMMON SCIENTIFIC ALIASES
# ============================================================

"""
Some aliases have become standard conventions.

NumPy:

import numpy as np


Pandas:

import pandas as pd


Matplotlib:

import matplotlib.pyplot as plt


These aliases are used throughout scientific and
engineering Python code.

Example:

np.array(...)
pd.read_csv(...)
plt.plot(...)
"""


# ============================================================
# 12. STANDARD LIBRARY - RANDOM
# ============================================================

"""
The random module can generate random values.

This can be useful for:

- Demonstrations
- Testing algorithms
- Simulated measurements
- Monte Carlo examples

For serious numerical simulation, NumPy normally provides
more advanced random-number functionality.
"""


import random


random_voltage = random.uniform(
    47,
    49
)


print("\n--- Random Module ---")

print(
    f"Simulated Voltage = "
    f"{random_voltage:.2f} V"
)


# ============================================================
# 13. STANDARD LIBRARY - DATETIME
# ============================================================

"""
datetime provides date and time functionality.

This can be useful for:

- Measurement timestamps
- Log files
- Experiment records
- Automated data processing
"""


from datetime import datetime


current_time = datetime.now()


print("\n--- Date and Time ---")

print(
    "Current Timestamp:",
    current_time
)


# ============================================================
# 14. STANDARD LIBRARY - PATHLIB
# ============================================================

"""
pathlib provides modern tools for file and folder paths.

It was introduced in the File Handling section.
"""


from pathlib import Path


current_directory = Path.cwd()


print("\n--- pathlib ---")

print(
    "Current Directory:",
    current_directory
)


# ============================================================
# 15. THIRD-PARTY PACKAGES
# ============================================================

"""
Third-party packages are not normally part of the basic
Python installation.

Examples:

numpy
pandas
matplotlib
scipy
scikit-learn
openpyxl
tensorflow
torch


They normally need to be installed before use.
"""


# ============================================================
# 16. INSTALL PACKAGES WITH pip
# ============================================================

"""
pip is Python's commonly used package installer.

Run these commands in a terminal or command prompt,
NOT normally inside the Python script.

Example:

pip install numpy

pip install pandas

pip install matplotlib

pip install scipy

pip install scikit-learn


Multiple packages:

pip install numpy pandas matplotlib scipy scikit-learn
"""


# ============================================================
# 17. CHECK INSTALLED PACKAGES
# ============================================================

"""
Terminal command:

pip list


This displays installed Python packages.


To inspect a particular package:

pip show numpy
"""


# ============================================================
# 18. PACKAGE VERSION
# ============================================================

"""
Many third-party libraries provide a version attribute.

Example:

import numpy as np

print(np.__version__)


Knowing package versions is important for reproducible
research because library behavior can change between
versions.
"""


# ============================================================
# 19. REQUIREMENTS.TXT
# ============================================================

"""
A requirements.txt file records dependencies required
by a Python project.

Example:

numpy
pandas
matplotlib
scipy
scikit-learn
openpyxl


A more reproducible version may specify versions:

numpy==2.x.x
pandas==2.x.x
matplotlib==3.x.x


Install all packages listed in requirements.txt using:

pip install -r requirements.txt


For this GitHub repository, we can create a requirements.txt
later as the project grows.
"""


# ============================================================
# 20. WHY REQUIREMENTS.TXT MATTERS
# ============================================================

"""
Suppose another researcher downloads a GitHub project.

Without dependency information, they may not know which
packages are required.

With:

requirements.txt

they can install the required environment more easily.

This improves:

- Reproducibility
- Collaboration
- Portability
- Research transparency
"""


# ============================================================
# 21. CREATING A CUSTOM MODULE
# ============================================================

"""
Suppose we create:

engineering_tools.py


Contents:

def calculate_power(voltage, current):

    return voltage * current


def calculate_efficiency(pin, pout):

    return (pout / pin) * 100


Then another Python file can use:

import engineering_tools


power = engineering_tools.calculate_power(
    48,
    5
)
"""


# ============================================================
# 22. IMPORT FUNCTION FROM CUSTOM MODULE
# ============================================================

"""
Instead of:

import engineering_tools

we could write:

from engineering_tools import calculate_power


Then:

power = calculate_power(
    48,
    5
)


The module must be available in a location Python can find.
"""


# ============================================================
# 23. CUSTOM MODULE WITH ALIAS
# ============================================================

"""
A custom module may also use an alias:

import engineering_tools as et


power = et.calculate_power(
    48,
    5
)
"""


# ============================================================
# 24. WHY CREATE CUSTOM MODULES?
# ============================================================

"""
Imagine a research script containing:

calculate_power()
calculate_efficiency()
calculate_rms()
calculate_fft()
load_measurement()
clean_data()
plot_signal()
save_figure()

Instead of keeping everything in one huge script,
functions can be organized into modules.

Example:

research_project/
│
├── main.py
│
├── calculations.py
│
├── signal_processing.py
│
├── data_processing.py
└── plotting.py
"""


# ============================================================
# 25. EXAMPLE PROJECT ORGANIZATION
# ============================================================

"""
A larger engineering project may eventually look like:

project/
│
├── main.py
│
├── data/
│   ├── case_A.csv
│   └── case_B.csv
│
├── results/
│
├── calculations/
│   ├── power.py
│   └── efficiency.py
│
├── processing/
│   ├── cleaning.py
│   └── fft.py
│
└── plotting/
    └── figures.py


This is easier to maintain than one very large
Python file.
"""


# ============================================================
# 26. __name__
# ============================================================

"""
Every Python module has a special variable:

__name__


When a Python file is run directly:

__name__ == "__main__"


When the file is imported as a module:

__name__

normally contains the module name.
"""


print("\n--- __name__ Example ---")

print(
    "__name__ =",
    __name__
)


# ============================================================
# 27. if __name__ == "__main__"
# ============================================================

"""
A common Python structure is:

if __name__ == "__main__":

    code


This means:

Run this part only when the file is executed directly.

Do not automatically run this part when the file is
imported into another Python program.
"""


def calculate_converter_power(
    voltage,
    current
):

    return voltage * current


if __name__ == "__main__":

    print(
        "\n--- Main Program ---"
    )

    power = calculate_converter_power(
        voltage=48,
        current=5
    )

    print(
        f"Converter Power = "
        f"{power:.2f} W"
    )


# ============================================================
# 28. WHY __main__ IS USEFUL
# ============================================================

"""
Suppose:

engineering_tools.py

contains many reusable functions.

If another file imports it:

import engineering_tools

we normally do not want all demonstration code inside
engineering_tools.py to execute automatically.

Therefore:

if __name__ == "__main__":

allows us to separate:

Reusable functions

from

Demonstration / test code.
"""


# ============================================================
# 29. SCIENTIFIC PYTHON ECOSYSTEM
# ============================================================

"""
For engineering and research, a typical Python ecosystem is:

Python
│
├── NumPy
│     Numerical arrays and matrix operations
│
├── Pandas
│     Tabular data and CSV/Excel processing
│
├── Matplotlib
│     Scientific plotting
│
├── SciPy
│     Scientific computing and signal processing
│
├── Scikit-learn
│     Machine learning
│
├── OpenPyXL
│     Excel workbook handling
│
├── TensorFlow / PyTorch
│     Deep learning
│
└── Other specialized packages
"""


# ============================================================
# 30. NUMPY EXAMPLE - PREVIEW
# ============================================================

"""
Later in this repository we will use:

import numpy as np


Example:

voltage = np.array(
    [48, 49, 50, 51]
)

mean_voltage = np.mean(
    voltage
)


NumPy will be covered thoroughly in the next major section.
"""


# ============================================================
# 31. PANDAS EXAMPLE - PREVIEW
# ============================================================

"""
Typical Pandas code:

import pandas as pd


data = pd.read_csv(
    "measurements.csv"
)


Then:

data["Voltage"]

selects the Voltage column.


Pandas will be covered in its own section.
"""


# ============================================================
# 32. MATPLOTLIB EXAMPLE - PREVIEW
# ============================================================

"""
Typical plotting code:

import matplotlib.pyplot as plt


plt.plot(
    time,
    voltage
)

plt.xlabel(
    "Time [s]"
)

plt.ylabel(
    "Voltage [V]"
)

plt.show()


Our Data Visualization section will explore plotting
much more thoroughly.
"""


# ============================================================
# 33. SCIPY EXAMPLE - PREVIEW
# ============================================================

"""
SciPy provides scientific tools such as:

Signal processing
Optimization
Integration
Interpolation
Statistics


Example import:

from scipy import signal


or:

from scipy.signal import find_peaks
"""


# ============================================================
# 34. SCIKIT-LEARN EXAMPLE - PREVIEW
# ============================================================

"""
Scikit-learn is commonly imported using specific modules.

Example:

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression


These will be covered later in the Machine Learning section.
"""


# ============================================================
# 35. ENGINEERING IMPORT PATTERN
# ============================================================

"""
A typical engineering data-analysis script may start with:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from scipy import signal


Then the workflow could be:

Load CSV
    ↓
Pandas

Numerical Calculation
    ↓
NumPy

Signal Processing
    ↓
SciPy

Plot Results
    ↓
Matplotlib
"""


# ============================================================
# 36. AVOID import *
# ============================================================

"""
Python allows:

from math import *


However, this is generally discouraged.

Why?

It becomes difficult to determine where functions
and variables originated.

Better:

import math

math.sqrt(25)


or:

from math import sqrt

sqrt(25)
"""


# ============================================================
# 37. IMPORT AT THE TOP OF THE FILE
# ============================================================

"""
Most Python scripts place imports near the beginning.

Typical structure:

import math
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


Then:

Constants
Functions
Main program


This makes dependencies easy to identify.
"""


# ============================================================
# 38. STANDARD VS THIRD-PARTY IMPORTS
# ============================================================

"""
A clean Python file may separate imports:

# Standard Library

import math
import csv
from pathlib import Path


# Third-Party Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Local Project Modules

from engineering_tools import calculate_power


This organization improves readability.
"""


# ============================================================
# 39. VIRTUAL ENVIRONMENTS
# ============================================================

"""
Different Python projects may require different package
versions.

A virtual environment creates an isolated Python
environment for a project.

Typical terminal command:

python -m venv .venv


Activation on Windows:

.venv\\Scripts\\activate


Activation on Linux/macOS:

source .venv/bin/activate


Then packages installed using pip remain associated with
that environment.

Virtual environments are especially useful for:

- Research projects
- Machine learning
- Reproducibility
- Different package versions
- GitHub projects
"""


# ============================================================
# 40. CHECK WHICH PYTHON IS RUNNING
# ============================================================

"""
The sys module can provide information about the
current Python environment.
"""


import sys


print("\n--- Python Environment ---")

print(
    "Python Version:"
)

print(
    sys.version
)


print(
    "\nPython Executable:"
)

print(
    sys.executable
)


# ============================================================
# 41. GOOD RESEARCH PRACTICE
# ============================================================

"""
For reproducible engineering or research code:

1. Keep code organized into modules.

2. Record required third-party packages.

3. Record package versions when reproducibility matters.

4. Use meaningful module names.

5. Avoid copying the same function into many files.

6. Use reusable functions.

7. Keep data, processing, plotting, and results logically
   organized.

8. Document dependencies in README.md or requirements.txt.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
MODULES AND PACKAGES


1. MODULE

Usually one Python file.

Example:

engineering_tools.py


------------------------------------------------------------


2. PACKAGE

Collection of related modules.

Example:

engineering_tools/
│
├── power.py
├── signals.py
└── plotting.py


------------------------------------------------------------


3. LIBRARY

Broader collection of reusable functionality.

Examples:

NumPy
Pandas
Matplotlib
SciPy


------------------------------------------------------------


4. BASIC IMPORT

import math


Use:

math.sqrt(25)


------------------------------------------------------------


5. IMPORT SPECIFIC FUNCTION

from math import sqrt


Use:

sqrt(25)


------------------------------------------------------------


6. IMPORT WITH ALIAS

import statistics as stats


Scientific conventions:

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt


------------------------------------------------------------


7. STANDARD LIBRARY

Usually included with Python.

Examples:

math
csv
json
statistics
pathlib
datetime
random
sys


------------------------------------------------------------


8. THIRD-PARTY PACKAGES

Normally installed separately.

Examples:

numpy
pandas
matplotlib
scipy
scikit-learn
openpyxl


------------------------------------------------------------


9. INSTALL PACKAGE

Terminal:

pip install numpy


------------------------------------------------------------


10. INSTALL MULTIPLE PACKAGES

pip install numpy pandas matplotlib scipy


------------------------------------------------------------


11. REQUIREMENTS FILE

requirements.txt

Example:

numpy
pandas
matplotlib
scipy


Install:

pip install -r requirements.txt


------------------------------------------------------------


12. CUSTOM MODULE

engineering_tools.py


Then:

import engineering_tools


or:

from engineering_tools import calculate_power


------------------------------------------------------------


13. MAIN GUARD

if __name__ == "__main__":

    main_program()


Useful when a file contains both:

Reusable functions

and

Demonstration/testing code.


------------------------------------------------------------


14. VIRTUAL ENVIRONMENT

Create:

python -m venv .venv


Purpose:

Keep project dependencies isolated.


------------------------------------------------------------


SCIENTIFIC PYTHON STACK


Python
   ↓
NumPy
   ↓
Pandas
   ↓
Matplotlib
   ↓
SciPy
   ↓
Scikit-learn
   ↓
Engineering / Research Applications


------------------------------------------------------------


QUICK REVISION


np
    NumPy


pd
    Pandas


plt
    Matplotlib pyplot


pip
    Package installer


requirements.txt
    Project dependency list


.venv
    Isolated project environment


__name__ == "__main__"
    Run code only when the file is executed directly


------------------------------------------------------------


ENGINEERING / RESEARCH USE

Modules and packages allow us to organize:

- Numerical calculations
- Data-processing functions
- Signal-processing algorithms
- FFT analysis
- Plotting utilities
- Measurement processing
- Simulation automation
- Machine-learning models
- Reusable research code


Instead of one very large Python script:

main.py
    2000+ lines


A project can be organized as:

main.py
calculations.py
processing.py
signals.py
plotting.py


This makes research code easier to:

Understand
Maintain
Reuse
Validate
Share
Reproduce
"""
