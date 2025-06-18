from db import db

class UserModel(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String, nullable=False)
    tasks = db.relationship("TaskModel", backref="user", lazy=True)
