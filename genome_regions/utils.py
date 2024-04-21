from models import Region


def get_regions_from_file(file_path):
    regions = []
    with open(file_path, 'r') as file:
        content = file.readlines()
        id = 0
        for line in content:
            region = Region()
            region.Id = id
            region.Start = int(line.split('\t')[0].strip())
            region.End = int(line.split('\t')[1].strip())
            regions.append(region)
            id += 1
        return regions

def generate_file(regions_dict, output_path, file_name):
    with open(str(output_path) + '/' + file_name, 'w') as file:
        for key in regions_dict.keys():
            for region in regions_dict[key]:
                file.write(f"{region.Start}\t{region.End}\n")
    

def create_dictionary_from_regions(regions, create_segments):
    sorted_regions = sorted(regions, key=lambda x: x.Start)
    regions_dict = {0: [sorted_regions[0]]}
    if create_segments:
        return create_segments_from_regions(sorted_regions, regions_dict)
    else:
        return create_rows_from_regions(sorted_regions, regions_dict)


def create_segments_from_regions(sorted_regions, regions_dict):
    key = 0
    for i, region in enumerate(sorted_regions):
        if i > 0:           
            while i < len(sorted_regions):                
                if region.Start <= regions_dict[key][len(regions_dict[key])-1].End:
                    if region.End > regions_dict[key][len(regions_dict[key])-1].End:                       
                        regions_dict[key][len(regions_dict[key])-1].End = region.End                    
                    break
                else:
                    key = key + 1
                    regions_dict[key] = [region]
                    break

    return regions_dict

def create_rows_from_regions(sorted_regions, regions_dict):
    for i, region in enumerate(sorted_regions):
        if i > 0:
            keys = len(list(regions_dict.keys()))
            for key in regions_dict.keys():
                if region.Start >= regions_dict[key][len(regions_dict[key])-1].End:
                    regions_dict[key].append(region)
                    break
                else:
                    regions_dict[keys+1] = [region]
                    break

    return regions_dict