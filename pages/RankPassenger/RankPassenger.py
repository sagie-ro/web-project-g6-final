from flask import Blueprint, render_template, redirect, url_for, session, request
from utilities.Models.RateModel import rateModel
# homepage blueprint definition
rankpassenger = Blueprint('RankPassenger', __name__,
                       static_folder='static',
                       static_url_path='/RankPassenger',
                       template_folder='templates')


# Routes
@rankpassenger.route('/rankpassenger/<ID>/<RideID>')
def index(ID, RideID):
    if "user" not in session:
        return redirect(url_for('homepage.index'))
    return render_template('RankPassenger.html', current_user=session["user"])

@rankpassenger.route('/rankpassenger/<ID>/<RideID>', methods=["POST"])
def rate(ID, RideID):
    rateModel.AddRate(ID, session["user"], RideID, request.form["message"], request.form["rate"])
    return redirect(url_for('MyRecords.passengers', RideID=RideID))

