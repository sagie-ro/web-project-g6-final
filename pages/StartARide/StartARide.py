from flask import Blueprint, render_template, redirect, url_for, session, request
from utilities.Models.RideModel import rideModel
# homepage blueprint definition
startaride = Blueprint('StartARide', __name__,
                       static_folder='static',
                       static_url_path='/StartARide',
                       template_folder='templates')


# Routes
@startaride.route('/StartARide')
def index():
    if "user" not in session:
        return redirect(url_for('homepage.index'))
    return render_template('StartARide.html', current_user=session["user"])

@startaride.route('/StartARide', methods=["POST"])
def addRide():
    driver = session["user"]
    date = request.form["datetime"]
    origin = request.form["origin"]
    destination = request.form["destination"]
    price = request.form["price"]
    seats = request.form["seats"]
    animals = True if request.form.get("animals") else False
    mask = True if request.form.get("masks") else False
    smoke = True if request.form.get("smoke") else False
    msg = request.form["message"]
    result = rideModel.AddRide(driver, date, origin, destination,price,seats, animals,mask,smoke,msg)
    if result>0:
        return render_template("success.html", msg="Your ride has been added", current_user=session["user"] if "user" in session else None)
    else:
        return render_template("success.html", msg="Could not add ride, try again", current_user=session["user"] if "user" in session else None)