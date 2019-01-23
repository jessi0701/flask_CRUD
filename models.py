from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)