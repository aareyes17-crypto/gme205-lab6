from models.spatial_object import SpatialObject


class Road(SpatialObject):
    def __init__(self, road_id, geometry, length, road_type):
        super().__init__(geometry)
        self.road_id = road_id
        self.length = length
        self.road_type = road_type

    def get_length(self):
        return self.length