from mongoengine import *
import mongoengine

connect('runoobdb', host='127.0.0.1', port=27017)


class ThemeNews(mongoengine.Document):
    _id = mongoengine.StringField()
    source = mongoengine.StringField()
    title = mongoengine.StringField()
    time = mongoengine.StringField()
    url = mongoengine.StringField()
    theme = mongoengine.StringField()
    key1 = mongoengine.StringField()
    key2 = mongoengine.StringField()
    key3 = mongoengine.StringField()
    key4 = mongoengine.StringField()
    key5 = mongoengine.StringField()
    key6 = mongoengine.StringField()
    key7 = mongoengine.StringField()
    key8 = mongoengine.StringField()
    key9 = mongoengine.StringField()
    key10 = mongoengine.StringField()
    name = mongoengine.StringField()
    place = mongoengine.StringField()

    # 集合：news
    meta = {'collection': 'news'}




class WeiboData(mongoengine.Document):
    _id = mongoengine.StringField()
    keyword = mongoengine.StringField()
    crawl_time = mongoengine.StringField()
    weibo_url = mongoengine.StringField()
    user_id = mongoengine.StringField()
    created_at = mongoengine.StringField()
    tool = mongoengine.StringField()
    like_num = mongoengine.StringField()
    repost_num = mongoengine.StringField()
    comment_num = mongoengine.StringField()
    image_url = mongoengine.StringField()
    content = mongoengine.StringField()
    theme = mongoengine.StringField()
    key_word = mongoengine.StringField()
    name = mongoengine.StringField()
    place = mongoengine.StringField()

    meta = {'collection': 'weibo'}


class newscontent(mongoengine.Document):
    _id= mongoengine.StringField()
    crawl_time= mongoengine.StringField()
    source= mongoengine.StringField()
    keyword= mongoengine.StringField()
    title= mongoengine.StringField()
    content= mongoengine.StringField()
    time= mongoengine.StringField()
    url= mongoengine.StringField()
    imgs=mongoengine.ListField()

    meta={'collection':'newscontent2'}

class Newsdata2(mongoengine.Document):
    _id = mongoengine.StringField()
    title = mongoengine.StringField()
    url = mongoengine.StringField()
    module = mongoengine.StringField()
    key1 = mongoengine.StringField()
    key2 = mongoengine.StringField()
    key3 = mongoengine.StringField()
    key4 = mongoengine.StringField()
    key5 = mongoengine.StringField()
    key6 = mongoengine.StringField()
    key7 = mongoengine.StringField()
    key8 = mongoengine.StringField()
    key9 = mongoengine.StringField()
    key10 = mongoengine.StringField()
    name = mongoengine.StringField()
    place = mongoengine.StringField()

    meta={'collection':'newsdata2'}


class WeiboComments(mongoengine.Document):
    _id= mongoengine.StringField()
    crawl_time= mongoengine.StringField()
    weibo_url= mongoengine.StringField()
    comment_user_id= mongoengine.StringField()
    content= mongoengine.StringField()
    like_num= mongoengine.StringField()
    created_at= mongoengine.StringField()
    depth= mongoengine.StringField()
    download_timeout= mongoengine.IntField()
    download_slot= mongoengine.StringField()
    download_latency= mongoengine.StringField()
    head_url= mongoengine.StringField()
    redirect_ttl= mongoengine.StringField()
    redirect_urls= mongoengine.StringField()
    redirect_times= mongoengine.StringField()

    meta={'collection':'comments'}


class commentCity(mongoengine.Document):
    _id = mongoengine.StringField()
    head=mongoengine.StringField()
    crawl_time = mongoengine.StringField()
    nick_name = mongoengine.StringField()
    gender = mongoengine.StringField()
    province = mongoengine.StringField()
    city= mongoengine.StringField()
    birthday= mongoengine.StringField()
    brief_introduction = mongoengine.StringField()
    vip_level = mongoengine.StringField()
    labels = mongoengine.StringField()
    tweets_num = mongoengine.IntField()
    follows_num = mongoengine.IntField()
    fans_num = mongoengine.IntField()
    authentication= mongoengine.StringField()
    sentiment= mongoengine.StringField()
    sex_orientation= mongoengine.StringField()

    meta = {'collection': 'commentCity'}
# # 返回集合里的所有文档对象的列表
# cate = commentCity.objects.all()
#
# # 返回所有符合查询条件的结果的文档对象列表
# for u in cate:
#     print(u.province)



class ThemeData(mongoengine.Document):
    title = mongoengine.StringField()
    url = mongoengine.StringField()
    module = mongoengine.StringField()
    key1 = mongoengine.StringField()
    key2 = mongoengine.StringField()
    key3 = mongoengine.StringField()
    key4 = mongoengine.StringField()
    key5 = mongoengine.StringField()
    key6 = mongoengine.StringField()
    key7 = mongoengine.StringField()
    key8 = mongoengine.StringField()
    key9 = mongoengine.StringField()
    key10 = mongoengine.StringField()
    name = mongoengine.StringField()
    place = mongoengine.StringField()
    age=mongoengine.StringField()

    # 数据库
    meta = {'collection':'test'}

class CommentData(mongoengine.Document):
    comment_user_id = mongoengine.StringField()
    content = mongoengine.StringField()
    weibo_url = mongoengine.StringField()
    created_at = mongoengine.StringField()
    like_num = mongoengine.StringField()
    crawl_time = mongoengine.StringField()
    download_latency= mongoengine.StringField()
    download_slot= mongoengine.StringField()
    depth= mongoengine.StringField()
    head_url= mongoengine.StringField()
    download_timeout= mongoengine.StringField()
    redirect_times= mongoengine.StringField()
    redirect_urls= mongoengine.StringField()
    redirect_ttl= mongoengine.StringField()
    # 数据库
    meta = {'collection':'test_comment'}

class InformationData(mongoengine.Document):
    _id = mongoengine.StringField()
    head = mongoengine.StringField()
    crawl_time =mongoengine.StringField()
    nick_name = mongoengine.StringField()
    gender = mongoengine.StringField()
    province = mongoengine.StringField()
    city = mongoengine.StringField()
    brief_introduction = mongoengine.StringField()
    birthday = mongoengine.StringField()
    vip_level = mongoengine.StringField()
    labels = mongoengine.StringField()
    authentication = mongoengine.StringField()
    tweets_num= mongoengine.StringField()
    follows_num= mongoengine.StringField()
    fans_num= mongoengine.StringField()
    sentiment= mongoengine.StringField()
    sex_orientation= mongoengine.StringField()
    # 数据库
    meta = {'collection':'test_infor'}
