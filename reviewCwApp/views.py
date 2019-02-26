from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    context = {
        "page": "home"
    }
    return render(request, "reviewCwApp/home.html", context)


def page2(request):
    context = {
        "page": "page2"
    }

    return render(request, "reviewCwApp/Page2.html", context)


def page3(request):
    context = {
        "page": "page3"
    }
    return render(request, "reviewCwApp/Page3.html", context)


def page4(request):
    context = {
        "page": "page4"
    }
    return render(request, "reviewCwApp/Page4.html", context)


def page5(request):
    context = {
        "page": "page5"
    }
    return render(request, "reviewCwApp/Page5.html", context)
