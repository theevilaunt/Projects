"""define URL patterns for learning_logs webapp (not top level)"""

from django.conf.urls import url # maps urls to views (code which executes)
from learning_logs import views
urlpatterns = [
  # home page
  url(r'^$', views.index, name='index'),
  url(r'learning_logs', views.index, name='index'),
  #url(r'', views.index, name='index'),
  # show all topics
  url(r'^topics/$', views.topics, name='topics'),
]
