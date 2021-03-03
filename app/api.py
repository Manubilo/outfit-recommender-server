from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins : " *"}})

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


# Resources
api.add_resource(OutfitResourceGenerate, "/outfit/generate")
