from flask import Blueprint, render_template, redirect, url_for, session, request
from utilities.Models.RideModel import rideModel

# homepage blueprint definition
searchresults = Blueprint('SearchResults', __name__,
                   static_folder='static',
                   static_url_path='/SearchResults',
                   template_folder='templates')


# Routes
@searchresults.route('/SearchResults')
def index():
    if "user" not in session:
        return redirect(url_for('homepage.index'))
    result = list(rideModel.ViewAll())
    return render_template('SearchResults.html', current_user=session["user"], rides=result)

@searchresults.route('/SearchResults', methods=["POST"])
def SearchRide():
    if "user" not in session:
        return redirect(url_for('homepage.index'))
    origin = request.form["origin"]
    destination = request.form["destination"]
    dTime = request.form["datetime"]
    animals = True if request.form.get("animals") else ''
    mask = True if request.form.get("masks") else ''
    smoke = True if request.form.get("smoke") else ''
    result = list(rideModel.ViewRides(origin, destination, dTime, animals, mask, smoke))
    return render_template('SearchResults.html', current_user=session["user"], rides=result)    
