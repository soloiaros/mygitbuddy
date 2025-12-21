import django.contrib.auth.urls
from django.contrib import admin
from django.urls import include, path

import homepage.urls


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path(
        'homepage/',
        include(homepage.urls),
        name='homepage',
    ),
]

urlpatterns += [path('', include(django.contrib.auth.urls))]
