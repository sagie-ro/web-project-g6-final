from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
rankdriver = Blueprint('RankDriver', __name__,
                       static_folder='static',
                       static_url_path='/RankDriver',
                       template_folder='templates')


# Routes
@rankdriver.route('/rankdriver')
def index():
    return render_template('RankDriver.html')

