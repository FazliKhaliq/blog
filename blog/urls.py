from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='bloglist'),
    path('<slug:post>/', views.blogpost, name='blogpost'),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search")
]
