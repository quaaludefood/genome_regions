class Region():
    '''Class to represent a region.'''
    Start: int
    End: int


class Segment():
    '''Class to represent a segment of overlapping regions.'''
    Regions: list[Region]
    def __init__(self):
        self.Regions = []

    def add_region(self, region):
        self.Regions.append(region)

    def regions_count(self):
        return len(self.Regions)
    
    def start(self):
        self.Regions = sorted(self.Regions, key=lambda x: x.Start)
        return self.Regions[0].Start
    
    def end(self):
        self.Regions = sorted(self.Regions, key=lambda x: x.End)
        return self.Regions[len(self.Regions)-1].End