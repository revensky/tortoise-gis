from tortoise.expressions import Function
from tortoise_gis import _pypika_functions as functions


class ST_3DDWithin(Function):
    database_func = functions.ST_3DDWithin


class ST_3DDifference(Function):
    database_func = functions.ST_3DDifference


class ST_3DDistance(Function):
    database_func = functions.ST_3DDistance


class ST_3DExtent(Function):
    database_func = functions.ST_3DExtent


class ST_3DIntersection(Function):
    database_func = functions.ST_3DIntersection


class ST_3DIntersects(Function):
    database_func = functions.ST_3DIntersects


class ST_3DLength(Function):
    database_func = functions.ST_3DLength


class ST_3DPerimeter(Function):
    database_func = functions.ST_3DPerimeter


class ST_3DUnion(Function):
    database_func = functions.ST_3DUnion


class ST_Area(Function):
    database_func = functions.ST_Area


class ST_AsBinary(Function):
    database_func = functions.ST_AsBinary


class ST_AsEWKT(Function):
    database_func = functions.ST_AsEWKT


class ST_AsFlatGeobuf(Function):
    database_func = functions.ST_AsFlatGeobuf


class ST_AsGeobuf(Function):
    database_func = functions.ST_AsGeobuf


class ST_AsGeoJSON(Function):
    database_func = functions.ST_AsGeoJSON


class ST_AsGML(Function):
    database_func = functions.ST_AsGML


class ST_AsGeoJSON(Function):
    database_func = functions.ST_AsGeoJSON


class ST_AsKML(Function):
    database_func = functions.ST_AsKML


class ST_AsMVT(Function):
    database_func = functions.ST_AsMVT


class ST_AsSVG(Function):
    database_func = functions.ST_AsSVG


class ST_AsText(Function):
    database_func = functions.ST_AsText


class ST_Azimuth(Function):
    database_func = functions.ST_Azimuth


class ST_Boundary(Function):
    database_func = functions.ST_Boundary


class ST_Buffer(Function):
    database_func = functions.ST_Buffer


class ST_Centroid(Function):
    database_func = functions.ST_Centroid


class ST_Centroid(Function):
    database_func = functions.ST_Centroid


class ST_ClosestPoint(Function):
    database_func = functions.ST_ClosestPoint


class ST_ClusterIntersecting(Function):
    database_func = functions.ST_ClusterIntersecting


class ST_ClusterWithin(Function):
    database_func = functions.ST_ClusterWithin


class ST_Collect(Function):
    database_func = functions.ST_Collect


class ST_Contains(Function):
    database_func = functions.ST_Contains


class ST_ConvexHull(Function):
    database_func = functions.ST_ConvexHull


class ST_CoordDim(Function):
    database_func = functions.ST_CoordDim


class ST_CoveredBy(Function):
    database_func = functions.ST_CoveredBy


class ST_Covers(Function):
    database_func = functions.ST_Covers


class ST_Crosses(Function):
    database_func = functions.ST_Crosses


class ST_CurveToLine(Function):
    database_func = functions.ST_CurveToLine


class ST_DWithin(Function):
    database_func = functions.ST_DWithin


class ST_Difference(Function):
    database_func = functions.ST_Difference


class ST_Dimension(Function):
    database_func = functions.ST_Dimension


class ST_Disjoint(Function):
    database_func = functions.ST_Disjoint


class ST_Distance(Function):
    database_func = functions.ST_Distance


class ST_EndPoint(Function):
    database_func = functions.ST_EndPoint


class ST_Envelope(Function):
    database_func = functions.ST_Envelope


class ST_Equals(Function):
    database_func = functions.ST_Equals


class ST_Extent(Function):
    database_func = functions.ST_Extent


class ST_ExteriorRing(Function):
    database_func = functions.ST_ExteriorRing


class ST_GeoHash(Function):
    database_func = functions.ST_GeoHash


class ST_GeometryN(Function):
    database_func = functions.ST_GeometryN


class ST_GeometryType(Function):
    database_func = functions.ST_GeometryType


class ST_InteriorRingN(Function):
    database_func = functions.ST_InteriorRingN


class ST_Intersection(Function):
    database_func = functions.ST_Intersection


class ST_Intersects(Function):
    database_func = functions.ST_Intersects


class ST_IsClosed(Function):
    database_func = functions.ST_IsClosed


class ST_IsCollection(Function):
    database_func = functions.ST_IsCollection


class ST_IsEmpty(Function):
    database_func = functions.ST_IsEmpty


class ST_IsRing(Function):
    database_func = functions.ST_IsRing


class ST_IsSimple(Function):
    database_func = functions.ST_IsSimple


class ST_IsValid(Function):
    database_func = functions.ST_IsValid


class ST_Length(Function):
    database_func = functions.ST_Length


class ST_MakeLine(Function):
    database_func = functions.ST_MakeLine


class ST_MakePoint(Function):
    database_func = functions.ST_MakePoint


class ST_MakePolygon(Function):
    database_func = functions.ST_MakePolygon


class ST_MakeSolid(Function):
    database_func = functions.ST_MakeSolid


class ST_MemUnion(Function):
    database_func = functions.ST_MemUnion


class ST_NumGeometries(Function):
    database_func = functions.ST_NumGeometries


class ST_NumInteriorRings(Function):
    database_func = functions.ST_NumInteriorRings


class ST_NumPoints(Function):
    database_func = functions.ST_NumPoints


class ST_OrderingEquals(Function):
    database_func = functions.ST_OrderingEquals


class ST_Overlaps(Function):
    database_func = functions.ST_Overlaps


class ST_Perimeter(Function):
    database_func = functions.ST_Perimeter


class ST_Point(Function):
    database_func = functions.ST_Point


class ST_PointN(Function):
    database_func = functions.ST_PointN


class ST_PointOnSurface(Function):
    database_func = functions.ST_PointOnSurface


class ST_Polygon(Function):
    database_func = functions.ST_Polygon


class ST_Polygonize(Function):
    database_func = functions.ST_Polygonize


class ST_Project(Function):
    database_func = functions.ST_Project


class ST_Relate(Function):
    database_func = functions.ST_Relate


class ST_SRID(Function):
    database_func = functions.ST_SRID


class ST_Segmentize(Function):
    database_func = functions.ST_Segmentize


class ST_SetSRID(Function):
    database_func = functions.ST_SetSRID


class ST_StartPoint(Function):
    database_func = functions.ST_StartPoint


class ST_SymDifference(Function):
    database_func = functions.ST_SymDifference


class ST_Touches(Function):
    database_func = functions.ST_Touches


class ST_Transform(Function):
    database_func = functions.ST_Transform


class ST_Union(Function):
    database_func = functions.ST_Union


class ST_Within(Function):
    database_func = functions.ST_Within


class ST_X(Function):
    database_func = functions.ST_X


class ST_Y(Function):
    database_func = functions.ST_Y


class ST_Z(Function):
    database_func = functions.ST_Z
