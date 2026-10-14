from django.urls import path
from . import views

urlpatterns = [
    path('', views.navigator),
    path('graphic_cards', views.graphic_cards),
    path('processors', views.processors),
    path('motherboards', views.motherboards),
    path('ram', views.ram),
    path('power_supply', views.power_supply),
    path('cases', views.cases),
    path('ssd', views.ssd),
    path('hdd', views.hdd),
]
