from marshmallow import fields, Schema
from . import db
from sqlalchemy.dialects.postgresql import UUID


class StateModel(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(UUID, db.ForeignKey('jobs.job_id'), nullable=False)
    app_name = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(128), nullable=True)
    date_created = db.Column(db.String(128), nullable=True)

    def __init__(self, data):
        self.owner_id = data.get('owner_id')
        self.app_name = data.get('app_name')
        self.state = data.get('state')
        self.date_created = data.get('date_created')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_states_of_job(job_id):
        return StateModel.query.filter(StateModel.owner_id == job_id).all()

    def __repr(self):
        return '<id {}>'.format(self.id)


class StateSchema(Schema):
    id = fields.Int(dump_only=True)
    owner_id = fields.UUID(required=True)
    app_name = fields.Str(required=True)
    state = fields.Str(required=True)
    date_created = fields.Str(required=True)
