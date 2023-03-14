from flask import request,make_response, Blueprint, jsonify
from app import db
from models.role import Roles
from serilalizer.roleShema import RoleSchema
import json

router = Blueprint('routes', __name__)
roleSchema = RoleSchema()

@router.route('/roles', methods =['GET','POST'])
def add_get_Role():
    if request.method == 'POST':
        try:
            data = request.get_json()
            role = Roles(**data)
            db.session.add(role)
            db.session.commit()
            return jsonify({'status':'data added successfully'}),200
        except Exception as e:
            return jsonify({'error':str(e)})
        
    elif request.method == 'GET':
        try:
            roles = Roles.query.all()
            return jsonify({'roles':roleSchema.dump(roles, many=True)}),200
        except Exception as e:
            return jsonify({"error":str(e)})
        
@router.route('/roles/<id>', methods = ['GET','DELETE','PUT'])
def get_delete_update_role_by_id(id):
    if request.method == 'GET':
        try:
            role = Roles.query.get(id)
            return jsonify({'role': roleSchema.dump(role)})
        except Exception as e:
            return jsonify({'error':str(e)})
        
    elif request.method == 'PUT':
        try:
            data = request.get_json()
            role = Roles.query.filter_by(id = id).update(data)
            db.session.commit()
            return jsonify({'status':'data updated successfully'})
        except Exception as e:
            return jsonify({'error':str(e)})
    else:
        try:
            role = Roles.query.get(id)
            db.session.delete(role)
            db.session.commit()
            return jsonify({'status':'data deleted successfully'})
        except Exception as e:
            return jsonify({'error':str(e)})



