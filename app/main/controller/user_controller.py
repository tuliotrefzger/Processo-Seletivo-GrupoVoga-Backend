from flask import request
from flask_restx import Resource
from app.main.service.user_service import *
from app.main.util.dto import *

api = UserDto.api
_user = UserDto.user
_user_get = UserDtoGet.user_get

@api.route("create_user")
class CreateUser(Resource):
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return create_user(data=data)

@api.route("get_user_by_id/<int:id>")
class GetUserById(Resource):
    @api.marshal_with(_user_get)
    def get(self, id):
        return get_user_by_id(id=id)

@api.route("get_all_users")
class GetAllUsers(Resource):
    @api.doc("Gets all users")
    @api.marshal_with(_user_get)
    def get(self):
        return get_all_users()

@api.route("delete_user/<int:id>")
class DeleteUser(Resource):
    @api.doc("Deletes a user")
    def delete(self, id):
        return delete_user(id=id)

@api.route("update_user/<int:id>")
class CreateUser(Resource):
    @api.expect(_user, validate=True)
    def put(self, id):
        data = request.json
        return update_user(id=id, data=data)
