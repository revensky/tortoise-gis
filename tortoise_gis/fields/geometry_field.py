from shapely.errors import ShapelyError
from shapely.geometry.base import BaseGeometry
from shapely.wkb import dumps as shapely_wkb_dumps, loads as shapely_wkb_loads
from shapely.wkt import loads as shapely_wkt_loads
from tortoise.exceptions import FieldError, OperationalError
from tortoise.fields import Field
from tortoise.models import Model
from tortoise.validators import Validator
from typing import Any, Callable, List, Optional, Type, TypeVar, Union


T = TypeVar("T", bound=BaseGeometry)


class GeometryField(Field[T]):
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

    :param source_field: Provide a source_field name if the DB column name needs to be
        something specific instead of generated off the field name.

    :param generated: Is this field DB-generated?

    :param pk: Is this field a Primary Key? Can only have a single such field on the Model,
        and if none is specified it will autogenerate a default primary key called ``id``.

    :param null: Is this field nullable?

    :param default: A default value for the field if not specified on Model creation.
        This can also be a callable for dynamic defaults in which case we will call it.
        The default value will not be part of the schema.

    :param unique: Is this field unique?

    :param index: Should this field be indexed by itself?

    :param description: Field description. Will also appear in ``Tortoise.describe_model()``
        and as DB comments in the generated DDL.

    :param validators: Validators for this field.
    """

    SQL_TYPE: str = "GEOMETRY"

    def __init__(
        self,
        srid: Optional[int] = None,
        spatial_index: bool = True,
        source_field: Optional[str] = None,
        generated: bool = False,
        pk: bool = False,
        null: bool = False,
        default: Any = None,
        unique: bool = False,
        index: bool = False,
        description: Optional[str] = None,
        model: Optional[Model] = None,
        validators: Optional[List[Union[Validator, Callable]]] = None,
        **kwargs: Any,
    ) -> None:
        self.srid = srid
        self.spatial_index = spatial_index

        super().__init__(
            source_field,
            generated,
            pk,
            null,
            default,
            unique,
            index,
            description,
            model,
            validators,
            **kwargs,
        )

    def to_db_value(
        self, value: Optional[Union[T, str, bytes]], instance: Union[Type[Model], Model]
    ) -> Optional[str]:
        """
        Converts from the Python type to the DB type.

        :param value: Current python value in model.
        :param instance: Model class or Model instance provided to look up.
        """

        if value is None:
            return value

        if not isinstance(value, (BaseGeometry, str, bytes)):
            raise FieldError(
                'The value to be saved must be one of ["BaseGeometry", "str", "bytes"].'
            )

        if isinstance(value, str):
            return value

        if isinstance(value, bytes):
            return value.hex()

        return shapely_wkb_dumps(value, hex=True, srid=self.srid)

    def to_python_value(self, value: Optional[Union[T, str, bytes]]) -> Optional[T]:
        """
        Converts from the DB type to the Python type.

        :param value: Value from DB
        """

        if value is None or isinstance(value, BaseGeometry):
            return value

        if not isinstance(value, (str, bytes)):
            raise FieldError(f'Invalid type: "{type(value)}", expected "str or bytes".')

        if isinstance(value, bytes):
            try:
                return shapely_wkb_loads(value)
            except ShapelyError as exc:
                raise OperationalError("Could not parse the provided data.") from exc

        try:
            int(value, 16)  # Prevents "ParseException: Invalid HEX char."
            return shapely_wkb_loads(value, hex=True)
        except (ValueError, ShapelyError):
            pass

        try:
            return shapely_wkt_loads(value)
        except ShapelyError:
            pass

        raise OperationalError("Could not parse the provided data.")
