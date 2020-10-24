from django.urls import path
from commodity import views

urlpatterns = [
    path('', views.commodity),
]