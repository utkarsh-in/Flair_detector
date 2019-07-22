# Flair_detector

URL for heroku app - https://gentle-river-26276.herokuapp.com/

Instructions - 
Open the URL given
The accuracy of the classification model is reported on the left hand side
Put the URL for the post whose flair is to be predicted on the right hand side
Click 'submit' and it will show you the predicted flair
Open https://gentle-river-26276.herokuapp.com/graphs for Interactive Graph of comments and upvotes of a flair
Run setupDB.py to refresh the database with new entries (make sure to clear previous one)

Sources - 
https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524
http://pygal.org/en/stable/documentation/output.html#png
http://t-redactyl.io/blog/2015/11/analysing-reddit-data-part-2-extracting-the-data.html

Approach followed -
TBD

Directory Structure -
Run webapp2.py with flask to test it locally
Open URL given above to test it on heroku
/static contains the css files
/templates contains the html files

Dependencies -
Flask
pymongo
pygal
scikit-learn
gunicorn

Codebase -
webapp2.py - to run the application
setupDB.py -  to setup the mongoDB database

PIP libraries used - 
cairocffi==1.0.2
CairoSVG==2.4.0
cffi==1.12.3
Click==7.0
cssselect2==0.2.1
defusedxml==0.6.0
Django==2.1.4
dnspython==1.16.0
Flask==1.1.1
Flask-PyMongo==2.3.0
itsdangerous==1.1.0
Jinja2==2.10.1
joblib==0.13.2
MarkupSafe==1.1.1
numpy==1.16.2
pandas==0.24.2
Pillow==6.1.0
pycparser==2.19
pygal==2.4.0
pymongo==3.8.0
python-dateutil==2.8.0
pytz==2018.7
scikit-learn==0.21.2
scipy==1.3.0
six==1.12.0
sklearn==0.0
tinycss2==1.0.2
virtualenv==16.1.0
virtualenvwrapper-win==1.2.5
webencodings==0.5.1
Werkzeug==0.15.4
gunicorn==19.9.0
