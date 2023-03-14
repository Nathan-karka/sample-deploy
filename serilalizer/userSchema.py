from app import ma 
from marshmallow import fields

class UserShema(ma.Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Str()
    password = fields.Str()
    mobile = fields.Str()
    role_id = fields.Str()
    status = fields.Str()
    is_deleted = fields.Str()
    created_at = fields.DateTime()
    created_by = fields.Str()
    updated_by = fields.DateTime()