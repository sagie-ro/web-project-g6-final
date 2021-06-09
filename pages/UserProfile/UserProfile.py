from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
userprofile = Blueprint('UserProdile', __name__,
                       static_folder='static',
                       static_url_path='/UserProfile',
                       template_folder='templates')


# Routes
@userprofile.route('/UserProfile')
def index():
    return render_template('UserProfile.html')

