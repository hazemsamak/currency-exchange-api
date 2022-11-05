from db import db

class RateModel(db.Model):
    __tablename__ = "rates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    value = db.Column(db.Float, nullable=False)
    

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()