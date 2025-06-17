from flask.views import MethodView
from db import users
from uuid import uuid4
from flask_smorest import Blueprint , abort
from schemas import UserSchema

blp = Blueprint("Users" , __name__ , description="Operations on users")

@blp.route("/users")
class UserListResource(MethodView):
    @blp.response(200 , UserSchema(many=True))
    def get(self):
        return list(users.values()) 

    @blp.arguments(UserSchema)
    @blp.response(201 ,UserSchema)
    def post(self , request_data):
        user_id = uuid4().hex
        user = {**request_data , "user_id" : user_id}
        users[user_id] = user

        return user

    
@blp.route("/users/<user_id>")
class UserResource(MethodView):
    
    @blp.response(200 , UserSchema)
    def get(self ,user_id):
        if user_id not in users:
            abort(404 , message="user_id not found")
        return users[user_id]
    

    @blp.response(200 )
    def delete(self ,user_id):
        if user_id not in users:
            abort(404 , message="user_id not found")
        del users[user_id]

        return {"message" : "User has deleted successfully"}
