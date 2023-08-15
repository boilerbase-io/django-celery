from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path("user/", views.UserViewSet.as_view()),
]
