from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from books.models import Book
from orders.models import Order

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            # User is logged in but not staff, redirect to books list
            return HttpResponseRedirect(reverse('books:book_list'))
        else:
            # User is not logged in, redirect to login with next parameter
            return HttpResponseRedirect(f"{reverse('accounts:login')}?next={self.request.path}")

class AdminDashboardView(AdminRequiredMixin, View):
    template_name = 'admin_panel/dashboard.html'
    
    def get(self, request):
        total_books = Book.objects.count()
        total_orders = Order.objects.count()
        recent_orders = Order.objects.order_by('-created_at')[:5]
        
        return render(request, self.template_name, {
            'total_books': total_books,
            'total_orders': total_orders,
            'recent_orders': recent_orders
        })

class BookListAdminView(AdminRequiredMixin, ListView):
    model = Book
    template_name = 'admin_panel/book_list.html'
    context_object_name = 'books'
    paginate_by = 10

class BookCreateView(AdminRequiredMixin, View):
    template_name = 'admin_panel/book_form.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        cover_image = request.POST.get('cover_image')
        
        # Form validation
        errors = {}
        if not title:
            errors['title'] = 'Title is required'
        if not author:
            errors['author'] = 'Author is required'
        if not price:
            errors['price'] = 'Price is required'
        else:
            try:
                price = float(price)
            except ValueError:
                errors['price'] = 'Price must be a number'
        
        if not inventory:
            errors['inventory'] = 'Inventory is required'
        else:
            try:
                inventory = int(inventory)
                if inventory < 0:
                    errors['inventory'] = 'Inventory must be a positive number'
            except ValueError:
                errors['inventory'] = 'Inventory must be a number'
        
        if errors:
            return render(request, self.template_name, {
                'errors': errors,
                'book': {
                    'title': title,
                    'author': author,
                    'description': description,
                    'price': price,
                    'inventory': inventory,
                    'cover_image': cover_image
                }
            })
        
        # Create book
        Book.objects.create(
            title=title,
            author=author,
            description=description,
            price=price,
            inventory=inventory,
            cover_image=cover_image
        )
        
        return redirect(reverse_lazy('admin_panel:book_list'))

class BookUpdateView(AdminRequiredMixin, View):
    template_name = 'admin_panel/book_form.html'
    
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, self.template_name, {'book': book})
    
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        cover_image = request.POST.get('cover_image')
        
        # Form validation
        errors = {}
        if not title:
            errors['title'] = 'Title is required'
        if not author:
            errors['author'] = 'Author is required'
        if not price:
            errors['price'] = 'Price is required'
        else:
            try:
                price = float(price)
            except ValueError:
                errors['price'] = 'Price must be a number'
        
        if not inventory:
            errors['inventory'] = 'Inventory is required'
        else:
            try:
                inventory = int(inventory)
                if inventory < 0:
                    errors['inventory'] = 'Inventory must be a positive number'
            except ValueError:
                errors['inventory'] = 'Inventory must be a number'
        
        if errors:
            return render(request, self.template_name, {
                'errors': errors,
                'book': {
                    'id': pk,
                    'title': title,
                    'author': author,
                    'description': description,
                    'price': price,
                    'inventory': inventory,
                    'cover_image': cover_image
                }
            })
        
        # Update book
        book.title = title
        book.author = author
        book.description = description
        book.price = price
        book.inventory = inventory
        book.cover_image = cover_image
        book.save()
        
        return redirect(reverse_lazy('admin_panel:book_list'))

class BookDeleteView(AdminRequiredMixin, View):
    template_name = 'admin_panel/book_confirm_delete.html'
    
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, self.template_name, {'book': book})
    
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect(reverse_lazy('admin_panel:book_list'))

class OrderListAdminView(AdminRequiredMixin, ListView):
    model = Order
    template_name = 'admin_panel/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10
    
    def get_queryset(self):
        return Order.objects.all().order_by('-created_at')

class OrderDetailAdminView(AdminRequiredMixin, DetailView):
    model = Order
    template_name = 'admin_panel/order_detail.html'
    context_object_name = 'order'