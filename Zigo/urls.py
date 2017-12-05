from django.conf.urls import  url
from Zigo import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.user, name='user'),
]
