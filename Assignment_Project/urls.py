from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Homeworks.urls')),
    path('admin/', admin.site.urls),
    path('homework/', include('Homeworks.urls')),
]
