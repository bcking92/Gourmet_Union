from django.shortcuts import render
from .models import Food_info

# Create your views here.
def home(request):
    context = {
    
    }
    return render(request, 'home.html', context)

def signin(request):
    context = {


    }
    return render(request, 'signin.html', context)

def location(request,region):
    context = {
        'region' : region,

    }
    return render(request, 'location.html', context)

def rate_restaurant(request, restaurant_id):
    context = {

    }
    return render(request, 'rate_restaurant.html', context)

def info_restaurant(request, restaurant_id):
    temp = Food_info()
    restaurant = temp.objects.get(id=restaurant_id)
    context = {
        'restaurant' : restaurant,
    }
    return render(request, 'info_restaurant.html', context)