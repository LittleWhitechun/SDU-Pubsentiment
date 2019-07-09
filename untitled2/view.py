from django.shortcuts import render
import json
from untitled2.data import ThemeNews


Topic=[]
Heat=[]
all=ThemeNews.objects
counter1=all.item_frequencies("theme")
for k, v in counter1.items():
    Topic.append(k)
    Heat.append(v)
res = {'a': Topic, 'b': Heat}
def topic(request):
    context1 = {}
    context1['topicheat'] = json.dumps(res,ensure_ascii=False)
    return render(request, 'TopicHeat.html', context1)


