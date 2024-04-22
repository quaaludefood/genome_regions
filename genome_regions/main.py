# Description: This is the main file for the genome_regions package. It is used to validate the file path.
from pathlib import Path
from utils import get_regions_from_file, create_rows_from_regions, create_segments_from_regions, generate_rows_file, generate_segments_file
import argparse, sys




def main():
    """"""
    #'../Regions_Large.txt'
    parser=argparse.ArgumentParser()
    parser.add_argument('-i', '--input',  help='regions file',  required=True)
    args=parser.parse_args()
    input_file = Path(args.input)
    output_path = Path('../output_folder')

    if input_file.exists():
        regions = get_regions_from_file(input_file)
        rows_dict = create_rows_from_regions(regions)
        generate_rows_file(rows_dict, output_path , 'rows_output.txt')
        segments_list = create_segments_from_regions(regions)
        generate_segments_file(segments_list, output_path, 'segments_output.txt')

    else:
        raise ValueError("The input file was not found!")

if __name__ == "__main__":
    main()