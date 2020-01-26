from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print(request.user)  # accessing the authenticated user on the request object
    return HttpResponse("<h1>Hello World</h1>")


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact page</h1>")
