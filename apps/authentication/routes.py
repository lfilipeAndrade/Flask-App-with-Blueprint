from flask import render_template
from apps.authentication import blueprint


@blueprint.route('/login')
def login():
    return render_template( 'accounts/login.html')

@blueprint.route('/register')
def register():
    return render_template( 'accounts/register.html')