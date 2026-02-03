from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name= 'login.html' ), name='login' ),
    path('logout/', auth_views.LogoutView.as_view( ), name='logout' ),
    path('register/', views.register, name='register' ),
    path('create-post/', views.create_post, name='create_post' ),
    path('', views.home, name='home' ),
    path('post/<int:pk>/', views.post_view, name='post_view' ),
    path('post/update/<int:pk>/', views.update_post, name='update_post' ),
    path('post/delete/<int:pk>/', views.delete_post, name='delete_post'),
    
]
