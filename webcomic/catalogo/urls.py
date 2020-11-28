from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,                                  name='index'),
    path('estante/'      ,views.estante,                  name='estante'),
    path('compra/'       ,views.compra,                   name='compra'), 
    path('vendidos/'     ,views.vendidos,                 name='vendidos'),
    path('comic_lista/'  ,views.comicListView.as_view(),  name='comic_lista'),
    path('comic/<int:pk>',views.comicDetailView.as_view(),name='comic_especificacion'),
    
]


urlpatterns += [
    path('comic/create/'         , views.comicCreate.as_view(), name='comic_create'),
    path('comic/<int:pk>/update/', views.comicUpdate.as_view(), name='comic_update'),
    path('comic/<int:pk>/delete/', views.comicDelete.as_view(), name='comic_delete'),
]