"""
============================================================
Python for Engineering and Research
19 - High-Resolution Figures
============================================================

Purpose:
    Demonstrate how figure size, DPI, pixel dimensions,
    font size, line width, marker size, raster/vector
    formats, and document scaling affect the quality of
    engineering and research figures.

Topics:
    1. What is a high-resolution figure?
    2. Figure size vs DPI
    3. Pixel dimensions
    4. 72, 150, 300, and 600 DPI
    5. Physical figure dimensions
    6. Inches, mm, and cm
    7. Single-column figures
    8. Double-column figures
    9. Font size and final document scaling
    10. Line width and marker size
    11. High-resolution PNG export
    12. PDF and SVG vector export
    13. Raster vs vector content
    14. File-size comparison
    15. Automatic DPI comparison
    16. Frequency-domain engineering example
    17. Saving publication-size figures
    18. Reusable high-resolution export function
    19. Rasterization concepts
    20. Common mistakes
    21. Key takeaways

Important:
    Higher DPI does NOT automatically improve the scientific
    quality of a figure.

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pathlib import Path


# ============================================================
# 2. WHAT IS A HIGH-RESOLUTION FIGURE?
# ============================================================

"""
A high-resolution figure contains enough graphical detail
for its intended final use.

Examples:

Screen preview
    ↓
Moderate resolution may be sufficient


Presentation
    ↓
High-resolution PNG may be useful


Journal paper
    ↓
High-resolution raster
or
vector PDF/SVG


Thesis
    ↓
Vector figures are often useful for line plots


A high-resolution figure is NOT simply:

"The largest possible DPI value."


Figure quality depends on:

- Figure dimensions
- Resolution
- Font size
- Line width
- Marker size
- File format
- Final document scaling
- Scientific clarity
"""


# ============================================================
# 3. BASIC ENGINEERING DATA
# ============================================================

load_percent = np.array(
    [
        10,
        20,
        30,
        40,
        50,
        60,
        70,
        80,
        90,
        100
    ],
    dtype=float
)


efficiency = np.array(
    [
        88.5,
        91.0,
        92.8,
        94.0,
        94.8,
        95.3,
        95.6,
        95.5,
        95.2,
        94.8
    ]
)


# ============================================================
# 4. OUTPUT FOLDER
# ============================================================

script_folder = Path(
    __file__
).resolve().parent


output_folder = (
    script_folder
    / "output_figures"
    / "high_resolution"
)


output_folder.mkdir(
    parents=True,
    exist_ok=True
)


print(
    "\n--- Output Folder ---"
)


print(
    output_folder
)


# ============================================================
# 5. FIGURE SIZE
# ============================================================

"""
Matplotlib figure size is normally specified in:

INCHES


Example:

figsize=(7, 4.5)


means:

Width  = 7 inches

Height = 4.5 inches
"""


fig, ax = plt.subplots(
    figsize=(
        7,
        4.5
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    linewidth=2
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Converter Efficiency"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 6. WHAT IS DPI?
# ============================================================

"""
DPI means:

Dots Per Inch


For raster graphics, DPI controls how many image pixels
are generated for each inch of physical figure size.


Simplified relationship:

Pixel Width
    =
Figure Width [inch]
    ×
DPI


Pixel Height
    =
Figure Height [inch]
    ×
DPI
"""


# ============================================================
# 7. PIXEL-DIMENSION EXAMPLE
# ============================================================

figure_width_in = 6

figure_height_in = 4

dpi = 300


pixel_width = (
    figure_width_in
    * dpi
)


pixel_height = (
    figure_height_in
    * dpi
)


print(
    "\n--- Pixel Dimension Example ---"
)


print(
    "Figure Width:",
    figure_width_in,
    "in"
)


print(
    "Figure Height:",
    figure_height_in,
    "in"
)


print(
    "DPI:",
    dpi
)


print(
    "Approximate Pixel Width:",
    pixel_width
)


print(
    "Approximate Pixel Height:",
    pixel_height
)


# ============================================================
# 8. EXAMPLE CALCULATION
# ============================================================

"""
For:

figsize=(6, 4)

dpi=300


Approximate raster dimensions:

6 × 300
=
1800 pixels


4 × 300
=
1200 pixels


Therefore:

approximately

1800 × 1200 pixels


Note:

bbox_inches="tight"

can slightly change the final pixel dimensions because
Matplotlib adjusts the exported bounding box.
"""


# ============================================================
# 9. COMMON DPI VALUES
# ============================================================

"""
Typical example values:

72 DPI
    Low-resolution / screen-type example


150 DPI
    Moderate-resolution example


300 DPI
    Common high-quality raster export


600 DPI
    Higher-resolution raster export


These are examples only.

Always follow the actual requirements of:

- Journal
- Conference
- Publisher
- Thesis template
- Institution
"""


# ============================================================
# 10. SAVE SAME FIGURE AT DIFFERENT DPI
# ============================================================

dpi_values = [
    72,
    150,
    300,
    600
]


fig, ax = plt.subplots(
    figsize=(
        6,
        4
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    linewidth=2
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Efficiency vs Load"
)


ax.grid(
    True
)


plt.tight_layout()


for dpi_value in dpi_values:

    output_file = (
        output_folder
        / f"efficiency_{dpi_value}dpi.png"
    )


    fig.savefig(
        output_file,
        dpi=dpi_value,
        bbox_inches="tight"
    )


    print(
        "Saved:",
        output_file
    )


plt.show()


# ============================================================
# 11. APPROXIMATE PIXEL SIZE FOR EACH DPI
# ============================================================

figure_width = 6

figure_height = 4


print(
    "\n--- Approximate Pixel Dimensions ---"
)


for dpi_value in dpi_values:

    width_pixels = (
        figure_width
        * dpi_value
    )


    height_pixels = (
        figure_height
        * dpi_value
    )


    print(
        f"{dpi_value} DPI:"
    )


    print(
        f"  Approx. "
        f"{width_pixels:.0f} × "
        f"{height_pixels:.0f} pixels"
    )


# ============================================================
# 12. EXPECTED PIXEL DIMENSIONS
# ============================================================

"""
For a 6 × 4 inch figure:


