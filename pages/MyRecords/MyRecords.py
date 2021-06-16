from flask import Blueprint, render_template, redirect, url_for, session
from utilities.Models.JoinRide import joinRideModel
from utilities.Models.RideModel import rideModel

# homepage blueprint definition
MyRecords = Blueprint('MyRecords', __name__,
                      static_folder='static',
                      static_url_path='/MyRecords',
                      template_folder='templates')


# Routes
@MyRecords.route('/MyRecords')
def index():
    if "user" not in session:
        return redirect(url_for('homepage.index'))
    aspassenger = list(joinRideModel.ViewMyRides(session["user"]))
    asdriver = list(rideModel.ViewMyRides(session["user"]))
    return render_template('myrides.html', current_user=session["user"], asdriver=asdriver, aspassenger=aspassenger)


@MyRecords.route('/markAsEnd/<RideID>')
def mark(RideID):
    rideModel.MarkAsEnd(RideID)
    return redirect(url_for('MyRecords.index'))


@MyRecords.route('/passengers/<RideID>')
def passengers(RideID):
    result = list(joinRideModel.ViewMyPassengers(RideID))
    return render_template('my_passengers.html', current_user=session["user"], passengers=result, RideID=RideID)
