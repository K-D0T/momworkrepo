from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Home, name='home'),
    path('addpics', views.addpics, name='addpics'),
    path('submitpics', views.submitpics, name='submitpics'),
    path('images', views.images, name='images'),
    path('create', views.create, name='create'),
    path('', views.login_request, name='login'),
    path('createUser', views.createUser, name='createUser'),
    path('logout/', views.logout_request, name='logout'),
    path('deleteimage/', views.deleteimage, name='deleteimage'),
    path('matching/', views.matching, name='matching'),
    
    ]