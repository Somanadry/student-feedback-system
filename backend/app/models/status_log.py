from datetime import datetime
from ..extensions import db

class StatusLog(db.Model):
    __tablename__ = "status_logs"

    id = db.Column(db.Integer, primary_key=True)
    issue_id = db.Column(db.Integer, db.ForeignKey("issues.id"), nullable=False)
    old_status = db.Column(db.String(50))
    new_status = db.Column(db.String(50))
    changed_by = db.Column(db.String(100))
    changed_at = db.Column(db.DateTime, default=datetime.utcnow)
