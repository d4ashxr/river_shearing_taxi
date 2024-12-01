from db import db

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_pier = db.Column(db.String(120), nullable=False)
    end_pier = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(50), default='pending')
