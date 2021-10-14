from django.http import HttpResponse
from django.shortcuts import render, redirect
import random

# Create your views here.
from Blog.models import Blog


def hello_world_view(request):

    return HttpResponse('<h1> Hello World!!!<h1/>')

def random_view(request):
    r=random.randint(0,100)
    return HttpResponse(str(r))

def test_form(request):
    if request.method == "POST":

        data = request.POST
        first_name = data["first_name"]
        last_name = data["last_name"]
        return HttpResponse(f"ваше имя {first_name} ваша фамилиия {last_name}")
    elif request.method == "GET":
        return render(request, "form.html")
def Blog_view(request):
    blog = Blog.objects.all()
    data= {
        'title' : 'Main page',
        'list':[1,2,3,4,5],
        'blog_list':blog,


    }

    return render ( request, 'blog.html', context=data )

