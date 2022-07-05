from flask_restx import Api
from flask import Blueprint

from .main.controller.string_controller import api as string_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTX API BOILER-PLATE WITH JWT',
          version='0.0.1',
          description='a boilerplate for flask restx web service'
          )

api.add_namespace(string_ns, path='/string')