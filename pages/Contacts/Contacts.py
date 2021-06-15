from flask import Blueprint, render_template, redirect, url_for, request, session
from utilities.Models.ContactModel import contactModel

contacts = Blueprint('Contacts', __name__,
                     static_folder='static',
                     static_url_path='/Contacts',
                     template_folder='templates')


# Routes
@contacts.route('/Contacts')
def index():
    current_user = None
    if "user" in session:
        current_user= session["user"]
    return render_template('Contacts.html', current_user=current_user)

@contacts.route('/Contacts', methods=["POST"])
def contactPost():
    name = request.form["name"]
    message = request.form["message"]
    email = request.form["email"]
    result = contactModel.AddContact(name, session["user"], email, message)
    if result>0:
        return render_template("success.html", msg="THANKS FOR APPROACHING US, YOUR MESSAGE IS RECEIVED", current_user=session["user"] if "user" in session else None)
    else:
        return render_template("success.html", msg="Unable to add message, try again", current_user=session["user"] if "user" in session else None)


