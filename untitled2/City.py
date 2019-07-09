from django.shortcuts import render
import json
from untitled2.data import commentCity



all=commentCity.objects
counter=all.item_frequencies("province")

def cityDis(request):
    print(counter)
    context1 = {}
    context1['cityDis'] = json.dumps(counter, ensure_ascii=False)
    return render(request, 'Comment.html', context1)

