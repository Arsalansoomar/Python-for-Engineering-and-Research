"""
============================================================
Python for Engineering and Research
18 - Save Figures as PNG, PDF, and SVG
============================================================

Purpose:
    Demonstrate how Matplotlib figures can be exported in
    common scientific and engineering formats including
    PNG, PDF, and SVG.

Topics:
    1. Why save figures?
    2. Raster vs vector graphics
    3. PNG format
    4. PDF format
    5. SVG format
    6. savefig()
    7. Figure size
    8. DPI and resolution
    9. bbox_inches="tight"
    10. Transparent backgrounds
    11. Creating output folders
    12. Reliable file paths
    13. Saving one figure in several formats
    14. Automatic filename generation
    15. Saving figures created in loops
    16. Frequency-domain engineering example
    17. Reusable export function
    18. File-size considerations
    19. Publication recommendations
    20. Common mistakes
    21. Key takeaways

Author:
    Arsalan Muhammad Soomar
============================================================
"""


# ============================================================
# 1. WHY SAVE FIGURES?
# ============================================================

"""
During research, figures are rarely created only for
interactive viewing.

They may be required for:

- Journal papers
- Conference papers
- Thesis chapters
- Technical reports
- Presentations
- Posters
- Websites
- GitHub documentation
- Research data archives


Instead of taking a screenshot of a Matplotlib window,
save the figure directly using:

fig.savefig()


This preserves much better quality.
"""


# ============================================================
# 2. REQUIRED IMPORTS
# ============================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pathlib import Path


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
# 4. CREATE OUTPUT FOLDER
# ============================================================

"""
It is good practice to keep generated figures in a
dedicated folder.

Example repository structure:

02_Data_Visualization/
│
├── 18_save_png_pdf_svg.py
│
└── output_figures/
    ├── efficiency_plot.png
    ├── efficiency_plot.pdf
    └── efficiency_plot.svg
"""


script_folder = Path(
    __file__
).resolve().parent


output_folder = (
    script_folder
    / "output_figures"
)


output_folder.mkdir(
    exist_ok=True
)


print(
    "\nOutput folder:"
)

print(
    output_folder
)


# ============================================================
# 5. CREATE BASIC FIGURE
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
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
    "Converter Efficiency vs Load"
)


ax.grid(
    True
)


plt.tight_layout()


# ============================================================
# 6. SAVE PNG
# ============================================================

"""
PNG:

Portable Network Graphics


PNG is a RASTER format.

A raster image is made from pixels.


Useful for:

- Presentations
- Websites
- GitHub README files
- Reports
- Quick sharing
- Screens
"""


png_file = (
    output_folder
    / "efficiency_plot.png"
)


fig.savefig(
    png_file
)


print(
    "\nPNG saved:"
)

print(
    png_file
)


# ============================================================
# 7. SAVE PNG WITH DPI
# ============================================================

"""
For raster formats such as PNG, resolution matters.

Use:

dpi=300


A commonly used high-quality export setting is:

300 DPI
"""


png_300_file = (
    output_folder
    / "efficiency_plot_300dpi.png"
)


fig.savefig(
    png_300_file,
    dpi=300
)


print(
    "\n300 DPI PNG saved:"
)

print(
    png_300_file
)


# ============================================================
# 8. SAVE PDF
# ============================================================

"""
PDF:

Portable Document Format


For Matplotlib line plots, text, markers, and axes,
PDF generally preserves vector information.

Vector graphics can be scaled without the same pixelation
seen in ordinary raster images.


Useful for:

- Journal papers
- Conference papers
- Thesis
- Technical reports
- LaTeX documents
"""


pdf_file = (
    output_folder
    / "efficiency_plot.pdf"
)


fig.savefig(
    pdf_file
)


print(
    "\nPDF saved:"
)

print(
    pdf_file
)


# ============================================================
# 9. SAVE SVG
# ============================================================

"""
SVG:

Scalable Vector Graphics


SVG is a vector-oriented graphics format.

Useful for:

- Websites
- GitHub
- Vector editing workflows
- Diagrams
- Further graphical modification
"""


svg_file = (
    output_folder
    / "efficiency_plot.svg"
)


fig.savefig(
    svg_file
)


print(
    "\nSVG saved:"
)

print(
    svg_file
)