72 DPI

432 × 288 pixels


150 DPI

900 × 600 pixels


300 DPI

1800 × 1200 pixels


600 DPI

3600 × 2400 pixels


The number of pixels increases significantly with DPI.
"""


# ============================================================
# 13. PIXEL COUNT INCREASE
# ============================================================

"""
Doubling DPI:

300
    ↓
600


doubles:

Width in pixels

and

Height in pixels


Therefore total pixel count increases approximately by:

2 × 2
=
4 times


This is one reason high-DPI raster files may become much
larger.
"""


# ============================================================
# 14. FIGURE SIZE VS DPI
# ============================================================

"""
Figure Size

controls:

Physical dimensions


DPI

controls:

Raster sampling density


They are related but NOT identical concepts.


Example A:

6 × 4 inches
at
300 DPI


Example B:

3 × 2 inches
at
600 DPI


Both produce approximately:

1800 × 1200 pixels


but their intended physical sizes are different.
"""


# ============================================================
# 15. DEMONSTRATE SAME PIXEL SIZE
# ============================================================

case_a_width = 6

case_a_height = 4

case_a_dpi = 300


case_b_width = 3

case_b_height = 2

case_b_dpi = 600


case_a_pixels = (
    case_a_width
    * case_a_dpi,
    case_a_height
    * case_a_dpi
)


case_b_pixels = (
    case_b_width
    * case_b_dpi,
    case_b_height
    * case_b_dpi
)


print(
    "\n--- Same Approximate Pixel Count ---"
)


print(
    "Case A:",
    case_a_pixels
)


print(
    "Case B:",
    case_b_pixels
)


# ============================================================
# 16. INCHES, MILLIMETERS, AND CENTIMETERS
# ============================================================

"""
Matplotlib uses inches for figsize.

However, journals often specify figure widths in:

mm

or

cm


Useful conversion:

1 inch = 25.4 mm

1 inch = 2.54 cm
"""


def mm_to_inches(
    millimeters
):
    """
    Convert millimeters to inches.
    """

    return (
        millimeters
        / 25.4
    )


def cm_to_inches(
    centimeters
):
    """
    Convert centimeters to inches.
    """

    return (
        centimeters
        / 2.54
    )


# ============================================================
# 17. MILLIMETER CONVERSION EXAMPLE
# ============================================================

width_mm = 90


width_inches = mm_to_inches(
    width_mm
)


print(
    "\n--- Millimeter Conversion ---"
)


print(
    f"{width_mm} mm = "
    f"{width_inches:.3f} inches"
)


# ============================================================
# 18. CENTIMETER CONVERSION EXAMPLE
# ============================================================

width_cm = 18


width_inches_from_cm = cm_to_inches(
    width_cm
)


print(
    "\n--- Centimeter Conversion ---"
)


print(
    f"{width_cm} cm = "
    f"{width_inches_from_cm:.3f} inches"
)


# ============================================================
# 19. EXAMPLE SINGLE-COLUMN FIGURE
# ============================================================

"""
Many journals use approximately one-column and two-column
figure layouts.

The exact dimensions vary between publishers.

Therefore the values below are EDUCATIONAL EXAMPLES,
not universal publication requirements.


Example single-column width:

approximately 85-90 mm
"""


single_column_width_mm = 88


single_column_width_in = mm_to_inches(
    single_column_width_mm
)


single_column_height_in = (
    single_column_width_in
    * 0.72
)


print(
    "\n--- Example Single-Column Size ---"
)


print(
    "Width:",
    single_column_width_in,
    "inches"
)


print(
    "Height:",
    single_column_height_in,
    "inches"
)


# ============================================================
# 20. CREATE SINGLE-COLUMN FIGURE
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        single_column_width_in,
        single_column_height_in
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    linewidth=1.5
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()


single_column_file = (
    output_folder
    / "single_column_example.png"
)


fig.savefig(
    single_column_file,
    dpi=300,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 21. EXAMPLE DOUBLE-COLUMN FIGURE
# ============================================================

"""
Example double-column width:

approximately 175-180 mm


Again:

This is only an example.

Always check the target publication requirements.
"""


double_column_width_mm = 178


double_column_width_in = mm_to_inches(
    double_column_width_mm
)


double_column_height_in = (
    double_column_width_in
    * 0.55
)


print(
    "\n--- Example Double-Column Size ---"
)


print(
    "Width:",
    double_column_width_in,
    "inches"
)


print(
    "Height:",
    double_column_height_in,
    "inches"
)


# ============================================================
# 22. CREATE DOUBLE-COLUMN FIGURE
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        double_column_width_in,
        double_column_height_in
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    linewidth=2
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)

ax.set_title(
    "Double-Column Figure Example"
)


ax.grid(
    True
)


plt.tight_layout()


double_column_file = (
    output_folder
    / "double_column_example.png"
)


fig.savefig(
    double_column_file,
    dpi=300,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 23. FINAL FIGURE SIZE MATTERS
# ============================================================

"""
Suppose a figure is created at:

8 inches wide


but later inserted into a paper at:

3.5 inches wide


The figure will be reduced significantly.


This also reduces the apparent size of:

- Text
- Markers
- Line widths
- Legend
- Annotations


Therefore publication figures should ideally be designed
close to their intended final dimensions.
"""


# ============================================================
# 24. FONT SIZE
# ============================================================

"""
High resolution does NOT automatically make text readable.

