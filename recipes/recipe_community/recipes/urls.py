from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe1/', views.recipe1, name='recipe1'),
    path('recipe2/', views.recipe2, name='recipe2'),
    path('recipe3/', views.recipe3, name='recipe3'),
    path('recipe4/', views.recipe4, name='recipe4'),
    path('recipe5/', views.recipe5, name='recipe5'),
]
