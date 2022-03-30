from config import Config
from flask import Flask, redirect
from flask_login import LoginManager
from flask_migrate import Migrate
from routes.general import general
from routes.admin import admin
import models
# from flask_statistics import Statistics


db = models.db

migrate = Migrate()
login_manager = LoginManager()
# statistics = Statistics()


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter_by(userid=user_id).first()


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login/')


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
    login_manager.init_app(app, db)
    # statistics.init_app(app, db, Request, check_user)

    return app


application = build_app()


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")
