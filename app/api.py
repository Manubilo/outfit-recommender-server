

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from flask import Flask, request


app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": " *"}})

from app.models import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


# Resources
api.add_resource(OutfitsResourceCreate, "/outfit/create")
api.add_resource(OutfitsResourceGenerate, "/outfit/generate")
api.add_resource(OutfitsResourceList, "/outfit/list")
api.add_resource(OutfitsResourceGetOne, "/outfit/get_one")
api.add_resource(OutfitsResourceEdit, "/outfit/edit")
api.add_resource(OutfitsResourceDelete, "/outfit/delete")

api.add_resource(MoodsResourceCreate, "/mood/create")
api.add_resource(MoodsResourceList, "/mood/list")
api.add_resource(MoodsResourceGetOne, "/mood/get_one")
api.add_resource(MoodsResourceEdit, "/mood/edit")
api.add_resource(MoodsResourceDelete, "/mood/delete")

api.add_resource(GarmentsResourceCreate, "/garment/create")
api.add_resource(GarmentsResourceList, "/garment/list")
api.add_resource(GarmentsResourceGetOne, "/garment/get_one")
api.add_resource(GarmentsResourceEdit, "/garment/edit")
api.add_resource(GarmentsResourceDelete, "/garment/delete")
