from django.urls import path

from . import views

urlpatterns = [
     path('person', views.person, name = "person"),
     path('wood', views.wood, name = "wood"),
     path('nomep', views.nomep, name = "nomep")

]
    #path('add/', views.person_create_view, name='person_add'),
    #path('<int:pk>/', views.person_update_view, name='person_change')


#    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
#]