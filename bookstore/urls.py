"""
URL configuration for bookstore project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Disable Django admin as per requirements
    # path('admin/', admin.site.urls),
    
    # App URLs
    path('', include('books.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('admin_panel/', include('admin_panel.urls')),
    
    # Redirect root to books list
    path('', RedirectView.as_view(url='/books/', permanent=True)),
]