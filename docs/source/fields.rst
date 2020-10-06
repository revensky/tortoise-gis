Fields
======

Provides the supported **Geometry** and **Geography** fields.
It has support for :meth:`Tortoise.generate_schemas()` for automatic generation.

All **Geometry** fields provide the support for setting a *SRID* on the column.
This ensures that the data will be saved with this metadata and will not require
a cast to the desired *SRID* upon retrieval.

.. note:: The storage of the *SRID* is handled entirely by the database.
   The field only ensures that a *SRID*, if provided, will be passed to the database
   for it to handle and store as it sees fit.

Example:::

   from tortoise import Model, fields
   from tortoise_gis import fields as gis


   class TreasureMap(Model):
      title = fields.CharField(32, unique=True)
      start = gis.PointField()
      end = gis.PointField()
      path = gis.LineStringField()

      class Meta:
         table = "treasure_maps"


.. automodule:: tortoise_gis.fields

.. autoclass:: GeometryField

.. autoclass:: PointField

.. autoclass:: LineStringField

.. autoclass:: PolygonField

.. autoclass:: MultiPointField

.. autoclass:: MultiLineStringField

.. autoclass:: MultiPolygonField

.. autoclass:: GeometryCollectionField
