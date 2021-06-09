from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
contacts = Blueprint('Contacts', __name__,
                     static_folder='static',
                     static_url_path='/Contacts',
                     template_folder='templates')


# Routes
@contacts.route('/Contacts')
def index():
    return render_template('Contacts.html')

