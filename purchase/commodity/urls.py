from django.urls import path
from commodity import views

urlpatterns = [
    path('', views.index),
    path('show/', views.commodity_show),
    path('delete/', views.commodity_delete),
    path('modify/', views.commodity_modify),
]