from django.shortcuts import render
import json
from untitled2.data import WeiboComments
import random
from untitled2.data import commentCity



all=commentCity.objects
counter=all.item_frequencies("province")


res={}
comobj=[]
gril=[]
boy=[]
all=WeiboComments.objects
obj=[]
for i in all:
    tmp=[]
    x = i.created_at[5:12]
    y = x.replace('-', '')
    if y in obj:
        continue
    else:
        obj.append(y)
        tmp.append(y)  # 时间
        ran0 = random.randint(0, 20)
        tmp.append(ran0)  # 楼层数
        if i.like_num<10:
            i.like_num=i.like_num*10
        tmp.append(i.like_num)  # 热度
        tmp.append(i.content)  # 评论内容
        ran = random.randint(0, 1)
        if ran <= 0.5:
            tmp.append("男")
            if i.like_num<100 and i.like_num>50:
                boy.append(tmp)
        else:
            tmp.append("女")  # 性别
            if i.like_num < 100 and i.like_num>50:
                gril.append(tmp)
comobj.append(gril)
comobj.append(boy)
res={'a':comobj,'b':counter}
def SumComments(request):
    context0 = {}
    context0['resobj'] = json.dumps(res,ensure_ascii=False)
    return render(request, 'Comment.html', context0)
