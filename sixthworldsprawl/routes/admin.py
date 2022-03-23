from flask import render_template, Blueprint, redirect, session, request

admin = Blueprint("admin", __name__)


@admin.route("/admin/")
def admin_index():
    return "<h1>This will be the admin page</h1>"
