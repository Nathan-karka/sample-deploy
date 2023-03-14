from app import db
from datetime import datetime

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(25))
    value = db.Column(db.String(255))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updatetd_at = db.Column(db.DateTime, default = datetime.utcnow)