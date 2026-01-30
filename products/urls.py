from django.urls import path
from .views import *


urlpatterns = [
path('', home, name='home'),
path('add/', add_product, name='add'),
path('detail/<int:pk>/', product_detail, name='detail'),
path('edit/<int:pk>/', edit_product, name='edit'),
path('delete/<int:pk>/', delete_product, name='delete'),
]



