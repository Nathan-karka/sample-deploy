from app import db
from datetime import datetime

class LevelChapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.Integer, nullable=False)
    chapter_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updatetd_at = db.Column(db.DateTime, default = datetime.utcnow)