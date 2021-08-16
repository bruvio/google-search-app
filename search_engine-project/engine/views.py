import threading

from django.http import HttpResponse
from django.shortcuts import render
from utils.google_search_utils import getSavePage, searchWeb


# Create your views here.
# Create your views here.
def home(request):
    return render(request, "engine/home.html", {"search": "how to data engineering"})


def search(request):
    urls = searchWeb(num=5, stop=5)

    threads = [threading.Thread(target=getSavePage, args=(url,)) for url in urls]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return HttpResponse(urls)
    # return render(request, "search results", {"search": mysearch})


def about(request):
    theauthor = "bruvio"
    return render(request, "engine/about.html", {"user": theauthor})
