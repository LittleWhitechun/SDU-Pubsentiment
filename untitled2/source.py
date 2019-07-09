#coding:utf-8
# from flask import request,Flask,current_app
# from flask_cors import CORS
import json
import csv
import collections
from django.shortcuts import HttpResponse, render, redirect
# app=Flask(__name__)

# @app.route("/source_media_title_by_key",methods=["GET"])
def getSourceTitleByKey(request):
    req_key = request.GET.get('key', default='')
    req_source=request.GET.get('source', default='')
    print(req_key+' '+req_source)
    with open('static/data/news_china.csv', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        res_list = []
        for row in f_csv:
            if (row[1] == req_source):
                for i in range(10):
                    if(row[3+i]==req_key):
                        res_list.append({'title':row[2],'time':row[3],'content':row[2]})
        print(res_list)
        r = HttpResponse(json.dumps(res_list, ensure_ascii=False))
        r['Access-Control-Allow-Origin'] = '*'
        return r

# @app.route("/source_media_key",methods=["GET"])
def getSourcMediaKey(request):
    req_source=request.GET.get('source',default='')
    with open('static/data/news_china.csv',encoding='utf-8') as f:
        f_csv=csv.reader(f)
        key_list=[]
        res_list=[]
        for row in f_csv:
            if(row[1]==req_source):
                for i in range(10):
                    key_list.append(row[3+i])
        res_count=collections.Counter(key_list)
        for key in res_count:
            res_list.append({'name':key,'value':res_count[key]})
        print(res_list)
        r=HttpResponse(json.dumps(res_list,ensure_ascii=False))
        r['Access-Control-Allow-Origin'] = '*'
        return r

# @app.route("/source_news",methods=["GET"])
def getSourceNews(request):
    # req_source=request.args.get('source',default='')
    req_source = request.GET['source']
    with open('static/data/WebData.news_china.json',encoding='utf-8') as f:
        source_list=json.load(f)
        res_list=[]
        for source_item in source_list:
            if source_item['source'] == req_source:
                res_list.append(source_item)
        # return jsonify(res_list)
        r=HttpResponse(json.dumps(res_list,ensure_ascii=False))
        r['Access-Control-Allow-Origin'] = '*'
        return r

# @app.route("/source")
def getSource(request):
    with open('static/data/WebData.news_china.json',encoding='utf-8') as f:
        print(json.load(f))
        r = HttpResponse(json.load(f))
        r['Access-Control-Allow-Origin'] = '*'
        return r

# @app.route("/place")
def getPlace(request):
    with open('static/data/sina_外交.csv',encoding='utf-8') as f:
        f_csv=csv.reader(f)
        res_list=[]
        place_list=[]
        for row in f_csv:
            # print(row[14])
            places=row[14].split('/')
            for p in places:
                place_list.append(p)
            res_list.append(row[14])
        res_obj=collections.Counter(place_list)
        # print(res_obj)
        r=HttpResponse(json.dumps(res_obj,ensure_ascii=False))
        r['Access-Control-Allow-Origin'] = '*'
        return r
#@app.route("/country_relation")
def getRelation(request):
    req_country=request.GET.get('country', default='')
    print("req_country:"+req_country)
    with open('static/data/sina_外交.csv',encoding='utf-8') as f:
        f_csv=csv.reader(f)
        res_list=[]
        place_list=[]
        for row in f_csv:
            # print(row[14])
            places=row[14].split('/')
            if req_country in places:
                print(places)
                for place in places:
                    if place !=req_country:
                        res_list.append(place)
        res_obj=collections.Counter(res_list)
        print(res_obj)
        r=HttpResponse(json.dumps(res_obj,ensure_ascii=False))
        r['Access-Control-Allow-Origin'] = '*'
        return r
#/manner_by_date        
def getMannerByDate(request):
    req_date=request.GET.get('date', default='')
    print("req_date:"+req_date)
    req_list=[0,0]
    with open('static/data/manner.json',encoding='utf-8') as f:
        fdata=json.load(f)
        for item in fdata:
            itemdate=item['created_at'][0:10]
            if req_date==itemdate:
                if item['opinion_attr']=='pos':
                    req_list[0]+=1*item['tend']
                else:
                    req_list[1]+=1*item['tend']    
    r=HttpResponse(json.dumps(req_list,ensure_ascii=False))
    r['Access-Control-Allow-Origin'] = '*'
    return r

#/theme_content_by_date
def getThemeContentByDate(request):
    req_manner=request.GET.get('manner', default='')
    req_manner='pos' if req_manner=='积极' else 'neg'
    req_date=request.GET.get('date',default='')
    res_obj={}
    res_like=-1
    with open('static/data/manner.json',encoding='utf-8') as f:
        fdata=json.load(f)
        for item in fdata:
            itemdate = item['created_at'][0:10]
            itemmanner=item['opinion_attr']
            itemlike=item['like_num'][-1]
            if res_like<itemlike and req_manner==itemmanner and req_date==itemdate:
                res_like=itemlike
                res_obj['theme']=item['theme']
                res_obj['content']=item['content']
    res_obj['date']=req_date
    r = HttpResponse(json.dumps(res_obj, ensure_ascii=False))
    r['Access-Control-Allow-Origin'] = '*'
    return r

def getMannerByMonth(request):
    req_month = request.GET.get('date', default='')
    print("req_month:" + req_month)
    res_obj = {}
    with open('static/data/manner.json', encoding='utf-8') as f:
        fdata=json.load(f)
        for i in range(1,31):
            for item in fdata:
                itemdate = item['created_at'][0:10]
                curdate=''
                if i <= 9:
                    curdate=req_month+'-0'+i
                else:
                    curdate=req_month+'-'+i
                if curdate == itemdate:
                    res_obj[curdate]=[0,0]
                    if item['opinion_attr'] == 'pos':
                        res_obj[curdate][0] += 1 * item['tend']
                    else:
                        res_obj[curdate][1] += 1 * item['tend']
    r = HttpResponse(json.dumps(res_obj, ensure_ascii=False))
    r['Access-Control-Allow-Origin'] = '*'
    return r


