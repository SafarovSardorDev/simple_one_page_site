from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/<int:id>/detail', views.new_detail, name='new_detail'),
    path('new/<int:id>/update', views.new_update, name='new_update'),
    path('new/<int:id>/delete', views.new_delete, name='new_delete'),
    path('new/create/', views.new_create, name='new_create'),
]