Example:

600 DPI figure
+
5-point font


may still be difficult to read after document scaling.


Font size should be chosen according to the intended final
figure dimensions.
"""


# ============================================================
# 25. BASIC FONT-SIZE CONTROL
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        6,
        4
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    linewidth=2
)


ax.set_xlabel(
    "Load [%]",
    fontsize=11
)


ax.set_ylabel(
    "Efficiency [%]",
    fontsize=11
)


ax.set_title(
    "Converter Efficiency",
    fontsize=12
)


ax.tick_params(
    axis="both",
    labelsize=10
)


ax.grid(
    True
)


plt.tight_layout()


font_example_file = (
    output_folder
    / "font_size_example.png"
)


fig.savefig(
    font_example_file,
    dpi=300,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 26. LEGEND FONT SIZE
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        6,
        4
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    label="Efficiency"
)


ax.set_xlabel(
    "Load [%]",
    fontsize=11
)


ax.set_ylabel(
    "Efficiency [%]",
    fontsize=11
)


ax.legend(
    fontsize=9
)


ax.tick_params(
    labelsize=9
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 27. LINE WIDTH
# ============================================================

"""
A high-resolution figure with extremely thin lines may
still be difficult to read.

Control line thickness using:

linewidth=
"""


fig, ax = plt.subplots(
    figsize=(
        6,
        4
    )
)


ax.plot(
    load_percent,
    efficiency,
    linewidth=2
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 28. MARKER SIZE
# ============================================================

"""
Marker visibility can be controlled using:

markersize=


Markers that look large on a computer monitor may become
small when the figure is reduced for publication.
"""


fig, ax = plt.subplots(
    figsize=(
        6,
        4
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    markersize=6,
    linewidth=1.8
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()

plt.show()


# ============================================================
# 29. DPI DOES NOT CONTROL FONT SIZE
# ============================================================

"""
Important:

dpi=600


does NOT mean:

font size = 600


Font sizes are controlled independently.


For example:

fontsize=10

linewidth=1.5

markersize=5


should be selected according to the final visual size and
publication requirements.
"""


# ============================================================
# 30. FIGURE DPI VS SAVE DPI
# ============================================================

"""
Matplotlib has two related concepts:

Figure DPI

and

Save DPI


Example:

fig, ax = plt.subplots(
    dpi=100
)


This affects the figure object's default rendering.


Later:

fig.savefig(
    "figure.png",
    dpi=600
)


exports the raster file at:

600 DPI


The savefig DPI can therefore differ from the interactive
figure DPI.
"""


# ============================================================
# 31. FIGURE DPI EXAMPLE
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        6,
        4
    ),
    dpi=100
)


ax.plot(
    load_percent,
    efficiency
)


print(
    "\nFigure Object DPI:"
)


print(
    fig.dpi
)


plt.close(
    fig
)


# ============================================================
# 32. SAVEFIG DPI EXAMPLE
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        6,
        4
    ),
    dpi=100
)


ax.plot(
    load_percent,
    efficiency
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


save_dpi_example = (
    output_folder
    / "figure_object_100dpi_saved_600dpi.png"
)


fig.savefig(
    save_dpi_example,
    dpi=600,
    bbox_inches="tight"
)


plt.close(
    fig
)


# ============================================================
# 33. USE dpi="figure"
# ============================================================

"""
Matplotlib can also save using the figure object's own DPI:

fig.savefig(
    "figure.png",
    dpi="figure"
)


This is useful when the figure's DPI has already been
configured intentionally.
"""


fig, ax = plt.subplots(
    figsize=(
        6,
        4
    ),
    dpi=200
)


ax.plot(
    load_percent,
    efficiency
)


figure_dpi_file = (
    output_folder
    / "use_figure_dpi.png"
)


fig.savefig(
    figure_dpi_file,
    dpi="figure",
    bbox_inches="tight"
)


plt.close(
    fig
)


# ============================================================
# 34. HIGH-RESOLUTION PNG
# ============================================================

"""
A common high-quality PNG workflow:

fig.savefig(
    "figure.png",
    dpi=300,
    bbox_inches="tight"
)
"""


fig, ax = plt.subplots(
    figsize=(
        6,
        4
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    markersize=5,
    linewidth=1.8
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()


high_resolution_png = (
    output_folder
    / "high_resolution_efficiency.png"
)


fig.savefig(
    high_resolution_png,
    dpi=300,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 35. 600 DPI PNG
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        6,
        4
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    markersize=5,
    linewidth=1.8
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()


very_high_resolution_png = (
    output_folder
    / "high_resolution_efficiency_600dpi.png"
)


fig.savefig(
    very_high_resolution_png,
    dpi=600,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 36. PDF VECTOR EXPORT
# ============================================================

"""
For line plots, PDF can preserve vector graphics.

This means lines and text are represented geometrically
rather than simply as a fixed grid of pixels.
"""


fig, ax = plt.subplots(
    figsize=(
        6,
        4
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    linewidth=1.8
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()


vector_pdf = (
    output_folder
    / "high_resolution_efficiency.pdf"
)


fig.savefig(
    vector_pdf,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 37. SVG VECTOR EXPORT
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        6,
        4
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    linewidth=1.8
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()


vector_svg = (
    output_folder
    / "high_resolution_efficiency.svg"
)


fig.savefig(
    vector_svg,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 38. RASTER VS VECTOR
# ============================================================

"""
RASTER

Examples:

PNG

JPEG

TIFF


Stored primarily as pixels.


Resolution matters strongly.


------------------------------------------------------------


VECTOR

Examples:

PDF

SVG


Lines, text, and shapes can be stored mathematically.


