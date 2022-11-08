from marshmallow import Schema, fields

class DefaultsRateSchema(Schema):
    rates = fields.Dict(keys=fields.Str(), values=fields.Float())

class RateConverterSchema(Schema):
    from_currency = fields.Str()
    to_currency = fields.Str()
    rate = fields.Float(dump_only=True)
