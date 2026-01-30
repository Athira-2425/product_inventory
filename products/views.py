from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product
from .forms import ProductForm


def home(request):
    products = Product.objects.all().order_by("-id")

    search = request.GET.get("search", "").strip()
    category = request.GET.get("category", "").strip()

  
    if search:
        products = products.filter(
            Q(name__icontains=search) | Q(sku__icontains=search)
        )

   
    if category:
        products = products.filter(category=category)

 
    low_stock_count = Product.objects.filter(stock__lt=10).count()

 
    paginator = Paginator(products, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

   
    categories = Product.objects.exclude(category__isnull=True).exclude(category="") \
        .values_list("category", flat=True).distinct()

    return render(request, "home.html", {
        "page_obj": page_obj,
        "low_stock_count": low_stock_count,
        "categories": categories,
        "search": search,
        "selected_category": category,
    })


def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Product added successfully')
        return redirect('home')
    return render(request, 'forms.html', {'form': form})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail.html', {'product': product})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, 'Product updated successfully')
        return redirect('home')
    return render(request, 'forms.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect('home')
    return render(request, 'delete.html', {'product': product})

