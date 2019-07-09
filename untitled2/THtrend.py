from collections import Counter
from django.http import JsonResponse
from untitled2.data import ThemeNews


# 点击的主题的热度变化趋势（随时间）

def trend(request):
    request.encoding = 'utf-8'
    if request.is_ajax():
        heatTrend = request.GET.get('heatTrend')
        print("所选主题：" + heatTrend)
        Times = []
        NewTimes = []
        top1 = ThemeNews.objects(theme=heatTrend)
        for i in top1:
            Times.append(i.time)
        for u in Times:
            tmp = u[0:12]  # 只截取年月日部分
            tmp2 = tmp.replace('-', '/')
            NewTimes.append(tmp2)
        print(NewTimes)
        print(Times)
        counter = Counter(NewTimes)
        Time = []
        Num = []
        for k, v in counter.items():
            Time.append(k)
            Num.append(v)
        res = {'a': Time, 'b': Num}
        jsondata = {'timedata': res}
        return JsonResponse(jsondata)
