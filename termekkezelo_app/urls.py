from django.urls import path

from . import views

urlpatterns = [
    path('kezdolap/', views.kezdolap, name='kezdolap'),
    path('termekek/', views.termek_lista, name='termek_lista'),
    path('uj/', views.termek_uj, name='termek_uj'),
    path('<int:pk>/', views.termek_reszletek, name='termek_reszletek'),
    path('<int:pk>/szerkesztes/', views.termek_szerkesztes, name='termek_szerkesztes'),
    path('<int:pk>/torles/', views.termek_torles, name='termek_torles'),
]