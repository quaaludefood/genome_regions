## Genome Regions Coding Project

A simple Python application which reads a Regions file and generates a file of regions assigned to drawing rows and a file of segments of overlapping regions with a read count.

The algorithms were developed by formulating a strategy to generate the data required and iterative rounds of testing on the files provided to achieve the expected outcome. The Rows algorithm creates a dictionary with row numbers as keys and arrays of non-overlapping regions as values; the Segments creates an array of segment objects which include an array of overlapping regions, and functions which provide the Start and End co-ordinates of the segment.

Time taken to develop: Approx 8 hours

## Running the application
- Naviate to the inner genome_regions directory
- The application accepts a commandline argument specifying the location of the input file, e.g:
`python main.py -i=../Regions_Small.txt`
- It generates two files in the output folder, rows_output.txt (for part one of the assignment) and segments_output.txt (for part two of the assignment)

### Dependencies
- Python ([download](https://www.python.org/downloads/))
- Python should be added to the environment variables of your system. If you are using Windows please refer to the [instructions ](https://www.python.org/downloads/)