from django.shortcuts import render
from .models import Category,Movie

# category_list= ["adventure", "romantic", "dram", "scientist"]
# movie_list = [
#     {
#         "id": 1,
#         "movie_name": "movie1",
#         "description":" movie 1's description",
#         "image": "1.jpg",
#         "homepage": True
#     },
#     {
#         "id": 2,
#         "movie_name": "movie2",
#         "description":" movie 2's description",
#         "image": "2.jpg",
#         "homepage": True
#     }
#     ,
#     {
#         "id": 3,
#         "movie_name": "movie3",
#         "description":" movie 3's description",
#         "image": "3.jpg",
#         "homepage": False
#     },
#     {
#         "id": 4,
#         "movie_name": "movie4",
#         "description":" movie 4's description",
#         "image": "4.jpg",
#         "homepage": False
#     }
# ]

# def home(request):
#     data ={
#         "categories": category_list,
#         "movies": movie_list
#     }
#     return render(request,"index.html",data)

# def movies(request):
#     data ={
#         "categories": category_list,
#         "movies": movie_list
#     }
#     return render(request,"movies.html",data)

# def moviesdetails(request,id):
#     data ={
#         "id": id
#     }
#     return render(request,"details.html",data)

###########################################################

def home(request):
    data ={
        "categories": Category.objects.all(),
        "movies": Movie.objects.filter(homepage=True)
    }
    return render(request,"index.html",data)

def movies(request):
    data ={
        "categories": Category.objects.all(),
        "movies": Movie.objects.all()
    }
    return render(request,"movies.html",data)

def moviesdetails(request,id):
    data ={
        "movie":Movie.objects.get(id=id)
    }
    return render(request,"details.html",data)

