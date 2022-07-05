from flask import request
from flask.json import jsonify
from flask_jwt_extended.utils import create_access_token
from app.main import db
from app.main.util.dto import StringJwtDto
from app.main.model.stringjwt import StringJwt

api = StringJwtDto.api

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def jwt_encode_service(data):
    data = request.get_json()
    print(data)
    string_to_encode = data.get('string')
    print(string_to_encode)
    access_token = create_access_token(identity=string_to_encode)
    print(access_token)
    string = StringJwt.query.filter_by(string=string_to_encode).all()
    if not string:
        try:
            new_string = StringJwt(
                string = string_to_encode,
                access_token=access_token
            )
            db.session.add(new_string)
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify('Falha na conexão com o banco de dados.')
            
    return jsonify('String codificada com sucesso.', {'Token':access_token})

def get_encoded_strings():
    try:
        return StringJwt.query.filter_by(delete_flag=False).all()
    except:
        return jsonify('Falha na conexão com o banco de dados.')

def get_string(string):
    try:
        string = StringJwt.query.filter_by(string=string).first()
    except:
        return jsonify('Falha na conexão com o banco de dados.')
    if not string or string.delete_flag:
        api.abort(404)
    else:
        return string

def get_string_by_token(token):
    try:
        string = StringJwt.query.filter_by(access_token=token).first()
    except:
        return jsonify('Falha na conexão com o banco de dados.')
    if not string or string.delete_flag:
        api.abort(404)
    else:
        return string