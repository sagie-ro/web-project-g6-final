from flask import Blueprint, render_template, redirect, url_for, session, request
from utilities.Models.RateModel import rateModel

# homepage blueprint definition
rankdriver = Blueprint('RankDriver', __name__,
                       static_folder='static',
                       static_url_path='/RankDriver',
                       template_folder='templates')


# Routes
@rankdriver.route('/rankdriver/<ID>/<RideID>')
def index(ID, RideID):
    if "user" not in session:
        return redirect(url_for('homepage.index'))
    return render_template('RankDriver.html', current_user=session["user"])

@rankdriver.route('/rankdriver/<ID>/<RideID>', methods=["POST"])
def rate(ID, RideID):
    rateModel.AddRate(ID, session["user"], RideID, request.form["message"], request.form["rate"])
    return redirect(url_for('MyRecords.index'))
