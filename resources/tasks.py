from flask import request
from flask.views import MethodView
# from db import tasks , users
from uuid import uuid4
from flask_smorest import Blueprint , abort
from schemas import TaskSchema, TaskUpdateSchema
from models import TaskModel , UserModel
from db import db

blp = Blueprint("Tasks" , __name__ , description="Operations on Tasks")

@blp.route("/tasks")
class TaskListResource(MethodView):
    @blp.response(200 ,TaskSchema(many=True))
    def get(self):
        return list(TaskModel.query.all()) 

    @blp.arguments(TaskSchema)
    @blp.response(201, TaskSchema)
    def post(self , request_data):
        user = UserModel.query.get(request_data["user_id"])
        if user is None:
            abort(404, message="User Id not found")

        new_task = TaskModel(title=request_data["title"] , user_id=request_data["user_id"])

        db.session.add(new_task)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500 , message="Database error while deleting user")
        return new_task

    
@blp.route("/tasks/<int:task_id>")
class TaskResource(MethodView):

    @blp.response(200 , TaskSchema)
    def get(self ,task_id):
        task  = TaskModel.query.get(task_id)
        if task is None:
            abort(404, message="Task Id not found")
        return task
    
    @blp.arguments(TaskUpdateSchema)
    @blp.response(200 ,TaskSchema)
    def put(self ,request_data ,task_id ):
        task = TaskModel.query.get(task_id)

        if task is None:
            abort(404 ,message="Task id not found")
        
        task.title = request_data["title"]

        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500 , message="Database error while deleting user")
        return task

    @blp.response(200)
    def delete(self ,task_id):
        task = TaskModel.query.get(task_id)

        if task is None:
            abort(404 , message="Task Id not found")
        db.session.delete(task)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500 , message="Database error while deleting user")

        return {"message": "User has been deleted successfully"}