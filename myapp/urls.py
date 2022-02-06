

from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
   path("", views.home, name="home") , 
   path("home", views.home, name="home") , 
   path("signin", views.signin, name="signin") ,
   path("signup", views.signup, name="signup") ,
   path("signout", views.signout, name="signout") ,
   path("roomalloc", views.roomalloc, name="roomalloc") ,
   path("instructions", views.instructions, name="instructions") ,
]