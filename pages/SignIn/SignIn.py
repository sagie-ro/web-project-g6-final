from flask import Blueprint, render_template, redirect, url_for, session, request
from utilities.Models.UserModel import userModel
import re, os, uuid
# homepage blueprint definition
signin = Blueprint('Signin', __name__,
                       static_folder='static',
                       static_url_path='/Signin',
                       template_folder='templates')


# Routes
@signin.route('/SignIn')
def index():
    if "user" in session:
        return redirect(url_for('homepage.index'))
    return render_template('SignIn.html')

@signin.route('/Logout')
def logout():
    session.clear()
    return redirect(url_for('homepage.index'))

@signin.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    result = userModel.Login(email, password)
    if len(result)==0:
        return render_template("success.html", msg="Invalid, try again", current_user=session["user"] if "user" in session else None)
    session["user"] = result[0][0] #result[0][0] means first record and first column that is ID attribute
    return redirect(url_for('homepage.index'))

@signin.route("/signup", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    dob = request.form["bday"]
    fb = request.form["facebook"]
    license = request.form["numLicense"]
    num = request.form["numOfCar"]
    comp = request.form["carCom"]
    model = request.form["carModelr"]
    phone=request.form["phone"]
    profile = upload_file(request.files["profile"])
    result = userModel.Register(name, email, dob, password, fb, license, num, comp, model, phone, profile)
    if result > 0:
        return render_template("success.html", msg="You are registered, please login to continue", current_user=session["user"] if "user" in session else None)
    else:
        return render_template("success.html", msg="Could not create account, try again", current_user=session["user"] if "user" in session else None)

@signin.route('/updateProfile', methods=["GET", "POST"])
def updateProfile():
    if "user" not in session:
        return redirect(url_for("homepage.index"))
    if request.method=="GET":
        user = list(userModel.GetUser(session["user"]))[0]
        return render_template("update_profile.html", current_user=session["user"], user=user)
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    dob = request.form["bday"]
    fb = request.form["facebook"]
    license = request.form["numLicense"]
    num = request.form["numOfCar"]
    comp = request.form["carCom"]
    model = request.form["carModelr"]
    phone=request.form["phone"]
    profile = upload_file(request.files["profile"]) if request.files["profile"] else request.form["profile_val"]
    result = userModel.Update(session["user"], name, email, dob, password, fb, license, num, comp, model, phone, profile)
    if result > 0:
        return redirect(url_for("UserProfile.index", ID=session["user"]))
    else:
        return render_template("success.html", msg="Could not update account, try again", current_user=session["user"] if "user" in session else None)    

def upload_file(file):
    from app import app
    file_folder = os.path.join(app.static_folder,"media")
    ext = file.filename.split('.')
    ext = ext[len(ext)-1]
    #to produce unique file name we use uuid.uuid4
    filename = str(uuid.uuid4())+"."+ext
    #join path folder with ur filname..so that we can save file
    filepath = os.path.join(file_folder, filename)
    # this function will save the file automatically
    file.save(filepath)
    return filename
