from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
jointheride = Blueprint('JoinTheRide', __name__,
                        static_folder='static',
                        static_url_path='/JoinTheRide',
                        template_folder='templates')


# Routes
@jointheride.route('/')
def index():
    return render_template('JoinTheRide.html')

