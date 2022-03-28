
from django.urls import path
from . import views 
app_name = 'news'
urlpatterns = [
    path('',views.news, name='news'),
    path('<slug>', views.News_detail.as_view(), name='news_detail'),
]