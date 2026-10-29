from django.urls import path
from . import views

urlpatterns = [
    path('navigator', views.navigator, name="navigator"),
    path('graphic_cards/', views.graphic_cards),
    path('processors/', views.processors),
    path('motherboards/', views.motherboards),
    path('ram/', views.ram),
    path('power_supply/', views.power_supply),
    path('cases/', views.cases),
    path('ssd/', views.ssd),
    path('hdd/', views.hdd),
    path('', views.redirect_to_home),
    path('home', views.home, name='home'),
    path('client',views.client),
    path('postuser',views.postuser),
    path('buy/', views.buy_component, name='buy_component'),
    path('success/', views.purchase_success, name='success'),

]
