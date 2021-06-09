from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
startaride = Blueprint('StartARide', __name__,
                       static_folder='static',
                       static_url_path='/StartARide',
                       template_folder='templates')


# Routes
@startaride.route('/StartARide')
def index():
    return render_template('StartARide.html')

