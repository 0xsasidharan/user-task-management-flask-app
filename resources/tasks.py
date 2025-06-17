from flask import request
from flask.views import MethodView
from db import tasks , users
from uuid import uuid4
from flask_smorest import Blueprint , abort
from schemas import TaskSchema, TaskUpdateSchema

blp = Blueprint("Tasks" , __name__ , description="Operations on Tasks")

@blp.route("/tasks")
class TaskListResource(MethodView):
    @blp.response(200 ,TaskSchema(many=True))
    def get(self):
        return list(tasks.values()) 

    @blp.arguments(TaskSchema)
    @blp.response(201, TaskSchema)
    def post(self , request_data):
        # request_data = request.get_json()
        # if "user_id" not in request_data or "title" not in request_data:
        #     return {"message": "Both user_id and title are required"}, 400

        # allowed_list= ["title" , "user_id"]

        # for key in request_data:
        #     if key not in allowed_list:
        #         return {"message" : f"{key} is not allowed"} , 400
        if (request_data["user_id"] not in users ):
            abort(404 , message="user_id not found")

        task_id = uuid4().hex
        task = {**request_data , "task_id" : task_id}

        tasks[task_id] = task
        return task 

    
@blp.route("/tasks/<string:task_id>")
class TaskResource(MethodView):

    @blp.response(200 , TaskSchema)
    def get(self ,task_id):
        if task_id not in tasks:
            abort(404 , message="task_id not found")
        return tasks[task_id] 
    
    @blp.arguments(TaskUpdateSchema)
    @blp.response(200 ,TaskSchema)
    def put(self ,request_data ,task_id ):

        if task_id not in tasks:
            abort(404 ,message="Task id not found")
        task = {**request_data}

        tasks[task_id].update(task)

        return tasks[task_id] 

    @blp.response(200)
    def delete(self ,task_id):

        if task_id not in tasks:
            abort(404 , message="task_id not found")

        del tasks[task_id]
        return {"message" : "Task deleted successfully"} 
