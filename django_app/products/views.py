from django.views.generic import ListView
from .models import Product


class ListProductsView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'
    paginate_by = 10
