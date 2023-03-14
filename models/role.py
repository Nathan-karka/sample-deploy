from app import db
from datetime import datetime

class Roles(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True, nullable = False)
    name = db.Column(db.String(50), nullable = False)
    status = db.Column(db.Enum('active', 'inactive'), default = 'active')
    is_deleted = db.Column(db.Enum('0', '1'), default = "0")
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    created_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)