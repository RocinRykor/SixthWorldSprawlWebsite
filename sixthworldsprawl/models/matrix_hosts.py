from .db import data_base as db


class Hosts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(11), nullable=False, unique=True)
    provider = db.Column(db.String(64), nullable=False)
    data = db.relationship('Data', backref='hosts', lazy='dynamic')
    nodes = db.relationship('Nodes', backref='host', lazy='dynamic')
    security_code = db.Column(db.String(16), nullable=False)
    system_rating = db.Column(db.Integer, nullable=False)
    access_rating = db.Column(db.Integer, nullable=False)
    control_rating = db.Column(db.Integer, nullable=False)
    file_rating = db.Column(db.Integer, nullable=False)
    index_rating = db.Column(db.Integer, nullable=False)
    slave_rating = db.Column(db.Integer, nullable=False)
    paydata_points = db.Column(db.Integer, nullable=False)

    def jsonify(self):
        return {
            "id": self.id,
            "hostname": self.hostname,
            "provider": self.provider,
            "data": self.data,
            "nodes": self.nodes,
            "security_code": self.security_code,
            "system_rating": self.system_rating,
            "access_rating": self.access_rating,
            "control_rating": self.control_rating,
            "file_rating": self.file_rating,
            "index_rating": self.index_rating,
            "slave_rating": self.slave_rating,
            "paydata_points": self.paydata_points
        }


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(2048), nullable=False)
    is_paydata = db.Column(db.Boolean, nullable=False, default=False)
    points = db.Column(db.Integer, nullable=False, default=0)
    value = db.Column(db.Integer, nullable=False, default=0)
    host_id = db.Column(db.Integer, db.ForeignKey('hosts.id'), nullable=False)

    def jsonify(self):
        return {
            "id": self.id,
            "description": self.description,
            "is_paydata": self.is_paydata,
            "points": self.points,
            "value": self.value,
            "host_id": self.host_id
        }


class Nodes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    host_id = db.Column(db.Integer, db.ForeignKey('hosts.id'), nullable=False)
    data_id = db.Column(db.Integer, db.ForeignKey('data.id'), nullable=False)

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "host_id": self.host_id,
            "data_id": self.data_id
        }
