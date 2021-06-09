from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## aboutus
from pages.AboutUs.aboutus import aboutus
app.register_blueprint(aboutus)

## About
from pages.about.about import about
app.register_blueprint(about)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

## Contacts
from pages.Contacts.Contacts import contacts
app.register_blueprint(contacts)

## JoinTheRide
from pages.JoinTheRide.JoinTheRide import jointheride
app.register_blueprint(jointheride)

## RankDriver
from pages.RankDriver.RankDriver import rankdriver
app.register_blueprint(rankdriver)

## RankPassenger
from pages.RankPassenger.RankPassenger import rankpassenger
app.register_blueprint(rankpassenger)

## RankUs
from pages.RankUs.RankUs import rankus
app.register_blueprint(rankus)

## SearchResults
from pages.SearchResults.SearchResults import searchresults
app.register_blueprint(searchresults)

## SignIn
from pages.SignIn.SignIn import signin
app.register_blueprint(signin)

## StartARide
from pages.StartARide.StartARide import startaride
app.register_blueprint(startaride)


## UserProfile
from pages.UserProfile.UserProfile import userprofile
app.register_blueprint(userprofile)




###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)
