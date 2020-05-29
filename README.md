# Flair_detector
NEW README ->
Use case -> Flair prediction
Datasource -> reddit api

Technology/framework for each concrete -
1. Initial data exploration - urllib, json, jupyter notebook
2. ETL - 
3. Feature creation -
4. Model defination -
5. Model training - 
6. Model evaluation - 
7. Model deployment - 


Naming convention

[project_name].data_exp.<technology>.<version>.<extension>
[project_name].etl.<technology>.<version>.<extension>
[project_name].feature_eng.<technology>.<version>.<extension>
[project_name].model_def.<technology>.<version>.<extension>
[project_name].model_train.<technology>.<version>.<extension>
[project_name].model_evaluate.<technology>.<version>.<extension>
[project_name].model_deployment.<technology>.<version>.<extension>
















OLD README ->
URL for heroku app - https://gentle-river-26276.herokuapp.com/

Instructions - 
1. Open the URL given
2. The accuracy of the classification model is reported on the left hand side
3. Put the URL for the post whose flair is to be predicted on the right hand side
4. Click 'submit' and it will show you the predicted flair
5. Open https://gentle-river-26276.herokuapp.com/graphs for Interactive Graph of comments and upvotes of a flair
6. Run setupDB.py to refresh the database with new entries (make sure to clear previous one)

Sources - 
* https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524
* http://pygal.org/en/stable/documentation/output.html#png
* http://t-redactyl.io/blog/2015/11/analysing-reddit-data-part-2-extracting-the-data.html

Approach followed -
1. The data is collected from the reddit/india site and saved in a mongoDB database.
2. The data is then split in testing and training and Naivebayes classification is used to train it.
3. Data is experimented with Gaussian, Multinomial and Bernoulli NaiveBayes.
4. Best is taken and a predict function is made.
5. This function is trained on the whole dataset (1068 entries).
6. It returns the predicted FLAIR which is shown on the webpage.
7. The data collected can also be used for answering questions like which flair gets more upvotes vs which gets more comments.
8. For that particular query, a interactive graph is made using pygal.

Directory Structure -
* Run webapp2.py with flask to test it locally
* Open URL given above to test it on heroku
* /static contains the css files
* /templates contains the html files

Dependencies -
* Flask
* pymongo
* pygal
* scikit-learn
* gunicorn

Codebase -
1. webapp2.py - to run the application
2. setupDB.py -  to setup the mongoDB database

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
