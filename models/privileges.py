from app import db
from datetime import datetime

class Privileges(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    module = db.Column(db.String(150))
    code = db.Column(db.String(150), nullable = False)
    privilege = db.Column(db.String(150))
    status = db.Column(db.Enum('active', 'inactive'), default = 'active')
    is_deleted = db.Column(db.Enum('0','1'), default = '0')
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    created_by = db.Column(db.String(100))
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)