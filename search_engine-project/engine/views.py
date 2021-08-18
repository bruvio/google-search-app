import threading

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from utils.google_search_utils import getSavePage, searchWeb

from .forms import SearchForm


# Create your views here.
# Create your views here.
def home(request):
    return render(request, "engine/home.html", {"search": "how to data engineering"})


def search(request):
    form = SearchForm(request.GET)
    search_text = form.data["search_text"]  # now you can access input
    urls = searchWeb(num=5, stop=5, query_string=search_text)

    threads = [threading.Thread(target=getSavePage, args=(url,)) for url in urls]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return render(request, "engine/search.html", {"search": urls})


def about(request):
    theauthor = "bruvio"
    return render(request, "engine/about.html", {"user": theauthor})
