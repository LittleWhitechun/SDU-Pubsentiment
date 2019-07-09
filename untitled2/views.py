from django.shortcuts import render
from untitled2.data import ThemeData
from untitled2.data import InformationData
from untitled2.data import CommentData
import json
import random
import jieba.analyse
from datetime import datetime
from operator import itemgetter

# Create your views here.

# EventWordCloud模块
############################################################################
# 将二组所得数据记录对象转换为字典
# 先读入所有数据，然后统计词频
# 返回值为字典列表
def toThemeDicts(objs):
    # 记录所有分词
    word_list = []
    for obj in objs:
        word_list.append(obj.key1)
        word_list.append(obj.key2)
        word_list.append(obj.key3)
        word_list.append(obj.key4)
        word_list.append(obj.key5)
        word_list.append(obj.key6)
        word_list.append(obj.key7)
        word_list.append(obj.key8)
        word_list.append(obj.key9)
        word_list.append(obj.key10)

    # 统计分词词频
    word_dict = {}
    for word in word_list:
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    # 变成json需要的格式
    json_arr = []
    for key in word_dict.keys():
        tmp = {}
        tmp['name'] = key
        tmp['value'] = word_dict[key]
        json_arr.append(tmp)

    # 返回keys为name value的字典数组
    return json_arr

# 向EventWordCloud界面传送数据，数据为json数组的格式
def EventWordCloud(request):
    #theme =  request.GET.get('theme')
    theme = "中美贸易影响"
    print("eventwc:", theme)
    all_objs = ThemeData.objects(module=theme)
    json_arr = toThemeDicts(all_objs)
    json_post = json.dumps(json_arr, ensure_ascii=False)
    context = {}
    context['data'] = json_post
    return render(request,'EventWordCloud.html',context)
    #return HttpResponse(json_post,content_type='application/json')
    #return render(request, 'EventWordCloud.html',json_arr)
    #return JsonResponse(json_arr, safe=False)

##################################################################################################


# 主题相关图模块
##################################################################################################
# 计算主题之间的相似度
def computeSimilarity_Jaccard(objs, keyword_id):
    # 得到每个主题下的关键词列表
    mod_num = {} # 字典：key是主题名，value是数目
    module_list = [] # 二维数组，与mod_num的主题名顺序一一对应，存放的是每个主题下的所有关键词
    field_id = keyword_id
    keyword=""
    #if field_id==1:
    #    keyword = "外交"
    for obj in objs:
        #if obj.keyword==keyword:
        mod = obj.module
        #print("mod:", mod)
        if mod not in mod_num.keys():
            mod_num[mod] = 1
            word_list = []
            word_list.append(obj.key1)
            word_list.append(obj.key2)
            word_list.append(obj.key3)
            word_list.append(obj.key4)
            word_list.append(obj.key5)
            word_list.append(obj.key6)
            word_list.append(obj.key7)
            word_list.append(obj.key8)
            word_list.append(obj.key9)
            word_list.append(obj.key10)
            module_list.append(word_list)
            #print("1", module_list)
        else:
            mod_num[mod] += 1
            index = list(mod_num.keys()).index(mod)
            module_list[index].append(obj.key1)
            module_list[index].append(obj.key2)
            module_list[index].append(obj.key3)
            module_list[index].append(obj.key4)
            module_list[index].append(obj.key5)
            module_list[index].append(obj.key6)
            module_list[index].append(obj.key7)
            module_list[index].append(obj.key8)
            module_list[index].append(obj.key9)
            module_list[index].append(obj.key10)
            #print("2",module_list)

    # 计算杰卡德相似度
    sim = [] # 两两之间的相似度
    for i in module_list:
        sim_i = [] # i与其他所有主题的相似度
        for j in module_list:
            word_list_ij = i + j
            word_set_ij = set(word_list_ij)
            total_num = len(word_list_ij)
            set_num = len(word_set_ij)
            sim_ij = (total_num - set_num) / total_num
            sim_i.append(sim_ij)
        sim.append(sim_i)

    #print(module_list)
    #print(mod_num)
    #print(sim)
    return sim,mod_num

def computeSimilarity_tfidf(objs):
    pass

