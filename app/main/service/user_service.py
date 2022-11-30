from flask import request, redirect, render_template
from flask.json import jsonify
from app.main import db
from app.main.model.user import User

def create_user(data):
    data = request.get_json()
    user_name = data.get("name").upper()
    user_email = data.get("email").lower()
    user_phone_number = data.get("phone_number")
    new_user = User(
        name=user_name, email=user_email, phone_number=user_phone_number
    )
    try:
        session.add(new_user)
        session.commit()
        return jsonify(new_user)
    except:
        return "There was an issue adding your user"

def get_user_by_id(id):
    try:
        user = User.query.filter_by(id).first()
        return user
    except:
        return jsonify("There was an issue finding your user")