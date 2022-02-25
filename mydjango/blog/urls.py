from django.urls import path, include
from . import views
from rest_framework import routers

from . import views
from . import viewsets

router = routers.DefaultRouter()
# http://localhost:8000/blog/posts
router.register(r'posts', viewsets.PostViewSet)
# http://localhost:8000/blog/comments
router.register(r'comments', viewsets.CommentViewSet)

urlpatterns = [
    # http://localhost:8000/blog
    path('', views.post_list, name='everyPost'),
    # http://localhost:8000/blog/post/2
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # http://localhost:8000/blog/post/new
    path('post/new/', views.post_new, name='post_new'),
    # http://localhost:8000/blog/post/1/edit
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # http://localhost:8000/blog/post/1/remove
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    # http://localhost:8000/blog/post/1/comment
    path('post/<int:pk>/comment/', views.add_comment_tp_post, name='add_comment'),
    # http://localhost:8000/blog/post/1/approve
    path('post/<int:pk>/comment/approve/', views.comment_approve, name='comment_approve'),
    # http://localhost:8000/blog/post/1/remove
    path('post/<int:pk>/comment/remove/', views.comment_remove, name='comment_remove'),

    path('', include(router.urls)),
    path('api/login/', views.login, name='login')
]
