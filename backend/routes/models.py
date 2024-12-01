from db import db

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    schedule = db.Column(db.Text, nullable=True)
