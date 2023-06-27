from tortoise.fields import IntField
from tortoise.models import Model
from tortoise_gis.fields import (
    GeometryCollectionField,
    LineStringField,
    MultiLineStringField,
    MultiPointField,
    MultiPolygonField,
    PointField,
    PolygonField,
)


class GeometryFields(Model):
    id = IntField(pk=True)
    geometry_collection = GeometryCollectionField(srid=4326, null=True)
    line_string = LineStringField(srid=4326, null=True)
    multi_line_string = MultiLineStringField(srid=4326, null=True)
    multi_point = MultiPointField(srid=4326, null=True)
    multi_polygon = MultiPolygonField(srid=4326, null=True)
    point = PointField(srid=4326, null=True)
    polygon = PolygonField(srid=4326, null=True)

    class Meta:
        table = "geometry_fields"