They can usually be enlarged without conventional
pixelation.


For scientific line plots:

PDF and SVG can be very useful.
"""


# ============================================================
# 39. VECTOR DOES NOT ALWAYS MEAN EVERYTHING IS VECTOR
# ============================================================

"""
A PDF or SVG figure may contain raster elements.

Examples:

Images

Photographs

Heatmaps

imshow()

Some very dense graphical objects

Explicitly rasterized artists


Therefore:

PDF / SVG
    ≠
guaranteed 100% vector content


The actual result depends on what is inside the figure.
"""


# ============================================================
# 40. CHECK GENERATED FILE SIZES
# ============================================================

"""
Higher-resolution raster files may require more storage.

Let's inspect the generated DPI examples.
"""


print(
    "\n--- File Size Comparison ---"
)


for dpi_value in dpi_values:

    file_path = (
        output_folder
        / f"efficiency_{dpi_value}dpi.png"
    )


    if file_path.exists():

        size_bytes = (
            file_path
            .stat()
            .st_size
        )


        size_kb = (
            size_bytes
            / 1024
        )


        print(
            f"{dpi_value} DPI:"
            f" {size_kb:.2f} kB"
        )


# ============================================================
# 41. FILE SIZE IS NOT QUALITY
# ============================================================

"""
A larger file does not automatically mean:

Better science

Better visualization

Better readability


A huge 1200 DPI image with:

Tiny text

Poor labels

Bad axes

and

unclear data


is still a poor figure.
"""


# ============================================================
# 42. AUTOMATIC DPI COMPARISON FUNCTION
# ============================================================

def save_at_multiple_dpi(
    fig,
    output_folder,
    filename,
    dpi_values
):
    """
    Save the same Matplotlib figure at several raster
    resolutions.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to export.

    output_folder : str or Path
        Output directory.

    filename : str
        Base filename.

    dpi_values : iterable
        DPI values.

    Returns
    -------
    saved_files : list
        Generated PNG files.
    """

    output_folder = Path(
        output_folder
    )


    output_folder.mkdir(
        parents=True,
        exist_ok=True
    )


    saved_files = []


    for dpi_value in dpi_values:

        if dpi_value <= 0:

            raise ValueError(
                "DPI must be greater than zero."
            )


        output_file = (
            output_folder
            / (
                f"{filename}_"
                f"{dpi_value}dpi.png"
            )
        )


        fig.savefig(
            output_file,
            dpi=dpi_value,
            bbox_inches="tight"
        )


        saved_files.append(
            output_file
        )


    return saved_files


# ============================================================
# 43. USE MULTIPLE-DPI FUNCTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        6,
        4
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    linewidth=2
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.grid(
    True
)


plt.tight_layout()


saved_dpi_files = save_at_multiple_dpi(

    fig=fig,

    output_folder=output_folder,

    filename="automatic_dpi_test",

    dpi_values=[
        150,
        300,
        600
    ]

)


print(
    "\n--- Automatic DPI Exports ---"
)


for file_path in saved_dpi_files:

    print(
        file_path
    )


plt.show()


# ============================================================
# 44. CREATE PIXEL-DIMENSION FUNCTION
# ============================================================

def calculate_pixel_dimensions(
    width_in,
    height_in,
    dpi
):
    """
    Calculate approximate raster dimensions.

    Returns
    -------
    width_pixels : int

    height_pixels : int
    """

    if width_in <= 0:

        raise ValueError(
            "Figure width must be positive."
        )


    if height_in <= 0:

        raise ValueError(
            "Figure height must be positive."
        )


    if dpi <= 0:

        raise ValueError(
            "DPI must be positive."
        )


    width_pixels = round(
        width_in
        * dpi
    )


    height_pixels = round(
        height_in
        * dpi
    )


    return (
        width_pixels,
        height_pixels
    )


# ============================================================
# 45. USE PIXEL-DIMENSION FUNCTION
# ============================================================

width_pixels, height_pixels = (
    calculate_pixel_dimensions(
        width_in=7,
        height_in=4.5,
        dpi=300
    )
)


print(
    "\n--- Calculated Raster Size ---"
)


print(
    f"{width_pixels} × "
    f"{height_pixels} pixels"
)


# ============================================================
# 46. TARGET PIXEL WIDTH
# ============================================================

"""
Sometimes the required raster width is known.

Example:

Target width:

2400 pixels


Desired DPI:

300


Required physical width:

