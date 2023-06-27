from shapely.geometry.polygon import Polygon
from tortoise_gis.fields.geometry_field import GeometryField


class PolygonField(GeometryField[Polygon]):
    """
    Polygon field.

    This field is used to save a polygon. It takes at least three points to create
    a polygon. The polygon can have one shell and one or more holes inside the shell.
    """

    field_type = Polygon

    @property
    def SQL_TYPE(self) -> str:
        return f"GEOMETRY(POLYGON,{self.srid})" if self.srid else "GEOMETRY(POLYGON)"
