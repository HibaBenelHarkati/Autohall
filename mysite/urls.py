from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from main import urls
from users import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('users.urls')),
]
