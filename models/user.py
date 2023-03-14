from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash

class User(db.Model):
     id = db.Column(db.Integer, primary_key = True, autoincrement = True)
     name = db.Column(db.String(50), nullable = False)
     email = db.Column(db.String(255), nullable = False, unique = True)
     password = db.Column(db.String(255), nullable = False)
     mobile =db.Column(db.String(15))
     role = db.Column(db.String(50))
     role_ref_id = db.Column(db.Integer)
     status = db.Column(db.Enum('active', 'inactive'), default = 'active')
     is_deleted = db.Column(db.Enum('0','1'), default = '0')
     created_at = db.Column(db.DateTime, default = datetime.utcnow)
     created_by = db.Column(db.String(255))
     updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

     # def __init__(self, password, name, email, role, role_ref_id, created_by, mobile):
     #      self.password = generate_password_hash(password, method="pbkdf2:sha256")
     #      self.name = name
     #      self.email = email
     #      self.role = role
     #      self.role_ref_id = role_ref_id
     #      self.created_by = created_by
     #      self.mobile = mobile