# 计算主题之间的相似度并向ThemeRelationGraph传送数据，数据为json数组
def ThemeRelationGraph(request):
    context = {}
    context['data_name'] = {}
    context['links'] = {}
    id = request.GET.get('txt')
    print("haha",id)
    if request.is_ajax():
        d = request.POST
        print(d)
        field_id = request.POST.get('target')
        print(field_id)
    all_objs = ThemeData.objects.all()
    sim_all,mod_num = computeSimilarity_Jaccard(all_objs, id)
    #print(sim_all)
    #print(mod_num)

    # data需要的内容：name x y，这里横纵坐标用随机数生成
    data = []
    for name in list(mod_num.keys()):
        tmp_i = {}
        tmp_i['name'] = name
        tmp_i['x'] = random.randint(10,600)
        tmp_i['y'] = random.randint(10,600)
        data.append(tmp_i)
    print("relations:----------")
    print(data)
    json_data_name = json.dumps(data,ensure_ascii=False)
    context['data_name'] = json_data_name # 是一个数组

    # link需要的内容，比较复杂：
    sou_tar = []
    mod_name = list(mod_num.keys())
    for i in range(len(mod_name)):
        for j in range(len(mod_name)):
            tmp_i = {} # 与第i个主题相关的主题
            #print("sim_ij",sim_all[i][j])
            if sim_all[i][j] > 0.6 and i!=j:
                tmp_i['source'] = mod_name[i]
                tmp_i['target'] = mod_name[j]
                sou_tar.append(tmp_i)
    json_links = json.dumps(sou_tar, ensure_ascii=False)
    context['links'] = json_links
    #print(sou_tar)
    return render(request, 'ThemeRelationGraph.html', context)

###########################################################################################################


# 微博评论用户地域分布显示模块
###########################################################################################################
# 好吧改不了名字就先这样吧
# 向地图页面传递评论用户的地点和数量
# 返回的值是{name: "",value:1}的形式
def CommentWordCloud(request):
    theme = request.GET.get('theme')
    data = []
    name_value = {}
    cites = ['海门', '鄂尔多斯', '招远', '舟山', '齐齐哈尔', '盐城', '赤峰', '青岛', '乳山', '金昌', '泉州', '莱西', '日照', '胶南', '南通', '拉萨', '云浮', '梅州', '文登', '上海', '攀枝花', '威海', '承德', '厦门', '汕尾', '潮州', '丹东', '太仓', '曲靖', '烟台', '福州', '瓦房店', '即墨', '抚顺', '玉溪', '张家口', '阳泉', '莱州', '湖州', '汕头', '昆山', '宁波', '湛江', '揭阳', '荣成', '连云港', '葫芦岛', '常熟', '东莞', '河源', '淮安', '泰州', '南宁', '营口', '惠州', '江阴', '蓬莱', '韶关', '嘉峪关', '广州', '延安', '太原', '清远', '中山', '昆明', '寿光', '盘锦', '长治', '深圳', '珠海', '宿迁', '咸阳', '铜川', '平度', '佛山', '海口', '江门', '章丘', '肇庆', '大连', '临汾', '吴江', '石嘴山', '沈阳', '苏州', '茂名', '嘉兴', '长春', '胶州', '银川', '张家港', '三门峡', '锦州', '南昌', '柳州', '三亚', '自贡', '吉林', '阳江', '泸州', '西宁', '宜宾', '呼和浩特', '成都', '大同', '镇江', '桂林', '张家界', '宜兴', '北海', '西安', '金坛', '东营', '牡丹江', '遵义', '绍兴', '扬州', '常州', '潍坊', '重庆', '台州', '南京', '滨州', '贵阳', '无锡', '本溪', '克拉玛依', '渭南', '马鞍山', '宝鸡', '焦作', '句容', '北京', '徐州', '衡水', '包头', '绵阳', '乌鲁木齐', '枣庄', '杭州', '淄博', '鞍山', '溧阳', '库尔勒', '安阳', '开封', '济南', '德阳', '温州', '九江', '邯郸', '临安', '兰州', '沧州', '临沂', '南充', '天津', '富阳', '泰安', '诸暨', '郑州', '哈尔滨', '聊城', '芜湖', '唐山', '平顶山', '邢台', '德州', '济宁', '荆州', '宜昌', '义乌', '丽水', '洛阳', '秦皇岛', '株洲', '石家庄', '莱芜', '常德', '保定', '湘潭', '金华', '岳阳', '长沙', '衢州', '廊坊', '菏泽', '合肥', '武汉', '大庆']
    objs = InformationData.objects.all()
    for obj in objs:
        city = obj.city
        if city in cites:
            if city not in list(name_value.keys()):
                name_value[city] = 1
            else:
                name_value[city] += 1
    for i in list(name_value.keys()):
        tmp = {}
        tmp['name'] = i
        tmp['value'] = name_value[i]
        data.append(tmp)
    context = {}
    context['data'] = data
    return render(request,'CommentWordCloud.html',context)
