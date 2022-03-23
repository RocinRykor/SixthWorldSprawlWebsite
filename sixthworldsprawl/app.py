from config import Config
from flask import Flask, Request
from flask_migrate import Migrate
from routes.general import general
from routes.admin import admin
from models import db
# from flask_statistics import Statistics


migrate = Migrate()
# statistics = Statistics()


def check_user():
    """
    A function that can be used to do some form of authentication for user
    login to view the statistics page. Currently this just returns True,
    which is no check at all, but you can add this in later.
    """
    return True


def build_app():

    app = Flask(__name__)
    app.config.from_object(Config())
    app.register_blueprint(general)
    app.register_blueprint(admin)
    db.init_app(app)
    migrate.init_app(app, db)
    # statistics.init_app(app, db, Request, check_user)

    return app


application = build_app()


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")
