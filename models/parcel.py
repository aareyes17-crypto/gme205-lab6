from models.spatial_object import SpatialObject

class Parcel(SpatialObject):
    def __init__(self, parcel_id, geometry, area, zone):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.area = area
        self.zone = zone

    def compute_area(self):
        return self.area