from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    # New paths for Edit and Delete
    path('review/edit/<int:pk>/', views.edit_review, name='edit_review'),
    path('review/delete/<int:pk>/', views.delete_review, name='delete_review'),
]