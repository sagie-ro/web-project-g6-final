from flask import Blueprint, render_template, redirect, url_for, session

# homepage blueprint definition
homepage = Blueprint('homepage', __name__,   
                     static_folder='static',
                     static_url_path='/homepage',
                     template_folder='templates')


# Routes
@homepage.route('/')
def index():
    user = None
    if "user" in session:
        user = session["user"]
    return render_template('homepage.html', current_user = user)


@homepage.route('/homepage')
@homepage.route('/home')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
