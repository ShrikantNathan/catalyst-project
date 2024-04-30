from django.shortcuts import render
from django.urls import path
from .views import login, upload, query_builder, logout_user, get_all_users, create_new_user, edit_user, delete_user, get_user_detail

urlpatterns = [
    path('login/', login, name='login-url'),
    path('upload/', upload, name='upload-url'),
    path('query/', query_builder, name='query-builder'),
    path('users/', get_all_users, name='user-list'),
    path('add-user/', create_new_user, name='add-user'),
    path('user-detail/<int:pk>/', get_user_detail, name='user-detail'),
    path('edit-user/<int:pk>/', edit_user, name='edit-user'),
    path('delete-user/<int:pk>/', delete_user, name='delete-user')
    # path('logout/', logout_user, name='logout')
]
