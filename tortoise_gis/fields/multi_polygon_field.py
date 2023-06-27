from shapely.geometry.multipolygon import MultiPolygon
from tortoise_gis.fields.geometry_field import GeometryField


class MultiPolygonField(GeometryField[MultiPolygon]):
    """
    MultiPolygon field.

    This field is used to save a collection of polygons.
    """

    field_type = MultiPolygon

    @property
    def SQL_TYPE(self) -> str:
        return (
            f"GEOMETRY(MULTIPOLYGON,{self.srid})"
            if self.srid
            else "GEOMETRY(MULTIPOLYGON)"
        )
