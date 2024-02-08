from marshmallow import Schema, fields


class DefaultsRateSchema(Schema):
    rates = fields.Dict(keys=fields.Str(), values=fields.Float())
    rates_bm = fields.Dict(keys=fields.Str(), values=fields.Float())

class PrayerTimingsSchema(Schema):
    timings = fields.Dict(keys=fields.Str(), values=fields.Str())

class DeskUsageSchema(Schema):
    utilization = fields.Dict(keys=fields.Str(), values=fields.Dict())

class RateConverterSchema(Schema):
    from_currency = fields.Str()
    to_currency = fields.Str()
    black_market = fields.Bool()
    rate = fields.Float(dump_only=True)

class LoopbackSchema(Schema):
    message = fields.Str()