# -*- coding: utf-8 -*-
from untitled2.data import ThemeNews
from django.http import JsonResponse
from untitled2.data import newscontent


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if request.is_ajax():
        clicktop = request.GET.get('clicktop')
        print(clicktop)
        News = []
        alldata = ThemeNews.objects(theme=clicktop)
        for i in alldata:
            News.append(i.title)
        jsondata = {'msg': News}
        return JsonResponse(jsondata)

def searchContent(request):
    request.encoding = 'utf-8'
    if request.is_ajax():
        cont=request.GET.get('clicktitle')
        print(cont)
        Content = []
        allcon=newscontent.objects(title=cont)
        for u in allcon:
            Content.append(u.content)
        print(Content)
        jsondata2={'tcon':Content}
        return JsonResponse(jsondata2)