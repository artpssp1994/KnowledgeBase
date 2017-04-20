from django.conf.urls import patterns, url
from knowledge_management import views

urlpatterns = patterns('',
                       url(r'^showtopic/$', views.showtopic, name='showtopic'),
                       url(r'^search/$', views.search, name='search'),
                       url(r'^recentpost/$', views.recentpost, name='recentpost'),
                       url(r'^mypost/page=(?P<page>[\w\-]+)/$', views.mypost, name='mypost'),
                       url(r'^newpost/$', views.newpost, name='newpost'),
                       url(r'^topknowledge/$', views.topknowledge, name='topknowledge'),
                       url(r'^add_category/$', views.add_category, name='add_category'),
                       url(r'^newpost/(?P<do_command>[\w\-]+)/(?P<to_page>[\w\-]+)/$', views.newpost, name='newpost'),
                       url(r'^category/$', views.category, name='category'),
                       url(r'^result/$', views.result, name='result'),
                       url(r'^tagresult/(?P<tag_name>[\w\-]+)/$', views.tagresult, name='tagresult'),
                       url(r'^category/(?P<supcategory_name_slug>[\w\-]+)/(?P<category_name_slug>[\w\-]+)/(?P<page_name_slug>[\w\-]+)/$', views.page, name='page'),
                       url(r'^category/(?P<supcategory_name_slug>[\w\-]+)/(?P<category_name_slug>[\w\-]+)page=(?P<page>[\w\-]+)/$', views.sub_category, name='category'),
                       url(r'^sub_category/$', views.sub_category, name='sub_category'),
                       url(r'^likecomment/(?P<supcategory_name_slug>[\w\-]+)/(?P<category_name_slug>[\w\-]+)/(?P<page_name_slug>[\w\-]+)/(?P<commentid>[\w\-]+)/$', views.likecomment, name='likecomment'),
                       url(r'^preview/$', views.index, name='preview'),
                       url(r'^likepage/(?P<supcategory_name_slug>[\w\-]+)/(?P<category_name_slug>[\w\-]+)/(?P<page_name_slug>[\w\-]+)/$', views.likepage, name='likecomment'),
                       url(r'^delete/(?P<supcategory_name_slug>[\w\-]+)/(?P<category_name_slug>[\w\-]+)/(?P<page_name_slug>[\w\-]+)/(?P<commentid>[\w\-]+)/$', views.deletecomment, name='likecomment'),
                       url(r'^list/(?P<check_status>[\w\-]+)/$', views.list, name='list'),
                       )