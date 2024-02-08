from django.urls import path, include
from . import views

app_name = 'music'

urlpatterns = [
	#/music/
    path(r'^$', views.IndexView.as_view(), name='index'),

    #/music/{album_id}/
    path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/music/album/add
    path(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

]