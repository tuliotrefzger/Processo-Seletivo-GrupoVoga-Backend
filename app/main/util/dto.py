
from flask_restx import Namespace, fields


class StringJwtDto:
    api = Namespace('stringjwt', description='log related operations')
    stringjwt = api.model('stringjwt', {
        'string': fields.String(required=True, description='string a ser protegida'),
    })

class StringJwtGDto:
    api = Namespace('stringjwt', description='log related operations')
    stringjwt = api.model('stringjwt', {
        'id': fields.Integer(required=True, description='id da string'),
        'string': fields.String(required=True, description='string a ser protegida'),
        'access_token': fields.String(description='token jwt da string'),
        'created_at': fields.String(description='data de criação da string'),
        'deleted_at': fields.String(description='data de deleção da string'),
        'update_at': fields.String(description='data de atualização da string'),
        'delete_flag': fields.Boolean(description='condição atual da string')
    })