import jwt
from app import app

def createAccesstoken(data):
    token = jwt.encode(data, app.config['SECRET_KEY'], algorithm="HS256")