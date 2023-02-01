from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('cross_off/<task_id>/', views.cross_off, name='cross_off'),
    path('uncross/<task_id>/', views.uncross, name='uncross'),
    path('delete/<task_id>', views.delete, name='delete'),
]



