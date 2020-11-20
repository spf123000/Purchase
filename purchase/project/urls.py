from django.urls import path
from project import views

urlpatterns = [
    path('', views.index),
    path('add/', views.project_add),
    path('show/', views.project_show),
    path('delete/', views.project_delete),
    path('modify/', views.project_modify),
]