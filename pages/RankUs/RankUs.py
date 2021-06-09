from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
rankus = Blueprint('RankUs', __name__,
                   static_folder='static',
                   static_url_path='/RankUs',
                   template_folder='templates')


# Routes
@rankus.route('/RankUs')
def index():
    return render_template('RankUs.html')
