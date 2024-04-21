# Description: This is the main file for the genome_regions package. It is used to validate the file path.
from pathlib import Path
from genome_regions.utils import create_regions_from_file, create_dictionary_from_regions


def main():
    """"""
    # print('Please enter the path:')
    # input_file = Path(input())
    input_file = Path('../Regions_Small.txt')
    if input_file.exists():
        regions = create_regions_from_file(input_file)
        regions_dict = create_dictionary_from_regions(regions, False)
        for key in regions_dict.keys():
            print(f"Row {key}:")
            for region in regions_dict[key]:
                print(f"{region.Start}\t{region.End}")

    else:
        raise ValueError("The file was not found!")

if __name__ == "__main__":
    main()