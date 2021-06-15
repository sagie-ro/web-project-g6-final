from flask import Blueprint, render_template, redirect, url_for, session
from utilities.Models.UserModel import userModel
# homepage blueprint definition
userprofile = Blueprint('UserProfile', __name__,
                       static_folder='static',
                       static_url_path='/UserProfile',
                       template_folder='templates')


# Routes
@userprofile.route('/UserProfile/<ID>')
def index(ID):
    if "user" not in session:
        return redirect(url_for('homepage.index'))
    result = list(userModel.GetUser(ID))
    if len(result)==0:
        return render_template("success.html", msg="INVALID USER ID", current_user=session["user"] if "user" in session else None)
    return render_template('UserProfile.html', current_user=session["user"], user=result[0])

