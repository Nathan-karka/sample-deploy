from app import db
from datetime import datetime

class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updatetd_at = db.Column(db.DateTime, default = datetime.utcnow)