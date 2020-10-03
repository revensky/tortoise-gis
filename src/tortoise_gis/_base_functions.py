from pypika.terms import Function


class Area(Function):
    def __init__(self, term, alias=None):
        super().__init__("ST_Area", term, alias=alias)


class AsBinary(Function):
    def __init__(self, term, alias=None):
        super().__init__("ST_AsBinary", term, alias=alias)


class AsGeoJSON(Function):
    def __init__(self, term, alias=None):
        super().__init__("ST_AsGeoJSON", term, alias=alias)


class AsMVT(Function):
    def __init__(self, term, alias=None):
        super().__init__("ST_AsMVT", term, alias=alias)
