from app import db
from datetime import datetime

class ChapterLesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, nullable=False)
    lesson_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updatetd_at = db.Column(db.DateTime, default = datetime.utcnow)