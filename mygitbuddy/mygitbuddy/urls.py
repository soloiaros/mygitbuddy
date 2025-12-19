import django.contrib.auth.views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path(
        'login/',
        django.contrib.auth.views.LoginView.as_view(
            template_name='login.html',
            next_page='/homepage/',
        ),
        name='login',
    ),
    path(
        'homepage/',
        include('homepage.urls'),
        name='homepage',
    ),
]
