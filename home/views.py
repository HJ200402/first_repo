from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#def home_view(request):
#    return HttpResponse ("<p>Hello World!</p>")

def home_view(request):
    return render(request, "index.html",{})


def home_view_quote(request):
    return render(request, "quote.html",{})

def var_view(request):  # 모든 view 함수는 request를 인자로 받는다
    nums = [1,2,3,4,5]
    return render(request, "var.html", {"student":nums})
