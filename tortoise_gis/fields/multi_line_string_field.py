from shapely.geometry.multilinestring import MultiLineString
from tortoise_gis.fields.geometry_field import GeometryField


class MultiLineStringField(GeometryField[MultiLineString]):
    """
    MultiLineString field.

    This field is used to save a collection of linestrings.
    """

    field_type = MultiLineString

    @property
    def SQL_TYPE(self) -> str:
        return (
            f"GEOMETRY(MULTILINESTRING,{self.srid})"
            if self.srid
            else "GEOMETRY(MULTILINESTRING)"
        )
