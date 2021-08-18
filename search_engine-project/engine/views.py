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
    form = SearchForm(request.POST)
    if form.is_valid():  # this will validate your form
        search_text = form.cleaned_data["search"]  # now you can access input
    urls = searchWeb(num=5, stop=5, query_string=search_text)

    threads = [threading.Thread(target=getSavePage, args=(url,)) for url in urls]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    # return JsonResponse(urls, safe=False)
    # return HttpResponse(urls)
    return render(request, "search results", {"search": urls})


def about(request):
    theauthor = "bruvio"
    return render(request, "engine/about.html", {"user": theauthor})
