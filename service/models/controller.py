from service.db import db


class ControllerModel(db.Model):
    __tablename__ = 'controllers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    set_value = db.Column(db.Integer)
    range = db.Column(db.Integer)
    unit = db.Column(db.String(80))

    clusted_id = db.Column(db.Integer, db.ForeignKey('clusters.id'))
    cluster = db.relationship('ClusterModel')

    def __init__(self, name, set_value, range, unit, cluster_id):
        self.name = name
        self.set_value = set_value
        self.range = range
        self.unit = unit
        self.clusted_id = cluster_id

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
