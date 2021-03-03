from app.api import app
from flask_sqlalchemy import SQLAlchemy
from io import StringIO
from app.commons.credentials import user, password, host, port, dbName


def getSessionServer():
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{}:{}@{}:{}/{}".format(
        user, password, host, port, dbName)
    app.config["SQLALCHEMY_POOL_SIZE"] = 5
    app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 31
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy(app)

    return db