2400 / 300
=
8 inches
"""


target_pixel_width = 2400

target_dpi = 300


required_width_inches = (

    target_pixel_width

    / target_dpi

)


print(
    "\n--- Required Physical Width ---"
)


print(
    f"{required_width_inches:.2f} inches"
)


# ============================================================
# 47. FUNCTION FOR TARGET PIXEL SIZE
# ============================================================

def pixels_to_inches(
    pixels,
    dpi
):
    """
    Calculate required physical size in inches from
    target raster pixels and DPI.
    """

    if pixels <= 0:

        raise ValueError(
            "Pixel count must be positive."
        )


    if dpi <= 0:

        raise ValueError(
            "DPI must be positive."
        )


    return (
        pixels
        / dpi
    )


# ============================================================
# 48. EXAMPLE TARGET WIDTH
# ============================================================

required_width = pixels_to_inches(
    pixels=1800,
    dpi=300
)


print(
    "\n1800 pixels at 300 DPI ="
)


print(
    f"{required_width:.2f} inches"
)


# ============================================================
# 49. LOAD SAMPLE FFT DATA
# ============================================================

fft_file = (
    script_folder
    / "sample_data"
    / "fft_example.csv"
)


if not fft_file.exists():

    raise FileNotFoundError(
        f"\nFFT sample file not found:\n"
        f"{fft_file}"
    )


fft_data = pd.read_csv(
    fft_file
)


print(
    "\n--- FFT Columns ---"
)


print(
    fft_data.columns.tolist()
)


# ============================================================
# 50. HIGH-RESOLUTION FREQUENCY-DOMAIN FIGURE
# ============================================================

frequency_cases = {

    "Unshielded":
        "Unshielded_dBuV",

    "Case A":
        "Case_A_dBuV",

    "Case B":
        "Case_B_dBuV",

    "Case C":
        "Case_C_dBuV"

}


fig, ax = plt.subplots(
    figsize=(
        7,
        4.5
    )
)


for case_name, column_name in frequency_cases.items():

    ax.plot(

        fft_data[
            "Frequency_Hz"
        ],

        fft_data[
            column_name
        ],

        linewidth=1.8,

        label=case_name

    )


ax.set_xscale(
    "log"
)


ax.set_xlim(
    10e3,
    30e6
)


ax.set_xlabel(
    "Frequency [Hz]",
    fontsize=11
)


ax.set_ylabel(
    "Magnitude [dBµV]",
    fontsize=11
)


ax.tick_params(
    axis="both",
    labelsize=9
)


ax.legend(
    fontsize=9,
    ncol=2
)


ax.grid(
    True,
    which="both"
)


plt.tight_layout()


# ============================================================
# 51. SAVE FFT AT 300 DPI
# ============================================================

fft_png_300 = (
    output_folder
    / "fft_comparison_300dpi.png"
)


fig.savefig(
    fft_png_300,
    dpi=300,
    bbox_inches="tight"
)


# ============================================================
# 52. SAVE FFT AT 600 DPI
# ============================================================

fft_png_600 = (
    output_folder
    / "fft_comparison_600dpi.png"
)


fig.savefig(
    fft_png_600,
    dpi=600,
    bbox_inches="tight"
)


# ============================================================
# 53. SAVE FFT AS PDF
# ============================================================

fft_pdf = (
    output_folder
    / "fft_comparison.pdf"
)


fig.savefig(
    fft_pdf,
    bbox_inches="tight"
)


# ============================================================
# 54. SAVE FFT AS SVG
# ============================================================

fft_svg = (
    output_folder
    / "fft_comparison.svg"
)


fig.savefig(
    fft_svg,
    bbox_inches="tight"
)


print(
    "\n--- FFT Figures Saved ---"
)


print(
    fft_png_300
)


print(
    fft_png_600
)


print(
    fft_pdf
)


print(
    fft_svg
)


plt.show()


# ============================================================
# 55. CREATE FIGURE AT FINAL PHYSICAL WIDTH
# ============================================================

"""
Suppose an example publication requires:

Width = 90 mm


Rather than creating:

10-inch figure

and shrinking it later,


create it close to:

90 mm
"""


final_width_mm = 90


final_width_in = mm_to_inches(
    final_width_mm
)


final_height_in = (
    final_width_in
    * 0.75
)


fig, ax = plt.subplots(
    figsize=(
        final_width_in,
        final_height_in
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    markersize=4,
    linewidth=1.4
)


ax.set_xlabel(
    "Load [%]",
    fontsize=9
)


ax.set_ylabel(
    "Efficiency [%]",
    fontsize=9
)


ax.tick_params(
    labelsize=8
)


ax.grid(
    True
)


plt.tight_layout()


final_size_file = (
    output_folder
    / "final_physical_size_example.pdf"
)


fig.savefig(
    final_size_file,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 56. WHY FINAL WIDTH SHOULD BE CONSIDERED EARLY
# ============================================================

"""
Suppose a plot is designed at:

200 mm width


with:

10-point text


Then the document reduces it to:

90 mm width


Scale factor:

90 / 200
=
0.45


The apparent text size will also become approximately:

10 × 0.45
=
4.5 points


This can become unreadable.


Therefore:

Design near final size

rather than relying on large later scaling.
"""


# ============================================================
# 57. DOCUMENT-SCALING EXAMPLE
# ============================================================

original_width_mm = 180

final_width_mm = 90

original_font_size = 10


scaling_factor = (

    final_width_mm

    / original_width_mm

)


approximate_final_font_size = (

    original_font_size

    * scaling_factor

)


print(
    "\n--- Document Scaling Example ---"
)


print(
    "Scaling Factor:",
    scaling_factor
)


print(
    "Approximate Final Font Size:",
    approximate_final_font_size
)


# ============================================================
# 58. REUSABLE HIGH-RESOLUTION SAVE FUNCTION
# ============================================================

def save_high_resolution_figure(
    fig,
    output_folder,
    filename,
    raster_dpi=300,
    save_png=True,
    save_pdf=True,
    save_svg=True
):
    """
    Save a figure in high-resolution raster and vector
    formats.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to export.

    output_folder : str or Path
        Output directory.

    filename : str
        Base filename without extension.

    raster_dpi : int
        Resolution for PNG output.

    save_png : bool
        Save PNG.

    save_pdf : bool
        Save PDF.

    save_svg : bool
        Save SVG.

    Returns
    -------
    saved_files : list
        Paths of generated files.
    """

    output_folder = Path(
        output_folder
    )


    output_folder.mkdir(
        parents=True,
        exist_ok=True
    )


    if raster_dpi <= 0:

        raise ValueError(
            "Raster DPI must be greater than zero."
        )


    saved_files = []


    if save_png:

        png_file = (
            output_folder
            / f"{filename}.png"
        )


        fig.savefig(
            png_file,
            dpi=raster_dpi,
            bbox_inches="tight"
        )


        saved_files.append(
            png_file
        )


    if save_pdf:

        pdf_file = (
            output_folder
            / f"{filename}.pdf"
        )


        fig.savefig(
            pdf_file,
            bbox_inches="tight"
        )


        saved_files.append(
            pdf_file
        )


    if save_svg:

        svg_file = (
            output_folder
            / f"{filename}.svg"
        )


        fig.savefig(
            svg_file,
            bbox_inches="tight"
        )


        saved_files.append(
            svg_file
        )


    return saved_files


# ============================================================
# 59. USE HIGH-RESOLUTION SAVE FUNCTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(
        6,
        4
    )
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    markersize=5,
    linewidth=1.8,
    label="Efficiency"
)


ax.set_xlabel(
    "Load [%]",
    fontsize=10
)


ax.set_ylabel(
    "Efficiency [%]",
    fontsize=10
)


ax.tick_params(
    labelsize=9
)


ax.legend(
    fontsize=9
)


ax.grid(
    True
)


plt.tight_layout()


high_resolution_files = (
    save_high_resolution_figure(

        fig=fig,

        output_folder=output_folder,

        filename="high_resolution_example",

        raster_dpi=300

    )
)


print(
    "\n--- High-Resolution Exports ---"
)


for file_path in high_resolution_files:

    print(
        file_path
    )


plt.show()


# ============================================================
# 60. RASTERIZATION CONCEPT
# ============================================================

"""
A figure can contain a mixture of:

