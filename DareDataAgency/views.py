from django.http.response import HttpResponse
from django.shortcuts import render
from news.models import News

# Create your views here.
def home(request):
    content = News.objects.all().order_by('-created_date')[:4]

    return render (request,'home.html',{'contant':content})