from flask import flash


def flash_form_errors(form, category):
    for field, error in form.errors.items():
        flash(f"{field}: {error[0]}", category)
