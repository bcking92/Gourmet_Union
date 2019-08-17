from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
    
    }
    return render(request, 'home.html', context)

def signin(request):
    context = {


    }
    return render(request, 'signin.html', context)