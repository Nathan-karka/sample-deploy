from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models.user import User
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required,get_jwt_identity ,current_user
from serilalizer.userSchema import UserShema

authBlueprint = Blueprint("authBlueprint", __name__)
userShema = UserShema() 

@authBlueprint.route('/login', methods = ['POST'])
def login():
    try:
        email = request.get_json()['email']
        password = request.get_json()['password']
        user = User.query.filter_by(email = email).first()
        if not user:
            return jsonify({"status":"user not found"}),404
        
        if not check_password_hash(user.password, password):
            return jsonify({"status":"email and password not match"}),401
        
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        return jsonify({"access_token":access_token, "refresh_token":refresh_token}),200
    except Exception as e:
        return jsonify({'error':str(e)})
    
@authBlueprint.route('/refresh', methods =['POST'])
@jwt_required(refresh = True)
def refresh():
    try:
        user_id = get_jwt_identity()
        access_token = create_access_token(identity = user_id)
        return jsonify({"access_token":access_token})
    except Exception as e:
        return jsonify({"error":str(e)})

@authBlueprint.route('/access', methods=['POST'])
@jwt_required()
def get_user_detail_by_access():
    try:
        id = get_jwt_identity()
        user = User.query.get(id)
        return jsonify({"data":userShema.dump(user)})
    except Exception as e:
        return jsonify({"error":str(e)})
