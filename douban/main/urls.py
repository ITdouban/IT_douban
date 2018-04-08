from django.conf.urls import url
from .views import (WriteArticle,userInformation,userPage,userArticle,
        deleteArticle,changeArticle,article_detail,commentList,articleList,
        newArticleList,articleCate)

urlpatterns = [
    url(r'^write/',WriteArticle,name='WriteArticl'),
    url(r'^informationChange/',userInformation),
    url(r'^$',userPage),
    url(r'^index/',userPage),
    url(r'^userArticleList/',userArticle,name='userArticle'),
    url(r'^delete/(?P<id>[0-9]+)/$',deleteArticle,name='deleteArticle'),
    url(r'^change/(?P<id>[0-9]+)/$',changeArticle,name='changeArticle'),
    url(r'^detail/(?P<id>[0-9]+)/$',article_detail,name='article_detail'),
    url(r'^comment/$',commentList,name='commentList'),
    url(r'^articleList/hot/(?P<page>[0-9]+)/$',articleList,name='articleList'),
    url(r'^articleList/new/(?P<page>[0-9]+)/$',newArticleList,name='newArticleList'),
    url(r'^articleList/(?P<cate>[0-9]+)/(?P<page>[0-9]+)/$',articleCate,name='articleCate'),
    
]
