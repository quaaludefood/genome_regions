# Description: This is the main file for the genome_regions package. It is used to validate the file path.
from pathlib import Path
from genome_regions.utils import get_regions_from_file, create_dictionary_from_regions
from genome_regions.utils import generate_file


def main():
    """"""
    # print('Please enter the path:')
    # input_file = Path(input())
    input_file = Path('../Regions_Large.txt')
    output_path = Path('../')
    if not output_path.exists():
        output_path.mkdir()
    if input_file.exists():
        regions = get_regions_from_file(input_file)
        regions_dict = create_dictionary_from_regions(regions, False)
        total_rows = 0
        total_regions = 0
        for key in regions_dict.keys():
            total_rows += 1
            for region in regions_dict[key]:
                total_regions += 1
                print(f"{region.Start}\t{region.End}")
        print(f"Total rows: {total_rows} Total regions: {total_regions}")
        generate_file(regions_dict, output_path , 'output.txt')

    else:
        raise ValueError("The input file was not found!")

if __name__ == "__main__":
    main()