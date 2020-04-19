from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from config import Config
from flask_sqlalchemy import SQLAlchemy

from app.security import authenticate, identity
from app.user import UserRegister
from app.item import Item, ItemList

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app) 
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

