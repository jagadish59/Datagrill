
from argparse import Namespace
from django.conf import settings
from django.conf.urls.static import static
from DareDataAgency import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('news/',include('news.urls', namespace='news')),
    path('account/', include('accounts.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)