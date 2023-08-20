from django.shortcuts import render
from django.views.generic import ListView

from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)


def store(request):
    return render(request, 'store.html')


def checkout(request):
    print(request)


def search(request):
    print('search')


def login(request):
    print('login')


def register(request):
    print('register')


def dashboard(request):
    print('dashboard')


def logout(request):
    print("logout")


def add_cart(request, id):
    print("Added to cart!")


def submit_review(request):
    print("Submitted!")
