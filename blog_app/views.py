from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
  # return HttpResponse('<h2>Blog homepage</h2>')


posts = [
  {
    'author': 'Karan Mahato',
    'title': 'Best Place To Learn Python From',
    'content': 'Corey Schafer is the best Python teacher out there.',
    'date_posted': 'April 24, 2023'
  },
  {
    'author': 'Joe Nuts',
    'title': 'Why the HTML/CSS course by SuperSimpleDev is the BEST!',
    'content': 'You will actually build a thing not just mess around with the HTML syntax.',
    'date_posted': 'April 25, 2023'
  }
]


def home(request):
  context = {
    'posts': posts
  }

  return render(request, 'blog_app/home.html', context)

def about(request):
  return render(request, 'blog_app/about.html', {'title': 'About'})
