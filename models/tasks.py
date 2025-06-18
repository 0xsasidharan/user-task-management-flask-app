from db import db

class TaskModel(db.Model):
    __tablename__ = "tasks"
    task_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey("users.user_id"), nullable=False)