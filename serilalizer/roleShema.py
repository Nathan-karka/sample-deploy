from marshmallow import fields
from app import ma
from enum import Enum

class StatusEnum(Enum):
    active = 'active'
    inactive = 'inactive'



class IsdeletedEnum(Enum):
    false = '0'
    true = '1'



class RoleSchema(ma.Schema):
    id = fields.Int()
    name = fields.Str()
    status = fields.Str()
    is_deleted = fields.Str()
    created_at = fields.DateTime()
    created_by = fields.Str()
    updated_at = fields.DateTime()