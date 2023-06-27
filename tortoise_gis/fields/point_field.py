from shapely.geometry.point import Point
from tortoise_gis.fields.geometry_field import GeometryField


class PointField(GeometryField[Point]):
    """
    Point field.

    This field is used to save points in the format (longitude, latitude).
    """

    field_type = Point

    @property
    def SQL_TYPE(self) -> str:
        return f"GEOMETRY(POINT,{self.srid})" if self.srid else "GEOMETRY(POINT)"
