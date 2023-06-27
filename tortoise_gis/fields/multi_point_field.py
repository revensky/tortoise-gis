from shapely.geometry.multipoint import MultiPoint
from tortoise_gis.fields.geometry_field import GeometryField


class MultiPointField(GeometryField[MultiPoint]):
    """
    MultiPoint field.

    This field is used to save a collection of points.
    """

    field_type = MultiPoint

    @property
    def SQL_TYPE(self) -> str:
        return (
            f"GEOMETRY(MULTIPOINT,{self.srid})" if self.srid else "GEOMETRY(MULTIPOINT)"
        )
