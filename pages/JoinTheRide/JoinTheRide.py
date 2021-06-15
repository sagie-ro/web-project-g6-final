from flask import Blueprint, render_template, redirect, url_for, session, request
from utilities.Models.JoinRide import joinRideModel
# homepage blueprint definition
jointheride = Blueprint('JoinTheRide', __name__,
                        static_folder='static',
                        static_url_path='/JoinTheRide',
                        template_folder='templates')


# Routes
@jointheride.route('/JoinTheRide/<ID>')
def index(ID):
    if "user" not in session:
        return redirect(url_for('homepage.index'))
    return render_template('JoinTheRide.html', current_user=session["user"])


@jointheride.route('/JoinTheRide/<ID>', methods=["POST"])
def JoinRide(ID):
    pickup = request.form["pickUpSpot"]
    dropoff = request.form["GetOffSpot"]
    message = request.form["message"]
    result = joinRideModel.JoinRide(session["user"], ID, pickup, dropoff, message)
    if result>0:
        return render_template('success.html', msg="You joined the ride", current_user=session["user"] if "user" in session else None)
    else:
        return render_template('success.html', msg="Unable to join, try again", current_user=session["user"] if "user" in session else None)


