from flask import render_template
from apps.authentication import blueprint


@blueprint.route('/login')
def login():
    return render_template( 'accounts/login.html')