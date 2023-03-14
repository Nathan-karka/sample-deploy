from app import db
from datetime import datetime

class TopicContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, nullable=False)
    content_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updatetd_at = db.Column(db.DateTime, default = datetime.utcnow)