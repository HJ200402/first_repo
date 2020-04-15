from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#def home_view(request):
#    return HttpResponse ("<p>Hello World!</p>")

def home_view(request):
    return render(request, "index.html",{})


def home_view_quote(request):
    return render(request, "quote.html", {})
