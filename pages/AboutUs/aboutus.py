from flask import Blueprint, render_template, redirect, url_for, session

aboutus = Blueprint('aboutus', __name__,
                    static_folder='static',
                    static_url_path='/aboutus',
                    template_folder='templates')


# Routes
@aboutus.route('/aboutus')
def index():
    current_user = None
    if "user" in session:
        current_user= session["user"]
    return render_template('aboutus.html', current_user=current_user)

