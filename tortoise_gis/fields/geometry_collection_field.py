from shapely.geometry.collection import GeometryCollection
from tortoise_gis.fields.geometry_field import GeometryField


class GeometryCollectionField(GeometryField[GeometryCollection]):
    """
    GeometryCollection field.

    This field is used to save a collection of geometries and/or multi-geometries.
    Note that it does not restrict the type of geometry or multi-geometry it supports.
    """

    field_type = GeometryCollection

    @property
    def SQL_TYPE(self) -> str:
        return (
            f"GEOMETRY(GEOMETRYCOLLECTION,{self.srid})"
            if self.srid
            else "GEOMETRY(GEOMETRYCOLLECTION)"
        )
