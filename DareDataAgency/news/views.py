from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView, View

# Create your views here.
def news(request):


    content=News.objects.all()

    return render (request,'news/news.html',{'contant':content})

class News_detail(DetailView):

    model=News
    template='news_detail.html'
