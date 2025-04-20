from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Order, OrderItem
from books.models import Book

class CheckoutView(LoginRequiredMixin, View):
    template_name = 'orders/checkout.html'
    
    def get(self, request):
        cart = request.session.get('cart', {})
        if not cart:
            return redirect(reverse('cart:view_cart'))
        
        cart_items = []
        total_price = 0
        
        for book_id, item_data in cart.items():
            try:
                book = Book.objects.get(id=book_id)
                quantity = item_data['quantity']
                price = item_data['price']
                item_total = quantity * price
                
                cart_items.append({
                    'book': book,
                    'quantity': quantity,
                    'price': price,
                    'total': item_total
                })
                
                total_price += item_total
            except Book.DoesNotExist:
                continue
        
        return render(request, self.template_name, {
            'cart_items': cart_items,
            'total_price': total_price
        })
    
    def post(self, request):
        cart = request.session.get('cart', {})
        if not cart:
            return redirect(reverse('cart:view_cart'))
        
        # Calculate total price
        total_price = 0
        for book_id, item_data in cart.items():
            total_price += item_data['quantity'] * item_data['price']
        
        # Create order
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            status='paid'  # Assuming payment is successful
        )
        
        # Create order items
        for book_id, item_data in cart.items():
            try:
                book = Book.objects.get(id=book_id)
                OrderItem.objects.create(
                    order=order,
                    book=book,
                    quantity=item_data['quantity'],
                    price=item_data['price']
                )
                
                # Update inventory
                book.inventory -= item_data['quantity']
                book.save()
            except Book.DoesNotExist:
                continue
        
        # Clear cart
        request.session['cart'] = {}
        request.session.modified = True
        
        return redirect(reverse('orders:payment_summary', kwargs={'order_id': order.id}))

class PaymentSummaryView(LoginRequiredMixin, View):
    template_name = 'orders/payment_summary.html'
    
    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            return render(request, self.template_name, {'order': order})
        except Order.DoesNotExist:
            return redirect(reverse('books:book_list'))

class OrderHistoryView(LoginRequiredMixin, ListView):
    template_name = 'orders/order_history.html'
    context_object_name = 'orders'
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')