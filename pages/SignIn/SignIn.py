from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
signin = Blueprint('Signin', __name__,
                       static_folder='static',
                       static_url_path='/Signin',
                       template_folder='templates')


# Routes
@signin.route('/SignIn')
def index():
    return render_template('SignIn.html')

