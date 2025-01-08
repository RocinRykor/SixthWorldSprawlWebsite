from flask import render_template, Blueprint, request
from sixthworldsprawl.forms import MatrixHostForm
from sixthworldsprawl.app import db, Hosts

# from sixthworldsprawl.app import db, User, Character
from sixthworldsprawl.utils.generators.matrix.sheaf_generator.security_sheaf import generate_sheaf

general = Blueprint("general", __name__)


@general.app_errorhandler(404)
def custom_error_page(e):
    return render_template("public/error.html", title="404 - Page Not Found!")


@general.route("/")
@general.route("/index")
@general.route("/home")
def index():
    return render_template("public/index.html", title="Sixth World Sprawl")


@general.route("/roller")
def roller():
    return render_template("public/rollers/diceroller.html", title="Dice Roller")


@general.route("/matrixhost", methods=["GET"])
def matrixhost():
    form = MatrixHostForm(request.form)
    return render_template("public/generators/matrixhost.html", title="Matrix Host Generator",
                           form=form)


@general.route("/matrixhost", methods=["POST"])
def finish_matrixhost():
    form = MatrixHostForm(request.form)

    hostname = form.hostname.data
    provider = form.provider.data
    security_code = form.security_code.data
    system_rating = form.system_rating.data
    access_rating = form.access_rating.data
    control_rating = form.control_rating.data
    file_rating = form.file_rating.data
    index_rating = form.index_rating.data
    slave_rating = form.slave_rating.data
    paydata_points = form.paydata_points.data

    host = Hosts(hostname=hostname, provider=provider, security_code=security_code,
                 system_rating=system_rating, access_rating=access_rating,
                 control_rating=control_rating, file_rating=file_rating,
                 index_rating=index_rating, slave_rating=slave_rating,
                 paydata_points=paydata_points)

    db.session.add(host)
    db.session.commit()

    return render_template("public/generators/matrixhost.html", title="Matrix Host Generator",
                           form=form)


@general.route("/matrixsecurity")
def matrixsecurity():
    sheaf = generate_sheaf(1, 6)  # Generates raw sheaf data as a list of SheafEvent objects

    # Format the sheaf data for clean and human-readable HTML output
    formatted_sheaf = []
    for event in sheaf:
        if event.title:  # Alert level changes
            formatted_sheaf.append(f"Current Step: {event.current_step}<br>Alert Status: {event.title}")
        elif event.ic_list:  # IC program activation
            for ic in event.ic_list:
                formatted_sheaf.append(f"Current Step: {event.current_step}<br>{ic}")
        else:  # Catch-all (potentially unused depending on generation logic)
            formatted_sheaf.append(f"Current Step: {event.current_step}")

    return render_template(
        "public/generators/matrixsecurity.html",
        title="Matrix Security Sheaf Generator",
        sheaf="<br>".join(formatted_sheaf)  # Join the clean format strings into an HTML-safe structure
    )
