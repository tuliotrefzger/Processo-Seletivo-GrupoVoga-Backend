
from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user')
    user = api.model('user', {
        'name' : fields.String(required=True, nullable=False),
        'email' : fields.String(required=True, nullable=False),
        'phone_number' : fields.String(required=True, nullable=False),
    })

class UserDtoGet:
    api_get = Namespace('user')
    user_get = api_get.model('user', {
        'name' : fields.String(required=True, nullable=False),
        'email' : fields.String(required=True, nullable=False),
        'phone_number' : fields.String(required=True, nullable=False),
        'id' : fields.Integer(required=False),
        'date_created' : fields.DateTime(required=False),
    })