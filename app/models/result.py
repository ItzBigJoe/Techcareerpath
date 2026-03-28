from app.core.extensions import db

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    career = db.Column(db.String(100))
    score = db.Column(db.Integer)
    skills = db.Column(db.JSON)
    gaps = db.Column(db.JSON)