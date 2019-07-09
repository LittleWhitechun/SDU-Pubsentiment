from django.http import JsonResponse
from collections import Counter
from untitled2.data import ThemeNews

def relations(request):
    request.encoding = 'utf-8'
    if request.is_ajax():
        NameCloud = request.GET.get('NameCloud')
        print("词云主题："+NameCloud)
        Names=[]
        alldata=ThemeNews.objects(theme=NameCloud)
        for i in alldata:
            Names.append(i.name)
        res_list=[]
        for i in Names:
            arr2=i.split('/')
            for item in arr2:
                res_list.append(item)
        print(res_list)
        counter=Counter(res_list)
        print(counter)
        jsondata={'namemsg':counter}
        return JsonResponse(jsondata)

