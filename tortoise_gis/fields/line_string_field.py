from shapely.geometry.linestring import LineString
from tortoise_gis.fields.geometry_field import GeometryField


class LineStringField(GeometryField[LineString]):
    """
    LineString field.

    This field is used to save a line. It takes a collection of at least two points.
    """

    field_type = LineString

    @property
    def SQL_TYPE(self) -> str:
        return (
            f"GEOMETRY(LINESTRING,{self.srid})" if self.srid else "GEOMETRY(LINESTRING)"
        )
