from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('topcorner/', admin.site.urls),
    path('', include('blog.urls')),
]
