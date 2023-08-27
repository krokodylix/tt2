"""tt2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import MainView, AddPost, ReadPosts, GetPost, DeletePost, RegistrationView, ViewUserProfile, UpdateUserInfo

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('add_post/', AddPost.as_view()),
    path('read_posts/', ReadPosts.as_view(), name='read_posts'),
    path('get_post/<uuid:uuid>/', GetPost.as_view()),
    path('delete_post/<uuid:pk>/', DeletePost.as_view(), name='delete_post'),
    path('sign-up/', RegistrationView.as_view(), name='sign-up'),
    path('view_user_posts/<str:author>/', ViewUserProfile.as_view(), name='user_profile'),
    path('update_user_info/', UpdateUserInfo.as_view(), name='update_user_info')
]