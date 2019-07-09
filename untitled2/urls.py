from django.conf.urls import url
from django.urls import path
from . import search
from . import view
from . import CharacterRel
from . import skip
from . import THtrend
from . import Comments
from . import views
from . import admin
from . import source

urlpatterns = [
    url(r'^topic$', view.topic),
    url(r'^search$', search.search),
    url(r'^relation$', CharacterRel.relations),
    url(r'^trend$', THtrend.trend),
    url(r'^THTrend$', skip.change),
    url(r'^searchContent$', search.searchContent),
    url(r'^comments$', Comments.SumComments),

    path('analysis/index/', views.index),
    path('index', views.index),
    path('analysis/source/', views.source),
    path('analysis/manner/', views.manner),
    path('analysis/EventWordCloud/', views.EventWordCloud),
    path('analysis/ThemeRelationGraph/', views.ThemeRelationGraph),
    path('analysis/CommentWordCloud/', views.CommentWordCloud),
    path('analysis/TestIndex/', views.search_index),
    path('analysis/RegionCommentWC/', views.RegionCommentWC),
    path('analysis/EventForm/', views.EventForm),
    path('analysis/CommentChanging/', views.CommentChanging),
    path('place', source.getPlace),
    path('source', source.getSource),
    path('source_news', source.getSourceNews),
    path('source_media_key', source.getSourcMediaKey),
    path('source_media_title_by_key', source.getSourceTitleByKey),
    path('homepage',views.homepage),
    path('country_relation',source.getRelation),
    path('manner_by_date',source.getMannerByDate),
    path('theme_content_by_date',source.getThemeContentByDate)
]
