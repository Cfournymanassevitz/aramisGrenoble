from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ventes/', views.ventes_json, name='ventes_json'),
]