from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('estante/',views.estante,name='estante'),
    path('compra/',views.compra,name='compra'), 
    
]