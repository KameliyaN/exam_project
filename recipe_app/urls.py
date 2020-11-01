from django.urls import path

from recipe_app import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('details/<int:pk>/', views.detail_recipe, name='details_recipe'),

]
