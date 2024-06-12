from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')


def acc(request):
    return render(request, 'accounts.html')

def login_page(request):
    return render(request, 'login.html')

def forgot_page(request):
    return render(request, 'forget.html')

def womens_store(request):
    return render(request, 'Womens.html')

def cartPage(request):
    return render(request, 'cart.html')

def orderPage(request):
    return render(request, 'order.html')


def detailsPage(request):
    return render(request, 'details.html')
