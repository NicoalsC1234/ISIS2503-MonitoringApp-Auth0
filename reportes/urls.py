from django.urls import path

from . import views

urlpatterns = [
    path('reportes/',views.reportes_create),
    path('reportescreate/', views.reportes_create, name='reportesCreate'),
]