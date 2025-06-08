# Image Processing Tool (PGM Format)

This is a grayscale image processing tool developed in pure Python, without using any external libraries.  
The tool is capable of loading `.pgm` images, applying various manipulations, and saving the output back in `.pgm` format.

Developed as part of the CMPE150 - Introduction to Computing course at Boğaziçi University.

## Features

- `read_imagefile(f)`  
  Parses `.pgm` image files and returns a 2D integer matrix representing pixel intensities.

- `write_imagefile(f, img_matrix)`  
  Writes a 2D integer matrix into a `.pgm` file according to the P2 format.

- `misalign(img_matrix)`  
  Reverses all odd-numbered columns from top to bottom.

- `sort_columns(img_matrix)`  
  Sorts each column independently in ascending order (top to bottom).

- `sort_rows_border(img_matrix)`  
  Sorts each row between black borders in ascending order (left to right).  
  Borders are pixels with value 0 and may span multiple columns.

- `convolution(img_matrix, kernel)`  
  Applies 3x3 kernel convolution with zero-padding and clamps the results between [0, 255].  
  High-pass filtering is supported with a built-in kernel.

## Usage

The program expects a command-line style input:
```
<INPUT_FILE> <COMMAND> <OUTPUT_FILE>
```

- `INPUT_FILE`: Name of the input `.pgm` image (e.g. `cat.pgm`)
- `COMMAND`: One of `misalign`, `sort_columns`, `sort_rows_border`, `highpass`
- `OUTPUT_FILE`: Name of the output file (e.g. `cat_filtered.pgm`)

### Example
```bash
cat.pgm highpass cat_highpass.pgm
```

## Example Outputs

Visual examples can be viewed using tools like PGMViewer or GIMP.  
Sample input/output files and screenshots are provided in the main repo folder.

## Constraints

- No imports allowed.
- All functionality implemented from scratch using built-in Python constructs.

## About the Course

CMPE150 – Introduction to Computing  
A foundational course focusing on programming fundamentals, control structures, and file I/O using Python.  
Boğaziçi University – Fall 2023
