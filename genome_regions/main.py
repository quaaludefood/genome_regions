from pathlib import Path
from utils import get_regions_from_file, create_rows_from_regions, create_segments_from_regions, generate_rows_file, generate_segments_file
import argparse
from datetime import datetime

def main():
    '''Main function to run the program.'''
    parser=argparse.ArgumentParser()
    parser.add_argument('-i', '--input',  help='regions file',  required=True)
    args=parser.parse_args()
    input_file = Path(args.input)
    output_path = Path('../output_folder')

    if input_file.exists():
        regions = get_regions_from_file(input_file)
        rows_dict = create_rows_from_regions(regions)
        now = datetime.now()
        timestamp = int(now.timestamp())
        rows_file_name = f'rows_output_{timestamp}.txt'
        segments_file_name = f'segments_output_{timestamp}.txt'
        generate_rows_file(rows_dict, output_path , rows_file_name)
        print(f'Rows file generated: {rows_file_name}')
        segments_list = create_segments_from_regions(regions)
        generate_segments_file(segments_list, output_path, segments_file_name)
        print(f'Segments file generated: {segments_file_name}')
        print(f'Output files will be saved in the {str(output_path)} directory.')

    else:
        raise ValueError("The file does not exist. Please check the path.")

if __name__ == "__main__":
    main()