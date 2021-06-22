import os

from flask import Flask
from . import db,añadirEmpleado,reconocerFoto
from flask import request

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

# Crea la aplicación


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        cur = db.get_db().cursor()
        cur.execute("INSERT INTO user (id,username, password) VALUES (?,?,?)",
                    ('55', 'diedgo', '12345'))

        db.get_db().commit()

        msg = "Record successfully added"
        return msg

    app.register_blueprint(añadirEmpleado.bpAñadir)
    app.register_blueprint(reconocerFoto.bpReconocer)

    db.init_app(app)

    return app
