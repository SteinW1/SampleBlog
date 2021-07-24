from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='articles-list'),
]