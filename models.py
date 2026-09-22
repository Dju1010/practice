from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    tags = db.relationship("Tag", backref="note", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "tags": [t.name for t in self.tags],
        }


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey("note.id"), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "note_id": self.note_id}