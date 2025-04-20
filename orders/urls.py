from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('payment-summary/<int:order_id>/', views.PaymentSummaryView.as_view(), name='payment_summary'),
    path('history/', views.OrderHistoryView.as_view(), name='order_history'),
]