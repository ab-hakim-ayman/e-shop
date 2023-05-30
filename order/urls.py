from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('add-to-wish/<int:pk>/', views.add_to_wish, name='add-to-wish'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('wish-view/', views.wish_view, name='wish'),
]
