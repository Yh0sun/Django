from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('new/', views.recipe_new, name='recipe_new'),
    path('<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('<int:pk>/remove/', views.recipe_remove, name='recipe_remove'),
    path('<int:pk>/comment/', views.comment_add, name='comment_add'),
    path('comment/.<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
