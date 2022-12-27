from flask import request, Blueprint, render_template
from flask import redirect
from flask_login import login_required, current_user
from sixthworldsprawl.app import db, User
from sixthworldsprawl.forms import EditUserForm

user = Blueprint("user", "__name__", url_prefix="/user")

@login_required
@user.route("/edit/", methods=["GET"])
def get_edit_user():
    form = EditUserForm(request.form)
    return render_template("/public/users/edituser.html", title="Edit User", form=form)

@login_required
@user.route("/edit/", methods=["POST"])
def edit_user():
    form = EditUserForm(request.form)
    
    # Get the form data
    name = form.name.data
    bio = form.bio.data

    current_user.display_name = name
    current_user.bio = bio
    db.session.commit()
    return redirect("/")