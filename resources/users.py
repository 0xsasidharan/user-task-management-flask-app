from flask.views import MethodView
# from db import users
# from uuid import uuid4
from flask_smorest import Blueprint , abort
from schemas import UserSchema
from models import UserModel
from db import db

blp = Blueprint("Users" , __name__ , description="Operations on users")

@blp.route("/users")
class UserListResource(MethodView):
    @blp.response(200 , UserSchema(many=True))
    def get(self):
        return list(UserModel.query.all())

    @blp.arguments(UserSchema)
    @blp.response(201 ,UserSchema)
    def post(self , request_data):
        new_user = UserModel(name=request_data["name"])
        db.session.add(new_user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500 , message="Database error while creating user")
        return new_user

    
@blp.route("/users/<int:user_id>")
class UserResource(MethodView):
    
    @blp.response(200 , UserSchema)
    def get(self ,user_id):
        user = UserModel.query.get(user_id)
        if user is None:
            abort(404 , message="User Id not found")
        return user
    

    @blp.response(200 )
    def delete(self ,user_id):
        user = UserModel.query.get(user_id)
        if user is None:
            abort(404 , message="User id not found")
        
        db.session.delete(user)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500 , message="Database error while deleting user")

        return {"message": "User has been deleted successfully"}