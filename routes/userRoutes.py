from flask import jsonify, request, Blueprint
from models.user import User
from app import db
from serilalizer.userSchema import UserShema
from werkzeug.security import generate_password_hash

userBlueprint = Blueprint("userBlueprint", __name__)
userShema = UserShema()

@userBlueprint.route('', methods = ['GET',"POST"])
def add_get_user():
    if request.method == 'POST':
        try:
            data = request.get_json()
            user_exists = User.query.filter_by(email = data['email']).first()
            # if user_exists:
            #     return jsonify({"error":"email is already exists"}),
            data['password'] = generate_password_hash(data['password'])
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            return jsonify({"status":"user added successfully"}),200
        except Exception as e:
            print(type(e))
            return jsonify({'error':str(e)})
    else:
        try:
            users = User.query.all()
            return jsonify({"users":userShema.dump(users, many=True)})
        except Exception as e:
            return jsonify({"error":str(e)})
        
@userBlueprint.route('/<id>', methods = ['GET', 'PUT', 'DELETE'])
def get_update_detete_user_by_id(id):
    if request.method == 'GET':
        try:
            user = User.query.get(id)
            return jsonify({"user": userShema.dump(user)})
        except Exception as e:
            return jsonify({"error": str(e)})
    elif request.method == 'PUT':
        try:
            data = request.get_json()
            if data['password']:
                data['password'] = generate_password_hash(data['password'])
            user = User.query.filter_by(id = id).update(data)
            db.session.commit()
            return jsonify({"status": "user data updated successfully"})
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        try:
            user = User.query.get(id)
            db.session.delete(user)
            db.session.commit()
            return jsonify({"status":"user record deleted successfully"})
        except Exception as e:
            return jsonify({'error': str(e)})