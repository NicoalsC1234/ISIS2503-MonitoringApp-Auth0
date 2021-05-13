from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

urlpatterns = [
    path('boletines/', views.boletin_list, name='boletinList'),
    path('boletin/<id>', views.single_boletin, name='singleBoletin'),
    path('boletincreate/', csrf_exempt(views.boletin_create), name='boletinCreate'),
]
