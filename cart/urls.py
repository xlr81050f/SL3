from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='view_cart'),
    path('update/', views.UpdateCartView.as_view(), name='update_cart'),
]