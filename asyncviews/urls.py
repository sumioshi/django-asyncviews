from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.async_view),
    path('sync/', views.sync_view),
    path('', views.home_view),  # Adicione esta linha
]


