from models.spatial_object import SpatialObject


class Building(SpatialObject):
    def __init__(self, building_id, geometry, height, usage):
        super().__init__(geometry)
        self.building_id = building_id
        self.height = height
        self.usage = usage

    def get_height(self):
        return self.height