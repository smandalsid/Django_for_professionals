from django.urls import path, include
from django.contrib import admin
from .views import HomePageView

urlpatterns=[
    path("", HomePageView.as_view(), name="home"),
]