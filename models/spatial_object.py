from math import sqrt


class SpatialObject:
    def __init__(self, geometry):
        self.geometry = geometry

    def distance_to(self, other):
        x1, y1 = self.geometry["x"], self.geometry["y"]
        x2, y2 = other.geometry["x"], other.geometry["y"]

        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def intersects(self, other, threshold=0.0):
        return self.distance_to(other) <= threshold
