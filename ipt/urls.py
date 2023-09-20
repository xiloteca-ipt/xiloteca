from django.urls import path

from ipt import views

urlpatterns = [
    path('', views.index, name='index'),
     path('busca', views.busca, name = "busca"),
     path('ficha', views.ficha, name='ficha'),
]
