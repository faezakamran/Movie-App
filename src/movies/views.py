from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
import json

def movie_list_view(request):

    with open('movies.json', encoding='utf-8') as data_file:
        json_data = json.loads(data_file.read())

        for movie_data in json_data:
            movie = Movie.create(**movie_data)

    queryset = Movie.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "movie_list.html", context)

def movie_detail_view(request, id):
    obj = get_object_or_404(Movie, id=id)
    context = {
        "object": obj
    }
    return render(request, "movie_detail.html", context)
