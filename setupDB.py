import pymongo
# client = pymongo.MongoClient("mongodb+srv://utkarsh:<password>@cluster0-qrht7.mongodb.net/test?retryWrites=true&w=majority")
# db = client.test
from flask import Flask, jsonify, request, render_template, url_for
from flask_pymongo import PyMongo
from urllib.request import Request, urlopen
import urllib 
import json


def setupDatabase():
    mongo_uri = "mongodb+srv://utkarsh:Utk2001@cluster0-qrht7.mongodb.net/test?retryWrites=true&w=majority"
    myclient = pymongo.MongoClient(mongo_uri)
    mydb = myclient["mydatabase"]
    mycol = mydb["reddit_data"]
    #mycol.remove()
    #result= mycol.delete_many({})

    hdr = {'User-Agent': 'osx:r/relationships.single.result:v1.0 (by /u/goodwillhunter01)'}
    url = 'https://www.reddit.com/r/india/.json?limit=100'
    req = Request(url)
    req.add_header('User-Agent', 'osx:r/relationships.single.result:v1.0 (by /u/goodwillhunter01)')
    content = urlopen(req).read()
    data = json.loads(content)
    data_all = data["data"]['children']
    while (len(data_all) <= 1000):
        #time.sleep(2)
        last = data["data"]["after"]
        url = 'https://www.reddit.com/r/india/.json?limit=100&after=%s' % last
        req = Request(url)
        req.add_header('User-Agent', 'osx:r/relationships.single.result:v1.0 (by /u/goodwillhunter01)')
        content = urlopen(req).read()
        data = json.loads(content)
        data_all += data["data"]['children']
    article_title = []
    article_author = []

    article_flairs = []

    article_date = []
    article_comments = []
    article_score = []
    article_ups = []
    article_downs = []

    for i in range(0, len(data_all)):
        article_title.append(data_all[i]['data']['title'])
        article_author.append(data_all[i]['data']['author'])
        article_ups.append(data_all[i]['data']['ups'])
        article_downs.append(data_all[i]['data']['downs'])
        article_flairs.append(data_all[i]['data']['link_flair_text'])
        article_date.append(data_all[i]['data']['created_utc'])
        article_comments.append(data_all[i]['data']['num_comments'])
        article_score.append(data_all[i]['data']['score'])
    for i in range(0, len(data_all)):
        if(str(type(article_flairs[i]))=="<class 'NoneType'>"):
            article_flairs[i]="None"
    
    # article_date_max = max(article_date)
    # article_comments_max = max(article_comments)
    # article_ups_max = max(article_ups)
    # #article_downs_max = max(article_downs)
    # article_date_min = min(article_date)
    # article_comments_min = min(article_comments)
    # article_ups_min = min(article_ups)
    # #article_downs_min = min(article_downs)
    # for i in range(0, len(data_all)):
    #     article_date[i] = (article_date[i] - article_date_min)/(article_date_max - article_date_min)
    #     article_comments[i] = (article_comments[i] - article_comments_min)/(article_comments_max - article_comments_min)
    #     article_ups[i] = (article_ups[i] - article_ups_min)/(article_ups_max - article_ups_min)
    #     #article_downs[i] = (article_downs[i] - article_downs_min)/(article_downs_max - article_downs_min)
    
    for i in range(0, len(data_all)):
        mydict = { 'flair':article_flairs[i],
        'title':article_title[i],
        'author':article_author[i],
        'date':abs(article_date[i]-1563000000.0),
        'comments':article_comments[i],
        'score':article_score[i],
        'ups':article_ups[i],
        }
        #print(mydict)
        x = mycol.insert_one(mydict)
        #X.append([article_date[i], article_comments[i], article_ups[i]])



setupDatabase()