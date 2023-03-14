from app import db
from datetime import datetime

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updatetd_at = db.Column(db.DateTime, default = datetime.utcnow)