from django.conf.urls import url
from youtubeapp import views


urlpatterns=[
    url(r'^search/new/$',views.SearchCreateView.as_view(),name='search_new'),
    url(r'^search/(?P<pk>\d+)/item/$',views.main,name='main'),
    
]   
    




