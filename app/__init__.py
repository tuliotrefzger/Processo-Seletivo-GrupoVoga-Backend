from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='PROCESSO SELETIVO GRUPO VOGA -- BACKEND ',
          version='0.0.1',
          description='A boilerplate for flask restx web service.'
          )

api.add_namespace(user_ns, path='/')