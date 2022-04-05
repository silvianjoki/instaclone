from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django_registration.backends.one_step.views import RegistrationView


urlpatterns=[
    re_path('^$', views.index, name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('^upload_image/', views.upload_image, name='upload_image'),
    path('results/', views.search, name='results'),
    
    
    
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/',
        RegistrationView.as_view(success_url=reverse_lazy('home')),
        name='django_registration_register'),

    re_path('^logout/$', auth_views.LogoutView.as_view(), name='logout'), 
    re_path('^login/$', LoginView.as_view(), {"next_page": '/'}),
]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)