from marshmallow import Schema, fields

class RateSchema(Schema):
    name = fields.Str()
    value = fields.Float()

class RateConverterSchema(Schema):
    from_currency = fields.Str()
    to_currency = fields.Str()
    rate = fields.Float(dump_only=True)