###########################################################################################################




# 微博用户行为统计分析模块
###########################################################################################################
def WeiboPostTime(objs):
    postTime_list = []
    time_value = {}
    for obj in objs:
        time = obj.created_at
        year = time[0:4]
        month = time[5:7]
        day = time[8:10]
        hour = time[11:14]
        date = year + month + day
        week = datetime.strptime(date,"%Y%m%d").weekday()
        idt = str(week) + "_" + hour
        if idt not in list(time_value.keys()):
            time_value[idt] = 0
        else:
            time_value[idt] += 1

    for item in list(time_value.keys()):
        tmp = []
        index_ = item.index('_')
        week = int(item[0:index_])
        hour = int(item[index_+1:-1])
        count = time_value[item]
        tmp.append(week)
        tmp.append(hour)
        tmp.append(count)
        postTime_list.append(tmp)
    #print("time_value",time_value)
    #print("post_time",postTime_list)
    return postTime_list


###########################################################################################################
# 微博评论用户区域评论热词词云模块
###########################################################################################################
def RegionCommentWC(request):
    city = request.GET.get('city')
    objs = InformationData.objects(city=city)
    id = []
    for obj in objs:
        id.append(obj._id)
    comments = ""
    for user in id:
        tmp_o = CommentData.objects(comment_user_id=user)
        for i in tmp_o:
            comments += i.content

    keywords = jieba.analyse.extract_tags(comments, topK=100, withWeight=True,allowPOS=())
    data = []
    for item in keywords:
        print(item[0], item[1])
        tmp = {}
        tmp['name'] = item[0]
        tmp['value'] = int(item[1]*100)
        data.append(tmp)

    objs = CommentData.objects.all()
    user_objs = InformationData.objects.all()
    postTime = WeiboPostTime(objs)
    # print("postTime",postTime)
    context = {}
    context['data'] = data
    context['postTime'] = postTime
    return render(request, 'RegionCommentWC.html', context)
###########################################################################################################

# 显示给定主题下的所有事件列表模块
###########################################################################################################
def EventForm(request):
    #theme = request.GET.get('theme')
    theme = "中美贸易影响"
    objs = ThemeData.objects(module=theme)
    data = []
    for obj in objs:
        tmp = {}
        tmp['content'] = obj.title
        tmp['url'] = obj.url
        data.append(tmp)
    context = {}
    context['data'] = data
    return render(request, 'EventForm.html', context)
###########################################################################################################

# 评论数量随时间变化趋势模块
###########################################################################################################
def CommentChanging(request):
    return render(request,'CommentChanging.html')
###########################################################################################################

def WeiboUserGender(objs):
    gend = {}
    gend['男'] = 0
    gend['女'] = 0
    for obj in objs:
        gen = obj.gender
        if gen in ['男','女']:
            gend[gen] += 1

    gend_list = []
    dic_m = {}
    dic_m['name'] = "男"
    dic_m['value'] = gend['男']
    gend_list.append(dic_m)
    dic_f = {}
    dic_f['name'] = "女"
    dic_f['value'] = gend['女']
    gend_list.append(dic_f)
    return gend_list

def WeiboUserV(con_objs, user_objs):
    con_fre = con_objs.item_frequencies('comment_user_id') #统计
    top_user = sorted(con_fre.items(), key=itemgetter(1),reverse=True)[:20]
    print(top_user)
    names = []
    for i in top_user:
        tmp_o = user_objs(_id=i[0])
        for j in tmp_o:
            name = j.nick_name
            names.append(name)
    print(names)
    return names

def WeiboUserAnalysis(request):
    objs = CommentData.objects.all()
    user_objs = InformationData.objects.all()
    postTime = WeiboPostTime(objs)
    #print("postTime",postTime)
    gender = WeiboUserGender(user_objs)
    UserV = WeiboUserV(objs, user_objs)

    context = {}
    context['postTime'] = postTime
    context['gender'] = gender
    context['userV'] = UserV
    return render(request,'RegionCommentWC.html', context)
###########################################################################################################

# 测试首页
def search_index(request):
    #context = {}
    #if request.POST:
    #    context['result'] = request.POST['q']
    #    print(context)
    #return render(request, "ThemeRelationGraph.html", context)
    context = {}
    context['field'] = "a"
    return render(request, "TestIndex.html", context)

def index(request):
    return render(request, "index.html")

def source(request):
    return render(request,"source.html")

def manner(request):
    return render(request,"manner.html")

def place(request):
    return render(request,"place.html")

def homepage(request):
    return render(request,"homepage.html")



