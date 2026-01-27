from datetime import datetime
from ..extensions import db

class Issue(db.Model):
    __tablename__ = "issues"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100))
    ai_summary = db.Column(db.Text)
    status = db.Column(db.String(50), default="open")
    priority = db.Column(db.String(50))
    student_name = db.Column(db.String(100))
    department = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "ai_summary": self.ai_summary,
            "status": self.status,
            "priority": self.priority,
            "student_name": self.student_name,
            "department": self.department,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
