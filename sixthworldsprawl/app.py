from flask import Flask, redirect
from flask_login import LoginManager
from flask_migrate import Migrate
from .models.db import data_base as db

from .models import users
from .models import characters
from .models import matrix_hosts

from .config import Config

# Create any items that will be used in the app
User = users.User

Character = characters.Character
Portrait = characters.Portrait
Tag = characters.Tag
PortraitTagLinker = characters.PortraitTagLinker

Hosts = matrix_hosts.Hosts
Data = matrix_hosts.Data
Nodes = matrix_hosts.Nodes


migrate = Migrate()
login_manager = LoginManager()


# statistics = Statistics()


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


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
        # Base Routes
        from .routes.general import general
        from .routes.auth import auth
        from .routes.user import user
        from .routes.character import character
        from .routes.game_rules import rules
        from .routes.calculators import calcs

        app.register_blueprint(general)
        app.register_blueprint(auth)
        app.register_blueprint(user)
        app.register_blueprint(character)
        app.register_blueprint(rules)
        app.register_blueprint(calcs)

        # API Routes
        from .routes.api.characters.character_api_routes import character_api
        from .routes.api.users.user_api_routes import user_api
        from .routes.api.portraits.portrait_api_routes import portrait_api
        from .routes.api.discord.discord_api_routes import bot_api

        app.register_blueprint(character_api)
        app.register_blueprint(user_api)
        app.register_blueprint(portrait_api)
        app.register_blueprint(bot_api)

        print("Creating")
        db.create_all()
        print("done")

    return app


application = build_app()

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")
