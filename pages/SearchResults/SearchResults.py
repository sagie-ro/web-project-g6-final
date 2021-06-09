from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
searchresults = Blueprint('SearchResults', __name__,
                   static_folder='static',
                   static_url_path='/SearchResults',
                   template_folder='templates')


# Routes
@searchresults.route('/SearchResults')
def index():
    return render_template('SearchResults.html')
