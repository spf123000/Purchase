from django.urls import path
from commodity import views

urlpatterns = [
    path('', views.index),
    path('show/', views.commodity_show),
    path('show_options/', views.commodity_show_options),
    path('delete/', views.commodity_delete),
    path('modify/', views.commodity_modify),
    path('submit/', views.commodity_submit),
]