Vector elements

and

Raster elements.


For example:

Axes
Text
Line plots

may remain vector,


while a very dense scatter collection can be rasterized.


This can reduce PDF file size in certain cases.
"""


# ============================================================
# 61. RASTERIZED SCATTER EXAMPLE
# ============================================================

"""
The argument:

rasterized=True


can rasterize selected graphical artists inside formats
such as PDF.

This can be useful for extremely dense data.

It is not normally necessary for simple line plots.
"""


random_generator = np.random.default_rng(
    42
)


x_dense = random_generator.normal(
    size=10000
)


y_dense = random_generator.normal(
    size=10000
)


fig, ax = plt.subplots(
    figsize=(
        6,
        4
    )
)


ax.scatter(
    x_dense,
    y_dense,
    s=5,
    alpha=0.4,
    rasterized=True
)


ax.set_xlabel(
    "X [-]"
)

ax.set_ylabel(
    "Y [-]"
)

ax.set_title(
    "Rasterized Dense Scatter Example"
)


ax.grid(
    True
)


plt.tight_layout()


rasterized_pdf = (
    output_folder
    / "rasterized_scatter.pdf"
)


fig.savefig(
    rasterized_pdf,
    dpi=300,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 62. WHEN RASTERIZATION MAY HELP
# ============================================================

"""
Rasterization may be useful for:

- Hundreds of thousands of scatter points
- Dense contour data
- Complex collections
- Very large vector files


Keep:

Text

Axes

Labels

simple line plots


as vector when practical.


Do not rasterize everything without a reason.
"""


# ============================================================
# 63. RASTERIZATION DPI
# ============================================================

"""
When raster elements are embedded in an otherwise vector
output, DPI can still affect those rasterized components.

Therefore:

PDF
+
rasterized artist

may still require a suitable DPI setting.
"""


# ============================================================
# 64. HIGH-RESOLUTION IMAGE DOES NOT FIX BAD DATA
# ============================================================

"""
Consider two figures:

Figure A:

1200 DPI
but:
- No units
- Tiny font
- Poor legend
- Wrong axis
- Misleading scale


Figure B:

300 DPI
with:
- Correct labels
- Correct units
- Appropriate scale
- Readable text
- Clear result


Figure B is scientifically much better.
"""


# ============================================================
# 65. HIGH-RESOLUTION FIGURE PIPELINE
# ============================================================

"""
Raw Data
    ↓
Determine Final Figure Purpose
    ↓
Paper / Thesis / Presentation / Web
    ↓
Check Required Physical Size
    ↓
Set figsize
    ↓
Choose Fonts
    ↓
Choose Line Widths
    ↓
Choose Marker Sizes
    ↓
Create Plot
    ↓
Check Labels + Units
    ↓
Choose Raster or Vector
    ↓
If Raster:
Choose Appropriate DPI
    ↓
Export
    ↓
Open Final File
    ↓
Check at Final Display Size
"""


# ============================================================
# 66. SCREEN VS PAPER
# ============================================================

"""
A figure can look excellent when displayed full-screen on
a large monitor but become unreadable after being inserted
into a two-column paper.

Always evaluate the figure at approximately its FINAL
display size.
"""


# ============================================================
# 67. PRESENTATION FIGURES
# ============================================================

"""
Presentation figures may require:

- Larger fonts
- Larger markers
- Thicker lines
- Less detail
- Wider layout


because the audience may view the slide from a distance.


This differs from a compact journal figure.
"""


# ============================================================
# 68. THESIS FIGURES
# ============================================================

"""
Thesis figures often have more available page width than
single-column journal figures.

However:

Consistency is still important.

Use consistent:

- Figure widths
- Fonts
- Axis labels
- Units
- Line widths
- Legends
"""


# ============================================================
# 69. JOURNAL FIGURES
# ============================================================

"""
For a journal figure:

Check the official author instructions for:

- Figure width
- Maximum dimensions
- File formats
- Resolution
- Font requirements
- Line thickness
- Color requirements
- Grayscale requirements
- File-size limits


Do not assume one publisher's requirements apply to
another publisher.
"""


# ============================================================
# 70. DPI FOR DIFFERENT GRAPHIC TYPES
# ============================================================

"""
Different publishers may request different raster
resolutions for:

Photographs

Line art

Combination figures


Therefore:

300 DPI

and

600 DPI


should be treated as common examples, not universal rules.


Always verify the target publication requirements.
"""


# ============================================================
# 71. PNG VS PDF FOR LINE PLOTS
# ============================================================

"""
For a line plot:

