from django.urls import path

from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('new/', views.recipe_new, name='recipe_new'),
    path('<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
]
