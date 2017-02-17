"""pizzas URL Configuration WEBAPP level

"""
from django.conf.urls import url
from pizzas import views

urlpatterns = [
    url(r'^$', views.index, name='index'),    
    url(r'pizzas', views.index, name='index'), 
    url(r'', views.index, name='index'),    
]