# ============================================================
# 10. DISPLAY FIGURE AFTER SAVING
# ============================================================

"""
Recommended workflow:

Create Figure
      ↓
Format Figure
      ↓
Save Figure
      ↓
plt.show()


Save BEFORE showing whenever possible.
"""


plt.show()


# ============================================================
# 11. PNG VS PDF VS SVG
# ============================================================

"""
PNG
------------------------------------------------------------

Type:

Raster


Made from:

Pixels


Advantages:

- Widely supported
- Good for slides
- Good for websites
- Easy to preview
- Easy to share


Disadvantage:

Can become pixelated when enlarged significantly.


------------------------------------------------------------


PDF
------------------------------------------------------------

Type:

Typically vector for Matplotlib lines/text


Advantages:

- Excellent for scientific papers
- Scales well
- Good for thesis documents
- Good for printing


------------------------------------------------------------


SVG
------------------------------------------------------------

Type:

Vector


Advantages:

- Scalable
- Good for web
- Can often be edited in vector graphics software
- Useful for diagrams and line plots


------------------------------------------------------------


Typical recommendation:

Presentation / GitHub
        ↓
PNG


Paper / Thesis
        ↓
PDF


Vector editing / Web
        ↓
SVG
"""


# ============================================================
# 12. bbox_inches="tight"
# ============================================================

"""
Sometimes labels, legends, or annotations extend beyond
the default figure boundary.

Use:

bbox_inches="tight"


This tells Matplotlib to calculate a tighter bounding box
around the complete figure.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency,
    marker="o",
    label="Efficiency"
)


ax.set_xlabel(
    "Load [%]"
)

ax.set_ylabel(
    "Efficiency [%]"
)


ax.legend(
    loc="center left",
    bbox_to_anchor=(
        1.02,
        0.5
    )
)


ax.grid(
    True
)


plt.tight_layout()


tight_file = (
    output_folder
    / "tight_bounding_box.png"
)


fig.savefig(
    tight_file,
    dpi=300,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 13. WHY bbox_inches="tight" IS USEFUL
# ============================================================

"""
Without:

bbox_inches="tight"


elements such as:

- Outside legends
- Long axis labels
- Annotations
- Text boxes

may sometimes be clipped or leave inconvenient margins.


A common export command is therefore:

fig.savefig(
    "figure.png",
    dpi=300,
    bbox_inches="tight"
)
"""


# ============================================================
# 14. TRANSPARENT BACKGROUND
# ============================================================

"""
Use:

transparent=True


when a transparent background is required.

This can be useful for:

- Presentation overlays
- Some websites
- Graphic design workflows
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency,
    marker="o"
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


transparent_file = (
    output_folder
    / "efficiency_transparent.png"
)


