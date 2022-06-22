from django.shortcuts import render, get_object_or_404, redirect
from .models import Category,  Product, Brand
from cart.forms import CartAddProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import JsonResponse
import json
from django.core import serializers


def register(request):
    categories = Category.objects.filter(parent=None)
    brands = Brand.objects.all()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You are registered successfully')
            return redirect('Eshopper:user_login')
        else:
            messages.error(request, form.errors)
    else:
        form = UserCreationForm()
    context = {
        'form': form,
        'categories': categories,
        'brands': brands,
    }

    return render(request, 'Eshopper/register.html', context=context)


def user_login(request):
    categories = Category.objects.filter(parent=None)
    brands = Brand.objects.all()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Eshopper:home')
    else:
        form = AuthenticationForm()
    context = {
        'categories': categories,
        'brands': brands,
        'form': form,
    }
    return render(request, 'Eshopper/login.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('Eshopper:home')


def index(request):
    products = Product.objects.order_by('-created_at')
    product = Product.objects.all().select_related('category')
    categories = Category.objects.filter(parent=None)
    brands = Brand.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'products': products,
        'product': product,
        'categories': categories,
        'cart_product_form': cart_product_form,
        'brands': brands,
    }
    return render(request, 'Eshopper/index.html', context=context)


def get_category(request, slug):
    products = Product.objects.filter(category__slug=slug)
    categories = Category.objects.filter(parent=None)
    category = Category.objects.filter(slug=slug)
    brands = Brand.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'category': category,
        'brands': brands,
    }
    return render(request, 'Eshopper/category_list.html', context=context)


def get_brand(request, slug):
    products = Product.objects.filter(brand__slug=slug)
    brands = Brand.objects.all()
    brand = Brand.objects.filter(slug=slug)
    categories = Category.objects.filter(parent=None)

    context = {
        'products': products,
        'brands': brands,
        'brand': brand,
        'categories': categories
    }
    return render(request, 'Eshopper/brand_list.html', context=context)


def detail_product(request, slug):
    product = Product.objects.get(slug=slug)
    brands = Brand.objects.all()
    categories = Category.objects.filter(parent=None)
    context = {
        'product': product,
        'brands': brands,
        'categories': categories
    }
    return render(request, 'Eshopper/product_details.html', context=context)


def ajax_price_range(request):
    global product
    if request.method == 'POST':
        min = request.POST['min']
        max = request.POST['max']
        product = Product.objects.filter(price__range=(min, max))
        tmpJson = serializers.serialize("json", product)
        data = json.loads(tmpJson)
    return JsonResponse(data, safe=False)


