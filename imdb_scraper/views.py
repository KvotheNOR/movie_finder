from django.http import HttpResponse


def index(request):
    return HttpResponse("hello, you're at the imdb_scraper index")
