from flask import request
from flask_restx import Resource

from ..util.dto import StringJwtDto, StringJwtGDto
from ..service.jwt_encode_service import get_encoded_strings, jwt_encode_service

api = StringJwtDto.api
_stringjwt = StringJwtDto.stringjwt
apiGet = StringJwtGDto.api
_stringjwtGet = StringJwtGDto.stringjwt



@api.route('/')
class LogList(Resource):
    @api.doc('list_of_registered_stringjwt')
    @api.marshal_list_with(_stringjwtGet, envelope='data')
    def get(self):
        """List all registered logs"""
        return get_encoded_strings()

    @api.response(201, 'Log sucessfully created.')
    @api.doc('Create a new Log')
    @api.expect(_stringjwt, validate=True)
    def post(self):
        """Create a new Log"""
        data = request.json
        return jwt_encode_service(data)