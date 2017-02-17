from django.shortcuts import render

# Create your views here.

def index(request):
  """learning_log home page"""
  return render(request, 'index.html')