PDF / SVG

may preserve scalable line and text information.


PNG:

uses pixels.


Therefore increasing PNG DPI may improve raster quality,
but vector output can often be preferable for scientific
line graphics when accepted by the publication workflow.
"""


# ============================================================
# 72. CHECK FILE EXISTS
# ============================================================

for file_path in high_resolution_files:

    if file_path.exists():

        print(
            "\nCreated:"
        )

        print(
            file_path
        )


# ============================================================
# 73. CHECK FILE SIZE FUNCTION
# ============================================================

def file_size_kb(
    file_path
):
    """
    Return file size in kilobytes.
    """

    file_path = Path(
        file_path
    )


    if not file_path.exists():

        raise FileNotFoundError(
            file_path
        )


    return (
        file_path
        .stat()
        .st_size
        / 1024
    )


# ============================================================
# 74. DISPLAY OUTPUT FILE SIZES
# ============================================================

print(
    "\n--- Export File Sizes ---"
)


for file_path in high_resolution_files:

    print(
        file_path.name,
        ":",
        f"{file_size_kb(file_path):.2f} kB"
    )


# ============================================================
# 75. HIGH DPI AND MEMORY
# ============================================================

"""
Extremely large raster figures require more:

Memory

Storage

Processing time


Example:

20 × 15 inch figure
at
1200 DPI


creates approximately:

24,000 × 18,000 pixels


That is:

432 million pixels


which is unnecessary for many ordinary engineering plots.
"""


# ============================================================
# 76. LARGE-IMAGE PIXEL COUNT EXAMPLE
# ============================================================

large_width = 20

large_height = 15

large_dpi = 1200


large_pixel_width = (
    large_width
    * large_dpi
)


large_pixel_height = (
    large_height
    * large_dpi
)


total_pixels = (

    large_pixel_width

    * large_pixel_height

)


print(
    "\n--- Excessively Large Example ---"
)


print(
    "Dimensions:"
)


print(
    large_pixel_width,
    "×",
    large_pixel_height
)


print(
    "Total Pixels:"
)


print(
    f"{total_pixels:,.0f}"
)


# ============================================================
# 77. COMMON MISTAKE - ONLY INCREASE DPI
# ============================================================

"""
Poor workflow:

Create tiny unreadable figure
        ↓
Set dpi=1200
        ↓
Assume figure is publication quality


High DPI does not correct:

- Tiny fonts
- Thin lines
- Bad labels
- Poor legends
- Misleading axes
- Incorrect data
"""


# ============================================================
# 78. COMMON MISTAKE - HUGE FIGURE THEN SHRINK
# ============================================================

"""
Creating:

figsize=(20, 15)


and later shrinking it dramatically in a document can make:

Fonts

Markers

Lines


appear much smaller than expected.


Prefer designing near the intended final dimensions.
"""


# ============================================================
# 79. COMMON MISTAKE - CONFUSING PIXELS WITH DPI
# ============================================================

"""
Pixels:

Image dimensions

Example:

1800 × 1200 pixels


DPI:

Pixel density relative to physical output size


They are related but not identical.
"""


# ============================================================
# 80. COMMON MISTAKE - IGNORING FINAL SIZE
# ============================================================

"""
A 300 DPI image can still appear poor if:

- It is enlarged far beyond its intended size
- Its original pixel dimensions are too small
- Labels become unreadable
- Compression damages the image


Always consider how the figure will finally be displayed.
"""


# ============================================================
# 81. COMMON MISTAKE - THINKING VECTOR NEEDS EXTREME DPI
# ============================================================

"""
Simple vector lines and text in PDF/SVG do not benefit
from extremely large DPI values in the same way that PNG
raster images do.

DPI becomes relevant when raster content is present.
"""


# ============================================================
# 82. COMMON MISTAKE - TOO SMALL FONT
# ============================================================

"""
A figure can have:

600 DPI


but still use:

4-point text


The raster resolution may be excellent while the figure
remains difficult to read.


High resolution and readability are different concepts.
"""


# ============================================================
# 83. COMMON MISTAKE - TOO THIN LINES
# ============================================================

"""
Very thin lines may become difficult to distinguish after
figure scaling or printing.

Choose line widths appropriate to:

- Figure size
- Number of curves
- Publication format
- Final display size
"""


# ============================================================
# 84. COMMON MISTAKE - TOO SMALL MARKERS
# ============================================================

"""
Markers that appear acceptable in an interactive Python
window may become almost invisible after a figure is
reduced for publication.

Check the exported figure at final size.
"""


# ============================================================
# 85. COMMON MISTAKE - VERY LARGE MARKERS
# ============================================================

"""
Increasing marker size too much can:

- Hide nearby points
- Cover error bars
- Make dense figures cluttered


High-resolution figures still require visual balance.
"""


# ============================================================
# 86. COMMON MISTAKE - ASSUME ALL JOURNALS WANT SAME DPI
# ============================================================

"""
There is no universal publication requirement such as:

"Every figure must be 600 DPI."


Requirements vary.

Always check the target publication.
"""


# ============================================================
# 87. COMMON MISTAKE - NOT OPENING FINAL FILE
# ============================================================

"""
Always inspect the exported file.

Check:

- Is text readable?
- Is anything clipped?
- Are lines visible?
- Are markers visible?
- Is the legend readable?
- Are special symbols correct?
- Does the figure look correct at final size?
"""


# ============================================================
# 88. HIGH-RESOLUTION DECISION WORKFLOW
# ============================================================

"""
Where Will Figure Be Used?
           ↓
Paper / Thesis / Slides / Web
           ↓
What Final Width?
           ↓
Set Physical Figure Size
           ↓
Choose Font Size
           ↓
