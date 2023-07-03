from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busca', views.search, name='search'),
    path('resultados', views.results, name='results'),
    path('madeira', views.details, name='details')
]
