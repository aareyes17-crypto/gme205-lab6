from own_model.spatial_object import SpatialObject


class Parcel(SpatialObject):
    def __init__(self, parcel_id, owner, geometry):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.owner = owner

    def compute_area(self):
        return self.area()

    def get_bounds(self):
        return self.geometry

    def detect_overlap(self, other_parcels):
        overlaps = []
        for parcel in other_parcels:
            if parcel is not self and self.intersects(parcel, threshold=5.0):
                overlaps.append(parcel.parcel_id)
        return overlaps

    @staticmethod
    def load_from_geojson(data):
        parcels = []
        for item in data:
            parcel = Parcel(
                parcel_id=item["id"],
                owner=item["owner"],
                geometry=item["geometry"]
            )
            parcels.append(parcel)
        return parcels

    def describe(self):
        return (
            f"Parcel {self.parcel_id} | Owner: {self.owner} | "
            f"Geometry: {self.geometry}"
        )
    