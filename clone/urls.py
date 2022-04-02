from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from . import views


urlpatterns=[
    re_path('^$',views.index,name = 'index'),
    
]
