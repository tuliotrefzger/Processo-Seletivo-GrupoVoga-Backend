from flask import request, redirect, render_template
from flask.json import jsonify
from app.main import db
from app.main.model.user import User

def create_user(data):
    data = request.get_json()
    try:
        user_name = data.get("name").upper()
        user_email = data.get("email").lower()
        user_phone_number = data.get("phone_number")
        new_user = User(
            name=user_name, email=user_email, phone_number=user_phone_number
        )
        db.session.add(new_user)
        db.session.commit()
        response_object={
            "status" : "Success",
            "message" : "User created successfully."
        }
        return response_object
    except Exception as e:
        # print(e)
        return "There was an issue adding this user"

def get_user_by_id(id):
    try:
        user = User.query.filter_by(id=id).first()
        return user
    except:
        return "There was an issue finding this user"

def get_all_users():
    try:
        users = User.query.all()
        return users
    except:
        return "There was an issue finding the users"

def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        response_object={
            "status" : "Success",
            "message" : "User deleted successfully."
        }
        return response_object
    except:
        return "There was an issue deleting this user"

def update_user(id, data):
    data = request.get_json()
    try:
        user = User.query.filter_by(id=id).first()
        user.name = data.get("name").upper()
        user.email = data.get("email").lower()
        user.phone_number = data.get("phone_number")
        db.session.commit()
        response_object={
            "status" : "Success",
            "message" : "User updated successfully."
        }
        return response_object
    except:
        return "There was an issue updating this user"
