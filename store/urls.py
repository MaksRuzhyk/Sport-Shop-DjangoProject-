from django.urls import path
from .views import HomeView, ProductView, CategoryView, save_order

urlpatterns = [
    # path('', work),
    path('', HomeView.as_view(), name='product_list_url'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_detail_url'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category_detail_url'),
    path('save_order', save_order),
]