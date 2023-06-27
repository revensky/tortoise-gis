import os

from dotenv import load_dotenv
from shapely.geometry import (
    GeometryCollection,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
from tortoise import Tortoise
from tortoise.backends.base.config_generator import generate_config
from tortoise.contrib import test
from tortoise.exceptions import FieldError

from .testmodels import GeometryFields

load_dotenv()


@test.requireCapability(dialect="postgres")
class TestGeometryFields(test.SimpleTestCase):
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        self.line_string = LineString(
            [[-46.657094, -23.560907], [-46.655092, -23.562609]]
        )

        self.line_string0 = LineString(
            [[-46.656035, -23.559848], [-46.654041, -23.561673]]
        )

        self.point = Point(-0.1179996, 51.501921)
        self.point0 = Point(31.1370197, 29.9788089)

        self.polygon = Polygon(
            [[139.690454, 35.667698], [139.698069, 35.681490], [139.703766, 35.668340]]
        )

        self.polygon0 = Polygon(
            [
                [-46.657094, -23.560907],
                [-46.656035, -23.559848],
                [-46.654041, -23.561673],
                [-46.655092, -23.562609],
            ]
        )

        self.multi_line_string = MultiLineString([self.line_string, self.line_string0])
        self.multi_point = MultiPoint([self.point, self.point0])
        self.multi_polygon = MultiPolygon([self.polygon, self.polygon0])

        self.geometry_collection = GeometryCollection(
            [self.line_string, self.point, self.polygon]
        )

    async def _setUpDB(self) -> None:
        config = generate_config(
            os.getenv("POSTGRES_URL"), {"models": ["tests.testmodels"]}, "models", True
        )

        await Tortoise.init(config)
        await Tortoise.generate_schemas(safe=True)

    async def _tearDownDB(self) -> None:
        pass

    async def test_invalid_type_assignment(self) -> None:
        with self.assertRaises(FieldError):
            await GeometryFields.create(point=123)

    async def test_create(self) -> None:
        obj0 = await GeometryFields.create(
            geometry_collection=self.geometry_collection,
            line_string=self.line_string,
            multi_line_string=self.multi_line_string,
            multi_point=self.multi_point,
            multi_polygon=self.multi_polygon,
            point=self.point,
            polygon=self.polygon,
        )

        obj = await GeometryFields.get(id=obj0.id)

        self.assertIsInstance(obj.geometry_collection, GeometryCollection)
        self.assertIsInstance(obj.line_string, LineString)
        self.assertIsInstance(obj.multi_line_string, MultiLineString)
        self.assertIsInstance(obj.multi_point, MultiPoint)
        self.assertIsInstance(obj.multi_polygon, MultiPolygon)
        self.assertIsInstance(obj.point, Point)
        self.assertIsInstance(obj.polygon, Polygon)

        self.assertEqual(obj.geometry_collection, self.geometry_collection)
        self.assertEqual(obj.line_string, self.line_string)
        self.assertEqual(obj.multi_line_string, self.multi_line_string)
        self.assertEqual(obj.multi_point, self.multi_point)
        self.assertEqual(obj.multi_polygon, self.multi_polygon)
        self.assertEqual(obj.point, self.point)
        self.assertEqual(obj.polygon, self.polygon)

    async def test_update(self) -> None:
        obj0 = await GeometryFields.create(
            geometry_collection=self.geometry_collection,
            line_string=self.line_string,
            multi_line_string=self.multi_line_string,
            multi_point=self.multi_point,
            multi_polygon=self.multi_polygon,
            point=self.point,
            polygon=self.polygon,
        )

        obj = await GeometryFields.get(id=obj0.id)

        line_string = LineString([[0, 0], [1, 1]])
        point = Point([0, 0])
        polygon = Polygon([[0, 0], [1, 1], [0, 2]])

        multi_line_string = MultiLineString(
            [LineString([[0, 0], [1, 1]]), LineString([[0, 1], [1, 0]])]
        )

        multi_point = MultiPoint(
            [Point([0, 0]), Point([0, 1]), Point([1, 0]), Point([1, 1])]
        )

        multi_polygon = MultiPolygon(
            [Polygon([[0, 0], [1, 1], [0, 2]]), Polygon([[1, 1], [1, 0], [1, 2]])]
        )

        geometry_collection = GeometryCollection([line_string, point, polygon])

        obj.line_string = line_string
        obj.multi_line_string = multi_line_string
        obj.multi_point = multi_point
        obj.multi_polygon = multi_polygon
        obj.point = point
        obj.polygon = polygon
        obj.geometry_collection = geometry_collection

        await obj.save()

        obj2 = await GeometryFields.get(id=obj0.id)

        self.assertEqual(obj2.geometry_collection, geometry_collection)
        self.assertEqual(obj2.line_string, line_string)
        self.assertEqual(obj2.multi_line_string, multi_line_string)
        self.assertEqual(obj2.multi_point, multi_point)
        self.assertEqual(obj2.multi_polygon, multi_polygon)
        self.assertEqual(obj2.point, point)
        self.assertEqual(obj2.polygon, polygon)
