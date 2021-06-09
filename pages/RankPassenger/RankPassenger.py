from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
rankpassenger = Blueprint('RankPassenger', __name__,
                       static_folder='static',
                       static_url_path='/RankPassenger',
                       template_folder='templates')


# Routes
@rankpassenger.route('/rankpassenger')
def index():
    return render_template('RankPassenger.html')

