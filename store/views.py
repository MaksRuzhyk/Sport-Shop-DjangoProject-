from _ast import Store
from itertools import product
from .utils import CategoryMixin
from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

# def work(request):
    # p = Product(title='Ford',price=100 )
    # p.save()

    # Product.objects.create(title='BMW', price=200)
    # p = Product.objects.filter(pk=8).update(price=300)
    # p = Product.objects.get(pk=8).delete()
    # print(p)
    # obj = Product.objects.exclude(title='Ford')
    # obj = Product.objects.all().order_by('-pk')
    # obj = Product.objects.filter(title='Ford').count()
    #
    # print(obj)
    # return HttpResponse("Hello, world. You're at the polls page.")

def build_template(lst: list, cols: int) -> list[list]:
    return [lst[i:i + cols] for i in range(0, len(lst), cols)]

class HomeView(ListView, CategoryMixin):
    model = Product

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        if search_query:
            return self.model.objects.filter(
                Q(title__icontains=search_query)
                |
                Q(info__icontains=search_query)
            )

        return Product.objects.all()



class ProductView(DetailView, CategoryMixin):
    model = Product



class CategoryView(DetailView, CategoryMixin):
    model = Category


def save_order(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    print(request.POST['username'], request.POST['email'], request.POST['product_id'])
    order = Order()
    order.name = request.POST['username']
    order.email = request.POST['email']
    order.product = Product.objects.get(pk=request.POST['product_id'])
    order.save()
    return render(request, 'store/order.html', context={
        'categories': categories,
        'order': order,
    })


# Create your views here.
# def product_list(request):
#     categories = Category.objects.all()
#     search_query = request.GET.get('search', None)
#     if search_query:
#         product_list = Product.objects.filter(
#             Q(title__icontains=search_query)
#             |
#             Q(info__icontains=search_query)
#         )
#     else:
#         product_list = Product.objects.all()
#     return render(request, 'store/product_list.html', context={
#         'product_list': product_list,
#         'categories': categories,
#     })


# def product_detail(request, pk: int):
#     categories = Category.objects.all()
#     product = Product.objects.get(pk=pk)
#     return render(request, 'store/product_detail.html', context={
#         'product': product,
#         'categories': categories,
#     })

# def category_detail(request, pk: int):
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=pk)
#     product_list = category.products.all()
#     return render(request, 'store/category_detail.html', context={
#         'product_list': product_list,
#         'category': category,
#         'categories': categories,
#     })


