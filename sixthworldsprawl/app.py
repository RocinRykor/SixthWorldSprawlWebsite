from .config import Config
from . import models
from flask import Flask, redirect
from flask_login import LoginManager
from flask_migrate import Migrate
#from .routes.general import general
#from .routes.admin import admin
#from .routes.auth import auth
# from flask_statistics import Statistics


db = models.db

# Create any items that will be used in the app
User = models.User
Character = models.Character

migrate = Migrate()
login_manager = LoginManager()
# statistics = Statistics()


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter_by(id=user_id).first()


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
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app, db)
    # statistics.init_app(app, db, Request, check_user)

    with app.app_context():
        from .routes.general import general
        from .routes.auth import auth
        from .routes.api.characters.character_api_routes import characters_api

        app.register_blueprint(general)
        app.register_blueprint(auth)
        app.register_blueprint(characters_api)

        print("Creating")
        db.create_all()
        print("done")

    return app


application = build_app()


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")
