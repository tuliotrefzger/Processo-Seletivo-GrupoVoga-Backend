from flask import request
from flask_restx import Resource
from app.main.service.user_service import *
from app.main.util.dto import *

api = UserDto.api
_user = UserDto.user
_user_get = UserDtoGet.user_get

@api.route("/")
class CreateUser(Resource):
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return create_user(data=data)

@api.route("/get_user_by_id/<int:id>")
@api.param("id")
class GetUserById(Resource):
    @api.marshal_with(_user_get)
    def get(self, id):
        return get_user_by_id(id)
