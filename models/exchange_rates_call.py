from db import db
from sqlalchemy.sql import func

class ExchangeRatesCallModel(db.Model):
    __tablename__ = "exchange_rates_calls"

    id = db.Column(db.Integer, primary_key=True)
    rates = db.Column(db.Text, unique=False, nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    

    def json(self):
        return {
            "id": self.id,
            "rates": self.rates,
            "time_created": self.time_created,
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()