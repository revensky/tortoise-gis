from typing import Any, Type, Union

import shapely.wkb
import shapely.wkt
from tortoise import Model
from tortoise.exceptions import FieldError
from tortoise.fields import Field
from shapely.errors import WKBReadingError, WKTReadingError
from shapely.geometry.base import BaseGeometry


class GeometryField(Field, BaseGeometry):
    """
    Base Geometry Field.
    """

    SQL_TYPE: str = "GEOMETRY"

    def __init__(self, srid: int = None, dimensions: int = 2, **kwargs: Any) -> None:
        self.srid = srid
        self.dimensions = dimensions
        super(GeometryField, self).__init__(**kwargs)

    def to_db_value(
        self, value: Union[BaseGeometry, str], instance: Union[Type[Model], Model]
    ) -> str:
        if value is None:
            return value

        if isinstance(value, BaseGeometry):
            return shapely.wkb.dumps(value, hex=True, srid=self.srid)

        if isinstance(value, str):
            return shapely.wkt.dumps(value)

    def to_python_value(self, value: Any) -> BaseGeometry:
        if value is None or isinstance(value, BaseGeometry):
            return value

        try:
            return shapely.wkb.loads(value, hex=True)
        except WKBReadingError:
            pass

        try:
            return shapely.wkt.loads(value)
        except WKTReadingError:
            pass

        raise FieldError("Could not parse geometry due to invalid input.")
