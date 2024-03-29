from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# django takes our template, and the template context, mashes them together, renders it and sends back raw html to the browser


def home_view(request, *args, **kwargs):
    print(request.user)  # accessing the authenticated user on the request object
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact page</h1>")
    my_context = {
        "my_text": "context value being shown",
        "my_number": 246,
        "my_list": [2, 3, 4, 5, "Hi"],
        "my_html": "<h2>This is html</h2>"
    }
    return render(request, 'contact.html', my_context)
