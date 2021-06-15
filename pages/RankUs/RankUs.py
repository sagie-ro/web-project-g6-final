from flask import Blueprint, render_template, redirect, url_for, request, session
from utilities.Models.RankUsModel import rankUsModel

rankus = Blueprint('RankUs', __name__,
                   static_folder='static',
                   static_url_path='/RankUs',
                   template_folder='templates')


# Routes
@rankus.route('/RankUs')
def index():
    if "user" not in session:
        return redirect(url_for('homepage.index'))
    return render_template('RankUs.html', current_user=session["user"])

@rankus.route('/RankUs', methods=["POST"])
def rankUsPost():
    if "user" not in session:
        return render_template("success.html", msg="Please login to rate us")
    rate = request.form["rate"]
    msg = request.form["message"]
    if rankUsModel.AddRank(session["user"], rate, msg)>0:
        return render_template("success.html", msg="Your Response is received, Thanks for rating us", current_user=session["user"] if "user" in session else None)
    return render_template("success.html", msg="Could not add rate, please try again", current_user=session["user"] if "user" in session else None)