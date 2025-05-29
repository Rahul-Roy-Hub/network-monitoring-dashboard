from django.contrib import admin
from django.urls import path
from monitor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('delete/<str:ip>/', views.delete_device, name='delete_device'),
    path('edit/<str:ip>/', views.edit_device, name='edit_device'),
]
