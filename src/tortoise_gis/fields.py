from typing import Any, Type, Union

import shapely.wkb
import shapely.wkt
from tortoise import Model
from tortoise.exceptions import FieldError, OperationalError
from tortoise.fields import Field
from shapely.errors import WKBReadingError, WKTReadingError
from shapely.geometry import (
    GeometryCollection,
    LineString,
    MultiPoint,
    MultiLineString,
    MultiPolygon,
    Point,
    Polygon,
)
from shapely.geometry.base import BaseGeometry


class GeometryField(Field):
    """
    Base Geometry Field.

    To save a data to the database, it **MUST** be either a string containing
    its Well-Known Text (WKT) value or a Shapely Geometry instance.

    Columns defined with restrictions, such as :class:`PointField`, will **ONLY** accept
    data that conform to the restricted geometry. For example, if a Polygon
    is provided as data to a :class:`PointField`, it **WILL** raise an error
    on the database.

    If there is the need to store different types of geometries in the same column,
    consider using this class directly instead of any of its children.

    :param srid: Defines the projection system of the geometry.
        Most applications dealing with coordinates in the form *(longitude, latitude)*
        will want to use **EPSG:4326** (aka **WSG84**) as the *SRID*.

        There are cases where the application is dealing
        with absolute distances in meters.
        In those cases, it is **SUGGESTED** to use a **UTM** coordinate system,
        such as **EPSG:32723**.

        If no value is provided, the database will set the *SRID*
        of the column as unknown. In this case, the sole responsibility of casting
        the values belong to the application.
    :type srid: int

    :param spatial_index: Defines whether the column will have a Spatial Index.
        This index is created by defining an index using *GIST* on the column.
        The default is True.
    :type spatial_index: bool
    """

    SQL_TYPE: str = "GEOMETRY"

    def __init__(
        self,
        srid: int = None,
        spatial_index: bool = True,
        **kwargs: Any,
    ) -> None:
        self.srid = srid
        self.spatial_index = spatial_index
        super().__init__(**kwargs)

    def to_db_value(
        self,
        value: BaseGeometry,
        instance: Union[Type[Model], Model],
    ) -> str:
        if value is None:
            return value

        if not isinstance(value, BaseGeometry):
            raise FieldError("The value to be saved must be a Shapely geometry.")

        return shapely.wkb.dumps(value, hex=True, srid=self.srid)

    def to_python_value(self, value: Any) -> BaseGeometry:
        if value is None or isinstance(value, BaseGeometry):
            return value

        if not isinstance(value, (bytes, str)):
            raise FieldError(f'Invalid type: "{type(value)}", expected "bytes or str".')

        if isinstance(value, bytes):
            try:
                return shapely.wkb.loads(value)
            except WKBReadingError as exc:
                raise OperationalError("Could not parse the provided data.") from exc

        try:
            int(value, 16)  # Prevents "ParseException: Invalid HEX char."
            return shapely.wkb.loads(value, hex=True)
        except (ValueError, WKBReadingError):
            pass

        try:
            return shapely.wkt.loads(value)
        except WKTReadingError:
            pass

        raise OperationalError("Could not parse the provided data.")


class PointField(GeometryField):
    """
    Point field.

    This field is used to save points in the format (longitude, latitude).
    """

    field_type = Point

    @property
    def SQL_TYPE(self) -> str:
        return f"GEOMETRY(POINT,{self.srid})" if self.srid else "GEOMETRY(POINT)"


class LineStringField(GeometryField):
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


class PolygonField(GeometryField):
    """
    Polygon field.

    This field is used to save a polygon. It takes at least three points to create
    a polygon. The polygon can have one shell and one or more holes inside the shell.
    """

    field_type = Polygon

    @property
    def SQL_TYPE(self) -> str:
        return f"GEOMETRY(POLYGON,{self.srid})" if self.srid else "GEOMETRY(POLYGON)"


class MultiPointField(GeometryField):
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


class MultiLineStringField(GeometryField):
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


class MultiPolygonField(GeometryField):
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


class GeometryCollectionField(GeometryField):
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
