from django.conf.urls import url
from blog.views.comentario import *
from blog.views.postagens import *
from . import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish,
        name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove,
        name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comentario/$', views.add_comentario_to_post,
        name='add_comentario_to_post'),
    url(r'^comentario/(?P<pk>\d+)/aprovado/$', views.comentario_aprovado,
        name='comentario_aprovado'),
    url(r'^comentario/(?P<pk>\d+)/remover/$', views.comentario_remover,
        name='comentario_remover'),

]
