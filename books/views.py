from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 10

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('accounts:login'))
        
        book = self.get_object()
        if 'add_to_cart' in request.POST:
            # Initialize cart in session if it doesn't exist
            if 'cart' not in request.session:
                request.session['cart'] = {}
            
            cart = request.session['cart']
            book_id = str(book.id)
            
            if book_id in cart:
                cart[book_id]['quantity'] += 1
            else:
                cart[book_id] = {
                    'quantity': 1,
                    'price': float(book.price)
                }
            
            request.session.modified = True
            return redirect('cart:view_cart')
        
        return self.get(request, *args, **kwargs)