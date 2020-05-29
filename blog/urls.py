from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('search/', views.search_blog, name="search"),
    path('detail/<str:pk>/', views.detail_page, name="detail"),
    path('update/<str:pk>/', views.update_blog, name="update"),
    path('delete/<str:pk>/', views.delete_blog, name="delete"),
    path('create/', views.create_blog, name="create"),
]