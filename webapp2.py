if('imports'=='imports'):
    from flask import Flask, jsonify, request, render_template, url_for
    from flask_pymongo import PyMongo
    import json
    import time
    from urllib.request import Request, urlopen
    import pprint 
    import pymongo
    import numpy as np
    import pandas as pd
    import sklearn
    from sklearn.naive_bayes import BernoulliNB
    from sklearn.naive_bayes import GaussianNB
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.model_selection import train_test_split
    from sklearn import metrics
    from sklearn.metrics import accuracy_score
    import pygal

app = Flask(__name__)
mongo = pymongo.MongoClient("mongodb+srv://utkarsh:Utk2001@cluster0-qrht7.mongodb.net/test?retryWrites=true&w=majority")
db = pymongo.database.Database(mongo, 'mydatabase')
col = pymongo.collection.Collection(db, 'reddit_data')



@app.route("/")
def hello():
    return render_template('accuracy.html', accuracy_percent=str(getaccuracy())+"%")


def getaccuracy():
    X = []
    y = []
    #framework = mongo.db.reddit_data
    framework = col
    for q in framework.find():
        X.append([abs(q['date']), q['comments'], q['ups']])
        y.append(q['flair'])
    #print(y)
    # for i in range(len(X)):
    #     print(X[i], y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    #NB = MultinomialNB()
    NB = GaussianNB()
    #NB = BernoulliNB(binarize=True)
    try:
        NB.fit(X_train, y_train)
    except ValueError:
        print(X_train)
    NB.fit(X_train, y_train)
    y_pred = NB.predict(X_test)
    # for i in range(len(y_pred)):
    #     print(y_pred[i], y_test[i])
    return int(accuracy_score(y_test, y_pred)*100)
    #return render_template(accuracy.html)


def predictFlair(url):
    hdr = {'User-Agent': 'osx:r/relationships.single.result:v1.0 (by /u/goodwillhunter01)'}
    #url = 'https://www.reddit.com/r/india/.json?limit=100'
    url = url + ".json"
    req = Request(url)
    req.add_header('User-Agent', 'osx:r/relationships.single.result:v1.0 (by /u/goodwillhunter01)')
    content = urlopen(req).read()
    data = json.loads(content)
    data_all = data[0]["data"]['children']
    X_input = [abs(data_all[0]['data']['created_utc']-1563000000.0), data_all[0]['data']['num_comments'], data_all[0]['data']['ups']]
    X = []
    y = []
    #framework = mongo.db.reddit_data
    framework = col
    for q in framework.find():
        X.append([abs(q['date']), q['comments'], q['ups']])
        y.append(q['flair'])
    NB = MultinomialNB()
    NB.fit(X, y)
    y_pred = NB.predict([X_input])
    return str(y_pred[0])

@app.route('/', methods=['POST'])
def my_form_post():
    url = request.form['url']
    pred = predictFlair(url)
    return render_template('accuracy.html', accuracy_percent=str(getaccuracy())+"%", pred=pred)

@app.route("/graphs")
def generateGraph():
    line_chart = pygal.Bar()
    line_chart.title = 'number of comments and upvotes for each flair'
    flairs_c = {}
    flairs_u = {}
    flairlist = []
    arr_comments = []
    arr_upvotes = []
    #framework = mongo.db.reddit_data
    framework = col
    for q in framework.find():
        if(q['flair'] in flairs_c):
            flairs_c[q['flair']] = flairs_c[q['flair']] + int(q['comments'])
        else:
            flairs_c[q['flair']] = int(q['comments'])
        if(q['flair'] in flairs_u):
            flairs_u[q['flair']] = flairs_u[q['flair']] + int(q['ups'])
        else:
            flairs_u[q['flair']] = int(q['ups'])
    for x in flairs_u:
        flairlist.append(x)
        arr_upvotes.append(flairs_u[x])
        arr_comments.append(flairs_c[x])
    line_chart.x_labels = flairlist
    line_chart.add('num_comments', arr_comments)
    line_chart.add('uppvotes', arr_upvotes)
    
    graph_data = line_chart.render_data_uri()
    return render_template('graph.html', graph_data=graph_data)


# client = pymongo.MongoClient("mongodb+srv://utkarsh:<password>@cluster0-qrht7.mongodb.net/test?retryWrites=true&w=majority")
# db = client.test

# app.config['MONGO_DBNAME'] = 'mydatabase'
# app.config["MONGO_URI"] = "mongodb+srv://utkarsh:Utk2001@cluster0-qrht7.mongodb.net/test?retryWrites=true&w=majority"

# mongo = PyMongo(app)


# hszdsjkjx

# if __name__ == '__main__':
#     app.run(debug=True)