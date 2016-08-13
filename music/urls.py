from django.conf.urls import url
from . import views

app_name= 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index , name= 'index'),  #it is for only "music/" meaning when user just requests music

    # /music/712/   (for an individual album)
    url(r'^(?P<album_id>[0-9]+)/$' , views.detail , name= 'detail'),

    # /music/712/favourite/   (for an individual album)
    url(r'^(?P<album_id>[0-9]+)/favourite/$' , views.favourite , name= 'favourite')

]
