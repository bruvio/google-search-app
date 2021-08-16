from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# Create your views here.
def home(request):
    return render(request, "engine/home.html", {"search": "how to data engineering"})


def search(request):
    return HttpResponse("these are your search results")
    # return render(request, "search results", {"search": mysearch})


def about(request):
    theauthor = "bruvio"
    return render(request, "engine/about.html", {"user": theauthor})
