from flask import Blueprint, render_template, redirect, url_for, session
from utilities.Models.ContactModel import ContactModel


# homepage blueprint definition
myMessages = Blueprint('myMessages', __name__,
                       static_folder='static',
                       static_url_path='/myMessages',
                       template_folder='templates')


# Routes
@myMessages.route('/myMessages/')
def index():
    current_user = session["user"]
    if "user" not in session:
        return redirect(url_for('homepage.index'))
    # query = "SELECT contact.ID AS ID,  contact.Message AS Message,  FROM  contact WHERE contact.ID  = '%s'" % ID
    # query = "SELECT * from contact"
    # queryResult =  interact_db(query, 'fetch')
    # return render_template('myMessages.html', current_user=session["user"], messageList=queryResult)
    queryResult = list(ContactModel.ViewMyMessages(current_user))
    return render_template('myMessages.html', current_user=current_user, messageList=queryResult)


@myMessages.route('/deleteMessage')
def delete(ID):
    ContactModel.deleteMessage(ID)
    return redirect('/myMessages')
