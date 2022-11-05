from marshmallow import Schema, fields

class RateSchema(Schema):
    name = fields.Str()
    value = fields.Float()
