# learninglog/learning_logs/views.py
from django.shortcuts import render
#from django.http import HttpResponseRedirect
#from django.http import HttpResponse
from .models import Topic

# Create your views here.

def index(request):
  """learning_log home page"""
  return render(request, 'index.html')
  #return HttpResponse("not sure why this doesn't work!")

def topics(request):
  """show all topics"""
  topics = Topic.objects.order_by('date_added')
  context = {'topics':topics}
  return render(request, 'topics.html', context)