fig.savefig(
    transparent_file,
    dpi=300,
    transparent=True,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 15. TRANSPARENT BACKGROUND WARNING
# ============================================================

"""
Transparent backgrounds are not always desirable.

For journal papers and technical reports, a normal solid
background is usually easier to manage.

Transparency can create unexpected appearance when the
figure is placed over:

Dark slides

Colored backgrounds

Different document themes


Use it intentionally.
"""


# ============================================================
# 16. FIGURE SIZE
# ============================================================

"""
Figure size is defined using:

figsize=(
    width,
    height
)


Matplotlib uses INCHES.


Example:

figsize=(7, 4.5)


means:

7 inches wide

4.5 inches high
"""


fig, ax = plt.subplots(
    figsize=(6, 4)
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


ax.grid(
    True
)


size_example_file = (
    output_folder
    / "figure_size_example.png"
)


fig.savefig(
    size_example_file,
    dpi=300,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 17. FIGURE SIZE AND PIXEL DIMENSIONS
# ============================================================

"""
For a PNG image:

Pixel Width

approximately equals:

Figure Width [inch] × DPI


Pixel Height

approximately equals:

Figure Height [inch] × DPI


Example:

figsize=(6, 4)

dpi=300


approximately gives:

Width:

6 × 300 = 1800 pixels


Height:

4 × 300 = 1200 pixels


before any adjustment caused by tight bounding boxes.
"""


figure_width = 6

figure_height = 4

dpi_value = 300


pixel_width = (
    figure_width
    * dpi_value
)


pixel_height = (
    figure_height
    * dpi_value
)


print(
    "\n--- Approximate Raster Dimensions ---"
)


print(
    "Width:",
    pixel_width,
    "pixels"
)


print(
    "Height:",
    pixel_height,
    "pixels"
)


# ============================================================
# 18. DPI
# ============================================================

"""
DPI means:

Dots Per Inch


In raster figure export, higher DPI generally means more
pixels for the same physical figure size.


Common examples:

72-100 DPI

    Screen preview


150 DPI

    Moderate-resolution graphics


300 DPI

    Common high-quality figure export


600 DPI

    Higher-resolution raster export when required


Always check the requirements of the journal, conference,
thesis template, or publisher.
"""


# ============================================================
# 19. 300 DPI EXAMPLE
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
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


file_300_dpi = (
    output_folder
    / "figure_300dpi.png"
)


fig.savefig(
    file_300_dpi,
    dpi=300,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 20. 600 DPI EXAMPLE
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
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


file_600_dpi = (
    output_folder
    / "figure_600dpi.png"
)


fig.savefig(
    file_600_dpi,
    dpi=600,
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 21. IMPORTANT: DPI AND VECTOR FILES
# ============================================================

"""
DPI is particularly important for raster formats such as:

PNG


For vector elements in formats such as:

PDF

SVG


the lines and text can generally scale without ordinary
pixelation.


However, if a figure contains rasterized content such as:

Images

Heatmaps

Photographs

Rasterized artists


resolution may still matter inside a PDF or SVG workflow.


Therefore:

Vector file

does not necessarily mean that every embedded element is
vector.
"""


# ============================================================
# 22. SAVE MULTIPLE FORMATS
# ============================================================

"""
A research figure can be saved in several formats from
the SAME Matplotlib figure.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
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


base_filename = (
    output_folder
    / "converter_efficiency"
)


fig.savefig(
    base_filename.with_suffix(
        ".png"
    ),
    dpi=300,
    bbox_inches="tight"
)


fig.savefig(
    base_filename.with_suffix(
        ".pdf"
    ),
    bbox_inches="tight"
)


fig.savefig(
    base_filename.with_suffix(
        ".svg"
    ),
    bbox_inches="tight"
)


plt.show()


# ============================================================
# 23. AUTOMATIC FORMAT LOOP
# ============================================================

"""
Instead of writing three separate savefig() commands,
we can use a loop.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
)


ax.plot(
    load_percent,
    efficiency,
    marker="o"
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


formats = [
    "png",
    "pdf",
    "svg"
]


for file_format in formats:

    output_file = (

        output_folder
        / f"automatic_export.{file_format}"

    )


    if file_format == "png":

        fig.savefig(
            output_file,
            dpi=300,
            bbox_inches="tight"
        )

    else:

        fig.savefig(
            output_file,
            bbox_inches="tight"
        )


    print(
        "Saved:",
        output_file
    )


plt.show()


# ============================================================
# 24. REUSABLE SAVE FUNCTION
# ============================================================

def save_figure(
    fig,
    output_folder,
    filename,
    dpi=300,
    formats=None,
    transparent=False
):
    """
    Save a Matplotlib figure in multiple formats.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to save.

    output_folder : str or Path
        Destination folder.

    filename : str
        Base filename without extension.

    dpi : int
        Raster resolution used primarily for PNG.

    formats : list of str, optional
        Output formats.

        Example:
        ["png", "pdf", "svg"]

    transparent : bool
        Whether to use a transparent background.

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


    if formats is None:

        formats = [
            "png",
            "pdf",
            "svg"
        ]


    supported_formats = {

        "png",
        "pdf",
        "svg"

    }


    saved_files = []


    for file_format in formats:

        file_format = (
            file_format
            .lower()
            .replace(
                ".",
                ""
            )
        )


        if file_format not in supported_formats:

            raise ValueError(
                f"Unsupported format: "
                f"{file_format}"
            )


        output_file = (

            output_folder

            / f"{filename}.{file_format}"

        )


        save_options = {

            "bbox_inches":
                "tight",

            "transparent":
                transparent

        }


        if file_format == "png":

            save_options[
                "dpi"
            ] = dpi


        fig.savefig(
            output_file,
            **save_options
        )


        saved_files.append(
            output_file
        )


    return saved_files


# ============================================================
# 25. USE REUSABLE SAVE FUNCTION
# ============================================================

fig, ax = plt.subplots(
    figsize=(7, 4.5)
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


saved_files = save_figure(

    fig=fig,

    output_folder=output_folder,

    filename="reusable_export_example",

    dpi=300,

    formats=[
        "png",
        "pdf",
        "svg"
    ]

)


print(
    "\n--- Reusable Export Function ---"
)


for file in saved_files:

    print(
        file
    )


plt.show()


# ============================================================
# 26. SAVE ONLY PNG AND PDF
# ============================================================

"""
The reusable function can save only selected formats.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
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


plt.tight_layout()


save_figure(

    fig=fig,

    output_folder=output_folder,

    filename="png_and_pdf_only",

    formats=[
        "png",
        "pdf"
    ]

)


plt.show()


# ============================================================
# 27. AUTOMATIC FILENAMES
# ============================================================

"""
Avoid filenames such as:

figure1.png

newfigure.png

final.png

final2.png

final_final.png


Prefer descriptive filenames:

converter_efficiency.png

voltage_transient.pdf

fft_comparison.svg

temperature_vs_load.png


Descriptive filenames make research projects easier to
manage.
"""


case_name = "Design_A"

measurement_name = "Efficiency"


automatic_name = (

    f"{case_name}_"
    f"{measurement_name}"

)


print(
    "\nAutomatic Filename:"
)


print(
    automatic_name
)


# ============================================================
# 28. CLEAN FILENAMES
# ============================================================

"""
If labels contain spaces, filenames can be cleaned.
"""


plot_title = (
    "Converter Efficiency Comparison"
)


clean_filename = (

    plot_title

    .lower()

    .replace(
        " ",
        "_"
    )

)


print(
    "\nClean Filename:"
)


print(
    clean_filename
)


# ============================================================
# 29. SAVE FIGURES GENERATED IN A LOOP
# ============================================================

"""
A common research workflow produces many figures
automatically.

Example:

Voltage

Current

Power

Temperature


Each variable can be plotted and saved automatically.
"""


time = np.linspace(
    0,
    0.02,
    100
)


signals = {

    "Voltage_V":
        48
        + 2
        * np.sin(
            2
            * np.pi
            * 100
            * time
        ),

    "Current_A":
        2
        + 0.2
        * np.sin(
            2
            * np.pi
            * 100
            * time
        ),

    "Power_W":
        96
        + 8
        * np.sin(
            2
            * np.pi
            * 100
            * time
        )

}


axis_labels = {

    "Voltage_V":
        "Voltage [V]",

    "Current_A":
        "Current [A]",

    "Power_W":
        "Power [W]"

}


for variable_name, values in signals.items():

    fig, ax = plt.subplots(
        figsize=(7, 4.5)
    )


    ax.plot(
        time,
        values,
        linewidth=2
    )


    ax.set_xlabel(
        "Time [s]"
    )


    ax.set_ylabel(
        axis_labels[
            variable_name
        ]
    )


    ax.set_title(
        variable_name.replace(
            "_",
            " "
        )
    )


    ax.grid(
        True
    )


    plt.tight_layout()


    save_figure(

        fig=fig,

        output_folder=output_folder,

        filename=variable_name.lower(),

        dpi=300,

        formats=[
            "png",
            "pdf"
        ]

    )


    # Close figure when generating many figures automatically.

    plt.close(
        fig
    )


# ============================================================
# 30. WHY plt.close(fig) MATTERS
# ============================================================

"""
If hundreds of figures are generated inside a loop,
keeping every figure open can consume unnecessary memory.

Use:

plt.close(
    fig
)


after saving a figure that no longer needs to remain open.


This is especially useful for:

- Batch processing
- Automated experiments
- Parameter sweeps
- Large datasets
"""


# ============================================================
# 31. SAVE FROM CSV DATA
# ============================================================

"""
Now demonstrate a practical file-based workflow.
"""


csv_file = (
    script_folder
    / "sample_data"
    / "fft_example.csv"
)


if not csv_file.exists():

    raise FileNotFoundError(
        f"\nSample FFT file not found:\n"
        f"{csv_file}"
    )


fft_data = pd.read_csv(
    csv_file
)


print(
    "\n--- FFT Columns ---"
)


print(
    fft_data.columns.tolist()
)


# ============================================================
# 32. FREQUENCY-DOMAIN FIGURE
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
    figsize=(8, 4.8)
)


for case_name, column_name in frequency_cases.items():

    ax.plot(

        fft_data[
            "Frequency_Hz"
        ],

        fft_data[
            column_name
        ],

        linewidth=2,

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
    "Frequency [Hz]"
)

ax.set_ylabel(
    "Magnitude [dBµV]"
)


ax.set_title(
    "Frequency-Domain Case Comparison"
)


ax.grid(
    True,
    which="both"
)


ax.legend(
    ncol=2
)


plt.tight_layout()


# ============================================================
# 33. EXPORT FREQUENCY FIGURE
# ============================================================

frequency_files = save_figure(

    fig=fig,

    output_folder=output_folder,

    filename="frequency_domain_comparison",

    dpi=300,

    formats=[
        "png",
        "pdf",
        "svg"
    ]

)


print(
    "\n--- Frequency-Domain Exports ---"
)


for file in frequency_files:

    print(
        file
    )


plt.show()


# ============================================================
# 34. SAVE WITH METADATA - PDF EXAMPLE
# ============================================================

"""
Some output formats can store metadata.

For example, PDF metadata may include:

Title

Author

Subject

Keywords


Support may vary between backends and formats.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
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


plt.tight_layout()


metadata = {

    "Title":
        "Converter Efficiency",

    "Author":
        "Arsalan Muhammad Soomar",

    "Subject":
        "Engineering Data Visualization",

    "Keywords":
        "Python, Matplotlib, Engineering"

}


metadata_pdf = (
    output_folder
    / "figure_with_metadata.pdf"
)


fig.savefig(
    metadata_pdf,
    bbox_inches="tight",
    metadata=metadata
)


plt.show()


# ============================================================
# 35. FILE EXTENSION DETERMINES FORMAT
# ============================================================

"""
Matplotlib commonly determines the output format from the
filename extension.

Example:

figure.png
        ↓
PNG


figure.pdf
        ↓
PDF


figure.svg
        ↓
SVG


Therefore:

fig.savefig(
    "figure.pdf"
)

creates a PDF file.
"""


# ============================================================
# 36. EXPLICIT format=
# ============================================================

"""
The format can also be specified explicitly:

fig.savefig(
    "figure_output",
    format="pdf"
)


However, including the correct extension in the filename
is often simpler and clearer.
"""


# ============================================================
# 37. PAD AROUND TIGHT BOUNDING BOX
# ============================================================

"""
When using:

bbox_inches="tight"


additional padding can be controlled using:

pad_inches=
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
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


padding_file = (
    output_folder
    / "figure_with_padding.png"
)


fig.savefig(
    padding_file,
    dpi=300,
    bbox_inches="tight",
    pad_inches=0.1
)


plt.show()


# ============================================================
# 38. SAVE WITH SPECIFIED BACKGROUND
# ============================================================

"""
A background can be controlled using:

facecolor=


Usually the default background is suitable.

This option is useful when a specific export background is
required.
"""


fig, ax = plt.subplots(
    figsize=(7, 4.5)
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


background_file = (
    output_folder
    / "figure_background.png"
)


fig.savefig(
    background_file,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)


plt.show()


# ============================================================
# 39. CHECK GENERATED FILE
# ============================================================

"""
Path.exists() can verify that an output file was created.
"""


check_file = (
    output_folder
    / "efficiency_plot.pdf"
)


if check_file.exists():

    print(
        "\nFile created successfully:"
    )

    print(
        check_file
    )

else:

    print(
        "\nFile was not created."
    )


# ============================================================
# 40. CHECK FILE SIZE
# ============================================================

"""
File size can also be inspected.

Path.stat().st_size

returns the number of bytes.
"""


if check_file.exists():

    size_bytes = (
        check_file
        .stat()
        .st_size
    )


    size_kb = (
        size_bytes
        / 1024
    )


    print(
        f"\nFile Size = "
        f"{size_kb:.2f} kB"
    )


# ============================================================
# 41. PNG FILE SIZE VS DPI
# ============================================================

"""
Increasing raster resolution may significantly increase
file size.

For example:

300 DPI PNG
      ↓
Smaller


600 DPI PNG
      ↓
More pixels
      ↓
Potentially larger file


Do not automatically choose extremely high DPI.

Follow the actual publication or application requirement.
"""


# ============================================================
# 42. VECTOR FILE SIZE
# ============================================================

"""
Vector figures often work extremely well for:

Lines

Markers

Text

Axes

Simple diagrams


However, very complex figures containing:

Thousands of markers

Dense scatter plots

Very large paths


can produce large PDF or SVG files.


In such cases, a carefully chosen raster or partially
rasterized workflow may be more practical.
"""


# ============================================================
# 43. SCREENSHOT VS savefig()
# ============================================================

"""
Avoid using screenshots for scientific figures.

Screenshot:

Display
   ↓
Screen resolution
   ↓
Captured pixels


Matplotlib:

Original figure
   ↓
savefig()
   ↓
Controlled resolution / vector export


Prefer:

fig.savefig()
"""


# ============================================================
# 44. SAVE BEFORE plt.show()
# ============================================================

"""
A reliable workflow is:

fig, ax = plt.subplots()

ax.plot(...)

ax.set_xlabel(...)

ax.set_ylabel(...)

plt.tight_layout()

fig.savefig(...)

plt.show()


This keeps figure creation, export, and display in a clear
order.
"""


# ============================================================
# 45. SAVE BEFORE plt.close()
# ============================================================

"""
If using:

plt.close(fig)


make sure the file has already been saved.

Correct:

fig.savefig(...)

plt.close(fig)


Do not close a figure before its required exports have
been created.
"""


# ============================================================
# 46. SAVE ALL FORMATS FROM SAME FIGURE
# ============================================================

"""
For research reproducibility:

Create the figure ONCE.

Then export:

PNG
PDF
SVG


from the same figure object.


This ensures the three files contain the same:

Data

Axis limits

Labels

Legend

Annotations

Formatting
"""


# ============================================================
# 47. USE CONSISTENT BASENAME
# ============================================================

"""
Good:

emi_comparison.png

emi_comparison.pdf

emi_comparison.svg


Less organized:

figure23.png

latest.pdf

new.svg


A consistent base filename simplifies version management.
"""


# ============================================================
# 48. VERSIONED FILENAMES
# ============================================================

"""
During research development, explicit version names can
sometimes help.

Example:

fft_comparison_v01.pdf

fft_comparison_v02.pdf


However, formal version control systems such as Git are
generally preferable to creating endless filenames such as:

final

final_new

final_final

final_final2
"""


# ============================================================
# 49. PUBLICATION EXPORT WORKFLOW
# ============================================================

"""
Research Figure
      ↓
Choose Final Figure Size
      ↓
Set Fonts / Labels
      ↓
Set Axis Limits
      ↓
Check Legend
      ↓
Check Annotations
      ↓
tight_layout()
      ↓
Save PDF
      ↓
Save PNG Preview
      ↓
Optional SVG
      ↓
Open Exported File
      ↓
Verify:
- Labels
- Units
- Font size
- Line visibility
- Cropping
- Resolution
"""


# ============================================================
# 50. COMMON MISTAKE - SCREENSHOT
# ============================================================

"""
Do not create publication figures by:

1. Running Python
2. Opening the plot
3. Taking a screenshot
4. Cropping manually


Instead:

fig.savefig(...)
"""


# ============================================================
# 51. COMMON MISTAKE - LOW-RESOLUTION PNG
# ============================================================

"""
A low-resolution PNG may look acceptable on the computer
screen but become pixelated when:

- Enlarged
- Printed
- Inserted into a paper
- Exported into another document


For final raster figures, use a resolution appropriate to
the target publication or document.
"""


# ============================================================
# 52. COMMON MISTAKE - ASSUMING 600 DPI IS ALWAYS BETTER
# ============================================================

"""
Higher DPI means more raster pixels.

It does NOT automatically make:

- Poor labels clearer
- Thin lines better designed
- Bad axis choices correct
- A confusing figure more scientific


Use sufficient resolution rather than unnecessary
resolution.
"""


# ============================================================
# 53. COMMON MISTAKE - DPI AS A SUBSTITUTE FOR FIGURE SIZE
# ============================================================

"""
Figure size and DPI are different concepts.

Figure size:

Physical dimensions


DPI:

Raster sampling density


Example:

figsize=(6, 4)

dpi=300


is not conceptually the same as simply increasing DPI
while ignoring the intended final figure dimensions.
"""


# ============================================================
# 54. COMMON MISTAKE - CLIPPED LABELS
# ============================================================

"""
If:

Axis labels

Legend

Annotations

are clipped, consider:

plt.tight_layout()

and:

bbox_inches="tight"
"""


# ============================================================
# 55. COMMON MISTAKE - SAVING AFTER CLOSE
# ============================================================

"""
Incorrect workflow:

plt.close(fig)

fig.savefig(...)


Correct:

fig.savefig(...)

plt.close(fig)
"""


# ============================================================
# 56. COMMON MISTAKE - OVERWRITING IMPORTANT FILES
# ============================================================

"""
Saving repeatedly to:

results.pdf


will normally replace the previous file.

This may be intended during development.

If previous versions must be retained, use:

- Version control
- Versioned filenames
- Separate output directories
"""


# ============================================================
# 57. COMMON MISTAKE - FILE PATH CONFUSION
# ============================================================

"""
Avoid relying entirely on the current working directory.

Example:

fig.savefig(
    "plot.png"
)


The file may be saved somewhere unexpected depending on
how the script is executed.


Using:

Path(__file__).resolve().parent

makes the output location more predictable.
"""


# ============================================================
# 58. COMMON MISTAKE - ASSUMING PDF IS ALWAYS 100% VECTOR
# ============================================================

"""
Matplotlib line objects and text can be represented as
vector content in PDF.

However, figures may also contain raster elements such as:

Images

Rasterized collections

Certain complex artists


Therefore:

"PDF"

does not automatically guarantee every element inside
the file is vector.
"""


# ============================================================
# 59. COMMON MISTAKE - VERY LARGE SVG FILE
# ============================================================

"""
A scatter plot containing hundreds of thousands of points
can produce a very large SVG because each point may be
stored as graphical information.

Vector is excellent for many line plots.

It is not automatically the best format for every type of
dataset.
"""


# ============================================================
# 60. COMMON MISTAKE - NOT CHECKING EXPORTED FILE
# ============================================================

"""
After saving:

OPEN THE EXPORTED FIGURE.


Check:

- Is anything clipped?
- Are fonts readable?
- Is the legend visible?
- Are line styles distinguishable?
- Are symbols displayed correctly?
- Does the PDF look correct?
- Is the PNG sharp enough?


Successful Python execution does not automatically mean
the final figure is publication-ready.
"""


# ============================================================
# 61. FORMAT SELECTION GUIDE
# ============================================================

"""
Need a figure for a presentation?
        ↓
PNG


Need a line figure for paper/thesis?
        ↓
PDF is often useful


Need scalable web/vector editing?
        ↓
SVG


Need all three for flexibility?
        ↓
Export:

PNG + PDF + SVG
"""


# ============================================================
# 62. ENGINEERING EXPORT EXAMPLES
# ============================================================

"""
TIME-DOMAIN WAVEFORM

Possible exports:

voltage_transient.png
voltage_transient.pdf


------------------------------------------------------------


FFT / EMI SPECTRUM

Possible exports:

fft_comparison.png
fft_comparison.pdf
fft_comparison.svg


------------------------------------------------------------


BAR CHART

Possible exports:

power_loss_comparison.png
power_loss_comparison.pdf


------------------------------------------------------------


PUBLICATION FIGURE

Common workflow:

PDF
    Main vector figure

PNG
    Preview / presentation / submission where raster is needed

SVG
    Optional editing or web version
"""


# ============================================================
# 63. COMPLETE EXPORT PIPELINE
# ============================================================

"""
Raw Data
    ↓
Create Figure
    ↓
Choose Figure Size
    ↓
Plot Data
    ↓
Axis Labels + Units
    ↓
Legend
    ↓
Axis Limits
    ↓
Annotations
    ↓
Layout Adjustment
    ↓
Choose Output Format
    ↓
Choose DPI if Raster
    ↓
savefig()
    ↓
Verify Exported File
    ↓
Paper / Thesis / Presentation / Web
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
SAVE PNG, PDF, AND SVG


1. SAVE BASIC FIGURE

fig.savefig(
    "figure.png"
)


------------------------------------------------------------


2. SAVE HIGH-RESOLUTION PNG

fig.savefig(

    "figure.png",

    dpi=300

)


------------------------------------------------------------


3. SAVE PDF

fig.savefig(
    "figure.pdf"
)


------------------------------------------------------------


4. SAVE SVG

fig.savefig(
    "figure.svg"
)


------------------------------------------------------------


5. TIGHT BOUNDING BOX

fig.savefig(

    "figure.png",

    dpi=300,

    bbox_inches="tight"

)


------------------------------------------------------------


6. TRANSPARENT BACKGROUND

fig.savefig(

    "figure.png",

    transparent=True

)


------------------------------------------------------------


7. FIGURE SIZE

fig, ax = plt.subplots(

    figsize=(
        7,
        4.5
    )

)


Units:

inches


------------------------------------------------------------


8. APPROXIMATE PNG PIXEL SIZE

Pixels ≈ Inches × DPI


Example:

6 inches × 300 DPI

≈ 1800 pixels


------------------------------------------------------------


9. PNG

Type:

Raster


Best suited for:

Slides

Web

GitHub

Raster-based submission requirements


------------------------------------------------------------


10. PDF

Typically excellent for:

Scientific papers

Thesis

Reports

Vector line graphics


------------------------------------------------------------


11. SVG

Useful for:

Scalable web graphics

Vector editing

Diagrams


------------------------------------------------------------


12. SAVE ALL FORMATS

for file_format in [

    "png",
    "pdf",
    "svg"

]:

    fig.savefig(
        f"figure.{file_format}"
    )


------------------------------------------------------------


13. RELIABLE OUTPUT FOLDER

script_folder = Path(
    __file__
).resolve().parent


output_folder = (

    script_folder

    / "output_figures"

)


output_folder.mkdir(
    exist_ok=True
)


------------------------------------------------------------


14. SAVE BEFORE SHOW

Recommended:

Create Plot
    ↓
Format
    ↓
Save
    ↓
Show


------------------------------------------------------------


15. SAVE BEFORE CLOSE

Correct:

fig.savefig(
    file
)

plt.close(
    fig
)


------------------------------------------------------------


16. CLOSE AUTOMATIC FIGURES

When processing many cases:

plt.close(
    fig
)


prevents unnecessary accumulation of open figures.


------------------------------------------------------------


17. DESCRIPTIVE FILENAMES

Prefer:

fft_comparison.pdf

efficiency_vs_load.png

voltage_transient.svg


Avoid:

figure1.png

new.pdf

final_final.svg


------------------------------------------------------------


18. VECTOR VS RASTER

Raster:

Pixels
    ↓
PNG


Vector:

Mathematical graphical elements
    ↓
PDF / SVG for many Matplotlib plots


------------------------------------------------------------


19. DPI

Mainly important for rasterized content.

Typical examples:

300 DPI
    High-quality raster export

600 DPI
    Higher raster resolution if required


Always follow the actual publication requirement.


------------------------------------------------------------


20. bbox_inches="tight"

Very useful for avoiding:

Clipped labels

Clipped legends

Clipped annotations


------------------------------------------------------------


21. ALWAYS VERIFY EXPORTED FILE

Do not assume a successful save means the figure is ready.

Open it and check:

Resolution

Cropping

Labels

Legend

Units

Line visibility


------------------------------------------------------------


22. PRACTICAL RESEARCH RECOMMENDATION

For an important final figure, keeping:

figure.png

figure.pdf

figure.svg


can provide flexibility for:

Presentation

Publication

Editing

Archiving


------------------------------------------------------------


23. MOST IMPORTANT PRINCIPLE

Resolution cannot fix poor scientific visualization.

First make the figure:

Correct

Clear

Readable

Scientifically meaningful


Then export it at the appropriate:

Size

Format

Resolution


------------------------------------------------------------


NEXT:

19_high_resolution_figures.py


The next file can go deeper into:

72 vs 150 vs 300 vs 600 DPI

Figure size vs DPI

Pixel dimensions

Single-column paper figures

Double-column paper figures

Font size after document scaling

Line width after scaling

Marker size

Rasterization

High-resolution PNG/TIFF concepts

Publication export workflow

Why increasing DPI alone does not make a figure
publication-quality
"""
