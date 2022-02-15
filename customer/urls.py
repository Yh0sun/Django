from django.urls import path
from . import views

urlpatterns = [
    path('', views.ctm_list, name='ctm_list'),
    path('member/<int:pk>', views.ctm_detail, name='ctm_detail'),
    path('member/new', views.ctm_new, name='ctm_edit'),
]