from models import Region
from models import Segment


def get_regions_from_file(file_path) -> list[Region]:
    '''Reads a file with regions and returns a list of Region objects.'''
    regions = []
    with open(file_path, 'r') as file:
        try:
            content = file.readlines()
            for line in content:
                region = Region()
                region.Start = int(line.split('\t')[0].strip())
                region.End = int(line.split('\t')[1].strip())
                regions.append(region)
        except:
            raise ValueError("The file could not be read. Please check the format.")
    if len(regions) == 0:
        raise ValueError("The file is empty.")
    return regions

def generate_rows_file(rows_dict, output_path, file_name):
    '''Generates a file with the regions assigned to rows.'''
    with open(str(output_path) + '/' + file_name, 'w') as file:
        for row in rows_dict.keys():
            for region in rows_dict[row]:
                file.write(f"{row}\t{region.Start}\t{region.End}\n")

def generate_segments_file(segments_list, output_path, file_name):
    '''Generates a file with the segments of overlapping regions.'''
    with open(str(output_path) + '/' + file_name, 'w') as file:
        for segment in segments_list:
            file.write(f"{segment.regions_count()}\t{segment.start()}\t{segment.end()}\n")
    

def create_segments_from_regions(regions) -> list[Segment]:
    '''Creates a list of Segment objects from a list of Region objects.'''
    sorted_regions = sorted(regions, key=lambda x: x.Start)
    key = 0
    regions_dict = {key: [sorted_regions[0]]}
    segments = []
    for i, region in enumerate(sorted_regions):
        if i > 0:           
            while i < len(sorted_regions):            
                if any(region.Start <= x.End for x in regions_dict[key]):
                    regions_dict[key].append(region)                 
                    break
                else:
                    key = key + 1
                    regions_dict[key] = [region]
                    break
    for key in regions_dict.keys():
        segment = Segment()
        for region in regions_dict[key]:
            segment.add_region(region)
        segments.append(segment)
    return segments

def create_rows_from_regions(regions) -> dict[int, list[Region]]:
    '''Creates a dictionary with the regions assigned to rows.'''
    sorted_regions = sorted(regions, key=lambda x: x.Start)
    rows_dict = {1: [sorted_regions[0]]}
    for i, region in enumerate(sorted_regions):
        if i > 0:
            rows = len(list(rows_dict.keys()))
            for row in rows_dict.keys():
                if region.Start >= rows_dict[row][len(rows_dict[row])-1].End:
                    rows_dict[row].append(region)
                    break
                else:
                    rows_dict[rows + 1] = [region]
                    break

    return rows_dict