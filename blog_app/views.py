from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# def home(request):
  # return HttpResponse('<h2>Blog homepage</h2>')



def home(request):
  context = {
    'posts': Post.objects.all()
  }

  return render(request, 'blog_app/home.html', context)

def about(request):
  return render(request, 'blog_app/about.html', {'title': 'About'})
