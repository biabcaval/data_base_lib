import click
import mysql.connector
import os

from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if "db" not in g or not g.db.is_connected():
        # connect to the database
        g.db = mysql.connector.connect(
            host = current_app.config["DB_HOST"],
            user = current_app.config["DB_USER"],
            password = current_app.config["DB_PASSWORD"],
            db = current_app.config["DB_NAME"],
            port = current_app.config["DB_PORT"],
            ssl_disabled=True
        )


    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        # close the database 
        db.close()



def init_app(app):
    app.teardown_appcontext(close_db)
