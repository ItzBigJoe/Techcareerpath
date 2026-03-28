from app.core.extensions import db

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100)) # Using session_id instead of user_id
    answers = db.Column(db.JSON)