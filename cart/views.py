from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from books.models import Book

class CartView(LoginRequiredMixin, View):
    template_name = 'cart/cart.html'
    
    def get(self, request):
        cart = request.session.get('cart', {})
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
                # Remove item if book doesn't exist
                del cart[book_id]
                request.session.modified = True
        
        return render(request, self.template_name, {
            'cart_items': cart_items,
            'total_price': total_price
        })

class UpdateCartView(LoginRequiredMixin, View):
    def post(self, request):
        cart = request.session.get('cart', {})
        action = request.POST.get('action')
        book_id = request.POST.get('book_id')
        
        if action == 'remove' and book_id in cart:
            del cart[book_id]
        
        elif action == 'update':
            quantity = int(request.POST.get('quantity', 1))
            if quantity > 0 and book_id in cart:
                cart[book_id]['quantity'] = quantity
            elif quantity <= 0 and book_id in cart:
                del cart[book_id]
        
        request.session.modified = True
        return redirect(reverse('cart:view_cart'))