from db import db
# from werkzeug.security import generate_password_hash, check_password_hash


class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True, nullable=False)


class Developer(db.Model):
    __tablename__ = 'developer'

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
