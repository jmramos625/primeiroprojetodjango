from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# HTTP request of the page "home/"
def home(request):
    return render(request, "recipes/home.html")

