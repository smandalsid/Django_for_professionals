from django.urls import path, include
from django.contrib import admin
from .views import HomePageView, AboutPageView

urlpatterns=[
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]