Choose Line Width
           ↓
Choose Marker Size
           ↓
Raster or Vector?
       /          \
   Raster         Vector
      ↓             ↓
Choose DPI       PDF / SVG
      ↓             ↓
Export          Export
       \          /
        ↓        ↓
       Verify Final Figure
"""


# ============================================================
# 89. PRACTICAL ENGINEERING EXAMPLE
# ============================================================

"""
Suppose an FFT figure is required for a paper.

Data:

10 kHz to 30 MHz

Magnitude:

dBµV


Recommended workflow:

Load FFT data
      ↓
Create figure near final width
      ↓
Use logarithmic frequency axis
      ↓
Use readable fonts
      ↓
Use visible line widths
      ↓
Add legend
      ↓
Export PDF
      ↓
Export 300/600 DPI PNG if required
      ↓
Inspect final paper-sized figure
"""


# ============================================================
# 90. COMPLETE HIGH-RESOLUTION WORKFLOW
# ============================================================

"""
Scientific Data
      ↓
Determine Final Application
      ↓
Determine Figure Dimensions
      ↓
Create Figure at Similar Size
      ↓
Set Fonts
      ↓
Set Lines
      ↓
Set Markers
      ↓
Check Labels / Units
      ↓
Choose File Format
      ↓
Choose Raster DPI if Required
      ↓
Export
      ↓
Inspect
      ↓
Insert into Document
      ↓
Inspect Again at Final Size
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
HIGH-RESOLUTION FIGURES


1. FIGURE SIZE

fig, ax = plt.subplots(

    figsize=(
        6,
        4
    )

)


Units:

inches


------------------------------------------------------------


2. PNG RESOLUTION

fig.savefig(

    "figure.png",

    dpi=300

)


------------------------------------------------------------


3. HIGHER RASTER RESOLUTION

fig.savefig(

    "figure.png",

    dpi=600

)


Use only when needed.


------------------------------------------------------------


4. PIXEL DIMENSIONS

Approximate:

Width Pixels
=
Width Inches × DPI


Height Pixels
=
Height Inches × DPI


------------------------------------------------------------


5. EXAMPLE

6 × 4 inches

at

300 DPI


approximately:

1800 × 1200 pixels


------------------------------------------------------------


6. 600 DPI

6 × 4 inches

at

600 DPI


approximately:

3600 × 2400 pixels


------------------------------------------------------------


7. PHYSICAL SIZE

Figure size and DPI are different concepts.


Figure size:

Physical dimensions


DPI:

Raster sampling density


------------------------------------------------------------


8. MM TO INCHES

inches = mm / 25.4


Example:

88 mm

≈

3.46 inches


------------------------------------------------------------


9. CM TO INCHES

inches = cm / 2.54


------------------------------------------------------------


10. DESIGN NEAR FINAL SIZE

Avoid:

Huge Figure
     ↓
Shrink Dramatically in Paper


Prefer:

Create Figure
     ↓
Approximately Final Width
     ↓
Export


------------------------------------------------------------


11. FONT SIZE

DPI does NOT control font size.


Use:

fontsize=

and:

tick_params(
    labelsize=
)


------------------------------------------------------------


12. LINE WIDTH

Use:

linewidth=


High DPI does not automatically make thin lines readable.


------------------------------------------------------------


13. MARKER SIZE

Use:

markersize=


Check markers at final document size.


------------------------------------------------------------


14. PNG

Raster format.

DPI is important.


------------------------------------------------------------


15. PDF

Useful vector-oriented format for scientific line plots.


------------------------------------------------------------


16. SVG

Useful scalable vector-oriented format.


------------------------------------------------------------


17. VECTOR DOES NOT GUARANTEE EVERYTHING IS VECTOR

Figures may contain raster:

Images

Heatmaps

Rasterized collections


------------------------------------------------------------


18. RASTERIZATION

For extremely dense artists:

rasterized=True


can reduce complexity of some vector outputs.


------------------------------------------------------------


19. COMMON DPI EXAMPLES

72
150
300
600


These are examples.

Follow the target publication requirements.


------------------------------------------------------------


20. FILE SIZE

Higher DPI often increases raster file size.

Bigger file
does NOT automatically mean
better figure.


------------------------------------------------------------


21. FINAL SIZE MATTERS

Always inspect the figure at approximately the dimensions
at which the reader will see it.


------------------------------------------------------------


22. SCREEN QUALITY != PAPER QUALITY

A figure that looks excellent full-screen may become
unreadable in a narrow journal column.


------------------------------------------------------------


23. MOST IMPORTANT PRINCIPLE

High resolution means more than DPI.

A strong scientific figure requires:

Correct Data

+
Appropriate Figure Size

+
Readable Fonts

+
Visible Lines

+
Visible Markers

+
Correct Units

+
Appropriate Resolution

+
Suitable File Format


------------------------------------------------------------


24. RECOMMENDED EXPORT WORKFLOW

Create Figure
      ↓
Use Final-Sized Dimensions
      ↓
Check Fonts
      ↓
Check Lines
      ↓
Check Markers
      ↓
Check Labels
      ↓
Save PNG if Raster Needed
      ↓
Save PDF / SVG if Vector Appropriate
      ↓
Inspect Export
      ↓
Inspect Again After Document Insertion


------------------------------------------------------------


NEXT:

20_publication_quality_plot.py


The next file will combine everything from the previous
visualization tutorials into one complete research figure:

Figure dimensions

Font hierarchy

Line widths

Markers

Axis limits

Major/minor ticks

Log frequency axis

Engineering units

Legend placement

Annotations

Grid control

Single-column / double-column layouts

PNG / PDF / SVG export

Consistent formatting

Reusable publication plotting function

and a complete engineering publication example.
"""
