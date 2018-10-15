from django.urls import path

from . import views

urlpatterns = [
    path('sincronizacao', views.sincronizacao),
]