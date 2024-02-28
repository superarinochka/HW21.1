from django.views.generic import ListView, DetailView
from catalog.models import Product, Contact


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    queryset = Product.objects.all()[:6]


class ContactDetailView(ListView):
    model = Contact
    template_name = 'catalog/contacts.html'
    context_object_name = 'contact'
    queryset = Contact.objects.first()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'