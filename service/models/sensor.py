from service.db import db


class SensorModel(db.Model):
    __tablename__ = 'controllers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    data = db.Column(db.Float(precision=2))

    def __init__(self, name, data):
        self.name = name
        self.data = data

    def json(self):
        return {'id': self.id, 'name': self.name, 'set_value': self.set_value, 'range': self.range, 'unit': self.unit}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # SELECT * FROM controllers WHERE name=? LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
