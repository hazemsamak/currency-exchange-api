from marshmallow import Schema, fields


class DefaultsRateSchema(Schema):
    rates = fields.Dict(keys=fields.Str(), values=fields.Float())

class PrayerTimingsSchema(Schema):
    timings = fields.Dict(keys=fields.Str(), values=fields.Str())

class DeskUsageSchema(Schema):
    utilization = fields.Dict(keys=fields.Str(), values=fields.Str())

class RateConverterSchema(Schema):
    from_currency = fields.Str()
    to_currency = fields.Str()
    rate = fields.Float(dump_only=True)

class LoopbackSchema(Schema):
    message = fields.Str()