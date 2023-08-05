from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('home/', views.home, name='home'),
    path('', views.welcome_page, name='welcome'),
    path('note/<str:pk>', views.note, name='note'),
    path('create-note/', views.creat_note, name='create-note'),
    path('update-note/<str:pk>', views.update_note, name='update-note'),
    path('delete-note/<str:pk>', views.delete_note, name='delete-note'),
]
